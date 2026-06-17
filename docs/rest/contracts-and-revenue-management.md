# Contracts and Revenue Management

## GET /objects/contracts/billing-price-list
_List billing price lists_

**Response 200 — List billing price lists:**
```json
{
  "ia::result": [
    {
      "key": "24",
      "id": "PL-SoftwarePackage",
      "href": "/objects/contracts/billing-price-list/24"
    },
    {
      "key": "37",
      "id": "PL-SoftwareSupport",
      "href": "/objects/contracts/billing-price-list/37"
    },
    {
      "key": "1",
      "id": "PL-SoftwareFinance",
      "href": "/objects/contracts/billing-price-list/1"
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

## POST /objects/contracts/billing-price-list
_Create a billing price list_

**Request example — Create a billing price list:**
```json
{
  "id": "PL-SoftwarePackage",
  "description": "Billing price list for software packages.",
  "status": "active"
}
```
**Response 201 — Reference to new billing price list:**
```json
{
  "ia::result": {
    "key": "30",
    "id": "PL-SoftwarePackage",
    "href": "/objects/contracts/billing-price-list/30"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/billing-price-list-entry
_List billing price list entries_

**Response 200 — List billing price list entries:**
```json
{
  "ia::result": [
    {
      "key": "300",
      "id": "300",
      "href": "/objects/contracts/billing-price-list-entry/300"
    },
    {
      "key": "296",
      "id": "296",
      "href": "/objects/contracts/billing-price-list-entry/296"
    },
    {
      "key": "298",
      "id": "298",
      "href": "/objects/contracts/billing-price-list-entry/298"
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

## POST /objects/contracts/billing-price-list-entry
_Create a billing price list entry_

**Request example — Create a billing price list entry:**
```json
{
  "status": "active",
  "billingPriceList": {
    "key": "1"
  },
  "item": {
    "id": "Software Services"
  },
  "currency": {
    "txnCurrency": "USD"
  },
  "priceType": "tiered",
  "flatAmountFrequency": "useBillingTemplate",
  "variableUnitDivisor": "1",
  "usageQuantityResetPeriod": "afterEachRenewal",
  "isQuantityRecurring": false,
  "tieredPricingType": "volume",
  "lines": [
    {
      "startDate": "2025-01-01",
      "flatAmount": "5900.00",
      "variableUnitRate": "1",
      "includedUnits": "1000",
      "tiers": [
        {
          "beginQuantity": "0",
          "tierRate": "49"
        },
        {
          "beginQuantity": "10001",
          "tierRate": "129"
        },
        {
          "beginQuantity": "30000",
          "tierRate": "150"
        }
      ]
    }
  ]
}
```
**Response 201 — Reference to new billing price list entry:**
```json
{
  "ia::result": {
    "key": "326",
    "id": "326",
    "href": "/objects/contracts/billing-price-list-entry/326"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/billing-price-list-entry-line
_List billing price list entry lines_

**Response 200 — List billing price list entry lines:**
```json
{
  "ia::result": [
    {
      "key": "304",
      "id": "304",
      "href": "/objects/contracts/billing-price-list-entry-line/304"
    },
    {
      "key": "301",
      "id": "301",
      "href": "/objects/contracts/billing-price-list-entry-line/301"
    },
    {
      "key": "302",
      "id": "302",
      "href": "/objects/contracts/billing-price-list-entry-line/302"
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

## GET /objects/contracts/billing-price-list-entry-line-tier
_List billing price list entry line tiers_

**Response 200 — List billing price list entry line tiers:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/billing-price-list-entry-line-tier/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/contracts/billing-price-list-entry-line-tier/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/contracts/billing-price-list-entry-line-tier/3"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/contracts/billing-price-list-entry-line-tier/4"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/contracts/billing-price-list-entry-line-tier
_Create a billing price list entry line tier_

**Request example — Create a billing price list entry line tier:**
```json
{
  "billingPriceListEntryLine": {
    "key": "4"
  },
  "beginQuantity": "0",
  "tierRate": "860"
}
```
**Response 201 — Reference to new billing price list entry line tier:**
```json
{
  "ia::result": {
    "key": "22",
    "id": "22",
    "href": "/objects/contracts/billing-price-list-entry-line-tier/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/billing-price-list-entry-line-tier/{key}
_Get a billing price list entry line tier_

**Response 200 — Get a billing price list entry line tier:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "billingPriceListEntryLine": {
      "key": "4",
      "id": "4",
      "href": "/objects/billing-price-list-entry-line/4"
    },
    "beginQuantity": "0",
    "tierRate": "850",
    "audit": {
      "modifiedDateTime": "2025-01-16T23:12:22Z",
      "createdDateTime": "2025-05-13T18:22:36Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "109",
        "id": "Admin",
        "href": "/objects/company-config/user/109"
      },
      "modifiedBy": "109"
    },
    "href": "/objects/contracts/billing-price-list-entry-line-tier/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/billing-price-list-entry-line-tier/{key}
_Update a billing price list entry line tier_

**Request example — Update a billing price list entry line tier:**
```json
{
  "beginQuantity": "0",
  "tierRate": "850"
}
```
**Response 200 — Reference to updated billing price list entry line tier:**
```json
{
  "ia::result": {
    "key": "32069",
    "id": "32069",
    "href": "/objects/contracts/billing-price-list-entry-line/32069"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/billing-price-list-entry-line-tier/{key}
_Delete a billing price list entry line tier_


## GET /objects/contracts/billing-price-list-entry-line/{key}
_Get a billing price list entry line_

**Response 200 — Get a billing price list entry line:**
```json
{
  "ia::result": {
    "id": "351",
    "key": "351",
    "billingPriceListEntry": {
      "key": "326",
      "id": "326",
      "href": "/objects/contracts/billing-price-list-entry/326"
    },
    "startDate": "2025-01-01",
    "flatAmount": "5900.00",
    "variableUnitRate": "0",
    "includedUnits": "1000",
    "memo": null,
    "audit": {
      "createdDateTime": "2025-10-07T11:47:20Z",
      "modifiedDateTime": "2025-10-07T11:47:20Z",
      "createdByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "createdBy": "159",
      "modifiedByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "modifiedBy": "159"
    },
    "tiers": [
      {
        "id": "71",
        "key": "71",
        "billingPriceListEntryLine": {
          "id": "351",
          "key": "351",
          "href": "/objects/contracts/billing-price-list-entry-line/351"
        },
        "beginQuantity": "0",
        "tierRate": "49",
        "audit": {
          "createdDateTime": "2025-10-07T11:47:20Z",
          "modifiedDateTime": "2025-10-07T11:47:20Z",
          "createdByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "createdBy": "159",
          "modifiedByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "modifiedBy": "159"
        }
      },
      {
        "id": "72",
        "key": "72",
        "billingPriceListEntryLine": {
          "id": "351",
          "key": "351",
          "href": "/objects/contracts/billing-price-list-entry-line/351"
        },
        "beginQuantity": "10001",
        "tierRate": "129",
        "audit": {
          "createdDateTime": "2025-10-07T11:47:20Z",
          "modifiedDateTime": "2025-10-07T11:47:20Z",
          "createdByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "createdBy": "159",
          "modifiedByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "modifiedBy": "159"
        }
      },
      {
        "id": "73",
        "key": "73",
        "billingPriceListEntryLine": {
          "id": "351",
          "key": "351",
          "href": "/objects/contracts/billing-price-list-entry-line/351"
        },
        "beginQuantity": "30000",
        "tierRate": "150",
        "audit": {
          "createdDateTime": "2025-10-07T11:47:20Z",
          "modifiedDateTime": "2025-10-07T11:47:20Z",
          "createdByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "createdBy": "159",
          "modifiedByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "modifiedBy": "159"
        }
      }
    ],
    "href": "/objects/contracts/billing-price-list-entry-line/351"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/billing-price-list-entry-line/{key}
_Update a billing price list entry line_

**Request example — Update a billing price list entry line:**
```json
{
  "startDate": "2025-01-01",
  "flatAmount": "0",
  "variableUnitRate": "1",
  "includedUnits": "9",
  "memo": null,
  "tiers": [
    {
      "key": "121",
      "beginQuantity": "0",
      "tierRate": "850"
    }
  ]
}
```
**Response 200 — Reference to updated billing price list entry line:**
```json
{
  "ia::result": {
    "key": "572",
    "id": "572",
    "href": "/objects/contracts/billing-price-list-entry-line/572"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/billing-price-list-entry-line/{key}
_Delete a billing price list entry line_


## GET /objects/contracts/billing-price-list-entry/{key}
_Get a billing price list entry_

**Response 200 — Get a billing price list entry:**
```json
{
  "ia::result": {
    "id": "326",
    "key": "326",
    "audit": {
      "createdDateTime": "2025-10-07T11:47:20Z",
      "modifiedDateTime": "2025-10-07T11:47:20Z",
      "createdByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "createdBy": "159",
      "modifiedByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "modifiedBy": "159"
    },
    "status": "active",
    "item": {
      "key": "321",
      "id": "Software Services",
      "name": "Software Services - Laptop Setup",
      "href": "/objects/inventory-control/item/321"
    },
    "billingPriceList": {
      "key": "1",
      "id": "SoftwarePackagePL",
      "href": "/objects/contracts/billing-price-list/1"
    },
    "currency": {
      "txnCurrency": "USD"
    },
    "priceType": "tiered",
    "flatAmountFrequency": "useBillingTemplate",
    "variableUnitDivisor": "1",
    "roundingType": null,
    "usageQuantityResetPeriod": "afterEachRenewal",
    "isQuantityRecurring": false,
    "tieredPricingType": "volume",
    "version": null,
    "lines": [
      {
        "id": "351",
        "key": "351",
        "billingPriceListEntry": {
          "id": "326",
          "key": "326",
          "href": "/objects/contracts/billing-price-list-entry/326"
        },
        "startDate": "2025-01-01",
        "flatAmount": "5900.00",
        "variableUnitRate": "0",
        "includedUnits": "1000",
        "memo": null,
        "audit": {
          "createdDateTime": "2025-10-07T11:47:20Z",
          "modifiedDateTime": "2025-10-07T11:47:20Z",
          "createdByUser": {
            "key": "159",
            "href": "/objects/company-config/user/159"
          },
          "createdBy": "159",
          "modifiedByUser": {
            "key": "159",
            "href": "/objects/company-config/user/159"
          },
          "modifiedBy": "159"
        },
        "tiers": [
          {
            "id": "71",
            "key": "71",
            "billingPriceListEntryLine": {
              "id": "351",
              "key": "351",
              "href": "/objects/contracts/billing-price-list-entry-line/351"
            },
            "beginQuantity": "0",
            "tierRate": "49",
            "audit": {
              "createdDateTime": "2025-10-07T11:47:20Z",
              "modifiedDateTime": "2025-10-07T11:47:20Z",
              "createdBy": "159",
              "modifiedBy": "159"
            }
          },
          {
            "id": "72",
            "key": "72",
            "billingPriceListEntryLine": {
              "id": "351",
              "key": "351",
              "href": "/objects/contracts/billing-price-list-entry-line/351"
            },
            "beginQuantity": "10001",
            "tierRate": "129",
            "audit": {
              "createdDateTime": "2025-10-07T11:47:20Z",
              "modifiedDateTime": "2025-10-07T11:47:20Z",
              "createdBy": "159",
              "modifiedBy": "159"
            }
          },
          {
            "id": "73",
            "key": "73",
            "billingPriceListEntryLine": {
              "id": "351",
              "key": "351",
              "href": "/objects/contracts/billing-price-list-entry-line/351"
            },
            "beginQuantity": "30000",
            "tierRate": "150",
            "audit": {
              "createdDateTime": "2025-10-07T11:47:20Z",
              "modifiedDateTime": "2025-10-07T11:47:20Z",
              "createdBy": "159",
              "modifiedBy": "159"
            }
          }
        ],
        "href": "/objects/contracts/billing-price-list-entry-line/351"
      }
    ],
    "href": "/objects/contracts/billing-price-list-entry/326",
    "webURL": "https://app.intacct.com/objects/contracts/billing-price-list-entry/326"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/billing-price-list-entry/{key}
_Update a billing price list entry_

**Request example — Update a billing price list entry:**
```json
{
  "status": "active",
  "currency": {
    "txnCurrency": "USD"
  },
  "priceType": "tiered",
  "flatAmountFrequency": "includeWithEveryInvoice",
  "variableUnitDivisor": "1",
  "roundingType": "standard",
  "usageQuantityResetPeriod": "afterEachInvoice",
  "isQuantityRecurring": true,
  "tieredPricingType": "step",
  "lines": [
    {
      "key": "351",
      "startDate": "2025-08-01",
      "flatAmount": "0",
      "variableUnitRate": "1",
      "includedUnits": "10",
      "memo": null,
      "tiers": [
        {
          "key": "121",
          "beginQuantity": "0",
          "tierRate": "850"
        }
      ]
    }
  ]
}
```
**Response 200 — Reference to updated billing price list entry:**
```json
{
  "ia::result": {
    "key": "326",
    "id": "326",
    "href": "/objects/contracts/billing-price-list-entry/326"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/billing-price-list-entry/{key}
_Delete a/an billing price list entry_


## GET /objects/contracts/billing-price-list/{key}
_Get a billing price list_

**Response 200 — Get a billing price list:**
```json
{
  "ia::result": {
    "key": "30",
    "audit": {
      "createdDateTime": "2025-10-07T10:57:53Z",
      "modifiedDateTime": "2025-10-07T10:57:53Z",
      "createdByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "createdBy": "159",
      "modifiedByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "modifiedBy": "159"
    },
    "status": "active",
    "id": "PL-SoftwarePackage",
    "description": "Billing price list for software packages.",
    "href": "/objects/contracts/billing-price-list/30"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/billing-price-list/{key}
_Update a billing price list_

**Request example — Update billing price list:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated billing price list:**
```json
{
  "ia::result": {
    "key": "30",
    "id": "PL-SoftwarePackage",
    "href": "/objects/contracts/billing-price-list/30"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/billing-price-list/{key}
_Delete a billing price list_


## GET /objects/contracts/billing-schedule
_List billing schedules_

**Response 200 — List billing schedules:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/contracts/billing-schedule/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/contracts/billing-schedule/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/contracts/billing-schedule/60"
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

## GET /objects/contracts/billing-schedule-line
_List billing schedule lines_

**Response 200 — List billing schedule lines:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/contracts/billing-schedule-line/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/contracts/billing-schedule-line/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/contracts/billing-schedule-line/60"
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

## GET /objects/contracts/billing-schedule-line/{key}
_Get a billing schedule line_

**Response 200 — Get a billing schedule line:**
```json
{
  "ia::result": {
    "id": "1243",
    "key": "1243",
    "contractBillingSchedule": {
      "id": "147",
      "key": "147",
      "href": "/objects/contracts/billing-schedule/147"
    },
    "scheduledOperationKey": null,
    "scheduledAmount": "2400.00",
    "scheduledBaseAmount": "2400.00",
    "actualBaseAmount": null,
    "scheduledExchangeRate": "1.000000000000",
    "actualExchangeRate": null,
    "scheduledBillingDate": "2025-01-01",
    "actualBillingDate": null,
    "billed": false,
    "isHistorical": false,
    "state": "open",
    "computationMemo": null,
    "approvedHours": null,
    "sourceHours": null,
    "linkedBillingScheduleLine": {
      "id": null,
      "key": null
    },
    "documentId": null,
    "audit": {
      "createdDateTime": "2025-11-02T19:48:54Z",
      "modifiedDateTime": "2025-03-28T04:14:00Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "contractUsage": {
      "id": null,
      "key": null
    },
    "servicePeriodStartDate": null,
    "servicePeriodEndDate": null,
    "href": "/objects/contracts/billing-schedule-line/1243"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/billing-schedule/{key}
_Get a billing schedule_

**Response 200 — Get a billing schedule:**
```json
{
  "ia::result": {
    "key": "1576",
    "id": "1576",
    "contract": {
      "key": "143",
      "id": "Committed_Quantity_Billing",
      "href": "/objects/contracts/contract/143"
    },
    "contractLine": {
      "id": "387",
      "key": "387",
      "href": "/objects/contracts/contract-line/387"
    },
    "status": "inProgress",
    "cancellationDate": null,
    "audit": {
      "createdDateTime": "2025-12-26T15:33:18Z",
      "modifiedDateTime": "2025-12-26T15:33:18Z",
      "createdByUser": {
        "key": "1",
        "id": "1",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "1",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "estimateRevaluationDate": null,
    "lines": [
      {
        "key": "14421",
        "id": "14421",
        "contractBillingSchedule": {
          "id": "1576",
          "key": "1576",
          "href": "/objects/contracts/billing-schedule/1576"
        },
        "scheduledOperationKey": null,
        "scheduledAmount": "200000.00",
        "scheduledBaseAmount": "200000.00",
        "actualBaseAmount": null,
        "scheduledExchangeRate": "1.000000000000",
        "actualExchangeRate": null,
        "scheduledBillingDate": "2025-01-01",
        "actualBillingDate": null,
        "billed": false,
        "isHistorical": false,
        "state": "open",
        "computationMemo": null,
        "approvedHours": null,
        "sourceHours": null,
        "linkedBillingScheduleLine": {
          "id": null,
          "key": null
        },
        "documentId": null,
        "audit": {
          "createdDateTime": "2025-12-26T15:33:18Z",
          "modifiedDateTime": "2025-12-26T15:33:18Z",
          "createdByUser": {
            "key": "1",
            "id": "1",
            "href": "/objects/company-config/user/1"
          },
          "createdBy": "1",
          "modifiedByUser": {
            "key": "1",
            "id": "1",
            "href": "/objects/company-config/user/1"
          },
          "modifiedBy": "1"
        },
        "contractUsage": {
          "id": null,
          "key": null
        },
        "servicePeriodStartDate": "2025-01-01",
        "servicePeriodEndDate": "2025-01-31",
        "href": "/objects/contracts/billing-schedule-line/14421"
      }
    ],
    "href": "/objects/contracts/billing-schedule/1576"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/billing-schedule/{key}
_Update a billing schedule_

**Request example — Update a billing schedule:**
```json
{
  "lines": [
    {
      "key": "12",
      "scheduledBillingDate": "2025-05-25",
      "scheduledAmount": "125.34"
    }
  ]
}
```
**Request example — Update multiple lines for a billing schedule:**
```json
{
  "lines": [
    {
      "key": "12",
      "scheduledBillingDate": "2025-05-25",
      "scheduledAmount": "125.34"
    },
    {
      "key": "13",
      "scheduledBillingDate": "2025-06-25",
      "scheduledAmount": "245.18"
    }
  ]
}
```
**Request example — Update service period dates for a billing schedule:**
```json
{
  "lines": [
    {
      "key": "1423189",
      "servicePeriodStartDate": "2025-05-10",
      "servicePeriodEndDate": "2025-05-31"
    },
    {
      "key": "1423191",
      "servicePeriodStartDate": "2025-07-01",
      "servicePeriodEndDate": "2025-07-31"
    }
  ]
}
```
**Request example — Add a new line to a billing schedule:**
```json
{
  "lines": [
    {
      "scheduledBillingDate": "2025-05-25",
      "scheduledAmount": "125.34"
    }
  ]
}
```
**Request example — Delete a line from a billing schedule:**
```json
{
  "lines": [
    {
      "key": "12",
      "ia::operation": "delete"
    }
  ]
}
```
**Response 200 — Reference to updated billing schedule:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "12",
    "href": "/objects/contracts/billing-schedule/12"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/contracts/billing-template
_List billing templates_

**Response 200 — List billing templates:**
```json
{
  "ia::result": [
    {
      "key": "7",
      "id": "202AN4PER_QUARTERLY",
      "href": "/objects/contracts/billing-template/7"
    },
    {
      "key": "19",
      "id": "18M_Straitline_Beg",
      "href": "/objects/contracts/billing-template/19"
    },
    {
      "key": "14",
      "id": "4P_25PER_MBEGIN",
      "href": "/objects/contracts/billing-template/14"
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

## POST /objects/contracts/billing-template
_Create a billing template_

**Request example — Create a billing template:**
```json
{
  "id": "202AN4PER_QUARTERLY",
  "description": "Custom percent billing beginning of 3,6,9,12 periods",
  "status": "active",
  "method": "predefinedPercentages",
  "source": "estimatedHours",
  "isStepBilling": false,
  "lines": [
    {
      "periodOffset": "3",
      "percentToBill": "5",
      "stepPercent": null
    },
    {
      "periodOffset": "6",
      "percentToBill": "25",
      "stepPercent": null
    },
    {
      "periodOffset": "9",
      "percentToBill": "45",
      "stepPercent": null
    },
    {
      "periodOffset": "12",
      "percentToBill": "25",
      "stepPercent": null
    }
  ]
}
```
**Response 201 — Reference to new billing template:**
```json
{
  "ia::result": {
    "key": "22",
    "id": "202AN4PER_QUARTERLY",
    "href": "/objects/contracts/billing-template/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/billing-template-line
_List billing template lines_

**Response 200 — Example-1:**
```json
{
  "ia::result": [
    {
      "key": "7",
      "id": "7",
      "href": "/objects/contracts/billing-template-line/7"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/contracts/billing-template-line/{key}
_Get a billing template line_

**Response 200 — Get a billing template line:**
```json
{
  "ia::result": {
    "key": "7",
    "contractBillingTemplate": {
      "key": "37",
      "id": "37",
      "href": "/objects/contracts/billing-template/37"
    },
    "periodOffset": "1",
    "stepPercent": "1.00000000",
    "percentToBill": "50.00000000",
    "href": "/objects/contracts/billing-template-line/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/billing-template/{key}
_Get a billing template_

**Response 200 — Get a billing template:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "50_6PRD_12PRD",
    "description": "Billing twice for the contract",
    "status": "inactive",
    "method": "predefinedPercentages",
    "source": "estimatedHours",
    "isStepBilling": false,
    "audit": {
      "modifiedDateTime": "2025-01-16T23:12:22Z",
      "createdDateTime": "2025-05-13T18:22:36Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "lines": [
      {
        "id": "55",
        "key": "55",
        "contractBillingTemplate": {
          "key": "10",
          "href": "/objects/contracts/billing-template/10"
        },
        "periodOffset": "5",
        "percentToBill": "50.00000000",
        "stepPercent": null,
        "href": "/objects/contracts/billing-template-line/55"
      },
      {
        "id": "56",
        "key": "56",
        "contractBillingTemplate": {
          "key": "10",
          "href": "/objects/contracts/billing-template/10"
        },
        "periodOffset": "11",
        "percentToBill": "50.00000000",
        "stepPercent": null,
        "href": "/objects/contracts/billing-template-line/56"
      }
    ],
    "href": "/objects/contracts/billing-template/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/billing-template/{key}
_Update a billing template_

**Request example — Update a billing template:**
```json
{
  "description": "Custom percent billing beginning of 3,6,9,12 periods",
  "status": "active",
  "method": "predefinedPercentages",
  "source": "estimatedHours",
  "isStepBilling": false,
  "lines": [
    {
      "key": "135",
      "periodOffset": "3",
      "percentToBill": "30",
      "stepPercent": null
    },
    {
      "key": "136",
      "periodOffset": "6",
      "percentToBill": "5",
      "stepPercent": null
    },
    {
      "key": "137",
      "periodOffset": "9",
      "percentToBill": "40",
      "stepPercent": null
    },
    {
      "key": "138",
      "periodOffset": "12",
      "percentToBill": "25",
      "stepPercent": null
    }
  ]
}
```
**Response 200 — Reference to updated billing template:**
```json
{
  "ia::result": {
    "key": "22",
    "id": "202AN4PER_QUARTERLY",
    "href": "/objects/contracts/billing-template/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/billing-template/{key}
_Delete a billing template_


## GET /objects/contracts/bulk-action-run-summary
_List bulk action run summaries_

**Response 200 — List bulk action run summaries:**
```json
{
  "ia::result": [
    {
      "key": "20",
      "id": "20",
      "href": "/objects/contracts/bulk-action-run-summary/20"
    },
    {
      "key": "14",
      "id": "14",
      "href": "/objects/contracts/bulk-action-run-summary/14"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/contracts/bulk-action-run-summary/9"
    },
    {
      "key": "13",
      "id": "13",
      "href": "/objects/contracts/bulk-action-run-summary/13"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/contracts/bulk-action-run-summary/{key}
_Get a bulk action run summary_

**Response 200 — Get a bulk action run summary:**
```json
{
  "ia::result": {
    "id": "7",
    "key": "7",
    "bulkActionRunType": "postRevenue",
    "executionMode": "offline",
    "location": {
      "key": "1",
      "id": "1",
      "name": "United States of America",
      "href": "/objects/company-config/location/1"
    },
    "entity": {
      "key": "1",
      "id": "1",
      "name": "United States of America",
      "href": "/objects/company-config/entity/1"
    },
    "runCount": {
      "inProgress": 0,
      "failure": 0,
      "success": 2,
      "queued": 0,
      "total": 2
    },
    "description": "Post revenue recognition for ASC-606",
    "audit": {
      "createdDateTime": "2024-02-09T02:16:40Z",
      "modifiedDateTime": "2024-02-09T00:00:00Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/contracts/bulk-action-run-summary/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/compliance-checklist-task
_List compliance checklist tasks_

**Response 200 — List compliance checklist tasks:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/compliance-checklist-task/1"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/contracts/compliance-checklist-task
_Create a compliance checklist task_

**Request example — Create a compliance checklist task:**
```json
{
  "id": "23",
  "contractComplianceTask": {
    "key": "2"
  },
  "completionDate": "2026-01-15",
  "isSignedOff": false,
  "contractKey": 1,
  "comment": "Completed monthly compliance review for vendor agreements - ASC 606.",
  "completedBy": {
    "id": "rkincaid"
  }
}
```
**Response 201 — Create a compliance checklist task:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "23",
    "href": "/objects/contracts/compliance-checklist-task/23"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/compliance-checklist-task/{key}
_Get a compliance checklist task_

**Response 200 — Get a compliance checklist task:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "contractComplianceTask": {
      "id": "23",
      "key": "23",
      "name": "Contract Compliance Review - Vendor Agreements ASC 606",
      "taskNumber": 1,
      "description": "Task for monthly review of vendor agreements for ASC 606 compliance.",
      "status": true,
      "href": "/objects/contracts/compliance-task/23"
    },
    "completedBy": {
      "id": "rkincaid",
      "key": "24",
      "primaryContact": {
        "lastName": "Nelon"
      },
      "href": "/objects/company-config/employee/24"
    },
    "completionDate": "2026-02-15",
    "isSignedOff": true,
    "contractKey": 1,
    "comment": "Completed monthly compliance review for vendor agreements - ASC 606 - February 2026.",
    "audit": {
      "createdDateTime": "2026-02-15T15:33:18Z",
      "modifiedDateTime": "2026-02-15T15:33:18Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "href": "/objects/contracts/compliance-checklist-task/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/compliance-checklist-task/{key}
_Update a compliance checklist task_

**Request example — Update a compliance checklist task:**
```json
{
  "completionDate": "2026-03-15",
  "isSignedOff": false,
  "comment": "Completed monthly compliance review for vendor agreements - ASC 606 - March 2026.",
  "completedBy": {
    "id": "rkincaid"
  }
}
```
**Response 200 — Reference to compliance checklist task:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/contracts/compliance-checklist-task/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/compliance-checklist-task/{key}
_Delete a compliance checklist task_


## GET /objects/contracts/compliance-note
_List compliance notes_

**Response 200 — List compliance notes:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/compliance-note/1"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/contracts/compliance-note/5"
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

## POST /objects/contracts/compliance-note
_Create a compliance note_

**Request example — Create a compliance note:**
```json
{
  "id": "2",
  "note": "Monthly compliance review completed with no issues.",
  "isPublic": true,
  "contractKey": 1,
  "status": "active"
}
```
**Response 201 — Create a compliance note:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "href": "/objects/contracts/compliance-note/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/compliance-note/{key}
_Get a compliance note_

**Response 200 — Reference to compliance note:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "note": "Monthly compliance review completed with no issues.",
    "isPublic": true,
    "status": "active",
    "contractKey": 1,
    "audit": {
      "createdDateTime": "2026-02-15T15:33:18Z",
      "modifiedDateTime": "2026-02-15T15:33:18Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "lastUpdatedBy": {
      "key": "1",
      "id": "Admin",
      "href": "/objects/company-config/user/1"
    },
    "href": "/objects/contracts/compliance-note/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/compliance-note/{key}
_Update a compliance note_

**Request example — Updates a compliance note:**
```json
{
  "note": "Monthly compliance review completed with no issues - ASC 606 - February 2026.",
  "isPublic": false,
  "status": "active"
}
```
**Response 200 — Reference to compliance note:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "href": "/objects/contracts/compliance-note/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/compliance-note/{key}
_Delete a compliance note_


## GET /objects/contracts/compliance-task
_List compliance tasks_

**Response 200 — List compliance tasks:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/compliance-task/1"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/contracts/compliance-task
_Create a compliance task_

**Request example — Creates a compliance task:**
```json
{
  "id": "3",
  "name": "Monthly compliance review - vendor agreements - ASC 606 - February 2026",
  "description": "Review of vendor agreements for monthly compliance as detailed in contract ASC 606.",
  "taskNumber": 12,
  "status": "active"
}
```
**Response 201 — Create a compliance task:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "href": "/objects/contracts/compliance-task/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/compliance-task/{key}
_Get a compliance task_

**Response 200 — Reference to compliance task:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "name": "Monthly compliance review - vendor agreements - ASC 606 - February 2026",
    "description": "Review of vendor agreements for monthly compliance as detailed in contract ASC 606.",
    "taskNumber": 1,
    "status": "active",
    "audit": {
      "modifiedDateTime": "2026-02-15T08:09:35Z",
      "createdDateTime": "2026-02-15T08:09:35Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "href": "/objects/contracts/compliance-task/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/compliance-task/{key}
_Update a compliance task_

**Request example — Update a compliance task:**
```json
{
  "name": "Monthly compliance review - vendor agreements - ASC 606 - March 2026",
  "description": "Review of vendor agreements for monthly compliance as detailed in contract ASC 606, updated for March 2026.",
  "taskNumber": 13
}
```
**Response 200 — Reference to compliance task:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "href": "/objects/contracts/compliance-task/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/compliance-task/{key}
_Delete a compliance task_


## GET /objects/contracts/contract
_List contracts_

**Response 200 — List contracts:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/contracts/contract/84"
    },
    {
      "key": "107",
      "id": "107",
      "href": "/objects/contracts/contract/107"
    },
    {
      "key": "108",
      "id": "108",
      "href": "/objects/contracts/contract/108"
    },
    {
      "key": "56",
      "id": "56",
      "href": "/objects/contracts/contract/56"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/contracts/contract
_Create a contract_

**Request example — Create a contract:**
```json
{
  "id": "ProjectTime_Completed_Flows34_45_4",
  "startDate": "2025-01-01",
  "endDate": "2025-12-31",
  "name": "ProjectTime_Completed_Flows",
  "dimensions": {
    "customer": {
      "key": "6"
    },
    "location": {
      "key": "1"
    },
    "department": {
      "key": "11"
    }
  },
  "currency": {
    "baseCurrency": "USD",
    "txnCurrency": "USD",
    "exchangeRateType": "Intacct Daily Rate"
  },
  "paymentTerm": {
    "key": "1"
  }
}
```
**Response 201 — Reference to new contract:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "ProjectTime_Completed_Flows34_45_4",
    "href": "/objects/contracts/contract/124"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/contract-group
_List contract groups_

**Response 200 — List contract groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "12434444",
      "href": "/objects/contracts/contract-group/1"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/contracts/contract-group
_Create a contract group_

**Request example — Create a contract group:**
```json
{
  "id": "CG-NA-RENEW-2026-001",
  "name": "Enterprise SaaS Annual Renewals - North America",
  "description": "Contains active enterprise SaaS contracts in North America that are due for annual renewal in the current fiscal year.",
  "groupType": "all",
  "memberFilter": {
    "object": "contracts/contract",
    "filterExpression": "and",
    "filters": [
      {
        "$eq": {
          "id": "CONT-128"
        }
      }
    ],
    "orderBy": [
      {
        "id": "asc"
      }
    ]
  }
}
```
**Response 201 — Create a contract group:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "CG-NA-RENEW-2026-001",
    "href": "/objects/contracts/contract-group/23"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/contract-group-member
_List contract group members_

**Response 200 — List contract group members:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/contract-group-member/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/contracts/contract-group-member/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/contracts/contract-group-member/{key}
_Get a contract group member_

**Response 200 — Get a contract group member:**
```json
{
  "ia::result": {
    "id": "11",
    "key": "11",
    "contractGroup": {
      "key": "5",
      "id": "5",
      "href": "/objects/contracts/contract-group/5"
    },
    "sortOrder": "0",
    "contract": {
      "key": "22",
      "id": "CONT-2026-EMEA-00427",
      "name": "Enterprise Software Subscription and Support Agreement - EMEA - FY2026 Renewal",
      "href": "/objects/contracts/contract/22"
    },
    "audit": {
      "createdDateTime": "2026-01-22T02:33:32Z",
      "modifiedDateTime": "2026-01-22T02:33:32Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "href": "/objects/contracts/contract-group-member/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/contract-group/{key}
_Get a contract group_

**Response 200 — Get a contract group:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "CG-NA-RENEW-2026-001",
    "entity": {
      "key": "2",
      "id": "2",
      "name": "North America",
      "href": "/objects/company-config/entity/2"
    },
    "name": "Enterprise SaaS Annual Renewals - North America",
    "description": "Contains active enterprise SaaS contracts in North America that are due for annual renewal in the current fiscal year.",
    "groupType": "all",
    "memberFilter": {
      "object": "contracts/contract",
      "filterExpression": "and",
      "filters": [
        {
          "$eq": {
            "id": "CONT-128"
          }
        }
      ],
      "orderBy": [
        {
          "id": "asc"
        }
      ]
    },
    "audit": {
      "createdDateTime": "2026-01-22T02:33:32Z",
      "modifiedDateTime": "2026-01-22T02:33:32Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "groupMembers": [],
    "href": "/objects/contracts/contract-group/23"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/contract-group/{key}
_Update a contract group_

**Request example — Update a contract group:**
```json
{
  "description": "Contains active enterprise SaaS contracts in North America that are due for quarterly renewal in the current fiscal year."
}
```
**Response 200 — Reference to contract group:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "CG-NA-RENEW-2026-001",
    "href": "/objects/contracts/contract-group/23"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/contract-group/{key}
_Delete a contract group_


## GET /objects/contracts/contract-line
_List contract lines_

**Response 200 — List contract lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/contract-line/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/contracts/contract-line/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/contracts/contract-line/3"
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

## POST /objects/contracts/contract-line
_Create a contract line_

**Request example — Create a contract line:**
```json
{
  "contract": {
    "key": "2001"
  },
  "item": {
    "key": "221"
  },
  "dimensions": {
    "location": {
      "key": "1"
    }
  },
  "startDate": "2025-02-01",
  "endDate": "2025-11-30",
  "billing": {
    "quantity": "12",
    "rate": "12",
    "multiplier": "1",
    "discount": "0",
    "method": "fixedPrice",
    "amountFrequency": "includeWithEveryInvoice",
    "frequency": "monthly",
    "flatFixedAmount": "144",
    "baseFlatFixedAmount": "144"
  },
  "changeType": "newMRR",
  "revenue": {
    "journal1": {
      "revenueTemplate": {
        "key": "3"
      }
    }
  },
  "postingDate": "2025-01-01",
  "historical": {
    "isHistorical": true,
    "billedAmount": "105",
    "recognizedAmount": "106",
    "asOfDate": "2025-02-01",
    "offsetGLAccount": {
      "id": "1000"
    }
  }
}
```
**Response 201 — Reference to new contract line:**
```json
{
  "ia::result": {
    "id": "2438",
    "key": "2438",
    "href": "/objects/contracts/contract-line/2438"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/contract-line/{key}
_Get a contract line_

**Response 200 — Get a contract line:**
```json
{
  "ia::result": {
    "id": "2438",
    "key": "2438",
    "webURL": "https://app.intacct.com/objects/contracts/contract-line/2438",
    "contract": {
      "key": "2001",
      "id": "ProjectTime_Completed_Flows34_45_4",
      "state": "inProgress",
      "name": "ProjectTime_Completed_Flows",
      "href": "/objects/contracts/contract/2001"
    },
    "parent": {
      "id": null,
      "key": null,
      "lineNumber": null
    },
    "state": "inProgress",
    "lineNumber": "1",
    "recurringBillingPeriod": 2,
    "startDate": "2025-02-01",
    "endDate": "2025-11-30",
    "cancelationDate": null,
    "item": {
      "key": "221",
      "id": "CONT-CUSTSUPP24/7",
      "name": "Customer Support Team 24/7",
      "href": "/objects/inventory-control/item/221"
    },
    "itemDescription": "Premium Support Package - with a dedicated Account Manager.",
    "revenueDeferralStatus": "deferRevenueUntilItemIsDelivered",
    "billing": {
      "quantity": "12",
      "rate": "12",
      "multiplier": "1",
      "discount": "0",
      "template": {
        "key": null,
        "id": null,
        "method": ""
      },
      "schedule": {
        "id": "11992",
        "key": "11992",
        "status": "inProgress",
        "href": "/objects/contracts/billing-schedule/11992"
      },
      "startDate": "2025-02-01",
      "endDate": "2025-11-30",
      "method": "fixedPrice",
      "amountFrequency": "includeWithEveryInvoice",
      "frequency": "monthly",
      "flatFixedAmount": "144",
      "baseFlatFixedAmount": "144",
      "totalFlatFixedAmount": "1440",
      "totalBaseFlatFixedAmount": "1440",
      "usageQuantityReset": null,
      "isUsageQuantityRecurring": false,
      "holdDate": null,
      "resumeDate": null,
      "memo": null,
      "durationInPeriods": "10",
      "proratePartialPeriods": false,
      "quantityType": null,
      "committedQuantityEndAction": null,
      "committedQuantityExcess": null
    },
    "currency": {
      "exchangeRateDate": null,
      "exchangeRate": "1.000000000000"
    },
    "contacts": {
      "billTo": {
        "key": "157",
        "id": "Kaba Circuit Co(CMR12)",
        "href": "/objects/company-config/contact/157"
      },
      "shipTo": {
        "key": "157",
        "id": "Kaba Circuit Co(CMR12)",
        "href": "/objects/company-config/contact/157"
      }
    },
    "billToSource": "contractValue",
    "shipToSource": "contractValue",
    "renewal": {
      "renew": false,
      "billingTemplate": {
        "key": null,
        "id": null
      }
    },
    "isRecurring": false,
    "lineType": "sale",
    "revenue": {
      "journal1": {
        "revenueTemplate": {
          "key": "3",
          "id": "STRAIGHTLINE_MANUAL",
          "recognitionMethod": "straightLine",
          "href": "/objects/contracts/revenue-template/3"
        },
        "startDate": "2025-02-01",
        "endDate": "2025-11-30",
        "revenueSchedule": {
          "id": "11994",
          "key": "11994",
          "status": "inProgress",
          "href": "/objects/contracts/revenue-schedule/11994"
        },
        "glJournal": {
          "key": "47",
          "id": "LEGACYREVREC",
          "name": "Legacy Revenue Recognition Journal",
          "href": "/objects/general-ledger/journal/47"
        }
      },
      "journal2": {
        "revenueTemplate": {
          "key": null,
          "id": null,
          "recognitionMethod": null
        },
        "startDate": null,
        "endDate": null,
        "revenueSchedule": {
          "id": null,
          "key": null,
          "status": null
        },
        "glJournal": {
          "key": "49",
          "id": "ASC606REVREC",
          "name": "ASC 606 Revenue Recognition Journal",
          "href": "/objects/general-ledger/journal/49"
        }
      },
      "totalQuantity": null,
      "holdDate": null,
      "resumeDate": null,
      "memo": null
    },
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
      },
      "department": {
        "key": null,
        "id": null,
        "name": null
      },
      "task": {
        "key": null,
        "name": null,
        "id": null
      },
      "customer": {
        "key": "6",
        "id": "MR12",
        "name": "Kaba Circuit Co",
        "href": "/objects/accounts-receivable/customer/6"
      },
      "vendor": {
        "key": null,
        "id": null,
        "name": null
      },
      "employee": {
        "key": null,
        "id": null,
        "name": null
      },
      "project": {
        "key": null,
        "id": null,
        "name": null
      },
      "class": {
        "key": null,
        "id": null,
        "name": null
      }
    },
    "audit": {
      "createdDateTime": "2025-08-28T17:01:22Z",
      "modifiedDateTime": "2025-08-28T17:01:23Z",
      "createdByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "createdBy": "159",
      "modifiedByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "modifiedBy": "159"
    },
    "changeType": null,
    "priceCalculationMemo": null,
    "deliveryStatus": "delivered",
    "deliveryDate": "2025-02-01",
    "postingDate": "2025-01-01",
    "expense": {
      "holdDate": null,
      "resumeDate": null,
      "memo": null
    },
    "memo": null,
    "renewalTriggerDate": null,
    "lineRenewalDate": null,
    "historical": {
      "isHistorical": true,
      "billedAmount": "101",
      "recognizedAmount": "102",
      "asOfDate": "2025-02-01",
      "offsetGLAccount": {
        "key": "9",
        "id": "1000",
        "name": "Bank of America A/c.",
        "href": "/objects/general-ledger/account/9"
      }
    },
    "customRenewalAmounts": [
      {
        "key": "45",
        "renewalNumber": 1,
        "overrideAmount": "10000"
      },
      {
        "key": "48",
        "renewalNumber": 2,
        "overrideAmount": "900.98"
      }
    ],
    "href": "/objects/contracts/contract-line/2438"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/contract-line/{key}
_Update a contract line_

**Request example — Update a contract line:**
```json
{
  "item": {
    "key": "221"
  },
  "dimensions": {
    "location": {
      "key": "1"
    }
  },
  "startDate": "2025-01-06",
  "endDate": "2025-12-31",
  "billing": {
    "quantity": "12",
    "rate": "12",
    "multiplier": "1",
    "discount": "0",
    "method": "fixedPrice",
    "amountFrequency": "includeWithEveryInvoice",
    "frequency": "monthly",
    "flatFixedAmount": "144",
    "baseFlatFixedAmount": "144"
  },
  "changeType": "newMRR",
  "revenue": {
    "journal1": {
      "revenueTemplate": {
        "key": "33"
      }
    },
    "journal2": {
      "revenueTemplate": {
        "key": "4"
      }
    }
  },
  "postingDate": "2025-04-01"
}
```
**Response 200 — Reference to updated contract line:**
```json
{
  "ia::result": {
    "id": "2438",
    "key": "2438",
    "href": "/objects/contracts/contract-line/2438"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/contract-line/{key}
_Delete a contract line_


## GET /objects/contracts/contract-mea-allocation
_List MEA allocations_

**Response 200 — List MEA allocations:**
```json
{
  "ia::result": [
    {
      "key": "22",
      "id": "CN-00001-MEA4",
      "href": "/objects/contracts/contract-mea-allocation/22"
    },
    {
      "key": "20",
      "id": "CN-00001-MEA3",
      "href": "/objects/contracts/contract-mea-allocation/20"
    },
    {
      "key": "16",
      "id": "CN-00001-MEA2",
      "href": "/objects/contracts/contract-mea-allocation/16"
    },
    {
      "key": "14",
      "id": "red_mea_debug3-MEA3",
      "href": "/objects/contracts/contract-mea-allocation/14"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/contracts/contract-mea-allocation
_Create an MEA allocation_

**Request example — Create an MEA allocation:**
```json
{
  "contract": {
    "id": "CN-00001"
  },
  "id": "MEA4",
  "description": "MEA4",
  "effectiveDate": "2026-01-01",
  "applyToJournal1": true,
  "applyToJournal2": false,
  "adjustmentType": "oneTime",
  "allocationDetails": [
    {
      "contractLineNumber": 1,
      "bundleNumber": 1
    },
    {
      "contractLineNumber": 2,
      "bundleNumber": 1
    }
  ]
}
```
**Response 201 — Create an MEA allocation:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "MEA4",
    "href": "/objects/contracts/contract-mea-allocation/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/contracts/contract-mea-allocation/{key}
_Get an MEA allocation_

**Response 200 — Reference to MEA allocation:**
```json
{
  "ia::result": {
    "key": "172",
    "contract": {
      "key": "159",
      "id": "MCP_Exchange rate",
      "href": "/objects/contracts/contract/159"
    },
    "id": "MCP_Exchange rate-MEA1",
    "description": "MEA1",
    "effectiveDate": "2026-01-01",
    "applyToJournal1": true,
    "applyToJournal2": false,
    "adjustmentType": "oneTime",
    "fairValuePriceEffectiveAsOf": "meaAllocationEffectiveDate",
    "status": "active",
    "audit": {
      "createdDateTime": "2026-03-08T11:04:20Z",
      "modifiedDateTime": "2026-03-08T11:04:20Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "allocationDetails": [
      {
        "contractLineNumber": 1,
        "bundleNumber": 1,
        "meaAmount": "523.81",
        "meaPercent": "0.079793278000",
        "meaBaseAmount": "43648.62",
        "rate": "230",
        "quantity": "100",
        "multiplier": "1",
        "totalFlatAmount": "23000.00",
        "totalFlatBaseAmount": "1916569.30",
        "fairValueUnitPrice": "165.00",
        "extendedFairValuePrice": "16500.00",
        "computationMemo": "Lower limit = 165, Upper limit = 165. Rule when outside range = Nearest boundary",
        "flatAmount": "23000.00"
      },
      {
        "contractLineNumber": 2,
        "bundleNumber": 1,
        "meaAmount": "655937.11",
        "meaPercent": "99.920206722000",
        "meaBaseAmount": "54658649.03",
        "rate": "678.776",
        "quantity": "77.77",
        "multiplier": "12",
        "totalFlatAmount": "633460.92",
        "totalFlatBaseAmount": "52785728.40",
        "fairValueUnitPrice": "22140.00",
        "extendedFairValuePrice": "20661933.60",
        "computationMemo": "Lower limit = 22140, Upper limit = 25830. Rule when outside range = Nearest boundary",
        "flatAmount": "52788.41"
      }
    ],
    "href": "/objects/contracts/contract-mea-allocation/172"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/contract-txn-history
_List contract transaction histories_

**Response 200 — List contract transaction histories:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/contract-txn-history/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/contracts/contract-txn-history/2"
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

## GET /objects/contracts/contract-txn-history/{key}
_Get a contract transaction history_

**Response 200 — Get a contract transaction history:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/contracts/contract-txn-history/1",
    "contractExpense": {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/expense/1"
    },
    "postingType": "accountsReceivable",
    "balanceType": "accountsReceivable",
    "journalType": "journal1",
    "amount": "50.00",
    "baseAmount": "50.00",
    "exchangeRate": "1.02",
    "txnType": "debit",
    "txnDate": "2024-01-01",
    "classification": "billed",
    "paymentEntry": {
      "key": "1",
      "id": "1",
      "href": "/objects/accounts-payable/subledger-record-line/1"
    },
    "eventType": "onRecognition",
    "resolveType": "usage",
    "isHistorical": true,
    "dataVersion": "1",
    "isRedone": false,
    "arAdjustment": {
      "key": "15",
      "id": "15",
      "href": "/objects/accounts-receivable/adjustment/23"
    },
    "contract": {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/contract/23"
    },
    "contractBillingScheduleLine": {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/billing-schedule-line/23"
    },
    "contractLine": {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/contract-line/1"
    },
    "contractExpenseScheduleLine": {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/expense-schedule-line/145"
    },
    "contractRevenueScheduleLine": {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/revenue-schedule-line/145"
    },
    "journalEntry": {
      "key": "1",
      "id": "1",
      "href": "/objects/general-ledger/journal-entry/1"
    },
    "audit": {
      "createdDateTime": "2025-08-28T17:01:22Z",
      "modifiedDateTime": "2025-08-28T17:01:23Z",
      "createdByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "createdBy": "159",
      "modifiedByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "modifiedBy": "159"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/contract-type
_List contract types_

**Response 200 — List contract types:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "Service_1",
      "href": "/objects/contracts/contract-type/2"
    },
    {
      "key": "1",
      "id": "API",
      "href": "/objects/contracts/contract-type/1"
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

## POST /objects/contracts/contract-type
_Create a contract type_

**Request example — Create a parent contract type:**
```json
{
  "id": "Auto-renewal",
  "description": "Parent type for automatic renewal contracts",
  "status": "active"
}
```
**Request example — Create a child contract type:**
```json
{
  "id": "Annual",
  "description": "Annual automatic renewals",
  "status": "active",
  "parent": {
    "key": "11"
  }
}
```
**Response 201 — Reference to new contract type:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "Auto-renewal",
    "href": "/objects/contracts/contract-type/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/contract-type/{key}
_Get a contract type_

**Response 200 — Get a contract type:**
```json
{
  "ia::result": {
    "key": "10",
    "parent": {
      "key": "2",
      "id": "Annual type",
      "href": "/objects/contracts/contract-type/2"
    },
    "id": "Auto-renewal",
    "status": "active",
    "description": "Parent type for automatic renewal contracts",
    "href": "/objects/contracts/contract-type/10",
    "webURL": "https://app.intacct.com/objects/contracts/contract-type/10",
    "audit": {
      "createdByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "createdBy": "159",
      "modifiedByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "modifiedBy": "159",
      "createdDateTime": "2025-09-04T00:00:00Z",
      "modifiedDateTime": "2025-09-04T00:00:00Z"
    },
    "entity": {
      "key": "2",
      "id": "2",
      "name": "India",
      "href": "/objects/company-config/entity/2"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/contract-type/{key}
_Update a contract type_

**Response 200 — Reference to updated contract type:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "Managed_IT_Service",
    "href": "/objects/contracts/contract-type/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/contract-type/{key}
_Delete a contract type_


## GET /objects/contracts/contract-usage
_List contract usage_

**Response 200 — List contract usage objects:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "RT-00001",
      "href": "/objects/contracts/contract-usage/84"
    },
    {
      "key": "85",
      "id": "RT-00002",
      "href": "/objects/contracts/contract-usage/85"
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

## POST /objects/contracts/contract-usage
_Create contract usage object_

**Request example — Create a contract usage object:**
```json
{
  "contractLine": {
    "key": "1"
  },
  "usageDate": "2025-04-01",
  "quantity": "3003.99",
  "usageType": "revenue"
}
```
**Response 201 — Reference to new contract usage object:**
```json
{
  "ia::result": {
    "id": "6",
    "key": "6",
    "href": "/objects/contracts/contract-usage/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/contract-usage/{key}
_Get a contract usage_

**Response 200 — Get a contract usage object:**
```json
{
  "ia::result": {
    "id": "4",
    "key": "4",
    "contractLine": {
      "id": "122",
      "key": "122",
      "lineNumber": "1",
      "href": "/objects/contracts/contract-line/122"
    },
    "usageDate": "2025-04-01",
    "quantity": "3003.99",
    "servicePeriodStartDate": "2025-01-01",
    "servicePeriodEndDate": "2025-12-31",
    "usageType": "revenue",
    "documentId": "Contract Invoice-CON-IN-0110.doc",
    "revenueScheduleLine": {
      "id": "5247",
      "key": "5247",
      "postingDate": "2025-01-15",
      "amount": "25",
      "href": "/objects/contracts/revenue-schedule-line/5247"
    },
    "revenueSchedule": {
      "id": "631",
      "key": "631",
      "href": "/objects/contracts/revenue-schedule/631"
    },
    "revenue2Schedule": {
      "id": null,
      "key": null
    },
    "audit": {
      "createdDateTime": "2024-02-08T00:10:25Z",
      "modifiedDateTime": "2024-02-08T00:10:25Z",
      "createdByUser": {
        "key": "109",
        "id": "Admin",
        "href": "/objects/company-config/user/109"
      },
      "createdBy": "109",
      "modifiedByUser": {
        "key": "109",
        "id": "Admin",
        "href": "/objects/company-config/user/109"
      },
      "modifiedBy": "109"
    },
    "contractUsageBilling": {
      "billedDate": "2017-01-31",
      "recurringUsageDate": null
    },
    "contract": {
      "key": "38",
      "id": "CON-028",
      "name": "Professional Power",
      "href": "/objects/contracts/contract/38"
    },
    "item": {
      "key": "2547",
      "id": "11",
      "name": "GP",
      "href": "/objects/inventory-control/item/2547"
    },
    "customer": {
      "key": "2",
      "id": "2",
      "name": "Logic Solutions",
      "href": "/objects/accounts-receivable/customer/2"
    },
    "href": "/objects/contracts/contract-usage/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/contract-usage/{key}
_Update a contract usage_

**Request example — Update quantity:**
```json
{
  "quantity": "400"
}
```
**Request example — Update usage type:**
```json
{
  "usageType": "billingCommitted"
}
```
**Response 200 — Reference to updated contract usage:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "2021-LV2",
    "href": "/objects/contracts/contract-usage/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/contract-usage/{key}
_Delete contract usage_


## GET /objects/contracts/contract/{key}
_Get a contract_

**Response 200 — Get a contract:**
```json
{
  "ia::result": {
    "key": "944",
    "id": "12_122_1",
    "href": "/objects/contracts/contract/944",
    "webURL": "https://app.intacct.com/objects/contracts/contract/944",
    "renewalTemplate": {
      "id": "32",
      "key": "32",
      "contractTermType": "termed",
      "name": "Renew_Contract12",
      "termLength": 12,
      "termPeriod": "years",
      "billInAdvanceLengthRenewal": null,
      "billInAdvancePeriodRenewal": null,
      "triggerDate": null,
      "renewalDate": "2025-01-01",
      "href": "/objects/order-entry/renewal-template/944"
    },
    "parent": {
      "key": "59",
      "id": "CON-0012-1",
      "href": "/objects/contracts/contract/59"
    },
    "description": "Contract for customer 12_122",
    "state": "renewed",
    "startDate": "2025-01-01",
    "endDate": "2025-12-31",
    "cancellationDate": null,
    "name": "12_122",
    "entity": {
      "key": "54",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/54"
    },
    "dimensions": {
      "customer": {
        "key": "2",
        "id": "2",
        "name": "Logic Solutions",
        "href": "/objects/accounts-receivable/customer/2"
      },
      "location": {
        "key": "2",
        "id": "2",
        "name": "India",
        "href": "/objects/company-config/location/2"
      },
      "department": {
        "key": "4",
        "id": "4",
        "name": "Human Resources",
        "href": "/objects/company-config/department/4"
      },
      "project": {
        "key": null,
        "id": null,
        "name": null
      },
      "vendor": {
        "key": "54",
        "id": "208",
        "name": "Quick and Easy Payroll",
        "href": "/objects/accounts-payable/vendor/54"
      },
      "employee": {
        "key": "55",
        "id": "EM 2",
        "name": "Ravi",
        "href": "/objects/company-config/employee/55"
      },
      "class": {
        "key": "15",
        "id": "vsoe_class_004_R",
        "name": "vsoe_class_name_004_R",
        "href": "/objects/company-config/class/15"
      }
    },
    "contacts": {
      "billTo": {
        "key": "117",
        "id": "Logic Solutions(C2)",
        "email1": "qa-auto-emails@company.com",
        "email2": "twoaddres@company.com",
        "href": "/objects/company-config/contact/117"
      },
      "shipTo": {
        "key": "117",
        "id": "Logic Solutions(C2)",
        "email1": "qa-auto-emails@company.com",
        "email2": "twoaddres@company.com",
        "href": "/objects/company-config/contact/117"
      },
      "additionalContact": {
        "key": "117",
        "id": "Logic Solutions(C2)",
        "email1": "qa-auto-emails@company.com",
        "email2": "twoaddres@company.com",
        "href": "/objects/company-config/contact/117"
      }
    },
    "billingFrequency": "quarterly",
    "paymentTerm": {
      "key": "16",
      "id": "N90",
      "href": "/objects/accounts-receivable/term/16"
    },
    "billingPriceList": {
      "key": "24",
      "id": "SaaSy Pricing",
      "href": "/objects/contracts/billing-price-list/24"
    },
    "meaPriceList": {
      "id": "2009 VSOE Price List USD_R",
      "key": "2",
      "href": "/objects/contracts/mea-price-list/2"
    },
    "holdBilling": false,
    "holdRevenue": false,
    "holdExpense": false,
    "currency": {
      "baseCurrency": "INR",
      "txnCurrency": "INR",
      "exchangeRateType": "EUR-Rate"
    },
    "billInAdvanceLength": null,
    "billInAdvancePeriod": null,
    "audit": {
      "createdDateTime": "2025-02-15T03:03:31Z",
      "modifiedDateTime": "2025-02-15T03:03:32Z",
      "createdByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "createdBy": "159",
      "modifiedByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "modifiedBy": "159"
    },
    "attachment": {
      "id": null,
      "key": null
    },
    "status": "active",
    "contractType": {
      "key": null,
      "name": null
    },
    "deferEstimatedTimeBasedRevenueBy": null,
    "postMemo": null,
    "contractTotalAmount": "1728",
    "billedAmount": "1728"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/contract/{key}
_Update a contract_

**Request example — Update location and billing contact:**
```json
{
  "location": {
    "key": "6"
  },
  "contacts": {
    "billTo": {
      "key": "2"
    }
  }
}
```
**Response 200 — Reference to updated contract:**
```json
{
  "ia::result": {
    "key": "121",
    "id": "CON-0045-1",
    "href": "/objects/contracts/contract/121"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/contract/{key}
_Delete a contract_


## GET /objects/contracts/evergreen-template
_List Evergreen templates_

**Response 200 — List evergreen templates:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/evergreen-template/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/contracts/evergreen-template/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/contracts/evergreen-template
_Create an evergreen template_

**Request example — Create an evergreen template:**
```json
{
  "id": "SubInv",
  "description": "Subscription Invoice RevRec Creation Same as original price",
  "pricing": {
    "type": "sameAsOriginal",
    "markup": "percentageMarkup",
    "markupValue": "null"
  },
  "status": "active",
  "recurrenceOptions": {
    "daysBeforeAfter": 1,
    "beforeOrAfterDateOfRenewal": "before"
  },
  "emailNotifications": {
    "customer": {
      "sendToCustomer": true,
      "afterNumberOfRecurrences": 1,
      "customerEmailTemplate": {
        "id": "1"
      }
    },
    "internal": {
      "sendToInternal": true,
      "afterNumberOfRecurrences": 10,
      "internalEmailTemplate": {
        "id": "1"
      }
    }
  }
}
```
**Response 201 — Reference to evergreen template:**
```json
{
  "ia::result": {
    "key": "25",
    "id": "25",
    "href": "/objects/contracts/evergreen-template/25"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/evergreen-template/{key}
_Get an evergreen template_

**Response 200 — Get an evergreen template:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "description": "Subscription Invoice RevRec Creation Same as original price",
    "pricing": {
      "type": "sameAsOriginal",
      "markup": "percentageMarkup",
      "markupValue": "null"
    },
    "status": "active",
    "recurrenceOptions": {
      "daysBeforeAfter": 1,
      "beforeOrAfterDateOfRenewal": "before"
    },
    "emailNotifications": {
      "customer": {
        "sendToCustomer": true,
        "afterNumberOfRecurrences": 1,
        "customerEmailTemplate": {
          "key": "1",
          "id": "1",
          "href": "/objects/company-config/email-template/1"
        }
      },
      "internal": {
        "sendToInternal": true,
        "afterNumberOfRecurrences": 1,
        "internalEmailTemplate": {
          "key": "1",
          "id": "1",
          "href": "/objects/company-config/email-template/1"
        }
      }
    },
    "href": "/objects/contracts/evergreen-template/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/evergreen-template/{key}
_Update an evergreen template_

**Request example — Update an evergreen template:**
```json
{
  "description": "Subscription Invoice RevRec Creation Same as original price - Updated",
  "emailNotifications": {
    "customer": {
      "sendToCustomer": false
    }
  }
}
```
**Response 200 — Reference to evergreen template:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/contracts/evergreen-template/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/evergreen-template/{key}
_Delete an evergreen template_


## GET /objects/contracts/expense
_List expenses_

**Response 200 — List expenses:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/contracts/expense/84"
    },
    {
      "key": "87",
      "id": "87",
      "href": "/objects/contracts/expense/87"
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

## POST /objects/contracts/expense
_Create an expense_

**Request example — Create an expense:**
```json
{
  "contract": {
    "key": "1"
  },
  "item": {
    "key": "1"
  },
  "dimensions": {
    "location": {
      "key": "1"
    }
  },
  "templates": {
    "expenseJournal1": {
      "expenseTemplate": {
        "key": "1"
      },
      "startDate": "2025-01-15",
      "endDate": "2025-03-31"
    }
  },
  "txnAmount": "8.25",
  "baseAmount": "8.25",
  "postingDate": "2025-01-15"
}
```
**Response 201 — Reference to expense:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "href": "/objects/contracts/expense/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/expense-schedule
_List expense schedules_

**Response 200 — List expense schedules:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "RT-00001",
      "href": "/objects/contracts/expense-schedule/84"
    },
    {
      "key": "85",
      "id": "RT-00002",
      "href": "/objects/contracts/expense-schedule/85"
    },
    {
      "key": "60",
      "id": "RT-00003",
      "href": "/objects/contracts/expense-schedule/60"
    },
    {
      "key": "78",
      "id": "RT-00004",
      "href": "/objects/contracts/expense-schedule/78"
    },
    {
      "key": "79",
      "id": "RT-00005",
      "href": "/objects/contracts/expense-schedule/79"
    }
  ],
  "ia::meta": {
    "totalCount": 5,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/contracts/expense-schedule-line
_List expense schedule lines_

**Response 200 — List expense schedule lines:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "RT-00001",
      "href": "/objects/contracts/expense-schedule-line/84"
    },
    {
      "key": "85",
      "id": "RT-00002",
      "href": "/objects/contracts/expense-schedule-line/85"
    },
    {
      "key": "60",
      "id": "RT-00003",
      "href": "/objects/contracts/expense-schedule-line/60"
    },
    {
      "key": "78",
      "id": "RT-00004",
      "href": "/objects/contracts/expense-schedule-line/78"
    },
    {
      "key": "79",
      "id": "RT-00005",
      "href": "/objects/contracts/expense-schedule-line/79"
    }
  ],
  "ia::meta": {
    "totalCount": 5,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/contracts/expense-schedule-line/{key}
_Get an expense schedule line_

**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/contracts/expense-schedule-line/145",
    "contractExpenseSchedule": {
      "key": "145",
      "id": "145",
      "href": "/objects/contracts/expense-schedule/145"
    },
    "scheduledOperationKey": "57665",
    "state": "posted",
    "scheduledAmount": "125.27",
    "scheduledBaseAmount": "137.52",
    "scheduledExchangeRate": "1.345",
    "isHistorical": false,
    "audit": {
      "createdDateTime": "2023-05-16T15:34:35Z",
      "modifiedDateTime": "2024-09-14T21:23:42Z",
      "createdBy": "436",
      "modifiedBy": "3086",
      "createdByUser": {
        "key": "436",
        "id": "JohnDoe",
        "href": "/objects/company-config/user/436"
      },
      "modifiedByUser": {
        "key": "3086",
        "id": "JaneDoe",
        "href": "/objects/company-config/user/3086"
      }
    },
    "scheduledPostingDate": "2025-04-30",
    "posted": false,
    "actualPostingDate": "2025-04-30",
    "journalEntry": {
      "key": "8153",
      "id": "4765",
      "href": "/objects/general-ledger/journal-entry/1981"
    }
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## GET /objects/contracts/expense-schedule/{key}
_Get an expense schedule_

**Response 200 — Get an expense schedule:**
```json
{
  "ia::result": {
    "id": "1563",
    "key": "1563",
    "journal": "J1",
    "contract": {
      "key": "138",
      "id": "2025_R1_Contract-NOVA",
      "href": "/objects/contracts/contract/138"
    },
    "contractLine": {
      "id": "377",
      "key": "377",
      "href": "/objects/contracts/contract-line/377"
    },
    "status": "inProgress",
    "cancellationDate": null,
    "audit": {
      "createdDateTime": "2025-01-29T11:26:52Z",
      "modifiedDateTime": "2025-01-29T11:26:52Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "expenseScheduleLines": [
      {
        "id": "14287",
        "key": "14287",
        "contractExpenseSchedule": {
          "id": "1563",
          "key": "1563",
          "href": "/objects/contracts/expense-schedule/1563"
        },
        "scheduledOperationKey": null,
        "scheduledAmount": "10833.26",
        "scheduledBaseAmount": "10833.26",
        "scheduledExchangeRate": "1.000000000000",
        "scheduledPostingDate": "2025-01-31",
        "actualPostingDate": null,
        "posted": false,
        "isHistorical": false,
        "journalEntry": {
          "key": null,
          "id": null
        },
        "audit": {
          "createdDateTime": "2025-01-29T11:26:52Z",
          "modifiedDateTime": "2025-03-28T04:15:24Z",
          "createdBy": "1",
          "modifiedBy": null
        },
        "href": "/objects/contracts/expense-schedule-line/14287"
      },
      {
        "id": "14288",
        "key": "14288",
        "contractExpenseSchedule": {
          "id": "1563",
          "key": "1563",
          "href": "/objects/contracts/expense-schedule/1563"
        },
        "scheduledOperationKey": null,
        "scheduledAmount": "10833.26",
        "scheduledBaseAmount": "10833.26",
        "scheduledExchangeRate": "1.000000000000",
        "scheduledPostingDate": "2025-02-28",
        "actualPostingDate": null,
        "posted": false,
        "isHistorical": false,
        "journalEntry": {
          "key": null,
          "id": null
        },
        "audit": {
          "createdDateTime": "2025-01-29T11:26:52Z",
          "modifiedDateTime": "2025-03-28T04:15:24Z",
          "createdBy": "1",
          "modifiedBy": null
        },
        "href": "/objects/contracts/expense-schedule-line/14288"
      }
    ],
    "href": "/objects/contracts/expense-schedule/1563"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/expense-schedule/{key}
_Update an expense schedule_

**Request example — Add an expense schedule line:**
```json
{
  "key": "145",
  "expenseScheduleLines": [
    {
      "scheduledPostingDate": "2025-05-25",
      "scheduledAmount": "125.34"
    }
  ]
}
```
**Request example — Update an expense schedule line:**
```json
{
  "key": "145",
  "expenseScheduleLines": [
    {
      "key": "12",
      "scheduledPostingDate": "2025-05-25",
      "scheduledAmount": "125.34"
    }
  ]
}
```
**Request example — Update multiple expense schedule lines:**
```json
{
  "key": "145",
  "expenseScheduleLines": [
    {
      "key": "12",
      "scheduledPostingDate": "2025-05-25",
      "scheduledAmount": "125.34"
    },
    {
      "key": "13",
      "scheduledPostingDate": "2025-06-25",
      "scheduledAmount": "245.18"
    }
  ]
}
```
**Request example — Delete an expense schedule line:**
```json
{
  "key": "145",
  "expenseScheduleLines": [
    {
      "ia::operation": "delete",
      "key": "12"
    }
  ]
}
```
**Response 200 — Reference to expense schedule:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "2025-LV2",
    "href": "/objects/contracts/expense-schedule/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/expense-template
_List expense templates_

**Response 200 — List expense templates:**
```json
{
  "ia::result": [
    {
      "key": "23",
      "id": "EXPDAILYRATE_MAN",
      "href": "/objects/contracts/expense-template/23"
    },
    {
      "key": "1",
      "id": "EXPSTRAIGHTLINE_MAN",
      "href": "/objects/contracts/expense-template/1"
    },
    {
      "key": "2",
      "id": "EXPSTRAIGHTLINE_AUTO",
      "href": "/objects/contracts/expense-template/2"
    },
    {
      "key": "22",
      "id": "EXPDAILYRATE_AUTO",
      "href": "/objects/contracts/expense-template/22"
    },
    {
      "key": "32",
      "id": "MM-Expense-Report1",
      "href": "/objects/contracts/expense-template/32"
    }
  ],
  "ia::meta": {
    "totalCount": 5,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/contracts/expense-template
_Create an expense template_

**Request example — Create an expense template:**
```json
{
  "id": "EXPSTRAIGHTLINE_MAN1",
  "description": "Expenses straight-line amortization monthly manual.",
  "defaultPostingType": "manual",
  "amortizationSchedulePeriod": "monthly",
  "amortizationMethod": "straightLine"
}
```
**Response 201 — Reference to expense template:**
```json
{
  "ia::result": {
    "key": "35",
    "id": "EXPSTRAIGHTLINE_MAN1",
    "href": "/objects/contracts/expense-template/35"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/expense-template-line
_List expense template lines_

**Response 200 — List expense template lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/expense-template-line/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/contracts/expense-template-line/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/contracts/expense-template-line/3"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/contracts/expense-template-line/4"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/contracts/expense-template-line/{key}
_Get an expense template line_

**Response 200 — Get an expense template line:**
```json
{
  "ia::result": {
    "id": "4",
    "key": "4",
    "contractExpenseTemplate": {
      "key": "30",
      "id": "EXPSTRAIGHTLINE",
      "href": "/objects/contracts/expense-template/30"
    },
    "periodOffset": "9",
    "percentToRecognize": "25.00000000",
    "href": "/objects/contracts/expense-template-line/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/expense-template/{key}
_Get an expense template_

**Response 200 — Get an expense template:**
```json
{
  "ia::result": {
    "key": "35",
    "id": "EXPSTRAIGHTLINE_MAN1",
    "description": "Expenses straight-line amortization monthly manual.",
    "defaultPostingType": "manual",
    "amortizationSchedulePeriod": "monthly",
    "postingDay": 1,
    "amortizationMethod": "straightLine",
    "status": "active",
    "audit": {
      "modifiedDateTime": "2025-09-11T15:00:53Z",
      "createdDateTime": "2025-09-11T15:00:53Z",
      "createdByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "createdBy": "159",
      "modifiedByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "modifiedBy": "159"
    },
    "lines": [],
    "href": "/objects/contracts/expense-template/35"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/expense-template/{key}
_Update an expense template_

**Request example — Update expense template:**
```json
{
  "description": "Expenses straight-line amortization monthly manual.",
  "defaultPostingType": "manual",
  "amortizationSchedulePeriod": "monthly",
  "amortizationMethod": "straightLine"
}
```
**Response 200 — Reference to expense template:**
```json
{
  "ia::result": {
    "key": "35",
    "id": "EXPSTRAIGHTLINE_MAN1",
    "href": "/objects/contracts/expense-template/35"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/expense-template/{key}
_Delete an expense template_


## GET /objects/contracts/expense/{key}
_Get an expense_

**Response 200 — Get an expense:**
```json
{
  "ia::result": {
    "id": "2",
    "key": "2",
    "contract": {
      "key": "1",
      "id": "CT-SERV-MKTG-0472",
      "href": "/objects/contracts/contract/1"
    },
    "contractLine": {
      "id": null,
      "key": null,
      "state": null
    },
    "item": {
      "key": "322",
      "id": "CONT-FUNC-SUPP-EXP",
      "name": "Functional Consultation support Charges",
      "href": "/objects/inventory-control/item/322"
    },
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
      },
      "department": {
        "key": null,
        "id": null,
        "name": null
      },
      "project": {
        "key": null,
        "id": null,
        "name": null
      },
      "customer": {
        "key": "013",
        "id": "CUS-ABIL-0011",
        "name": "Ability Marketing Solutions",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "vendor": {
        "key": null,
        "id": null,
        "name": null
      },
      "employee": {
        "key": null,
        "id": null,
        "name": null
      },
      "class": {
        "key": null,
        "id": null,
        "name": null
      }
    },
    "templates": {
      "expenseJournal1": {
        "expenseTemplate": {
          "key": "1",
          "id": "EXPSTRAIGHTLINE_MAN",
          "defaultPostingType": "M",
          "href": "/objects/contracts/expense-template/1"
        },
        "startDate": "2025-01-15",
        "endDate": "2025-03-31",
        "schedule": {
          "key": "15",
          "status": "inProgress",
          "href": "/objects/contracts/expense-schedule/15"
        },
        "glJournal": {
          "key": "52",
          "href": "/objects/general-ledger/journal/52"
        },
        "postingType": null,
        "postingConversionDate": "2025-04-30"
      },
      "expenseJournal2": {
        "expenseTemplate": {
          "key": null,
          "id": null,
          "defaultPostingType": null
        },
        "startDate": null,
        "endDate": null,
        "schedule": {
          "key": null,
          "status": null
        },
        "glJournal": {
          "key": "54",
          "href": "/objects/general-ledger/journal/54"
        },
        "postingType": null,
        "postingConversionDate": "2025-04-30"
      }
    },
    "txnAmount": "8.25",
    "baseAmount": "8.25",
    "currency": {
      "txnCurrency": "USD",
      "baseCurrency": "USD",
      "exchangeRateDate": null,
      "exchangeRate": "1.000000000000"
    },
    "postingDate": "2025-01-15",
    "cancelationDate": null,
    "deferredExpenseGLAccount": {
      "key": "427",
      "href": "/objects/general-ledger/account/427"
    },
    "recognizedExpenseGLAccount": {
      "key": "433",
      "href": "/objects/general-ledger/account/433"
    },
    "expenseAccrualGLAccount": {
      "key": "439",
      "href": "/objects/general-ledger/account/439"
    },
    "state": "inProgress",
    "expenseType": "contract",
    "audit": {
      "createdDateTime": "2025-02-15T03:03:31Z",
      "modifiedDateTime": "2025-02-15T03:03:32Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "calculatedExpensePostingType": "M",
    "memo": null,
    "lineNumber": 2,
    "href": "/objects/contracts/expense/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/expense/{key}
_Update an expense_

**Request example — Update an expense:**
```json
{
  "templates": {
    "expenseJournal1": {
      "expenseTemplate": {
        "key": "1"
      },
      "startDate": "2025-01-15",
      "endDate": "2025-03-31"
    }
  },
  "txnAmount": "8.25",
  "baseAmount": "8.25",
  "postingDate": "2025-01-15"
}
```
**Response 200 — Reference to expense:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "href": "/objects/contracts/expense/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/expense/{key}
_Delete an expense_


## GET /objects/contracts/historical-schedule-run
_List historical schedule runs_

**Response 200 — List historical schedule runs:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/contracts/historical-schedule-run/1"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/contracts/historical-schedule-run/{key}
_Get a historical schedule run_

**Response 200 — Get a historical schedule run:**
```json
{
  "ia::result": {
    "id": "1",
    "key": "1",
    "state": "success",
    "asOfDate": "2018-03-31",
    "notificationEmail": "john.smith@company.com",
    "audit": {
      "createdDateTime": "2026-02-01T02:16:40Z",
      "modifiedDateTime": "2026-02-09T00:00:00Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/contracts/historical-schedule-run/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/mea-category
_List MEA fair value categories_

**Response 200 — List MEA categories:**
```json
{
  "ia::result": [
    {
      "key": "3",
      "id": "Software-License-ERP",
      "href": "/objects/contracts/mea-category/3"
    },
    {
      "key": "9",
      "id": "Functional consultation support",
      "href": "/objects/contracts/mea-category/9"
    },
    {
      "key": "2",
      "id": "Software-Implementation",
      "href": "/objects/contracts/mea-category/2"
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

## POST /objects/contracts/mea-category
_Create an MEA category_

**Request example — Create a new MEA category:**
```json
{
  "id": "Software-License-ERP-1",
  "description": "Fair value category for software licenses ERP",
  "status": "active"
}
```
**Response 201 — Reference to new MEA category:**
```json
{
  "ia::result": {
    "key": "13",
    "id": "Software-License-ERP-2",
    "href": "/objects/contracts/mea-category/13"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/mea-category/{key}
_Get an MEA category_

**Response 200 — Get an MEA category:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "Software-License-ERP",
    "description": "Fair value category for software licenses --ERP",
    "status": "active",
    "audit": {
      "modifiedDateTime": "2025-01-16T23:12:22Z",
      "createdDateTime": "2024-05-13T18:22:36Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "href": "/objects/contracts/mea-category/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/mea-category/{key}
_Update an MEA category_

**Request example — Update an MEA category:**
```json
{
  "status": "active"
}
```
**Response 200 — Reference to updated MEA category:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "Software-License-ERP-1",
    "href": "/objects/contracts/mea-category/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/mea-category/{key}
_Delete an MEA category_


## GET /objects/contracts/mea-price-list
_List MEA price lists_

**Response 200 — List MEA price lists:**
```json
{
  "ia::result": [
    {
      "key": "30",
      "id": "CONMEA_FVPriceBand_Amount_USD",
      "href": "/objects/contracts/mea-price-list/30"
    },
    {
      "key": "31",
      "id": "CONMEA_FVPriceBand_Amount_EUR",
      "href": "/objects/contracts/mea-price-list/31"
    },
    {
      "key": "32",
      "id": "CONMEA_FVPriceBand_Amount_GBP",
      "href": "/objects/contracts/mea-price-list/32"
    },
    {
      "key": "33",
      "id": "CONMEA_FVPriceBand_Amount_INR",
      "href": "/objects/contracts/mea-price-list/33"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/contracts/mea-price-list
_Create an MEA price list_

**Request example — Create a new MEA price list:**
```json
{
  "status": "active",
  "id": "CONMEA_FVPriceBand_Amount_USD_1",
  "description": "MEA NearestBoundary PriceBand Amount"
}
```
**Response 201 — Reference to MEA price list:**
```json
{
  "ia::result": {
    "key": "39",
    "id": "CONMEA_FVPriceBand_Amount_USD_2",
    "href": "/objects/contracts/mea-price-list/39"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/mea-price-list-entry
_List MEA price list entries_

**Response 200 — List MEA price list entries:**
```json
{
  "ia::result": [
    {
      "key": "516",
      "id": "516",
      "href": "/objects/contracts/mea-price-list-entry/516"
    },
    {
      "key": "514",
      "id": "514",
      "href": "/objects/contracts/mea-price-list-entry/514"
    },
    {
      "key": "515",
      "id": "515",
      "href": "/objects/contracts/mea-price-list-entry/515"
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

## POST /objects/contracts/mea-price-list-entry
_Create an MEA price list entry_

**Request example — Create a new MEA price list entry:**
```json
{
  "status": "active",
  "meaPriceList": {
    "key": "7"
  },
  "item": {
    "key": "211"
  },
  "currency": {
    "txnCurrency": "CAD"
  },
  "priceType": "amount",
  "usePriceRange": false,
  "priceRangeVarianceType": null,
  "priceRuleOutsideRange": null,
  "lines": [
    {
      "startDate": "2024-01-01",
      "amountOrPercent": "100.00",
      "markUp": "0",
      "markDown": "0",
      "upperLimit": "0",
      "lowerLimit": "0",
      "memo": "ERP Implementation_Memo"
    }
  ]
}
```
**Response 201 — Reference to new MEA price list entry:**
```json
{
  "ia::result": {
    "id": "532",
    "key": "532",
    "href": "/objects/contracts/mea-price-list-entry/532"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/mea-price-list-entry-line
_List MEA price list entry lines_

**Response 200 — List of MEA price list entry lines:**
```json
{
  "ia::result": [
    {
      "key": "574",
      "id": "574",
      "href": "/objects/contracts/mea-price-list-entry-line/574"
    },
    {
      "key": "513",
      "id": "513",
      "href": "/objects/contracts/mea-price-list-entry-line/513"
    },
    {
      "key": "514",
      "id": "514",
      "href": "/objects/contracts/mea-price-list-entry-line/514"
    },
    {
      "key": "515",
      "id": "515",
      "href": "/objects/contracts/mea-price-list-entry-line/515"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/contracts/mea-price-list-entry-line/{key}
_Get an MEA price list entry line_

**Response 200 — Get an MEA price list entry line:**
```json
{
  "ia::result": {
    "id": "574",
    "key": "574",
    "meaPriceListEntry": {
      "id": "516",
      "key": "516",
      "href": "/objects/contracts/mea-price-list-entry/516"
    },
    "startDate": "2024-08-01",
    "amountOrPercent": "10.00",
    "markUp": "0",
    "markDown": "0",
    "upperLimit": "0",
    "lowerLimit": "0",
    "memo": null,
    "audit": {
      "modifiedDateTime": "2025-01-16T23:12:22Z",
      "createdDateTime": "2024-05-13T18:22:36Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "href": "/objects/contracts/mea-price-list-entry-line/574"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/mea-price-list-entry-line/{key}
_Update an MEA price list entry line_

**Request example — Update an MEA price list entry line:**
```json
{
  "startDate": "2024-08-02",
  "amountOrPercent": "10.00",
  "markUp": "0",
  "markDown": "0",
  "upperLimit": "0",
  "lowerLimit": "0",
  "memo": null
}
```
**Response 200 — Reference to updated MEA price list entry line:**
```json
{
  "ia::result": {
    "id": "574",
    "key": "574",
    "href": "/objects/contracts/mea-price-list-entry-line/574"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/mea-price-list-entry-line/{key}
_Delete an MEA price list entry line_


## GET /objects/contracts/mea-price-list-entry/{key}
_Get an MEA price list entry_

**Response 200 — Get an MEA price list entry:**
```json
{
  "ia::result": {
    "id": "521",
    "key": "521",
    "webURL": "https://app.intacct.com/objects/contracts/mea-price-list-entry/521",
    "audit": {
      "modifiedDateTime": "2025-01-16T23:12:22Z",
      "createdDateTime": "2024-05-13T18:22:36Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "status": "active",
    "meaPriceList": {
      "key": "7",
      "id": "2024 VSOE Price List CAD_R",
      "href": "/objects/contracts/mea-price-list/7"
    },
    "item": {
      "id": "ERP Software License_R",
      "name": "ERP Software License_R",
      "key": "211",
      "href": "/objects/inventory-control/item/211"
    },
    "currency": {
      "txnCurrency": "CAD"
    },
    "priceType": "percent",
    "fairValueCategory": {
      "key": "3",
      "id": "Software-License-ERP",
      "href": "/objects/contracts/mea-category/3"
    },
    "calculatePercentageBasedOn": "extendedFairValuePrice",
    "usePriceRange": false,
    "priceRangeVarianceType": null,
    "priceRuleOutsideRange": null,
    "lines": [
      {
        "id": "575",
        "key": "575",
        "meaPriceListEntry": {
          "id": "521",
          "key": "521",
          "href": "/objects/contracts/mea-price-list-entry/521"
        },
        "startDate": "2024-01-01",
        "amountOrPercent": "100.00",
        "markUp": "0",
        "markDown": "0",
        "upperLimit": "0",
        "lowerLimit": "0",
        "memo": "ERP Implementation_Memo",
        "audit": {
          "modifiedDateTime": "2025-01-16T23:12:22Z",
          "createdDateTime": "2024-05-13T18:22:36Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "createdBy": "1",
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "modifiedBy": "1"
        },
        "href": "/objects/contracts/mea-price-list-entry-line/575"
      },
      {
        "id": "576",
        "key": "576",
        "meaPriceListEntry": {
          "id": "521",
          "key": "521",
          "href": "/objects/contracts/mea-price-list-entry/521"
        },
        "startDate": "2024-01-01",
        "amountOrPercent": "100.00",
        "markUp": "0",
        "markDown": "0",
        "upperLimit": "0",
        "lowerLimit": "0",
        "memo": "ERP Training_Memo",
        "audit": {
          "modifiedDateTime": "2025-01-16T23:12:22Z",
          "createdDateTime": "2024-05-13T18:22:36Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "createdBy": "1",
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "modifiedBy": "1"
        },
        "href": "/objects/contracts/mea-price-list-entry-line/576"
      },
      {
        "id": "577",
        "key": "577",
        "meaPriceListEntry": {
          "id": "521",
          "key": "521",
          "href": "/objects/contracts/mea-price-list-entry/521"
        },
        "startDate": "2024-01-01",
        "amountOrPercent": "100.00",
        "markUp": "0",
        "markDown": "0",
        "upperLimit": "0",
        "lowerLimit": "0",
        "memo": "ERP Training_Memo",
        "audit": {
          "modifiedDateTime": "2025-01-16T23:12:22Z",
          "createdDateTime": "2024-05-13T18:22:36Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "createdBy": "1",
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "modifiedBy": "1"
        },
        "href": "/objects/contracts/mea-price-list-entry-line/577"
      },
      {
        "id": "578",
        "key": "578",
        "meaPriceListEntry": {
          "id": "521",
          "key": "521",
          "href": "/objects/contracts/mea-price-list-entry/521"
        },
        "startDate": "2024-01-01",
        "amountOrPercent": "100.00",
        "markUp": "0",
        "markDown": "0",
        "upperLimit": "0",
        "lowerLimit": "0",
        "memo": "ERP Software License_Memo",
        "audit": {
          "modifiedDateTime": "2025-01-16T23:12:22Z",
          "createdDateTime": "2024-05-13T18:22:36Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "createdBy": "1",
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "modifiedBy": "1"
        },
        "href": "/objects/contracts/mea-price-list-entry-line/578"
      }
    ],
    "href": "/objects/contracts/mea-price-list-entry/521"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/mea-price-list-entry/{key}
_Update an MEA price list entry_

**Request example — Update an MEA price list entry:**
```json
{
  "status": "active",
  "priceType": "amount",
  "usePriceRange": false,
  "priceRangeVarianceType": null,
  "priceRuleOutsideRange": null
}
```
**Response 200 — Reference to updated MEA price list entry:**
```json
{
  "ia::result": {
    "id": "532",
    "key": "532",
    "href": "/objects/contracts/mea-price-list-entry/532"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/mea-price-list-entry/{key}
_Delete an MEA price list entry_


## GET /objects/contracts/mea-price-list/{key}
_Get an MEA price list_

**Response 200 — Get an MEA price list:**
```json
{
  "ia::result": {
    "key": "37",
    "audit": {
      "createdDateTime": "2023-06-08T06:06:15Z",
      "modifiedDateTime": "2023-06-08T06:06:15Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "status": "active",
    "id": "CONMEA_FVPriceBand_Amount_USD_2",
    "description": "MEA NearestBoundary PriceBand Amount",
    "isDefault": false,
    "href": "/objects/contracts/mea-price-list/37"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/mea-price-list/{key}
_Update an MEA price list_

**Request example — Update an MEA price list:**
```json
{
  "status": "active"
}
```
**Response 200 — Reference to updated MEA price list:**
```json
{
  "ia::result": {
    "key": "38",
    "id": "CONMEA_FVPriceBand_Amount_USD",
    "href": "/objects/contracts/mea-price-list/38"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/contracts/mea-price-list/{key}
_Delete an MEA price list_


## GET /objects/contracts/revenue-schedule
_List revenue schedules_

**Response 200 — List revenue schedules:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/contracts/revenue-schedule/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/contracts/revenue-schedule/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/contracts/revenue-schedule/60"
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

## GET /objects/contracts/revenue-schedule-line
_List revenue schedule lines_

**Response 200 — List revenue schedule lines:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/contracts/revenue-schedule-line/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/contracts/revenue-schedule-line/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/contracts/revenue-schedule-line/60"
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

## GET /objects/contracts/revenue-schedule-line/{key}
_Get a revenue schedule line_

**Response 200 — Get a revenue schedule line:**
```json
{
  "ia::result": {
    "id": "4657",
    "key": "4657",
    "contractRevenueSchedule": {
      "id": "420",
      "key": "420",
      "href": "/objects/contracts/revenue-schedule/420"
    },
    "scheduledOperationKey": null,
    "scheduledAmount": "35000",
    "scheduledBaseAmount": "35000",
    "postedBaseAmount": null,
    "scheduledExchangeRate": "1.000000000000",
    "scheduledPostingDate": "2025-03-09",
    "actualPostingDate": null,
    "derivedPostingDate": "2025-03-09",
    "posted": false,
    "isHistorical": false,
    "state": "onHold",
    "journalEntry": {
      "key": null,
      "id": null
    },
    "computationMemo": "Between 2025-02-09 and 2025-02-28, partial period amount is 35000 for 20 days with daily rate 1750.",
    "meaDetails": "(35000 * 1 {line# 2})",
    "adjustedFor": null,
    "approvedHours": null,
    "sourceHours": null,
    "percentageRecognized": null,
    "audit": {
      "createdDateTime": "2025-08-22T17:08:46Z",
      "modifiedDateTime": "2025-08-22T22:50:04Z",
      "createdByUser": {
        "key": "1",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "linkedBillingScheduleLine": {
      "id": null,
      "key": null
    },
    "href": "/objects/contracts/revenue-schedule-line/4657"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/revenue-schedule/{key}
_Get a revenue schedule_

**Response 200 — Get a revenue schedule:**
```json
{
  "ia::result": {
    "key": "1578",
    "id": "1578",
    "journal": "J1",
    "contract": {
      "key": "143",
      "id": "Committed_Quantity_Billing",
      "href": "/objects/contracts/contract/143"
    },
    "contractLine": {
      "id": "387",
      "key": "387",
      "href": "/objects/contracts/contract-line/387"
    },
    "status": "inProgress",
    "audit": {
      "createdDateTime": "2025-02-15T03:03:31Z",
      "modifiedDateTime": "2025-02-15T03:03:32Z",
      "createdByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "createdBy": "159",
      "modifiedByUser": {
        "key": "159",
        "id": "Admin",
        "href": "/objects/company-config/user/159"
      },
      "modifiedBy": "159"
    },
    "estimateRevaluationDate": "2025-02-01",
    "revenueScheduleLines": [
      {
        "key": "14423",
        "id": "14423",
        "contractRevenueSchedule": {
          "id": "1578",
          "key": "1578",
          "href": "/objects/contracts/revenue-schedule/1578"
        },
        "scheduledAmount": "16666.66",
        "scheduledBaseAmount": "16666.66",
        "scheduledExchangeRate": "1.000000000000",
        "scheduledPostingDate": "2025-01-31",
        "actualPostingDate": "2025-01-31",
        "derivedPostingDate": "2025-01-31",
        "state": "open",
        "computationMemo": "MEA amount 1000, adjustment amount 333.32. Prorated amount before effective date 03/01/2025 is 0.",
        "meaDetails": "(1000 * 1 {line# 1})",
        "adjustedFor": "Contract modification, term reduced from 12 months to 6 months.",
        "approvedHours": "99",
        "sourceHours": "118",
        "percentageRecognized": "25.18",
        "audit": {
          "createdDateTime": "2025-02-15T03:03:31Z",
          "modifiedDateTime": "2025-02-15T03:03:32Z",
          "createdByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "createdBy": "159",
          "modifiedByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "modifiedBy": "159"
        },
        "linkedBillingScheduleLine": {
          "id": "145",
          "key": "145",
          "href": "/objects/contracts/billing-schedule-line/145"
        },
        "href": "/objects/contracts/revenue-schedule-line/14423"
      },
      {
        "key": "14424",
        "id": "14424",
        "contractRevenueSchedule": {
          "id": "1578",
          "key": "1578",
          "href": "/objects/contracts/revenue-schedule/1578"
        },
        "scheduledAmount": "16666.66",
        "scheduledBaseAmount": "16666.66",
        "scheduledExchangeRate": "1.000000000000",
        "scheduledPostingDate": "2025-02-28",
        "actualPostingDate": "2025-02-28",
        "derivedPostingDate": "2025-02-28",
        "posted": false,
        "isHistorical": false,
        "state": "open",
        "computationMemo": "MEA amount 1000, adjustment amount 333.32. Prorated amount before effective date 03/01/2025 is 0.",
        "meaDetails": "(1000 * 1 {line# 1})",
        "adjustedFor": "Contract modification, term reduced from 12 months to 6 months.",
        "approvedHours": "99",
        "sourceHours": "118",
        "percentageRecognized": "25.18",
        "audit": {
          "createdDateTime": "2025-02-15T03:03:31Z",
          "modifiedDateTime": "2025-02-15T03:03:32Z",
          "createdByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "createdBy": "159",
          "modifiedByUser": {
            "key": "159",
            "id": "Admin",
            "href": "/objects/company-config/user/159"
          },
          "modifiedBy": "159"
        },
        "linkedBillingScheduleLine": {
          "id": "145",
          "key": "145",
          "href": "/objects/contracts/billing-schedule-line/145"
        },
        "href": "/objects/contracts/revenue-schedule-line/14424"
      }
    ],
    "href": "/objects/contracts/revenue-schedule/1578"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/revenue-schedule/{key}
_Update a revenue schedule_

**Request example — Update a revenue schedule:**
```json
{
  "key": "145",
  "revenueScheduleLines": [
    {
      "key": "12",
      "computationMemo": "MEA amount 1000, adjustment amount 333.32. Prorated amount before effective date 03/01/2025 is 0.",
      "scheduledAmount": "125.34"
    }
  ]
}
```
**Response 200 — Reference to updated revenue schedule:**
```json
{
  "ia::result": {
    "key": "145",
    "id": "145",
    "href": "/objects/contracts/revenue-schedule/145"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/contracts/revenue-template
_List revenue templates_

**Response 200 — List revenue templates:**
```json
{
  "ia::result": [
    {
      "key": "26",
      "id": "Evergreen Revenue",
      "href": "/objects/contracts/revenue-template/26"
    },
    {
      "key": "18",
      "id": "Conprjobserved%compA",
      "href": "/objects/contracts/revenue-template/18"
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

## POST /objects/contracts/revenue-template
_Create a revenue template_

**Request example — Create a revenue template:**
```json
{
  "id": "PREDEFINED QUARTERLY",
  "description": "QUARTERLY RECOGNITION",
  "schedulePeriod": "monthly",
  "recognitionMethod": "predefinedPercentages",
  "recognitionSource": "estimatedHours",
  "stepRevenue": false,
  "revenueAdjustmentOption": null,
  "defaultPostingType": "manual",
  "status": "active",
  "isSystemGenerated": false,
  "recognitionPercentages": [
    {
      "monthsOffset": 0,
      "thresholdPercent": "60",
      "percentToRecognize": "20"
    },
    {
      "monthsOffset": 3,
      "thresholdPercent": "40",
      "percentToRecognize": "40"
    },
    {
      "monthsOffset": 5,
      "thresholdPercent": "25",
      "percentToRecognize": "25"
    },
    {
      "monthsOffset": 7,
      "thresholdPercent": "15",
      "percentToRecognize": "15"
    }
  ]
}
```
**Response 201 — Reference to new revenue template:**
```json
{
  "ia::result": {
    "key": "34",
    "id": "PREDEFINED QUARTERLY",
    "href": "/objects/contracts/revenue-template/34"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/contracts/revenue-template/{key}
_Get a revenue template_

**Response 200 — Get a revenue template:**
```json
{
  "ia::result": {
    "key": "25",
    "id": "PREDEFINED QUARTERLY",
    "description": "QUARTERLY RECOGNITION",
    "schedulePeriod": "monthly",
    "recognitionMethod": "predefinedPercentages",
    "recognitionSource": "estimatedHours",
    "stepRevenue": false,
    "revenueAdjustmentOption": null,
    "defaultPostingType": "manual",
    "status": "active",
    "isSystemGenerated": false,
    "audit": {
      "modifiedDateTime": "2023-09-26T07:35:01Z",
      "createdDateTime": "2019-04-26T06:00:38Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "recognitionPercentages": [
      {
        "monthsOffset": null,
        "thresholdPercent": "50.00",
        "percentToRecognize": "70.00"
      },
      {
        "monthsOffset": null,
        "thresholdPercent": "100.00",
        "percentToRecognize": "30.00"
      }
    ],
    "href": "/objects/contracts/revenue-template/25"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/contracts/revenue-template/{key}
_Update a revenue template_

**Request example — Update a revenue template:**
```json
{
  "description": "QUARTERLY RECOGNITION",
  "schedulePeriod": "monthly",
  "recognitionMethod": "predefinedPercentages",
  "recognitionSource": "estimatedHours",
  "stepRevenue": false,
  "revenueAdjustmentOption": null,
  "defaultPostingType": "manual",
  "status": "active",
  "recognitionPercentages": [
    {
      "monthsOffset": null,
      "thresholdPercent": "50.00",
      "percentToRecognize": "70.00"
    },
    {
      "monthsOffset": null,
      "thresholdPercent": "100.00",
      "percentToRecognize": "30.00"
    }
  ]
}
```
**Response 200 — Reference to updated revenue template:**
```json
{
  "ia::result": {
    "key": "25",
    "id": "PREDEFINED QUARTERLY",
    "href": "/objects/contracts/revenue-template/25"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/contracts/revenue-template/{key}
_Delete a revenue template_


## POST /services/contracts/expense-schedule/reallocate
_Reallocate an expense schedule_

**Request example — Request Example:**
```json
{
  "journal": "J1",
  "schedule": {
    "key": "546"
  },
  "startDate": "2022-02-24",
  "endDate": "2022-02-24",
  "postPastOpenPeriods": true
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "status": "completed"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /services/contracts/revenue-schedule/reallocate
_Reallocate a revenue schedule_

**Request example — Request Example:**
```json
{
  "journal": "J1",
  "schedule": {
    "key": "546"
  },
  "startDate": "2022-02-24",
  "endDate": "2022-02-24",
  "postPastOpenPeriods": true
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "status": "completed"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/contracts/contract-line/deliver
_Deliver a contract line_

**Request example — Deliver a contract line:**
```json
{
  "key": "895",
  "deliveryDate": "2025-01-01"
}
```
**Response 200 — Reference to contract line:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "delivered",
    "href": "/objects/contracts/contract-line/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract-line/hold-schedules
_Hold schedules for a contract line_

**Request example — Hold schedules for a contract line:**
```json
{
  "key": "895",
  "asOfDate": "2025-01-01",
  "memo": "Hold contract schedules for NetGen Technology Inc",
  "holdBilling": true,
  "holdRevenue": true,
  "holdExpense": false
}
```
**Response 200 — Reference to contract line with held schedules:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract-line/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract-line/post
_Post a contract line_

**Request example — Post a contract line:**
```json
{
  "key": "895",
  "glPostingDate": "2025-01-01",
  "postMemo": "Post a contract line to a draft contract for NetGen Technology Inc."
}
```
**Response 200 — Reference to contract line:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract-line/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract-line/reestimate
_Re-estimate a contract line_

**Request example — Re-estimate a contract line:**
```json
{
  "key": "895",
  "revaluedDate": "2025-01-01",
  "quantity": "2",
  "rate": "2",
  "flatFixedAmount": "4"
}
```
**Response 200 — Reference to contract line with revalued state:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "revalued",
    "href": "/objects/contracts/contract-line/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract-line/resume-schedules
_Resume schedules for a contract line_

**Request example — Resume schedules for a contract line:**
```json
{
  "key": "895",
  "asOfDate": "2025-01-01",
  "memo": "Resume schedules on the contract line for March.",
  "resumeBilling": true,
  "resumeRevenue": true,
  "resumeExpense": false,
  "revenueAdjustmentType": "oneTime"
}
```
**Response 200 — Reference to contract line with resumed schedules:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract-line/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract-line/revalue
_Revalue a contract line_

**Request example — Revalue a contract line:**
```json
{
  "key": "895",
  "revaluedDate": "2025-01-01"
}
```
**Response 200 — Reference to revalued contract line:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "revalued",
    "href": "/objects/contracts/contract-line/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract-line/uncancel
_Uncancel a contract line_

**Request example — Uncancel a contract line:**
```json
{
  "key": "895"
}
```
**Response 200 — Reference to the uncanceled contract line:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract-line/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract/clear-all-mea
_Clear all MEA allocations_

**Request example — Clear all MEA allocations for a contract:**
```json
{
  "key": "895"
}
```
**Response 200 — Reference to updated contract:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract/clear-last-active-mea
_Clear last active MEA allocation_

**Request example — Clear last active MEA allocation for a contract:**
```json
{
  "key": "895"
}
```
**Response 200 — Reference to updated contract:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract/expire
_Expire a contract_

**Request example — Expire a contract:**
```json
{
  "key": "895"
}
```
**Response 200 — Reference to expired contract:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "notRenewed",
    "href": "/objects/contracts/contract/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract/hold-schedules
_Hold contract schedules_

**Request example — Place contract schedules on hold:**
```json
{
  "key": "895",
  "contractLineKeys": "1539,1540",
  "asOfDate": "2024-01-01",
  "memo": "Hold billing and revenue schedule for Logic Solutions.",
  "holdBilling": true,
  "holdRevenue": true,
  "holdExpense": false
}
```
**Response 200 — Reference to updated contract:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract/post
_Post a contract_

**Request example — Post a contract:**
```json
{
  "key": "895",
  "glPostingDate": "2024-01-01",
  "postMemo": "Post draft service contract for service delivery tracking and invoicing."
}
```
**Response 200 — Reference to posted contract:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract/renew
_Renew a contract_

**Request example — Renew a contract:**
```json
{
  "key": "895"
}
```
**Response 200 — Reference to renewed contract:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "renewed",
    "href": "/objects/contracts/contract/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract/resume-schedules
_Resume contract schedules_

**Request example — Resume contract schedules:**
```json
{
  "key": "895",
  "contractLineKeys": "1539,1540",
  "asOfDate": "2024-01-01",
  "memo": "Resumed billing and revenue schedule for Logic Solutions.",
  "resumeBilling": true,
  "resumeRevenue": true,
  "resumeExpense": false,
  "revenueAdjustmentType": "oneTime"
}
```
**Response 200 — Reference to updated contract:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/contract/uncancel
_Uncancel a contract_

**Request example — Uncancel a contract:**
```json
{
  "key": "895"
}
```
**Response 200 — Reference to uncanceled contract:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/contract/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/expense-schedule-line/post
_Post an expense schedule line_

**Request example — Post an expense schedule line:**
```json
{
  "key": "12958",
  "actualPostingDate": "2025-01-31"
}
```
**Response 200 — Reference to expense schedule line:**
```json
{
  "ia::result": {
    "key": "12958",
    "state": "posted",
    "href": "/objects/contracts/expense-schedule-line/12958"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/expense-schedule-line/unpost
_Unpost an expense schedule line_

**Request example — Unpost an expense schedule line:**
```json
{
  "key": "12958"
}
```
**Response 200 — Reference to expense schedule line:**
```json
{
  "ia::result": {
    "key": "12958",
    "state": "open",
    "href": "/objects/contracts/expense-schedule-line/12958"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/expense/hold-schedules
_Hold a schedule for an expense_

**Request example — Hold a schedule for an expense:**
```json
{
  "key": "895",
  "asOfDate": "2025-01-01"
}
```
**Response 200 — Reference to expense with held schedule:**
```json
{
  "ia::result": {
    "key": "48",
    "state": "inProgress",
    "templates": {
      "expenseJournal1": {
        "schedule": {
          "id": "1563",
          "key": "1563",
          "status": "onHold",
          "href": "/objects/contracts/expense-schedule/1563"
        }
      },
      "expenseJournal2": {
        "schedule": {
          "id": "1564",
          "key": "1564",
          "status": "onHold",
          "href": "/objects/contracts/expense-schedule/1564"
        }
      }
    },
    "href": "/objects/contracts/expense/48"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/expense/post
_Post an expense_

**Request example — Post an expense:**
```json
{
  "key": "895",
  "glPostingDate": "2026-01-01",
  "postMemo": "Monthly payment for IT support as per contract 3462-HWQ."
}
```
**Response 200 — Reference to expense:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "href": "/objects/contracts/expense/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/expense/resume-schedules
_Resume an expense schedule_

**Request example — Resume expense schedule for an expense:**
```json
{
  "key": "895",
  "asOfDate": "2025-01-01"
}
```
**Response 200 — Reference to expense with resumed schedule:**
```json
{
  "ia::result": {
    "key": "895",
    "state": "inProgress",
    "templates": {
      "expenseJournal1": {
        "schedule": {
          "id": "1563",
          "key": "1563",
          "status": "inProgress",
          "href": "/objects/contracts/expense-schedule/1563"
        }
      },
      "expenseJournal2": {
        "schedule": {
          "id": "1564",
          "key": "1564",
          "status": "inProgress",
          "href": "/objects/contracts/expense-schedule/1564"
        }
      }
    },
    "href": "/objects/contracts/expense/895"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/revenue-schedule-line/post
_Post a revenue schedule line_

**Request example — Post a revenue schedule line:**
```json
{
  "key": "12958",
  "actualPostingDate": "2025-01-31"
}
```
**Response 200 — Reference to revenue schedule line:**
```json
{
  "ia::result": {
    "key": "12958",
    "state": "posted",
    "href": "/objects/contracts/revenue-schedule-line/12958"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /workflows/contracts/revenue-schedule-line/unpost
_Unpost a revenue schedule line_

**Request example — Unpost a revenue schedule line:**
```json
{
  "key": "12958"
}
```
**Response 200 — Reference to revenue schedule line:**
```json
{
  "ia::result": {
    "key": "12958",
    "state": "open",
    "href": "/objects/contracts/revenue-schedule-line/12958"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
