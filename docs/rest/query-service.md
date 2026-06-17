# Query Service

The query service lets you query one or more Sage Intacct objects, filter by any combination of conditions, and shape results. It gives you more flexibility than the standard List (GET) endpoint.

## Overview

- **URI:** `POST /services/core/query`
- **Minimum required fields:** `object` and `fields`
- All query requests use the POST method.

## Basic Query

```json
{
  "object": "accounts-payable/vendor",
  "fields": ["id", "name", "email", "phone"]
}
```

## Query Types

### Single Object Query

Query a single REST API object:

```json
{
  "object": "accounts-payable/vendor",
  "fields": ["key", "id", "name"]
}
```

### Document Type Query

Query document types. You can query the base object, which returns all documents of all types, or use the `::DocumentType` notation to query a specific type:

```json
{
  "object": "order-entry/document::Sales Invoice",
  "fields": ["key", "id", "txnDate"]
}
```

### Multiple Object Query

Query multiple objects by providing an array:

```json
[
  {
    "object": "accounts-payable/vendor",
    "fields": ["key", "id", "name"]
  },
  {
    "object": "accounts-receivable/customer",
    "fields": ["key", "id", "name"]
  }
]
```

### Referenced Object Query

Use dot notation to include fields from related/referenced objects:

```json
{
  "object": "accounts-payable/bill",
  "fields": ["key", "id", "vendor.id", "vendor.name", "vendor.email"]
}
```

### Owning Parent Query

You can query a child (owned) object and include fields from its owning parent using dot notation. You cannot go in the other direction (querying parent and including child fields):

```json
{
  "object": "accounts-payable/bill-line",
  "fields": ["key", "txnAmount", "bill.id", "bill.postingDate"]
}
```

### Custom Fields Query

Custom fields require the derived object form with the namespace prefix:

```json
{
  "object": "accounts-payable/vendor::CRE Partner",
  "fields": ["key", "id", "CRE::CUSTOMFIELD1"]
}
```

## Sorting

Use `orderBy` to sort results:

```json
{
  "object": "accounts-payable/vendor",
  "fields": ["key", "id", "name"],
  "orderBy": [
    { "id": "asc" }
  ]
}
```

Multiple sort fields and dot notation for related object fields are supported:

```json
{
  "orderBy": [
    { "vendor.name": "asc" },
    { "txnDate": "desc" }
  ]
}
```

## Pagination

- `start` — 1-based index of the first record to return (default: 1)
- `size` — number of records per page (max: 4,000 per response)
- The response includes a `next` field in `ia::meta` when more records exist; it's `null` when you're on the last page.

```json
{
  "object": "accounts-payable/vendor",
  "fields": ["key", "id", "name"],
  "start": 1,
  "size": 100
}
```

### Navigating Large Datasets

```
start=1 → fetch page → check ia::meta.next → if not null, next start = previous start + size → repeat until next is null
```

## Filtering

Use the `filters` array with one or more filter conditions.

### Filter Structure

```json
{
  "object": "accounts-payable/vendor",
  "fields": ["key", "id", "name"],
  "filters": [
    {
      "field": "status",
      "operator": "$eq",
      "value": "active"
    }
  ]
}
```

### Comparison Operators

| Operator | Description |
|----------|-------------|
| `$eq` | Equals. Also supports `null` as value. |
| `$ne` | Not equals. Also supports `null` as value. |
| `$lt` | Less than |
| `$lte` | Less than or equal |
| `$gt` | Greater than |
| `$gte` | Greater than or equal |
| `$in` | Value is in a list (array value) |
| `$notIn` | Value is not in a list (array value) |
| `$between` | Value is between two values (array of two) |
| `$notBetween` | Value is not between two values (array of two) |
| `$contains` | String contains substring |
| `$notContains` | String does not contain substring |
| `$startsWith` | String starts with value |
| `$notStartsWith` | String does not start with value |
| `$endsWith` | String ends with value |
| `$notEndsWith` | String does not end with value |

### Relative Date Values

For date fields, you can use relative date strings instead of absolute dates:

| Value | Description |
|-------|-------------|
| `today` | Today's date |
| `yesterday` | Yesterday's date |
| `currentWeek` | Current calendar week |
| `lastWeek` | Previous calendar week |
| `currentMonth` | Current calendar month |
| `priorMonth` | Previous calendar month |
| `currentQuarter` | Current calendar quarter |
| `priorQuarter` | Previous calendar quarter |
| `currentYear` | Current calendar year |
| `priorYear` | Previous calendar year |

```json
{
  "filters": [
    {
      "field": "txnDate",
      "operator": "$gte",
      "value": "currentMonth"
    }
  ]
}
```

### Multiple Filters

Multiple filters in the `filters` array are combined with `AND` by default:

```json
{
  "filters": [
    { "field": "status", "operator": "$eq", "value": "active" },
    { "field": "totalDue", "operator": "$gt", "value": 0 }
  ]
}
```

### Filter Expressions

Use `filterExpression` for complex AND/OR logic. Filters are indexed 1-based and can be combined with parentheses:

```json
{
  "filters": [
    { "field": "status", "operator": "$eq", "value": "active" },
    { "field": "txnDate", "operator": "$gte", "value": "currentMonth" },
    { "field": "totalDue", "operator": "$gt", "value": 0 }
  ],
  "filterExpression": "(1 and 2) or 3"
}
```

### Filter Parameters

Additional filter behavior options:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `asOfDate` | today | Anchor date for relative date values (e.g., `today`, `currentMonth`) |
| `caseSensitiveComparison` | `true` | Whether string comparisons are case-sensitive |
| `includePrivate` | `false` | Whether to include private records (top-level company only) |

```json
{
  "object": "accounts-payable/vendor",
  "fields": ["key", "id", "name"],
  "filters": [
    { "field": "name", "operator": "$startsWith", "value": "abc" }
  ],
  "filterParameters": {
    "caseSensitiveComparison": false
  }
}
```

## Aggregate Functions

You can use aggregate functions in the `fields` array. Non-aggregate fields in the same query automatically become implicit `GROUP BY` fields.

| Function | Syntax | Description |
|----------|--------|-------------|
| Sum | `"sum:fieldName"` | Sum of field values |
| Average | `"avg:fieldName"` | Average of field values |
| Minimum | `"min:fieldName"` | Minimum field value |
| Maximum | `"max:fieldName"` | Maximum field value |
| Count | `"count:fieldName"` | Count of records (boolean/array/enum fields only) |

```json
{
  "object": "accounts-payable/bill",
  "fields": ["vendor.id", "sum:totalDue", "count:status"],
  "filters": [
    { "field": "status", "operator": "$eq", "value": "open" }
  ]
}
```

**Restrictions:**
- Binary and base64 fields are not supported in aggregate queries.
- `count` only works on boolean, array, or enum fields.

## Complete Example

Query all open bills for a specific vendor, sorted by due date, with pagination:

```json
{
  "object": "accounts-payable/bill",
  "fields": [
    "key",
    "id",
    "vendor.id",
    "vendor.name",
    "txnDate",
    "dueDate",
    "totalDue",
    "status"
  ],
  "filters": [
    { "field": "vendor.id", "operator": "$eq", "value": "V001" },
    { "field": "status", "operator": "$eq", "value": "open" }
  ],
  "orderBy": [
    { "dueDate": "asc" }
  ],
  "start": 1,
  "size": 50
}
```

## FAQs

**Can I use `href` in `filters` or `orderBy`?**
No. The `href` field is derived and is not available for filtering or sorting.

**Can I use `*` as a wildcard to return all fields?**
No. You must explicitly list the fields you want in the `fields` array.

**Can I query `writeOnly`, list (deprecated), or deprecated fields?**
No. These fields are not queryable.

**Can I query a parent object and get child object fields?**
No. You can only go upward — query child objects and retrieve parent fields via dot notation. You cannot query a parent and traverse downward to owned/child objects.

**How do I query custom fields?**
Use the derived object form: `"object": "accounts-payable/vendor::CustomType"` and reference custom fields with their namespace prefix: `"nsp::FIELD_NAME"`.
