# Owner and Owned Objects

Objects in the REST API may be owned by other objects. For example, `accounts-payable/bill-line` is an owned object of `accounts-payable/bill`.

You can use the Model service to examine an owned object's relationship to the owning object. The relationship is indicated by the `isOwner: true` property in the `ref` section of the model response.

```json
"bill": {
  "apiObject": "accounts-payable/bill",
  "fields": { "..." : "..." },
  "isOwner": true
}
```

## Operations on Owned Objects

You can invoke operations on an owned object directly or via its owner:

- Create an owner and its owned objects at the same time
- Create an owner first, then create individual owned objects that designate their owner
- Update an owner by adding new owned objects and/or modifying existing owned objects by key
- Update an owned object directly
- Delete an owned object via the owner
- Delete an owned object directly

> **Note:** Some owned objects can only be added/updated/deleted through the owning object. Use the Model service to check `httpMethods` for supported operations.

Multiple records of owned objects specified in one request are processed in **one atomic transaction** when the request is made via the owning object.

## Create an Object and Its Owned Objects

To create a new bill and its line items, provide required fields for the bill and include the `lines` array:

```
POST https://api.intacct.com/ia/api/{version}/objects/accounts-payable/bill
```

```json
{
  "billNumber": "B-0073",
  "vendor": { "id": "1099 Int" },
  "postingDate": "2024-05-05",
  "dueDate": "2024-10-02",
  "createdDate": "2024-05-05",
  "lines": [
    {
      "account": { "id": "7120" },
      "txnAmount": 100,
      "location": { "id": "1" }
    },
    {
      "account": { "id": "7120" },
      "txnAmount": 175,
      "location": { "id": "1" }
    }
  ]
}
```

## Create an Owned Object Directly

You must specify a reference to the owning object in the request:

```
POST https://api.intacct.com/ia/api/{version}/objects/accounts-payable/bill-line
```

```json
{
  "account": { "id": "7120" },
  "txnAmount": 100,
  "department": { "id": "1" },
  "location": { "id": "1" },
  "bill": { "key": "901" }
}
```

## Update an Object and Its Owned Objects

- If you specify a `key` for an owned object → you are **updating** that owned object
- If you do not specify a `key` → you are **adding** a new owned object

```
PATCH https://api.intacct.com/ia/api/{version}/objects/accounts-payable/bill/901
```

```json
{
  "description": "Update line, add line",
  "lines": [
    {
      "key": "644",
      "txnAmount": "555.00"
    },
    {
      "txnAmount": "99.00",
      "accountLabel": { "id": "Accounting fees" }
    }
  ]
}
```

## Update an Owned Object Directly

```
PATCH https://api.intacct.com/ia/api/{version}/objects/accounts-payable/bill-line/644
```

```json
{
  "txnAmount": "150"
}
```

> You cannot update an owned object's reference to its owning object (can't change it to be owned by a different object).

## Delete an Owned Object Directly

```
DELETE https://api.intacct.com/ia/api/{version}/objects/accounts-payable/bill-line/1092
```

Successful delete operations return `204 No Content` (empty response).

## Mixed Operations

Use PATCH on the owning object to add, update, or delete owned objects in one atomic request.

The operation on each item record is determined as:
- **POST** — when no `key` is specified
- **PATCH** — when `key` is specified
- **DELETE** — set `ia::operation` to `"delete"`

```
PATCH https://api.intacct.com/ia/api/{version}/objects/accounts-payable/bill/901
```

```json
{
  "description": "UPDATED journal entry, deleted two lines",
  "lines": [
    {
      "ia::operation": "delete",
      "key": "7200"
    },
    {
      "ia::operation": "delete",
      "key": "7201"
    },
    {
      "key": "3455",
      "txnAmount": "560.00"
    },
    {
      "txnAmount": "109.00",
      "accountLabel": { "id": "Service fee" }
    }
  ]
}
```
