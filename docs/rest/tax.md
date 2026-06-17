# Tax

## GET /objects/tax/account-label-tax-group
_List account label tax groups_

**Response 200 — List account label tax groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Auto Account Label Tax",
      "href": "/objects/tax/account-label-tax-group/1"
    },
    {
      "key": "2",
      "id": "Electronic Account Label Tax",
      "href": "/objects/tax/account-label-tax-group/2"
    },
    {
      "key": "3",
      "id": "Gardening Account Label Tax",
      "href": "/objects/tax/account-label-tax-group/3"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/tax/account-label-tax-group
_Create an account label tax group_

**Request example — Create an account label tax group:**
```json
{
  "id": "Auto Account Label Tax",
  "taxSolution": {
    "id": "1"
  }
}
```
**Response 201 — Reference to new account label tax group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Auto Account Label Tax",
    "href": "/objects/tax/account-label-tax-group/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/account-label-tax-group/{key}
_Get an account label tax group_

**Response 200 — Get an account label tax group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Auto Account Label Tax",
    "href": "/objects/tax/account-label-tax-group/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/tax/account-label-tax-group/{key}
_Update an account label tax group_

**Request example — Update an account label tax group:**
```json
{
  "taxSolution": {
    "id": "1"
  }
}
```
**Response 200 — Reference to updated account label tax group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Auto Account Label Tax",
    "href": "/objects/tax/account-label-tax-group/1"
  },
  "ia-meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/tax/account-label-tax-group/{key}
_Delete an account label tax group_


## GET /objects/tax/contact-tax-group
_List contact tax groups_

