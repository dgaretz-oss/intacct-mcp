"""XML Gateway fallback for the Sage Intacct legacy XML API.

When to use this module
-----------------------
The XML gateway is a **fallback** for the small set of operations that the
REST v1 API does not yet cover. It is NOT a default error handler — most REST
errors are caused by bad schema, missing fields, or wrong request shape, NOT
by a true REST limitation. Switch to XML only when there is good evidence
that the operation cannot be done via REST.

Authentication
--------------
The XML gateway accepts a session ID in place of a user login. The session ID
is obtained by exchanging the existing OAuth bearer token at the REST endpoint
``GET services/core/session/id``. So no NEW user credentials are needed.

The legacy XML gateway envelope still requires a registered ``senderid`` and
``password`` in the ``<control>`` block (outer firewall validation). Those are
read from the optional environment variables ``INTACCT_SENDER_ID`` and
``INTACCT_SENDER_PASSWORD``. Without them, the XML fallback tool cannot be
used — but normal REST operation continues to work.
"""

from __future__ import annotations

import asyncio
import logging
import os
import re
import time
import uuid
import xml.etree.ElementTree as ET
from typing import Any

import httpx

from intacct_mcp import auth

logger = logging.getLogger("intacct-mcp.xml")

# Default production XML gateway endpoint. Can be overridden via env in case
# the deployment lives in a different region.
DEFAULT_XML_GATEWAY_URL = "https://api.intacct.com/ia/xml/xmlgw.phtml"

# XML session IDs from /services/core/session/id are valid for 21,600 seconds.
# Refresh 60 seconds before expiry to avoid edge-of-expiry failures.
_SESSION_EXPIRY_SKEW_SECONDS = 60


class XmlGatewayConfigError(RuntimeError):
    """Raised when the XML gateway is invoked without required configuration."""


class XmlGatewayError(RuntimeError):
    """Raised when the XML gateway returns a failure status."""

    def __init__(self, message: str, raw_response: str = "") -> None:
        super().__init__(message)
        self.raw_response = raw_response


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

def _sender_id() -> str | None:
    return os.getenv("INTACCT_SENDER_ID") or None


def _sender_password() -> str | None:
    return os.getenv("INTACCT_SENDER_PASSWORD") or None


def _xml_gateway_url() -> str:
    return os.getenv("INTACCT_XML_GATEWAY_URL", DEFAULT_XML_GATEWAY_URL)


def _rest_base_url() -> str:
    return os.getenv("INTACCT_BASE_URL", "https://api.intacct.com/ia/api/v1").rstrip("/")


def is_configured() -> bool:
    """Return True if both XML sender env vars are present."""
    return bool(_sender_id() and _sender_password())


def config_status() -> dict:
    """Report XML fallback configuration without exposing secret values."""
    return {
        "sender_id_loaded": bool(_sender_id()),
        "sender_password_loaded": bool(_sender_password()),
        "xml_gateway_url": _xml_gateway_url(),
        "ready": is_configured(),
    }


def assert_configured() -> None:
    """Raise XmlGatewayConfigError if env is missing."""
    missing = []
    if not _sender_id():
        missing.append("INTACCT_SENDER_ID")
    if not _sender_password():
        missing.append("INTACCT_SENDER_PASSWORD")
    if missing:
        raise XmlGatewayConfigError(
            "XML fallback is not configured. Missing environment variable(s): "
            + ", ".join(missing)
            + ".\nAdd them to your .env file. These are ONLY required for the XML "
            "fallback — normal REST operation does not need them. "
            "Obtain a Web Services sender ID from your Intacct administrator "
            "(Company > Setup > Web Services Sender IDs)."
        )


# ---------------------------------------------------------------------------
# Session ID exchange (OAuth bearer -> XML session ID)
# ---------------------------------------------------------------------------

