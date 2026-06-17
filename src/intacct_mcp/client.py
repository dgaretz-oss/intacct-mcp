"""Shared async HTTP client for the Sage Intacct REST API.

``IntacctClient`` wraps a singleton ``httpx.AsyncClient``, injects a fresh
Client Credentials bearer token on every request, raises ``IntacctError`` on
non-2xx responses, and passes 207 Multi-Status responses through as data so the
caller can inspect per-operation results of a bulk request.
"""

from __future__ import annotations

import logging
import os
import pathlib
import sys

import httpx

from intacct_mcp import auth

# --- Logging --------------------------------------------------------------
# Log to logs/intacct_mcp.log under the project root (three levels up from
# this file: src/intacct_mcp/client.py -> project root). Distinct filename from
# the XML server's intacct_mcp.log. Never logs token values or response bodies.
_PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
_LOG_DIR = _PROJECT_ROOT / "logs"
_LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("intacct-mcp")
if not logger.handlers:
    logger.setLevel(logging.INFO)
    _formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    _file_handler = logging.FileHandler(_LOG_DIR / "intacct_mcp.log")
    _file_handler.setFormatter(_formatter)
    logger.addHandler(_file_handler)
    _stream_handler = logging.StreamHandler(sys.stderr)
    _stream_handler.setFormatter(_formatter)
    logger.addHandler(_stream_handler)

DEFAULT_BASE_URL = "https://api.intacct.com/ia/api/v1"

# 207 Multi-Status is returned by bulk requests when some operations succeed and
# others fail. It is data, not an error - the caller inspects per-op statuses.
_MULTI_STATUS = 207


class IntacctError(RuntimeError):
    """Raised on a non-2xx (and non-207) response from the Intacct REST API.

    Carries the HTTP status, the request method/path, and the Intacct error
    description and correction hint when present in the response body.
    """

    def __init__(
        self,
        status_code: int,
        method: str,
        path: str,
        description: str,
        correction: str = "",
    ) -> None:
        self.status_code = status_code
        self.method = method
        self.path = path
        self.description = description
        self.correction = correction

        message = f"IntacctError [{status_code}] {method} {path}:\n  ia::error: {description}"
        if correction:
            message += f"\n  Correction: {correction}"
        super().__init__(message)


