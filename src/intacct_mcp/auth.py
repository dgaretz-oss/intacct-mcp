"""Authentication for the Sage Intacct REST API.

Token priority (highest first):

1. **Authorization Code tokens** (``~/.intacct_mcp_tokens.json``) — produced by
   ``intacct-mcp login``.  The access token is refreshed automatically
   using the stored refresh token and saved back to disk.

2. **Client Credentials** — used when no token file exists and both
   ``INTACCT_CLIENT_ID`` + ``INTACCT_CLIENT_SECRET`` are present.  This is the
   machine-to-machine fallback; it never involves a user login.

The active access token is cached in memory and reused until it is within
60 seconds of expiry, at which point a fresh one is fetched transparently.

Token values are never logged or returned to callers.
"""

from __future__ import annotations

import asyncio
import base64
import binascii
import json
import logging
import os
import pathlib
import time

import httpx

logger = logging.getLogger("intacct-mcp.auth")

DEFAULT_BASE_URL = "https://api.intacct.com/ia/api/v1"

# Re-fetch this many seconds *before* the token actually expires.
_EXPIRY_SKEW_SECONDS = 60

# Fallback lifetime (seconds) when neither ``expires_in`` nor a JWT ``exp``
# claim is available in the token response.
_FALLBACK_LIFETIME_SECONDS = 300


class IntacctAuthError(RuntimeError):
    """Raised when a token cannot be obtained (missing config or token failure)."""


# ---------------------------------------------------------------------------
# JWT helpers
# ---------------------------------------------------------------------------

def _decode_jwt_exp(token: str) -> float | None:
    """Return the ``exp`` claim (Unix seconds) from a JWT, or None if unreadable.

    The token is trusted (came directly from Intacct over HTTPS), so the
    signature is not verified here — we only read the payload to learn expiry.
    """
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return None
        payload_b64 = parts[1]
        padding = "=" * (-len(payload_b64) % 4)
        payload_bytes = base64.urlsafe_b64decode(payload_b64 + padding)
        payload = json.loads(payload_bytes)
        exp = payload.get("exp")
        return float(exp) if exp is not None else None
    except (ValueError, binascii.Error, json.JSONDecodeError, TypeError):
        return None


def _compute_expiry(token: str, token_response: dict) -> float:
    """Decide when a token expires (absolute Unix seconds).

    Prefers the JWT ``exp`` claim, then ``expires_in``, then a short default.
    """
    exp = _decode_jwt_exp(token)
    if exp is not None:
        return exp

    expires_in = token_response.get("expires_in")
    if expires_in is not None:
        try:
            return time.time() + float(expires_in)
        except (TypeError, ValueError):
            pass

    logger.warning(
        "Token response had no JWT exp or expires_in; using %ss fallback lifetime",
        _FALLBACK_LIFETIME_SECONDS,
    )
    return time.time() + _FALLBACK_LIFETIME_SECONDS


# ---------------------------------------------------------------------------
# Configuration helpers
# ---------------------------------------------------------------------------