class _SessionCache:
    """In-memory cache for the XML session ID obtained via the REST bridge.

    The session ID is valid for 21,600 seconds. We refresh slightly before
    expiry to avoid a thundering herd at the cusp.
    """

    def __init__(self) -> None:
        self._session_id: str | None = None
        self._expires_at: float = 0.0
        self._endpoint_url: str | None = None
        self._lock = asyncio.Lock()

    def _is_valid(self) -> bool:
        return bool(self._session_id) and time.time() < (
            self._expires_at - _SESSION_EXPIRY_SKEW_SECONDS
        )

    async def get(self) -> tuple[str, str]:
        """Return (session_id, endpoint_url), fetching if needed."""
        if self._is_valid():
            return self._session_id, self._endpoint_url or _xml_gateway_url()  # type: ignore[return-value]

        async with self._lock:
            if self._is_valid():
                return self._session_id, self._endpoint_url or _xml_gateway_url()  # type: ignore[return-value]
            await self._fetch()
            return self._session_id, self._endpoint_url or _xml_gateway_url()  # type: ignore[return-value]

    async def _fetch(self) -> None:
        headers = await auth.get_auth_headers()
        headers["Accept"] = "application/json"

        url = f"{_rest_base_url()}/services/core/session/id"
        logger.info("Exchanging OAuth bearer for XML session ID")

        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.get(url, headers=headers)

        if resp.status_code != 200:
            raise XmlGatewayError(
                f"Failed to obtain XML session ID (HTTP {resp.status_code}): "
                f"{(resp.text or '')[:300]}"
            )

        try:
            body = resp.json()
        except ValueError as exc:
            raise XmlGatewayError(
                "session/id endpoint returned non-JSON response"
            ) from exc

        # Response shape can be either:
        #   {"ia::result": {"sessionId": "...", "expiresIn": 21600}}
        # or the flatter:
        #   {"sessionId": "...", "endpointUrl": "..."}
        result = body.get("ia::result") if isinstance(body, dict) else None
        payload = result if isinstance(result, dict) else body
        if not isinstance(payload, dict):
            raise XmlGatewayError(f"Unexpected session/id response shape: {body}")

        session_id = payload.get("sessionId") or payload.get("sessionid")
        endpoint_url = payload.get("endpointUrl") or payload.get("endpointURL")
        expires_in = payload.get("expiresIn") or payload.get("expiresin") or 21600

        if not session_id:
            raise XmlGatewayError(f"session/id response missing sessionId: {body}")

        self._session_id = str(session_id)
        self._endpoint_url = str(endpoint_url) if endpoint_url else _xml_gateway_url()
        try:
            self._expires_at = time.time() + float(expires_in)
        except (TypeError, ValueError):
            self._expires_at = time.time() + 21600
        logger.info(
            "XML session ID obtained (expires in ~%ss)",
            max(0, int(self._expires_at - time.time())),
        )

    def invalidate(self) -> None:
        self._session_id = None
        self._expires_at = 0.0


_session_cache = _SessionCache()


# ---------------------------------------------------------------------------
# Envelope construction and posting
# ---------------------------------------------------------------------------

# Match a leading "<function ...>" so we can detect whether the caller already
# wrapped their body in a <function> element. If they did, we use it as-is; if
# they did not, we wrap it with a controlid.
_FUNCTION_TAG_RE = re.compile(r"^\s*<function\b", re.IGNORECASE)


def _xml_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def _wrap_function(function_xml: str, control_id: str) -> str:
    """Wrap raw XML in a <function controlid="..."> element if not already wrapped."""
    if _FUNCTION_TAG_RE.match(function_xml):
        return function_xml
    return f'<function controlid="{_xml_escape(control_id)}">{function_xml}</function>'


def build_envelope(
    function_xml: str,
    session_id: str,
    sender_id: str,
    sender_password: str,
    control_id: str,
    transaction: bool = False,
) -> str:
    """Build a complete <request> envelope for posting to the XML gateway."""
    transaction_attr = ' transaction="true"' if transaction else ""
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<request>\n"
        "  <control>\n"
        f"    <senderid>{_xml_escape(sender_id)}</senderid>\n"
        f"    <password>{_xml_escape(sender_password)}</password>\n"
        f"    <controlid>{_xml_escape(control_id)}</controlid>\n"
        "    <uniqueid>false</uniqueid>\n"
        "    <dtdversion>3.0</dtdversion>\n"
        "    <includewhitespace>false</includewhitespace>\n"
        "  </control>\n"
        f"  <operation{transaction_attr}>\n"
        "    <authentication>\n"
        f"      <sessionid>{_xml_escape(session_id)}</sessionid>\n"
        "    </authentication>\n"
        "    <content>\n"
        f"      {_wrap_function(function_xml, control_id)}\n"
        "    </content>\n"
        "  </operation>\n"
        "</request>\n"
    )


# ---------------------------------------------------------------------------
# Response parsing
# ---------------------------------------------------------------------------

def _element_to_dict(element: ET.Element) -> Any:
    """Convert an XML element subtree to a JSON-compatible dict/str/None."""
    result: dict[str, Any] = {}
    if element.attrib:
        result.update(element.attrib)

    for child in element:
        child_value = _element_to_dict(child)
        if child.tag in result:
            existing = result[child.tag]
            if isinstance(existing, list):
                existing.append(child_value)
            else:
                result[child.tag] = [existing, child_value]
        else:
            result[child.tag] = child_value

    if not result:
        if element.text and element.text.strip():
            return element.text.strip()
        return None
    return result


