"""Browser-based OAuth 2.0 Authorization Code + PKCE login flow.

Usage:
    intacct-mcp login [--port PORT]

Flow
----
1. Generates a PKCE challenge + random state nonce.
2. Opens the Sage Intacct authorization URL in the user's browser.
3. User logs in and grants access.
4. Intacct redirects to the registered redirect URI with ``?code=...``.
5. The user copies the ``code`` value from the browser address bar and
   pastes it into the terminal prompt.
6. The code is exchanged for access + refresh tokens, which are saved to
   ``~/.intacct_mcp_tokens.json`` for the MCP server to use.

Why no localhost callback server?
----------------------------------
Sage Intacct requires HTTPS for all redirect URIs (including loopback), so
``http://127.0.0.1`` cannot be registered.  The copy-paste approach works with
any HTTPS redirect URI — the code appears in the address bar as a query
parameter even if the destination page returns a 404.

Required setup
--------------
1. Set ``INTACCT_CLIENT_ID`` in your ``.env``.
2. In your Intacct OAuth application settings, register your redirect URI.
   Set ``INTACCT_REDIRECT_URI`` in ``.env`` to the same value
   (default: ``https://localhost/callback`` — update to match what you
   registered).
"""

from __future__ import annotations

import base64
import hashlib
import json
import logging
import os
import pathlib
import secrets
import time
import urllib.parse
import webbrowser

import httpx
from dotenv import find_dotenv, load_dotenv

logger = logging.getLogger("intacct-mcp.login")

# Where tokens are persisted between MCP server restarts.
TOKENS_PATH = pathlib.Path.home() / ".intacct_mcp_tokens.json"

# Locate .env by searching upward from CWD (portable across devices), with
# a fallback to the path relative to this file.
_DOTENV_PATH = find_dotenv(usecwd=True) or str(
    pathlib.Path(__file__).resolve().parent.parent.parent / ".env"
)

# Default redirect URI — update INTACCT_REDIRECT_URI in .env to match what
# you registered in Intacct.  Any HTTPS URI works; the code will appear in
# the address bar after redirect even if the page itself returns a 404.
DEFAULT_REDIRECT_URI = "https://localhost/callback"


# ---------------------------------------------------------------------------
# PKCE helpers
# ---------------------------------------------------------------------------

def _pkce_pair() -> tuple[str, str]:
    """Return (code_verifier, code_challenge) using S256.

    Verifier: 64 random bytes → 86-char base64url string (within the
    43–128 char range required by RFC 7636).
    Challenge: SHA-256(verifier), base64url-encoded without padding.
    """
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(64)).rstrip(b"=").decode("ascii")
    digest = hashlib.sha256(verifier.encode("ascii")).digest()
    challenge = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return verifier, challenge


# ---------------------------------------------------------------------------
# Token storage
# ---------------------------------------------------------------------------

def save_tokens(tokens: dict) -> None:
    """Write tokens to disk, readable only by the current user."""
    TOKENS_PATH.parent.mkdir(parents=True, exist_ok=True)
    TOKENS_PATH.write_text(json.dumps(tokens, indent=2), encoding="utf-8")
    try:
        TOKENS_PATH.chmod(0o600)
    except NotImplementedError:
        pass  # Windows handles file permissions differently
    print(f"  Tokens saved to {TOKENS_PATH}")


