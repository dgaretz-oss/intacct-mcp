# Intacct MCP

An MCP server for the Sage Intacct REST and XML API. Gives Claude direct access to your Intacct data — vendors, bills, journal entries, queries, and more — via natural language.

---

## Requirements

Before you start, make sure you have all of the following.

**Sage Intacct**
- An active Intacct subscription with the **Web Services** license enabled. This is a separate add-on — contact your Intacct account manager if it isn't already active.
- A user account with sufficient permissions to read/write the objects you want Claude to access.

> Please take careful consideration with your choice in user account.  Strongly advised to create a separate login with specific permissions required for your intended workflow.

**Sage Developer Portal**
- A free account at [developer.sage.com](https://developer.sage.com). This is where you register the OAuth application and obtain credentials.

**Local tools**
- Python 3.10 or later
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — the Python package manager used to run this project

---

## Step 1 — Install the project


In Windows PowerShell / bash:

```
git clone https://github.com/dgaretz-oss/intacct-mcp
cd intacct-mcp
uv sync
```

---

## Step 2 — Host the OAuth callback page

Intacct requires HTTPS for OAuth redirect URIs, so a localhost server won't work. The simplest solution is a one-page static site hosted for free on Netlify.

1. Locate the `oauth-callback/` folder in this repository.
2. Go to [netlify.com/drop](https://netlify.com/drop) — no account required.
3. Drag the `oauth-callback/` folder onto the page.
4. Netlify gives you a URL like `https://random-name-abc123.netlify.app`. Save it — you'll need it in the next two steps.

> The page reads the `code` parameter from the redirect URL and displays it with a copy button. Netlify cannot use the code to obtain tokens — it doesn't have your PKCE verifier or client secret.

> Alternatively, you could host this on your own web server but it needs to be SSL compliant.

---

## Step 3 — Register an OAuth application on the Sage Developer Portal

1. Sign in to [developer.sage.com](https://developer.sage.com).
2. Confirm under [Programmes](https://developer.sage.com/console/programmes) you have access and the account is assigned to your Intacct Company ID
3. Click [Applications](https://developer.sage.com/console/applications) and create a New Application.  Check "Sage Intacct" and give it a Name.
4. Under **Redirect URIs**, add your Netlify URL from Step 1 (e.g. `https://random-name-abc123.netlify.app`).
5. Save the application. Note your **Client ID** and **Secret Key** — you'll add these to `.env` shortly.


---

## Step 4 — Configure environment variables

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

Edit `.env`:

```env
# From Step 2 — Sage Developer Portal
INTACCT_CLIENT_ID=your-client-id.app.sage.com
INTACCT_CLIENT_SECRET=your-client-secret
INTACCT_USERNAME=your-intacct-username

# Your Netlify callback URL from Step 2
INTACCT_REDIRECT_URI=https://your-site.netlify.app

# Optional — only needed if your Intacct instance is not on the default US endpoint
INTACCT_BASE_URL=https://api.intacct.com/ia/api/v1

# --- XML gateway fallback (OPTIONAL) -----------------------------------------
# REST does not need these. They are ONLY required if you plan to use the
# call_xml_gateway tool for the small set of operations REST cannot do
# (legacy transaction functions, post/unpost, XML-only objects, etc.).
#
# The legacy XML gateway's outer firewall envelope still requires a registered
# Web Services sender ID + password even when the inner authentication is a
# REST-derived session ID. Obtain them from your Intacct administrator at
# Company > Setup > Web Services Sender IDs.
#
INTACCT_SENDER_ID=
INTACCT_SENDER_PASSWORD=
#
# Optional: override the XML gateway URL (defaults to production US).
INTACCT_XML_GATEWAY_URL=https://api.intacct.com/ia/xml/xmlgw.phtml
```

---

## Step 5 — Log in

Run the login command:

```bash
uv run intacct-mcp login
```

This will:
1. Open your browser to the Intacct authorization page.
2. After you log in and click **Accept**, your browser redirects to your Netlify callback page.  Netlify password for drop sites is "My-Drop-Site" which displays the authorization code.
3. Copy the code and paste it into the terminal prompt.
4. The code is exchanged for tokens, which are saved to `~/.intacct_mcp_tokens.json`.

You should see:

```
  Tokens saved to C:\Users\You\.intacct_mcp_tokens.json
  Access token expires in : 86400s
  Refresh token obtained  : yes ✓
```

**You only need to do this once.** The MCP server automatically refreshes the access token using the refresh token. Re-login is only needed if the refresh token is revoked (e.g. you revoke it in Intacct's app settings, or it expires after a long period of inactivity).

---

## Step 6 — Add to Claude Desktop or Other MCP Compatible App

Open your Claude Desktop configuration file.  In Claude Desktop, click Settings -> Developer -> Edit Config.  Common locations:

- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

Add the server under `mcpServers`:

```json
{
  "mcpServers": {
    "intacct": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Users\\You\\path\\to\\intacct-mcp",
        "run",
        "intacct-mcp"
      ]
    }
  }
}
```

Replace the `--directory` value with the absolute path to the `intacct-mcp` folder on your machine. Restart Claude Desktop.

> Note that, absolute path on Windows requires double back slash "\\".

---

## Step68 — Verify the connection

In Claude, ask:

> Run `test_connection` to confirm authentication and connectivity.

If you see an authentication error, check:
- `.env` values are correct and saved
- The Client ID is authorized in Intacct (Step 3)
- `~/.intacct_mcp_tokens.json` exists (re-run `uv run intacct-mcp login` if not)

---

## Setting up on a new device

The `.venv` folder and `.env` file are both gitignored and **must not be copied between machines** — the virtual environment contains hardcoded absolute paths to the original machine and will not work elsewhere.

On the new device, from inside the `intacct-mcp` folder:

```bash
# 1. Install dependencies and recreate the virtual environment
uv sync

# 2. Create a fresh .env with your credentials
cp .env.example .env
#    then edit .env and fill in INTACCT_CLIENT_ID, INTACCT_CLIENT_SECRET,
#    INTACCT_REDIRECT_URI (and optionally INTACCT_USERNAME / INTACCT_BASE_URL)

# 3. Log in to obtain tokens (skip if using client credentials only)
uv run intacct-mcp login
```

That's it — `uv sync` recreates the venv from `pyproject.toml` in one step. No pip, no manual venv creation.

> **Why not just copy `.venv`?** The virtual environment embeds absolute paths to the original machine's Python installation and source directory. Even if the project folder is in the same location, the launcher executables and editable-install path file will point to the wrong machine.

---

## Environment variable reference

| Variable | Required | Description |
|---|---|---|
| `INTACCT_CLIENT_ID` | Yes | OAuth client ID from the Sage Developer Portal |
| `INTACCT_CLIENT_SECRET` | Yes | OAuth client secret from the Sage Developer Portal |
| `INTACCT_USERNAME` | Yes (client credentials) | Intacct username to associate with the token. Intacct's client credentials grant is non-standard and requires this to establish user context. |
| `INTACCT_REDIRECT_URI` | Yes (for login) | Your Netlify callback URL |
| `INTACCT_BASE_URL` | No | Defaults to `https://api.intacct.com/ia/api/v1` |
| `INTACCT_SENDER_ID` | No | Obtain them from your Intacct administrator |
| `INTACCT_SENDER_PASSWORD` | No | Obtain them from your Intacct administrator |
| `INTACCT_XML_GATEWAY_URL` | No | Override the XML gateway URL (defaults to production US) |

---

## XML gateway fallback (optional)

The MCP exposes a `call_xml_gateway` tool for the small set of operations the REST v1 API does not cover — legacy transaction functions (`create_sotransaction`, etc.), `readByQuery` on XML-only objects, post/unpost actions, and other legacy workflows. See `docs/xml/xml-only-objects.md` for the full list of objects that exist only in XML, and `docs/rest/rest-only-objects.md` for the REST-only set.

The fallback uses the **existing OAuth bearer token** — no new user credentials are needed. The MCP exchanges it for an XML session ID via the REST endpoint `GET services/core/session/id` automatically, and caches it.

The legacy XML gateway envelope still requires a **registered Web Services sender ID and password** in the `<control>` block for outer firewall validation. These are configured via the optional `INTACCT_SENDER_ID` / `INTACCT_SENDER_PASSWORD` environment variables. Without them, REST keeps working but `call_xml_gateway` returns a `config_error`.

**Use the XML fallback sparingly.** Most REST errors are bad payload shape, missing required fields, or the wrong path — not a real REST gap. The MCP guidance steers Claude to diagnose REST first and only switch to XML when there is concrete evidence the operation cannot be done via REST.

**FRW reports cannot be retrieved via XML either.** `<readReport>` only returns Custom Report Writer reports. Balance Sheet / Income Statement / Statement of Cash Flows / `gl_fin` / `gl_tb` / financial graphs must come from the Intacct UI or a scheduled SFTP/cloud delivery.

---

## Known Issues

- **OAuth / entity-level actions:** The current OAuth structure does not appear to pass `location_id` for entity-level operations (e.g. transacting at the entity level vs. the top-level company). XML fallback via `call_xml_gateway` is required for these cases.
- **Financial Reports:** Neither the REST nor the XML API exposes a valid endpoint for Financial Report Writer reports. Only the default standard reports (General Ledger, Accounts Payable, etc.) and reports created through the Interactive Custom Report Writer are accessible programmatically.

---

## Token storage and security

- Tokens are stored in `~/.intacct_mcp_tokens.json` with permissions set to owner-read-only (`600`).
- The access token is cached in memory and refreshed automatically — it is never logged.
- The authorization code obtained during login is protected by PKCE: even if intercepted, it cannot be exchanged for tokens without the code verifier that exists only in your terminal process.
