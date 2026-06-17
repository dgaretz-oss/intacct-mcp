# Outbound Webhooks

Using Platform Triggers, you can automate tasks to streamline your workflows. When working with POST request trigger types, you can use outbound webhooks to push payloads to servers that you want automatically updated.

## Create a Platform Trigger Webhook

1. Follow the instructions to create a trigger using the steps in "Add Platform triggers to automate tasks."
2. Ensure you select **HTTP post** as your trigger type.
3. When defining the trigger type properties, select **Use webhook delivery**.
4. When you select **Use webhook delivery**, the **Client ID** field appears. Add your client ID information. (Obtain a client ID via the REST developer quick start.)
5. Define the remainder of your property details.

If a call is unsuccessful, retries occur until a successful HTTP status code of 200 is received, up to 4 attempts. The following HTTP status codes trigger retries:
- 408 Request Timeout
- 429 Too Many Requests
- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable
- 504 Gateway Timeout

If the first call fails, retries occur at the following intervals:
- First retry after 10 seconds
- Second retry after 30 seconds
- Third retry after 90 seconds

## Idempotency Handling

To ensure idempotent message processing:

1. Each webhook request includes a unique `Idempotency-Key`.
2. Recipients should:
   - Use the `Idempotency-Key` for deduplication.
   - Check if the `Idempotency-Key` has been processed before handling.
   - Return the same response for duplicate `Idempotency-Key`s.
   - Keep the `Idempotency-Key` history for at least 24 hours.

## Integrate with Sage Intacct

If you need to integrate a system with Sage Intacct to receive webhook requests, endpoints must:
- Support HTTPS
- Be publicly accessible
- Accept HTTP POST requests
- Respond within the specified timeout periods

Sage Intacct recommends verifying request JWT signatures and using HTTPS for transport encryption. Required headers in webhook requests from Sage Intacct:

- `Authorization` bearer token
- `x-clientcontext` — your trigger information
- `X-IA-Sage-Signature` — base64 encoded context information, including the client ID and the JWT token (decoded on the server side)
- `X-IdempotencyKey` — for duplicate request checking

## Security Steps

Use the following security steps to verify that the webhook originated from Sage Intacct:

1. Decode and verify the JWT contained in `X-IA-Sage-Signature` using your client secret (HS256).
2. Validate standard claims: Check `exp` has not passed, `iss` is `"Sage Intacct"`.
3. Hash the raw received request body with SHA-256 (hex-encoded).
4. Compare the hash to the `payload_signature` claim in the JWT.
5. If all checks pass, the payload is authentic and has not been tampered with.

### JWT Claims

| Claim | Description |
|-------|-------------|
| `iat` | Issued at (epoch ms) |
| `exp` | Expiration (iat + 1 hour) |
| `iss` | `"Sage Intacct"` |
| `tenant_id` | Client ID / Tenant identifier |
| `app_id` | Partner application ID |
| `payload_signature` | SHA-256 hex hash of the exact posted body string |
| `payload_signature_alg` | `SHA-256` |

### Subscriber Verification (Pseudocode)

```python
import jwt, hashlib

def verify_jwt_signature(received_body, jwt_token, shared_secret):
    # Two-step verification:
    # 1. Verify the JWT signature (proves it came from someone with the shared secret)
    # 2. Verify the payload hash (proves the HTTP body was not swapped)
    # Both steps are REQUIRED for secure verification.

    # Step 1: Verify JWT signature and decode claims
    # This also validates exp (expiration) automatically
    claims = jwt.decode(jwt_token, shared_secret, algorithms=["HS256"], issuer="Sage Intacct")

    # Step 2: Verify payload integrity (CRITICAL - do not skip)
    # Without this, an attacker could present a valid JWT with a different HTTP body
    expected_hash = hashlib.sha256(received_body).hexdigest()
    return claims["payload_signature"] == expected_hash
```

### Decoded Client Context Example

```json
{
  "COMPANY": "199056",
  "ENTITY": false,
  "USER": "9",
  "OBJECTNAME": "CLASS",
  "RESTOBJECTNAME": "company-config/class",
  "DOCTYPE": "",
  "ID": {},
  "VID": "200",
  "EVENT": "after_update",
  "EVENTNAME": "CreateUpdate class"
}
```

Other suggested practices include implementing rate-limiting and logging all webhook requests to assist with troubleshooting.