**Response 200 — List contact tax groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Auto Contact Tax",
      "href": "/objects/tax/contact-tax-group/1"
    },
    {
      "key": "2",
      "id": "Electronic Contact Tax",
      "href": "/objects/tax/contact-tax-group/2"
    },
    {
      "key": "3",
      "id": "Gardening Contact Tax",
      "href": "/objects/tax/contact-tax-group/3"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/tax/contact-tax-group
_Create a contact tax group_

**Request example — Create a contact tax group:**
```json
{
  "id": "Auto Contact Tax",
  "taxSolution": {
    "id": "1"
  }
}
```
**Response 201 — Create a contact tax group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Auto Contact Tax",
    "href": "/objects/tax/contact-tax-group/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/contact-tax-group/{key}
_Get a contact tax group_

**Response 200 — Details of the contact tax group:**
```json
{
  "ia::result": {
    "key": "126",
    "id": "Australian Export Customers",
    "isVATEnabled": true,
    "href": "/objects/tax/contact-tax-group/126"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/tax/contact-tax-group/{key}
_Update a contact tax group_

**Request example — Update a contact tax group:**
```json
{
  "taxSolution": {
    "id": "1"
  }
}
```
**Response 200 — Update a contact tax group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Auto Contact Tax",
    "href": "/objects/tax/contact-tax-group/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/tax/contact-tax-group/{key}
_Delete a contact tax group_


## GET /objects/tax/item-tax-group
_List item tax groups_

**Response 200 — List item tax groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Auto Item Tax",
      "href": "/objects/tax/item-tax-group/1"
    },
    {
      "key": "2",
      "id": "Electronic Item Tax",
      "href": "/objects/tax/item-tax-group/2"
    },
    {
      "key": "3",
      "id": "Gardening Item Tax",
      "href": "/objects/tax/item-tax-group/3"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/tax/item-tax-group
_Create an item tax group_

**Request example — Create an item tax group:**
```json
{
  "id": "Auto Item Tax",
  "taxSolution": {
    "id": "1"
  }
}
```
**Response 201 — Create an item tax group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Auto Item Tax",
    "href": "/objects/tax/item-tax-group/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/item-tax-group/{key}
_Get an item tax group_

**Response 200 — Details of the item tax group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Auto Item Tax",
    "isVATEnabled": true,
    "href": "/objects/tax/item-tax-group/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/tax/item-tax-group/{key}
_Update an item tax group_

**Request example — Update an item tax group:**
```json
{
  "taxSolution": {
    "id": "1"
  }
}
```
**Response 200 — Update an item tax group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Auto Item Tax",
    "href": "/objects/tax/item-tax-group/1"
  },
  "ia-meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/tax/item-tax-group/{key}
_Delete an item tax group_


## GET /objects/tax/order-entry-tax-detail
_List Order Entry tax details_

**Response 200 — List Order Entry tax details:**
```json
{
  "ia::result": [
    {
      "key": "82",
      "id": "UK Sale Goods Exempt Rate",
      "href": "/objects/tax/order-entry-tax-detail/82"
    },
    {
      "key": "83",
      "id": "UK Sale Goods Reduced Rate",
      "href": "/objects/tax/order-entry-tax-detail/83"
    },
    {
      "key": "84",
      "id": "UK Sale Goods Standard Rate",
      "href": "/objects/tax/order-entry-tax-detail/84"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/tax/order-entry-tax-detail
_Create an Order Entry tax detail_

**Request example — Create an Order Entry tax detail:**
```json
{
  "id": "UK General Export Reduced Rate",
  "taxUniqueId": "GB.ECOutput_GB.ExemptGB.VAT",
  "description": "Reduced Rate for UK General Export",
  "taxPercent": 10.02,
  "taxLimit": {
    "minTax": 10,
    "maxTax": 150,
    "minTaxable": 10,
    "maxTaxable": 2000
  },
  "amountToTax": "fullAmount",
  "salesGLAccount": {
    "id": "1200.01"
  },
  "taxAuthority": {
    "id": "California"
  },
  "taxSolution": {
    "id": "United Kingdom - VAT"
  },
  "status": "active",
  "taxRate": "standard",
  "useExpenseAccount": false
}
```
**Response 201 — New Order Entry tax detail:**
```json
{
  "ia::result": {
    "key": "308",
    "id": "UK General Export Reduced Rate",
    "href": "/objects/tax/order-entry-tax-detail/308"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/order-entry-tax-detail/{key}
_Get an Order Entry tax detail_

**Response 200 — Get an Order Entry tax detail:**
```json
{
  "ia::result": {
    "key": "308",
    "id": "UK General Export Reduced Rate",
    "taxUniqueId": "GB.ECOutput_GB.ExemptGB.VAT",
    "description": "Reduced Rate for UK General Export",
    "taxPercent": 10.02,
    "taxLimit": {
      "minTax": 10,
      "maxTax": 150,
      "minTaxable": 10,
      "maxTaxable": 2000
    },
    "amountToTax": "fullAmount",
    "salesGLAccount": {
      "id": "1200.01--Accounts Receivable - a/c label offset"
    },
    "accountLabel": {
      "id": "Accounting Fees",
      "key": "14"
    },
    "taxAuthority": {
      "id": "California",
      "key": "24",
      "href": "/objects/tax/tax-authority/24"
    },
    "status": "active",
    "isSystemGenerated": false,
    "reverseCharge": false,
    "germanTaxDetailKey": null,
    "taxRate": "standard",
    "taxSolution": {
      "id": "United Kingdom - VAT",
      "key": "1",
      "href": "/objects/tax/tax-solution/1"
    },
    "useExpenseAccount": false,
    "href": "/objects/tax/order-entry-tax-detail/308"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/tax/order-entry-tax-detail/{key}
_Update an Order Entry tax detail_

**Request example — Update an Order Entry tax detail:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated Order Entry tax detail:**
```json
{
  "ia::result": {
    "key": "308",
    "id": "UK General Export Reduced Rate",
    "href": "/objects/tax/order-entry-tax-detail/308"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/tax/order-entry-tax-detail/{key}
_Delete an Order Entry tax detail_


## GET /objects/tax/order-entry-tax-schedule
_List Order Entry tax schedules_

**Response 200 — List Order Entry tax schedules:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "8",
      "href": "/objects/tax/order-entry-tax-schedule/8"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/tax/order-entry-tax-schedule/9"
    },
    {
      "key": "10",
      "id": "10",
      "href": "/objects/tax/order-entry-tax-schedule/10"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/tax/order-entry-tax-schedule
_Create an Order Entry tax schedule_

**Request example — Create an Order Entry tax schedule:**
```json
{
  "name": "TaxSched-00004",
  "description": "Sales Tax for New York",
  "taxSolution": {
    "key": 10
  },
  "status": "active",
  "lines": [
    {
      "taxDetail": {
        "id": "New York Sales Tax"
      },
      "effectiveDate": "2022-02-26"
    }
  ]
}
```
**Response 201 — New Order Entry tax schedule:**
```json
{
  "ia::result": {
    "key": "308",
    "id": "308",
    "href": "/objects/tax/order-entry-tax-schedule/308"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/order-entry-tax-schedule-detail
_List Order Entry tax schedule details_

**Response 200 — List Order Entry tax schedule details:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "8",
      "href": "/objects/tax/order-entry-tax-schedule-detail/8"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/tax/order-entry-tax-schedule-detail/9"
    },
    {
      "key": "10",
      "id": "10",
      "href": "/objects/tax/order-entry-tax-schedule-detail/10"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/tax/order-entry-tax-schedule-detail/{key}
_Get an Order Entry tax schedule detail_

**Response 200 — Get an Order Entry tax schedule detail:**
```json
{
  "ia::result": {
    "taxSchedule": {
      "key": "162",
      "id": "162",
      "name": "Tax Florida",
      "href": "/objects/tax/order-entry-tax-schedule/162"
    },
    "key": "44",
    "id": "44",
    "taxDetail": {
      "id": "Sales Tax California",
      "key": "22",
      "href": "/objects/tax/order-entry-tax-detail/22"
    },
    "effectiveDate": "2022-02-03",
    "href": "/objects/tax/order-entry-tax-schedule-detail/44"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/order-entry-tax-schedule/{key}
_Get an Order Entry tax schedule_

**Response 200 — Get an Order Entry tax schedule:**
```json
{
  "ia::result": {
    "id": "162",
    "name": "Sales Tax New York",
    "key": "162",
    "description": "Sales Tax for New York",
    "status": "active",
    "isSystemGenerated": false,
    "taxSolution": {
      "id": "Avalara Tax",
      "key": "1",
      "href": "/objects/tax/tax-solution/1"
    },
    "lines": [
      {
        "taxSchedule": {
          "key": "162",
          "id": "162",
          "name": "Sales Tax New York",
          "href": "/objects/tax/order-entry-tax-schedule/162"
        },
        "key": "44",
        "id": "44",
        "taxDetail": {
          "id": "New York State Sales Tax",
          "key": "22",
          "href": "/objects/tax/order-entry-tax-detail/22"
        },
        "effectiveDate": "2022-02-03",
        "href": "/objects/tax/order-entry-tax-schedule-detail/44"
      }
    ],
    "href": "/objects/tax/order-entry-tax-schedule/162"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/tax/order-entry-tax-schedule/{key}
_Update an Order Entry tax schedule_

**Request example — Update a single value:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Updated order entry tax schedule:**
```json
{
  "ia::result": {
    "key": "162",
    "href": "/objects/tax/order-entry-tax-schedule/162"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/tax/order-entry-tax-schedule/{key}
_Delete an Order Entry tax schedule_


## GET /objects/tax/purchasing-tax-detail
_List Purchasing tax details_

**Response 200 — List Purchasing tax details:**
```json
{
  "ia::result": [
    {
      "key": "4",
      "id": "State Tax Arkansas",
      "href": "/objects/tax/purchasing-tax-detail/4"
    },
    {
      "key": "2",
      "id": "State Tax Alaska",
      "href": "/objects/tax/purchasing-tax-detail/2"
    },
    {
      "key": "3",
      "id": "State Tax Arizona",
      "href": "/objects/tax/purchasing-tax-detail/3"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/tax/purchasing-tax-detail
_Create a Purchasing tax detail_

**Request example — Create a new Purchasing tax detail:**
```json
{
  "id": "UK Import Services Standard Rate",
  "taxUniqueId": "GB.ECOutput_GB.ExemptGB.VAT",
  "description": "Standard Rate for UK Import Services",
  "taxPercent": 10.02,
  "taxLimit": {
    "minTax": 10,
    "maxTax": 150,
    "minTaxable": 10,
    "maxTaxable": 2000
  },
  "amountToTax": "fullAmount",
  "purchaseGLAccount": {
    "id": "1200.01"
  },
  "taxAuthority": {
    "id": "California"
  },
  "taxSolution": {
    "id": "United Kingdom - VAT"
  },
  "status": "active",
  "taxRate": "standard",
  "useExpenseAccount": false
}
```
**Response 201 — New Purchasing tax detail:**
```json
{
  "ia::result": {
    "key": "304",
    "id": "Purchasing Tax Detail New",
    "href": "/objects/tax/purchasing-tax-detail/304"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/purchasing-tax-detail/{key}
_Get a Purchasing tax detail_

**Response 200 — Get a Purchasing tax detail:**
```json
{
  "ia::result": {
    "key": "304",
    "id": "UK Import Services Standard Rate",
    "taxUniqueId": "GB.ECOutput_GB.ExemptGB.VAT",
    "description": "Standard Rate for UK Import Services",
    "taxPercent": 10.02,
    "taxLimit": {
      "minTax": 10,
      "maxTax": 150,
      "minTaxable": 10,
      "maxTaxable": 2000
    },
    "amountToTax": "fullAmount",
    "purchaseGLAccount": {
      "id": "1200.01--Accounts Receivable - a/c label offset",
      "key": "57",
      "href": "/objects/account/57"
    },
    "taxAuthority": {
      "id": "California",
      "key": "24",
      "href": "/objects/tax/tax-authority/24"
    },
    "status": "active",
    "isSystemGenerated": false,
    "reverseCharge": false,
    "germanTaxDetailKey": null,
    "taxRate": "standard",
    "taxSolution": {
      "id": "United Kingdom - VAT",
      "key": "1",
      "href": "/objects/tax/tax-solution/1"
    },
    "useExpenseAccount": false,
    "href": "/objects/tax/purchasing-tax-detail/304"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/tax/purchasing-tax-detail/{key}
_Update a Purchasing tax detail_

**Request example — Update a Purchasing tax detail:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Updated Purchasing tax detail:**
```json
{
  "ia::result": {
    "key": "304",
    "id": "UK Import Services Standard Rate",
    "href": "/objects/tax/purchasing-tax-detail/304"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/tax/purchasing-tax-detail/{key}
_Delete a Purchasing tax detail_


## GET /objects/tax/purchasing-tax-schedule
_List Purchasing tax schedules_

**Response 200 — List Purchasing tax schedules:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/tax/purchasing-tax-schedule/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/tax/purchasing-tax-schedule/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/tax/purchasing-tax-schedule/3"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/tax/purchasing-tax-schedule
_Create a Purchasing tax schedule_

**Request example — Create a Purchasing tax schedule:**
```json
{
  "name": "TaxSched-00005",
  "description": "Purchase Tax for New York City",
  "taxSolution": {
    "key": 10
  },
  "status": "active",
  "lines": [
    {
      "taxDetail": {
        "id": "New York City Sales Tax"
      },
      "effectiveDate": "2022-02-26"
    }
  ]
}
```
**Response 201 — New Purchasing tax schedule:**
```json
{
  "ia::result": {
    "key": "308",
    "id": "308",
    "href": "/objects/tax/purchasing-tax-schedule/308"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/purchasing-tax-schedule-detail
_List Purchasing tax schedule details_

**Response 200 — List Purchasing tax schedule details:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "8",
      "href": "/objects/tax/purchasing-tax-schedule-detail/8"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/tax/purchasing-tax-schedule-detail/9"
    },
    {
      "key": "10",
      "id": "10",
      "href": "/objects/tax/purchasing-tax-schedule-detail/10"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/tax/purchasing-tax-schedule-detail/{key}
_Get a Purchasing tax schedule detail_

**Response 200 — Get a Purchasing tax schedule detail:**
```json
{
  "ia::result": {
    "taxSchedule": {
      "key": "162",
      "id": "162",
      "name": "Tax Florida",
      "href": "/objects/tax/purchasing-tax-schedule/162"
    },
    "key": "44",
    "id": "44",
    "taxDetail": {
      "id": "Sales Tax California",
      "key": "22",
      "href": "/objects/tax/purchasing-tax-detail/22"
    },
    "effectiveDate": "2022-02-03",
    "href": "/objects/tax/purchasing-tax-schedule-detail/44"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/purchasing-tax-schedule/{key}
_Get a Purchasing tax schedule_

**Response 200 — Get a Purchasing tax schedule:**
```json
{
  "ia::result": {
    "name": "Tax Florida",
    "id": "165",
    "key": "165",
    "description": "Purchase tax for Florida",
    "status": "active",
    "isSystemGenerated": false,
    "taxSolution": {
      "id": "Avalara Tax",
      "key": "1",
      "href": "/objects/tax/tax-solution/1"
    },
    "lines": [
      {
        "taxSchedule": {
          "key": "165",
          "id": "165",
          "name": "Tax Florida",
          "href": "/objects/tax/purchasing-tax-schedule/165"
        },
        "key": "44",
        "id": "44",
        "taxDetail": {
          "id": "Sales Tax Florida",
          "key": "22",
          "href": "/objects/tax/purchasing-tax-detail/22"
        },
        "effectiveDate": "2022-02-03",
        "href": "/objects/tax/purchasing-tax-schedule-detail/44"
      }
    ],
    "href": "/objects/tax/purchasing-tax-schedule/167"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/tax/purchasing-tax-schedule/{key}
_Update a Purchasing tax schedule_

**Request example — Update a single value:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Updated Purchasing tax schedule:**
```json
{
  "ia::result": {
    "key": "162",
    "href": "/objects/tax/purchasing-tax-schedule/162"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/tax/purchasing-tax-schedule/{key}
_Delete a Purchasing tax schedule_


## GET /objects/tax/tax-authority
_List tax authorities_

**Response 200 — List tax authorities:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "Alaska",
      "href": "/objects/tax/tax-authority/2"
    },
    {
      "key": "5",
      "id": "California",
      "href": "/objects/tax/tax-authority/5"
    },
    {
      "key": "3",
      "id": "Arizona",
      "href": "/objects/tax/tax-authority/3"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/tax/tax-authority
_Create a tax authority_

**Request example — Create a tax authority:**
```json
{
  "id": "Texas",
  "description": "Texas tax authority",
  "vendorId": "Vendor_Visa_C",
  "parent": {
    "id": "5"
  }
}
```
**Response 201 — Create a tax authority:**
```json
{
  "ia::result": {
    "key": "105",
    "id": "Texas",
    "href": "/objects/tax/tax-authority/105"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/tax/tax-authority/{key}
_Get a tax authority_

**Response 200 — Get a tax authority:**
```json
{
  "ia::result": {
    "key": "105",
    "id": "Texas",
    "description": "Texas tax authority",
    "vendorId": "Vendor_Visa_C",
    "parent": {
      "name": "California",
      "href": "/objects/tax/tax-authority/24"
    },
    "href": "/objects/tax/tax-authority/105"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/tax/tax-authority/{key}
_Update a tax authority_

**Request example — Update a tax authority:**
```json
{
  "description": "Updated description"
}
```
**Response 200 — Updated tax authority:**
```json
{
  "ia::result": {
    "key": "105",
    "id": "Texas",
    "href": "/objects/tax/tax-authority/105"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/tax/tax-authority/{key}
_Delete a tax authority_


## GET /objects/tax/tax-detail
_List tax details_

**Response 200 — List tax details:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "CGST",
      "href": "/objects/tax/tax-detail/1"
    },
    {
      "key": "2",
      "id": "SGST",
      "href": "/objects/tax/tax-detail/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/tax/tax-detail/{key}
_Get a tax detail_

**Response 200 — Get a tax detail:**
```json
{
  "ia::result": {
    "key": "29",
    "id": "SGST",
    "taxUniqueId": "AU.InputCapitalPurchase.StandardAU.GST",
    "description": "G10 Capital Acquisition SGST",
    "taxType": "purchase",
    "taxPercent": "10.00",
    "taxLimit": {
      "minTaxable": 10,
      "maxTaxable": 2000,
      "minTax": 10,
      "maxTax": 150
    },
    "amountToTax": "fullAmount",
    "glAccount": {
      "id": "6850.03--Taxes"
    },
    "taxAuthority": {
      "id": ""
    },
    "status": "active",
    "isSystemGenerated": false,
    "reverseCharge": false,
    "germanTaxDetailKey": null,
    "taxRate": null,
    "taxSolution": {
      "id": "Australia - GST",
      "key": "3",
      "href": "/objects/tax/tax-solution/3"
    },
    "useExpenseAccount": false,
    "href": "/objects/tax/tax-detail/29"
  }
}
```

## GET /objects/tax/tax-record
_List tax records_

**Response 200 — List tax records:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/tax/tax-record/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/tax/tax-record/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/tax/tax-record/{key}
_Get a tax record_

**Response 200 — Details of the tax record:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "txnInformation": {
      "txnDate": "2024-08-26",
      "label": "Demo_bill_1111",
      "txnType": "apbill",
      "currency": {
        "txnCurrency": "AUD",
        "baseCurrency": "AUD",
        "exchangeRate": 1,
        "exchangeRateDate": "2024-08-16",
        "sourceAmount": "800.00",
        "taxAmount": "80.00"
      },
      "txnId": "PR_2"
    },
    "taxPointDate": "2024-08-26",
    "description": "demo bill",
    "journalEntry": {
      "key": "2",
      "id": "2",
      "href": "/objects/general-ledger/journal-entry/2"
    },
    "sourceJournalEntryLine": {
      "id": "6",
      "key": "6",
      "href": "/objects/general-ledger/journal-entry-line/6"
    },
    "taxJournalEntryLine": {
      "id": "8",
      "key": "8",
      "href": "/objects/general-ledger/journal-entry-line/8"
    },
    "taxDetail": {
      "key": "28",
      "id": "CGST",
      "taxType": "purchase",
      "taxFiling": "reporting",
      "taxRate": "10.00",
      "taxUniqueId": "AU.InputCapitalPurchase.StandardAU.GST",
      "href": "/objects/tax/tax-detail/28"
    },
    "creditOrDebitTxn": "debit",
    "taxType": "inputTax",
    "sourceAmount": "800.00",
    "taxAmount": "80.00",
    "isFiled": false,
    "isFromReverseTxn": false,
    "state": "posted",
    "customerOrVendorName": "1099 Int",
    "dimensions": {
      "contact": {
        "key": "302",
        "id": "1099 Int",
        "tax": {
          "taxId": "40071007326",
          "isTaxable": true,
          "group": {
            "key": "43",
            "id": "CONTACT_GRP_1",
            "href": "/objects/tax/contact-tax-group/43"
          }
        },
        "mailingAddress": {
          "country": "Australia",
          "isoCountryCode": "AU"
        }
      },
      "department": {
        "key": "3",
        "id": "3",
        "name": "Engineering",
        "href": "/objects/company-config/department/3"
      },
      "location": {
        "key": "24",
        "id": "BB",
        "name": "Brisbane",
        "href": "/objects/company-config/location/24"
      }
    },
    "taxId": "40071007326",
    "isCredit": false,
    "filingDate": "2024-08-26",
    "taxReturn": {
      "id": "61",
      "key": "61",
      "href": "/objects/tax/tax-return/61"
    },
    "isReclaimable": false,
    "capturePaymentTax": false,
    "href": "/objects/tax/tax-record/3",
    "audit": {
      "modifiedDateTime": "2024-08-26T11:14:22Z",
      "createdDateTime": "2024-08-26T11:14:22Z",
      "createdBy": "1",
      "modifiedBy": "1"
    }
  }
}
```

## GET /objects/tax/tax-return
_List tax returns_

**Response 200 — List tax returns:**
```json
{
  "ia::result": [
    {
      "key": "9",
      "id": "9",
      "href": "/objects/tax/tax-return/9"
    },
    {
      "key": "54",
      "id": "54",
      "href": "/objects/tax/tax-return/54"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/tax/tax-return
_Create a tax return_

**Request example — Create a tax return:**
```json
{
  "name": "VAT_Sub",
  "taxSolution": {
    "key": "1"
  },
  "taxId": "445025391",
  "recipientEmail": "apiuser@sage.com"
}
```
**Response 201 — Reference to new tax return:**
```json
{
  "ia::result": {
    "id": "626",
    "key": "626",
    "href": "/objects/tax/tax-return/626"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/tax/tax-return/{key}
_Get a tax return_

**Response 200 — Get a tax return:**
```json
{
  "ia::result": {
    "id": "9",
    "key": "9",
    "name": "Tax return ABCompany Q3",
    "taxId": "30 616 935 623",
    "recipientEmail": "first.last@abcompany.com",
    "submissionPeriodStartDate": "2019-06-01",
    "submissionPeriodEndDate": "2020-02-29",
    "submissionDate": "2020-03-03",
    "submittersEmail": "joe.smith@abcompany.com",
    "legalCountryCode": "au",
    "setEmailAddressAsDefault": true,
    "currentStepStage": "submitToGovernment",
    "currentStepStatus": "completed",
    "adjustmentNotes": "Verified using tax solution",
    "bundleNumber": "891204442498",
    "receiptId": "4c907ee0-a76f-42a7-b582-1a3fb78ae4b8",
    "reportingEntity": {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/entity/1"
    },
    "taxSolution": {
      "id": "Australia - GST",
      "key": "2",
      "href": "/objects/tax/tax-solution/2"
    },
    "submissionType": null,
    "taxProcessingSteps": [
      {
        "stage": "prepareTaxData",
        "status": "completed",
        "description": "11 records eligible for submission.",
        "recentActivityDate": "2020-04-02"
      },
      {
        "stage": "transmitTaxData",
        "status": "completed",
        "description": "Source data successfully transmitted to Sage Regulatory Reporting. Ready to prepare tax return in Regulatory Reporting.",
        "recentActivityDate": "2020-04-03"
      },
      {
        "stage": "prepareTaxReturn",
        "status": "completed",
        "description": "The BAS report was generated. A PDF copy is available in the Related files section of this page.",
        "recentActivityDate": "2020-04-04"
      },
      {
        "stage": "submitToGovernment",
        "status": "completed",
        "description": "Submitted to Government",
        "recentActivityDate": "2020-03-03"
      },
      {
        "stage": "manualAdjustment",
        "status": "notApplicable",
        "description": "Manual Adjustment",
        "recentActivityDate": "2020-03-03"
      }
    ],
    "relatedFiles": [
      {
        "stage": "Prepare source tax data",
        "fileName": "transactions.json",
        "creationDate": "2020-03-03"
      },
      {
        "stage": "Prepare source tax data",
        "fileName": "business_info.json",
        "creationDate": "2020-03-03"
      },
      {
        "stage": "Prepare tax return in Sage Regulatory Reporting",
        "fileName": "detailed_report.csv",
        "creationDate": "2020-03-03"
      },
      {
        "stage": "Prepare tax return in Sage Regulatory Reporting",
        "fileName": "late_tax.csv",
        "creationDate": "2020-03-03"
      },
      {
        "stage": "Submit to government",
        "fileName": "gst_BAS.pdf",
        "creationDate": "2020-03-03"
      },
      {
        "stage": "Submit to government",
        "fileName": "gst_calculation.pdf",
        "creationDate": "2020-03-03"
      },
      {
        "stage": "Submit to government",
        "fileName": "manual_adjustments.csv",
        "creationDate": "2020-03-03"
      },
      {
        "stage": "Submit to government",
        "fileName": "submitted_source_entries",
        "creationDate": "2020-03-03"
      }
    ],
    "href": "/objects/tax/tax-return/9"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/tax/tax-return/{key}
_Update a tax return_

**Request example — Update a tax return:**
```json
{
  "adjustmentNotes": "Tax Submission notes"
}
```
**Response 200 — Reference to updated tax return:**
```json
{
  "ia::result": {
    "key": "105",
    "id": "105",
    "href": "/objects/tax/tax-return/105"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/tax/tax-return/{key}
_Delete a tax return_


## GET /objects/tax/tax-solution
_List tax solutions_

**Response 200 — List tax solutions:**
```json
{
  "ia::result": [
    {
      "key": "265",
      "id": "Oregon",
      "href": "/objects/tax/tax-solution/265"
    },
    {
      "key": "263",
      "id": "Alaska",
      "href": "/objects/tax/tax-solution/263"
    },
    {
      "key": "264",
      "id": "Montana",
      "href": "/objects/tax/tax-solution/264"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/tax/tax-solution/{key}
_Get a tax solution_

**Response 200 — GET:**
```json
{
  "key": "1",
  "id": "Australia - GST",
  "description": "Australian tax solution",
  "taxCalculationMethod": "VAT",
  "status": "active",
  "taxSolutionType": "standard",
  "taxSubmissionStartDate": "2019-05-01",
  "enableMultilineTax": false,
  "purchaseGLAccount": {
    "key": "7",
    "id": "6850.03",
    "href": "/objects/general-ledger/account/23"
  },
  "salesGLAccount": {
    "key": "9",
    "id": "6500.05",
    "href": "/objects/general-ledger/account/13"
  },
  "alternativeSetup": false,
  "lastUpdatedTaxDate": null,
  "href": "/objects/tax/tax-solution/1"
}
```

## DELETE /objects/tax/tax-solution/{key}
_Delete a tax solution_

