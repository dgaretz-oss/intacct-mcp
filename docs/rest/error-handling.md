# Error Handling

Sage Intacct REST API requests return HTTP status codes. In addition to the status codes, errors include a JSON response payload with more details about the error and its causes.

## Successful Requests (2XX)

| Code | Description | Notes |
|------|-------------|-------|
| 200 OK | The request succeeded. | |
| 201 Created | A POST operation successfully created a new resource. | Response payload contains an `href` for the new resource. |
| 202 Accepted | The server accepted the request and will execute it later. | |
| 204 No Content | The server successfully executed the method but returns no response body. | A successful DELETE always returns 204. |
| 207 Multi-Status | A bulk request that returns multiple status codes. | In some cases only one status code is returned when applicable to all records. |

## Failed Requests (4XX / 5XX)

| Code | Description | Notes |
|------|-------------|-------|
| 400 Bad Request | Error detected in the request that can be fixed by the client. | e.g., schema error in payload. |
| 401 Unauthorized | OAuth2 is not able to authenticate the login credential. | |
| 403 Forbidden | Authenticated user lacks permission to run the operation or access the target resource. | |
| 404 Not Found | Specified resource does not exist for GET or PATCH operation. | |
| 405 Method Not Allowed | The requested method is not supported for the specified resource. | Regardless of authentication or authorization. |
| 409 Conflict | Two requests from the same user have the same idempotency key or unique key. | |
| 422 Unprocessable Entity | Business logic or business validation error. | Payload conforms to schema but values are not valid. |
| 429 Too Many Requests | Bulk size exceeds rate limit or total requests in a period exceed quota. | |
| 500 Internal Server Error | Sage Intacct internal server error. | Provide `supportId` or `requestId` to Support for assistance. |

## Error Response Payload

REST API errors include a response payload with the following structure:

**`ia::error` object:**
- `code` — REST API error code (subcategory of HTTP status), e.g., `invalidKey`, `invalidRequest`, `operationFailed`. May also be a gateway error code such as `GW-0011`.
- `message` — Human-readable error message, e.g., `Version is not supported` or `Malformed URL`.
- `supportId` — Intacct support ID.
- `details` — Additional details (included when multiple errors are detected or business logic errors are returned).

**`ia::meta` object:**
- `totalCount` — Total number of operations processed
- `totalSuccess` — Number of operations that succeeded
- `totalError` — Number of operations that failed

### Example: Invalid Request

```json
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "ia::error": {
    "code": "invalidRequest",
    "message": "Version is not supported.",
    "supportId": "63avN%7EYPhcEDEPVpw1ywI1oV0iNQAAAAw"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 0,
    "totalError": 1
  }
}
```

### Example: Error with Details

```json
HTTP/1.1 422 Bad Request
Content-Type: application/json

{
  "ia::error": {
    "code": "operationFailed",
    "message": "Operation create object HQemployee failed",
    "supportId": "sojLj%7EX2vg0DE3Vop0PJU6UeQVxQAAAEw",
    "details": [
      {
        "code": "BL01001973",
        "message": "Employee Contact info cannot be empty [Support ID: ...]"
      }
    ]
  }
}
```

## API Gateway Error Responses

When a REST API request fails due to a gateway error, the `code` in the error response payload starts with `GW-` followed by 4 numeric values (e.g., `GW-0001`).

- **4XX gateway errors:** codes `GW-0010` through `GW-0042`
- **5XX gateway errors:** codes `GW-0001` through `GW-0009`

### Example Gateway Error

```json
{
  "ia::error": {
    "code": "GW-0011",
    "message": "Invalid Request",
    "details": {
      "requestId": "AC47C2BE:D9EE_63EBC07F.59"
    }
  }
}
```

### 4XX Gateway Error Codes

| Code | Message | Description |
|------|---------|-------------|
| GW-0010 | API rate limit exceeded | Throttle/rate-limit exceeded, no remaining slots. |
| GW-0011 | Invalid Request | Tenant not available/found, inactive/invalid sender ID, inactive/invalid client ID, or inactive tenant. |
| GW-0012 | Missing Tenant Data | Missing tenant in OAuth request (e.g., `username` element present but value doesn't include the tenant). |
| GW-0014 | Invalid Content Type | XML content included in a REST API request. |
| GW-0015 | Missing `<attribute-name>` Attribute | Required attribute missing from request payload. |
| GW-0031 | Invalid Token | JWT token cannot be decoded or doesn't contain required elements. |
| GW-0032 | Invalid Token Payload | `grant_type` is invalid or payload is not in attribute-value format. |
| GW-0033 | Invalid Token Endpoint | `/oauth2` endpoint is not one of the supported options. |
| GW-0034 | Invalid Authorization Header | Header value does not start with `Bearer`. |
| GW-0035 | Missing Token Payload | Body is missing from the OAuth token request. |
| GW-0036 | Missing User Name | `username` element present but value is missing or empty. |
| GW-0037 | Missing Client ID | `client_id` is missing in an OAuth token request. |
| GW-0038 | Multiple Client IDs | Multiple `client_id` values in an OAuth token request. |
| GW-0039 | Multiple Usernames | More than one `username` key-value specified in OAuth token request. |
| GW-0042 | Forbidden | External IP with an override cookie. |

For 5XX gateway errors, the only returned code is: **GW-0001 Unable to process request**. Contact Support for assistance.
