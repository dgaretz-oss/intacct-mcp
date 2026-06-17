# Accounts Payable

## GET /objects/accounts-payable/account-label
_List account labels_

**Response 200 — List account labels:**
```json
{
  "ia::result": [
    {
      "key": "32",
      "id": "Ref Matls",
      "href": "/objects/accounts-payable/account-label/32"
    },
    {
      "key": "33",
      "id": "Rent",
      "href": "/objects/accounts-payable/account-label/33"
    },
    {
      "key": "34",
      "id": "Repairs and Maintenance",
      "href": "/objects/accounts-payable/account-label/34"
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

## POST /objects/accounts-payable/account-label
_Create an account label_

**Request example — Create an account label:**
```json
{
  "id": "Sales",
  "description": "Sales team expenses",
  "status": "active",
  "glAccount": {
    "id": "4000--Sales"
  },
  "offsetGLAccount": {
    "id": "4001--Miscellaneous - Sales"
  }
}
```
**Response 201 — Create an account label:**
```json
{
  "ia::result": {
    "key": "37",
    "id": "Sales",
    "href": "/objects/accounts-payable/account-label/37"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/account-label/{key}
_Get an account label_

**Response 200 — Get an account label:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "Accounting Fees",
    "description": "Accounting Fees",
    "glAccount": {
      "id": "6600.01--Accounting Fees",
      "key": "318",
      "href": "/objects/general-ledger/account/318"
    },
    "status": "active",
    "offsetGLAccount": {
      "id": null,
      "key": null
    },
    "audit": {
      "modifiedDateTime": "2025-09-17T00:00:00Z",
      "createdDateTime": "2025-09-18T00:00:00Z",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1"
    },
    "form1099Type": "DIV",
    "form1099Box": "1B",
    "href": "/objects/accounts-payable/account-label/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/account-label/{key}
_Update an account label_

**Request example — Update an account label:**
```json
{
  "description": "This is Sales Account label",
  "status": "active",
  "offsetGLAccount": {
    "id": "4000.03--Sales-Others"
  }
}
```
**Response 200 — Update an account label:**
```json
{
  "ia::result": {
    "key": "37",
    "id": "Sales",
    "href": "/objects/accounts-payable/account-label/37"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/account-label/{key}
_Delete an account label_


## GET /objects/accounts-payable/adjustment
_List adjustments_

**Response 200 — List adjustments:**
```json
{
  "ia::result": [
    {
      "key": "186",
      "id": "186",
      "href": "/objects/accounts-payable/adjustment/186"
    },
    {
      "key": "187",
      "id": "187",
      "href": "/objects/accounts-payable/adjustment/187"
    },
    {
      "key": "319",
      "id": "319",
      "href": "/objects/accounts-payable/adjustment/319"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/accounts-payable/adjustment
_Create an adjustment_

**Request example — Create an adjustment:**
```json
{
  "adjustmentNumber": "ADJ124",
  "vendor": {
    "id": "GK183"
  },
  "createdDate": "2024-03-05",
  "currency": {
    "baseCurrency": "USD",
    "txnCurrency": "USD"
  },
  "lines": [
    {
      "glAccount": {
        "id": "2200"
      },
      "txnAmount": "150.00",
      "dimensions": {
        "department": {
          "id": "11"
        },
        "location": {
          "id": "CA"
        }
      }
    }
  ]
}
```
**Response 201 — Reference to new adjustment:**
```json
{
  "ia::result": {
    "key": "26",
    "id": "26",
    "href": "/objects/accounts-payable/adjustment/26"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/adjustment-line
_List adjustment lines_

**Response 200 — List adjustment lines:**
```json
{
  "ia::result": [
    {
      "key": "5336",
      "id": "5336",
      "href": "/objects/accounts-payable/adjustment-line/5336"
    },
    {
      "key": "5348",
      "id": "5348",
      "href": "/objects/accounts-payable/adjustment-line/5348"
    },
    {
      "key": "5296",
      "id": "5296",
      "href": "/objects/accounts-payable/adjustment-line/5296"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/accounts-payable/adjustment-line
_Create an adjustment line_

**Request example — Create an adjustment line:**
```json
{
  "apAdjustment": {
    "key": "89"
  },
  "accountLabel": {
    "id": "Bank Fees"
  },
  "txnAmount": "-1800.00",
  "totalTxnAmount": "-1800.00",
  "dimensions": {
    "location": {
      "id": "1"
    },
    "department": {
      "id": "4"
    }
  },
  "hasForm1099": "true",
  "form1099": {
    "type": "NEC",
    "box": "7"
  },
  "memo": "Created memo for adjustment line charges"
}
```
**Response 201 — Reference to new adjustment line:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/accounts-payable/adjustment-line/5",
    "ia::meta": {
      "totalCount": 1
    }
  }
}
```

## GET /objects/accounts-payable/adjustment-line/{key}
_Get an adjustment line_

**Response 200 — Get an adjustment line:**
```json
{
  "ia::result": {
    "id": "146",
    "key": "146",
    "apAdjustment": {
      "id": "24",
      "key": "24",
      "href": "/objects/accounts-payable/adjustment/24"
    },
    "glAccount": {
      "key": "246",
      "id": "6000",
      "name": "G&A Salaries",
      "href": "/objects/general-ledger/account/246"
    },
    "adjustmentAsset": {
      "key": "1",
      "id": "Asset 1",
      "name": "Asset 1",
      "href": "/objects/fixed-assets/asset/1"
    },
    "overrideOffsetGLAccount": {
      "key": "109",
      "id": "2000",
      "name": "Accounts Payable",
      "href": "/objects/general-ledger/account/109"
    },
    "accountLabel": {
      "key": null,
      "id": null
    },
    "baseAmount": "-318.23",
    "txnAmount": "-210.00",
    "dimensions": {
      "department": {
        "key": "9",
        "id": "11",
        "name": "Accounting",
        "href": "/objects/company-config/department/9"
      },
      "location": {
        "key": "4",
        "id": "4",
        "name": "Australia",
        "href": "/objects/company-config/location/4"
      },
      "project": {
        "key": "8",
        "id": "8",
        "name": "Client Services - Power Aerospace Materials",
        "href": "/objects/projects/project/8"
      },
      "customer": {
        "key": "1",
        "id": "1",
        "name": "Power Aerospace Materials",
        "href": "/objects/accounts-receivable/customer/1"
      },
      "vendor": {
        "key": "43",
        "id": "1099 Int",
        "name": "1099 Int",
        "href": "/objects/accounts-payable/vendor/43"
      },
      "employee": {
        "key": "1",
        "id": "1",
        "name": "Reser",
        "href": "/objects/company-config/employee/1"
      },
      "item": {
        "key": "12",
        "id": "12",
        "name": "PC Computer",
        "href": "/objects/inventory-control/item/12"
      },
      "class": {
        "key": "21",
        "id": "3",
        "name": "Health Care",
        "href": "/objects/company-config/class/21"
      }
    },
    "memo": "Adj for Bil -001",
    "currency": {
      "exchangeRate": {
        "date": "2024-03-08",
        "typeId": "-1",
        "rate": "1.5154"
      },
      "txnCurrency": "USD",
      "baseCurrency": "AUD"
    },
    "lineNumber": "1",
    "paymentInformation": {
      "totalBaseAmountPaid": "0.00",
      "txnTotalPaid": "0.00",
      "totalBaseAmountSelected": "0.00",
      "txnTotalSelected": "0.00"
    },
    "adjustmentType": "pa",
    "audit": {
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1",
      "createdDateTime": "2024-03-09T06:57:38Z",
      "modifiedDateTime": "2024-03-10T06:50:38Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1"
    },
    "hasForm1099": "false",
    "form1099": {
      "type": null,
      "box": null
    },
    "href": "/objects/accounts-payable/adjustment-line/146"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/adjustment-line/{key}
_Update an adjustment line_

**Request example — Update adjustment line with multiple fields:**
```json
{
  "txnAmount": "-12.00",
  "totalTxnAmount": "-12.00",
  "accountLabel": {
    "id": "Bank Interest Earned"
  },
  "dimensions": {
    "department": {
      "id": "3"
    },
    "location": {
      "id": "2"
    }
  },
  "memo": "Updated memo for adjustment-line"
}
```
**Response 200 — Update an adjustment line:**
```json
{
  "ia::result": {
    "key": "315783",
    "id": "315783",
    "href": "/objects/accounts-payable/adjustment-line/315783"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/adjustment-line/{key}
_Delete an adjustment line._


## GET /objects/accounts-payable/adjustment-summary
_List adjustment summaries_

**Response 200 — List adjustment summaries:**
```json
{
  "ia::result": [
    {
      "key": "13",
      "id": "13",
      "href": "/objects/accounts-payable/adjustment-summary/13"
    },
    {
      "key": "26",
      "id": "26",
      "href": "/objects/accounts-payable/adjustment-summary/26"
    },
    {
      "key": "20",
      "id": "20",
      "href": "/objects/accounts-payable/adjustment-summary/20"
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

## GET /objects/accounts-payable/adjustment-summary/{key}
_Get an adjustment summary_

**Response 200 — Get an adjustment summary:**
```json
{
  "ia::result": {
    "key": "13",
    "id": "13",
    "name": "Adjustments: 2019/01/18 Batch",
    "glPostingDate": "2019-01-18",
    "status": "active",
    "recordType": "apAdjustments",
    "totalAmount": "43.00",
    "state": "open",
    "parent": {
      "key": "null",
      "id": "null"
    },
    "preventGLPosting": false,
    "bankAccountId": {
      "key": "null",
      "id": "null"
    },
    "summaryCreationType": "system",
    "isQuickPaymentSummary": false,
    "audit": {
      "createdDateTime": "2019-01-18T11:10:49Z",
      "modifiedDateTime": "2019-01-19T10:10:49Z",
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
    "href": "/objects/accounts-payable/adjustment-summary/13"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/adjustment-tax-entry
_List adjustment tax entries_

**Response 200 — List adjustment tax entries:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "8",
      "href": "/objects/accounts-payable/adjustment-tax-entry/8"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/accounts-payable/adjustment-tax-entry/9"
    },
    {
      "key": "10",
      "id": "10",
      "href": "/objects/accounts-payable/adjustment-tax-entry/10"
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

## GET /objects/accounts-payable/adjustment-tax-entry/{key}
_Get an adjustment tax entry_

**Response 200 — Get an adjustment tax entry:**
```json
{
  "ia::result": {
    "key": "300",
    "id": "300",
    "baseTaxAmount": "100",
    "txnTaxAmount": "100",
    "taxRate": 5.5,
    "purchasingTaxDetail": {
      "id": "UK Export Reduced Rate",
      "key": "24",
      "href": "/objects/tax/purchasing-tax-detail/24"
    },
    "adjustmentLine": {
      "id": "148",
      "key": "148",
      "href": "/objects/accounts-payable/adjustment-line/148"
    },
    "href": "/objects/accounts-payable/adjustment-tax-entry/300"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/adjustment/{key}
_Get an adjustment_

**Response 200 — Get an adjustment:**
```json
{
  "ia::result": {
    "id": "67",
    "key": "67",
    "recordType": "pa",
    "adjustmentNumber": "credit-001",
    "state": "posted",
    "vendor": {
      "id": "1099 Int",
      "key": "1099 Int",
      "name": "1099 Int",
      "totalDue": "28.94",
      "href": "/objects/accounts-payable/vendor/1099 Int"
    },
    "referenceNumber": "Bill-001-02",
    "description": "Adj for Bil -001",
    "createdDate": "2024-03-05",
    "audit": {
      "createdDateTime": "2024-03-05T06:57:38Z",
      "modifiedDateTime": "2024-03-05T06:57:38Z",
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
    "adjustmentSummary": {
      "glPostingDate": "2024-03-05",
      "name": "Adjustments: 2024/03/05 Batch",
      "id": "45",
      "key": "45",
      "state": "open",
      "preventGLPosting": false,
      "href": "/objects/accounts-payable/adjustment-summary/45"
    },
    "currency": {
      "baseCurrency": "AUD",
      "txnCurrency": "USD",
      "exchangeRateDate": "2024-03-08",
      "exchangeRateTypeId": "Intacct Daily Rate",
      "exchangeRate": 1.5154
    },
    "totalEntered": "7.58",
    "totalBaseAmountDue": "7.58",
    "txnTotalEntered": "5.00",
    "txnTotalDue": "5.00",
    "contacts": {
      "payTo": {
        "id": "1099 Int",
        "key": "299",
        "href": "/objects/company-config/contact/299"
      },
      "returnTo": {
        "id": "1099 Int",
        "key": "299",
        "href": "/objects/company-config/contact/299"
      }
    },
    "attachment": {
      "id": "Adj_Bill_001",
      "key": "8",
      "href": "/objects/company-config/attachment/8"
    },
    "invoiceType": "invoice",
    "invoiceMode": "b1",
    "eInvoiceStatus": "paymentReceived",
    "moduleKey": "3.AP",
    "isTaxInclusive": false,
    "lines": [
      {
        "id": "700",
        "key": "700",
        "apAdjustment": {
          "id": "67",
          "key": "67",
          "href": "/objects/accounts-payable/adjustment/67"
        },
        "glAccount": {
          "key": "246",
          "id": "6000",
          "name": "G&A Salaries",
          "href": "/objects/general-ledger/account/246"
        },
        "adjustmentAsset": {
          "key": "1",
          "id": "Asset 1",
          "name": "Asset 1",
          "href": "/objects/fixed-assets/asset/1"
        },
        "overrideOffsetGLAccount": {
          "key": "109",
          "id": "2000",
          "name": "Accounts Payable",
          "href": "/objects/general-ledger/account/109"
        },
        "accountLabel": {
          "key": null,
          "id": null
        },
        "baseAmount": "7.58",
        "txnAmount": "5.00",
        "dimensions": {
          "department": {
            "key": "9",
            "id": "11",
            "name": "Accounting",
            "href": "/objects/company-config/department/9"
          },
          "location": {
            "key": "4",
            "id": "4",
            "name": "Australia",
            "href": "/objects/company-config/location/4"
          },
          "project": {
            "key": "8",
            "id": "8",
            "name": "Client Services - Power Aerospace Materials",
            "href": "/objects/projects/project/8"
          },
          "customer": {
            "key": "1",
            "id": "1",
            "name": "Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          },
          "vendor": {
            "key": "43",
            "id": "1099 Int",
            "name": "1099 Int",
            "href": "/objects/accounts-payable/vendor/43"
          },
          "employee": {
            "key": "1",
            "id": "1",
            "name": "Reser",
            "href": "/objects/company-config/employee/1"
          },
          "item": {
            "key": "1",
            "id": "1",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/1"
          },
          "class": {
            "key": "1",
            "id": "3",
            "name": "Heath Care",
            "href": "/objects/company-config/class/1"
          }
        },
        "memo": "Adj for Bil -001",
        "currency": {
          "exchangeRate": {
            "date": "2024-03-08",
            "typeId": "-1",
            "rate": "1.5154"
          },
          "txnCurrency": "USD",
          "baseCurrency": "AUD"
        },
        "lineNumber": "1",
        "paymentInformation": {
          "totalBaseAmountPaid": "0.00",
          "txnTotalPaid": "0.00",
          "totalBaseAmountSelected": "0.00",
          "txnTotalSelected": "0.00"
        },
        "adjustmentType": "pa",
        "audit": {
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "modifiedBy": "1",
          "createdDateTime": "2024-03-05T06:57:38Z",
          "modifiedDateTime": "2024-03-06T06:50:38Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "createdBy": "1"
        },
        "hasForm1099": "false",
        "href": "/objects/accounts-payable/adjustment-line/700"
      }
    ],
    "href": "/objects/accounts-payable/adjustment/67"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/adjustment/{key}
_Update an adjustment_

**Request example — Update an adjustment:**
```json
{
  "description": "Bill -001 adjustment-1"
}
```
**Response 200 — Reference to updated adjustment:**
```json
{
  "ia::result": {
    "key": "26",
    "id": "26",
    "href": "/objects/accounts-payable/adjustment/625459"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/adjustment/{key}
_Delete an adjustment_


## GET /objects/accounts-payable/advance
_List advances_

**Response 200 — List advances:**
```json
{
  "ia::result": [
    {
      "key": "625510",
      "id": "625510",
      "href": "/objects/accounts-payable/advance/625510"
    },
    {
      "key": "558105",
      "id": "558105",
      "href": "/objects/accounts-payable/advance/558105"
    },
    {
      "key": "558543",
      "id": "558543",
      "href": "/objects/accounts-payable/advance/558543"
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

## POST /objects/accounts-payable/advance
_Create an advance_

**Request example — Create an advance:**
```json
{
  "description": "Advance for new equipment",
  "paymentMethod": "cash",
  "financialEntity": {
    "entityId": "BOA"
  },
  "advanceDate": "2023-07-23",
  "vendor": {
    "id": "1099 Int"
  },
  "lines": [
    {
      "baseAmount": "12.34",
      "memo": "Advance payment to vendor for retainer fee - to be applied against future invoices.",
      "txnAmount": "1.23",
      "dimensions": {
        "department": {
          "id": "11"
        },
        "location": {
          "id": "1"
        },
        "project": {
          "id": "8"
        },
        "customer": {
          "id": "1"
        },
        "vendor": {
          "id": "1099 Int"
        },
        "employee": {
          "id": "1"
        },
        "item": {
          "id": "1"
        },
        "class": {
          "id": "3"
        }
      },
      "glAccount": {
        "id": "6000"
      }
    }
  ]
}
```
**Response 201 — Reference to new advance:**
```json
{
  "ia::result": {
    "key": "625530",
    "id": "625530",
    "href": "/objects/accounts-payable/advance/625530"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/advance-line
_List advance lines_

**Response 200 — List advance lines:**
```json
{
  "ia::result": [
    {
      "key": "1103722",
      "id": "1103722",
      "href": "/objects/accounts-payable/advance-line/1103722"
    },
    {
      "key": "5145328",
      "id": "5145328",
      "href": "/objects/accounts-payable/advance-line/5145328"
    },
    {
      "key": "5145339",
      "id": "5145339",
      "href": "/objects/accounts-payable/advance-line/5145339"
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

## GET /objects/accounts-payable/advance-line/{key}
_Get an advance line_

**Response 200 — Get an advance line:**
```json
{
  "ia::result": {
    "id": "39",
    "key": "39",
    "apAdvance": {
      "id": "20",
      "key": "20",
      "recordType": "pr",
      "href": "/objects/accounts-payable/advance/20"
    },
    "bank": {
      "amount": "120",
      "txnAmount": "120",
      "txnCurrency": "USD",
      "baseCurrency": "USD",
      "bankExchangeRate": {
        "date": "2025-01-23",
        "rate": 1,
        "typeId": "-1"
      }
    },
    "glAccount": {
      "key": "81",
      "id": "1304",
      "name": "Vendor Advances",
      "href": "/objects/general-ledger/account/81"
    },
    "accountLabel": {
      "id": null
    },
    "baseAmount": "120.00",
    "txnAmount": "120.00",
    "dimensions": {
      "department": {
        "key": "9",
        "id": "11",
        "name": "Accounting",
        "href": "/objects/company-config/department/9"
      },
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
      },
      "project": {
        "key": "8",
        "id": "8",
        "name": "Client Services - Power Aerospace Materials",
        "href": "/objects/projects/project/8"
      },
      "customer": {
        "key": "1",
        "id": "1",
        "name": "Power Aerospace Materials",
        "href": "/objects/accounts-receivable/customer/1"
      },
      "vendor": {
        "key": "43",
        "id": "1099 Int",
        "name": "1099 Int",
        "href": "/objects/accounts-payable/vendor/43"
      },
      "employee": {
        "key": "1",
        "id": "1",
        "name": "Reser",
        "href": "/objects/company-config/employee/1"
      },
      "item": {
        "key": "1",
        "id": "1",
        "name": "PC Computer",
        "href": "/objects/inventory-control/item/1"
      },
      "class": {
        "key": "1",
        "id": "3",
        "name": "Heath Care",
        "href": "/objects/company-config/class/1"
      },
      "nsp::refcode_gl": {
        "key": "10004",
        "href": "/objects/platform-apps/nsp::refcode_gl/10004"
      },
      "nsp::vssn": {
        "key": "10008",
        "href": "/objects/platform-apps/nsp::vssn/10008"
      },
      "nsp::restriction": {
        "key": null
      }
    },
    "baseLocation": {
      "name": "United States of America",
      "key": "1",
      "href": "/objects/company-config/location/1"
    },
    "memo": "Invc-001",
    "currency": {
      "exchangeRate": {
        "date": "2024-05-20",
        "typeId": null,
        "rate": "1"
      },
      "baseCurrency": "USD",
      "txnCurrency": "USD"
    },
    "lineNumber": 1,
    "paymentInformation": {
      "totalPaid": "0.00",
      "txnTotalPaid": "0.00",
      "totalSelected": "0.00",
      "txnTotalSelected": "0.00"
    },
    "audit": {
      "createdDateTime": "2024-05-20T11:16:41Z",
      "modifiedDateTime": "2024-05-21T10:57:23Z",
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
    "href": "/objects/accounts-payable/advance-line/39"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /objects/accounts-payable/advance-line/{key}
_Creates advance lines_

**Request example — Create an advance line:**
```json
{
  "apAdvance": {
    "key": "89"
  },
  "txnAmount": "2500.00",
  "baseAmount": "2500.00",
  "accountLabel": {
    "id": "Bank Fees"
  },
  "dimensions": {
    "location": {
      "id": "1"
    },
    "department": {
      "id": "4"
    }
  },
  "memo": "Created memo for advance line charges"
}
```
**Response 201 — Reference to new advance line:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/accounts-payable/advance-line/5",
    "ia::meta": {
      "totalCount": 1
    }
  }
}
```

## PATCH /objects/accounts-payable/advance-line/{key}
_Update advance lines_

**Request example — Update a single advance line:**
```json
{
  "txnAmount": "1300.00"
}
```
**Request example — Update advance lines:**
```json
{
  "txnAmount": "1300.00",
  "baseAmount": "1300.00",
  "accountLabel": {
    "id": "Bank Interest Earned"
  },
  "dimensions": {
    "department": {
      "id": "3"
    },
    "location": {
      "id": "2"
    }
  },
  "memo": "Updated memo for advance-line"
}
```
**Response 201 — Reference to new advance line:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/accounts-payable/advance-line/5",
    "ia::meta": {
      "totalCount": 1
    }
  }
}
```

## DELETE /objects/accounts-payable/advance-line/{key}
_Delete advance lines_


## GET /objects/accounts-payable/advance/{key}
_Get an advance_

**Response 200 — Get an advance:**
```json
{
  "ia::result": {
    "id": "20",
    "key": "20",
    "recordType": "pr",
    "paymentMethod": "eft",
    "description": null,
    "advanceNumber": "Advance-001",
    "advanceSummary": {
      "id": "399",
      "key": "399",
      "name": "Advances(Bank-BOA) 2024/10/23 21:21:03:5361 Batch",
      "href": "/objects/accounts-payable/summary/399"
    },
    "vendor": {
      "name": "1099 Int",
      "id": "1099 Int",
      "key": "43",
      "totalDue": "-120.00",
      "href": "/objects/accounts-payable/vendor/43"
    },
    "totalEntered": "120.00",
    "paymentInformation": {
      "totalPaid": "0.00",
      "totalSelected": "0.00",
      "paidDate": "2024-05-20",
      "txnTotalPaid": "0.00",
      "txnTotalSelected": "0.00"
    },
    "totalDue": "120.00",
    "state": "advancePaid",
    "audit": {
      "createdDateTime": "2024-05-20T11:16:41Z",
      "modifiedDateTime": "2024-05-20T11:16:41Z",
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
    "entity": {
      "id": "1",
      "key": "1",
      "name": "United States of America"
    },
    "dueDate": "2024-05-20",
    "referenceNumber": "Advace for 1099 Int",
    "reconciliationGroup": {
      "cleared": "false",
      "clearingDate": null
    },
    "isSystemGenerated": "false",
    "currency": {
      "txnCurrency": "USD",
      "baseCurrency": "USD",
      "exchangeRate": {
        "date": null,
        "typeId": null,
        "rate": null
      }
    },
    "txnTotalEntered": "120.00",
    "txnTotalDue": "120.00",
    "location": {
      "key": "1"
    },
    "financialEntity": {
      "entityId": "BOA",
      "currency": "USD",
      "txnAmount": "120.00",
      "baseAmount": "120.00",
      "baseCurrency": "USD"
    },
    "advanceDate": "2024-05-20",
    "attachment": {
      "id": "Invc-001",
      "key": "2",
      "href": "/objects/company-config/attachment/2"
    },
    "lines": [
      {
        "id": "39",
        "key": "39",
        "apAdvance": {
          "id": "20",
          "key": "20",
          "recordType": "pr",
          "href": "/objects/accounts-payable/advance/20"
        },
        "glAccount": {
          "key": "81",
          "id": "1304",
          "name": "Vendor Advances",
          "href": "/objects/general-ledger/account/81"
        },
        "accountLabel": {
          "id": null
        },
        "baseAmount": "120.00",
        "txnAmount": "120.00",
        "dimensions": {
          "department": {
            "key": "9",
            "id": "11",
            "name": "Accounting",
            "href": "/objects/company-config/department/9"
          },
          "location": {
            "key": "1",
            "id": "1",
            "name": "United States of America",
            "href": "/objects/company-config/location/1"
          },
          "project": {
            "key": "8",
            "id": "8",
            "name": "Client Services - Power Aerospace Materials",
            "href": "/objects/projects/project/8"
          },
          "customer": {
            "key": "1",
            "id": "1",
            "name": "Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          },
          "vendor": {
            "key": "43",
            "id": "1099 Int",
            "name": "1099 Int",
            "href": "/objects/accounts-payable/vendor/43"
          },
          "employee": {
            "key": "1",
            "id": "1",
            "name": "Reser",
            "href": "/objects/company-config/employee/1"
          },
          "item": {
            "key": "1",
            "id": "1",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/1"
          },
          "class": {
            "key": "1",
            "id": "3",
            "name": "Heath Care",
            "href": "/objects/company-config/class/1"
          },
          "nsp::refcode_gl": {
            "key": "10004",
            "href": "/objects/platform-apps/nsp::refcode_gl/10004"
          },
          "nsp::vssn": {
            "key": "10008",
            "href": "/objects/platform-apps/nsp::vssn/10008"
          },
          "nsp::restriction": {
            "key": null
          }
        },
        "baseLocation": {
          "name": "United States of America",
          "key": "1",
          "href": "/objects/company-config/location/1"
        },
        "memo": "Invc-001",
        "currency": {
          "exchangeRate": {
            "date": "2024-05-20",
            "typeId": null,
            "rate": "1"
          },
          "baseCurrency": "USD",
          "txnCurrency": "USD"
        },
        "lineNumber": 1,
        "paymentInformation": {
          "totalPaid": "0.00",
          "txnTotalPaid": "0.00",
          "totalSelected": "0.00",
          "txnTotalSelected": "0.00"
        },
        "audit": {
          "createdDateTime": "2024-05-20T11:16:41Z",
          "modifiedDateTime": "2024-05-21T10:57:23Z",
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
        "href": "/objects/accounts-payable/advance-line/39"
      }
    ],
    "href": "/objects/accounts-payable/advance/20"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/advance/{key}
_Update an advance_

**Request example — Update an advance:**
```json
{
  "description": "Updated description of advance"
}
```
**Response 200 — Reference to updated advance:**
```json
{
  "ia::result": {
    "key": "625529",
    "id": "625529",
    "href": "/objects/accounts-payable/advance/625529"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/advance/{key}
_Delete an advance_


## GET /objects/accounts-payable/bill
_List bills_

**Response 200 — List bills:**
```json
{
  "ia::result": [
    {
      "key": "299",
      "id": "299",
      "href": "/objects/accounts-payable/bill/299"
    },
    {
      "key": "294",
      "id": "294",
      "href": "/objects/accounts-payable/bill/294"
    },
    {
      "key": "295",
      "id": "295",
      "href": "/objects/accounts-payable/bill/295"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/accounts-payable/bill
_Create a bill_

**Request example — Create a bill:**
```json
{
  "billNumber": "Bill-001-06",
  "vendor": {
    "id": "1099 Int"
  },
  "referenceNumber": "Ref-123",
  "description": "bill - 001 - vendor 1099",
  "createdDate": "2024-02-21",
  "postingDate": "2024-02-21",
  "discountCutOffDate": "2024-03-01",
  "dueDate": "2024-03-08",
  "recommendedPaymentDate": "2024-02-26",
  "paymentPriority": "normal",
  "isOnHold": false,
  "currency": {
    "baseCurrency": "USD",
    "txnCurrency": "USD",
    "exchangeRate": {
      "date": "2022-02-21",
      "typeId": "Intacct Daily Rate",
      "rate": 1.0679
    }
  },
  "contacts": {
    "payTo": {
      "id": "1099 Int"
    },
    "returnTo": {
      "id": "1099 Int"
    }
  },
  "attachment": {
    "id": "atch1"
  },
  "isTaxInclusive": false,
  "lines": [
    {
      "glAccount": {
        "id": "6000"
      },
      "txnAmount": "5",
      "totalTxnAmount": "15.00",
      "dimensions": {
        "location": {
          "id": "4"
        },
        "department": {
          "id": "11"
        },
        "project": {
          "id": "8"
        },
        "customer": {
          "id": "1"
        },
        "vendor": {
          "id": "1099 Int"
        },
        "employee": {
          "id": "15"
        },
        "item": {
          "id": "12"
        },
        "class": {
          "id": "3"
        }
      },
      "memo": "bill - 001 - vendor 1099",
      "hasForm1099": "false",
      "project": {
        "isBillable": false
      }
    }
  ]
}
```
**Response 201 — Reference to new bill:**
```json
{
  "ia::result": {
    "key": "299",
    "id": "299",
    "href": "/objects/accounts-payable/bill/299"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/bill-line
_List bill lines_

**Response 200 — List bill lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/accounts-payable/bill-line/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/accounts-payable/bill-line/3"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/accounts-payable/bill-line/5"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/accounts-payable/bill-line
_Create bill lines_

**Request example — Create a bill line:**
```json
{
  "bill": {
    "key": "11579"
  },
  "txnAmount": "2500",
  "totalTxnAmount": "2500",
  "glAccount": {
    "key": "254"
  },
  "overrideOffsetGLAccount": {
    "key": "359"
  },
  "accountLabel": {
    "key": "28"
  },
  "dimensions": {
    "location": {
      "key": "1"
    },
    "vendor": {
      "id": "209"
    },
    "department": {
      "id": "77"
    },
    "project": {
      "key": "27"
    },
    "customer": {
      "id": "HC"
    },
    "employee": {
      "id": "EMP1-US"
    },
    "item": {
      "id": "GAMESUBKEY"
    },
    "class": {
      "id": "3"
    },
    "warehouse": {
      "id": "33"
    },
    "task": {
      "id": "619"
    }
  },
  "hasForm1099": "true",
  "releaseToPay": true,
  "project": {
    "isBillable": true
  },
  "form1099": {
    "type": "NEC",
    "box": "7"
  },
  "fixedAsset": {
    "nameOfAcquiredAsset": "ergonomic chair",
    "includeTaxInAssetCost": false
  },
  "memo": "server charges bill"
}
```
**Response 200 — New bill lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/accounts-payable/bill-line/1"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/accounts-payable/bill-line/{key}
_Get a bill line_

**Response 200 — Get a bill line:**
```json
{
  "ia::result": {
    "id": "94",
    "key": "94",
    "bill": {
      "id": "18",
      "key": "18",
      "href": "/objects/accounts-payable/bill/18"
    },
    "glAccount": {
      "key": "246",
      "id": "6000",
      "name": "G&A Salaries",
      "href": "/objects/general-ledger/account/246"
    },
    "overrideOffsetGLAccount": {
      "key": "109",
      "id": "2000",
      "name": "Accounts Payable",
      "href": "/objects/general-ledger/account/109"
    },
    "accountLabel": {
      "key": null,
      "id": null
    },
    "createdDate": "2024-02-21",
    "baseAmount": "48550.00",
    "txnAmount": "48550.00",
    "dimensions": {
      "department": {
        "key": "9",
        "id": "11",
        "name": "Accounting",
        "href": "/objects/company-config/department/9"
      },
      "location": {
        "key": "4",
        "id": "4",
        "name": "Australia",
        "href": "/objects/company-config/location/4"
      },
      "project": {
        "key": "8",
        "id": "8",
        "name": "Client Services - Power Aerospace Materials",
        "href": "/objects/projects/project/8"
      },
      "customer": {
        "key": "1",
        "id": "1",
        "name": "Power Aerospace Materials",
        "href": "/objects/accounts-receivable/customer/1"
      },
      "vendor": {
        "key": "43",
        "id": "1099 Int",
        "name": "1099 Int",
        "href": "/objects/accounts-payable/vendor/43"
      },
      "employee": {
        "key": "1",
        "id": "1",
        "name": "Reser",
        "href": "/objects/company-config/employee/1"
      },
      "item": {
        "key": "1",
        "id": "1",
        "name": "PC Computer",
        "href": "/objects/inventory-control/item/1"
      },
      "class": {
        "key": "1",
        "id": "3",
        "name": "Health Care",
        "href": "/objects/company-config/class/1"
      },
      "warehouse": {
        "key": "2",
        "id": "Distribution",
        "name": "Distribution center",
        "href": "/objects/inventory-control/warehouse/2"
      },
      "contract": {
        "key": null,
        "id": null,
        "name": null
      },
      "task": {
        "key": null,
        "id": null,
        "name": null
      }
    },
    "baseLocation": {
      "name": "Australia",
      "key": "4",
      "href": "/objects/company-config/location/4"
    },
    "memo": "bill - 001 - vendor 1099",
    "currency": {
      "exchangeRate": {
        "date": "2024-02-21",
        "typeId": "-99",
        "rate": 1.0679
      },
      "txnCurrency": "USD",
      "baseCurrency": "AUD"
    },
    "allocation": {
      "name": null,
      "id": null,
      "key": null
    },
    "hasForm1099": "false",
    "lineNumber": "1",
    "paymentInformation": {
      "totalBaseAmountPaid": "0.00",
      "totalTxnAmountPaid": "0.00",
      "totalBaseAmountSelectedForPayment": "48550.00",
      "totalTxnAmountSelectedForPayment": "48550.00"
    },
    "project": {
      "isBillable": false,
      "isBilled": false
    },
    "releaseToPay": false,
    "form1099": {
      "type": null,
      "box": null
    },
    "audit": {
      "createdDateTime": "2024-02-01T08:29:09Z",
      "modifiedDateTime": "2024-02-01T08:29:09Z",
      "createdByUser": {
        "key": "81",
        "id": "Abhilash",
        "href": "/objects/company-config/user/81"
      },
      "createdBy": "81",
      "modifiedByUser": {
        "key": "81",
        "id": "Abhilash",
        "href": "/objects/company-config/user/81"
      },
      "modifiedBy": "81"
    },
    "retainage": {
      "percentage": null,
      "txnAmountRetained": null,
      "baseAmountRetained": null,
      "hasRetainage": null,
      "txnAmountReleased": null,
      "release": null
    },
    "isSubTotal": null,
    "purchasing": {
      "document": {
        "key": null,
        "id": null
      },
      "documentLine": {
        "key": null,
        "id": null
      }
    },
    "fixedAsset": {
      "nameOfAcquiredAsset": null,
      "includeTaxInAssetCost": false,
      "assetCreationMode": "createFixedAsset",
      "assetQuantity": 2
    },
    "href": "/objects/accounts-payable/bill-line/94"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/bill-line/{key}
_Update a bill line_

**Request example — Update a single value:**
```json
{
  "txnAmount": "2400"
}
```
**Request example — Update multiple values:**
```json
{
  "txnAmount": "400",
  "glAccount": {
    "key": "254"
  },
  "dimensions": {
    "location": {
      "key": "2"
    },
    "vendor": {
      "id": "1099 Int"
    },
    "department": {
      "id": "77"
    },
    "project": {
      "key": "27"
    },
    "customer": {
      "id": "HC"
    },
    "employee": {
      "id": "EMP1-US"
    },
    "item": {
      "id": "GAMESUBKEY"
    },
    "class": {
      "id\"": "3"
    },
    "warehouse": {
      "id": "33"
    },
    "task": {
      "id": "619"
    }
  },
  "hasForm1099": "true",
  "releaseToPay": true,
  "form1099": {
    "type": "NEC",
    "box": "7"
  },
  "baseLocation": {
    "key": "4"
  },
  "fixedAsset": {
    "nameOfAcquiredAsset": "ergonomic chair",
    "includeTaxInAssetCost": false
  },
  "project": {
    "isBillable": true
  },
  "memo": "server charges bill"
}
```
**Response 200 — Reference to updated bill line:**
```json
{
  "ia::result": {
    "key": "63",
    "id": "198376",
    "href": "/objects/accounts-payable/bill-line/63"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/accounts-payable/bill-line/{key}
_Delete a bill line_


## GET /objects/accounts-payable/bill-summary
_List bill summaries_

**Response 200 — List bill summaries:**
```json
{
  "ia::result": [
    {
      "key": "94",
      "id": "94",
      "href": "/objects/accounts-payable/bill-summary/94"
    },
    {
      "key": "96",
      "id": "96",
      "href": "/objects/accounts-payable/bill-summary/96"
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

## GET /objects/accounts-payable/bill-summary/{key}
_Get a bill summary_

**Response 200 — Get a bill summary:**
```json
{
  "ia::result": {
    "id": "98",
    "key": "98",
    "name": "Bills: 2022/08/02 Batch",
    "glPostingDate": "2022-08-02",
    "status": "active",
    "recordType": "apBill",
    "totalAmount": "100.23",
    "state": "open",
    "parent": {
      "id": null,
      "key": null
    },
    "preventGLPosting": false,
    "bankAccountId": {
      "id": null,
      "key": null
    },
    "summaryCreationType": "Auto-Summary",
    "isQuickPaymentSummary": false,
    "audit": {
      "createdDateTime": "2022-08-02T10:15:31Z",
      "modifiedDateTime": "2022-08-02T10:25:30Z",
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
    "href": "/objects/accounts-payable/bill-summary/98"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/bill-tax-entry
_List bill tax entries_

**Response 200 — List bill tax entries:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "8",
      "href": "/objects/accounts-payable/bill-tax-entry/8"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/accounts-payable/bill-tax-entry/9"
    },
    {
      "key": "10",
      "id": "10",
      "href": "/objects/accounts-payable/bill-tax-entry/10"
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

## GET /objects/accounts-payable/bill-tax-entry/{key}
_Get a bill tax entry_

**Response 200 — Get a bill tax entry:**
```json
{
  "ia::result": {
    "key": "300",
    "id": "300",
    "baseTaxAmount": "100",
    "txnTaxAmount": "100",
    "taxRate": 5.5,
    "purchasingTaxDetail": {
      "id": "UK Export Reduced Rate",
      "key": "24",
      "href": "/objects/tax/purchasing-tax-detail/24"
    },
    "billLine": {
      "id": "148",
      "key": "148",
      "href": "/objects/accounts-payable/bill-line/148"
    },
    "href": "/objects/accounts-payable/bill-tax-entry/300"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/bill/{key}
_Get a bill_

**Response 200 — Get a bill:**
```json
{
  "ia::result": {
    "id": "60",
    "key": "60",
    "recordType": "pi",
    "billNumber": "Bill-001-06",
    "moduleName": "accountsPayable",
    "state": "posted",
    "vendor": {
      "id": "1099 Int",
      "name": "1099 Int",
      "key": "43",
      "form1099": {
        "type": null,
        "box": null,
        "vendorTypeForm1099Type": null
      },
      "vendorDue": "21.36",
      "href": "/objects/accounts-payable/vendor/43"
    },
    "referenceNumber": "Ref-123",
    "description": "bill - 001 - vendor 1099",
    "purchasingDocument": {
      "id": "Vendor Invoice-VI0031-doc",
      "key": "416",
      "href": "/objects/purchasing/document/416"
    },
    "term": {
      "id": "NET-30",
      "key": "3",
      "href": "/objects/accounts-payable/term/3"
    },
    "createdDate": "2022-02-21",
    "audit": {
      "createdDateTime": "2024-02-21T00:00:00Z",
      "modifiedDateTime": "2024-03-20T08:31:41Z",
      "createdBy": "95",
      "modifiedBy": "95"
    },
    "postingDate": "2024-02-21",
    "discountCutOffDate": "2024-02-21",
    "dueDate": "2024-03-08",
    "paymentInformation": {
      "fullyPaidDate": null,
      "totalBaseAmountSelectedForPayment": "0.00",
      "totalBaseAmountPaid": "0.00",
      "totalTxnAmountSelectedForPayment": "0.00",
      "totalTxnAmountPaid": "0.00"
    },
    "recommendedPaymentDate": "2024-02-26",
    "paymentPriority": "normal",
    "isOnHold": false,
    "currency": {
      "baseCurrency": "AUD",
      "txnCurrency": "USD",
      "exchangeRate": {
        "date": "2024-02-21",
        "typeId": "Custom",
        "rate": 1.0679
      }
    },
    "totalBaseAmount": "100.68",
    "totalBaseAmountDue": "100.68",
    "totalTxnAmount": "100.00",
    "totalTxnAmountDue": "100.00",
    "contacts": {
      "payTo": {
        "id": "1099 Int",
        "key": "299",
        "tax": {
          "group": {
            "id": null,
            "key": null
          },
          "taxId": null
        },
        "href": "/objects/company-config/contact/299"
      },
      "returnTo": {
        "id": "1099 Int",
        "key": "299",
        "href": "/objects/company-config/contact/299"
      }
    },
    "billSummary": {
      "name": "Bills: 2022/02/21 Batch",
      "id": "37",
      "key": "37",
      "isSummaryOpen": "open",
      "isSummaryPosted": "false",
      "href": "/objects/accounts-payable/bill-summary/37"
    },
    "recurringSchedule": {
      "id": "20",
      "key": "20",
      "href": "/objects/core/schedule/20"
    },
    "isSystemGenerated": false,
    "dueInDays": "23",
    "isTaxInclusive": false,
    "taxSolution": {
      "key": null,
      "id": null,
      "showMultiLineTax": null,
      "method": null,
      "taxCalculationMethod": null
    },
    "retainage": {
      "defaultPercentage": null,
      "totalTxnAmountRetained": "0.00",
      "totalTxnAmountReleased": "0.00",
      "totalBaseAmountRetained": "0.00"
    },
    "attachment": {
      "id": "atch1",
      "key": "6",
      "href": "/objects/company-config/attachment/6"
    },
    "customerRefund": {
      "id": "RF-1",
      "key": "1",
      "href": "/objects/accounts-receivable/customer-refund/1"
    },
    "documentSource": "billUpload",
    "importStatus": "resolve",
    "importErrorMessage": "Failed to upload the file info to STX [Support ID: IGHSzWEB002%7EZusFKP3t0u-8kc5-M9eO1gAAAAM]",
    "recipientEmail": null,
    "senderEmail": null,
    "sourceModule": "accountsPayable",
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "lines": [
      {
        "id": "440",
        "key": "440",
        "bill": {
          "id": "60",
          "key": "60",
          "href": "/objects/accounts-payable/bill/60"
        },
        "glAccount": {
          "key": "246",
          "id": "6000",
          "name": "G&A Salaries",
          "href": "/objects/general-ledger/account/246"
        },
        "overrideOffsetGLAccount": {
          "key": "109",
          "id": "2000",
          "name": "Accounts Payable",
          "href": "/objects/general-ledger/account/109"
        },
        "accountLabel": {
          "key": null,
          "id": null
        },
        "createdDate": "2022-02-21",
        "baseAmount": "5.34",
        "txnAmount": "5.00",
        "dimensions": {
          "department": {
            "key": "9",
            "id": "11",
            "name": "Accounting",
            "href": "/objects/company-config/department/9"
          },
          "location": {
            "key": "4",
            "id": "4",
            "name": "Australia",
            "href": "/objects/company-config/location/4"
          },
          "project": {
            "key": "8",
            "id": "8",
            "name": "Client Services - Power Aerospace Materials",
            "href": "/objects/projects/project/8"
          },
          "customer": {
            "key": "1",
            "id": "1",
            "name": "Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          },
          "vendor": {
            "key": "43",
            "id": "1099 Int",
            "name": "1099 Int",
            "href": "/objects/accounts-payable/vendor/43"
          },
          "employee": {
            "key": "1",
            "id": "1",
            "name": "Reser",
            "href": "/objects/company-config/employee/1"
          },
          "item": {
            "key": "1",
            "id": "1",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/1"
          },
          "class": {
            "key": "1",
            "id": "3",
            "name": "Health Care",
            "href": "/objects/company-config/class/1"
          },
          "warehouse": {
            "key": null,
            "id": null,
            "name": null
          },
          "contract": {
            "key": null,
            "id": null,
            "name": null
          },
          "task": {
            "key": null,
            "id": null,
            "name": null
          }
        },
        "baseLocation": {
          "name": "Australia",
          "key": "4",
          "href": "/objects/company-config/location/4"
        },
        "memo": "bill - 001 - vendor 1099",
        "currency": {
          "exchangeRate": {
            "date": "2022-02-21",
            "typeId": "-99",
            "rate": 1.0679
          },
          "txnCurrency": "USD",
          "baseCurrency": "AUD"
        },
        "allocation": {
          "id": null,
          "key": null
        },
        "hasForm1099": "false",
        "lineNumber": "1",
        "paymentInformation": {
          "totalBaseAmountPaid": "0.00",
          "totalTxnAmountPaid": "0.00",
          "totalBaseAmountSelectedForPayment": "0.00",
          "totalTxnAmountSelectedForPayment": "0.00"
        },
        "project": {
          "isBillable": false,
          "isBilled": false
        },
        "releaseToPay": false,
        "form1099": {
          "type": null,
          "box": null
        },
        "retainage": {
          "percentage": "10",
          "txnAmountRetained": "100",
          "baseAmountRetained": "50",
          "hasRetainage": false,
          "txmAmountReleased": "50",
          "release": false
        },
        "isSubtotal": false,
        "purchasing": {
          "document": {
            "key": "23",
            "id": "23"
          },
          "documentLine": {
            "key": "23",
            "id": "23"
          }
        },
        "fixedAsset": {
          "nameOfAcquiredAsset": null,
          "includeTaxInAssetCost": false,
          "assetCreationMode": "createFixedAsset",
          "assetQuantity": 2
        },
        "href": "/objects/accounts-payable/bill-line/440"
      }
    ],
    "href": "/objects/accounts-payable/bill/60"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a bill (France E-invoicing):**
```json
{
  "ia::result": {
    "id": "60",
    "key": "60",
    "recordType": "pi",
    "billNumber": "Bill-001-06",
    "moduleName": "accountsPayable",
    "state": "posted",
    "vendor": {
      "id": "1099 Int",
      "name": "1099 Int",
      "key": "43",
      "form1099": {
        "type": null,
        "box": null,
        "vendorTypeForm1099Type": null
      },
      "vendorDue": "21.36",
      "href": "/objects/accounts-payable/vendor/43"
    },
    "referenceNumber": "Ref-123",
    "description": "bill - 001 - vendor 1099",
    "purchasingDocument": {
      "id": "Vendor Invoice-VI0031-doc",
      "key": "416",
      "href": "/objects/purchasing/document/416"
    },
    "term": {
      "id": "NET-30",
      "key": "3",
      "href": "/objects/accounts-payable/term/3"
    },
    "createdDate": "2022-02-21",
    "audit": {
      "createdDateTime": "2024-02-21T00:00:00Z",
      "modifiedDateTime": "2024-03-20T08:31:41Z",
      "createdBy": "95",
      "modifiedBy": "95"
    },
    "postingDate": "2024-02-21",
    "discountCutOffDate": "2024-02-21",
    "dueDate": "2024-03-08",
    "paymentInformation": {
      "fullyPaidDate": null,
      "totalBaseAmountSelectedForPayment": "0.00",
      "totalBaseAmountPaid": "0.00",
      "totalTxnAmountSelectedForPayment": "0.00",
      "totalTxnAmountPaid": "0.00"
    },
    "recommendedPaymentDate": "2024-02-26",
    "paymentPriority": "normal",
    "isOnHold": false,
    "currency": {
      "baseCurrency": "AUD",
      "txnCurrency": "USD",
      "exchangeRate": {
        "date": "2024-02-21",
        "typeId": "Custom",
        "rate": 1.0679
      }
    },
    "totalBaseAmount": "100.68",
    "totalBaseAmountDue": "100.68",
    "totalTxnAmount": "100.00",
    "totalTxnAmountDue": "100.00",
    "contacts": {
      "payTo": {
        "id": "1099 Int",
        "key": "299",
        "tax": {
          "group": {
            "id": null,
            "key": null
          },
          "taxId": null
        },
        "href": "/objects/company-config/contact/299"
      },
      "returnTo": {
        "id": "1099 Int",
        "key": "299",
        "href": "/objects/company-config/contact/299"
      }
    },
    "billSummary": {
      "name": "Bills: 2022/02/21 Batch",
      "id": "37",
      "key": "37",
      "isSummaryOpen": "open",
      "isSummaryPosted": "false",
      "href": "/objects/accounts-payable/bill-summary/37"
    },
    "recurringSchedule": {
      "id": "20",
      "key": "20",
      "href": "/objects/core/schedule/20"
    },
    "isSystemGenerated": false,
    "dueInDays": "23",
    "isTaxInclusive": false,
    "taxSolution": {
      "key": null,
      "id": null,
      "showMultiLineTax": null,
      "method": null,
      "taxCalculationMethod": null
    },
    "retainage": {
      "defaultPercentage": null,
      "totalTxnAmountRetained": "0.00",
      "totalTxnAmountReleased": "0.00",
      "totalBaseAmountRetained": "0.00"
    },
    "attachment": {
      "id": "atch1",
      "key": "6",
      "href": "/objects/company-config/attachment/6"
    },
    "documentSource": "billUpload",
    "importStatus": "resolve",
    "importErrorMessage": "Failed to upload the file info to STX [Support ID: IGHSzWEB002%7EZusFKP3t0u-8kc5-M9eO1gAAAAM]",
    "recipientEmail": null,
    "senderEmail": null,
    "sourceModule": "accountsPayable",
    "invoiceType": "invoice",
    "invoiceMode": "b1",
    "eInvoiceStatus": "paymentReceived",
    "dispute": {
      "reason": "recipientNotConnected",
      "notes": "Does not have an active invoice receiving address"
    },
    "refuse": {
      "reason": "incorrectVATRate",
      "notes": "The VAT rate used is not the one that should have been"
    },
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "lines": [
      {
        "id": "440",
        "key": "440",
        "bill": {
          "id": "60",
          "key": "60",
          "href": "/objects/accounts-payable/bill/60"
        },
        "glAccount": {
          "key": "246",
          "id": "6000",
          "name": "G&A Salaries",
          "href": "/objects/general-ledger/account/246"
        },
        "overrideOffsetGLAccount": {
          "key": "109",
          "id": "2000",
          "name": "Accounts Payable",
          "href": "/objects/general-ledger/account/109"
        },
        "accountLabel": {
          "key": null,
          "id": null
        },
        "createdDate": "2022-02-21",
        "baseAmount": "5.34",
        "txnAmount": "5.00",
        "dimensions": {
          "department": {
            "key": "9",
            "id": "11",
            "name": "Accounting",
            "href": "/objects/company-config/department/9"
          },
          "location": {
            "key": "4",
            "id": "4",
            "name": "Australia",
            "href": "/objects/company-config/location/4"
          },
          "project": {
            "key": "8",
            "id": "8",
            "name": "Client Services - Power Aerospace Materials",
            "href": "/objects/projects/project/8"
          },
          "customer": {
            "key": "1",
            "id": "1",
            "name": "Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          },
          "vendor": {
            "key": "43",
            "id": "1099 Int",
            "name": "1099 Int",
            "href": "/objects/accounts-payable/vendor/43"
          },
          "employee": {
            "key": "1",
            "id": "1",
            "name": "Reser",
            "href": "/objects/company-config/employee/1"
          },
          "item": {
            "key": "1",
            "id": "1",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/1"
          },
          "class": {
            "key": "1",
            "id": "3",
            "name": "Health Care",
            "href": "/objects/company-config/class/1"
          },
          "warehouse": {
            "key": null,
            "id": null,
            "name": null
          },
          "contract": {
            "key": null,
            "id": null,
            "name": null
          },
          "task": {
            "key": null,
            "id": null,
            "name": null
          }
        },
        "baseLocation": {
          "name": "Australia",
          "key": "4",
          "href": "/objects/company-config/location/4"
        },
        "memo": "bill - 001 - vendor 1099",
        "currency": {
          "exchangeRate": {
            "date": "2022-02-21",
            "typeId": "-99",
            "rate": 1.0679
          },
          "txnCurrency": "USD",
          "baseCurrency": "AUD"
        },
        "allocation": {
          "id": null,
          "key": null
        },
        "hasForm1099": "false",
        "lineNumber": "1",
        "paymentInformation": {
          "totalBaseAmountPaid": "0.00",
          "totalTxnAmountPaid": "0.00",
          "totalBaseAmountSelectedForPayment": "0.00",
          "totalTxnAmountSelectedForPayment": "0.00"
        },
        "project": {
          "isBillable": false,
          "isBilled": false
        },
        "releaseToPay": false,
        "form1099": {
          "type": null,
          "box": null
        },
        "retainage": {
          "percentage": "10",
          "txnAmountRetained": "100",
          "baseAmountRetained": "50",
          "hasRetainage": false,
          "txmAmountReleased": "50",
          "release": false
        },
        "isSubtotal": false,
        "purchasing": {
          "document": {
            "key": "23",
            "id": "23"
          },
          "documentLine": {
            "key": "23",
            "id": "23"
          }
        },
        "fixedAsset": {
          "nameOfAcquiredAsset": null,
          "includeTaxInAssetCost": false,
          "assetCreationMode": "createFixedAsset",
          "assetQuantity": 2
        },
        "href": "/objects/accounts-payable/bill-line/440"
      }
    ],
    "href": "/objects/accounts-payable/bill/60"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/bill/{key}
_Update a bill_

**Request example — Update a single value:**
```json
{
  "billNumber": "bill10"
}
```
**Response 200 — Reference to updated bill:**
```json
{
  "ia::result": {
    "key": "63",
    "id": "198376",
    "href": "/objects/accounts-payable/bill/63"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/accounts-payable/bill/{key}
_Delete a bill_


## GET /objects/accounts-payable/check-run
_List check runs_

**Response 200 — List check runs:**
```json
{
  "ia::result": [
    {
      "key": "4",
      "id": "All Checks For Mar 2025",
      "href": "/objects/accounts-payable/check-run/4"
    },
    {
      "key": "2",
      "id": "All Checks For Apr 2025",
      "href": "/objects/accounts-payable/check-run/2"
    },
    {
      "key": "3",
      "id": "All Checks For First week of March 2024",
      "href": "/objects/accounts-payable/check-run/3"
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

## POST /objects/accounts-payable/check-run
_Create a check run_

**Request example — Create a check run:**
```json
{
  "title": "All Checks For Mar 2025",
  "checkStock": "prePrintedCheckStock",
  "checkingAccount": {
    "id": "BDF"
  },
  "sortOrder": [
    "Entity",
    "Check",
    "Vendor",
    "Amount",
    "Date",
    "Bank"
  ],
  "checksPerPage": "3",
  "printCheckStubDetail": true,
  "printVendorStubDetail": true,
  "status": "active"
}
```
**Response 201 — Reference to new check run:**
```json
{
  "ia::result": {
    "id": "6",
    "key": "6",
    "title": "All Checks For Mar 2025",
    "href": "/objects/accounts-payable/check-run/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/check-run/{key}
_Get a check run_

**Response 200 — Get a check run:**
```json
{
  "ia::result": {
    "id": "6",
    "key": "6",
    "title": "First week Jan 2025",
    "checkStock": "prePrintedCheckStock",
    "checkingAccount": {
      "id": "BDF"
    },
    "sortOrder": [
      "Entity",
      "Check",
      "Vendor",
      "Amount",
      "Date",
      "Bank"
    ],
    "checksPerPage": "3",
    "printCheckStubDetail": true,
    "printVendorStubDetail": true,
    "status": "active",
    "whenCreated": "2024-12-21",
    "href": "/objects/accounts-payable/check-run/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/check-run/{key}
_Update a check run_

**Request example — Update a check run:**
```json
{
  "printCheckStubDetail": false,
  "printVendorStubDetail": false,
  "status": "active"
}
```
**Response 200 — Reference to updated check run:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "6",
    "title": "All Checks For Mar 2025",
    "href": "/objects/accounts-payable/check-run/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/check-run/{key}
_Delete a check run_


## GET /objects/accounts-payable/joint-payee
_List joint payees_

**Response 200 — List joint payees:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/accounts-payable/joint-payee/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/accounts-payable/joint-payee/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/accounts-payable/joint-payee/3"
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

## POST /objects/accounts-payable/joint-payee
_Create a joint payee_

**Request example — Create a joint payee:**
```json
{
  "name": "John Smith",
  "printAs": "Orchard Supply Hardware & John Smith",
  "bill": {
    "key": "1"
  }
}
```
**Response 201 — Reference to new joint payee:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "href": "/objects/accounts-payable/joint-payee/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/payment
_List payments_

**Response 200 — List payments:**
```json
{
  "ia::result": [
    {
      "key": "1718",
      "id": "1718",
      "href": "/objects/accounts-payable/payment/1718"
    },
    {
      "key": "1717",
      "id": "1717",
      "href": "/objects/accounts-payable/payment/1717"
    },
    {
      "key": "3228",
      "id": "3228",
      "href": "/objects/accounts-payable/payment/3228"
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

## POST /objects/accounts-payable/payment
_Create a payment_

**Request example — Create a payment:**
```json
{
  "financialEntity": {
    "entityId": "BOA"
  },
  "paymentDate": "2024-04-04",
  "description": "From billing through March",
  "documentNumber": "3086",
  "documentId": "Prim-Vendor-Invoice-VI#0008",
  "paymentRequestMethod": "generateOneRequestPerBill",
  "baseCurrency": {
    "currency": "USD"
  },
  "txnCurrency": {
    "currency": "USD"
  },
  "paymentMethod": "creditCard",
  "vendor": {
    "id": "201"
  },
  "details": [
    {
      "txnCurrency": {
        "paymentAmount": "10.00"
      },
      "bill": {
        "key": "1221"
      }
    }
  ]
}
```
**Response 201 — Reference to new payment:**
```json
{
  "ia::result": {
    "id": "3323",
    "key": "3323",
    "href": "/objects/accounts-payable/payment/3323"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/payment-detail
_List payment details_

**Response 200 — List payment details:**
```json
{
  "ia::result": [
    {
      "key": "367",
      "id": "367",
      "href": "/objects/accounts-payable/payment-detail/367"
    },
    {
      "key": "1043",
      "id": "1043",
      "href": "/objects/accounts-payable/payment-detail/1043"
    },
    {
      "key": "1203",
      "id": "1203",
      "href": "/objects/accounts-payable/payment-detail/1203"
    }
  ],
  "ia::meta": {
    "totalCount": 509,
    "start": 1,
    "pageSize": 100,
    "next": 101,
    "previous": null
  }
}
```

## GET /objects/accounts-payable/payment-detail/{key}
_Get payment details_

**Response 200 — Get a payment detail object:**
```json
{
  "ia::result": {
    "id": "1133",
    "key": "1133",
    "bill": {
      "id": "2570",
      "key": "2570",
      "href": "/objects/accounts-payable/bill/2570"
    },
    "billLine": {
      "id": "25392",
      "key": "25392",
      "href": "/objects/accounts-payable/bill-line/25392"
    },
    "apCreditAdjustment": {
      "id": null,
      "key": null
    },
    "apCreditAdjustmentLine": {
      "id": null,
      "key": null
    },
    "apPayment": {
      "id": "3346",
      "key": "3346",
      "href": "/objects/accounts-payable/payment/3346"
    },
    "apPaymentLine": {
      "id": "31060",
      "key": "31060",
      "href": "/objects/accounts-payable/payment-line/31060"
    },
    "paymentDate": "2024-04-12",
    "baseCurrency": {
      "paymentAmount": "100.00",
      "inlineAmount": null,
      "discountAmount": null,
      "adjustmentAmount": null,
      "postedAdvanceAmount": null
    },
    "txnCurrency": {
      "paymentAmount": "100.00",
      "inlineAmount": null,
      "discountAmount": null,
      "adjustmentAmount": null,
      "postedAdvanceAmount": null,
      "currency": "USD"
    },
    "inlineBill": {
      "id": null,
      "key": null
    },
    "inlineBillLine": {
      "id": null,
      "key": null
    },
    "discountDate": null,
    "apDebitAdjustment": {
      "id": null,
      "key": null
    },
    "apDebitAdjustmentLine": {
      "id": null,
      "key": null
    },
    "apAdvance": {
      "id": null,
      "key": null
    },
    "apAdvanceLine": {
      "id": null,
      "key": null
    },
    "apPostedAdvance": {
      "id": null,
      "key": null
    },
    "apPostedAdvanceLine": {
      "id": null,
      "key": null
    },
    "state": "confirmed",
    "moduleKey": "3.AP",
    "audit": {
      "createdDateTime": "2024-04-12T03:25:56Z",
      "modifiedDateTime": "2024-04-12T04:45:10Z",
      "createdByUser": {
        "key": "7",
        "id": "Aman",
        "href": "/objects/company-config/user/7"
      },
      "createdBy": "7",
      "modifiedByUser": {
        "key": "7",
        "id": "Aman",
        "href": "/objects/company-config/user/7"
      },
      "modifiedBy": "7"
    },
    "jointPayee": {
      "id": null,
      "key": null,
      "printAs": null
    },
    "href": "/objects/accounts-payable/payment-detail/1133"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/payment-line
_List payment lines_

**Response 200 — List payment lines:**
```json
{
  "ia::result": [
    {
      "key": "3936",
      "id": "3936",
      "href": "/objects/accounts-payable/payment-line/3936"
    },
    {
      "key": "3938",
      "id": "3938",
      "href": "/objects/accounts-payable/payment-line/3938"
    },
    {
      "key": "3940",
      "id": "3940",
      "href": "/objects/accounts-payable/payment-line/3940"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 0,
    "pageSize": 1,
    "next": 0,
    "previous": null
  }
}
```

## GET /objects/accounts-payable/payment-line/{key}
_Get a payment line_

**Response 200 — Get a payment line:**
```json
{
  "ia::result": {
    "id": "3936",
    "key": "3936",
    "apPayment": {
      "id": "267",
      "key": "267",
      "href": "/objects/accounts-payable/payment/267"
    },
    "glAccount": {
      "key": "109",
      "id": "2000",
      "name": "Accounts Payable",
      "href": "/objects/general-ledger/account/109"
    },
    "baseCurrency": {
      "amount": "100.00",
      "currency": "USD",
      "totalPaid": "0.00",
      "totalSelected": "100.00"
    },
    "txnCurrency": {
      "amount": "100",
      "currency": "USD",
      "totalPaid": "0.00",
      "totalSelected": "100.00"
    },
    "dimensions": {
      "department": {
        "id": "11",
        "name": "Accounting"
      },
      "location": {
        "id": "1",
        "name": "United States of America"
      },
      "customer": {
        "key": null,
        "id": null,
        "name": null
      },
      "vendor": {
        "key": "17",
        "id": "VEN-0019",
        "name": "EC",
        "href": "/objects/accounts-payable/vendor/17"
      },
      "employee": {
        "key": null,
        "id": null,
        "name": null
      },
      "item": {
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
    "description": "Invoice for development in March 2024",
    "exchangeRate": {
      "date": "2024-07-21",
      "typeId": null,
      "rate": "1"
    },
    "lineNumber": "1",
    "paymentLineRecord": "pp",
    "baseLocation": "1",
    "bank": {
      "amount": "10",
      "txnAmount": "10",
      "txnCurrency": "USD",
      "baseCurrency": "USD",
      "bankExchangeRate": {
        "date": "2025-01-23",
        "rate": 1.0789,
        "typeId": "-1"
      }
    },
    "audit": {
      "createdDateTime": "2024-07-21T10:00:13Z",
      "modifiedDateTime": "2024-07-21T11:00:13Z",
      "createdByUser": {
        "key": "7",
        "id": "Aman",
        "href": "/objects/company-config/user/7"
      },
      "modifiedByUser": {
        "key": "7",
        "id": "Aman",
        "href": "/objects/company-config/user/7"
      }
    },
    "taxDetail": {
      "id": null,
      "key": null
    },
    "isTax": false,
    "href": "/objects/accounts-payable/payment-line/3936"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/payment/{key}
_Get a payment_

**Response 200 — Get a payment:**
```json
{
  "ia::result": {
    "id": "3302",
    "key": "3302",
    "paymentSummary": {
      "id": "1843",
      "key": "1843",
      "name": "Payments: 2024/03/30 04:08:58:5637 Batch",
      "postingDate": "2024-03-21",
      "href": "/objects/accounts-payable/summary/1843"
    },
    "recordType": "apPayment",
    "financialEntity": {
      "entityId": "BOA",
      "currency": "USD",
      "txnAmount": "10.00",
      "baseAmount": "10.00",
      "baseCurrency": "USD"
    },
    "state": "submitted",
    "paymentMethod": "creditCard",
    "vendor": {
      "entity": "V201",
      "id": "201",
      "name": "PG & E",
      "key": "38",
      "href": "/objects/accounts-payable/payment/38"
    },
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "entity": {
      "id": "1",
      "key": "1",
      "name": "United States of America"
    },
    "documentNumber": "123",
    "description": "Payment for 2024-03-21",
    "documentId": "Paid For PrjUS_InvWParent_4",
    "txnDate": "2024-03-21",
    "txnPaidDate": "2024-03-21",
    "baseCurrency": {
      "currency": "USD",
      "totalAmount": "10.00",
      "totalSelected": "0.00",
      "totalPaid": "10.00",
      "totalDue": "0.00"
    },
    "txnCurrency": {
      "currency": "USD",
      "totalAmount": "10.00",
      "totalSelected": "0.00",
      "totalPaid": "10.00",
      "totalDue": "0.00"
    },
    "exchangeRate": {
      "date": null,
      "typeId": null,
      "rate": null
    },
    "payTo": {
      "id": "PG & E(V201)",
      "key": "6886",
      "href": "/objects/company-config/contact/6886"
    },
    "audit": {
      "createdDateTime": "2024-03-29T18:08:57Z",
      "modifiedDateTime": "2024-03-29T18:08:59Z",
      "createdByUser": {
        "key": "1",
        "href": "/objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "href": "/objects/company-config/user/1"
      }
    },
    "cleared": "uncleared",
    "clearedDate": null,
    "isInclusiveTax": false,
    "taxSolution": {
      "key": null,
      "id": null,
      "taxCalculationMethod": null
    },
    "paymentRequestMethod": "useVendorPreference",
    "paymentSubmitter": "Alex",
    "paymentFileType": "none",
    "bankFile": {
      "id": null,
      "key": null
    },
    "jointPayee": {
      "id": null,
      "key": null
    },
    "lines": [
      {
        "id": "30762",
        "key": "30762",
        "apPayment": {
          "id": "3302",
          "key": "3302",
          "href": "/objects/accounts-payable/payment/3302"
        },
        "glAccount": {
          "key": "376",
          "id": "2000.02",
          "name": "Accounts Payable2",
          "href": "/objects/general-ledger/account/376"
        },
        "baseCurrency": {
          "amount": "10.00",
          "currency": "USD",
          "totalPaid": "10.00",
          "totalSelected": "0.00"
        },
        "txnCurrency": {
          "amount": "10.00",
          "currency": "USD",
          "totalPaid": "10.00",
          "totalSelected": "0.00"
        },
        "dimensions": {
          "department": {
            "id": null,
            "name": null
          },
          "location": {
            "id": "1",
            "name": "United States"
          },
          "customer": {
            "key": null,
            "id": null,
            "name": null
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
          "item": {
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
        "description": "Create_MP_02",
        "exchangeRate": {
          "date": "2024-03-21",
          "typeId": null,
          "rate": "1"
        },
        "lineNumber": 1,
        "paymentLineRecord": "pp",
        "bankLocation": "1",
        "audit": {
          "createdDateTime": "2024-03-29T18:08:57Z",
          "modifiedDateTime": "2024-03-29T18:08:59Z",
          "createdByUser": {
            "key": "1",
            "href": "/objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "href": "/objects/company-config/user/1"
          }
        },
        "taxDetail": {
          "id": null,
          "key": null
        },
        "isTax": false,
        "href": "/objects/accounts-payable/payment-line/30762"
      }
    ],
    "details": [
      {
        "id": "1059",
        "key": "1059",
        "bill": {
          "id": "3289",
          "key": "3289",
          "href": "/objects/accounts-payable/bill/3289"
        },
        "billLine": {
          "id": "30724",
          "key": "30724",
          "href": "/objects/accounts-payable/bill-line/30724"
        },
        "apCreditAdjustment": {
          "id": null,
          "key": null
        },
        "apCreditAdjustmentLine": {
          "id": null,
          "key": null
        },
        "apPayment": {
          "id": "3302",
          "key": "3302",
          "href": "/objects/accounts-payable/payment/3302"
        },
        "apPaymentLine": {
          "id": "30762",
          "key": "30762",
          "href": "/objects/accounts-payable/payment-line/30762"
        },
        "paymentDate": "2024-03-21",
        "baseCurrency": {
          "paymentAmount": "10.00",
          "inlineAmount": null,
          "discountAmount": null,
          "adjustmentAmount": null,
          "postedAdvanceAmount": null
        },
        "txnCurrency": {
          "paymentAmount": "10.00",
          "inlineAmount": null,
          "discountAmount": null,
          "adjustmentAmount": null,
          "postedAdvanceAmount": null,
          "currency": "USD"
        },
        "inlineBill": {
          "id": null,
          "key": null
        },
        "inlineBillLine": {
          "id": null,
          "key": null
        },
        "apDiscount": {
          "id": null,
          "key": null
        },
        "apDiscountLine": {
          "id": null,
          "key": null
        },
        "discountDate": null,
        "apDebitAdjustment": {
          "id": null,
          "key": null
        },
        "apDebitAdjustmentLine": {
          "id": null,
          "key": null
        },
        "apAdvance": {
          "id": null,
          "key": null
        },
        "apAdvanceLine": {
          "id": null,
          "key": null
        },
        "apPostedAdvance": {
          "id": null,
          "key": null
        },
        "apPostedAdvanceLine": {
          "id": null,
          "key": null
        },
        "state": "confirmed",
        "moduleKey": "3.AP",
        "audit": {
          "createdDateTime": "2024-03-29T18:08:58Z",
          "modifiedDateTime": "2024-03-29T18:08:58Z",
          "createdByUser": {
            "key": "1",
            "href": "/objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "href": "/objects/company-config/user/1"
          }
        },
        "jointPayee": {
          "id": null,
          "key": null
        },
        "href": "/objects/accounts-payable/payment-detail/1059"
      }
    ],
    "href": "/objects/accounts-payable/payment/3302"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/payment/{key}
_Update a payment_

**Request example — Update a payment:**
```json
{
  "description": "Payment for DOC Number: 22345",
  "documentNumber": "22345",
  "documentId": "22345"
}
```
**Response 200 — Reference to updated payment:**
```json
{
  "ia::result": {
    "id": "3325",
    "key": "3325",
    "href": "/objects/accounts-payable/payment/3325"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/payment/{key}
_Delete a payment_


## GET /objects/accounts-payable/recurring-bill
_List recurring bills_

**Response 200 — List recurring bills:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Adjustment Increase",
      "href": "/objects/accounts-payable/recurring-bill/1"
    },
    {
      "key": "2",
      "id": "Adjustment Increase",
      "href": "/objects/accounts-payable/recurring-bill/2"
    },
    {
      "key": "3",
      "id": "Bill",
      "href": "/objects/accounts-payable/recurring-bill/3"
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

## POST /objects/accounts-payable/recurring-bill
_Create a recurring bill_

**Request example — Create a recurring bill:**
```json
{
  "description": "DNO Recurring Bill 001",
  "schedule": {
    "startDate": "2025-03-21",
    "repeatBy": "days",
    "repeatInterval": "1",
    "endDate": "2025-03-29",
    "emailNotifications": "joe.smith@mycompany.com"
  },
  "term": {
    "id": "N15"
  },
  "referenceNumber": "DNO Recur bill",
  "status": "active",
  "contract": {
    "id": "128",
    "description": "DNO contract"
  },
  "vendor": {
    "id": "1099 Int"
  },
  "currency": {
    "baseCurrency": "USD",
    "txnCurrency": "USD",
    "exchangeRate": {
      "date": "2024-02-21",
      "typeId": "Intacct Daily Rate",
      "rate": 1.0679
    }
  },
  "lines": [
    {
      "memo": "DNO Recurring Bill line 01",
      "glAccount": {
        "id": "6000"
      },
      "baseAmount": "120",
      "hasForm1099": "false",
      "currency": {
        "txnCurrency": "USD",
        "baseCurrency": "AUD"
      },
      "txnAmount": "150"
    },
    {
      "memo": "DNO Recurring Bill line 02",
      "glAccount": {
        "id": "6000"
      },
      "baseAmount": "110",
      "hasForm1099": "false",
      "currency": {
        "txnCurrency": "USD",
        "baseCurrency": "AUD"
      },
      "txnAmount": "130.00"
    }
  ]
}
```
**Response 201 — Reference to new recurring bill:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/accounts-payable/recurring-bill/5",
    "ia::meta": {
      "totalCount": 1
    }
  }
}
```

## GET /objects/accounts-payable/recurring-bill-line
_List recurring bill lines_

**Response 200 — List recurring bill lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/accounts-payable/recurring-bill-line/1"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/accounts-payable/recurring-bill-line/4"
    },
    {
      "key": "7",
      "id": "7",
      "href": "/objects/accounts-payable/recurring-bill-line/7"
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

## POST /objects/accounts-payable/recurring-bill-line
_Create a recurring bill line_

**Request example — Create a recurring bill line:**
```json
{
  "recurringBill": {
    "key": "1159"
  },
  "txnAmount": "2500",
  "glAccount": {
    "key": "254"
  },
  "dimensions": {
    "location": {
      "key": "1"
    },
    "vendor": {
      "id": "209"
    },
    "department": {
      "id": "77"
    },
    "project": {
      "key": "27"
    },
    "customer": {
      "id": "HC"
    }
  },
  "memo": "server charges bill",
  "overrideOffsetGLAccount": {
    "key": "252"
  },
  "hasForm1099": "true",
  "form1099": {
    "type": "NEC",
    "box": "7"
  },
  "accountLabel": {
    "key": "28"
  }
}
```
**Response 201 — Reference to new recurring bill line:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/accounts-payable/recurring-bill-line/5",
    "ia::meta": {
      "totalCount": 1
    }
  }
}
```

## GET /objects/accounts-payable/recurring-bill-line/{key}
_Get a recurring bill line_

**Response 200 — Get a recurring bill line:**
```json
{
  "ia::result": {
    "id": "15",
    "key": "15",
    "recurringBill": {
      "id": "32'",
      "key": "32",
      "href": "/objects/accounts-payable/recurring-bill/32"
    },
    "memo": "DNO Recurring Bill",
    "glAccount": {
      "key": "246",
      "id": "6000",
      "name": "G&A Salaries",
      "href": "/objects/general-ledger/account/246"
    },
    "baseAmount": "183.83",
    "dimensions": {
      "location": {
        "id": "1",
        "name": "United States of America"
      },
      "department": {
        "id": "11",
        "name": "Accounting"
      },
      "project": {
        "key": "8",
        "id": "8",
        "name": "Client Services - Power Aerospace Materials",
        "href": "/objects/projects/project/8"
      },
      "customer": {
        "key": "1",
        "id": "1",
        "name": "Power Aerospace Materials",
        "href": "/objects/accounts-receivable/customer/1"
      },
      "vendor": {
        "key": "43",
        "id": "1099 Int",
        "name": "1099 Int",
        "href": "/objects/accounts-payable/vendor/43"
      },
      "employee": {
        "key": "31",
        "id": "31",
        "name": "Reser",
        "href": "/objects/company-config/employee/31"
      },
      "item": {
        "key": "12",
        "id": "12",
        "name": "PC Computer",
        "href": "/objects/inventory-control/item/12"
      },
      "class": {
        "key": "13",
        "id": "33",
        "name": "Health Care",
        "href": "/objects/company-config/class/13"
      }
    },
    "lineNumber": 0,
    "hasForm1099": "false",
    "form1099": {
      "type": null,
      "box": null
    },
    "accountLabel": {
      "id": null
    },
    "currency": {
      "txnCurrency": "USD",
      "baseCurrency": "AUD"
    },
    "txnAmount": "120.00",
    "allocation": {
      "id": null,
      "key": null,
      "name": null
    },
    "isBillable": null,
    "audit": {
      "createdDateTime": "2024-03-20T11:16:41Z",
      "modifiedDateTime": "2024-03-21T10:57:23Z",
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
      }
    },
    "href": "/objects/accounts-payable/recurring-bill-line/15"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/recurring-bill-line/{key}
_Update a recurring bill line_

**Request example — Update a bill line:**
```json
{
  "txnAmount": "2400",
  "overrideOffsetGLAccount": {
    "key": "254"
  }
}
```
**Response 200 — Reference to updated recurring bill line:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/accounts-payable/recurring-bill-line/5",
    "ia::meta": {
      "totalCount": 1
    }
  }
}
```

## DELETE /objects/accounts-payable/recurring-bill-line/{key}
_Delete recurring bill lines_


## GET /objects/accounts-payable/recurring-bill-tax-entry
_List recurring bill tax entries_

**Response 200 — List recurring bill tax entries:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "8",
      "href": "/objects/accounts-payable/recurring-bill-tax-entry/8"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/accounts-payable/recurring-bill-tax-entry/9"
    },
    {
      "key": "10",
      "id": "10",
      "href": "/objects/accounts-payable/recurring-bill-tax-entry/10"
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

## GET /objects/accounts-payable/recurring-bill-tax-entry/{key}
_Get a recurring bill tax entry_

**Response 200 — Get a recurring bill tax entry:**
```json
{
  "ia::result": {
    "key": "300",
    "id": "300",
    "baseTaxAmount": "100",
    "txnTaxAmount": "100",
    "taxRate": 5.5,
    "purchasingTaxDetail": {
      "id": "UK Export Reduced Rate",
      "key": "24",
      "href": "/objects/tax/purchasing-tax-detail/24"
    },
    "recurringBillLine": {
      "id": "148",
      "key": "148",
      "href": "/objects/accounts-payable/recurring-bill-line/148"
    },
    "href": "/objects/accounts-payable/recurring-bill-tax-entry/300"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/recurring-bill/{key}
_Get a recurring bill_

**Response 200 — Get a recurring bill:**
```json
{
  "ia::result": {
    "key": "12",
    "description": "DNO Recurring Bill",
    "audit": {
      "createdDateTime": "2024-03-20T00:00:00Z",
      "modifiedDateTime": "2024-03-20T11:38:13Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "term": {
      "key": "8",
      "id": "N15",
      "href": "/objects/accounts-payable/term/8"
    },
    "id": "Invoice",
    "totalEntered": "337.02",
    "referenceNumber": "DNO Recurr bill",
    "moduleKey": "3.AP",
    "status": "active",
    "recurringSchedule": {
      "id": "1",
      "key": "1",
      "href": "/objects/core/schedule/1"
    },
    "contract": {
      "id": "128",
      "description": "DNO contract"
    },
    "vendor": {
      "id": "1099 Int",
      "name": "1099 Int",
      "key": "43",
      "href": "/objects/accounts-payable/vendor/43"
    },
    "currency": {
      "txnCurrency": "USD",
      "baseCurrency": "AUD"
    },
    "txnTotalEntered": "220.00",
    "lines": [
      {
        "id": "1",
        "key": "1",
        "recurringBill": {
          "id": "1",
          "key": "1",
          "href": "/objects/accounts-payable/recurring-bill/1"
        },
        "memo": "DNO Recurring Bill",
        "glAccount": {
          "key": "246",
          "id": "6000",
          "name": "G&A Salaries",
          "href": "/objects/general-ledger/account/246"
        },
        "baseAmount": "183.83",
        "dimensions": {
          "location": {
            "id": "1",
            "name": "United States of America"
          },
          "department": {
            "id": "11",
            "name": "Accounting"
          },
          "project": {
            "key": "8",
            "id": "8",
            "name": "Client Services - Power Aerospace Materials",
            "href": "/objects/projects/project/8"
          },
          "customer": {
            "key": "1",
            "id": "1",
            "name": "Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          },
          "vendor": {
            "key": "43",
            "id": "1099 Int",
            "name": "1099 Int",
            "href": "/objects/accounts-payable/vendor/43"
          },
          "employee": {
            "key": "1",
            "id": "1",
            "name": "Reser",
            "href": "/objects/company-config/employee/1"
          },
          "item": {
            "key": "1",
            "id": "1",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/1"
          },
          "class": {
            "key": "1",
            "id": "3",
            "name": "Health Care",
            "href": "/objects/company-config/class/1"
          }
        },
        "lineNumber": 0,
        "hasForm1099": "false",
        "accountLabel": {
          "id": null
        },
        "currency": {
          "txnCurrency": "USD",
          "baseCurrency": "AUD"
        },
        "txnAmount": "120.00",
        "audit": {
          "createdDateTime": "2024-03-20T11:38:13Z",
          "modifiedDateTime": "2024-03-20T11:38:13Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/accounts-payable/recurring-bill-line/1",
        "entity": {
          "key": "46",
          "id": "Western Region",
          "name": "Western Region",
          "href": "/objects/company-config/entity/46"
        }
      },
      {
        "id": "2",
        "key": "2",
        "recurringBill": {
          "id": "1",
          "key": "1",
          "href": "/objects/accounts-payable/recurring-bill/1"
        },
        "memo": "DNO Recurring Bill",
        "glAccount": {
          "key": "246",
          "id": "6000",
          "name": "G&A Salaries",
          "href": "/objects/general-ledger/account/246"
        },
        "baseAmount": "153.19",
        "dimensions": {
          "location": {
            "id": "1",
            "name": "United States of America"
          },
          "department": {
            "id": "11",
            "name": "Accounting"
          },
          "project": {
            "key": "8",
            "id": "8",
            "name": "Client Services - Power Aerospace Materials",
            "href": "/objects/projects/project/8"
          },
          "customer": {
            "key": "1",
            "id": "1",
            "name": "Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          },
          "vendor": {
            "key": "43",
            "id": "1099 Int",
            "name": "1099 Int",
            "href": "/objects/accounts-payable/vendor/43"
          },
          "employee": {
            "key": "1",
            "id": "1",
            "name": "Reser",
            "href": "/objects/company-config/employee/1"
          },
          "item": {
            "key": "1",
            "id": "1",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/1"
          },
          "class": {
            "key": "1",
            "id": "3",
            "name": "Heath Care",
            "href": "/objects/company-config/class/1"
          }
        },
        "lineNumber": 1,
        "hasForm1099": "false",
        "accountLabel": {
          "id": null
        },
        "currency": {
          "txnCurrency": "USD",
          "baseCurrency": "AUD"
        },
        "txnAmount": "100.00",
        "audit": {
          "createdDateTime": "2024-03-20T11:38:13Z",
          "modifiedDateTime": "2024-03-20T11:38:13Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/accounts-payable/recurring-bill-line/2",
        "entity": {
          "key": "46",
          "id": "Western Region",
          "name": "Western Region",
          "href": "/objects/company-config/entity/46"
        }
      }
    ],
    "href": "/objects/accounts-payable/recurring-bill/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/recurring-bill/{key}
_Update a recurring bill_

**Request example — Update a recurring bill:**
```json
{
  "description": "New payouts recurring bill"
}
```
**Response 200 — Reference to updated recurring bill:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/accounts-payable/recurring-bill/5",
    "ia::meta": {
      "totalCount": 1,
      "totalSuccess": 1,
      "totalError": 0
    }
  }
}
```

## DELETE /objects/accounts-payable/recurring-bill/{key}
_Delete a recurring bill_


## GET /objects/accounts-payable/summary
_List summaries_

**Response 200 — List summaries:**
```json
{
  "ia::result": [
    {
      "key": "36",
      "id": "36",
      "href": "/objects/accounts-payable/summary/36"
    },
    {
      "key": "43",
      "id": "43",
      "href": "/objects/accounts-payable/summary/43"
    },
    {
      "key": "55",
      "id": "55",
      "href": "/objects/accounts-payable/summary/55"
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

## POST /objects/accounts-payable/summary
_Create a summary_

**Request example — Create a new summary:**
```json
{
  "name": "Jan Summary 2024",
  "glPostingDate": "2024-02-01",
  "status": "active",
  "recordType": "apBill"
}
```
**Response 201 — Reference to new summary:**
```json
{
  "ia::result": {
    "key": "56",
    "id": "56",
    "href": "/objects/accounts-payable/summary/56"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/summary/{key}
_Get a summary_

**Response 200 — Get a summary:**
```json
{
  "ia::result": {
    "id": "36",
    "key": "36",
    "name": "Bills: Jan Summary 2024",
    "glPostingDate": "2024-02-01",
    "status": "active",
    "recordType": "apBill",
    "totalAmount": "4000.23",
    "state": "open",
    "parent": {
      "id": null,
      "key": null
    },
    "preventGLPosting": false,
    "summaryCreationType": "manual",
    "isQuickPaymentSummary": false,
    "audit": {
      "createdDateTime": "2024-02-01T10:42:15Z",
      "modifiedDateTime": "2025-02-02T04:24:13Z",
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
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "href": "/objects/accounts-payable/summary/36"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/summary/{key}
_Update a summary_

**Request example — Updates a summary:**
```json
{
  "name": "Sep To Oct 2024 Summary",
  "glPostingDate": "2024-11-01",
  "status": "active"
}
```
**Response 200 — Reference to updated summary:**
```json
{
  "ia::result": {
    "id": "50",
    "key": "50",
    "href": "/objects/accounts-payable/summary/50"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/summary/{key}
_Delete a summary_


## GET /objects/accounts-payable/term
_List terms_

**Response 200 — List terms:**
```json
{
  "ia::result": [
    {
      "key": "15",
      "id": "Net40",
      "href": "/objects/accounts-payable/term/15"
    },
    {
      "key": "17",
      "id": "N40_G",
      "href": "/objects/accounts-payable/term/17"
    },
    {
      "key": "9",
      "id": "N30",
      "href": "/objects/accounts-payable/term/9"
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

## POST /objects/accounts-payable/term
_Create a term_

**Request example — Create a term:**
```json
{
  "id": "N500",
  "description": "60 Days term",
  "status": "active",
  "due": {
    "days": 2,
    "from": "of5thMonthFromBillDate"
  },
  "discount": {
    "days": 1,
    "from": "of3rdMonthFromBillDate",
    "amount": 10,
    "unit": "amount",
    "graceDays": 15,
    "calculateOn": "billTotal"
  },
  "penalty": {
    "cycle": "quarterly",
    "amount": 101,
    "unit": "amount",
    "graceDays": 16
  }
}
```
**Response 201 — Create a term:**
```json
{
  "ia::result": {
    "key": "27",
    "id": "N500",
    "href": "/objects/accounts-payable/term/27"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/term/{key}
_Get a term_

**Response 200 — Get a term:**
```json
{
  "ia::result": {
    "id": "N500",
    "description": "60 Days term",
    "status": "active",
    "key": "27",
    "audit": {
      "modifiedDateTime": "2024-10-28T06:18:13Z",
      "createdDateTime": "2020-07-28T15:19:16Z",
      "modifiedByUser": {
        "key": "71",
        "id": "Aman",
        "href": "/objects/company-config/user/71"
      },
      "modifiedBy": "71",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1"
    },
    "due": {
      "days": 2,
      "from": "of5thMonthFromBillDate"
    },
    "discount": {
      "days": 1,
      "from": "of3rdMonthFromBillDate",
      "amount": 10,
      "unit": "percentage",
      "graceDays": 15,
      "calculateOn": "billTotal"
    },
    "penalty": {
      "cycle": "quarterly",
      "amount": 10.5,
      "unit": "percentage",
      "graceDays": 16
    },
    "href": "/objects/accounts-payable/term/27"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/term/{key}
_Update a term_

**Request example — Update a single value:**
```json
{
  "penalty": {
    "amount": 10.5
  }
}
```
**Response 200 — Update a term:**
```json
{
  "ia::result": {
    "key": "27",
    "id": "N500",
    "href": "/objects/accounts-payable/term/27"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/term/{key}
_Delete a term_


## GET /objects/accounts-payable/vendor
_List vendors_

**Response 200 — List vendors:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "Vend-00001",
      "href": "/objects/accounts-payable/vendor/84"
    },
    {
      "key": "85",
      "id": "Vend-00002",
      "href": "/objects/accounts-payable/vendor/85"
    },
    {
      "key": "60",
      "id": "Vend-00003",
      "href": "/objects/accounts-payable/vendor/60"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/accounts-payable/vendor
_Create a vendor_

**Request example — Create a vendor:**
```json
{
  "id": "Vend-00010",
  "name": "Design Works",
  "creditLimit": 40000,
  "isOnHold": false,
  "doNotPay": false,
  "billingType": "openItem",
  "paymentPriority": "normal",
  "billPayment": {
    "defaultDateOptions": "none"
  }
}
```
**Request example — Create an unrestricted vendor:**
```json
{
  "id": "Vendor_A0000003",
  "name": "Global Networks",
  "form1099": {
    "is1099Eligible": true,
    "nameOn1099": "ISC 1099",
    "type": "MISC",
    "box": "3"
  },
  "parent": {
    "id": "201"
  },
  "contacts": {
    "default": {
      "mailingAddress": {
        "addressLine1": "300 Park Avenue",
        "addressLine2": "Suite 1400",
        "addressLine3": "Western industrial area",
        "city": "San Jose",
        "country": "United States",
        "postCode": "95110",
        "state": "California"
      },
      "tax": {
        "isTaxable": true
      },
      "URL1": "https://mycompany.com",
      "URL2": "https://anothercompany.com",
      "companyName": "Ecology Corporation",
      "email1": "asmith@mycompany.com",
      "email2": "asmith@jmail.com",
      "fax": "14085555309",
      "firstName": "Alice",
      "lastName": "Smith",
      "middleName": "Mary",
      "mobile": "14085554420",
      "pager": "14085559987",
      "phone1": "14085551212",
      "printAs": "Smith.Alice",
      "hideContactList": false
    },
    "primary": {
      "id": "1099 IntCA"
    },
    "payTo": {
      "id": "1099 Int"
    },
    "returnTo": {
      "id": "111(V111)"
    },
    "recipient1099": {
      "id": "123515(V123515)"
    }
  },
  "term": {
    "id": "Net 60"
  },
  "vendorAccountNumber": "123456789",
  "taxId": "111-22-1111",
  "creditLimit": 1000,
  "billingType": "openItem",
  "vendorType": {
    "id": "Retailer"
  },
  "accountGroup": {
    "id": "Stationary VGL Group"
  },
  "priceSchedule": {
    "id": "PO Price S"
  },
  "discountPercent": 20,
  "priceList": {
    "id": "PO Price List"
  },
  "notes": "Comments of IN202",
  "defaultExpenseGLAccount": {
    "id": "6700.04"
  },
  "paymentPriority": "normal",
  "status": "active",
  "isOneTimeUse": true,
  "isOnHold": true,
  "doNotPay": true,
  "ach": {
    "enablePayments": true,
    "routingNumber": "123456789",
    "accountNumber": "987654321",
    "accountType": "checkingAccount",
    "remittanceType": "businessCTX"
  },
  "displayTermDiscountOnCheckStub": false,
  "displayVendorAccountOnCheckStub": false,
  "sendPaymentNotification": true,
  "preferredPaymentMethod": "printedCheck",
  "mergePaymentRequests": true,
  "overrideOffsetGLAccount": {
    "id": "1000.00"
  },
  "attachment": {
    "id": "Attach-12574"
  },
  "contactList": [
    {
      "name": "primary",
      "contact": {
        "id": "1099 IntCA"
      }
    },
    {
      "name": "pay to",
      "contact": {
        "id": "1099 Int"
      }
    },
    {
      "name": "return to",
      "contact": {
        "id": "111(V111)"
      }
    },
    {
      "name": "1099",
      "contact": {
        "id": "123515(V123515)"
      }
    }
  ],
  "vendorAccountNumberList": [
    {
      "locationId": "1--United States of America",
      "accountNo": "111111111"
    }
  ],
  "vendorEmailTemplates": [
    {
      "vendor": {
        "id": "Vendor_A0000003"
      },
      "txnDefinitionName": "Purchase Order",
      "emailTemplate": {
        "id": "5",
        "name": "AP"
      }
    }
  ],
  "billPayment": {
    "defaultDateOptions": "none"
  }
}
```
**Request example — Create a restricted vendor:**
```json
{
  "id": "Vend-00100",
  "name": "Regulatory Filing Group",
  "parent": {
    "id": "202"
  },
  "contacts": {
    "default": {
      "mailingAddress": {
        "addressLine1": "9500 Arboretum Blvd",
        "addressLine2": "Suite 310",
        "addressLine3": "Western industrial area",
        "city": "Austin",
        "country": "United States",
        "postCode": "78759",
        "state": "TX"
      },
      "tax": {
        "isTaxable": true
      },
      "URL1": "https:/rfginc.com",
      "companyName": "RFG Inc",
      "email1": "jjones@mycompany.com",
      "email2": "jjones@jmail.com",
      "fax": "14085555522",
      "firstName": "Jack",
      "lastName": "Jones",
      "middleName": "Inc",
      "mobile": "14085554420",
      "pager": "14085554400",
      "phone1": "14085551212",
      "printAs": "RFG Inc",
      "hideContactList": true
    }
  },
  "term": {
    "id": "Net 60"
  },
  "vendorAccountNumber": "203",
  "taxId": "192-35-4308",
  "creditLimit": 350000,
  "billingType": "balanceForward",
  "notes": "None",
  "defaultExpenseGLAccount": {
    "id": "1500"
  },
  "paymentPriority": "normal",
  "status": "active",
  "state": "a",
  "isOneTimeUse": false,
  "isOnHold": false,
  "doNotPay": false,
  "displayTermDiscountOnCheckStub": false,
  "displayVendorAccountOnCheckStub": false,
  "sendPaymentNotification": false,
  "mergePaymentRequests": true,
  "billPayment": {
    "defaultDateOptions": "none"
  }
}
```
**Request example — Create a vendor in a PO-match enabled company:**
```json
{
  "id": "VEND-0001",
  "name": "Office Supplies",
  "taxId": "12-3456788",
  "creditLimit": 50000,
  "isOnHold": false,
  "doNotPay": false,
  "alwaysCreateBill": true,
  "billingType": "openItem",
  "paymentPriority": "normal",
  "billPayment": {
    "defaultDateOptions": "none"
  }
}
```
**Response 201 — Reference to new vendor:**
```json
{
  "ia::result": {
    "key": "111",
    "href": "/objects/accounts-payable/vendor/111"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/vendor-account-number
_List vendor account numbers_

**Response 200 — List vendor account numbers:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/accounts-payable/vendor-account-number/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/accounts-payable/vendor-account-number/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/accounts-payable/vendor-account-number/3"
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

## POST /objects/accounts-payable/vendor-account-number
_Create a vendor account number_

**Request example — Create a vendor account number:**
```json
{
  "location": {
    "key": "2"
  },
  "vendor": {
    "key": "127"
  },
  "vendorAccountNumber": "1234567555"
}
```
**Response 201 — Reference to new vendor account number:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "7",
    "href": "/objects/accounts-payable/vendor-account-number/7"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/vendor-account-number/{key}
_Get a vendor account number_

**Response 200 — Get a vendor account number:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "7",
    "location": {
      "key": "11",
      "id": "11",
      "name": "United States of America",
      "href": "/objects/company-config/location/11"
    },
    "vendor": {
      "key": "33",
      "id": "33",
      "href": "/objects/accounts-payable/vendor/33"
    },
    "vendorAccountNumber": "VAN-5134986722",
    "href": "/objects/accounts-payable/vendor-account-number/7"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/accounts-payable/vendor-account-number/{key}
_Update a vendor account number_

**Request example — Update vendor account number:**
```json
{
  "vendorAccountNumber": "1234567888"
}
```
**Response 200 — Reference to updated vendor account number:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "href": "/objects/accounts-payable/vendor-account-number/2"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/accounts-payable/vendor-account-number/{key}
_Delete a vendor account number_


## GET /objects/accounts-payable/vendor-bank-file-setup
_List vendor bank file setup objects_

**Response 200 — List vendor bank file setup objects:**
```json
{
  "ia::result": [
    {
      "key": "25",
      "id": "25",
      "href": "/objects/accounts-payable/vendor-bank-file-setup/25"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/accounts-payable/vendor-bank-file-setup/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/accounts-payable/vendor-bank-file-setup/60"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/accounts-payable/vendor-bank-file-setup/{key}
_Get a vendor bank file setup object_

**Response 200 — Get a bank file setup object for South Africa (ZA):**
```json
{
  "ia::result": {
    "key": "25",
    "id": "25",
    "vendor": {
      "key": "202",
      "id": "SA1Vendor",
      "href": "/objects/accounts-payable/vendor/202"
    },
    "bsbNumber": null,
    "paymentReference": "EB32131016",
    "sortCode": null,
    "branchCode": "123433",
    "bankAccountType": "1",
    "bankAccountCode": "345678",
    "proofOfPayment": true,
    "bankAccountNumber": "87402896",
    "bankAccountName": "Jax Corp cheque",
    "businessIdCode": null,
    "href": "/objects/accounts-payable/vendor-bank-file-setup/25"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```
**Response 200 — Get a bank file setup object for Australia (AU):**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "vendor": {
      "key": "162",
      "id": "AU1Vendor",
      "href": "/objects/accounts-payable/vendor/162"
    },
    "bsbNumber": "163-821",
    "paymentReference": "EB32131016",
    "sortCode": null,
    "branchCode": null,
    "bankAccountType": null,
    "bankAccountCode": null,
    "proofOfPayment": null,
    "bankAccountNumber": "87402896",
    "bankAccountName": "Bea Corp transaction",
    "businessIdCode": null,
    "href": "/objects/accounts-payable/vendor-bank-file-setup/2"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```
**Response 200 — Get a bank file setup object for United Kingdom (GB):**
```json
{
  "ia::result": {
    "key": "26",
    "id": "26",
    "vendor": {
      "key": "203",
      "id": "UKVendor",
      "href": "/objects/accounts-payable/vendor/203"
    },
    "bsbNumber": null,
    "paymentReference": "EB32131016",
    "sortCode": "849571",
    "branchCode": null,
    "bankAccountType": null,
    "bankAccountCode": null,
    "proofOfPayment": null,
    "bankAccountNumber": "87402896",
    "bankAccountName": "State Corp current",
    "businessIdCode": null,
    "href": "/objects/accounts-payable/vendor-bank-file-setup/26"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```
**Response 200 — Get a bank file setup for United States (US):**
```json
{
  "ia::result": {
    "key": "78",
    "id": "78",
    "vendor": {
      "key": "389",
      "id": "USVendor",
      "href": "/objects/accounts-payable/vendor/389"
    },
    "bsbNumber": null,
    "paymentReference": "EB32131016",
    "sortCode": null,
    "branchCode": null,
    "bankAccountType": "32",
    "bankAccountCode": null,
    "proofOfPayment": null,
    "bankAccountNumber": "4534455667",
    "bankAccountName": "Lion Corp checking",
    "businessIdCode": "564534456",
    "accountClassification": "ppd",
    "href": "/objects/accounts-payable/vendor-bank-file-setup/78"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/vendor-contact
_List vendor contacts_

**Response 200 — List vendor contacts:**
```json
{
  "ia::result": [
    {
      "key": "17",
      "id": "17",
      "href": "/objects/accounts-payable/vendor-contact/17"
    },
    {
      "key": "18",
      "id": "18",
      "href": "/objects/accounts-payable/vendor-contact/18"
    },
    {
      "key": "19",
      "id": "19",
      "href": "/objects/accounts-payable/vendor-contact/19"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": 101,
    "previous": null
  }
}
```

## POST /objects/accounts-payable/vendor-contact
_Create a vendor contact_

**Request example — Create a vendor contact:**
```json
{
  "categoryName": "Branch Office",
  "vendor": {
    "key": "43"
  },
  "contact": {
    "key": "202",
    "id": "Jeffrey Post"
  }
}
```
**Response 201 — Reference to new vendor contact:**
```json
{
  "ia::result": {
    "id": "12",
    "key": "12",
    "href": "/objects/accounts-payable/vendor-contact/12"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/vendor-contact/{key}
_Get a vendor contact_

**Response 200 — Get a vendor contact:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "12",
    "categoryName": "Main Office",
    "contact": {
      "key": "197",
      "id": "Jeffrey Post",
      "href": "/objects/company-config/contact/197"
    },
    "audit": {
      "createdDateTime": "2024-04-20T16:20:00Z",
      "modifiedDateTime": "2024-04-20T16:20:00Z",
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
    "vendor": {
      "key": "15",
      "id": "VPACBELT",
      "href": "/objects/accounts-payable/vendor/15"
    },
    "href": "/objects/accounts-payable/vendor-contact/12"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/accounts-payable/vendor-contact/{key}
_Update a vendor contact_

**Request example — Update a vendor contact:**
```json
{
  "categoryName": "Home Office",
  "contact": {
    "id": "Emily Rose"
  }
}
```
**Response 200 — Reference to updated vendor contact:**
```json
{
  "ia::result": {
    "key": "18",
    "id": "18",
    "href": "/objects/accounts-payable/vendor-contact/18"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/accounts-payable/vendor-contact/{key}
_Delete a vendor contact_


## GET /objects/accounts-payable/vendor-email-template
_List vendor email templates_

**Response 200 — List vendor email templates:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "2",
      "href": "/objects/accounts-payable/vendor-email-template/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/accounts-payable/vendor-email-template/3"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/accounts-payable/vendor-email-template/4"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": 0,
    "previous": 0
  }
}
```

## POST /objects/accounts-payable/vendor-email-template
_Create a vendor email template_

**Request example — Create a vendor email template:**
```json
{
  "vendor": {
    "key": "127"
  },
  "txnDefinitionName": "Vendor Invoice",
  "emailTemplate": {
    "key": "1",
    "name": "Vendor Trial"
  }
}
```
**Response 201 — Reference to new vendor email template:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "V0504",
    "href": "/objects/accounts-payable/vendor-email-template/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/vendor-email-template/{key}
_Get a vendor email template_

**Response 200 — Get a vendor email template:**
```json
{
  "ia::result": {
    "id": "4",
    "key": "4",
    "vendor": {
      "key": "127",
      "id": "vendorId-1652196661",
      "href": "/objects/accounts-payable/vendor/127"
    },
    "txnDefinitionName": "Vendor Invoice",
    "emailTemplate": {
      "id": "6",
      "key": "6",
      "name": "Vendor Trial",
      "href": "/objects/company-config/email-template/6"
    },
    "href": "/objects/accounts-payable/vendor-email-template/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/vendor-email-template/{key}
_Update a vendor email template_

**Request example — Update a vendor email template:**
```json
{
  "txnDefinitionName": "PO Return",
  "emailTemplate": {
    "key": "2",
    "name": "Purchasing Trial"
  }
}
```
**Response 200 — Reference to updated vendor email template:**
```json
{
  "ia::result": {
    "key": "14",
    "id": "14",
    "href": "/objects/accounts-payable/vendor-email-template/14"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/accounts-payable/vendor-email-template/{key}
_Delete a vendor email template_


## GET /objects/accounts-payable/vendor-group
_List vendor groups_

**Response 200 — List vendor groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Top Level Vendors",
      "href": "/objects/accounts-payable/vendor-group/1"
    },
    {
      "key": "2",
      "id": "1st Level Vendors",
      "href": "/objects/accounts-payable/vendor-group/2"
    },
    {
      "key": "3",
      "id": "2nd Level Vendors",
      "href": "/objects/accounts-payable/vendor-group/3"
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

## POST /objects/accounts-payable/vendor-group
_Create a vendor group_

**Request example — Create a vendor group:**
```json
{
  "id": "1099 related vendors",
  "name": "1099 related vendor group",
  "description": "group of vendors who have 1099",
  "groupType": "allMembers",
  "isDimensionStructure": false,
  "memberFilter": {
    "object": "accounts-payable/vendor",
    "filterExpression": "and",
    "filters": [
      {
        "$contains": {
          "id": 1099
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
**Response 201 — Reference to new vendor group:**
```json
{
  "ia::result": {
    "key": "13",
    "id": "1099 related vendors",
    "href": "/objects/accounts-payable/accounts-payable-vendor-group/13"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/vendor-group/{key}
_Get a vendor group_

**Response 200 — Get a vendor group:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "2nd Level Vendors",
    "name": "Level 2 Vendors",
    "description": "Level 2 Vendors",
    "groupType": "specificMembers",
    "audit": {
      "createdDateTime": "2016-06-28T17:56:21Z",
      "modifiedDateTime": "2016-06-28T17:58:21Z",
      "createdByUser": {
        "key": "11",
        "id": "Anish",
        "href": "/objects/company-config/user/11"
      },
      "createdBy": "11",
      "modifiedByUser": {
        "key": "11",
        "id": "Anish",
        "href": "/objects/company-config/user/11"
      },
      "modifiedBy": "11"
    },
    "entity": {
      "id": "3",
      "key": "3",
      "href": "/objects/company-config/entity/3"
    },
    "groupMembers": [
      {
        "key": "12",
        "id": "AUT",
        "name": "Auto_Supplies Inc.",
        "status": "active",
        "sortOrder": "0",
        "href": "/objects/accounts-payable/vendor/12"
      },
      {
        "key": "13",
        "id": "CAL",
        "name": "CALOIL Corporation",
        "status": "active",
        "sortOrder": "1",
        "href": "/objects/accounts-payable/vendor/13"
      }
    ],
    "isDimensionStructure": false,
    "memberFilter": {
      "object": "accounts-payable/vendor",
      "filterExpression": "and",
      "orderBy": [
        {
          "name": "asc"
        }
      ]
    },
    "href": "/objects/accounts-payable/vendor-group/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/vendor-group/{key}
_Update a vendor group_

**Request example — Update a vendor group:**
```json
{
  "description": "Group of vendors who have enabled 1099"
}
```
**Response 200 — Reference to updated vendor group:**
```json
{
  "ia::result": {
    "key": "15",
    "id": "1099 related vendors",
    "href": "/objects/accounts-payable/vendor-group/15"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/vendor-group/{key}
_Delete a vendor group_


## GET /objects/accounts-payable/vendor-payment-provider
_List vendor payment providers_

**Response 200 — List vendor payment providers:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/accounts-payable/vendor-payment-provider/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/accounts-payable/vendor-payment-provider/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/accounts-payable/vendor-payment-provider/3"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": 0,
    "previous": 0
  }
}
```

## POST /objects/accounts-payable/vendor-payment-provider
_Create a vendor payment provider_

**Request example — Create a vendor payment provider:**
```json
{
  "paymentProvider": {
    "id": "CSI"
  },
  "vendor": {
    "id": "PV001"
  },
  "status": "active"
}
```
**Response 201 — Create a vendor payment provider:**
```json
{
  "ia::result": {
    "key": "111",
    "href": "/objects/accounts-payable/vendor-payment-provider/111"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/vendor-payment-provider/{key}
_Get a vendor payment provider_

**Response 200 — Get a vendor payment provider:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "paymentProvider": {
      "key": "3",
      "id": "CSI",
      "name": "CSI",
      "href": "/objects/cash-management/payment-provider/3"
    },
    "vendor": {
      "key": "111",
      "id": "VEND-00010",
      "name": "Design Works",
      "href": "/objects/accounts-payable/vendor/111"
    },
    "state": "subscribed",
    "message": "44299680-351-1628136894",
    "status": "active",
    "audit": {
      "createdDateTime": "2021-08-05T04:14:56Z",
      "modifiedDateTime": "2021-09-29T06:43:06Z",
      "createdBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "preferredPaymentMethod": {
      "key": "454",
      "id": "454",
      "name": "Check",
      "href": "/objects/cash-management/provider-payment-method/454"
    },
    "href": "/objects/accounts-payable/vendor-payment-provider/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/accounts-payable/vendor-payment-provider/{key}
_Update a vendor payment provider_

**Request example — Update a single value:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Update a single value:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/accounts-payable/vendor-payment-provider/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/accounts-payable/vendor-restricted-department
_List vendor restricted departments_

**Response 200 — List vendor restricted departments:**
```json
{
  "ia::result": [
    {
      "key": "76",
      "id": "76",
      "href": "/objects/accounts-payable/vendor-restricted-department/76"
    },
    {
      "key": "77",
      "id": "77",
      "href": "/objects/accounts-payable/vendor-restricted-department/77"
    },
    {
      "key": "78",
      "id": "78",
      "href": "/objects/accounts-payable/vendor-restricted-department/78"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/accounts-payable/vendor-restricted-department/{key}
_Get a vendor restricted department_

**Response 200 — Get a vendor restricted department:**
```json
{
  "ia::result": {
    "key": "77",
    "id": "77",
    "department": {
      "key": "24",
      "id": "DES",
      "href": "/objects/company-config/department/24"
    },
    "departmentGroup": {
      "key": null,
      "id": null
    },
    "vendor": {
      "key": "330",
      "id": "D10",
      "href": "/objects/accounts-payable/vendor/330"
    },
    "href": "/objects/accounts-payable/vendor-restricted-department/77"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/vendor-restricted-location
_List vendor restricted locations_

**Response 200 — List vendor restricted locations:**
```json
{
  "ia::result": [
    {
      "key": "200",
      "id": "200",
      "href": "/objects/accounts-payable/vendor-restricted-location/200"
    },
    {
      "key": "198",
      "id": "198",
      "href": "/objects/accounts-payable/vendor-restricted-location/198"
    },
    {
      "key": "196",
      "id": "196",
      "href": "/objects/accounts-payable/vendor-restricted-location/196"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/accounts-payable/vendor-restricted-location/{key}
_Get a vendor restricted location_

**Response 200 — Get a vendor restricted location:**
```json
{
  "ia::result": {
    "key": "142",
    "id": "142",
    "location": {
      "key": "3",
      "id": "3",
      "href": "/objects/company-config/location/3"
    },
    "locationGroup": {
      "key": null,
      "id": null
    },
    "vendor": {
      "key": "330",
      "id": "vendor-16521",
      "href": "/objects/accounts-payable/vendor/330"
    },
    "href": "/objects/accounts-payable/vendor-restricted-location/142"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/vendor-total
_List vendor totals_

**Response 200 — List vendor totals:**
```json
{
  "ia::result": [
    {
      "key": "85",
      "id": "111",
      "href": "/objects/accounts-payable/vendor-total/85"
    },
    {
      "key": "86",
      "id": "113",
      "href": "/objects/accounts-payable/vendor-total/86"
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

## GET /objects/accounts-payable/vendor-total/{key}
_Get a vendor total_

**Response 200 — Get a vendor total:**
```json
{
  "ia::result": {
    "key": "85",
    "vendor": {
      "id": "202",
      "name": "Pac Bell",
      "key": "48",
      "href": "/objects/accounts-payable/vendor/48"
    },
    "entity": {
      "id": "1",
      "name": "United States"
    },
    "totalDue": "1400.00",
    "id": "48",
    "href": "/objects/accounts-payable/vendor-total/85"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/vendor-type
_List vendor types_

**Response 200 — List vendor types:**
```json
{
  "ia::result": [
    {
      "key": "14",
      "id": "WholeSale",
      "href": "/objects/accounts-payable/vendor-type/14"
    },
    {
      "key": "2",
      "id": "Supplier",
      "href": "/objects/accounts-payable/vendor-type/2"
    },
    {
      "key": "4",
      "id": "VType-1099INT",
      "href": "/objects/accounts-payable/vendor-type/4"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100,
    "next": 0,
    "previous": 0
  }
}
```

## POST /objects/accounts-payable/vendor-type
_Create a vendor type_

**Request example — Create a vendor type:**
```json
{
  "id": "WholeSaleDistributor",
  "form1099": {
    "type": "DIV",
    "box": "1B"
  }
}
```
**Response 201 — Create a vendor type:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "WholeSaleDistributor",
    "href": "/objects/accounts-payable/vendor-type/23"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/accounts-payable/vendor-type/{key}
_Get a vendor type_

**Response 200 — Get a vendor type:**
```json
{
  "ia::result": {
    "id": "Wholesaler",
    "parent": {
      "id": "WholeSaleDistributor",
      "key": "23",
      "href": "/objects/accounts-payable/vendor-type/23"
    },
    "status": "active",
    "form1099": {
      "type": "DIV",
      "box": "1B"
    },
    "key": "5",
    "audit": {
      "createdDateTime": "2018-07-28T19:29:46Z",
      "modifiedDateTime": "2023-04-11T06:53:27Z",
      "createdByUser": {
        "key": "68",
        "id": "Aaron",
        "href": "/objects/company-config/user/68"
      },
      "createdBy": "68",
      "modifiedByUser": {
        "key": "68",
        "id": "Aaron",
        "href": "/objects/company-config/user/68"
      },
      "modifiedBy": "68"
    },
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "href": "/objects/accounts-payable/vendor-type/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/vendor-type/{key}
_Update a vendor type_

**Request example — Update a vendor type:**
```json
{
  "status": "inactive"
}
```
**Request example — Update a parent vendor type:**
```json
{
  "parent": {
    "id": "WholeSaleDistributor"
  },
  "status": "inactive"
}
```
**Response 200 — Update a vendor type:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "Wholesaler",
    "href": "/objects/accounts-payable/vendor-type/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/accounts-payable/vendor-type/{key}
_Delete a vendor type_


## GET /objects/accounts-payable/vendor/{key}
_Get a vendor_

**Response 200 — Get a vendor:**
```json
{
  "ia::result": {
    "key": "111",
    "id": "VEND-00010",
    "name": "Design Works",
    "status": "active",
    "state": "a",
    "taxId": "12-3456789",
    "form1099": {
      "nameOn1099": "Design Works Inc",
      "type": "MISC",
      "box": "3"
    },
    "creditLimit": 40000,
    "isOnHold": true,
    "doNotPay": true,
    "alwaysCreateBill": false,
    "currency": "USD",
    "contacts": {
      "primary": {
        "id": "Doe, John",
        "key": "271",
        "href": "/objects/company-config/contact/271"
      },
      "payTo": {
        "id": "Ho, Amy",
        "key": "298",
        "href": "/objects/company-config/contact/298"
      },
      "returnTo": {
        "id": "Doe, John",
        "key": "271",
        "href": "/objects/company-config/contact/271"
      },
      "recipient1099": {
        "id": "Ho, Amy",
        "key": "298",
        "href": "/objects/company-config/contact/298"
      }
    },
    "mergePaymentRequests": true,
    "sendPaymentNotification": true,
    "restriction": {
      "restrictionType": "unrestricted"
    },
    "billingType": "openItem",
    "paymentPriority": "normal",
    "displayTermDiscountOnCheckStub": true,
    "billPayment": {
      "defaultDateOptions": "none"
    },
    "displayVendorAccountOnCheckStub": true,
    "ach": {
      "enablePayments": false,
      "routingNumber": null,
      "accountNumber": null,
      "accountType": null,
      "remittanceType": null
    },
    "audit": {
      "modifiedDateTime": "2021-03-24T22:12:50Z",
      "createdDateTime": "2021-03-24T21:16:54Z",
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
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "entity": {
      "id": "1",
      "key": "1",
      "name": "United States of America"
    },
    "href": "/objects/accounts-payable/vendor/111"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```
**Response 200 — Get an unrestricted vendor:**
```json
{
  "ia::result": {
    "key": "69",
    "id": "Vendor_A0000001",
    "name": "Vendor_A0000001",
    "form1099": {
      "nameOn1099": "ISC 1099",
      "type": "MISC",
      "box": "3"
    },
    "parent": {
      "key": "47",
      "id": "201",
      "name": "PG & E",
      "href": "/objects/accounts-payable/vendor/47"
    },
    "contacts": {
      "default": {
        "mailingAddress": {
          "addressLine1": "300 Park Avenue",
          "addressLine2": "Suite 1400",
          "addressLine3": "Western industrial area",
          "city": "San Jose",
          "country": "United States",
          "postCode": "95110",
          "state": "California"
        },
        "tax": {
          "isTaxable": true
        },
        "URL1": "https://mycompany.com",
        "URL2": "https://anothercompany.com",
        "companyName": "Ecology Corp",
        "email1": "asmith@ecocorp.com",
        "email2": "asmith@jmail.com",
        "fax": "14085555309",
        "firstName": "Alice",
        "id": "Vendor_A0000001",
        "lastName": "Smith",
        "middleName": "Marie",
        "mobile": "14085554420",
        "pager": "14085559987",
        "phone1": "14085551212",
        "phone2": "14085559876",
        "prefix": "Ms.",
        "printAs": "Alice.Smith",
        "key": "237",
        "hideContactList": false,
        "href": "/objects/company-config/contact/237"
      },
      "primary": {
        "id": "1099 IntCA",
        "key": "206",
        "href": "/objects/company-config/contact/206"
      },
      "payTo": {
        "id": "1099 Int",
        "key": "211",
        "href": "/objects/company-config/contact/211"
      },
      "returnTo": {
        "id": "111(V111)",
        "key": "748",
        "href": "/objects/company-config/contact/748"
      },
      "recipient1099": {
        "id": "123515(V123515)",
        "key": "341",
        "href": "/objects/company-config/contact/341"
      }
    },
    "term": {
      "id": "Net 60",
      "key": "11",
      "href": "/objects/accounts-payable/term/11"
    },
    "vendorAccountNumber": "123456789",
    "taxId": "111-22-1111",
    "creditLimit": 1000,
    "totalDue": "0",
    "billingType": "openItem",
    "vendorType": {
      "id": "Retailer",
      "key": "14",
      "href": "/objects/accounts-payable/vendor-type/14"
    },
    "accountGroup": {
      "id": "Stationary VGL Group",
      "key": "14",
      "href": "/objects/purchasing/vendor-gl-group/14"
    },
    "priceSchedule": {
      "id": "PO Price S"
    },
    "discountPercent": 20,
    "priceList": {
      "id": "PO Price List",
      "key": "2",
      "href": "/objects/purchasing/price-list/2"
    },
    "notes": "Comments of IN202",
    "accountlabel": {
      "id": "Equipment",
      "key": "10"
    },
    "accountLabel": {
      "id": "Equipment",
      "key": "10"
    },
    "defaultExpenseGLAccount": {
      "id": "6700.04",
      "name": "CC Other Charges & Fees",
      "key": "326",
      "href": "/objects/general-ledger/account/326"
    },
    "paymentPriority": "normal",
    "status": "active",
    "state": "a",
    "isOneTimeUse": true,
    "isOnHold": true,
    "audit": {
      "modifiedDateTime": "2022-05-26T04:49:44Z",
      "createdDateTime": "2018-07-28T19:35:16Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "doNotPay": true,
    "alwaysCreateBill": false,
    "currency": "USD",
    "ach": {
      "enablePayments": true,
      "routingNumber": "123456789",
      "accountNumber": "987654321",
      "accountType": "checkingAccount",
      "remittanceType": "businessCTX"
    },
    "displayTermDiscountOnCheckStub": false,
    "displayVendorAccountOnCheckStub": false,
    "sendPaymentNotification": true,
    "preferredPaymentMethod": "printedCheck",
    "mergePaymentRequests": true,
    "overrideOffsetGLAccount": {
      "id": "1000.00",
      "key": "1000.00",
      "name": "10000",
      "href": "/objects/general-ledger/account/1000.00--10000"
    },
    "attachment": {
      "id": "Attach-12574",
      "key": "Attach-12574",
      "href": "/objects/company-config/attachment/Attach-12574"
    },
    "defaultLeadTime": 5,
    "retainagePercentage": 10,
    "isIndividualPerson": false,
    "lastBillCreatedDate": null,
    "lastPaymentMadeDate": null,
    "tpar": {
      "isTparEnabled": true,
      "name": "4IMPRINT INC"
    },
    "t5018": {
      "isT5018Enabled": true,
      "t5018Number": "123OOR652"
    },
    "contactList": [
      {
        "id": "215",
        "key": "215",
        "name": "primary",
        "contact": {
          "id": "1099 IntCA"
        },
        "audit": {
          "modifiedDateTime": "2022-05-26T04:49:44Z",
          "createdDateTime": "2022-05-26T04:49:44Z",
          "createdBy": "1",
          "modifiedBy": "1"
        }
      },
      {
        "id": "216",
        "key": "216",
        "name": "pay to",
        "contact": {
          "id": "1099 Int"
        },
        "audit": {
          "modifiedDateTime": "2022-05-26T04:49:44Z",
          "createdDateTime": "2022-05-26T04:49:44Z",
          "createdBy": "1",
          "modifiedBy": "1"
        }
      },
      {
        "id": "217",
        "key": "217",
        "name": "return to",
        "contact": {
          "id": "111(V111)"
        },
        "audit": {
          "modifiedDateTime": "2022-05-26T04:49:44Z",
          "createdDateTime": "2022-05-26T04:49:44Z",
          "createdBy": "1",
          "modifiedBy": "1"
        }
      },
      {
        "id": "218",
        "key": "218",
        "name": "1099",
        "contact": {
          "id": "123515(V123515)"
        },
        "audit": {
          "modifiedDateTime": "2022-05-26T04:49:44Z",
          "createdDateTime": "2022-05-26T04:49:44Z",
          "createdBy": "1",
          "modifiedBy": "1"
        }
      }
    ],
    "vendorAccountNumberList": [
      {
        "locationId": "1--United States of America",
        "accountNo": "111111111"
      }
    ],
    "vendorEmailTemplates": [
      {
        "id": "11",
        "key": "11",
        "vendor": {
          "key": "69",
          "id": "Vendor_A0000001",
          "href": "/objects/accounts-payable/vendor/69"
        },
        "txnDefinitionName": "Purchase Order",
        "emailTemplate": {
          "id": "5",
          "key": "5",
          "name": "AP",
          "href": "/objects/company-config/email-template/5"
        },
        "href": "/objects/accounts-payable/vendor-email-template/11"
      }
    ],
    "vendorPaymentProviders": [],
    "billPayment": {
      "defaultDateOptions": "none"
    },
    "href": "/objects/accounts-payable/vendor/69"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```
**Response 200 — Get a restricted vendor:**
```json
{
  "ia::result": {
    "key": "49",
    "id": "203",
    "name": "NCS, Inc.",
    "form1099": {
      "nameOn1099": null,
      "type": null,
      "box": null
    },
    "parent": {
      "key": "48",
      "id": "202",
      "name": "Pac Bell",
      "href": "/objects/accounts-payable/vendor/48"
    },
    "contacts": {
      "default": {
        "mailingAddress": {
          "addressLine1": "9500",
          "addressLine2": "Arboretum Blvd, Suite 310",
          "addressLine3": "Western industrial area",
          "city": "Austin",
          "country": "United States",
          "postCode": "78759",
          "state": "TX"
        },
        "tax": {
          "isTaxable": true
        },
        "URL1": "https://mycompany.com",
        "URL2": "https://anothercompany.com",
        "companyName": "NCS, Inc.",
        "email1": "jhenry@mycompany.com",
        "email2": "jhenry@jmail.com",
        "fax": "14085555522",
        "firstName": "Jack",
        "id": "NCS, Inc.",
        "lastName": "Henry",
        "middleName": "James",
        "mobile": "14085554420",
        "pager": "14085554400",
        "phone1": "14085551212",
        "phone2": "14085559876",
        "prefix": "Mr.",
        "printAs": "Jack Henry & Associates",
        "key": "217",
        "hideContactList": true,
        "href": "/objects/company-config/contact/217"
      },
      "primary": {
        "id": null,
        "key": null
      },
      "payTo": {
        "id": null,
        "key": null
      },
      "returnTo": {
        "id": null,
        "key": null
      },
      "recipient1099": {
        "id": null,
        "key": null
      }
    },
    "term": {
      "id": "Net 60",
      "key": "11",
      "href": "/objects/accounts-payable/term/11"
    },
    "vendorAccountNumber": "203",
    "taxId": "192-35-4308",
    "creditLimit": 350000,
    "totalDue": "0",
    "billingType": "balanceForward",
    "vendorType": {
      "id": "Wholesaler",
      "key": "12"
    },
    "accountGroup": {
      "id": "Midwest",
      "key": "5"
    },
    "priceSchedule": {
      "id": null
    },
    "discountPercent": null,
    "priceList": {
      "id": null,
      "key": null
    },
    "notes": "None",
    "accountlabel": {
      "id": null,
      "key": null
    },
    "accountLabel": {
      "id": null,
      "key": null
    },
    "defaultExpenseGLAccount": {
      "id": "1500",
      "name": "Equipment",
      "key": "93",
      "href": "/objects/general-ledger/account/93"
    },
    "paymentPriority": "normal",
    "status": "active",
    "state": "a",
    "isOneTimeUse": false,
    "isOnHold": false,
    "audit": {
      "modifiedDateTime": "2024-05-26T05:28:54Z",
      "createdDateTime": "2023-07-28T19:35:15Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "doNotPay": false,
    "alwaysCreateBill": false,
    "currency": "USD",
    "ach": {
      "enablePayments": false,
      "routingNumber": null,
      "accountNumber": null,
      "accountType": null,
      "remittanceType": null
    },
    "displayTermDiscountOnCheckStub": false,
    "displayVendorAccountOnCheckStub": false,
    "sendPaymentNotification": false,
    "preferredPaymentMethod": null,
    "mergePaymentRequests": true,
    "overrideOffsetGLAccount": {
      "id": null,
      "key": null,
      "name": null
    },
    "attachment": {
      "id": null,
      "key": null
    },
    "defaultLeadTime": null,
    "retainagePercentage": null,
    "lastBillCreatedDate": null,
    "lastPaymentMadeDate": null,
    "tpar": {
      "isTparEnabled": true,
      "name": "4IMPRINT INC"
    },
    "t5018": {
      "isT5018Enabled": true,
      "t5018Number": "123OOR652"
    },
    "contactList": [],
    "vendorAccountNumberList": [],
    "vendorEmailTemplates": [],
    "vendorPaymentProviders": [],
    "billPayment": {
      "defaultDateOptions": "none"
    },
    "href": "/objects/accounts-payable/vendor/49"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```
**Response 200 — Get a vendor enabled for United Kingdom (GB) bank files:**
```json
{
  "ia::result": {
    "key": "203",
    "id": "UKVendor",
    "name": "UKVendor",
    "form1099": {
      "nameOn1099": null,
      "type": null,
      "box": null
    },
    "parent": {
      "key": null,
      "id": null,
      "name": null
    },
    "contacts": {
      "default": {
        "mailingAddress": {
          "addressLine1": "300 Park Avenue",
          "addressLine2": "Suite 1400",
          "addressLine3": "Western industrial area",
          "city": "San Jose",
          "country": "United Kingdom",
          "postCode": "95110",
          "state": "California"
        },
        "tax": {
          "isTaxable": true
        },
        "URL1": "https://mycompany.com",
        "URL2": "https://anothercompany.com",
        "companyName": "AlcoSoft Inc",
        "email1": "asmith@company.com",
        "email2": "asmith@jmail.com",
        "fax": "14085555309",
        "firstName": "Alice",
        "id": "UKVendor(VUKVendor)",
        "lastName": "Smith",
        "middleName": "Marie",
        "mobile": "14085554420",
        "pager": "14085559987",
        "phone1": "14085551212",
        "phone2": "14085559876",
        "prefix": "Ms.",
        "printAs": "UKVendor",
        "key": "442",
        "hideContactList": false,
        "href": "/objects/company-config/contact/237"
      },
      "primary": {
        "id": null,
        "key": null
      },
      "payTo": {
        "id": null,
        "key": null
      },
      "returnTo": {
        "id": null,
        "key": null
      },
      "recipient1099": {
        "id": null,
        "key": null
      }
    },
    "term": {
      "id": null,
      "key": null
    },
    "vendorAccountNumber": null,
    "taxId": null,
    "creditLimit": 1000,
    "totalDue": "507.40",
    "billingType": "openItem",
    "vendorType": {
      "id": null,
      "key": null
    },
    "accountGroup": {
      "id": null,
      "key": null
    },
    "priceSchedule": {
      "id": null
    },
    "discountPercent": null,
    "priceList": {
      "id": null,
      "key": null
    },
    "notes": null,
    "accountlabel": {
      "id": null,
      "key": null
    },
    "accountLabel": {
      "id": null,
      "key": null
    },
    "defaultExpenseGLAccount": {
      "id": null,
      "name": null,
      "key": null
    },
    "paymentPriority": "normal",
    "status": "active",
    "state": "a",
    "isOneTimeUse": false,
    "isOnHold": false,
    "audit": {
      "modifiedDateTime": "2024-01-03T06:43:34Z",
      "createdDateTime": "2024-01-03T06:39:33Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "doNotPay": false,
    "alwaysCreateBill": false,
    "currency": "USD",
    "ach": {
      "enablePayments": false,
      "routingNumber": null,
      "accountNumber": null,
      "accountType": null,
      "remittanceType": null
    },
    "bankFiles": {
      "paymentCountryCode": "gb",
      "paymentCurrency": "GBP"
    },
    "displayTermDiscountOnCheckStub": false,
    "displayVendorAccountOnCheckStub": false,
    "sendPaymentNotification": false,
    "preferredPaymentMethod": null,
    "mergePaymentRequests": true,
    "overrideOffsetGLAccount": {
      "id": null,
      "key": null,
      "name": null
    },
    "attachment": {
      "id": null,
      "key": null
    },
    "defaultLeadTime": null,
    "retainagePercentage": null,
    "lastBillCreatedDate": null,
    "lastPaymentMadeDate": null,
    "tpar": {
      "isTparEnabled": true,
      "name": "4IMPRINT INC"
    },
    "t5018": {
      "isT5018Enabled": true,
      "t5018Number": "123OOR652"
    },
    "vendorBankFileSetup": [
      {
        "id": "26",
        "key": "26",
        "vendor": {
          "key": "203",
          "id": "UKVendor",
          "href": "/objects/accounts-payable/vendor/203"
        },
        "bsbNumber": "047-359",
        "paymentReference": "BACS HSBC corp",
        "sortCode": "849571",
        "branchCode": "213456",
        "bankAccountType": "4",
        "bankAccountCode": "345624",
        "proofOfPayment": true,
        "bankAccountNumber": "87402896",
        "bankAccountName": "UK Bank Corp.",
        "businessIdCode": "AIBKIE2D491",
        "href": "/objects/accounts-payable/vendor-bank-file-setup/26"
      }
    ],
    "vendorEmailTemplates": null,
    "vendorPaymentProviders": [],
    "billPayment": {
      "defaultDateOptions": "none"
    },
    "href": "/objects/accounts-payable/vendor/203"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```
**Response 200 — Get a vendor with French primary contact:**
```json
{
  "ia::result": {
    "key": "203",
    "id": "UKVendor",
    "name": "UKVendor",
    "form1099": {
      "nameOn1099": null,
      "type": null,
      "box": null
    },
    "parent": {
      "key": null,
      "id": null,
      "name": null
    },
    "contacts": {
      "default": {
        "electronicInvoiceDetails": {
          "legalCategory": "24 Fiduciary",
          "mainActivity": "10.3 Transformation and conservation of fruits and vegetables",
          "registeredCapital": "37 000",
          "typeOfCompany": "03 Intermediate sized enterprises",
          "valueAddedTaxRegime": "Monthly"
        },
        "mailingAddress": {
          "addressLine1": "300 Park Avenue",
          "addressLine2": "Suite 1400",
          "addressLine3": "Western industrial area",
          "city": "Paris",
          "country": "France",
          "postCode": "95110",
          "state": null
        },
        "tax": {
          "isTaxable": true
        },
        "URL1": "https://mycompany.com",
        "URL2": "https://anothercompany.com",
        "companyName": "AllPro Inc",
        "email1": "asmith@company.com",
        "email2": "asmith@jmail.com",
        "fax": "14085555309",
        "firstName": "Alice",
        "id": "1099 Int",
        "internationalTaxId": "123",
        "lastName": "Smith",
        "middleName": "Marie",
        "mobile": "14085554420",
        "pager": "14085559987",
        "phone1": "14085551212",
        "phone2": "14085559876",
        "prefix": "Ms.",
        "printAs": "1099 Int",
        "key": "211",
        "hideContactList": false,
        "href": "/objects/company-config/contact/211"
      },
      "primary": {
        "id": null,
        "key": null
      },
      "payTo": {
        "id": null,
        "key": null
      },
      "returnTo": {
        "id": null,
        "key": null
      },
      "recipient1099": {
        "id": null,
        "key": null
      }
    },
    "term": {
      "id": null,
      "key": null
    },
    "vendorAccountNumber": null,
    "taxId": null,
    "creditLimit": 1000,
    "totalDue": "507.40",
    "billingType": "openItem",
    "vendorType": {
      "id": null,
      "key": null
    },
    "accountGroup": {
      "id": null,
      "key": null
    },
    "priceSchedule": {
      "id": null
    },
    "discountPercent": null,
    "priceList": {
      "id": null,
      "key": null
    },
    "notes": null,
    "accountlabel": {
      "id": null,
      "key": null
    },
    "accountLabel": {
      "id": null,
      "key": null
    },
    "defaultExpenseGLAccount": {
      "id": null,
      "name": null,
      "key": null
    },
    "paymentPriority": "normal",
    "status": "active",
    "state": "a",
    "isOneTimeUse": false,
    "isOnHold": false,
    "audit": {
      "modifiedDateTime": "2024-01-03T06:43:34Z",
      "createdDateTime": "2024-01-03T06:39:33Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "doNotPay": false,
    "alwaysCreateBill": false,
    "currency": "USD",
    "ach": {
      "enablePayments": false,
      "routingNumber": null,
      "accountNumber": null,
      "accountType": null,
      "remittanceType": null
    },
    "bankFiles": {
      "paymentCountryCode": "gb",
      "paymentCurrency": "GBP"
    },
    "displayTermDiscountOnCheckStub": false,
    "displayVendorAccountOnCheckStub": false,
    "sendPaymentNotification": false,
    "preferredPaymentMethod": null,
    "restrictions": {
      "restrictionType": "unrestricted"
    },
    "mergePaymentRequests": true,
    "overrideOffsetGLAccount": {
      "id": null,
      "key": null,
      "name": null
    },
    "attachment": {
      "id": null,
      "key": null
    },
    "defaultLeadTime": null,
    "retainagePercentage": null,
    "lastBillCreatedDate": null,
    "lastPaymentMadeDate": null,
    "tpar": {
      "isTparEnabled": true,
      "name": "4IMPRINT INC"
    },
    "t5018": {
      "isT5018Enabled": true,
      "t5018Number": "123OOR652"
    },
    "vendorBankFileSetup": [],
    "vendorEmailTemplates": [],
    "vendorPaymentProviders": [],
    "billPayment": {
      "defaultDateOptions": "none"
    },
    "href": "/objects/accounts-payable/vendor/43"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/accounts-payable/vendor/{key}
_Update a vendor_

**Request example — Update a single value:**
```json
{
  "billingType": "balanceForward"
}
```
**Request example — Update multiple values:**
```json
{
  "defaultLeadTime": 5,
  "taxId": "192354308",
  "form1099": {
    "nameOn1099": "NCS",
    "type": "MISC",
    "box": "3"
  },
  "isOnHold": true,
  "doNotPay": true,
  "alwaysCreateBill": true,
  "creditLimit": 10000,
  "retainagePercentage": 20,
  "notes": "Make sure to include on 1099",
  "discountPercent": 20
}
```
**Response 200 — Reference to updated vendor:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "RituDate11-21-2015",
    "href": "/objects/accounts-payable/vendor/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/accounts-payable/vendor/{key}
_Delete a vendor_


## GET /objects/acounts-payable/joint-payee/{key}
_Get a joint payee_

**Response 200 — Get a joint payee:**
```json
{
  "ia::result": {
    "id": "3",
    "key": "3",
    "name": "John Smith",
    "printAs": "Orchard Supply Hardware & John Smith",
    "bill": {
      "key": "1",
      "id": "INV1258",
      "href": "/objects/accounts-payable/bill/1"
    },
    "href": "/objects/accounts-payable/joint-payee/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/acounts-payable/joint-payee/{key}
_Update a joint payee_

**Request example — Update a joint payee:**
```json
{
  "printAs": "Orchard Wholesale Co. & John Smith Jr."
}
```
**Response 200 — Reference to updated joint payee:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "href": "/objects/accounts-payable/joint-payee/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/acounts-payable/joint-payee/{key}
_Delete a joint payee_


## POST /workflows/accounts-payable/adjustment/reverse
_Reverse an adjustment_

**Request example — Request Example:**
```json
{
  "key": "22",
  "reverseDate": "2026-03-15",
  "memo": "Reversed the adjustment for duplicate entry"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "23",
    "href": "/objects/accounts-payable/adjustment/23",
    "state": "reversed"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/adjustment/submit
_Submit an adjustment_

**Request example — Request Example:**
```json
{
  "key": "11"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "11",
    "href": "/objects/accounts-payable/adjustment/11",
    "state": "posted"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/advance/reverse
_Reverse an AP advance_

**Request example — Request Example:**
```json
{
  "key": "22",
  "reversedDate": "2026-03-15",
  "memo": "Reversed the advance due to duplicate entry"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "23",
    "href": "/objects/accounts-payable/advance/23",
    "state": "reversed"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/advance/submit
_Submit an advance_

**Request example — Request Example:**
```json
{
  "key": "11"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "11",
    "href": "/objects/accounts-payable/advance/11",
    "state": "posted"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/bill-line/release
_Release a bill line_

**Request example — Request Example:**
```json
{
  "key": "132"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "releaseToPay": true,
    "href": "/objects/accounts-payable/bill-line/132"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/bill/approve
_Approve a bill_

**Request example — Request Example:**
```json
{
  "key": "132",
  "notes": "Approved, ready for use"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/bill/132",
    "state": "approved"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/bill/decline
_Decline a bill_

**Request example — Request Example:**
```json
{
  "key": "132",
  "notes": "Declined, missing information"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/bill/132",
    "state": "declined"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/bill/recall
_Recall a bill_

**Request example — Request Example:**
```json
{
  "key": "132"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/bill/132",
    "state": "draft"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/bill/reverse
_Reverse a bill_

**Request example — Request Example:**
```json
{
  "key": "132",
  "reverseDate": "2026-03-03",
  "notes": "Reversed for re-posting."
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/bill/132",
    "state": "reversed"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/bill/submit
_Submit a bill_

**Request example — Request Example:**
```json
{
  "key": "132"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/bill/132",
    "state": "posted"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/payment/approve
_Approve a payment_

**Request example — Request Example:**
```json
{
  "key": "132",
  "notes": "Approved, ready for use"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/payment/132",
    "state": "approved"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/payment/confirm
_Confirm a payment_

**Request example — Request Example:**
```json
{
  "key": "132"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/payment/132",
    "state": "confirmed"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/payment/decline
_Decline a payment_

**Request example — Request Example:**
```json
{
  "key": "132",
  "notes": "Declined, missing information"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/payment/132",
    "state": "declined"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/payment/print
_Print a payment_

**Request example — Request Example:**
```json
{
  "key": "132"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/payment/132",
    "state": "delivered"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/payment/reverse
_Reverse a payment or void a check_

**Request example — Request Example:**
```json
{
  "key": "132",
  "paymentDate": "2026-01-23",
  "description": "From billing through August 31"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/payment/132",
    "state": "reversed"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/payment/submit
_Submit a payment_

**Request example — Request Example:**
```json
{
  "key": "132"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "132",
    "id": "132",
    "href": "/objects/accounts-payable/payment/132",
    "state": "submitted"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/vendor/approve
_Approve a vendor_

**Request example — Request Example:**
```json
{
  "key": "518",
  "notes": "Approved, ready for use"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "518",
    "id": "V-00014",
    "href": "/objects/accounts-payable/vendor/518",
    "state": "approved"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /workflows/accounts-payable/vendor/decline
_Decline a vendor_

**Request example — Request Example:**
```json
{
  "key": "518",
  "notes": "Declined, missing information"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "518",
    "id": "V-00014",
    "href": "/objects/accounts-payable/vendor/518",
    "state": "declined"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```