def load_tokens() -> dict | None:
    """Return the stored token dict, or None if the file doesn't exist."""
    if not TOKENS_PATH.exists():
        return None
    try:
        return json.loads(TOKENS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


# ---------------------------------------------------------------------------
# Token exchange
# ---------------------------------------------------------------------------

def _base_url() -> str:
    from intacct_mcp.auth import DEFAULT_BASE_URL
    return os.getenv("INTACCT_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


def _exchange_code(code: str, verifier: str, redirect_uri: str) -> dict:
    """POST authorization code + PKCE verifier → token response dict."""
    client_id = os.getenv("INTACCT_CLIENT_ID")
    if not client_id:
        raise RuntimeError("INTACCT_CLIENT_ID is not set. Add it to your .env file.")

    token_url = f"{_base_url()}/oauth2/token"
    data: dict[str, str] = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "code_verifier": verifier,
    }

    # Include client_secret only for confidential clients.
    client_secret = os.getenv("INTACCT_CLIENT_SECRET")
    if client_secret:
        data["client_secret"] = client_secret

    resp = httpx.post(
        token_url,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        },
        timeout=30.0,
    )
    if resp.status_code != 200:
        raise RuntimeError(
            f"Token exchange failed (HTTP {resp.status_code}): {resp.text[:400]}"
        )
    return resp.json()


# ---------------------------------------------------------------------------
# Main flow
# ---------------------------------------------------------------------------

def run_login_flow() -> None:
    """Interactive OAuth 2.0 Authorization Code + PKCE login.

    Opens the Intacct login page in the browser, then prompts the user to
    paste the authorization code from the redirect URL.
    """
    # Re-resolve at call time in case CWD changed, and override=True so .env
    # always wins over any stale shell environment variables.
    dotenv_path = find_dotenv(usecwd=True) or _DOTENV_PATH
    load_dotenv(dotenv_path, override=True)

    client_id = os.getenv("INTACCT_CLIENT_ID")
    if not client_id:
        print(
            "\n[ERROR] INTACCT_CLIENT_ID is not set.\n"
            "Add it to your .env file and try again.\n"
        )
        return

    redirect_uri: str = os.getenv("INTACCT_REDIRECT_URI", DEFAULT_REDIRECT_URI)

    verifier, challenge = _pkce_pair()
    state = secrets.token_urlsafe(32)

    params: dict[str, str] = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "state": state,
        "scope": "offline_access",
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    }
    auth_url = f"{_base_url()}/oauth2/authorize?" + urllib.parse.urlencode(params)

    print("\n─── Sage Intacct OAuth Login ──────────────────────────────────────")
    print(f"\nRedirect URI : {redirect_uri}")
    if redirect_uri == DEFAULT_REDIRECT_URI:
        print(
            "  (Set INTACCT_REDIRECT_URI in .env to match what you registered\n"
            "   in your Intacct OAuth application settings.)"
        )

    print("\nStep 1 — Opening your browser to the Intacct login page...")
    print(f"\n  {auth_url}\n")
    print("  If the browser doesn't open automatically, copy the URL above.")

    try:
        webbrowser.open(auth_url)
    except Exception:  # noqa: BLE001
        pass  # Non-fatal — URL is already printed above

    print(
        "\nStep 2 — Log in and authorize the app in your browser.\n"
        "\nStep 3 — After you click Accept, your browser will redirect to:\n"
        f"\n  {redirect_uri}?code=XXXXXXXX&state=...\n"
        "\n  Copy the value of the 'code' parameter from the address bar.\n"
        "  (The page may show a 404 — that's fine, the code is in the URL.)\n"
    )

    code = ""
    while not code.strip():
        try:
            code = input("Paste the authorization code here and press Enter:\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nLogin cancelled.\n")
            return

    print("\nExchanging authorization code for tokens...")
    try:
        tokens = _exchange_code(code, verifier, redirect_uri)
    except Exception as exc:  # noqa: BLE001
        print(f"\n[ERROR] Token exchange failed:\n  {exc}\n")
        return

    if "access_token" not in tokens:
        print(f"\n[ERROR] Unexpected token response (no access_token):\n  {tokens}\n")
        return

    tokens["issued_at"] = time.time()
    save_tokens(tokens)

    expires_in = tokens.get("expires_in", "unknown")
    has_refresh = "refresh_token" in tokens
    print(
        f"\n  Access token expires in : {expires_in}s"
        f"\n  Refresh token obtained  : {'yes ✓' if has_refresh else 'no (re-login required when token expires)'}"
        f"\n\n─── Login complete ────────────────────────────────────────────────\n"
    )
