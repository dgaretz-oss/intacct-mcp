# Intacct REST API — Entity Filter for Reports

## Summary

The `X-IA-API-ParamEntity` request header does **not** scope financial report output to a specific entity. Entity filtering must be passed in the request body under `parameters.dimensions.location.id`.

---

## Working Pattern

### Endpoint

```
POST /ia/api/v1/services/reports/general-ledger/trial-balance
```

### Request Body

```json
{
  "reportName": "Trial Balance - Entity 102 - March 2026",
  "outputType": "csv",
  "outputLocation": "intacct",
  "parameters": {
    "dimensions": {
      "location": {
        "id": "102"
      }
    },
    "timePeriod": {
      "dateRange": {
        "startDate": "2026-03-01",
        "endDate": "2026-03-31"
      }
    }
  }
}
```

### Key Points

- `parameters.dimensions.location.id` — the entity/location ID (e.g. `"102"` for Greenville Gardens)
- `parameters.timePeriod.dateRange` — use for trial balance (start + end date)
- `parameters.timePeriod.periodToDate.asOfDate` — use for balance sheet / point-in-time reports
- `reportName` — display label for the stored output; does not select the report definition
- `outputType` — valid values: `html`, `pdf`, `csv`, `excel`, `text`
- `outputLocation` — `intacct` or `cloud`

---

## Statistical Accounts

By default, statistical accounts are excluded. To include them, add to `parameters`:

```json
"showStatisticalAccounts": "showStatisticalAccounts"
```

Valid enum values (note: the API default value contains a typo — `incluseStatisticalAccounts` — which causes the default behavior to exclude them):

| Value | Behavior |
|-------|----------|
| `showStatisticalAccounts` | Include statistical accounts alongside regular accounts |
| `onlyShowStatisticalAccounts` | Show statistical accounts only |
| `doNotShowStatisticalAccounts` | Exclude statistical accounts |

---

## Polling and Download

### Check Status

```
GET /ia/api/v1/services/reports/status?reportId={id}&outputType={type}&outputLocation={location}
```

Status values: `pending`, `completed` (returns HTTP 303 redirect), `failed`

### Download

```
GET /ia/api/v1/services/reports/download?reportId={id}&outputType={type}
```

A 303 on the status endpoint means the report is ready. Proceed directly to the download endpoint.

---

## Confirmed Working Report Slugs (general-ledger namespace)

| Report | Slug | Time Parameter |
|--------|------|----------------|
| Trial Balance | `general-ledger/trial-balance` | `timePeriod.dateRange` |
| Account Balance (raw) | `general-ledger/account-balance` | `timePeriod.dateRange` or `periodToDate.asOfDate` — requires `glAccountRange` or `glAccountGroup` |

---

## Known Limitations

- **`financial-reports` namespace** (`services/reports/financial-reports/...`) returns "not supported in version 1" for all paths, including with random/garbage paths — confirming this namespace is not yet enabled for this company instance, not a path naming issue.
- **`gl_fin` and `gl_tb`** are internal Intacct report type codes visible in the stored report CSV export. They do not map to REST API path slugs.
- **Formatted financial reports** (Balance Sheet, Income Statement, etc.) built in Intacct's Financial Report Writer are not currently accessible via the REST `services/reports/` API for this instance.
- **`X-IA-API-ParamEntity` header** — establishes session context but is ignored by the report service for data filtering. Always use `parameters.dimensions.location.id` in the body.