def _base_url() -> str:
    return os.getenv("INTACCT_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


# Where login.py saves OAuth2 authorization-code tokens.
TOKENS_PATH = pathlib.Path.home() / ".intacct_mcp_tokens.json"


def _load_disk_tokens() -> dict | None:
    """Return the stored token dict from disk, or None."""
    if not TOKENS_PATH.exists():
        return None
    try:
        return json.loads(TOKENS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning("Could not read token file %s: %s", TOKENS_PATH, exc)
        return None


def _save_disk_tokens(tokens: dict) -> None:
    """Persist a refreshed token dict to disk."""
    try:
        TOKENS_PATH.write_text(json.dumps(tokens, indent=2), encoding="utf-8")
        try:
            TOKENS_PATH.chmod(0o600)
        except NotImplementedError:
            pass
    except OSError as exc:
        logger.warning("Could not save refreshed tokens to %s: %s", TOKENS_PATH, exc)


# ---------------------------------------------------------------------------
# Token fetching
# ---------------------------------------------------------------------------

async def _refresh_access_token(refresh_token: str, disk_tokens: dict) -> tuple[str, float]:
    """Exchange a refresh token for a new access token.

    Updates and re-saves the on-disk token file with the new values.
    Returns (access_token, absolute_expiry).
    """
    client_id = os.getenv("INTACCT_CLIENT_ID")
    if not client_id:
        raise IntacctAuthError(
            "INTACCT_CLIENT_ID not set — cannot refresh token. "
            "Run 'intacct-mcp login' after setting it in .env."
        )

    token_url = f"{_base_url()}/oauth2/token"
    data: dict[str, str] = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
    }
    client_secret = os.getenv("INTACCT_CLIENT_SECRET")
    if client_secret:
        data["client_secret"] = client_secret

    logger.info("Refreshing access token via refresh_token grant")
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(
                token_url,
                data=data,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "application/json",
                },
            )
    except httpx.HTTPError as exc:
        raise IntacctAuthError(f"Token refresh request failed: {exc}") from exc

    if resp.status_code != 200:
        detail = _safe_error_detail(resp)
        raise IntacctAuthError(
            f"Token refresh failed (HTTP {resp.status_code}): {detail}. "
            "Run 'intacct-mcp login' to re-authenticate."
        )

    try:
        new_tokens = resp.json()
    except ValueError as exc:
        raise IntacctAuthError("Refresh endpoint returned non-JSON response.") from exc

    access_token = new_tokens.get("access_token")
    if not access_token:
        raise IntacctAuthError("Refresh response did not contain an 'access_token'.")

    expires_at = _compute_expiry(access_token, new_tokens)

    # Merge: keep the existing refresh_token if the response doesn't include a new one
    # (some providers rotate it, others don't).
    updated = {**disk_tokens, **new_tokens, "issued_at": time.time()}
    if "refresh_token" not in new_tokens and "refresh_token" in disk_tokens:
        updated["refresh_token"] = disk_tokens["refresh_token"]

    _save_disk_tokens(updated)
    logger.info("Access token refreshed (expires in ~%ss)", max(0, int(expires_at - time.time())))
    return access_token, expires_at


async def _fetch_client_credentials_token() -> tuple[str, float]:
    """POST the Client Credentials grant and return (token, absolute_expiry).

    Intacct's client_credentials grant is non-standard: it requires either a
    ``username`` or ``session_id`` parameter to associate the token with a
    specific Intacct user context. Set ``INTACCT_USERNAME`` in .env.
    """
    client_id = os.getenv("INTACCT_CLIENT_ID")
    client_secret = os.getenv("INTACCT_CLIENT_SECRET")
    username = os.getenv("INTACCT_USERNAME")

    missing = [
        name
        for name, value in (
            ("INTACCT_CLIENT_ID", client_id),
            ("INTACCT_CLIENT_SECRET", client_secret),
            ("INTACCT_USERNAME", username),
        )
        if not value
    ]
    if missing:
        raise IntacctAuthError(
            "No saved login tokens found and no client credentials available. "
            "Either run 'intacct-mcp login' to authenticate via browser, "
            "or set INTACCT_CLIENT_ID + INTACCT_CLIENT_SECRET + INTACCT_USERNAME "
            "in your .env for the Client Credentials grant. "
            f"(Missing: {', '.join(missing)})"
        )

    token_url = f"{_base_url()}/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
    }

    logger.info("Requesting Client Credentials token from %s/oauth2/token", _base_url())
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(
                token_url,
                data=data,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "application/json",
                },
            )
    except httpx.HTTPError as exc:
        raise IntacctAuthError(f"Failed to reach Intacct token endpoint: {exc}") from exc

    if resp.status_code != 200:
        detail = _safe_error_detail(resp)
        raise IntacctAuthError(
            f"Client Credentials token request failed (HTTP {resp.status_code}): {detail}. "
            "Verify INTACCT_CLIENT_ID / INTACCT_CLIENT_SECRET and that the client "
            "is authorized in Intacct."
        )

    try:
        token_response = resp.json()
    except ValueError as exc:
        raise IntacctAuthError("Token endpoint returned a non-JSON response.") from exc

    token = token_response.get("access_token")
    if not token:
        raise IntacctAuthError("Token response did not contain an 'access_token'.")

    expires_at = _compute_expiry(token, token_response)
    logger.info(
        "Client Credentials token obtained (expires in ~%ss)",
        max(0, int(expires_at - time.time())),
    )
    return token, expires_at


