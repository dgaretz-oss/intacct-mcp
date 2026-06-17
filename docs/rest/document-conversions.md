# Document Conversions

The Order Entry and Purchasing document endpoints support document conversions. For example, you can convert a Sales Invoice to a Sales Return or a Purchase Order to a Vendor Invoice.

To convert one document type to another, issue a POST request specifying the transaction definition you want to convert to in the endpoint, and pass these key fields in the request payload:

- `sourceDocument` (at the top level)
- `sourceDocument` (in the `lines` array)
- `sourceDocumentLine` (in the `lines` array)

The conversion creates the transaction definition specified in the endpoint while marking the `sourceDocument` specified in the payload as converted.

## Order Entry Example

Converts an Order Entry Sales Invoice to a Sales Return.

**Endpoint:**

```
POST https://api.intacct.com/ia/api/{version}/objects/order-entry/document::Sales Return
```

**Example request body:**

```json
{
  "sourceDocument": {
    "id": "Sales Invoice-SUBINV#5812#doc"
  },
  "customer": {
    "id": "1"
  },
  "state": "pending",
  "txnDate": "2025-01-29",
  "dueDate": "2026-10-28",
  "txnCurrency": "USD",
  "baseCurrency": "USD",
  "lines": [
    {
      "dimensions": {
        "item": { "id": "1" },
        "warehouse": { "id": "1" },
        "location": { "id": "1" }
      },
      "sourceDocument": {
        "key": "12920"
      },
      "sourceDocumentLine": {
        "key": "14468"
      },
      "unit": "Each",
      "unitQuantity": "1",
      "unitPrice": "1000"
    }
  ]
}
```

**Example response:**

```json
{
  "ia::result": {
    "id": "12922",
    "key": "12922",
    "href": "/objects/order-entry/document::Sales%20Return/12922"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## Purchasing Example

Converts a Purchase Order to a Vendor Invoice.

**Endpoint:**

```
POST https://api.intacct.com/ia/api/{version}/objects/purchasing/document::Vendor Invoice
```

**Example request body:**

```json
{
  "sourceDocument": {
    "id": "Purchase Order-PO#0171#doc"
  },
  "state": "pending",
  "documentNumber": "1235",
  "txnDate": "2025-05-27",
  "postingDate": "2025-05-27",
  "dueDate": "2025-07-31",
  "referenceNumber": "REST API convert",
  "memo": "test memo",
  "txnCurrency": "USD",
  "exchangeRate": {
    "date": "2025-05-27",
    "rate": "1.1234567891"
  },
  "baseCurrency": "USD",
  "shippingMethod": { "id": "Air" },
  "vendor": { "id": "201" },
  "lines": [
    {
      "unit": "Each",
      "unitQuantity": "1",
      "unitPrice": "1000",
      "dimensions": {
        "item": { "id": "1" },
        "warehouse": { "id": "1" },
        "location": { "id": "1" }
      },
      "sourceDocument": {
        "key": "12924"
      },
      "sourceDocumentLine": {
        "key": "14472"
      }
    }
  ]
}
```

**Example response:**

```json
{
  "ia::result": {
    "id": "12925",
    "key": "12925",
    "href": "/objects/purchasing/document::Vendor%20Invoice/12925"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