def parse_response(xml_text: str) -> dict:
    """Parse the gateway response XML into a dict."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise XmlGatewayError(
            f"Failed to parse XML gateway response: {exc}",
            raw_response=xml_text[:1000],
        ) from exc
    parsed = _element_to_dict(root)
    if not isinstance(parsed, dict):
        return {"value": parsed}
    return parsed


def check_status(parsed: dict) -> dict:
    """Inspect parsed gateway response for control/operation/function failures.

    Returns ``{"success": True}`` on success or a dict with details on failure.
    """
    control = parsed.get("control")
    if isinstance(control, dict) and control.get("status") not in (None, "success"):
        return {
            "success": False,
            "level": "control",
            "description": _str_or_default(
                control.get("description"), "Control-level failure (sender auth/envelope)"
            ),
            "errorno": control.get("errormessage", {}).get("errorno")
            if isinstance(control.get("errormessage"), dict)
            else None,
        }

    operation = parsed.get("operation")
    if not isinstance(operation, dict):
        return {"success": True}

    if operation.get("status") == "failure":
        return {
            "success": False,
            "level": "operation",
            "description": _str_or_default(
                operation.get("description"), "Operation-level failure"
            ),
        }

    auth_block = operation.get("authentication")
    if isinstance(auth_block, dict) and auth_block.get("status") not in (None, "success"):
        return {
            "success": False,
            "level": "authentication",
            "description": _str_or_default(
                auth_block.get("description"),
                "Authentication failure (session ID rejected)",
            ),
        }

    # Function-level results
    result_block = operation.get("result")
    if result_block is None:
        return {"success": True}
    results = result_block if isinstance(result_block, list) else [result_block]
    failures = []
    for idx, item in enumerate(results):
        if not isinstance(item, dict):
            continue
        if item.get("status") not in (None, "success"):
            failures.append(
                {
                    "index": idx,
                    "function": item.get("function"),
                    "controlid": item.get("controlid"),
                    "description": _str_or_default(
                        item.get("description"), "Function failed"
                    ),
                    "errormessage": item.get("errormessage"),
                }
            )
    if failures:
        return {
            "success": False,
            "level": "function",
            "description": failures[0]["description"],
            "failures": failures,
        }
    return {"success": True}


def _str_or_default(value: Any, default: str) -> str:
    if isinstance(value, str) and value:
        return value
    if isinstance(value, dict):
        return str(value)
    return default


# ---------------------------------------------------------------------------
# Public coroutines
# ---------------------------------------------------------------------------

async def post_xml(
    function_xml: str,
    control_id: str | None = None,
    transaction: bool = False,
    parse: bool = True,
) -> dict:
    """Build envelope, fetch a session, and POST raw XML to the gateway."""
    assert_configured()

    sender_id = _sender_id()
    sender_password = _sender_password()
    assert sender_id and sender_password  # for type checker; assert_configured guards

    control_id = control_id or f"mcp_{uuid.uuid4().hex[:12]}"

    session_id, endpoint_url = await _session_cache.get()
    envelope = build_envelope(
        function_xml=function_xml,
        session_id=session_id,
        sender_id=sender_id,
        sender_password=sender_password,
        control_id=control_id,
        transaction=transaction,
    )

    logger.info("POST XML gateway %s controlid=%s", endpoint_url, control_id)
    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post(
            endpoint_url,
            content=envelope.encode("utf-8"),
            headers={
                "Content-Type": "application/xml",
                "Accept": "application/xml",
            },
        )

    raw_text = resp.text or ""

    if resp.status_code >= 500:
        raise XmlGatewayError(
            f"XML gateway returned HTTP {resp.status_code}: {raw_text[:300]}",
            raw_response=raw_text,
        )

    parsed = parse_response(raw_text)
    status = check_status(parsed)

    if not status["success"]:
        # Authentication failure may just mean the session expired between cache
        # check and post; invalidate and let caller retry.
        if status.get("level") == "authentication":
            _session_cache.invalidate()
        if parse:
            return {
                "status": "error",
                "level": status.get("level"),
                "description": status.get("description"),
                "failures": status.get("failures"),
                "parsed_response": parsed,
                "raw_response": raw_text,
            }
        return {
            "status": "error",
            "level": status.get("level"),
            "description": status.get("description"),
            "raw_response": raw_text,
        }

    if parse:
        return {"status": "success", "parsed_response": parsed}
    return {"status": "success", "xml_response": raw_text}


def invalidate_session() -> None:
    """Drop the cached XML session ID. Next call will re-fetch."""
    _session_cache.invalidate()