# ---------------------------------------------------------------------------
# In-memory token cache
# ---------------------------------------------------------------------------

class _TokenCache:
    """In-memory cache for an access token.

    On cache miss, tries (in order):
      1. Disk tokens from ~/.intacct_mcp_tokens.json  (auth-code flow)
         - If valid, uses the access token directly.
         - If expired but a refresh token is present, refreshes automatically.
      2. Client Credentials grant (machine-to-machine fallback).

    Access is serialized with an asyncio lock to prevent concurrent fetches.
    """

    def __init__(self) -> None:
        self._token: str | None = None
        self._expires_at: float = 0.0
        self._lock = asyncio.Lock()

    def _is_valid(self) -> bool:
        return bool(self._token) and time.time() < (self._expires_at - _EXPIRY_SKEW_SECONDS)

    async def get_token(self) -> str:
        """Return a valid access token, fetching/refreshing as needed."""
        if self._is_valid():
            return self._token  # type: ignore[return-value]

        async with self._lock:
            if self._is_valid():
                return self._token  # type: ignore[return-value]

            token, expires_at = await self._acquire_token()
            self._token = token
            self._expires_at = expires_at
            return token

    async def _acquire_token(self) -> tuple[str, float]:
        """Try disk tokens first, then client credentials."""
        disk = _load_disk_tokens()

        if disk:
            access_token = disk.get("access_token")
            if access_token:
                # Compute expiry from what's on disk.
                issued_at: float = disk.get("issued_at", 0.0)
                expires_in = disk.get("expires_in")
                if expires_in:
                    disk_expires_at = issued_at + float(expires_in)
                else:
                    disk_expires_at = _decode_jwt_exp(access_token) or (issued_at + _FALLBACK_LIFETIME_SECONDS)

                if time.time() < disk_expires_at - _EXPIRY_SKEW_SECONDS:
                    logger.info("Using valid access token from disk (%s)", TOKENS_PATH)
                    return access_token, disk_expires_at

            # Access token expired — try refresh.
            refresh_token = disk.get("refresh_token")
            if refresh_token:
                logger.info("Access token expired; refreshing via refresh_token")
                try:
                    return await _refresh_access_token(refresh_token, disk)
                except IntacctAuthError as exc:
                    logger.warning("Refresh token failed (%s); falling back to client credentials", exc)
            else:
                logger.info(
                    "Disk token file found but access token expired and no refresh_token present. "
                    "Run 'intacct-mcp login' to re-authenticate."
                )

        # Fall back to client credentials (server-to-server).
        return await _fetch_client_credentials_token()

    def invalidate(self) -> None:
        """Force the next call to re-fetch (e.g. after a 401 response)."""
        self._token = None
        self._expires_at = 0.0

    def status(self) -> dict:
        """Diagnostics about the cached token (never exposes the token value)."""
        now = time.time()
        disk = _load_disk_tokens()
        return {
            "token_cached": bool(self._token),
            "expires_in_seconds": max(0, int(self._expires_at - now)) if self._token else 0,
            "is_valid": self._is_valid(),
            "disk_tokens_present": bool(disk),
            "disk_has_refresh_token": bool(disk and disk.get("refresh_token")),
            "tokens_path": str(TOKENS_PATH),
        }


_cache = _TokenCache()


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

async def get_auth_headers() -> dict:
    """Return the Authorization header carrying a valid bearer token."""
    token = await _cache.get_token()
    return {"Authorization": f"Bearer {token}"}


def get_credentials_status() -> dict:
    """Report auth configuration without exposing any credential values."""
    return {
        "client_id_loaded": bool(os.getenv("INTACCT_CLIENT_ID")),
        "client_secret_loaded": bool(os.getenv("INTACCT_CLIENT_SECRET")),
        "base_url": _base_url(),
        "token": _cache.status(),
    }


def _safe_error_detail(resp: httpx.Response) -> str:
    """Extract a short, secret-free error description from a token error response."""
    try:
        body = resp.json()
    except ValueError:
        return resp.text[:200] if resp.text else "(empty body)"
    parts = [str(body.get(k)) for k in ("error", "error_description") if body.get(k)]
    return " - ".join(parts) if parts else json.dumps(body)[:200]
