# HTTP Headers

HTTP headers are key-value pairs sent between the client and server in an HTTP request or response. They provide essential information about the request or response, such as content type, authentication details, caching policies, and more.

## Request Headers

All non-standard HTTP headers are prefixed with `X-`.

| Name | Required | Default / Sample Value | Description |
|------|----------|----------------------|-------------|
| `Authorization` | Yes | Null | Specifies the access token. See OAuth 2.0 authorization topic for details. |
| `Content-Type` | No | `application/json` | Specifies the format of the request body. |
| `Accept` | No | `application/json` | Specifies the desired output format. |
| `X-Policy` | No | Null | Specifies a policy for asynchronous API calls. |
| `X-IA-API-ParamEntity` | No | `CentralUS-35` | Specifies the entity for the request. If not provided, the default entity for the access token is used. |
| `X-IA-SageSignature` | No | | Provides trusted context information for enhanced security. See Outbound webhooks topic for details. |
| `X-IA-API-ParamTransaction` | No | `False` | Indicates whether all records in a batch request should be handled atomically. See Atomic requests topic for details. |

## Response Headers

The HTTP status codes that indicate limits reached for CPU or throttling are 429 and 503.

- **429** — Client has sent too many requests in a given time (rate limit violation).
- **503** — Server is temporarily unable to handle the request due to overload or other issues.

When a **soft limit** is reached, the request is permitted and `-Limit` and `-Remaining` headers are included in the response. When a **hard limit** is reached, the request is rejected on the first failed validation.

| Name | Sample Value | Description |
|------|-------------|-------------|
| `X-IA-CPU-Request-Cost` | `46800000` | The soft limit of the total hours per calendar month. |
| `X-IA-CPU-Limit` | `46800000` | Upper limit for process CPU usage. |
| `X-IA-CPU-Limit-Remaining` | `46799020` | CPU usage remaining for the time window. |
| `X-IA-CPU-Limit-Reset` | `1656633600` | The remaining window before the CPU limit resets, in seconds. |
| `X-IA-Throttle-Limit` | `13` | Throttle hard limit for the number of concurrent requests. |
| `X-IA-Throttle-Limit-Remaining` | `-1` | The number of available concurrent requests remaining for the time window. |
| `X-IA-Throttle-Limit-RetryAfter` | `60` | The number of seconds before the throttle limit resets. |
| `X-Kong-Response-Latency` | `1539` | Time for Kong to execute plugins and process the request, in seconds. |
| `X-IA-Minute-Rate-Limit` | `13` | The soft limit for total number of requests per 60 seconds. |
| `X-IA-Minute-Rate-Limit-Remaining` | `-1` | The number of requests remaining for the 60-second window. |
| `X-IA-Hour-Rate-Limit` | `13` | The hard limit for the total number of requests per 60 minutes. |
| `X-IA-Hour-Rate-Limit-Remaining` | `-1` | The number of requests remaining for the 60-minute window. |
| `X-IA-Hour-Rate-Limit-Retry-After` | `60` | The number of minutes before the rate limit resets, in seconds. |
| `X-IA-TENANT-Throttle-Limit` | `LIMIT001-10` | Maximum number of requests per tenant or resource. |
| `X-IA-TENANT-Throttle-Limit-Remaining` | `-1` | The number of available concurrent requests remaining for the time window, per tenant. |
| `X-IA-TENANT-Throttle-Limit-Retry-After` | `60` | The number of seconds before the tenant throttle limit resets. |
