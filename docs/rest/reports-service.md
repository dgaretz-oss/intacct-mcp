# Reports

There are many types of reports offered in Sage Intacct: standard application reports, financial reports, and custom reports.

Using the report service, you can:
- Submit a request for asynchronous processing of a report
- Retrieve the status of a report job
- Cancel a queued report
- Download report output
- Request a stored report in a different format

User-defined report definitions are represented by REST objects (see [Report Objects](#report-objects) below).

## Report Service URI and Examples

Reports are exposed through the `/reports/` resource type. Report output can be stored in the Intacct database (`intacct`) or in the cloud (`cloud`).

**URI:**
```
https://{hostname}/api/<version>/services/reports/<application-name>/<report-name>
```

**HTTP method:** POST

**Example:** `/services/reports/general-ledger/trial-balance`

**Payload parameters:**
- `reportName` — name for the report (required)
- `outputType` — format: `html`, `pdf`, `csv`, `excel`, or `text`
- `outputLocation` — storage location: `intacct` or `cloud`
- `parameters` — optional properties specific to the report

**Sample request body:**

```json
{
  "name": "Trial Balance Report",
  "outputType": "csv",
  "outputLocation": "intacct",
  "parameters": {
    "includeStatisticalAccounts": "false",
    "asOfDate": "2025-09-09"
  }
}
```

**Sample success response:**

```
HTTP status: 202 Accepted
Location header: ../status?reportId=<reportId>&outputType=<outputType>&outputLocation=<outputLocation>
Retry-After: 30 (seconds)
```

```json
{
  "ia::result": {
    "status": "submitted",
    "outputType": "pdf",
    "name": "Q2 Report",
    "reportId": "<reportId>",
    "outputLocation": "<outputLocation>",
    "href": "/services/reports/status?reportId=<reportId>&outputType=<outputType>&outputLocation=<outputLocation>"
  }
}
```

## Retrieve Report Definition

Use the model service:

```
https://{hostname}/api/<version>/services/core/model?name=services/reports/<application-name>/<report-name>
```

## Report Status Service

Use the `/reports/status` resource to retrieve the status of a report job.

**URI:** `https://{hostname}/api/<version>/services/reports/status`  
**HTTP method:** GET

**Parameters:**
- `reportId` — report ID from the run-report response (required)
- `outputType` — `html`, `pdf`, `csv`, `excel`, or `text` (required)
- `outputLocation` — `intacct` or `cloud` (required)

**Sample Intacct storage completed response:**

```json
{
  "ia::result": {
    "status": "completed",
    "outputType": "pdf",
    "name": "Customer Report",
    "reportId": "10",
    "outputLocation": "intacct",
    "downloadURL": "/services/reports/download?reportId=10&outputType=pdf",
    "href": "/services/reports/status?reportId=10&outputType=pdf&outputLocation=intacct"
  }
}
```

**Sample cloud storage completed response:**

```json
{
  "ia::result": {
    "status": "completed",
    "outputType": "pdf",
    "name": "Customer Report",
    "outputLocation": "cloud",
    "cloudStore": {
      "target": "<storage name>",
      "path": "/"
    }
  }
}
```

## Cancel a Queued Report

You cannot cancel an in-progress report job, but you can change `submitted` to `canceled`.

**URI:** `https://{hostname}/api/<version>/services/reports/cancel`  
**HTTP method:** POST

```json
{
  "reportId": "<id>",
  "outputType": "pdf",
  "outputLocation": "intacct"
}
```

**Sample success response:**

```json
{
  "ia::result": {
    "status": "canceled",
    "outputType": "pdf",
    "reportId": "10",
    "outputLocation": "intacct",
    "href": "/services/reports/status?reportId=10&outputType=pdf&outputLocation=intacct"
  }
}
```

## Download Report Output

Use `/reports/download` to download report output stored in Intacct.

**URI:** `https://{hostname}/api/<version>/services/reports/download?reportId=<reportId>&outputType=<type>`  
**HTTP method:** GET

**Parameters:**
- `reportId` — report ID (required)
- `outputType` — output format (required)

**HTTP status:**
- `200 Success` — download starts
- `404 Not Found` — report is not available

## Request a Stored Report in a Different Format

Use `/services/reports/stored-reports` to request a completed report in a different format.

If stored in Intacct, you can request it be sent to the cloud (set `outputLocation` to `cloud`). You can request an `intacct` report in a specified format only if it hasn't been requested in that format already.

**URI:** `https://{hostname}/api/<version>/services/reports/stored-reports`  
**HTTP method:** POST

```json
{
  "reportId": "<id>",
  "name": "<name>",
  "outputType": "pdf",
  "outputLocation": "intacct",
  "cloudStoreDetails": {}
}
```

## Report Objects

User-defined report definitions are represented by REST objects. This includes out-of-the-box application reports, financial reports, and definitions created through Custom Report Writer and Interactive Custom Report Writer.

A report group is a collection of two or more memorized reports that can be scheduled to run at the same time.

**User-defined report objects:**
- `/objects/reports/report-group`
- `/objects/reports/custom-report`
- `/objects/reports/interactive-custom-report`

**Stored reports** — logged-in user's reports stored in Intacct or the cloud (not report definitions).

**Delete a report:** Issue a DELETE request on `/objects/reports/stored-report/<key>`.