def _base_url() -> str:
    return os.getenv("INTACCT_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


def _extract_error(body: object) -> tuple[str, str]:
    """Pull (message, correction) from an Intacct REST error response.

    Standard REST shape has ia::error at the top level:
        {"ia::error": {"code": "...", "message": "...", "supportId": "...", "details": [...]}}

    Also handles ia::error nested under ia::result and legacy list shapes.
    Appends supportId and details to the message for easier debugging.
    """
    if isinstance(body, dict):
        # Standard REST shape: ia::error at top level (or nested under ia::result)
        error_obj: object = body.get("ia::error")
        if error_obj is None:
            result = body.get("ia::result")
            if isinstance(result, dict):
                error_obj = result.get("ia::error")

        if isinstance(error_obj, dict):
            msg = str(error_obj.get("message") or error_obj.get("description") or "Unknown error")
            correction = str(error_obj.get("correction") or "")
            code = str(error_obj.get("code") or error_obj.get("errorId") or "")
            support_id = error_obj.get("supportId") or ""
            details = error_obj.get("details")

            full_msg = f"[{code}] {msg}" if code else msg
            if support_id:
                full_msg += f" (supportId: {support_id})"
            if details:
                if isinstance(details, list):
                    detail_strs = [
                        f"[{d.get('code','')}] {d.get('message','')}" if isinstance(d, dict) else str(d)
                        for d in details[:5]
                    ]
                    full_msg += " | details: " + "; ".join(detail_strs)
                elif isinstance(details, dict):
                    full_msg += f" | details: {details}"
            return full_msg, correction

        if isinstance(error_obj, list) and error_obj:
            first = error_obj[0]
            if isinstance(first, dict):
                return (
                    str(first.get("description") or "Unknown error"),
                    str(first.get("correction") or ""),
                )

        # OAuth-style error at top level
        if "error" in body:
            return str(body["error"]), str(body.get("error_description") or "")

    if isinstance(body, str) and body:
        return body[:300], ""
    return "Unknown error (no error detail in response body)", ""


class IntacctClient:
    """Singleton-friendly async client for the Intacct REST API."""

    def __init__(self) -> None:
        # Trailing slash is required so httpx appends relative paths correctly.
        # Without it, RFC 3986 resolution of an absolute path (starting with /)
        # replaces the entire path, stripping /ia/api/v1 from the URL.
        base = _base_url().rstrip("/") + "/"
        self._client = httpx.AsyncClient(base_url=base, timeout=60.0)

    async def request(
        self,
        method: str,
        path: str,
        params: dict | None = None,
        body: dict | None = None,
        extra_headers: dict | None = None,
        multipart: dict | None = None,
    ) -> dict:
        """Execute a REST request and return the parsed JSON response.

        Args:
            method:        HTTP method - GET, POST, PATCH, or DELETE.
            path:          API path relative to the base URL (leading slash optional).
            params:        Optional query string parameters.
            body:          Optional request body (sent as JSON for POST/PATCH/DELETE).
            extra_headers: Optional additional headers merged on top of auth headers
                           (e.g. {"Prefer": "respond-async"},
                           {"X-IA-API-ParamTransaction": "true"},
                           {"Idempotency-Key": "abc123"}).
            multipart:     Optional multipart form fields dict. When provided,
                           body is ignored and Content-Type is set by httpx.
                           Values may be strings or (filename, bytes, mime_type)
                           tuples for file fields.

        Returns:
            The parsed JSON response. 2xx and 207 Multi-Status both return data.

        Raises:
            IntacctError: On any non-2xx, non-207 response.
        """
        method = method.upper()
        # Strip leading slash -- base_url has a trailing slash, so paths must be
        # relative to append correctly rather than replacing the full URL path.
        path = path.lstrip("/")

        headers = await auth.get_auth_headers()
        headers["Accept"] = "application/json"
        if method in ("POST", "PATCH") and multipart is None:
            headers["Content-Type"] = "application/json"
        if extra_headers:
            headers.update(extra_headers)

        logger.info("%s %s", method, path)

        try:
            if multipart is not None:
                resp = await self._client.request(
                    method,
                    path,
                    params=params or None,
                    files=multipart,
                    headers=headers,
                )
            else:
                resp = await self._client.request(
                    method,
                    path,
                    params=params or None,
                    json=body if body else None,
                    headers=headers,
                )
        except httpx.HTTPError as exc:
            logger.warning("Transport error on %s %s: %s", method, path, exc)
            raise IntacctError(
                0, method, path, f"Network error: {exc}",
                "Check connectivity and INTACCT_BASE_URL.",
            ) from exc

        # 207 Multi-Status: partial bulk result - return as data, do not raise.
        if resp.status_code == _MULTI_STATUS:
            logger.info("207 Multi-Status on %s %s (partial bulk result)", method, path)
            return _parse_json(resp)

        if not (200 <= resp.status_code < 300):
            body_obj = _safe_json(resp)
            description, correction = _extract_error(body_obj)
            # Log raw body so 400s with no ia::error structure are diagnosable.
            raw_preview = (resp.text or "")[:500]
            logger.warning(
                "HTTP %s on %s %s: %s | raw body: %s",
                resp.status_code, method, path, description, raw_preview,
            )
            raise IntacctError(
                resp.status_code, method, path, description, correction
            )

        return _parse_json(resp)

    async def aclose(self) -> None:
        await self._client.aclose()


def _parse_json(resp: httpx.Response) -> dict:
    """Parse a successful response body as JSON, tolerating empty bodies."""
    if not resp.content:
        return {}
    try:
        return resp.json()
    except ValueError:
        return {"raw": resp.text}


def _safe_json(resp: httpx.Response) -> object:
    """Parse an error response body as JSON, falling back to raw text."""
    try:
        return resp.json()
    except ValueError:
        return resp.text


_client_instance: IntacctClient | None = None


def get_client() -> IntacctClient:
    """Return the process-wide singleton ``IntacctClient``, creating it lazily."""
    global _client_instance
    if _client_instance is None:
        _client_instance = IntacctClient()
    return _client_instance
