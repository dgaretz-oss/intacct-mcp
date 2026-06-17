# Batch, Bulk, and Composite Requests

To increase the performance of your application, use batch, bulk, or composite requests to combine multiple REST API requests into a single request.

## Batch Requests

You can process multiple records for a single REST API object in one request. Maximum: **500 records** per batch request. Also supported for workflows (`/workflows/`).

### GET (Batch Retrieval)

```
GET https://api.intacct.com/ia/api/{version}/objects/accounts-payable/bill/194,195,310,145
```

### POST (Batch Create)

Send an array of objects in the request body:

```bash
curl --request POST 'https://api.intacct.com/ia/api/{version}/objects/company-config/contact' \
--header 'Authorization: Bearer ' \
--header 'Content-Type: application/json' \
--data-raw '[
  { "id": "CYoung", "email1": "info@bakinggoods.com", "printAs": "Caroline Young" },
  { "id": "FYoung", "email1": "info@campingsupplies.com", "printAs": "Fred Young" },
  { "id": "WYoung", "email1": "info@bulbsandseed.com", "printAs": "Wes Young" }
]'
```

Response includes `ia::result` (array of created object references) and `ia::meta` (overall status summary).

### PATCH (Batch Update)

Unlike individual requests, specify the object `key` in the request body (not the path):

```bash
curl --request PATCH 'https://api.intacct.com/ai/api/{version}/objects/company-config/contact' \
--data-raw '[
  { "key": "1", "email1": "ofni@bakinggoods.com" },
  { "key": "2", "email1": "ofni@campingsupplies.com" }
]'
```

### DELETE (Batch Delete)

```
DELETE https://api.intacct.com/ai/api/{version}/objects/company-config/contact/1,2,3
```

A successful response returns HTTP 204 No Content. For partially successful DELETE requests, correlate successful responses with the request by array position (index), as successful deletes do not include the `key` property.

## Atomic Requests

Configure batch requests to be processed atomically or non-atomically.

In atomic mode, if any operation fails, the entire transaction is rolled back. To enable:

```
--header 'X-IA-API-Param-Transaction: true'
```

> **Note:** Multiple records of owned objects specified in one request via the owning object are automatically processed atomically. This is not considered a batch request.

When atomic mode fails, the REST API returns 207 Multi-Status, 404 Not Found, 422 Unprocessable Entity, or another HTTP error. Each individual response contains `ia::status` and `ia::error`, with an overall summary in `ia::meta`.

## Non-Atomic Requests

By default, batch requests are non-atomic. When unsuccessful or partially successful, each individual response contains its request status, and the overall status is summarized in `ia::meta`.

## Batch Requests on Owned Objects

You can include owned objects in batch requests. You must include the `key` of the owning object for each record. Supports mixed operations (`ia::operation`: `"delete"`, `"patch"`) within the lines array.

## Bulk Requests

Use the bulk request service to process multiple operations for one REST object with a single HTTPS call. Data is passed via a JSON file. No limit on number of operations. Operations are processed as separate transactions — processing continues on success or failure.

### Submit a Bulk Request

**URI:** `https://api.intacct.com/ia/api/{version}/services/bulk/job/create`  
**HTTP method:** POST

```bash
curl --location 'https://api.intacct.com/ia/api/v1/services/bulk/job/create' \
--header 'Authorization: Bearer {{your_authorization_token}}' \
--form 'ia::requestBody="{ \"objectName\" : \"accounts-payable/vendor\", \"operation\": \"create\", \"jobFile\": \"vendors.json\", \"fileContentType\": \"json\" }"' \
--form 'file=@"/path/to/vendors.json"'
```

**`ia::requestBody` attributes:**
- `objectName` — the REST object (e.g., `accounts-payable/vendor`)
- `operation` — `create` (POST), `update` (PATCH), or `delete` (DELETE)
- `jobFile` — name of the file input
- `fileContentType` — must be `json`

**`file`:** JSON array of objects to create/update/delete. Object properties must match the schema definition.

### Check Bulk Request Status

**URI:** `https://api.intacct.com/ia/api/{version}/services/bulk/job/status`  
**HTTP method:** GET

```bash
curl --location 'https://api.intacct.com/ia/api/v1/services/bulk/job/status?jobId={{job_id}}&download=true' \
--header 'Authorization: Bearer {{your_authorization_token}}'
```

Job statuses: `queued`, `processing`, `completed`, or `failed`. Set `download=true` to download results as JSON once completed.

## Composite Requests

Send a single HTTPS call containing multiple sub-requests for different objects or services.

**Capabilities:**
- Support mixed operations (e.g., GET and POST)
- Support different objects in one request
- Use output from one sub-request in subsequent sub-requests (via `resultReference`)
- Support HTTP headers per sub-request (`Authorization`, `Content-Type`, `Accept` are inherited)

**Constraints:**
- Supports 2–10 sub-requests
- All sub-requests must use the same API version
- Sub-requests execute sequentially; execution stops on first failure (no rollback)
- Responses are synchronous

**URI:** `https://api.intacct.com/ia/api/{version}/services/core/composite`  
**HTTP method:** POST

```json
[
  {
    "method": "POST",
    "path": "/objects/accounts-payable/vendor",
    "body": { "..." : "..." },
    "resultReference": "vendor",
    "headers": { "X-ABC": "123" }
  },
  {
    "method": "GET",
    "path": "/objects/accounts-payable/vendor/@{vendor.1.key}"
  }
]
```

## Preventing Duplicate Requests (Idempotency)

Use the `Idempotency-Key` header to prevent duplicate POST and PATCH requests. GET and DELETE are already idempotent and don't support this header. Max 256 characters.

```
--header 'Idempotency-Key: e9606bb2-6be1-4c9e-a2a7-134cd644a5ee'
```

**Behavior:**
- Intacct saves the key, original request, and response (even on failure)
- The `Idempotency-Key` header is included in the response
- Response also includes `x-ia-idempotency-cached-date` header
- Results are cached for 48 hours; duplicates return the original status and cached result
- Reusing a key with a different request body returns **409 Conflict**
- Key is stored for 60 days; same key during that period returns 409

**Additional notes:**
- Core services like `model` and `query` do not support idempotency
- If multiple identical requests arrive before the first finishes, the first gets the idempotency lock; others return an error
