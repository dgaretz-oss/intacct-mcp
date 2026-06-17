# Cash Management

## GET /objects/cash-management/ar-advance-txn-line-template
_List AR advance transaction line templates_

**Response 200 — List AR advance transaction line templates:**
```json
{
  "ia::result": [
    {
      "key": "6",
      "id": "6",
      "href": "/objects/cash-management/ar-advance-txn-line-template/6"
    },
    {
      "key": "7",
      "id": "7",
      "href": "/objects/cash-management/ar-advance-txn-line-template/7"
    },
    {
      "key": "8",
      "id": "8",
      "href": "/objects/cash-management/ar-advance-txn-line-template/8"
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

## GET /objects/cash-management/ar-advance-txn-line-template/{key}
_Get an AR advance transaction line template_

**Response 200 — Get an AR advance transaction line template:**
```json
{
  "ia::result": {
    "id": "10",
    "key": "10",
    "arAdvanceTxnTemplate": {
      "key": "14",
      "id": "14",
      "href": "/objects/cash-management/ar-advance-txn-template/14"
    },
    "memo": "ar-advance-template05 description",
    "glAccount": {
      "key": "9",
      "id": "1000",
      "href": "/objects/general-ledger/account/9"
    },
    "dimensions": {
      "location": {
        "key": "2",
        "id": "LOC-002",
        "name": "India",
        "href": "/objects/company-config/location/2"
      },
      "department": {
        "key": "6",
        "id": "DEP-006",
        "name": "Sales and Marketing",
        "href": "/objects/company-config/department/6"
      },
      "project": {
        "key": "8",
        "id": "CLI-SVCS-008",
        "name": "Client Services - Power Aerospace Materials",
        "href": "/objects/projects/project/8"
      },
      "customer": {
        "key": "13",
        "id": "CUST-0013",
        "name": "Power Aerospace Materials",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "vendor": {
        "key": "38",
        "id": "1099 INTCA",
        "name": "1099 IntCA",
        "href": "/objects/accounts-payable/vendor/38"
      },
      "employee": {
        "key": "29",
        "id": "EMP-00234",
        "name": "Reyes",
        "href": "/objects/company-config/employee/29"
      },
      "item": {
        "key": "14",
        "id": "COMP-0014",
        "name": "PC Computer",
        "href": "/objects/inventory-control/item/14"
      },
      "class": {
        "key": "3",
        "id": "WSD",
        "name": "Whole Sales Distribution",
        "href": "/objects/company-config/class/1"
      }
    },
    "audit": {
      "createdDateTime": "2025-04-29T15:26:00Z",
      "modifiedDateTime": "2025-04-29T15:26:00Z",
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
    "href": "/objects/cash-management/ar-advance-txn-line-template/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/ar-advance-txn-template
_List AR advance transaction templates_

**Response 200 — List AR advance transaction templates:**
```json
{
  "ia::result": [
    {
      "key": "7",
      "id": "ar-advance-tmp-02",
      "href": "/objects/cash-management/ar-advance-txn-template/7"
    },
    {
      "key": "12",
      "id": "ar-advance-tmp-03",
      "href": "/objects/cash-management/ar-advance-txn-template/12"
    },
    {
      "key": "13",
      "id": "ar-advance-tmp-04",
      "href": "/objects/cash-management/ar-advance-txn-template/13"
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

## POST /objects/cash-management/ar-advance-txn-template
_Create an AR advance transaction template_

**Request example — Create an AR advance transaction template:**
```json
{
  "id": "AR-CUST-DEPOSIT-TMPL-03",
  "name": "AR Customer Deposit Template 03",
  "description": "AR Customer Deposit - Standard",
  "lines": [
    {
      "memo": "Standard AR transaction template for customer deposits.",
      "glAccount": {
        "key": "9"
      },
      "dimensions": {
        "location": {
          "id": "1"
        },
        "project": {
          "key": "8"
        },
        "customer": {
          "key": "1"
        },
        "vendor": {
          "key": "38"
        },
        "employee": {
          "key": "29"
        },
        "item": {
          "key": "1"
        },
        "class": {
          "key": "1"
        }
      }
    }
  ]
}
```
**Response 201 — Reference to the new AR advance transaction template:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "AR-CUST-DEPOSIT-TMPL-03",
    "href": "/objects/cash-management/ar-advance-txn-template/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/ar-advance-txn-template/{key}
_Get an AR advance transaction template_

**Response 200 — Get an AR advance transaction template:**
```json
{
  "ia::result": {
    "key": "13",
    "id": "AR-PROJ-BILL-04",
    "name": "AR Advance Project Billing Template - 04",
    "txnSource": "CSV Import",
    "description": "AR Project Billing",
    "status": "active",
    "audit": {
      "createdDateTime": "2025-04-29T15:26:00Z",
      "modifiedDateTime": "2025-04-29T15:26:00Z",
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
    "lines": [
      {
        "id": "9",
        "key": "9",
        "arAdvanceTxnTemplate": {
          "key": "13",
          "href": "/objects/cash-management/ar-advance-txn-template/13"
        },
        "memo": "Standard AR transaction template for project billing",
        "glAccount": {
          "key": "19",
          "id": "1010",
          "href": "/objects/general-ledger/account/19"
        },
        "dimensions": {
          "location": {
            "key": "2",
            "id": "LOC-002",
            "name": "India",
            "href": "/objects/company-config/location/2"
          },
          "department": {
            "key": "6",
            "id": "DEP-006",
            "name": "Sales and Marketing",
            "href": "/objects/company-config/department/6"
          },
          "project": {
            "key": "8",
            "id": "CLI-SVCS-008",
            "name": "Client Services - Power Aerospace Materials",
            "href": "/objects/projects/project/8"
          },
          "customer": {
            "key": "13",
            "id": "CUST-0013",
            "name": "Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "vendor": {
            "key": "38",
            "id": "1099 INTCA",
            "name": "1099 IntCA",
            "href": "/objects/accounts-payable/vendor/38"
          },
          "employee": {
            "key": "29",
            "id": "EMP-00234",
            "name": "Reyes",
            "href": "/objects/company-config/employee/29"
          },
          "item": {
            "key": "14",
            "id": "COMP-0014",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/14"
          },
          "class": {
            "key": "3",
            "id": "WSD",
            "name": "Whole Sales Distribution",
            "href": "/objects/company-config/class/1"
          }
        },
        "audit": {
          "createdDateTime": "2025-04-29T15:26:00Z",
          "modifiedDateTime": "2025-04-29T15:26:00Z",
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
        "href": "/objects/cash-management/ar-advance-line-template/9"
      }
    ],
    "href": "/objects/cash-management/ar-advance-txn-template/13"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/ar-advance-txn-template/{key}
_Update an AR advance transaction template_

**Request example — Update an AR advance transaction template:**
```json
{
  "key": "12",
  "name": "AR-CUST-DEPOSIT-HIGH-VOL-03",
  "description": "AR Customer Deposit - High Volume Clients 03",
  "lines": [
    {
      "key": "8",
      "glAccount": {
        "key": "9"
      },
      "memo": "AR transaction template for customer deposits - high volume clients",
      "dimensions": {
        "location": {
          "key": "2"
        },
        "department": {
          "key": "6"
        },
        "project": {
          "key": "8"
        },
        "customer": {
          "key": "1"
        },
        "vendor": {
          "key": "38"
        },
        "employee": {
          "key": "29"
        },
        "item": {
          "key": "1"
        },
        "class": {
          "key": "1"
        }
      }
    }
  ]
}
```
**Response 200 — Reference to updated AR advanced transaction template:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "AR-CUST-DEPOSIT-HIGH-VOL-03",
    "href": "/objects/cash-management/ar-advance-txn-template/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/ar-advance-txn-template/{key}
_Delete an AR advance transaction template_


## GET /objects/cash-management/bank-account
_List bank accounts_

**Response 200 — List bank accounts:**
```json
{
  "ia::result": [
    {
      "key": "29",
      "id": "CITI",
      "href": "/objects/cash-management/bank-account/29"
    },
    {
      "key": "30",
      "id": "BOA",
      "href": "/objects/cash-management/bank-account/30"
    }
  ],
  "ia::meta": {
    "totalCount": 2
  }
}
```

## GET /objects/cash-management/bank-account/{key}
_Get a bank account_

**Response 200 — Get a bank account:**
```json
{
  "ia::result": {
    "key": "29",
    "referenceKey": "90",
    "id": "CITI",
    "name": "CitiBank12",
    "currency": "USD",
    "accountType": "checking",
    "connectionStatus": "inProgress",
    "supportMultiAccountLinking": true,
    "financialInstitution": {
      "id": "8",
      "key": "8",
      "href": "/objects/cash-management/financial-institution/8"
    },
    "href": "/objects/cash-management/bank-account/29"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-fee
_List bank fees_

**Response 200 — List bank fees:**
```json
{
  "ia::result": [
    {
      "key": "1718",
      "id": "1718",
      "href": "/objects/cash-management/bank-fee/1718"
    },
    {
      "key": "1717",
      "id": "1717",
      "href": "/objects/cash-management/bank-fee/1717"
    },
    {
      "key": "3228",
      "id": "3228",
      "href": "/objects/cash-management/bank-fee/3228"
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

## POST /objects/cash-management/bank-fee
_Create a bank fee_

**Request example — Create a bank fee:**
```json
{
  "txnDate": "2024-01-20",
  "referenceNumber": "10920920",
  "documentNumber": "FEE0020",
  "description": "Check cashing fee for check 0020",
  "isInclusiveTax": true,
  "currency": {
    "txnCurrency": "CAD",
    "baseCurrency": "USD",
    "exchangeRate": {
      "date": "2021-01-20",
      "typeId": "Intacct Daily Rate",
      "rate": 0.7306
    }
  },
  "bankAccount": {
    "id": "BOA"
  },
  "taxSolution": {
    "key": "7",
    "id": "United Kingdom - VAT"
  },
  "attachment": {
    "id": "18"
  },
  "txnType": "serviceCharge",
  "lines": [
    {
      "totalTxnAmount": "100.00",
      "txnAmount": "100.00",
      "description": "Service charge",
      "glAccount": {
        "key": "318"
      },
      "dimensions": {
        "location": {
          "id": "USA"
        },
        "department": {
          "id": "OP-EE"
        }
      },
      "taxEntries": [
        {
          "purchasingTaxDetail": {
            "key": "105"
          }
        },
        {
          "purchasingTaxDetail": {
            "key": "101"
          }
        }
      ]
    }
  ]
}
```
**Response 201 — Reference to new bank fee:**
```json
{
  "ia::result": {
    "key": "500",
    "id": "500",
    "href": "/objects/cash-management/bank-fee/500"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-fee-line
_List bank fee lines_

**Response 200 — List bank fee lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/bank-fee-line/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/bank-fee-line/3"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/cash-management/bank-fee-line/5"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/cash-management/bank-fee-line/{key}
_Get a bank fee line_

**Response 200 — Get a bank fee line:**
```json
{
  "ia::result": {
    "id": "2801",
    "key": "2801",
    "bankFee": {
      "id": "516",
      "key": "516",
      "href": "/objects/cash-management/bank-fee/516"
    },
    "glAccount": {
      "key": "329",
      "id": "6700.07",
      "name": "Financial Fees - Bank Service Charges",
      "href": "/objects/general-ledger/account/329"
    },
    "apAccountLabel": {
      "key": "9",
      "id": "Bank Fees",
      "href": "/objects/accounts-payable/account-label/9"
    },
    "baseAmount": "100.00",
    "txnAmount": "100.00",
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
        "key": null,
        "id": null,
        "name": null
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
      "class": {
        "key": null,
        "id": null,
        "name": null
      }
    },
    "baseLocation": {
      "name": "United States of America",
      "key": "1",
      "href": "/objects/company-config/location/1"
    },
    "description": "Service charge",
    "currency": {
      "exchangeRate": {
        "date": "2024-01-20",
        "typeId": "Intacct Daily Rate",
        "rate": 1
      },
      "txnCurrency": "USD",
      "baseCurrency": "USD"
    },
    "status": "active",
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "href": "/objects/cash-management/bank-fee-line/2801"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-fee-tax-entry
_List bank fee tax entries_

**Response 200 — List bank fee tax entries:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "8",
      "href": "/objects/cash-management/bank-fee-tax-entry/8"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/cash-management/bank-fee-tax-entry/9"
    },
    {
      "key": "10",
      "id": "10",
      "href": "/objects/cash-management/bank-fee-tax-entry/10"
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

## GET /objects/cash-management/bank-fee-tax-entry/{key}
_Get a bank fee tax entry_

**Response 200 — Get a bank fee tax entry:**
```json
{
  "ia::result": {
    "key": "300",
    "id": "300",
    "baseTaxAmount": "100",
    "txnTaxAmount": "100",
    "description": "Standard Rate for UK Import Services",
    "taxRate": 5.5,
    "purchasingTaxDetail": {
      "id": "UK Export Reduced Rate",
      "key": "24",
      "href": "/objects/tax/purchasing-tax-detail/24"
    },
    "bankFeeLine": {
      "id": "148",
      "key": "148",
      "href": "/objects/cash-management/bank-fee-line/148"
    },
    "href": "/objects/cash-management/tax/bank-fee-tax-entry/300"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-fee/{key}
_Get a bank fee_

**Response 200 — Get a bank fee:**
```json
{
  "ia::result": {
    "id": "547",
    "key": "547",
    "bankAccount": {
      "id": "BOA",
      "currency": "USD"
    },
    "txnDate": "2024-01-20",
    "referenceNumber": "10920920",
    "documentNumber": "doc1289",
    "txnType": "serviceCharge",
    "description": "Check cashing fee for check 0020",
    "currency": {
      "baseCurrency": "USD",
      "txnCurrency": "CAD",
      "exchangeRate": {
        "date": "2024-01-20",
        "typeId": "Intacct Daily Rate",
        "rate": 0.7306
      }
    },
    "totalEntered": "73.06",
    "txnTotalEntered": "100.00",
    "state": "confirmed",
    "reconciliationState": "cleared",
    "clearingDate": "2024-01-23",
    "reversedBy": {
      "id": null,
      "key": null,
      "reversalDate": null
    },
    "reversalOf": {
      "id": null,
      "key": null,
      "txnDate": null
    },
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "isInclusiveTax": true,
    "taxSolution": {
      "key": "7",
      "id": "United Kingdom - VAT",
      "href": "/objects/tax/tax-solution/7"
    },
    "attachment": {
      "id": "111",
      "key": "2",
      "href": "/objects/company-config/attachment/2"
    },
    "lines": [
      {
        "id": "2901",
        "key": "2901",
        "bankFee": {
          "id": "547",
          "key": "547",
          "href": "/objects/cash-management/bank-fee/547"
        },
        "glAccount": {
          "key": "346",
          "id": "7509.03",
          "name": "Fee Account",
          "href": "/objects/general-ledger/account/346"
        },
        "apAccountLabel": {
          "key": "123",
          "id": "Accounting Fees",
          "href": "/objects/accounts-payable/ap-account-label/14"
        },
        "arAccountLabel": {
          "key": "456",
          "id": "SALES",
          "href": "/objects/accounts-receivable/account-label/456"
        },
        "baseAmount": "58.45",
        "txnAmount": "80.00",
        "dimensions": {
          "department": {
            "key": "21",
            "id": "OP-EE",
            "name": "Operations Engineering",
            "href": "/objects/company-config/department/21"
          },
          "location": {
            "key": "65",
            "id": "RICH-065",
            "name": "Richmond District",
            "href": "/objects/company-config/location/65"
          },
          "project": {
            "key": "35",
            "id": "QSF - BTI",
            "name": "Quick Start Financial - Berkeley Technology Inc",
            "href": "/objects/projects/project/35"
          },
          "customer": {
            "key": "14",
            "id": "BTI",
            "name": "Berkeley Technology Inc",
            "href": "/objects/accounts-receivable/customer/14"
          },
          "vendor": {
            "key": "56",
            "id": "210",
            "name": "Office Supply and Copier Co.",
            "href": "/objects/accounts-payable/vendor/56"
          },
          "employee": {
            "key": "27",
            "id": "12",
            "name": "John Smith",
            "href": "/objects/company-config/employee/27"
          },
          "item": {
            "key": "117",
            "id": "DELL",
            "name": "DELL Laptops",
            "href": "/objects/inventory-control/item/117"
          },
          "class": {
            "key": "3",
            "id": "WSD",
            "name": "Whole Sales Distribution",
            "href": "/objects/company-config/class/3"
          }
        },
        "baseLocation": {
          "name": "Richmond District",
          "key": "65",
          "href": "/objects/company-config/location/65"
        },
        "description": "Service charge",
        "currency": {
          "exchangeRate": {
            "date": "2024-04-25",
            "typeId": "Intacct Daily Rate",
            "rate": 0.7306
          },
          "txnCurrency": "CAD",
          "baseCurrency": "USD"
        },
        "status": "active",
        "audit": {
          "createdDateTime": "2025-04-11T12:56:46Z",
          "modifiedDateTime": "2025-04-11T12:56:46Z",
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
        "totalTxnAmount": "100.00",
        "taxEntries": [
          {
            "txnTaxAmount": "4.00",
            "baseTaxAmount": "2.92",
            "purchasingTaxDetail": {
              "id": "EC Purchase Services Reduced Rate Input",
              "key": "105",
              "href": "/objects/tax/purchasing-tax-detail/105"
            },
            "id": "118",
            "key": "118",
            "taxRate": 5,
            "bankFeeLine": {
              "id": "116",
              "key": "116",
              "href": "/objects/cash-management/bank-fee-line/116"
            },
            "href": "/objects/cash-management/bank-fee-tax-entry/118"
          },
          {
            "txnTaxAmount": "16.00",
            "baseTaxAmount": "11.69",
            "purchasingTaxDetail": {
              "id": "EC Purchase Goods Standard Rate Input",
              "key": "101",
              "href": "/objects/tax/purchasing-tax-detail/101"
            },
            "id": "120",
            "key": "120",
            "taxRate": 20,
            "bankFeeLine": {
              "id": "116",
              "key": "116",
              "href": "/objects/cash-management/bank-fee-line/116"
            },
            "href": "/objects/cash-management/bank-fee-tax-entry/120"
          }
        ],
        "href": "/objects/cash-management/bank-fee-line/2901"
      }
    ],
    "href": "/objects/cash-management/bank-fee/547"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/bank-fee/{key}
_Update a bank fee_

**Request example — Update a bank fee:**
```json
{
  "description": "Bank fee for the check cashing for check number 2002",
  "lines": [
    {
      "key": "88",
      "bankFee": {
        "key": "26"
      },
      "txnAmount": "80.00",
      "description": "Bank fee update check 2002",
      "status": "active",
      "totalTxnAmount": "100.00",
      "taxEntries": [
        {
          "purchasingTaxDetail": {
            "key": "101"
          }
        }
      ]
    }
  ]
}
```
**Response 200 — Reference to updated bank fee:**
```json
{
  "ia::result": {
    "id": "547",
    "key": "547",
    "href": "/objects/cash-management/bank-fee/547"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-feed
_List bank feeds_

**Response 200 — List bank feeds:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/bank-feed/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/cash-management/bank-feed/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/bank-feed/3"
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

## POST /objects/cash-management/bank-feed
_Create a bank feed_

**Request example — Create an XML bank feed:**
```json
{
  "financialAccount": {
    "id": "BOA"
  },
  "feedDate": "2021-06-21",
  "feedType": "xml",
  "transactions": [
    {
      "postingDate": "2021-06-20",
      "txnType": "withdrawal",
      "documentType": "Check",
      "documentNumber": "Bill 100",
      "payee": "Office Warehouse",
      "amount": "56000.34",
      "description": "payment Bill 100"
    },
    {
      "postingDate": "2021-06-22",
      "txnType": "deposit",
      "documentType": "Check",
      "documentNumber": "Bill 101",
      "payee": "Office Supplies Distribution",
      "amount": "126000.00",
      "description": "transaction Bill 101"
    }
  ]
}
```
**Response 201 — Reference to new bank feed:**
```json
{
  "ia::result": {
    "key": "119",
    "id": "119",
    "href": "/objects/cash-management/bank-feed/119"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-feed/{key}
_Get a bank feed_

**Response 200 — Get an XML bank feed:**
```json
{
  "ia::result": {
    "key": "88",
    "id": "88",
    "financialAccount": {
      "id": "BOA",
      "key": "38",
      "href": "/objects/cash-management/bank-account/38",
      "name": "Bank of America",
      "accountType": "bank"
    },
    "feedDate": "2021-10-06",
    "feedType": "xml",
    "feedState": "processed",
    "fileName": "bank-feed-import-1000-1100.csv",
    "errorId": "1",
    "errorMessage": "Error - not all transactions received.",
    "entity": {
      "id": 3,
      "key": 3,
      "href": "/objects/company-config/entity/3"
    },
    "importId": "0e26366f-cc60-4638-a1d3-d96a5282b313",
    "importedFileStatus": "initiated",
    "expectedTxnQuantity": 5,
    "downloadedTxnQuantity": 5,
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
    "transactions": [
      {
        "key": "2215",
        "id": "2215",
        "financialAccount": {
          "id": "BOA",
          "name": "Bank of America",
          "accountType": "bank",
          "currency": "USD",
          "key": "38",
          "href": "/objects/cash-management/bank-account/38"
        },
        "bankFeed": {
          "id": "88",
          "key": "88",
          "feedType": "xml",
          "fileName": "bank-feed-import-1000-1100.csv",
          "importId": "0e26366f-cc60-4638-a1d3-d96a5282b313",
          "feedDate": "2024-07-17",
          "href": "/objects/cash-management/bank-feed/88"
        },
        "txnId": null,
        "bankReconciliation": {
          "id": null,
          "key": null
        },
        "postingDate": "2021-09-20",
        "txnType": "deposit",
        "documentType": "Check",
        "documentNumber": "Bill100",
        "payee": "Office Warehouse",
        "amount": "56000.00",
        "description": "Created with Rest API XMl option",
        "reconciliationInformation": {
          "status": "unmatched",
          "amountToMatch": "56000.00",
          "matchingSequence": null
        },
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
        "customer": {
          "key": "14",
          "id": "BTI",
          "name": "Berkeley Technology Inc",
          "href": "/objects/accounts-receivable/customer/14"
        },
        "payeeAddress": {
          "street": "51 New Street",
          "city": "Newcastle",
          "state": "Tyne and Wear, UK",
          "postCode": "NE13 9AA"
        },
        "categoryData": {
          "category": "Interest",
          "subCategory": "Interest Earned",
          "categoryId": "1"
        },
        "extendedDescription": "Regular Deposit",
        "bankReferenceNumber": "17944",
        "href": "/objects/cash-management/bank-transaction/2215"
      },
      {
        "key": "2216",
        "id": "2216",
        "financialAccount": {
          "id": "BOA",
          "name": "Bank of America",
          "accountType": "bank",
          "currency": "USD",
          "key": "38",
          "href": "/objects/cash-management/bank-account/38"
        },
        "bankFeed": {
          "id": "88",
          "key": "88",
          "feedType": "xml",
          "fileName": "bank-feed-import-1000-1100.csv",
          "importId": "0e26366f-cc60-4638-a1d3-d96a5282b313",
          "feedDate": "2024-07-17",
          "href": "/objects/cash-management/bank-feed/88"
        },
        "txnId": null,
        "bankReconciliation": {
          "id": null,
          "key": null
        },
        "postingDate": "2021-09-22",
        "reconciliationDate": null,
        "txnType": "deposit",
        "documentType": "Check",
        "documentNumber": "Bill101",
        "payee": "Office Warehouse",
        "amount": "126000.00",
        "description": "Created with Rest API XMl option- rec2",
        "reconciliationInformation": {
          "status": "unmatched",
          "amountToMatch": "126000.00",
          "matchingSequence": null
        },
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
        "customer": {
          "key": null,
          "id": null,
          "name": null
        },
        "payeeAddress": {
          "street": null,
          "city": null,
          "state": null,
          "postCode": null
        },
        "categoryData": {
          "category": null,
          "subCategory": null,
          "categoryId": null
        },
        "extendedDescription": null,
        "bankReferenceNumber": null,
        "href": "/objects/cash-management/bank-transaction/2216"
      }
    ],
    "href": "/objects/cash-management/bank-feed/88"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```
**Response 200 — Get an online bank feed:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "11",
    "financialAccount": {
      "id": "BOA",
      "key": "38",
      "href": "/objects/cash-management/bank-account/38",
      "name": "Bank of America",
      "accountType": "bank"
    },
    "feedDate": "2020-10-28",
    "feedType": "online",
    "feedState": "inProgress",
    "fileName": "bank-feed-import-1000-1100.csv",
    "errorId": "1",
    "errorMessage": "Error - ending balance does not match the cash account balance.",
    "entity": {
      "id": 3,
      "key": 3,
      "href": "/objects/company-config/entity/3"
    },
    "importId": "0e26366f-cc60-4638-a1d3-d96a5282b313",
    "importedFileStatus": "completed",
    "expectedTxnQuantity": 5,
    "downloadedTxnQuantity": 5,
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
    "transactions": [
      {
        "key": "196",
        "id": "196",
        "financialAccount": {
          "id": "BOA",
          "name": "Bank of America",
          "accountType": "bank",
          "currency": "USD",
          "key": "38",
          "href": "/objects/cash-management/bank-account/38"
        },
        "bankFeed": {
          "id": "11",
          "key": "11",
          "feedType": "online",
          "fileName": "bank-feed-import-1000-1100.csv",
          "importId": "0e26366f-cc60-4638-a1d3-d96a5282b313",
          "feedDate": "2024-07-15",
          "href": "/objects/cash-management/bank-feed/11"
        },
        "txnId": "1",
        "bankReconciliation": {
          "id": null,
          "key": null
        },
        "postingDate": "2020-08-29",
        "reconciliationDate": null,
        "txnType": "deposit",
        "documentType": "CREDIT",
        "documentNumber": "Check 12345",
        "payee": "Office Warehouse",
        "amount": "110.00",
        "description": "Transaction Narrative",
        "reconciliationInformation": {
          "status": "partiallyMatched",
          "amountToMatch": "109.00",
          "matchingSequence": null
        },
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
        "customer": {
          "key": null,
          "id": null,
          "name": null
        },
        "payeeAddress": {
          "street": "51 New Street",
          "city": "Newcastle",
          "state": "Tyne and Wear, UK",
          "postCode": "NE13 9AA"
        },
        "categoryData": {
          "category": "Interest",
          "subCategory": "Interest Earned",
          "categoryId": null
        },
        "extendedDescription": "Regular deposit",
        "bankReferenceNumber": "17944",
        "href": "/objects/cash-management/bank-transaction/196"
      },
      {
        "key": "197",
        "id": "197",
        "financialAccount": {
          "id": "BOA",
          "name": "Bank of America",
          "accountType": "bank",
          "currency": "USD",
          "key": "38",
          "href": "/objects/cash-management/bank-account/38"
        },
        "bankFeed": {
          "id": "11",
          "key": "11",
          "feedType": "online",
          "fileName": "bank-feed-import-1000-1100.csv",
          "importId": "0e26366f-cc60-4638-a1d3-d96a5282b313",
          "feedDate": "2024-07-17",
          "href": "/objects/cash-management/bank-feed/11"
        },
        "txnId": "2",
        "bankReconciliation": {
          "id": null,
          "key": null
        },
        "postingDate": "2020-08-29",
        "reconciliationDate": null,
        "txnType": "withdrawal",
        "documentType": "DEBIT",
        "documentNumber": "234",
        "payee": "Office Warehouse",
        "amount": "75.00",
        "description": "Payment 9956",
        "reconciliationInformation": {
          "status": "matched",
          "amountToMatch": "0.00",
          "matchingSequence": null
        },
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
        "customer": {
          "key": null,
          "id": null,
          "name": null
        },
        "payeeAddress": {
          "street": null,
          "city": null,
          "state": null,
          "postCode": null
        },
        "categoryData": {
          "category": null,
          "subCategory": null,
          "categoryId": null
        },
        "extendedDescription": null,
        "bankReferenceNumber": null,
        "href": "/objects/cash-management/bank-transaction/197"
      },
      {
        "key": "214",
        "id": "214",
        "financialAccount": {
          "id": "BOA",
          "name": "Bank of America",
          "accountType": "bank",
          "currency": "USD",
          "key": "38",
          "href": "/objects/cash-management/bank-account/38"
        },
        "bankFeed": {
          "id": "11",
          "key": "11",
          "feedType": "online",
          "fileName": "bank-feed-import-1000-1100.csv",
          "importId": "0e26366f-cc60-4638-a1d3-d96a5282b313",
          "feedDate": "2024-07-15",
          "href": "/objects/cash-management/bank-feed/11"
        },
        "txnId": "19",
        "bankReconciliation": {
          "id": null,
          "key": null
        },
        "postingDate": "2020-09-06",
        "reconciliationDate": null,
        "txnType": "deposit",
        "documentType": "CHECK",
        "documentNumber": "56788",
        "payee": "Office Warehouse",
        "amount": "2103.09",
        "description": "Shares 56788",
        "reconciliationInformation": {
          "status": "matched",
          "amountToMatch": "0.00",
          "matchingSequence": null
        },
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
        "customer": {
          "key": null,
          "id": null,
          "name": null
        },
        "payeeAddress": {
          "street": null,
          "city": null,
          "state": null,
          "postCode": null
        },
        "categoryData": {
          "category": null,
          "subCategory": null,
          "categoryId": null
        },
        "extendedDescription": null,
        "bankReferenceNumber": null,
        "href": "/objects/cash-management/bank-transaction/214"
      }
    ],
    "href": "/objects/cash-management/bank-feed/11"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/cash-management/bank-feed/{key}
_Delete a bank feed_


## GET /objects/cash-management/bank-file
_List bank files_

**Response 200 — List bank files:**
```json
{
  "ia::result": [
    {
      "key": "29",
      "id": "29",
      "href": "/objects/cash-management/bank-file/29"
    },
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/bank-file/1"
    },
    {
      "key": "28",
      "id": "28",
      "href": "/objects/cash-management/bank-file/28"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/cash-management/bank-file/5"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "start": 1,
    "pageSize": 100,
    "next": 0,
    "previous": 0
  }
}
```

## GET /objects/cash-management/bank-file-detail
_List bank file details_

**Response 200 — List bank file detail objects:**
```json
{
  "ia::result": [
    {
      "key": "152",
      "id": "152",
      "href": "/objects/cash-management/bank-file-detail/152"
    },
    {
      "key": "147",
      "id": "147",
      "href": "/objects/cash-management/bank-file-detail/147"
    },
    {
      "key": "213",
      "id": "213",
      "href": "/objects/cash-management/bank-file-detail/213"
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

## GET /objects/cash-management/bank-file-detail/{key}
_Get a bank file detail object_

**Response 200 — Get bank file details:**
```json
{
  "ia::result": {
    "key": "792",
    "id": "792",
    "amount": "1200.00",
    "description": "Bank file payment for Invoice 02387429",
    "audit": {
      "createdDateTime": "2025-03-27T16:24:18Z",
      "modifiedDateTime": "2025-03-27T16:24:18Z",
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
    "paymentId": "1579",
    "payee": {
      "key": "2107",
      "id": "TECHSOL",
      "name": "Tech Solutions",
      "href": "/objects/accounts-payable/vendor/2107"
    },
    "bankFile": {
      "key": "13",
      "id": "13",
      "href": "/objects/cash-management/bank-file/13"
    },
    "bankFileErrors": [
      "{Field Name : payments.debtorAgent.identification, Error : must contain 6 numbers and no spaces.}",
      "{Field Name : payments.creditorAgent.identification, Error : must contain 6 numbers.}"
    ],
    "href": "/objects/cash-management/bank-file-detail/792"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-file/{key}
_Get a bank file_

**Response 200 — Get a bank file:**
```json
{
  "ia::result": {
    "id": "13",
    "key": "13",
    "bankAccount": {
      "id": "88",
      "key": "88",
      "name": "HSBC UK",
      "href": "/objects/cash-management/checking-account/88"
    },
    "fileName": "UKAccount-Dec-08-2025 08:50:07686",
    "fileExtension": "csv",
    "totalPayments": 1,
    "totalAmount": "1200",
    "currency": "GBP",
    "audit": {
      "createdDateTime": "2025-03-27T16:24:18Z",
      "modifiedDateTime": "2025-03-27T16:24:18Z",
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
    "state": "failed",
    "bankFileDetails": [
      {
        "key": "792",
        "id": "792",
        "bankFile": {
          "id": "13",
          "key": "13",
          "href": "/objects/cash-management/bank-file/13"
        },
        "amount": "1200.00",
        "description": "Undeposited fund from GPay invoice",
        "audit": {
          "createdDateTime": "2025-03-27T16:24:18Z",
          "modifiedDateTime": "2025-03-27T16:24:18Z",
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
        "paymentId": "1579",
        "payee": {
          "key": "2107",
          "id": "TECHSOL",
          "name": "Technical Solutions",
          "href": "/objects/accounts-payable/vendor/2107"
        },
        "bankFileErrors": [
          "{Field Name : payments.debtorAgent.identification, Error : must contain 6 numbers and no spaces.}",
          "{Field Name : payments.creditorAgent.identification, Error : must contain 6 numbers.}"
        ],
        "href": "/objects/cash-management/bank-file-detail/792"
      }
    ],
    "href": "/objects/cash-management/bank-file/13"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/bank-file/{key}
_Delete a Bank file_


## GET /objects/cash-management/bank-reconciliation
_List bank reconciliations_

**Response 200 — List bank reconciliations:**
```json
{
  "ia::result": [
    {
      "key": "16",
      "id": "16",
      "href": "/objects/cash-management/bank-reconciliation/16"
    },
    {
      "key": "17",
      "id": "17",
      "href": "/objects/cash-management/bank-reconciliation/17"
    },
    {
      "key": "18",
      "id": "18",
      "href": "/objects/cash-management/bank-reconciliation/18"
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

## POST /objects/cash-management/bank-reconciliation
_Create a bank reconciliation_

**Request example — Create an automatchWithReview reconciliation:**
```json
{
  "bankAccount": {
    "id": "CDB"
  },
  "reconciliationDate": "2025-03-21",
  "cutoffDate": "2025-03-21",
  "endingBalance": "50000.35",
  "reconciliationMode": "automatchWithReview",
  "feedType": "xml"
}
```
**Request example — Create a manual reconciliation:**
```json
{
  "bankAccount": {
    "id": "SBME"
  },
  "reconciliationDate": "2025-03-31",
  "cutoffDate": "2025-03-21",
  "endingBalance": "12346.55",
  "reconciliationMode": "manual"
}
```
**Response 201 — Reference to a new bank reconciliation:**
```json
{
  "ia::result": {
    "key": "57",
    "id": "57",
    "href": "/objects/cash-management/bank-reconciliation/57"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-reconciliation-record
_List reconciliation source records_

**Response 200 — List bank reconciliation records:**
```json
{
  "ia::result": [
    {
      "key": "306",
      "id": "306",
      "href": "/objects/cash-management/bank-reconciliation-record/306"
    },
    {
      "key": "307",
      "id": "307",
      "href": "/objects/cash-management/bank-reconciliation-record/307"
    },
    {
      "key": "308",
      "id": "308",
      "href": "/objects/cash-management/bank-reconciliation-record/308"
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

## GET /objects/cash-management/bank-reconciliation-record/{key}
_Get a bank reconciliation source record_

**Response 200 — Get a bank reconciliation record:**
```json
{
  "ia::result": {
    "key": "2214",
    "id": "2214",
    "bankReconciliation": {
      "key": "16",
      "id": "16",
      "href": "/objects/cash-management/bank-reconciliation/16"
    },
    "bankAccount": {
      "id": "BOA",
      "key": "38",
      "href": "/objects/cash-management/bank-account/38"
    },
    "txnInformation": {
      "recordType": "apPayment",
      "subledgerRecord": {
        "key": "1981",
        "id": "1981",
        "href": "/objects/accounts-payable/subledger-record/1981"
      },
      "journalEntryLine": {
        "key": "10",
        "id": "10"
      },
      "intialOpenItem": {
        "key": "234",
        "id": "234"
      },
      "txnType": "withdrawal",
      "documentNumber": "CHK100",
      "documentDate": "2025-05-26",
      "txnAmount": "482.88",
      "baseAmount": "482.88",
      "txnCurrency": "USD",
      "baseCurrency": "USD",
      "postingDate": "2025-05-26",
      "reconciliationInformation": {
        "lastReconcileDate": "2025-04-26",
        "state": "unmatched"
      },
      "payee": "Business Software Inc.",
      "description": "Refund for overpayment of subscription fees.",
      "postingState": "confirmed"
    },
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "href": "/objects/cash-management/bank-reconciliation-record/2214"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-reconciliation/{key}
_Get a bank reconciliation_

**Response 200 — Get a bank reconciliation:**
```json
{
  "ia::result": {
    "key": "52",
    "id": "52",
    "bankAccount": {
      "id": "SBME",
      "key": "132",
      "href": "/objects/cash-management/bank-account/132"
    },
    "reconciliationDate": "2025-01-31",
    "cutoffDate": "2025-01-21",
    "endingBalance": "12346.55",
    "reconciliationMode": "manual",
    "reconciliationStatus": "reconciled",
    "feedType": "online",
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "isReopened": false,
    "attachment": {
      "key": "19",
      "id": "Bank_Statement_003",
      "href": "/objects/company-config/attachment/19"
    },
    "reconciliationSourceRecords": [
      {
        "key": "2250",
        "id": "2250",
        "bankReconciliation": {
          "key": "52",
          "id": "52",
          "href": "/objects/cash-management/bank-reconciliation/52"
        },
        "bankAccount": {
          "id": "SBME",
          "key": "132",
          "href": "/objects/cash-management/bank-account/132"
        },
        "txnInformation": {
          "recordType": "otherReceipts",
          "subledgerRecord": {
            "key": "2226",
            "id": "2226",
            "href": "/objects/accounts-payable/subledger-record/2226"
          },
          "journalEntryLine": {
            "key": "10",
            "id": "10"
          },
          "intialOpenItem": {
            "key": "234",
            "id": "234"
          },
          "txnType": "deposit",
          "documentNumber": "CHK100",
          "documentDate": "2025-01-01",
          "txnAmount": "11.00",
          "baseAmount": "11.00",
          "txnCurrency": "USD",
          "baseCurrency": "USD",
          "postingDate": "2025-01-01",
          "reconciliationInformation": {
            "lastReconcileDate": "2025-01-31",
            "state": "cleared"
          },
          "payee": "Business Software Inc.",
          "description": "Refund for overpayment of subscription fees.",
          "postingState": "approved"
        },
        "audit": {
          "createdDateTime": "2025-04-11T12:56:46Z",
          "modifiedDateTime": "2025-04-11T12:56:46Z",
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
        "href": "/objects/cash-management/bank-reconciliation-record/2250"
      }
    ],
    "href": "/objects/cash-management/bank-reconciliation/52"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```
**Response 200 — Get a reopened reconciliation:**
```json
{
  "ia::result": {
    "key": "40",
    "id": "40",
    "bankAccount": {
      "id": "CITI",
      "key": "132",
      "href": "/objects/cash-management/bank-account/132"
    },
    "reconciliationDate": "2025-01-31",
    "cutoffDate": "2025-01-01",
    "endingBalance": "-2930.00",
    "reconciliationMode": "automatchWithReview",
    "reconciliationStatus": "reconciled",
    "feedType": "online",
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "isReopened": true,
    "reconciliationSourceRecords": [],
    "href": "/objects/cash-management/bank-reconciliation/40"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-transaction
_List bank transactions_

**Response 200 — List bank transactions:**
```json
{
  "ia::result": [
    {
      "key": "57",
      "id": "57",
      "href": "/objects/cash-management/bank-transaction/57"
    },
    {
      "key": "58",
      "id": "58",
      "href": "/objects/cash-management/bank-transaction/58"
    },
    {
      "key": "59",
      "id": "59",
      "href": "/objects/cash-management/bank-transaction/59"
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

## GET /objects/cash-management/bank-transaction/{key}
_Get a bank transaction_

**Response 200 — Get a bank transaction:**
```json
{
  "ia::result": {
    "key": "281",
    "id": "281",
    "financialAccount": {
      "id": "BOA",
      "name": "Bank of America",
      "type": "bank",
      "currency": "USD",
      "key": "38",
      "href": "/objects/cash-management/bank-account/38"
    },
    "bankFeed": {
      "id": "11",
      "key": "11",
      "createdBy": 1,
      "feedType": "online",
      "fileName": "bank-file-import-3.csv",
      "importId": "0e26366f-cc60-4638-a1d3-d96a5282b313",
      "feedDate": "2025-07-15",
      "href": "/objects/cash-management/bank-feed/11"
    },
    "txnId": "86",
    "bankReconciliation": {
      "id": "200",
      "key": "200",
      "href": "/objects/cash-management/bank-reconciliation/200"
    },
    "creditReconciliation": {
      "id": "null,",
      "key": null
    },
    "postingDate": "2025-01-30",
    "reconciliationDate": null,
    "txnType": "withdrawal",
    "documentType": "DEBIT",
    "documentNumber": null,
    "payee": null,
    "payeeAccountId": null,
    "amount": "100.00",
    "description": null,
    "shortDescription1": null,
    "shortDescription2": null,
    "reconciliationInformation": {
      "status": "matched",
      "amountToMatch": "0.00",
      "matchingSequence": "aq|aao|xyz"
    },
    "audit": {
      "createdDateTime": "2025-02-01T00:00:00Z",
      "modifiedDateTime": "2025-02-01T00:00:00Z",
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
    "customer": {
      "key": "14",
      "id": "TLC_IND_00121",
      "name": "TalComp Industries Inc"
    },
    "payeeAddress": {
      "street": "51 New Street",
      "city": "Newcastle",
      "state": "Tyne and Wear",
      "postCode": "NE13 9AA"
    },
    "categoryData": {
      "category": "Interest",
      "subCategory": "Interest Earned",
      "categoryId": null
    },
    "extendedDescription": "Monthly deposit for training venue for TalComp training project.",
    "bankReferenceNumber": "17944",
    "href": "/objects/cash-management/bank-transaction/281"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-txn-assignment-rule
_List bank transaction assignment rules_

**Response 200 — List bank transaction assignment rules:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/bank-txn-assignment-rule/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/cash-management/bank-txn-assignment-rule/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/bank-txn-assignment-rule/3"
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

## POST /objects/cash-management/bank-txn-assignment-rule
_Create a bank transaction assignment rule_

**Request example — Create a bank transaction assignment rule:**
```json
{
  "customer": {
    "key": "15"
  },
  "bankAccount": {
    "key": "157",
    "id": "Chase - 340293",
    "href": "/objects/cash-management/bank-account/157"
  },
  "ruleId": "ASSIGN_CUST_DEP_001",
  "name": "Assign Customer to Unmatched Deposit Transactions",
  "description": "Links unmatched bank deposit transactions to a customer based on keywords in the transaction description.",
  "filterAttributes": [
    {
      "bankTxnAttribute": "txnType",
      "operator": "equals",
      "value": "debit",
      "filterOrder": 1
    },
    {
      "bankTxnAttribute": "description",
      "operator": "contains",
      "value": "Blue Wave Digital",
      "filterOrder": 2
    }
  ]
}
```
**Response 201 — Reference to bank transaction assignment rule:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "href": "/objects/cash-management/bank-txn-assignment-rule/3"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-txn-assignment-rule-filter
_List bank transaction assignment rule filters_

**Response 200 — List bank transaction assignment rule filters:**
```json
{
  "ia::result": [
    {
      "key": "10",
      "id": "10",
      "href": "/objects/cash-management/bank-assignment-txn-rule-filter/10"
    },
    {
      "key": "11",
      "id": "11",
      "href": "/objects/cash-management/bank-txn-assignment-rule-filter/11"
    },
    {
      "key": "12",
      "id": "12",
      "href": "/objects/cash-management/bank-txn-assignment-rule-filter/12"
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

## GET /objects/cash-management/bank-txn-assignment-rule-filter/{key}
_Get a bank transaction assignment rule filter_

**Response 200 — Get a bank transaction assignment rule filter:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "10",
    "bankTxnAssignmentRule": {
      "id": "3",
      "key": "3",
      "href": "/objects/cash-management/bank-txn-assignment-rule/3"
    },
    "bankTxnAttribute": "txnType",
    "operator": "equals",
    "value": "debit",
    "filterOrder": 1,
    "href": "/objects/cash-management/bank-txn-assignment-rule-filter/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-txn-assignment-rule/{key}
_Get a bank transaction assignment rule_

**Response 200 — Get a bank transaction assignment rule:**
```json
{
  "ia::result": {
    "id": "3",
    "key": "3",
    "ruleId": "ASSIGN_CUST_DEP_001",
    "name": "Assign Customer to Unmatched Deposit Transactions",
    "description": "Links unmatched bank deposit transactions to a customer based on keywords in the transaction description.",
    "assignmentType": "customer",
    "status": "active",
    "customer": {
      "key": "15",
      "id": "BTI",
      "href": "/objects/accounts-receivable/customer/15"
    },
    "accountType": "bank",
    "bankAccount": {
      "key": "157",
      "id": "Chase - 340293",
      "href": "/objects/cash-management/bank-account/157"
    },
    "audit": {
      "createdDateTime": "2024-05-21T04:46:41Z",
      "modifiedDateTime": "2024-05-21T04:46:41Z",
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
    "filterAttributes": [
      {
        "id": "10",
        "key": "10",
        "bankTxnAssignmentRule": {
          "id": "3",
          "key": "3",
          "href": "/objects/cash-management/bank-txn-assignment-rule/3"
        },
        "bankTxnAttribute": "txnType",
        "operator": "equals",
        "value": "credit",
        "filterOrder": 1,
        "href": "/objects/cash-management/bank-txn-assignment-rule-filter/10"
      },
      {
        "id": "11",
        "key": "11",
        "bankTxnAssignmentRule": {
          "id": "3",
          "key": "3",
          "href": "/objects/cash-management/bank-txn-assignment-rule/3"
        },
        "bankTxnAttribute": "description",
        "operator": "contains",
        "value": "Blue Wave Digital",
        "filterOrder": 2,
        "href": "/objects/cash-management/bank-txn-assignment-rule-filter/11"
      }
    ],
    "href": "/objects/cash-management/bank-txn-assignment-rule/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/bank-txn-assignment-rule/{key}
_Update a bank transaction assignment rule_

**Request example — Update a bank transaction assignment rule:**
```json
{
  "ruleId": "ASSIGN_CUST_DEP_001",
  "name": "Assign Customer to Unmatched Deposit Transactions",
  "description": "Links unmatched bank deposit transactions to a customer based on keywords in the transaction description.",
  "filterAttributes": [
    {
      "key": "10",
      "filterOrder": 2
    },
    {
      "key": "11",
      "bankTxnAttribute": "description",
      "operator": "contains",
      "value": "1000",
      "filterOrder": 1
    }
  ]
}
```
**Response 200 — Reference to bank transaction assignment rule:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "href": "/objects/cash-management/bank-txn-assignment-rule/3"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/cash-management/bank-txn-assignment-rule/{key}
_Delete a bank transaction assignment rule_


## GET /objects/cash-management/bank-txn-rule
_List bank transaction rules_

**Response 200 — List bank transaction rules:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/bank-txn-rule/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/bank-txn-rule/3"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/cash-management/bank-txn-rule/4"
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

## POST /objects/cash-management/bank-txn-rule
_Create a bank transaction rule_

**Request example — Create a bank transaction rule to add Journal Entry:**
```json
{
  "ruleId": "GL-JE-157",
  "description": "Rule to create journal entry.",
  "name": "Create Journal Entry rule",
  "ruleType": "create",
  "createRuleObject": {
    "objectType": "journalEntry",
    "journalEntryTemplate": {
      "id": "3"
    }
  },
  "filterAttributes": [
    {
      "dataSource": "bankTransaction",
      "bankTxnAttribute": "postingDate",
      "operator": "greaterThan",
      "value": "01/03/2025",
      "order": 1
    },
    {
      "dataSource": "bankTransaction",
      "bankTxnAttribute": "transactionType",
      "operator": "equals",
      "value": "debit",
      "order": 2
    }
  ]
}
```
**Request example — Create a match bank transaction rule:**
```json
{
  "ruleId": "BOA-DOC-AMT-MATCH-003",
  "description": "Match rule for BOA accounts by document number.",
  "name": "BOA match by amount and doc no.",
  "ruleType": "match",
  "matchRuleAttributes": [
    {
      "intacctTxnAttribute": "amount",
      "bankTxnAttribute": "amount",
      "operator": "equals",
      "order": 2
    },
    {
      "intacctTxnAttribute": "documentNumber",
      "bankTxnAttribute": "documentNumber",
      "operator": "equals",
      "order": 1
    }
  ],
  "filterAttributes": [
    {
      "dataSource": "intacctTransaction",
      "intacctTxnAttribute": "documentNumber",
      "operator": "equals",
      "value": "DOC-1002",
      "order": 1
    }
  ]
}
```
**Request example — Create a bank transaction rule to add CC txn:**
```json
{
  "ruleId": "CC-TXN-234",
  "name": "Create CC txn from bank txn",
  "description": "Rule to create credit card transaction from bank transaction.",
  "ruleType": "create",
  "location": {
    "id": "1"
  },
  "createRuleObject": {
    "objectType": "cctransaction",
    "creditCardTxnTemplate": {
      "id": "3"
    }
  },
  "filterAttributes": [
    {
      "dataSource": "bankTransaction",
      "bankTxnAttribute": "postingDate",
      "operator": "greaterThan",
      "value": "07/03/2025",
      "order": 1
    }
  ]
}
```
**Response 201 — Reference to new bank transaction rule:**
```json
{
  "ia::result": {
    "key": "15",
    "id": "15",
    "href": "/objects/cash-management/bank-txn-rule/15"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-txn-rule-filter
_List bank transaction rule filters_

**Response 200 — List bank transaction rule filters:**
```json
{
  "ia::result": [
    {
      "key": "25",
      "id": "25",
      "href": "/objects/cash-management/bank-txn-rule-filter/25"
    },
    {
      "key": "57",
      "id": "57",
      "href": "/objects/cash-management/bank-txn-rule-filter/57"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/cash-management/bank-txn-rule-filter/85"
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

## GET /objects/cash-management/bank-txn-rule-filter/{key}
_Get a bank transaction rule filter_

**Response 200 — Get a bank transaction rule filter:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "23",
    "bankTransactionRule": {
      "id": "17",
      "key": "17",
      "href": "/objects/cash-management/bank-txn-rule/17"
    },
    "dataSource": "bankTransaction",
    "intacctTxnAttribute": null,
    "bankTxnAttribute": "transactionType",
    "operator": "equals",
    "value": "debit",
    "order": 2,
    "href": "/objects/cash-management/bank-txn-rule-filter/110"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-txn-rule-group
_List bank transaction rule groups_

**Response 200 — List bank transaction rule groups:**
```json
{
  "ia::result": [
    {
      "key": "9",
      "id": "9",
      "href": "/objects/cash-management/bank-txn-rule-group/9"
    },
    {
      "key": "21",
      "id": "21",
      "href": "/objects/cash-management/bank-txn-rule-group/21"
    },
    {
      "key": "35",
      "id": "35",
      "href": "/objects/cash-management/bank-txn-rule-group/35"
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

## GET /objects/cash-management/bank-txn-rule-group/{key}
_Get a bank transaction rule group_

**Response 200 — Get a bank transaction rule group:**
```json
{
  "ia::result": {
    "key": "27",
    "id": "27",
    "bankTransactionRule": {
      "id": "21",
      "key": "21",
      "href": "/objects/cash-management/bank-txn-rule/21"
    },
    "dataSource": "intacctTransaction",
    "intacctTxnAttribute": "documentNumber",
    "bankTxnAttribute": null,
    "order": 1,
    "href": "/objects/cash-management/bank-txn-rule-group/27"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-txn-rule-map
_List bank transaction rule maps_

**Response 200 — List bank transaction rule maps:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/bank-txn-rule-map/1"
    },
    {
      "key": "26",
      "id": "26",
      "href": "/objects/cash-management/bank-txn-rule-map/26"
    },
    {
      "key": "182",
      "id": "182",
      "href": "/objects/cash-management/bank-txn-rule-map/182"
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

## GET /objects/cash-management/bank-txn-rule-map/{key}
_Get a bank transaction rule map_

**Response 200 — Get a bank transaction rule map:**
```json
{
  "ia::result": {
    "id": "2",
    "key": "2",
    "bankTxnRule": {
      "id": "28",
      "key": "28",
      "ruleId": "Match_Amt_Plus_Date_Range",
      "name": "Match amount plus 2 day range",
      "ruleType": "create",
      "href": "/objects/cash-management/bank-txn-rule/28"
    },
    "bankTxnRuleSet": {
      "id": "2",
      "key": "2",
      "href": "/objects/cash-management/bank-txn-rule-set/2"
    },
    "ruleOrder": 2,
    "audit": {
      "createdDateTime": "2025-03-27T00:00:00Z",
      "modifiedDateTime": "2025-03-27T00:00:00Z",
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
    "href": "/objects/cash-management/bank-txn-rule-map/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/bank-txn-rule-map/{key}
_Delete a bank transaction rule map_


## GET /objects/cash-management/bank-txn-rule-match
_List bank transaction rule matches_

**Response 200 — List bank transaction rule matches:**
```json
{
  "ia::result": [
    {
      "key": "97",
      "id": "97",
      "href": "/objects/cash-management/bank-txn-rule-match/97"
    },
    {
      "key": "100",
      "id": "100",
      "href": "/objects/cash-management/bank-txn-rule-match/100"
    },
    {
      "key": "104",
      "id": "104",
      "href": "/objects/cash-management/bank-txn-rule-match/104"
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

## GET /objects/cash-management/bank-txn-rule-match/{key}
_Get a bank transaction rule match entry_

**Response 200 — Get a bank transaction rule match entry:**
```json
{
  "ia::result": {
    "key": "28",
    "id": "28",
    "bankTransactionRule": {
      "id": "21",
      "key": "21",
      "href": "/objects/cash-management/bank-txn-rule/21"
    },
    "intacctTxnAttribute": "amount",
    "bankTxnAttribute": "amount",
    "operator": "equals",
    "value": "100",
    "order": 2,
    "href": "/objects/cash-management/bank-txn-rule-match/28"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-txn-rule-set
_List bank transaction rule sets_

**Response 200 — List bank transaction rule sets:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/bank-txn-rule-set/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/cash-management/bank-txn-rule-set/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/bank-txn-rule-set/3"
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

## POST /objects/cash-management/bank-txn-rule-set
_Create a bank transaction rule set_

**Request example — Create a bank transaction rule set:**
```json
{
  "ruleSetId": "TalComp_Operating_Rules",
  "name": "TalComp Training - Operating Account Rules",
  "description": "Rule set for all training related operating account transactions.",
  "accountType": "creditcard",
  "location": {
    "key": "1"
  },
  "status": "active"
}
```
**Response 201 — Create a bank transaction rule set:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/cash-management/bank-txn-rule-set/5"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-txn-rule-set-run-detail
_List bank transaction rule set run details_

**Response 200 — List bank transaction rule set run details:**
```json
{
  "ia::result": [
    {
      "key": "10",
      "id": "10",
      "href": "/objects/cash-management/bank-txn-rule-set-run-detail/10"
    },
    {
      "key": "11",
      "id": "11",
      "href": "/objects/cash-management/bank-txn-rule-set-run-detail/11"
    },
    {
      "key": "12",
      "id": "12",
      "href": "/objects/cash-management/bank-txn-rule-set-run-detail/12"
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

## GET /objects/cash-management/bank-txn-rule-set-run-detail/{key}
_Get a bank transaction rule set run detail_

**Response 200 — Get bank transaction rule set run details:**
```json
{
  "ia::result": {
    "id": "10",
    "key": "10",
    "bankTxnRuleSetRunLog": {
      "id": "1",
      "key": "1",
      "href": "/objects/cash-management/bank-txn-rule-set-run-log/1"
    },
    "bankTxnRule": {
      "key": "10",
      "id": "match-by-amount",
      "href": "/objects/cash-management/bank-txn-rule/10"
    },
    "intacctTxnRecord": {
      "id": "53",
      "key": "53",
      "href": "/objects/cash-management/reconciliation-source-record/53"
    },
    "bankTxnRecord": {
      "id": "33",
      "key": "33",
      "href": "/objects/cash-management/bank-transaction/33"
    },
    "status": "success",
    "errorMessage": null,
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2024-05-28T11:45:18Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/cash-management/bank-txn-rule-set-run-detail/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-txn-rule-set-run-log
_List bank transaction rule set run logs_

**Response 200 — List bank transaction rule set run logs:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/bank-txn-rule-set-run-log/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/cash-management/bank-txn-rule-set-run-log/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/bank-txn-rule-set-run-log/3"
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

## POST /objects/cash-management/bank-txn-rule-set-run-log
_Create a bank transaction rule set run log_

**Request example — Create a bank transaction rule set run log:**
```json
{
  "bankAccount": {
    "id": "BOA"
  },
  "feedType": "csv"
}
```
**Response 201 — Reference to bank transaction rule set run log:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/cash-management/bank-txn-rule-set-run-log/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/bank-txn-rule-set-run-log/{key}
_Get a bank transaction rule set run log_

**Response 200 — Get a bank transaction rule set run log:**
```json
{
  "ia::result": {
    "id": "1",
    "key": "1",
    "bankAccount": {
      "key": "1",
      "id": "BOA",
      "name": "VISA",
      "href": "/objects/cash-management/bank-account/1"
    },
    "bankTxnRuleSet": {
      "key": "1",
      "id": "RuleSetToMatch",
      "href": "/objects/cash-management/bank-txn-rule-set/1"
    },
    "feedType": "csv",
    "totalProcessedTxns": "8",
    "totalProcessedBankTxns": "4",
    "totalMatchedTxns": "1",
    "startDateTime": "05/28/2024 11:45:17",
    "endDateTime": "05/28/2024 11:45:18",
    "status": "success",
    "errorMessage": null,
    "ruleCount": "2",
    "totalCreatedTxns": "0",
    "audit": {
      "createdBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "bankTxnRuleSetRunDetail": [
      {
        "id": "10",
        "key": "10",
        "bankTxnRuleSetRunLog": {
          "id": "1",
          "key": "1",
          "href": "/objects/cash-management/bank-txn-rule-set-run-log/1"
        },
        "bankTxnRule": {
          "key": "10",
          "id": "match-by-amount",
          "href": "/objects/cash-management/bank-txn-rule/10"
        },
        "intacctTxnRecord": {
          "id": "53",
          "key": "53",
          "href": "/objects/cash-management/reconciliation-source-record/53"
        },
        "bankTxnRecord": {
          "id": "33",
          "key": "33",
          "href": "/objects/cash-management/bank-transaction/33"
        },
        "status": "success",
        "errorMessage": null,
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2024-05-28T11:45:18Z"
        },
        "href": "/objects/cash-management/bank-txn-rule-set-run-detail/10"
      }
    ],
    "href": "/objects/cash-management/bank-txn-rule-set-run-log/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/bank-txn-rule-set/{key}
_Get a bank transaction rule set_

**Response 200 — Get a bank transaction rule set:**
```json
{
  "ia::result": {
    "id": "2",
    "key": "2",
    "ruleSetId": "BankRuleSetChase",
    "name": "Rule set for chase bank",
    "description": "Primary rule set for CB",
    "accountType": "bank",
    "numberOfAccounts": 7,
    "numberOfRules": 1,
    "status": "active",
    "location": {
      "key": "5"
    },
    "audit": {
      "createdDateTime": "2025-01-26T00:15:14Z",
      "modifiedDateTime": "2025-03-24T21:41:10Z",
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
    "rules": [
      {
        "id": "26",
        "key": "26",
        "bankTxnRule": {
          "id": "11",
          "key": "11",
          "ruleId": "gl-create-rule-2",
          "name": "gl-create-rule-2",
          "ruleType": "create",
          "href": "/objects/cash-management/bank-txn-rule/11"
        },
        "bankTxnRuleSet": {
          "id": "2",
          "key": "2",
          "href": "/objects/cash-management/bank-txn-rule-set/2"
        },
        "ruleOrder": 1,
        "audit": {
          "createdDateTime": "2025-03-24T00:00:00Z",
          "modifiedDateTime": "2025-03-24T00:00:00Z",
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
        "href": "/objects/cash-management/bank-txn-rule-map/26"
      }
    ],
    "href": "/objects/cash-management/bank-txn-rule-set/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/bank-txn-rule-set/{key}
_Update a bank transaction rule set_

**Request example — Update bank transaction rule set:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to bank transaction rule set:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "4",
    "href": "/objects/cash-management/bank-txn-rule-set/4"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/cash-management/bank-txn-rule-set/{key}
_Delete a bank transaction rule set_


## GET /objects/cash-management/bank-txn-rule/{key}
_Get a bank transaction rule_

**Response 200 — Get a bank transaction create rule:**
```json
{
  "ia::result": {
    "id": "79",
    "key": "79",
    "ruleId": "BOA-CC-TXN-2119",
    "name": "BOA Create CC txn from bank txn",
    "description": "BOA rule to create CC txn from bank txn.",
    "ruleType": "create",
    "createRuleObject": {
      "objectType": "journalEntry",
      "journalEntryTemplate": {
        "id": "3",
        "key": "3",
        "href": "/objects/cash-management/journal-entry-template/3"
      },
      "creditCardTxnTemplate": {
        "id": null,
        "key": null
      }
    },
    "status": "active",
    "location": {
      "key": null
    },
    "rulesetCount": 0,
    "audit": {
      "createdDateTime": "2025-03-27T16:13:03Z",
      "modifiedDateTime": "2025-03-27T16:13:03Z",
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
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "filterAttributes": [
      {
        "id": "81",
        "key": "81",
        "bankTransactionRule": {
          "id": "79",
          "key": "79",
          "href": "/objects/cash-management/bank-txn-rule/79"
        },
        "dataSource": "bankTransaction",
        "intacctTxnAttribute": null,
        "bankTxnAttribute": "postingDate",
        "operator": "greaterThan",
        "value": "07/03/2025",
        "order": 1,
        "href": "/objects/cash-management/bank-txn-rule-filter/81"
      },
      {
        "id": "82",
        "key": "82",
        "bankTransactionRule": {
          "id": "79",
          "key": "79",
          "href": "/objects/cash-management/bank-txn-rule/79"
        },
        "dataSource": "bankTransaction",
        "intacctTxnAttribute": null,
        "bankTxnAttribute": "transactionType",
        "operator": "equals",
        "value": "debit",
        "order": 1,
        "href": "/objects/cash-management/bank-txn-rule-filter/82"
      }
    ],
    "groupAttributes": [],
    "matchRuleAttributes": [],
    "href": "/objects/cash-management/bank-txn-rule/79"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a match bank transaction rule:**
```json
{
  "ia::result": {
    "id": "28",
    "key": "28",
    "ruleId": "Match_Amt_Plus_Date_Range",
    "name": "Match amount plus date range",
    "description": "Match amount and 2 days range",
    "ruleType": "match",
    "createRuleObject": {
      "objectType": "journalEntry",
      "journalEntryTemplate": {
        "id": "3",
        "key": "3",
        "href": "/objects/cash-management/journal-entry-template/3"
      },
      "creditCardTxnTemplate": {
        "id": null,
        "key": null
      }
    },
    "status": "active",
    "location": {
      "key": null
    },
    "rulesetCount": 0,
    "audit": {
      "createdDateTime": "2025-03-27T16:24:18Z",
      "modifiedDateTime": "2025-03-27T16:24:18Z",
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
    "filterAttributes": [
      {
        "id": "36",
        "key": "36",
        "bankTransactionRule": {
          "id": "28",
          "key": "28",
          "href": "/objects/cash-management/bank-txn-rule/28"
        },
        "dataSource": "bankTransaction",
        "intacctTxnAttribute": null,
        "bankTxnAttribute": "postingDate",
        "operator": "greaterThan",
        "value": "01/03/2025",
        "order": 1,
        "href": "/objects/cash-management/bank-txn-rule-filter/36"
      },
      {
        "id": "37",
        "key": "37",
        "bankTransactionRule": {
          "id": "28",
          "key": "28",
          "href": "/objects/cash-management/bank-txn-rule/28"
        },
        "dataSource": "bankTransaction",
        "intacctTxnAttribute": null,
        "bankTxnAttribute": "transactionType",
        "operator": "equals",
        "value": "debit",
        "order": 2,
        "href": "/objects/cash-management/bank-txn-rule-filter/37"
      }
    ],
    "groupAttributes": [],
    "matchRuleAttributes": [
      {
        "id": "33",
        "key": "33",
        "bankTransactionRule": {
          "id": "28",
          "key": "28",
          "href": "/objects/cash-management/bank-txn-rule/28"
        },
        "intacctTxnAttribute": "amount",
        "bankTxnAttribute": "amount",
        "operator": "equals",
        "value": "100",
        "order": 1,
        "href": "/objects/cash-management/bank-txn-rule-match/33"
      },
      {
        "id": "34",
        "key": "34",
        "bankTransactionRule": {
          "id": "28",
          "key": "28",
          "href": "/objects/cash-management/bank-txn-rule/28"
        },
        "intacctTxnAttribute": "postingDate",
        "bankTxnAttribute": "postingDate",
        "operator": "within",
        "value": "2",
        "order": 2,
        "href": "/objects/cash-management/bank-txn-rule-match/34"
      }
    ],
    "href": "/objects/cash-management/bank-txn-rule/28"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/bank-txn-rule/{key}
_Update a bank transaction rule_

**Request example — Update a bank transaction rule:**
```json
{
  "matchRuleAttributes": [
    {
      "key": "33",
      "order": 2
    },
    {
      "key": "34",
      "intacctTxnAttribute": "postingDate",
      "bankTxnAttribute": "postingDate",
      "operator": "within",
      "value": "4",
      "order": 1
    }
  ]
}
```
**Response 200 — Reference to updated bank transaction rule:**
```json
{
  "ia::result": {
    "key": "28",
    "id": "28",
    "href": "/objects/cash-management/bank-txn-rule/28"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/bank-txn-rule/{key}
_Delete a bank transaction rule_


## GET /objects/cash-management/checking-account
_List checking accounts_

**Response 200 — List checking accounts:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "AUDCHK",
      "href": "/objects/cash-management/checking-account/84"
    },
    {
      "key": "85",
      "id": "BDF",
      "href": "/objects/cash-management/checking-account/85"
    },
    {
      "key": "60",
      "id": "BOA",
      "href": "/objects/cash-management/checking-account/60"
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

## POST /objects/cash-management/checking-account
_Create a checking account_

**Request example — Create a checking account:**
```json
{
  "id": "BOA",
  "bankAccountDetails": {
    "accountNumber": "890000088",
    "bankName": "Bank of America",
    "routingNumber": "123456789",
    "branchId": "00-1355",
    "phoneNumber": "9007780000",
    "bankAddress": {
      "addressLine1": "40714",
      "addressLine2": "Grimmer Blvd",
      "addressLine3": "West Cameron",
      "city": "Fremont",
      "country": "United States",
      "postCode": "98765",
      "state": "CA"
    },
    "currency": "USD",
    "accountHolderName": "ACME Software"
  },
  "accounting": {
    "glAccount": {
      "id": "9090.09.90-RestNextGenGL"
    },
    "apJournal": {
      "id": "AR ADJ-AR Adjustment Journal"
    },
    "arJournal": {
      "id": "RCPT-Receipts Journal"
    },
    "bankingTimeZone": "GMT+02:00 Central Europe Summer Time",
    "serviceChargeAccountLabel": {
      "key": "15"
    },
    "interestAccountLabel": {
      "id": "Sales"
    },
    "disableInterEntityTransfer": false
  },
  "checkPrinting": {
    "addressSettings": {
      "addressToPrint": "company",
      "printAddress": true,
      "printLogo": true,
      "address": {
        "addressLine1": "75688 Post st",
        "addressLine2": "456",
        "addressLine3": "West Cameron",
        "city": "San Jose",
        "country": "United States",
        "countryCode": "US",
        "postCode": "94536",
        "state": "CA",
        "phone": "6609336532"
      },
      "name": "Zine Inc."
    },
    "micrSettings": {
      "regionalSettings": {
        "positionOfOnUsSymbol": "position31",
        "printCode45": true,
        "printOnUsSymbol": true,
        "printUSFundsUnderCheckAmount": false
      },
      "accountNumberAlignment": "right",
      "accountNumberPositioning": 1,
      "minCheckNumberLength": "6"
    },
    "printSettings": {
      "additionalText": "Pay to check holder",
      "paperFormat": "top",
      "printLineItems": true,
      "printLocation": "id",
      "printingFormat": "standard",
      "nextCheckNumber": "1012",
      "numberOfChecksInPreview": "One",
      "printOn": "blankCheckStock"
    },
    "signatures": {
      "firstSignature": "sigimg1_g.gif",
      "limitForFirstSignatureAmount": "20",
      "limitForSecondSignatureAmount": "30",
      "secondSignature": "sigimg2_g.gif",
      "thresholdForSecondSignatureAmount": "99.00"
    },
    "disablePrinting": false
  },
  "reconciliation": {
    "matchSequence": {
      "key": "48"
    },
    "useMatchSequenceForAutoMatch": true,
    "useMatchSequenceForManualMatch": true
  },
  "ach": {
    "bankId": "ACH-1",
    "companyName": "origin",
    "companyIdentification": "originid",
    "originatingFinancialInstitution": "8909",
    "companyEntryDescription": "entry desc",
    "companyDiscretionaryData": "disc",
    "serviceClassCode": "220",
    "batchId": "BOA_ACH_BatchNo",
    "traceNumberSequence": "BOA_ACH_TraceNo",
    "paymentNumberSequence": "CONTINVOICE",
    "useTraceNumber": "T",
    "enableACH": true,
    "useRecommendedSetup": true
  },
  "ruleSet": {
    "key": "53",
    "id": "MatchDateAmountGrpbyDateRuleSet"
  },
  "restrictions": {
    "restrictionType": "restricted",
    "locations": [
      "1-United States of America",
      "200-My New Entity"
    ]
  },
  "location": {
    "key": "1",
    "id": "1-United States of America"
  }
}
```
**Response 201 — Reference to new checking account:**
```json
{
  "id": "BOA-000987g",
  "bankAccountDetails": {
    "accountNumber": "890000088",
    "bankName": "Bank of America",
    "routingNumber": "123456789",
    "branchId": "00-1355",
    "phoneNumber": "9007780000",
    "bankAddress": {
      "addressLine1": "40714",
      "addressLine2": "Grimmer Blvd",
      "addressLine3": null,
      "city": "Fremont",
      "country": "United States",
      "postCode": "98765",
      "state": "CA"
    },
    "currency": "GBP",
    "accountHolderName": "ACME Software"
  },
  "accounting": {
    "glAccount": {
      "id": "9090.09.90-RestNextGenGL"
    },
    "apJournal": {
      "id": "AR ADJ-AR Adjustment Journal"
    },
    "arJournal": {
      "id": "CHASE D-CHASE BANK DISB"
    },
    "bankingTimeZone": "GMT+05:30 Bombay, Calcutta, Madras, New Delhi",
    "serviceChargeAccountLabel": {
      "key": "15"
    },
    "interestAccountLabel": {
      "id": "Sales"
    },
    "disableInterEntityTransfer": false
  },
  "checkPrinting": {
    "addressSettings": {
      "addressToPrint": "company",
      "printAddress": true,
      "printLogo": true,
      "address": {
        "addressLine1": "75688 Post st",
        "addressLine2": "456",
        "addressLine3": null,
        "city": "San Jose",
        "country": "United States",
        "countryCode": "US",
        "postCode": "94536",
        "state": "CA",
        "phone": "6609336532"
      },
      "name": "Zine Inc."
    },
    "micrSettings": {
      "regionalSettings": {
        "positionOfOnUsSymbol": "position31",
        "printCode45": true,
        "printOnUsSymbol": true,
        "printUSFundsUnderCheckAmount": false
      },
      "accountNumberAlignment": "right",
      "accountNumberPositioning": 1,
      "minCheckNumberLength": "6"
    },
    "printSettings": {
      "additionalText": "Pay to check holder",
      "paperFormat": "top",
      "printLineItems": true,
      "printLocation": "id",
      "printingFormat": "standard",
      "nextCheckNumber": "1012",
      "// \"printPreview\"": "One",
      "printOn": "blankCheckStock"
    },
    "signatures": {
      "firstSignature": "sigimg1_g.gif",
      "limitForFirstSignatureAmount": null,
      "limitForSecondSignatureAmount": null,
      "secondSignature": "sigimg2_g.gif",
      "thresholdForSecondSignatureAmount": "99.00"
    },
    "disablePrinting": false
  },
  "reconciliation": {
    "matchSequence": {
      "key": "48"
    },
    "useMatchSequenceForAutoMatch": true,
    "useMatchSequenceForManualMatch": true
  },
  "department": {
    "id": "11-Accounting"
  },
  "location": {
    "id": "1-United States of America"
  }
}
```

## GET /objects/cash-management/checking-account/{key}
_Get a checking account_

**Response 200 — Get a checking account:**
```json
{
  "ia::result": {
    "id": "BOA-000987g",
    "bankAccountDetails": {
      "accountNumber": "890000088",
      "bankName": "Bank of America",
      "routingNumber": "123456789",
      "branchId": "00-1355",
      "phoneNumber": "9007780000",
      "bankAddress": {
        "addressLine1": "40714",
        "addressLine2": "Grimmer Blvd",
        "addressLine3": null,
        "city": "Fremont",
        "country": "United States",
        "postCode": "98765",
        "state": "CA"
      },
      "currency": "GBP",
      "accountHolderName": "ACME Software"
    },
    "accounting": {
      "glAccount": {
        "id": "9090.09.90-RestNextGenGL",
        "key": "584",
        "name": "RestNextGenGL",
        "href": "/objects/general-ledger/account/584"
      },
      "apJournal": {
        "id": "AR ADJ-AR Adjustment Journal",
        "key": "17",
        "href": "/objects/general-ledger/journal/17"
      },
      "arJournal": {
        "id": "CHASE D-CHASE BANK DISB",
        "key": "12",
        "href": "/objects/general-ledger/journal/12"
      },
      "bankingTimeZone": "GMT+05:30 Bombay, Calcutta, Madras, New Delhi",
      "serviceChargeGLAccount": {
        "key": null,
        "id": null
      },
      "serviceChargeAccountLabel": {
        "key": "15",
        "id": "Car Payment",
        "href": "/objects/accounts-payable/account-label/15"
      },
      "interestGLAccount": {
        "key": null,
        "id": null
      },
      "interestAccountLabel": {
        "key": null,
        "id": null
      },
      "disableInterEntityTransfer": false
    },
    "checkPrinting": {
      "addressSettings": {
        "addressToPrint": "company",
        "printAddress": true,
        "printLogo": true,
        "address": {
          "addressLine1": "75688 Post st",
          "addressLine2": "456",
          "addressLine3": null,
          "city": "San Jose",
          "country": "United States",
          "countryCode": "US",
          "postCode": "94536",
          "state": "CA",
          "phone": "6609336532"
        },
        "name": "Zine Inc."
      },
      "micrSettings": {
        "regionalSettings": {
          "positionOfOnUsSymbol": "position31",
          "printCode45": true,
          "printOnUsSymbol": true,
          "printUSFundsUnderCheckAmount": false
        },
        "accountNumberAlignment": "right",
        "accountNumberPositioning": 1,
        "minCheckNumberLength": "6"
      },
      "printSettings": {
        "additionalText": "Pay to check holder",
        "paperFormat": "top",
        "printLineItems": true,
        "printLocation": "id",
        "printingFormat": "standard",
        "nextCheckNumber": "1012",
        "numberOfChecksInPreview": "one",
        "printOn": "blankCheckStock"
      },
      "signatures": {
        "firstSignature": "sigimg1_g.gif",
        "limitForFirstSignatureAmount": null,
        "limitForSecondSignatureAmount": null,
        "secondSignature": "sigimg2_g.gif",
        "thresholdForSecondSignatureAmount": "99.00"
      },
      "disablePrinting": false
    },
    "reconciliation": {
      "matchSequence": {
        "key": "48",
        "id": "48-bankseq-1",
        "href": "/objects/company-config/document-sequence/48"
      },
      "useMatchSequenceForAutoMatch": true,
      "useMatchSequenceForManualMatch": true,
      "lastReconciledBalance": null,
      "lastReconciledDate": null,
      "cutOffDate": null,
      "inProgressBalance": null,
      "inProgressDate": null
    },
    "department": {
      "key": "9",
      "id": "11-Accounting",
      "href": "/objects/company-config/department/9"
    },
    "location": {
      "key": "1",
      "id": "1-United States of America",
      "href": "/objects/company-config/location/1"
    },
    "status": "active",
    "audit": {
      "createdDateTime": "2024-03-07T19:39:43Z",
      "modifiedDateTime": "2024-03-07T19:39:43Z",
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
    "key": "291",
    "ach": {
      "bankId": null,
      "companyName": null,
      "companyIdentification": null,
      "originatingFinancialInstitution": null,
      "companyEntryDescription": null,
      "companyDiscretionaryData": null,
      "recordTypeCode": "5",
      "serviceClassCode": "220",
      "originatorStatusCode": "1",
      "batchId": null,
      "traceNumberSequence": null,
      "paymentNumberSequence": null,
      "useTraceNumber": "useAsPayment",
      "enableACH": null,
      "useRecommendedSetup": null
    },
    "bankingCloudConnection": {
      "status": "notConnected",
      "bankName": null,
      "name": null,
      "lastBankTxnDateTime": null,
      "lastRefreshedDateTime": null,
      "refreshStatus": null,
      "supportMultiAccountLinking": null
    },
    "bankFile": {
      "enableBankFile": false,
      "bankFileFormat": null,
      "bankCode": null,
      "apcaNumber": null,
      "sunNumber": null,
      "bsbNumber": null,
      "sortCode": null,
      "seedValue": null,
      "userReference": null,
      "clientCode": null,
      "serviceType": null,
      "originatorId": null,
      "businessIdCode": null,
      "processingDataCenterCode": null,
      "debtorBankNumber": null,
      "returnAccountNumber": null,
      "branchTransitNumber": null,
      "messageIdPrefix": null,
      "immediateDestinationId": null,
      "immediateOriginId": null,
      "immediateDestinationName": null,
      "immediateOriginName": null,
      "companyName": null,
      "paymentNumberSequence": null,
      "fileIdSequence": null,
      "companyEntryDescription": null,
      "postalAddress": {
        "addressLine1": null,
        "addressLine2": null,
        "postCode": null,
        "county": null,
        "countryCode": null
      }
    },
    "financialInstitution": {
      "key": null,
      "id": null
    },
    "ruleSet": {
      "id": "53-MatchDateAmountGrpbyDateRuleSet",
      "key": "53",
      "name": "MatchDateAmountGrpbyDateRuleSet",
      "href": "/objects/cash-management/bank-txn-rule-set/53"
    },
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "paymentProviderBankAccounts": [],
    "href": "/objects/cash-management/checking-account/291"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a checking account enabled for bank files for United States (US):**
```json
{
  "ia::result": {
    "id": "USBankfileAccount001",
    "bankAccountDetails": {
      "accountNumber": "890000088",
      "bankName": "Bank of America",
      "routingNumber": "123456789",
      "branchId": 6578,
      "phoneNumber": "9007780000",
      "bankAddress": {
        "addressLine1": "40714",
        "addressLine2": "Grimmer Blvd",
        "addressLine3": null,
        "city": "Fremont",
        "country": "United States",
        "postCode": "98765",
        "state": "CA"
      },
      "currency": "GBP",
      "accountHolderName": "ACME Software"
    },
    "accounting": {
      "glAccount": {
        "id": "9090.09.90-RestNextGenGL",
        "key": "584",
        "href": "/objects/general-ledger/account/584"
      },
      "apJournal": {
        "id": "AR ADJ-AR Adjustment Journal",
        "key": "17",
        "href": "/objects/general-ledger/journal/17"
      },
      "arJournal": {
        "id": "CHASE D-CHASE BANK DISB",
        "key": "12",
        "href": "/objects/general-ledger/journal/12"
      },
      "bankingTimeZone": "GMT+05:30 Bombay, Calcutta, Madras, New Delhi",
      "serviceChargeGLAccount": {
        "key": null,
        "id": null
      },
      "serviceChargeAccountLabel": {
        "key": "15",
        "id": "Car Payment",
        "href": "/objects/accounts-payable/account-label/15"
      },
      "interestGLAccount": {
        "key": null,
        "id": null
      },
      "interestAccountLabel": {
        "key": null,
        "id": null
      },
      "disableInterEntityTransfer": false
    },
    "checkPrinting": {
      "addressSettings": {
        "addressToPrint": "company",
        "printAddress": true,
        "printLogo": true,
        "address": {
          "addressLine1": "75688 Post st",
          "addressLine2": "456",
          "addressLine3": null,
          "city": "San Jose",
          "country": "United States",
          "countryCode": "US",
          "postCode": "94536",
          "state": "CA",
          "phone": "6609336532"
        },
        "name": "Zine Inc."
      },
      "micrSettings": {
        "regionalSettings": {
          "positionOfOnUsSymbol": "position31",
          "printCode45": true,
          "printOnUsSymbol": true,
          "printUSFundsUnderCheckAmount": false
        },
        "accountNumberAlignment": "right",
        "accountNumberPositioning": 1,
        "minCheckNumberLength": "6"
      },
      "printSettings": {
        "additionalText": "Pay to check holder",
        "paperFormat": "top",
        "printLineItems": true,
        "printLocation": "id",
        "printingFormat": "standard",
        "nextCheckNumber": "1012",
        "numberOfChecksInPreview": "one",
        "printOn": "blankCheckStock"
      },
      "signatures": {
        "firstSignature": "sigimg1_g.gif",
        "limitForFirstSignatureAmount": null,
        "limitForSecondSignatureAmount": null,
        "secondSignature": "sigimg2_g.gif",
        "thresholdForSecondSignatureAmount": "99.00"
      },
      "disablePrinting": false
    },
    "reconciliation": {
      "matchSequence": {
        "key": "48",
        "id": "48-bankseq-1",
        "href": "/objects/company-config/document-sequence/48"
      },
      "useMatchSequenceForAutoMatch": true,
      "useMatchSequenceForManualMatch": true,
      "lastReconciledBalance": null,
      "lastReconciledDate": null,
      "cutOffDate": null,
      "inProgressBalance": null,
      "inProgressDate": null
    },
    "department": {
      "key": "9",
      "id": "11-Accounting",
      "href": "/objects/company-config/department/9"
    },
    "location": {
      "key": "1",
      "id": "1-United States of America",
      "href": "/objects/company-config/location/1"
    },
    "status": "active",
    "audit": {
      "createdDateTime": "2024-03-07T19:39:43Z",
      "modifiedDateTime": "2024-03-07T19:39:43Z",
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
    "key": "291",
    "ach": {
      "bankId": null,
      "companyName": null,
      "companyIdentification": null,
      "originatingFinancialInstitution": null,
      "companyEntryDescription": null,
      "companyDiscretionaryData": null,
      "recordTypeCode": "5",
      "serviceClassCode": "220",
      "originatorStatusCode": "1",
      "batchId": null,
      "traceNumberSequence": null,
      "paymentNumberSequence": null,
      "useTraceNumber": "useAsPayment",
      "enableACH": null,
      "useRecommendedSetup": null
    },
    "bankingCloudConnection": {
      "status": "notConnected",
      "bankName": null,
      "name": null,
      "lastBankTxnDateTime": null,
      "lastRefreshedDateTime": null,
      "refreshStatus": null,
      "supportMultiAccountLinking": null
    },
    "bankFile": {
      "enableBankFile": true,
      "bankFileFormat": "NACHA - Unbalanced",
      "bankCode": null,
      "apcaNumber": null,
      "sunNumber": null,
      "bsbNumber": null,
      "sortCode": null,
      "seedValue": null,
      "userReference": null,
      "clientCode": null,
      "serviceType": null,
      "originatorId": null,
      "businessIdCode": null,
      "processingDataCenterCode": null,
      "debtorBankNumber": null,
      "returnAccountNumber": null,
      "branchTransitNumber": null,
      "messageIdPrefix": null,
      "immediateDestinationId": "984569845",
      "immediateOriginId": "878767675",
      "immediateDestinationName": "BOA",
      "immediateOriginName": "Investment corp",
      "companyName": "Ventura",
      "paymentNumberSequence": "0000006",
      "fileIdSequence": "E",
      "companyEntryDescription": "Investment",
      "postalAddress": {
        "addressLine1": "75688 Post st",
        "addressLine2": "Suite 100",
        "postCode": "94536",
        "county": "North Yorkshire",
        "country": "GB"
      }
    },
    "financialInstitution": {
      "key": null,
      "id": null
    },
    "ruleSet": {
      "id": null,
      "key": null
    },
    "paymentProviderBankAccounts": [],
    "href": "/objects/cash-management/checking-account/143"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/checking-account/{key}
_Update a checking account_

**Request example — Update a checking account:**
```json
{
  "bankAccountDetails": {
    "bankName": "Bank of America New"
  },
  "ruleSet": {
    "key": "53",
    "id": "MatchDateAmountGrpbyDateRuleSet"
  },
  "restrictions": {
    "restrictionType": "unrestricted",
    "locations": []
  },
  "reconciliation": {
    "matchSequence": {
      "key": "48"
    },
    "useMatchSequenceForAutoMatch": true,
    "useMatchSequenceForManualMatch": true
  }
}
```
**Response 201 — Reference to updated checking account:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "AUDCHK",
      "href": "/objects/cash-management/checking-account/84"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/checking-account/{key}
_Delete a checking account_


## GET /objects/cash-management/credit-card-account
_List credit card accounts_

**Response 200 — List credit card accounts:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "MC001",
      "href": "/objects/cash-management/credit-card-account/1"
    },
    {
      "key": "2",
      "id": "MC002",
      "href": "/objects/cash-management/credit-card-account/2"
    },
    {
      "key": "3",
      "id": "AMEX_CARD_1",
      "href": "/objects/cash-management/credit-card-account/3"
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

## POST /objects/cash-management/credit-card-account
_Create a credit card account_

**Request example — Create a credit card account:**
```json
{
  "id": "V002",
  "accountDetails": {
    "description": "Card for employee expense",
    "cardType": "visa",
    "expirationMonth": "01",
    "expirationYear": "2028",
    "billingAddress": {
      "addressLine1": "1295",
      "addressLine2": null,
      "addressLine3": "Adobe Ave",
      "city": "San Jose",
      "country": "United States",
      "countryCode": "US",
      "postCode": "978754",
      "state": "CA"
    },
    "accountType": "credit",
    "currency": "USD"
  },
  "status": "active",
  "accounting": {
    "offsetGLAccount": {
      "id": "4564.44.44",
      "key": "561"
    },
    "otherFeesGLAccount": {
      "id": "0077",
      "key": "432"
    },
    "defaultAccrualBasisGLJournal": {
      "id": "DISB",
      "key": "14"
    },
    "disableInterEntityTransfer": false
  },
  "vendor": {
    "id": "First Security - Gold",
    "key": "263"
  },
  "department": {
    "id": "CHS--Channel Sales",
    "key": "34"
  },
  "location": {
    "id": "San Francisco"
  },
  "reconciliation": {
    "matchSequence": {
      "id": "48--bankseq-1"
    },
    "useMatchSequenceForAutoMatch": true,
    "useMatchSequenceForManualMatch": true
  },
  "ruleSet": {
    "key": "35",
    "id": "35--creditcard"
  }
}
```
**Response 201 — Reference to new credit card account object:**
```json
{
  "ia::result": {
    "key": "34",
    "id": "V002",
    "href": "/objects/cash-management/credit-card-account/34"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-account/{key}
_Get a credit card account_

**Response 200 — Get a credit card account:**
```json
{
  "ia::result": {
    "key": "106",
    "id": "V002",
    "accountDetails": {
      "description": "card for employee expense",
      "cardType": "visa",
      "expirationMonth": "01",
      "expirationYear": "2028",
      "billingAddress": {
        "addressLine1": "1295",
        "addressLine2": null,
        "addressLine3": "Adobe Ave",
        "city": "San Jose",
        "country": "United States",
        "countryCode": "US",
        "postCode": "978754",
        "state": "CA"
      },
      "accountType": "credit",
      "debitCardCheckingAccount": {
        "id": null,
        "key": null
      },
      "currency": "USD"
    },
    "status": "active",
    "accounting": {
      "offsetGLAccount": {
        "id": "8907.89",
        "key": "589",
        "href": "/objects/general-ledger/account/589"
      },
      "otherFeesGLAccount": {
        "id": "6700.01",
        "key": "323",
        "href": "/objects/general-ledger/account/323"
      },
      "defaultAccrualBasisGLJournal": {
        "id": "DISB",
        "key": "14",
        "href": "/objects/general-ledger/journal/14"
      },
      "defaultCashBasisGLJournal": {
        "id": null,
        "key": null
      },
      "bankingTimeZone": "GMT+01:00 Berlin, Stockholm, Rome, Bern, Brussels",
      "disableInterEntityTransfer": false,
      "otherFeesAPAccountLabel": {
        "id": "Bank Service Charge",
        "key": "11",
        "href": "/objects/accounts-payable/account-label/11"
      },
      "financeChargeGLAccount": {
        "id": "6700.02",
        "key": "324",
        "href": "/objects/general-ledger/account/324"
      },
      "financeChargeAPAccountLabel": {
        "id": "Bank Interest Earned",
        "key": "10",
        "href": "/objects/accounts-payable/account-label/10"
      },
      "useInEmployeeExpense": true,
      "employeeExpenseGLAccount": {
        "key": "287",
        "id": "6800.03",
        "href": "/objects/general-ledger/account/287"
      },
      "employeeExpenseAccountLabel": {
        "id": "Gas and Electric",
        "key": "23",
        "href": "/objects/accounts-payable/account-label/23"
      }
    },
    "vendor": {
      "id": "First Security - Gold",
      "key": "35",
      "href": "/objects/accounts-payable/vendor/35"
    },
    "department": {
      "id": "COMP--Compliance",
      "key": "16",
      "href": "/objects/company-config/department/16"
    },
    "location": {
      "id": "San Francisco",
      "key": "24",
      "href": "/objects/company-config/location/24"
    },
    "reconciliation": {
      "lastReconciledDate": null,
      "lastReconciledBalance": null,
      "inProgressDate": null,
      "inProgressBalance": null,
      "matchSequence": {
        "key": "48",
        "id": "48--bankseq-1",
        "href": "/objects/company-config/document-sequence/48"
      },
      "useMatchSequenceForAutoMatch": true,
      "useMatchSequenceForManualMatch": true,
      "cutOffDate": null
    },
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "audit": {
      "modifiedDateTime": "2024-03-12T23:46:56Z",
      "createdDateTime": "2024-03-04T20:33:04Z",
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
    "bankingCloudConnection": {
      "status": null,
      "bankName": null,
      "name": null,
      "lastBankTxnDateTime": null,
      "lastRefreshedDateTime": null,
      "refreshStatus": null,
      "supportMultiAccountLinking": null
    },
    "financialInstitution": {
      "key": null,
      "id": null
    },
    "ruleSet": {
      "id": "35--creditcard",
      "key": "35",
      "href": "/objects/cash-management/bank-txn-rule-set/35"
    },
    "href": "/objects/cash-management/credit-card-account/106"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/credit-card-account/{key}
_Update a credit card account_

**Request example — Update a credit card account:**
```json
{
  "accountDetails": {
    "description": "Card for employee expenses",
    "expirationMonth": "01",
    "expirationYear": "2030"
  }
}
```
**Response 200 — Reference to updated credit card account:**
```json
{
  "ia::result": {
    "key": "32",
    "id": "V002",
    "href": "/objects/cash-management/credit-card-account/32"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/credit-card-account/{key}
_Delete a credit card account_


## GET /objects/cash-management/credit-card-fee
_List credit card fees_

**Response 200 — List credit card fees:**
```json
{
  "ia::result": [
    {
      "key": "1718",
      "id": "1718",
      "href": "/objects/cash-management/credit-card-fee/1221"
    },
    {
      "key": "1717",
      "id": "1717",
      "href": "/objects/cash-management/credit-card-fee/1222"
    },
    {
      "key": "3228",
      "id": "3228",
      "href": "/objects/cash-management/credit-card-fee/1223"
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

## POST /objects/cash-management/credit-card-fee
_Create a credit card fee_

**Request example — Create a credit card fee:**
```json
{
  "txnDate": "2024-01-23",
  "referenceNumber": "9AB0212788Z",
  "description": "Fee for purchasing ad-hoc software.",
  "isInclusiveTax": true,
  "currency": {
    "txnCurrency": "USD",
    "baseCurrency": "USD"
  },
  "taxSolution": {
    "key": "5",
    "id": "Canadian Sales Tax - SYS"
  },
  "creditCardAccount": {
    "id": "VISA-002"
  },
  "attachment": {
    "id": "18"
  },
  "lines": [
    {
      "txnAmount": "550.00",
      "totalTxnAmount": "500.00",
      "description": "Purchasing fee",
      "glAccount": {
        "id": "7509.03"
      },
      "dimensions": {
        "location": {
          "id": "USA"
        },
        "department": {
          "id": "OP-EE"
        }
      },
      "taxEntries": [
        {
          "purchasingTaxDetail": {
            "key": "67"
          }
        }
      ]
    }
  ]
}
```
**Response 201 — Reference to new credit card fee:**
```json
{
  "ia::result": {
    "key": "501",
    "id": "501",
    "href": "/objects/cash-management/credit-card-fee/501"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-fee-line
_List credit card fee lines_

**Response 200 — List credit card fee lines:**
```json
{
  "ia::result": [
    {
      "key": "1717",
      "id": "1717",
      "href": "/objects/credit-card-fee-line/1717"
    },
    {
      "key": "1718",
      "id": "1718",
      "href": "/objects/credit-card-fee-line/1718"
    },
    {
      "key": "1719",
      "id": "1719",
      "href": "/objects/credit-card-fee-line/1719"
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

## GET /objects/cash-management/credit-card-fee-line/{key}
_Get a credit card fee line_

**Response 200 — Get a credit card fee line:**
```json
{
  "ia::result": {
    "id": "2955",
    "key": "2955",
    "creditCardFee": {
      "id": "563",
      "key": "563",
      "href": "/objects/cash-management/credit-card-fee/563"
    },
    "glAccount": {
      "key": "346",
      "id": "7509.03",
      "name": "Exchange Gain / Loss Account on Net Assets- AR",
      "href": "/objects/general-ledger/account/346"
    },
    "apAccountLabel": {
      "key": null,
      "id": null
    },
    "baseAmount": "14.50",
    "txnAmount": "14.50",
    "dimensions": {
      "department": {
        "key": "21",
        "id": "OP-EE",
        "name": "Operations Engineering",
        "href": "/objects/company-config/department/21"
      },
      "location": {
        "key": "65",
        "id": "RICH-065",
        "name": "Richmond District",
        "href": "/objects/company-config/location/65"
      },
      "project": {
        "key": "35",
        "id": "QSF - BTI",
        "name": "Quick Start Financial - Berkeley Technology Inc",
        "href": "/objects/projects/project/35"
      },
      "customer": {
        "key": "14",
        "id": "BTI",
        "name": "Berkeley Technology Inc",
        "href": "/objects/accounts-receivable/customer/14"
      },
      "vendor": {
        "key": "56",
        "id": "210",
        "name": "Office Supply and Copier Co.",
        "href": "/objects/accounts-payable/vendor/56"
      },
      "employee": {
        "key": "27",
        "id": "12",
        "name": "John Smith",
        "href": "/objects/company-config/employee/27"
      },
      "item": {
        "key": "117",
        "id": "DELL",
        "name": "DELL Laptops",
        "href": "/objects/inventory-control/item/117"
      },
      "class": {
        "key": "3",
        "id": "WSD",
        "name": "Whole Sales Distribution",
        "href": "/objects/company-config/class/3"
      }
    },
    "baseLocation": {
      "name": "Richmond District",
      "key": "65",
      "href": "/objects/company-config/location/65"
    },
    "description": "CC fee charge",
    "currency": {
      "txnCurrency": "USD",
      "baseCurrency": "USD"
    },
    "status": "active",
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "href": "/objects/cash-management/credit-card-fee-line/2955"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-fee-tax-entry
_List credit card fee tax entries_

**Response 200 — List credit card fee tax entries:**
```json
{
  "ia::result": [
    {
      "key": "39",
      "id": "39",
      "href": "/objects/cash-management/credit-card-fee-tax-entry/39"
    },
    {
      "key": "40",
      "id": "40",
      "href": "/objects/cash-management/credit-card-fee-tax-entry/40"
    },
    {
      "key": "42",
      "id": "42",
      "href": "/objects/cash-management/credit-card-fee-tax-entry/42"
    },
    {
      "key": "41",
      "id": "41",
      "href": "/objects/cash-management/credit-card-fee-tax-entry/41"
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

## GET /objects/cash-management/credit-card-fee-tax-entry/{key}
_Get a credit card fee tax entry_

**Response 200 — Get a credit card fee tax entry:**
```json
{
  "ia::result": {
    "key": "300",
    "id": "300",
    "baseTaxAmount": "100",
    "txnTaxAmount": "100",
    "description": "Standard Rate for UK Import Services",
    "taxRate": 5.5,
    "purchasingTaxDetail": {
      "id": "UK Export Reduced Rate",
      "key": "24",
      "href": "/objects/tax/purchasing-tax-detail/24"
    },
    "creditCardFeeLine": {
      "id": "148",
      "key": "148",
      "href": "/objects/cash-management/credit-card-fee-line/148"
    },
    "href": "/objects/cash-management/tax/credit-card-fee-tax-entry/300"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/credit-card-fee/{key}
_Get a credit card fee_

**Response 200 — Get a credit card fee:**
```json
{
  "ia::result": {
    "id": "563",
    "key": "563",
    "creditCardAccount": {
      "id": "A0000004"
    },
    "txnDate": "2024-01-26",
    "referenceNumber": "CCFee-001",
    "description": "Credit card fee for 02993",
    "currency": {
      "baseCurrency": "USD",
      "txnCurrency": "USD"
    },
    "totalEntered": "500.00",
    "txnTotalEntered": "500.00",
    "reversedBy": {
      "id": null,
      "key": null,
      "reversalDate": null
    },
    "reversalOf": {
      "id": null,
      "key": null,
      "txnDate": null
    },
    "state": null,
    "reconciliationState": "cleared",
    "clearingDate": "2024-01-23",
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "attachment": {
      "id": null,
      "key": null
    },
    "isInclusiveTax": false,
    "taxSolution": {
      "key": "5",
      "id": "Canadian Sales Tax - SYS",
      "href": "/objects/tax/tax-solution/5"
    },
    "lines": [
      {
        "id": "2955",
        "key": "2955",
        "creditCardFee": {
          "id": "563",
          "key": "563",
          "href": "/objects/cash-management/credit-card-fee/563"
        },
        "glAccount": {
          "key": "346",
          "id": "7509.03",
          "name": "Exchange Gain / Loss Account on Net Assets- AR",
          "href": "/objects/general-ledger/account/346"
        },
        "apAccountLabel": {
          "key": "123",
          "id": "Accounting Fees",
          "href": "/objects/accounts-payable/ap-account-label/14"
        },
        "baseAmount": "438.60",
        "txnAmount": "438.60",
        "dimensions": {
          "department": {
            "key": "21",
            "id": "OP-EE",
            "name": "Operations Engineering",
            "href": "/objects/company-config/department/21"
          },
          "location": {
            "key": "65",
            "id": "RICH-065",
            "name": "Richmond District",
            "href": "/objects/company-config/location/65"
          },
          "project": {
            "key": "35",
            "id": "QSF - BTI",
            "name": "Quick Start Financial - Berkeley Technology Inc",
            "href": "/objects/projects/project/35"
          },
          "customer": {
            "key": "14",
            "id": "BTI",
            "name": "Berkeley Technology Inc",
            "href": "/objects/accounts-receivable/customer/14"
          },
          "vendor": {
            "key": "56",
            "id": "210",
            "name": "Office Supply and Copier Co.",
            "href": "/objects/accounts-payable/vendor/56"
          },
          "employee": {
            "key": "27",
            "id": "12",
            "name": "John Smith",
            "href": "/objects/company-config/employee/27"
          },
          "item": {
            "key": "117",
            "id": "DELL",
            "name": "DELL Laptops",
            "href": "/objects/inventory-control/item/117"
          },
          "class": {
            "key": "3",
            "id": "WSD",
            "name": "Whole Sales Distribution",
            "href": "/objects/company-config/class/3"
          }
        },
        "baseLocation": {
          "name": "Richmond District",
          "key": "65",
          "href": "/objects/company-config/location/65"
        },
        "description": "CC fee charge",
        "currency": {
          "txnCurrency": "USD",
          "baseCurrency": "USD"
        },
        "status": "active",
        "audit": {
          "createdDateTime": "2025-04-11T12:56:46Z",
          "modifiedDateTime": "2025-04-11T12:56:46Z",
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
        "totalTxnAmount": "500.00",
        "taxEntries": [
          {
            "txnTaxAmount": "30.70",
            "baseTaxAmount": "30.70",
            "purchasingTaxDetail": {
              "id": "BC PST Standard Rate Services Purchase - CA",
              "key": "67",
              "href": "/objects/tax/purchasing-tax-detail/67"
            },
            "id": "144",
            "key": "144",
            "taxRate": 7,
            "creditCardFeeLine": {
              "id": "142",
              "key": "142",
              "href": "/objects/cash-management/credit-card-fee-line/142"
            },
            "href": "/objects/cash-management/credit-card-fee-tax-entry/144"
          },
          {
            "txnTaxAmount": "30.70",
            "baseTaxAmount": "30.70",
            "purchasingTaxDetail": {
              "id": "BC PST Standard Rate Goods Purchase - CA",
              "key": "65",
              "href": "/objects/tax/purchasing-tax-detail/65"
            },
            "id": "146",
            "key": "146",
            "taxRate": 7,
            "creditCardFeeLine": {
              "id": "142",
              "key": "142",
              "href": "/objects/cash-management/credit-card-fee-line/142"
            },
            "href": "/objects/cash-management/credit-card-fee-tax-entry/146"
          },
          {
            "txnTaxAmount": "30.00",
            "baseTaxAmount": "30.00",
            "purchasingTaxDetail": {
              "id": "BC PST Standard Rate Goods Purchase - CA",
              "key": "79",
              "href": "/objects/tax/purchasing-tax-detail/79"
            },
            "id": "160",
            "key": "160",
            "taxRate": 7,
            "creditCardFeeLine": {
              "id": "142",
              "key": "142",
              "href": "/objects/cash-management/credit-card-fee-line/142"
            },
            "href": "/objects/cash-management/credit-card-fee-tax-entry/160"
          }
        ],
        "href": "/objects/cash-management/credit-card-fee-line/2955"
      }
    ],
    "href": "/objects/cash-management/credit-card-fee/563"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/credit-card-fee/{key}
_Update a credit card fee_

**Request example — Update a credit card fee:**
```json
{
  "description": "Fee for purchasing tickets.",
  "isInclusiveTax": false,
  "lines": [
    {
      "key": "142",
      "totalTxnAmount": "500.00",
      "description": "Fee for purchasing tickets",
      "taxEntries": [
        {
          "purchasingTaxDetail": {
            "key": "65"
          }
        },
        {
          "purchasingTaxDetail": {
            "key": "79"
          }
        },
        {
          "purchasingTaxDetail": {
            "key": "67"
          }
        }
      ]
    }
  ]
}
```
**Response 200 — Reference to updated credit card fee:**
```json
{
  "ia::result": {
    "id": "563",
    "key": "563",
    "href": "/objects/cash-management/credit-card-fee/563"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-reconciliation
_List credit card reconciliations_

**Response 200 — List credit card reconciliations:**
```json
{
  "ia::result": [
    {
      "key": "16",
      "id": "16",
      "href": "/objects/cash-management/credit-card-reconciliation/16"
    },
    {
      "key": "17",
      "id": "17",
      "href": "/objects/cash-management/credit-card-reconciliation/17"
    },
    {
      "key": "120",
      "id": "120",
      "href": "/objects/cash-management/credit-card-reconciliation/120"
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

## POST /objects/cash-management/credit-card-reconciliation
_Create a credit card reconciliation_

**Request example — Create a credit card reconciliation for manual matching:**
```json
{
  "creditCardAccount": {
    "id": "A0000001"
  },
  "reconciliationDate": "2025-04-28",
  "cutoffDate": "2025-03-21",
  "endingBalance": "50000.35",
  "reconciliationMode": "manual"
}
```
**Request example — Create an credit card reconciliation with matches for review:**
```json
{
  "creditCardAccount": {
    "id": "A0000001"
  },
  "reconciliationDate": "2025-05-28",
  "cutoffDate": "2025-04-21",
  "endingBalance": "50000.35",
  "reconciliationMode": "automatchReview",
  "feedType": "xml"
}
```
**Response 201 — Reference to the new credit card reconciliation:**
```json
{
  "ia::result": {
    "id": "69",
    "key": "69",
    "href": "/objects/cash-management/credit-card-reconciliation/69"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-reconciliation-record
_List credit card reconciliation records_

**Response 200 — List credit card reconciliation records:**
```json
{
  "ia::result": [
    {
      "key": "993",
      "id": "993",
      "href": "/objects/cash-management/credit-card-reconciliation-record/993"
    },
    {
      "key": "1289",
      "id": "1289",
      "href": "/objects/cash-management/credit-card-reconciliation-record/1289"
    },
    {
      "key": "1475",
      "id": "1475",
      "href": "/objects/cash-management/credit-card-reconciliation-record/1475"
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

## GET /objects/cash-management/credit-card-reconciliation-record/{key}
_Get a credit card reconciliation record_

**Response 200 — Get a credit card reconciliation record:**
```json
{
  "ia::result": {
    "id": "1755",
    "key": "1755",
    "creditCardReconciliation": {
      "id": "120",
      "key": "120",
      "href": "/objects/cash-management/credit-card-reconciliation/120",
      "reconciliationDate": "2025-05-31"
    },
    "creditCardAccount": {
      "id": "A0000077",
      "key": "132",
      "href": "/objects/cash-management/credit-card-account/132"
    },
    "txnInformation": {
      "recordType": "chargePayoffPayment",
      "subledgerRecord": {
        "id": "484",
        "key": "484",
        "href": "/objects/accounts-payable/subledger-record/484"
      },
      "journalEntryLine": {
        "id": "15",
        "key": "15",
        "href": "/objects/general-ledger/journal-entry-line/15"
      },
      "initialOpenItem": {
        "id": "4",
        "key": "4",
        "href": "/objects/cash-management/initial-open-item/4"
      },
      "txnType": "withdrawal",
      "documentNumber": "DOC-10578",
      "documentDate": "2025-05-26",
      "txnAmount": "86.00",
      "baseAmount": "86.00",
      "txnCurrency": "USD",
      "baseCurrency": "USD",
      "postingDate": "2025-05-26",
      "reconciliationInformation": {
        "lastReconcileDate": "2025-05-07",
        "state": "cleared"
      },
      "payee": "Business Software Inc",
      "description": "Annual subscription for accounting software.",
      "postingState": "approved"
    },
    "audit": {
      "createdDateTime": "2024-05-28T00:00:00Z",
      "modifiedDateTime": "2024-05-28T00:00:00Z",
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
    "href": "/objects/cash-management/credit-card-reconciliation-record/1755"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-reconciliation/{key}
_Get a credit card reconciliation_

**Response 200 — Get a credit card reconciliation:**
```json
{
  "ia::result": {
    "id": 120,
    "key": "120",
    "creditCardAccount": {
      "id": "A0000077",
      "key": "132",
      "href": "/objects/cash-management/credit-card-account/132"
    },
    "reconciliationDate": "2025-05-07",
    "endingBalance": "-1011.00",
    "reconciliationMode": "manual",
    "reconciliationStatus": "reconciled",
    "feedType": "online",
    "audit": {
      "createdDateTime": "2024-10-31T00:00:00Z",
      "modifiedDateTime": "2025-05-28T00:00:00Z",
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
    "isReopened": false,
    "reconciliationSourceRecords": [
      {
        "id": "1755",
        "key": "1755",
        "creditCardReconciliation": {
          "id": "120",
          "key": "120",
          "href": "/objects/cash-management/credit-card-reconciliation/120"
        },
        "creditCardAccount": {
          "id": "A0000077",
          "key": "132",
          "href": "/objects/cash-management/credit-card-account/132"
        },
        "txnInformation": {
          "recordType": "creditCardCharge",
          "subledgerRecord": {
            "id": "478",
            "key": "478",
            "href": "/objects/accounts-payable/subledger-record/478"
          },
          "journalEntryLine": {
            "id": "10",
            "key": "10",
            "href": "/objects/general-ledger/journal-entry-line/10"
          },
          "initialOpenItem": {
            "id": "2",
            "key": "2",
            "href": "/objects/cash-management/initial-open-item/2"
          },
          "txnType": "withdrawal",
          "documentNumber": "DOC100",
          "documentDate": "2024-05-26",
          "txnAmount": "86.00",
          "baseAmount": "86.00",
          "txnCurrency": "USD",
          "baseCurrency": "USD",
          "postingDate": "2024-05-26",
          "reconciliationInformation": {
            "lastReconcileDate": "2024-08-07",
            "state": "cleared"
          },
          "payee": "Business Software Inc.",
          "description": "Payment for design software.",
          "postingState": "approved"
        },
        "audit": {
          "createdDateTime": "2024-10-31T00:00:00Z",
          "modifiedDateTime": "2025-05-28T00:00:00Z",
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
        "href": "/objects/cash-management/credit-card-reconciliation-record/1755"
      },
      {
        "id": "1756",
        "key": "1756",
        "creditCardReconciliation": {
          "id": "120",
          "key": "120",
          "href": "/objects/cash-management/credit-card-reconciliation/120"
        },
        "creditCardAccount": {
          "id": "A0000077",
          "key": "132",
          "href": "/objects/cash-management/credit-card-account/132"
        },
        "txnInformation": {
          "recordType": "chargePayoffPayment",
          "subledgerRecord": {
            "id": "481",
            "key": "481",
            "href": "/objects/accounts-payable/subledger-record/481"
          },
          "journalEntryLine": {
            "id": "11",
            "key": "11",
            "href": "/objects/general-ledger/journal-entry-line/11"
          },
          "initialOpenItem": {
            "id": "3",
            "key": "3",
            "href": "/objects/cash-management/initial-open-item/3"
          },
          "txnType": "withdrawal",
          "documentNumber": "DOC-10579",
          "documentDate": "2024-06-04",
          "txnAmount": "45.00",
          "baseAmount": "45.00",
          "txnCurrency": "USD",
          "baseCurrency": "USD",
          "postingDate": "2024-06-04",
          "reconciliationInformation": {
            "lastReconcileDate": "2024-08-07",
            "state": "cleared"
          },
          "payee": "Office Solutions Ltd",
          "description": "A0000001 liability transferred to AP",
          "postingState": "approved"
        },
        "audit": {
          "createdDateTime": "2024-10-31T00:00:00Z",
          "modifiedDateTime": "2025-05-28T00:00:00Z",
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
        "href": "/objects/cash-management/credit-card-reconciliation-record/1756"
      },
      {
        "id": "1757",
        "key": "1757",
        "creditCardReconciliation": {
          "id": "120",
          "key": "120",
          "href": "/objects/cash-management/credit-card-reconciliation/120"
        },
        "creditCardAccount": {
          "id": "A0000077",
          "key": "132",
          "href": "/objects/cash-management/credit-card-account/132"
        },
        "txnInformation": {
          "recordType": "creditCardCharge",
          "subledgerRecord": {
            "id": "484",
            "key": "484",
            "href": "/objects/accounts-payable/subledger-record/484"
          },
          "journalEntryLine": {
            "id": "15",
            "key": "15",
            "href": "/objects/general-ledger/journal-entry-line/15"
          },
          "initialOpenItem": {
            "id": "4",
            "key": "4",
            "href": "/objects/cash-management/initial-open-item/4"
          },
          "txnType": "withdrawal",
          "documentNumber": "NEW CI - 1055",
          "txnAmount": "100.00",
          "baseAmount": "100.00",
          "txnCurrency": "USD",
          "baseCurrency": "USD",
          "postingDate": "2024-06-05",
          "reconciliationInformation": {
            "lastReconcileDate": "2024-08-07",
            "state": "cleared"
          },
          "payee": "Operational Consultancy Inc",
          "description": "Payment for operational support staff",
          "postingState": "approved"
        },
        "audit": {
          "createdDateTime": "2024-10-31T00:00:00Z",
          "modifiedDateTime": "2025-05-28T00:00:00Z",
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
        "href": "/objects/cash-management/credit-card-reconciliation-record/1757"
      }
    ],
    "href": "/objects/cash-management/credit-card-reconciliation/120"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/credit-card-reconciliation/{key}
_Delete a credit reconciliation_


## GET /objects/cash-management/credit-card-txn
_List credit card transactions_

**Response 200 — List credit card transactions:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "2",
      "href": "/objects/cash-management/credit-card-txn/2"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/cash-management/credit-card-txn/4"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/cash-management/credit-card-txn/5"
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

## POST /objects/cash-management/credit-card-txn
_Create a credit card transaction_

**Request example — Create a credit card transaction:**
```json
{
  "txnDate": "2025-04-11",
  "creditCardAccount": {
    "id": "A0000001"
  },
  "referenceNumber": "CCTxn-001",
  "payee": "Vendor-AAA",
  "description": "Travel expenses",
  "isInclusiveTax": true,
  "currency": {
    "baseCurrency": "USD",
    "txnCurrency": "CAD",
    "exchangeRate": {
      "date": "2023-12-04",
      "typeId": "Intacct Daily Rate",
      "rate": 0.7306
    }
  },
  "taxSolution": {
    "key": "5",
    "id": "Canadian Sales Tax - SYS"
  },
  "attachment": {
    "id": "111",
    "key": "2"
  },
  "lines": [
    {
      "glAccount": {
        "key": "326"
      },
      "totalTxnAmount": "500.00",
      "dimensions": {
        "department": {
          "id": "PS"
        },
        "location": {
          "id": "7"
        },
        "project": {
          "id": "QSF - BTI"
        },
        "customer": {
          "id": "BTI"
        },
        "vendor": {
          "id": "210"
        },
        "employee": {
          "id": "12"
        },
        "item": {
          "id": "DELL"
        },
        "class": {
          "id": "WSD"
        }
      },
      "description": "Travel expenses - BTI",
      "taxEntries": [
        {
          "purchasingTaxDetail": {
            "key": "65"
          }
        }
      ],
      "isBillable": false,
      "isBilled": false
    }
  ]
}
```
**Response 201 — Reference to new credit card transaction:**
```json
{
  "ia::result": {
    "id": "12",
    "key": "12",
    "href": "/objects/cash-management/credit-card-txn/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-txn-line
_List credit card transaction lines_

**Response 200 — List credit card transaction lines:**
```json
{
  "ia::result": [
    {
      "key": "13",
      "id": "13",
      "href": "/objects/cash-management/credit-card-txn-line/13"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/cash-management/credit-card-txn-line/5"
    },
    {
      "key": "15",
      "id": "15",
      "href": "/objects/cash-management/credit-card-txn-line/15"
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

## GET /objects/cash-management/credit-card-txn-line-template
_List credit card transaction line templates_

**Response 200 — List credit card transaction line templates:**
```json
{
  "ia::result": [
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/credit-card-txn-line-template/3"
    },
    {
      "key": "6",
      "id": "6",
      "href": "/objects/cash-management/credit-card-txn-line-template/6"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/cash-management/credit-card-txn-line-template/2"
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

## GET /objects/cash-management/credit-card-txn-line-template/{key}
_Get a credit card transaction line template_

**Response 200 — Get a credit card transaction line template:**
```json
{
  "ia::result": {
    "key": "98",
    "id": "98",
    "creditCardTxnTemplate": {
      "key": "117",
      "href": "/objects/cash-management/credit-card-txn-template/117"
    },
    "memo": "Credit card transaction template 98",
    "glAccount": {
      "key": "339",
      "id": "7505.06",
      "name": "CC Other Charges & Fees",
      "href": "/objects/general-ledger/account/339"
    },
    "dimensions": {
      "location": {
        "id": "7",
        "name": "Canada"
      },
      "project": {
        "key": "11",
        "id": "CON",
        "name": "Contract - QuickMedia M C Services",
        "href": "/objects/projects/project/11"
      },
      "customer": {
        "key": "5",
        "id": "MR1",
        "name": "QuickMedia M C Services",
        "href": "/objects/accounts-receivable/customer/5"
      },
      "vendor": {
        "key": "50",
        "id": "204",
        "name": "Bridge Water Garden Supply",
        "href": "/objects/accounts-payable/vendor/50"
      },
      "employee": {
        "key": "29",
        "id": "234",
        "name": "Judith Reeves",
        "href": "/objects/company-config/employee/29"
      },
      "item": {
        "key": "1",
        "id": "1",
        "name": "PC Computer",
        "href": "/objects/inventory-control/item/1"
      },
      "class": {
        "key": "9",
        "id": "REAL_EST_009",
        "name": "Real Estate",
        "href": "/objects/company-config/class/9"
      }
    },
    "lineNumber": 1,
    "accountLabel": {
      "id": "CC Other Fees"
    },
    "exchangeRate": {
      "date": null,
      "typeId": null,
      "rate": null
    },
    "isBillable": null,
    "audit": {
      "createdDateTime": "2025-03-27T15:40:34Z",
      "modifiedDateTime": "2025-03-27T15:40:34Z",
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
    "href": "/objects/cash-management/credit-card-txn-line-template/98"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-txn-line/{key}
_Get a credit card transaction line_

**Response 200 — Get a credit card transaction line:**
```json
{
  "ia::result": {
    "id": "5299",
    "key": "5299",
    "creditCardTxn": {
      "id": "1482",
      "key": "1482",
      "href": "/objects/cash-management/credit-card-txn/1482"
    },
    "glAccount": {
      "key": "259",
      "id": "6254.04",
      "name": "Travel",
      "href": "/objects/general-ledger/account/259"
    },
    "accountLabel": {
      "key": "15",
      "id": "Travel Expenses"
    },
    "amount": "741.00",
    "txnAmount": "1000.00",
    "dimensions": {
      "department": {
        "key": "28",
        "id": "PS",
        "name": "Professional Services",
        "href": "/objects/company-config/department/28"
      },
      "location": {
        "key": "7",
        "id": "7",
        "name": "Canada",
        "href": "/objects/company-config/location/7"
      },
      "project": {
        "key": "35",
        "id": "QSF - BTI",
        "name": "Quick Start Financial's - Berkeley Technology Inc",
        "href": "/objects/projects/project/35"
      },
      "customer": {
        "key": "14",
        "id": "BTI",
        "name": "Berkeley Technology Inc",
        "href": "/objects/accounts-receivable/customer/14"
      },
      "vendor": {
        "key": "56",
        "id": "210",
        "name": "Office Supply and Copier Co.",
        "href": "/objects/accounts-payable/vendor/56"
      },
      "employee": {
        "key": "27",
        "id": "12",
        "name": "John Smith",
        "href": "/objects/company-config/employee/27"
      },
      "item": {
        "key": "117",
        "id": "DELL",
        "name": "DELL Laptops",
        "href": "/objects/inventory-control/item/117"
      },
      "class": {
        "key": "3",
        "id": "WSD",
        "name": "Whole Sales Distribution",
        "href": "/objects/company-config/class/3"
      }
    },
    "baseLocation": {
      "name": "Canada",
      "key": "7",
      "href": "/objects/company-config/location/7"
    },
    "description": "Travel expenses - John Smith",
    "currency": {
      "exchangeRate": {
        "date": "2025-04-11",
        "rate": 0.741
      },
      "txnCurrency": "CAD",
      "baseCurrency": "USD"
    },
    "lineNumber": 1,
    "totalPaid": "0.00",
    "txnTotalPaid": "0.00",
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "taxDetail": {
      "key": null,
      "taxRate": null,
      "id": null
    },
    "isBillable": false,
    "isBilled": false,
    "taxEntries": [],
    "href": "/objects/cash-management/credit-card-txn-line/5299"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-txn-tax-entry
_List credit card transaction tax entries_

**Response 200 — List credit card transaction tax entries:**
```json
{
  "ia::result": [
    {
      "key": "792",
      "id": "792",
      "href": "/objects/cash-management/credit-card-txn-tax-entry/792"
    },
    {
      "key": "797",
      "id": "797",
      "href": "/objects/cash-management/credit-card-txn-tax-entry/797"
    },
    {
      "key": "831",
      "id": "831",
      "href": "/objects/cash-management/credit-card-txn-tax-entry/831"
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

## GET /objects/cash-management/credit-card-txn-tax-entry/{key}
_Get a credit card transaction tax entry_

**Response 200 — Get a credit card transaction tax entry:**
```json
{
  "ia::result": {
    "key": "300",
    "id": "300",
    "baseTaxAmount": "100",
    "txnTaxAmount": "100",
    "description": "Standard Rate for UK Import Services",
    "taxRate": 5.5,
    "purchasingTaxDetail": {
      "id": "UK Export Reduced Rate",
      "key": "24",
      "href": "/objects/tax/purchasing-tax-detail/24"
    },
    "creditCardTxnLine": {
      "id": "148",
      "key": "148",
      "href": "/objects/cash-management/credit-card-txn-line/148"
    },
    "href": "/objects/cash-management/tax/credit-card-txn-tax-entry/300"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/credit-card-txn-template
_List credit card transaction templates_

**Response 200 — List credit card transaction templates:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "CC-TXN-002 Travel",
      "href": "/objects/cash-management/credit-card-txn-template/2"
    },
    {
      "key": "3",
      "id": "CC-TXN-003 Accommodation",
      "href": "/objects/cash-management/credit-card-txn-template/3"
    },
    {
      "key": "4",
      "id": "CC-TXN-004 Meals",
      "href": "/objects/cash-management/credit-card-txn-template/4"
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

## POST /objects/cash-management/credit-card-txn-template
_Create a credit card transaction template_

**Request example — Create a credit card transaction template:**
```json
{
  "id": "CC-TXN-005 Software NA",
  "name": "Software NA - CC TXNs",
  "description": "Template for North American software credit card transactions.",
  "lines": [
    {
      "lineNumber": 1,
      "isBillable": true,
      "glAccount": {
        "key": "326"
      },
      "dimensions": {
        "location": {
          "id": "North America"
        }
      }
    }
  ]
}
```
**Request example — Create a credit card transaction template with tax:**
```json
{
  "id": "CC-TXN-010 Inbound AUS-GST",
  "name": "Inbound Australia GST - CC TXNs",
  "description": "Template for Australian GST credit card transactions.",
  "taxImplication": "inbound",
  "taxSolution": {
    "id": "Australia - GST"
  },
  "taxSchedule": {
    "id": "77"
  },
  "lines": [
    {
      "lineNumber": 1,
      "isBillable": false,
      "glAccount": {
        "key": "327"
      },
      "dimensions": {
        "location": {
          "id": "33"
        }
      }
    }
  ]
}
```
**Response 201 — Reference to new credit card  transaction template:**
```json
{
  "ia::result": {
    "key": "78",
    "id": "CC-TXN-078",
    "href": "/objects/cash-management/credit-card-txn-template/78"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 201 — Reference to new credit card transaction template with tax:**
```json
{
  "ia::result": {
    "key": "79",
    "id": "CC-TXN-079 Inbound TAX AUS",
    "href": "/objects/cash-management/credit-card-txn-template/79"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/credit-card-txn-template/{key}
_Get a credit card transaction template_

**Response 200 — Get a credit card transaction template:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "CC-TXN-VAT-003",
    "name": "VAT Payment - CC TXNs",
    "description": "Template for VAT payments using a credit card.",
    "payee": "Revenue Service",
    "numberOfRulesUsingTemplate": 0,
    "status": "active",
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "taxImplication": "inbound",
    "taxSolution": {
      "key": "1",
      "id": "Australia - GST",
      "href": "/objects/tax/tax-solution/1"
    },
    "taxSchedule": {
      "name": "G11 Other Acquisition",
      "key": "10",
      "id": "10",
      "href": "/objects/tax/purchasing-tax-schedule/10"
    },
    "isInclusiveTax": true,
    "lines": [
      {
        "key": "3",
        "id": "3",
        "creditCardTxnTemplate": {
          "key": "3",
          "href": "/objects/cash-management/credit-card-txn-template/3"
        },
        "memo": "VAT payment for Q1 2025",
        "glAccount": {
          "key": "249",
          "id": "6003",
          "name": "Input VAT",
          "href": "/objects/general-ledger/account/249"
        },
        "dimensions": {
          "location": {
            "id": null,
            "name": null
          },
          "project": {
            "key": null,
            "id": null,
            "name": null
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
          "class": {
            "key": null,
            "id": null,
            "name": null
          }
        },
        "lineNumber": 0,
        "accountLabel": {
          "id": null
        },
        "exchangeRate": {
          "date": null,
          "typeId": null,
          "rate": null
        },
        "isBillable": null,
        "audit": {
          "createdDateTime": "2025-04-11T12:56:46Z",
          "modifiedDateTime": "2025-04-11T12:56:46Z",
          "createdByUser": {
            "key": "159",
            "href": "/objects/company-config/user/159"
          },
          "createdBy": "159",
          "modifiedByUser": {
            "key": "159",
            "href": "/objects/company-config/user/159"
          }
        },
        "href": "/objects/cash-management/credit-card-txn-line-template/3"
      }
    ],
    "href": "/objects/cash-management/credit-card-txn-template/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/credit-card-txn-template/{key}
_Update a credit card transaction template_

**Request example — Update a credit card transaction template:**
```json
{
  "key": "189",
  "lines": [
    {
      "key": "160",
      "lineNumber": 1,
      "isBillable": false
    }
  ]
}
```
**Response 200 — Reference to updated credit card transaction template:**
```json
{
  "ia::result": {
    "key": "189",
    "id": "CC-TXN-189",
    "href": "/objects/cash-management/credit-card-txn-template/189"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/credit-card-txn-template/{key}
_Delete a credit card transaction template_


## GET /objects/cash-management/credit-card-txn/{key}
_Get a credit card transaction_

**Response 200 — Get a credit card transaction:**
```json
{
  "ia::result": {
    "id": "27",
    "key": "27",
    "creditCardAccount": {
      "id": "A0000001",
      "key": "1",
      "href": "/objects/cash-management/credit-card-account/1"
    },
    "txnDate": "2025-04-11",
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "referenceNumber": "CCTxn-001",
    "payee": "Vendor-AAA",
    "description": "Travel expenses in december",
    "currency": {
      "baseCurrency": "USD",
      "txnCurrency": "CAD",
      "exchangeRate": {
        "date": "2025-04-11",
        "typeId": "Intacct Daily Rate",
        "rate": 0.7306
      }
    },
    "totalEntered": "365.30",
    "txnTotalEntered": "500.00",
    "totalPaid": "0.00",
    "txnTotalPaid": "0.00",
    "totalSelected": "0.00",
    "txnTotalSelected": "0.00",
    "totalDue": "365.30",
    "txnTotalDue": "500.00",
    "whenPaid": null,
    "reversedBy": {
      "id": null,
      "key": null,
      "reversalDate": null
    },
    "reversalOf": {
      "id": null,
      "key": null,
      "txnDate": null
    },
    "state": "posted",
    "reconciliationState": "cleared",
    "clearingDate": "2024-01-23",
    "isInclusiveTax": true,
    "taxSolution": {
      "key": "5",
      "id": "Canadian Sales Tax - SYS",
      "href": "/objects/tax/tax-solution/5"
    },
    "transactionSource": null,
    "attachment": {
      "id": "111",
      "key": "20",
      "href": "/objects/company-config/attachment/20"
    },
    "lines": [
      {
        "id": "92",
        "key": "92",
        "creditCardTxn": {
          "id": "27",
          "key": "27",
          "href": "/objects/cash-management/credit-card-txn/27"
        },
        "glAccount": {
          "key": "326",
          "id": "6700.04",
          "name": "CC Other Charges & Fees",
          "href": "/objects/general-ledger/account/326"
        },
        "accountLabel": {
          "key": null,
          "id": null
        },
        "amount": "320.44",
        "txnAmount": "438.60",
        "dimensions": {
          "department": {
            "key": "28",
            "id": "PS",
            "name": "Professional Services",
            "href": "/objects/company-config/department/28"
          },
          "location": {
            "key": "7",
            "id": "7",
            "name": "Canada",
            "href": "/objects/company-config/location/7"
          },
          "project": {
            "key": "35",
            "id": "QSF - BTI",
            "name": "Quick Start Financial - Berkeley Technology Inc",
            "href": "/objects/projects/project/35"
          },
          "customer": {
            "key": "14",
            "id": "BTI",
            "name": "Berkeley Technology Inc",
            "href": "/objects/accounts-receivable/customer/14"
          },
          "vendor": {
            "key": "56",
            "id": "210",
            "name": "Office Supply and Copier Co.",
            "href": "/objects/accounts-payable/vendor/56"
          },
          "employee": {
            "key": "27",
            "id": "12",
            "name": "John Smith",
            "href": "/objects/company-config/employee/27"
          },
          "item": {
            "key": "117",
            "id": "DELL",
            "name": "DELL Laptops",
            "href": "/objects/inventory-control/item/117"
          },
          "class": {
            "key": "3",
            "id": "WSD",
            "name": "Whole Sales Distribution",
            "href": "/objects/company-config/class/3"
          }
        },
        "baseLocation": {
          "name": "Calgary",
          "key": "30",
          "href": "/objects/company-config/location/30"
        },
        "description": "Travel expenses - Smith",
        "currency": {
          "exchangeRate": {
            "date": "2025-04-11",
            "rate": 0.7306
          },
          "txnCurrency": "CAD",
          "baseCurrency": "USD"
        },
        "lineNumber": 1,
        "totalPaid": "0.00",
        "txnTotalPaid": "0.00",
        "audit": {
          "createdDateTime": "2025-04-11T12:56:46Z",
          "modifiedDateTime": "2025-04-11T12:56:46Z",
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
        "isBillable": false,
        "isBilled": false,
        "totalTxnAmount": "500.00",
        "taxEntries": [
          {
            "txnTaxAmount": "30.70",
            "baseTaxAmount": "22.43",
            "purchasingTaxDetail": {
              "id": "BC PST Standard Rate Services Purchase - CA",
              "key": "67",
              "href": "/objects/tax/purchasing-tax-detail/67"
            },
            "id": "94",
            "key": "94",
            "taxRate": 7,
            "creditCardTxnLine": {
              "id": "92",
              "key": "92",
              "href": "/objects/cash-management/credit-card-txn-line/92"
            },
            "href": "/objects/cash-management/credit-card-txn-tax-entry/94"
          },
          {
            "txnTaxAmount": "30.70",
            "baseTaxAmount": "22.43",
            "purchasingTaxDetail": {
              "id": "BC PST Standard Rate Goods Purchase - CA",
              "key": "65",
              "href": "/objects/tax/purchasing-tax-detail/65"
            },
            "id": "96",
            "key": "96",
            "taxRate": 7,
            "creditCardTxnLine": {
              "id": "92",
              "key": "92",
              "href": "/objects/cash-management/credit-card-txn-line/92"
            },
            "href": "/objects/cash-management/credit-card-txn-tax-entry/96"
          }
        ],
        "href": "/objects/cash-management/credit-card-txn-line/92"
      }
    ],
    "href": "/objects/cash-management/credit-card-txn/27"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/credit-card-txn/{key}
_Update a credit card transaction_

**Request example — Update a credit card transaction:**
```json
{
  "description": "Travel expenses in December",
  "attachment": {
    "id": "travel-receipt"
  },
  "isInclusiveTax": true,
  "lines": [
    {
      "key": "92",
      "creditCardTxn": {
        "key": "27"
      },
      "description": "Travel expenses - John Smith",
      "totalTxnAmount": "500.00",
      "taxEntries": [
        {
          "purchasingTaxDetail": {
            "key": "67"
          }
        },
        {
          "purchasingTaxDetail": {
            "key": "65"
          }
        }
      ]
    }
  ]
}
```
**Response 200 — Reference to updated credit card transaction:**
```json
{
  "ia::result": {
    "id": "12",
    "key": "12",
    "href": "/objects/cash-management/credit-card-txn/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/credit-card-txn/{key}
_Delete a credit card transaction_


## GET /objects/cash-management/deposit
_List deposits_

**Response 200 — List deposits:**
```json
{
  "ia::result": [
    {
      "key": "1718",
      "id": "1718",
      "href": "/objects/cash-management/deposit/1718"
    },
    {
      "key": "1717",
      "id": "1717",
      "href": "/objects/cash-management/deposit/1717"
    },
    {
      "key": "3228",
      "id": "3228",
      "href": "/objects/cash-management/deposit/3228"
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

## POST /objects/cash-management/deposit
_Create a deposit_

**Request example — Create a deposit:**
```json
{
  "txnDate": "2025-01-22",
  "description": "Monday Deposit 0314-001",
  "depositId": "Deposit slip 01/22/2025",
  "bankAccount": {
    "id": "BOA"
  },
  "attachment": {
    "id": "18"
  },
  "details": [
    {
      "id": "123"
    }
  ]
}
```
**Response 201 — Reference to new deposit:**
```json
{
  "ia::result": {
    "key": "500",
    "id": "500",
    "href": "/objects/cash-management/deposit/500"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/deposit-detail
_List deposit details_

**Response 200 — List deposit details:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/deposit-detail/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/deposit-detail/3"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/cash-management/deposit-detail/5"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/cash-management/deposit-detail/{key}
_Get a deposit detail_

**Response 200 — Get deposit details:**
```json
{
  "ia::result": {
    "id": "587",
    "key": "587",
    "deposit": {
      "id": "291",
      "key": "291",
      "depositType": "cd",
      "href": "/objects/cash-management/deposit/291"
    },
    "glAccount": {
      "id": "33",
      "key": "33",
      "accountNumber": "1070",
      "name": "Undeposited Funds",
      "href": "/objects/general-ledger/account/33"
    },
    "arAccountLabel": {
      "label": null,
      "id": null,
      "key": null
    },
    "amount": "1002.00",
    "txnAmount": "1002.00",
    "department": {
      "key": null,
      "id": null,
      "name": null
    },
    "location": {
      "key": "1",
      "name": "United States of America",
      "href": "/objects/company-config/location/1"
    },
    "baseLocation": {
      "name": "United States of America",
      "key": "1"
    },
    "description": "Deposited from undeposited fund from GPay invoice",
    "exchangeRate": {
      "date": "2025-01-23",
      "typeId": "-1",
      "rate": 1
    },
    "currency": "USD",
    "baseCurrency": "USD",
    "status": "active",
    "state": "deposited",
    "audit": {
      "createdDateTime": "2025-04-16T00:57:25Z",
      "modifiedDateTime": "2025-04-16T00:57:43Z",
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
    "href": "/objects/cash-management/deposit-detail/587"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/deposit-line
_List deposit lines_

**Response 200 — List deposit lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/deposit-line/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/deposit-line/3"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/cash-management/deposit-line/5"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/cash-management/deposit-line/{key}
_Get a deposit line_

**Response 200 — Get a deposit line:**
```json
{
  "ia::result": {
    "id": "1253",
    "key": "1253",
    "deposit": {
      "id": "628",
      "key": "628",
      "depositType": "cd",
      "href": "/objects/cash-management/deposit/628"
    },
    "glAccount": {
      "id": "33",
      "key": "33",
      "accountNumber": "1070",
      "name": "Undeposited Funds",
      "href": "/objects/general-ledger/account/33"
    },
    "arAccountLabel": {
      "label": null,
      "id": null,
      "key": null
    },
    "amount": "12.50",
    "txnAmount": "12.50",
    "dimensions": {
      "department": {
        "key": null,
        "id": null,
        "name": null
      },
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
      }
    },
    "baseLocation": {
      "name": "United States of America",
      "key": "1"
    },
    "description": "Deposit from other receipt for Vivian grapes inc",
    "currency": {
      "exchangeRate": {
        "date": "2025-04-25",
        "typeId": "-1",
        "rate": "1.0"
      },
      "baseCurrency": "USD",
      "txnCurrency": "USD"
    },
    "status": "active",
    "audit": {
      "createdDateTime": "2025-11-15T20:55:20Z",
      "modifiedDateTime": "2025-11-15T20:55:25Z",
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
    "href": "/objects/cash-management/deposit-line/1253"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/deposit/{key}
_Get a deposit_

**Response 200 — Get a deposit:**
```json
{
  "ia::result": {
    "id": "628",
    "key": "628",
    "bankAccount": {
      "id": "BOA",
      "name": "Bank of America"
    },
    "txnDate": "2025-11-15",
    "depositId": "Deposit Slip 2025-11-15",
    "description": "Deposit for pay-go online services",
    "baseCurrency": "USD",
    "txnCurrency": "USD",
    "totalEntered": "120.50",
    "txnTotalEntered": "120.50",
    "voidPaymentKey": "1236",
    "reversalDate": "2025-09-23",
    "reversedVoidPaymentKey": "1234",
    "reversedDate": "2025-09-23",
    "state": "void",
    "reconciliationState": "uncleared",
    "audit": {
      "createdDateTime": "2025-11-15T20:55:20Z",
      "modifiedDateTime": "2025-11-15T20:55:25Z",
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
    "attachment": {
      "key": "18",
      "id": "Attach-01",
      "href": "/objects/company-config/attachment/18"
    },
    "lines": [
      {
        "id": "1253",
        "key": "1253",
        "deposit": {
          "id": "628",
          "key": "628",
          "depositType": "cd",
          "href": "/objects/cash-management/deposit/628"
        },
        "glAccount": {
          "id": "33",
          "key": "33",
          "accountNumber": "1070",
          "name": "Undeposited Funds",
          "href": "/objects/general-ledger/account/33"
        },
        "arAccountLabel": {
          "label": "ACCOUNTING",
          "id": "10",
          "key": "10"
        },
        "amount": "120.50",
        "txnAmount": "120.50",
        "dimensions": {
          "department": {
            "key": "9",
            "id": "DEPT-0135-09",
            "name": "Accounting",
            "href": "/objects/company-config/department/9"
          },
          "location": {
            "key": "1",
            "name": "United States of America",
            "href": "/objects/company-config/location/1"
          }
        },
        "baseLocation": {
          "key": "1",
          "name": "United States of America",
          "href": "/objects/company-config/location/1"
        },
        "description": "Deposit from other receipt 101",
        "currency": {
          "exchangeRate": {
            "date": "2025-01-23",
            "typeId": "-1",
            "rate": 1
          },
          "txnCurrency": "USD",
          "baseCurrency": "USD"
        },
        "status": "active",
        "audit": {
          "createdDateTime": "2025-11-15T20:55:20Z",
          "modifiedDateTime": "2025-11-15T20:55:25Z",
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
        "href": "/objects/cash-management/deposit-line/1253"
      }
    ],
    "details": [
      {
        "id": "624",
        "key": "624",
        "undepositedFund": {
          "key": "624",
          "id": "624",
          "href": "/objects/cash-management/undeposited-fund/624"
        },
        "depositedFund": {
          "key": "624",
          "id": "624",
          "href": "/objects/cash-management/deposited-fund/624"
        },
        "summary": "Cash Management Transactions: 2025/12/20 Batch",
        "customerID": "PH-00215735",
        "customerName": "Peter Hansen",
        "payee": "Toulouse - 03",
        "totalEntered": "120.50",
        "txnTotalEntered": "120.50",
        "currency": "USD",
        "paymentMethod": "cash",
        "documentNumber": "Check 0019",
        "deposit": {
          "id": "628",
          "key": "628",
          "href": "/objects/cash-management/deposit/628"
        },
        "href": "/objects/cash-management/deposit-detail/624"
      }
    ],
    "href": "/objects/cash-management/deposit/628"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/financial-institution
_List financial institutions_

**Response 200 — List financial institutions:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "FinInst1",
      "href": "/objects/cash-management/financial-institution/1"
    },
    {
      "key": "2",
      "id": "FinInst2",
      "href": "/objects/cash-management/financial-institution/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/cash-management/financial-institution
_Create a financial institution_

**Request example — Create a financial institution:**
```json
{
  "financialInstitutionId": "FinInst-BOA",
  "name": "FinOn4ss5e",
  "addOnServices": [
    {
      "name": "MAL",
      "serviceContract": {
        "key": "129",
        "accountType": "checking"
      }
    }
  ],
  "checkingAccounts": [
    {
      "key": "72",
      "externalBankAccount": {
        "id": "a421d6c8-ed48-454d-a60e-7b697c67b956",
        "name": "Plaid Saving"
      },
      "requestedStartDate": "2021-01-23"
    },
    {
      "key": "69",
      "externalBankAccount": {
        "id": "412f0837-c236-4917-9796-84ec52cd3edb",
        "name": "Plaid CD"
      },
      "requestedStartDate": "2021-01-23"
    }
  ],
  "savingsAccounts": [
    {
      "key": "33",
      "externalBankAccount": {
        "id": "d6c05270-66f0-4d1b-8c1e-d35b4914e991",
        "name": "Plaid IRA"
      },
      "requestedStartDate": "2021-01-23"
    },
    {
      "key": "30",
      "externalBankAccount": {
        "id": "11dd5715-2585-43e5-8a6c-501923ca72ec",
        "name": "Plaid 401k"
      },
      "requestedStartDate": "2021-01-23"
    }
  ],
  "creditCards": [
    {
      "key": "60",
      "externalBankAccount": {
        "id": "be157d12-d181-4409-958f-1d8fb95b504f",
        "name": "Plaid Credit Card"
      },
      "requestedStartDate": "2021-01-23"
    },
    {
      "key": "7",
      "externalBankAccount": {
        "id": "41650f07-0f3f-432d-9d57-e56a6286bdf0",
        "name": "Plaid Money Market"
      },
      "requestedStartDate": "2021-01-23"
    }
  ]
}
```
**Response 201 — Reference to new financial institution:**
```json
{
  "ia::result": {
    "key": "103",
    "id": "103",
    "href": "/objects/cash-management/financial-institution/103"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/financial-institution/{key}
_Get a financial institution_

**Response 200 — Get a financial institution:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "financialInstitutionId": "FinInst1",
    "name": "FinOn4ddss5e",
    "totalAccounts": 7,
    "checkingAccounts": [
      {
        "key": "129",
        "href": "/objects/cash-management/checking-account/129"
      },
      {
        "key": "72",
        "href": "/objects/cash-management/checking-account/72"
      },
      {
        "key": "69",
        "href": "/objects/cash-management/checking-account/69"
      }
    ],
    "savingsAccounts": [
      {
        "key": "33",
        "href": "/objects/cash-management/savings-account/33"
      },
      {
        "key": "30",
        "href": "/objects/cash-management/savings-account/30"
      }
    ],
    "creditCards": [
      {
        "key": "7",
        "href": "/objects/cash-management/credit-card-account/7"
      },
      {
        "key": "60",
        "href": "/objects/cash-management/credit-card-account/60"
      }
    ],
    "addOnServices": [
      {
        "name": "MAL",
        "serviceContract": {
          "key": "129",
          "accountType": "checking"
        }
      }
    ],
    "href": "/objects/cash-management/financial-institution/96"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/cash-management/financial-institution/{key}
_Update a financial institution_

**Request example — Update a financial institution:**
```json
{
  "financialInstitutionId": "FinInst-BOA",
  "checkingAccounts": [
    {
      "key": "99",
      "externalBankAccount": {
        "id": "a532e7d9-ed59-565d-a71e-8b718c7c167",
        "name": "Corp Saving"
      },
      "requestedStartDate": "2021-01-23"
    }
  ]
}
```
**Response 200 — Reference to updated financial institution:**
```json
{
  "ia::result": {
    "key": "96",
    "id": "96",
    "href": "/objects/cash-management/financial-institution/96"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/cash-management/financial-institution/{key}
_Delete a financial institution_


## GET /objects/cash-management/funds-transfer
_List funds transfers_

**Response 200 — List funds transfers:**
```json
{
  "ia::result": [
    {
      "key": "30",
      "id": "30",
      "href": "/objects/cash-management/funds-transfer/30"
    },
    {
      "key": "31",
      "id": "31",
      "href": "/objects/cash-management/funds-transfer/31"
    },
    {
      "key": "32",
      "id": "32",
      "href": "/objects/cash-management/funds-transfer/32"
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

## POST /objects/cash-management/funds-transfer
_Create a funds transfer_

**Request example — Create a funds transfer:**
```json
{
  "sendDate": "2025-02-14",
  "transferFromAccount": {
    "bankAccount": {
      "id": "CHSE"
    },
    "transferAmount": "1000.50"
  },
  "transferToAccount": {
    "bankAccount": {
      "id": "BOA"
    },
    "receivedAmount": "1000.50"
  },
  "description": "Transfer to BOA from Chase",
  "referenceNumber": "Transfer 001"
}
```
**Response 201 — Reference to new funds transfer:**
```json
{
  "ia::result": {
    "id": "39",
    "key": "39",
    "href": "/objects/cash-management/funds-transfer/39"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/funds-transfer-line
_List funds transfer lines_

**Response 200 — List funds transfer lines:**
```json
{
  "ia::result": [
    {
      "key": "13",
      "id": "13",
      "href": "/objects/cash-management/funds-transfer-line/13"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/cash-management/funds-transfer-line/5"
    },
    {
      "key": "15",
      "id": "15",
      "href": "/objects/cash-management/funds-transfer-line/15"
    },
    {
      "key": "7",
      "id": "7",
      "href": "/objects/cash-management/funds-transfer-line/7"
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

## GET /objects/cash-management/funds-transfer-line/{key}
_Get a funds transfer line_

**Response 200 — Get a funds transfer line:**
```json
{
  "ia::result": {
    "id": "87",
    "key": "87",
    "fundsTransfer": {
      "id": "40",
      "key": "40",
      "href": "/objects/cash-management/funds-transfer/40"
    },
    "glAccount": {
      "key": "14",
      "id": "1005",
      "name": "Bank of Montreal",
      "href": "/objects/general-ledger/account/14"
    },
    "baseAmount": "2560.60",
    "txnAmount": "3457.00",
    "dimensions": {
      "department": {
        "key": "6",
        "id": "6",
        "name": "Marketing",
        "href": "/objects/company-config/department/6"
      },
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
      },
      "customer": {
        "key": "2",
        "id": "2",
        "name": "Logic Solutions",
        "href": "/objects/accounts-receivable/customer/2"
      },
      "vendor": {
        "key": "62",
        "id": "A201",
        "name": "D Link Technologies",
        "href": "/objects/accounts-payable/vendor/62"
      },
      "employee": {
        "key": null,
        "id": null,
        "name": null
      },
      "item": {
        "key": "55",
        "id": "F002",
        "name": "Accessories-Dell",
        "href": "/objects/inventory-control/item/55"
      },
      "contract": {
        "key": null,
        "id": null,
        "name": null
      },
      "project": {
        "key": "9",
        "id": "9",
        "name": "Implementation - Logic Solutions",
        "href": "/objects/projects/project/9"
      },
      "class": {
        "key": null,
        "id": null,
        "name": null
      }
    },
    "currency": {
      "exchangeRateDate": "2025-02-14",
      "exchangeRateTypeId": "-1",
      "exchangeRate": 0.7407,
      "txnCurrency": "CAD",
      "baseCurrency": "USD"
    },
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
    "href": "/objects/cash-management/funds-transfer-line/87"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/funds-transfer/{key}
_Get a funds transfer_

**Response 200 — Get a funds transfer:**
```json
{
  "ia::result": {
    "id": "40",
    "key": "40",
    "sendDate": "2025-02-14",
    "transferFromAccount": {
      "bankAccount": {
        "id": "CHSE",
        "name": "Chase",
        "currency": "USD",
        "accountType": "checking",
        "key": "2",
        "href": "/objects/cash-management/bank-account/2"
      },
      "glAccountNumber": "1003",
      "transferAmount": "3457.00"
    },
    "transferToAccount": {
      "bankAccount": {
        "id": "BOM",
        "name": "Bank of Montreal",
        "currency": "CAD",
        "accountType": "checking",
        "key": "57",
        "href": "/objects/cash-management/bank-account/57"
      },
      "glAccountNumber": "1005",
      "receivedAmount": "3457.00"
    },
    "referenceNumber": "CHSE-BOM-0040",
    "description": "Transfer to BOM from Chase",
    "baseCurrencyConversion": {
      "transferToCurrency": {
        "baseCurrencyAmount": "2560.60",
        "companyBaseCurrency": "USD",
        "exchangeRateDate": "2025-02-14",
        "exchangeRateTypeId": "Intacct Daily Rate",
        "exchangeRate": 0.7407
      },
      "transferFromCurrency": {
        "companyBaseCurrency": "USD",
        "exchangeRateTypeId": "Intacct Daily Rate",
        "exchangeRateDate": "2025-02-14",
        "exchangeRate": 1,
        "baseCurrencyAmount": "3457.00"
      }
    },
    "reversedBy": {
      "id": null,
      "key": null,
      "reversalDate": null
    },
    "reversalOf": {
      "id": null,
      "key": null,
      "txnDate": null
    },
    "state": "posted",
    "reconciliationState": "cleared",
    "clearingDate": "2024-01-23",
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
    "attachment": {
      "id": null,
      "key": null
    },
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "lines": [
      {
        "id": "87",
        "key": "87",
        "fundsTransfer": {
          "id": "40",
          "key": "40",
          "href": "/objects/cash-management/funds-transfer/40"
        },
        "glAccount": {
          "key": "14",
          "id": "1005",
          "name": "Bank of Montreal",
          "href": "/objects/general-ledger/account/14"
        },
        "baseAmount": "2560.60",
        "txnAmount": "3457.00",
        "dimensions": {
          "department": {
            "key": "6",
            "id": "6",
            "name": "Marketing",
            "href": "/objects/company-config/department/6"
          },
          "location": {
            "key": "1",
            "id": "1",
            "name": "United States of America",
            "href": "/objects/company-config/location/1"
          },
          "project": {
            "key": "9",
            "id": "9",
            "name": "Implementation - Logic Solutions",
            "href": "/objects/projects/project/9"
          },
          "customer": {
            "key": "2",
            "id": "2",
            "name": "Logic Solutions",
            "href": "/objects/accounts-receivable/customer/2"
          },
          "vendor": {
            "key": "62",
            "id": "A201",
            "name": "D Link Technologies",
            "href": "/objects/accounts-payable/vendor/62"
          },
          "employee": {
            "key": null,
            "id": null,
            "name": null
          },
          "item": {
            "key": "55",
            "id": "F002",
            "name": "Accessories-Dell",
            "href": "/objects/inventory-control/item/55"
          },
          "class": {
            "key": null,
            "id": null,
            "name": null
          }
        },
        "currency": {
          "exchangeRateDate": "2025-02-14",
          "exchangeRateTypeId": "-1",
          "exchangeRate": 0.7407,
          "txnCurrency": "CAD",
          "baseCurrency": "USD"
        },
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
        "href": "/objects/cash-management/funds-transfer-line/87"
      }
    ],
    "href": "/objects/cash-management/funds-transfer/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/initial-open-item
_List initial open items_

**Response 200 — List initial open items:**
```json
{
  "ia::result": [
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/initial-open-item/3"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/cash-management/initial-open-item/4"
    },
    {
      "key": "12",
      "id": "12",
      "href": "/objects/cash-management/initial-open-item/12"
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

## GET /objects/cash-management/initial-open-item/{key}
_Get an initial open item_

**Response 200 — Get an initial open item:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "12",
    "bankAccountId": "SBME-18954320",
    "txnInformation": {
      "documentNumber": "18956",
      "txnType": "payment",
      "baseAmount": "12335.55",
      "payee": "Premier Venue Group",
      "description": "Final payment for conference facilities.",
      "isCleared": true
    },
    "audit": {
      "createdDateTime": "2026-05-28T00:00:00Z",
      "modifiedDateTime": "2026-05-28T00:00:00Z",
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
    "href": "/objects/cash-management/initial-open-item/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/journal-entry-line-template
_List journal entry line templates_

**Response 200 — List journal entry line templates:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/journal-entry-line-template/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/cash-management/journal-entry-line-template/2"
    },
    {
      "key": "7",
      "id": "7",
      "href": "/objects/cash-management/journal-entry-line-template/7"
    }
  ],
  "ia::meta": {
    "totalCount": 6,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/cash-management/journal-entry-line-template/{key}
_Get a journal entry line template_

**Response 200 — Get a journal entry line template:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "8",
    "journalEntryTemplate": {
      "id": "6",
      "key": "6",
      "href": "/objects/cash-management/journal-entry-template/6"
    },
    "dimensions": {
      "location": {
        "key": "3",
        "id": "3",
        "name": "United Kingdom",
        "href": "/objects/company-config/location/3"
      },
      "department": {
        "key": "9",
        "id": "OPS",
        "name": "Operations",
        "href": "/objects/company-config/department/9"
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
      "contract": {
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
    "glAccount": {
      "key": "11",
      "id": "1002",
      "name": "HSBC - GBP",
      "href": "/objects/general-ledger/account/11"
    },
    "documentId": "156",
    "txnType": "debit",
    "memo": "Purchases for UK Office Supplies",
    "allocation": {
      "key": "2",
      "id": "ALLOC_JE_OFFICE_SUPPLIES"
    },
    "numberOfUnits": null,
    "exchangeRate": {
      "date": null,
      "typeId": null,
      "rate": null
    },
    "isBillable": false,
    "href": "/objects/cash-management/journal-entry-line-template/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/journal-entry-template
_List journal entry templates_

**Response 200 — List journal entry templates:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "JET_BANK_IMPORT_001",
      "href": "/objects/cash-management/journal-entry-template/1"
    },
    {
      "key": "3",
      "id": "JET_MONTHLY_ACCRUAL_003",
      "href": "/objects/cash-management/journal-entry-template/3"
    },
    {
      "key": "4",
      "id": "JET_YE_ADJ_2025",
      "href": "/objects/cash-management/journal-entry-template/4"
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

## POST /objects/cash-management/journal-entry-template
_Create a journal entry template_

**Request example — Create a journal entry template:**
```json
{
  "id": "JET_PAYROLL",
  "name": "Payroll Accrual Entry",
  "description": "Template to record monthly payroll accruals for salaries and wages.",
  "postingState": "draft",
  "status": "active",
  "glJournal": {
    "id": "APJ"
  },
  "lines": [
    {
      "dimensions": {
        "location": {
          "id": "1"
        }
      },
      "glAccount": {
        "key": "316"
      },
      "documentId": null,
      "memo": "Accrual of payroll expenses for month-end closing"
    }
  ]
}
```
**Response 201 — Reference to new journal entry template:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "JET_PAYROLL",
    "href": "/objects/cash-management/journal-entry-template/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/journal-entry-template/{key}
_Get a journal entry template_

**Response 200 — Get a journal entry template:**
```json
{
  "ia::result": {
    "key": "6",
    "name": "UK Office Purchases Journal Entry",
    "description": "Purchases for UK Office Supplies inclusive of UK VAT",
    "glJournal": {
      "id": "POJ",
      "key": "1",
      "href": "/objects/general-ledger/journal/1"
    },
    "postingState": "draft",
    "status": "active",
    "numberOfRulesUsingTemplate": 0,
    "id": "JET_UK_OFFICE_PURCHASES",
    "audit": {
      "createdDateTime": "2025-04-29T15:26:00Z",
      "modifiedDateTime": "2025-04-29T15:26:00Z",
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
    "taxImplication": "inbound",
    "taxSolution": {
      "key": "4",
      "id": "United Kingdom - VAT",
      "href": "/objects/tax/tax-solution/4"
    },
    "salesTaxSchedule": {
      "name": null,
      "key": null,
      "id": null
    },
    "purchasingTaxSchedule": {
      "name": "UK Purchase Goods Standard Rate",
      "id": "41",
      "key": "41",
      "href": "/objects/tax/purchasing-tax-schedule/41"
    },
    "vendor": {
      "key": "56",
      "id": "210",
      "name": "Office Supply and Copier Co.",
      "href": "/objects/accounts-payable/vendor/56"
    },
    "customer": {
      "key": null,
      "id": null,
      "name": null
    },
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "lines": [
      {
        "key": "8",
        "id": "8",
        "journalEntryTemplate": {
          "id": "6",
          "key": "6",
          "href": "/objects/cash-management/journal-entry-template/6"
        },
        "dimensions": {
          "location": {
            "key": "3",
            "id": "3",
            "name": "United Kingdom",
            "href": "/objects/company-config/location/3"
          },
          "department": {
            "key": "9",
            "id": "OPS",
            "name": "Operations",
            "href": "/objects/company-config/department/9"
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
          "contract": {
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
          },
          "glAccount": {
            "key": "11",
            "id": "1002",
            "name": "HSBC - GBP",
            "href": "/objects/general-ledger/account/11"
          }
        },
        "documentId": "156",
        "txnType": "debit",
        "memo": "Purchases for UK Office Supplies",
        "allocation": {
          "key": null,
          "id": null
        },
        "numberOfUnits": null,
        "exchangeRate": {
          "date": null,
          "typeId": null,
          "rate": null
        },
        "isBillable": false,
        "href": "/objects/cash-management/journal-entry-line-template/8"
      }
    ],
    "href": "/objects/cash-management/journal-entry-template/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/journal-entry-template/{key}
_Update a journal entry template_

**Request example — Update a journal entry template:**
```json
{
  "postingState": "posted"
}
```
**Response 200 — Reference to the updated journal entry template:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "6",
    "href": "/objects/cash-management/journal-entry-template/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/journal-entry-template/{key}
_Delete a journal entry template_


## GET /objects/cash-management/other-receipt
_List other receipts_

**Response 200 — List other receipts:**
```json
{
  "ia::result": [
    {
      "key": "182",
      "id": "182",
      "href": "/objects/cash-management/other-receipt/182"
    },
    {
      "key": "193",
      "id": "193",
      "href": "/objects/cash-management/other-receipt/193"
    },
    {
      "key": "501",
      "id": "501",
      "href": "/objects/cash-management/other-receipt/501"
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

## POST /objects/cash-management/other-receipt
_Create an other receipt_

**Request example — Create an other receipt:**
```json
{
  "payer": "Benson Hugo",
  "txnDate": "2022-01-23",
  "txnPaidDate": "2022-01-23",
  "txnNumber": "22365",
  "description": "Refund for overpayment",
  "baseCurrency": "USD",
  "currency": "USD",
  "state": "approved",
  "reconciliationState": "uncleared",
  "isInclusiveTax": false,
  "bankAccount": {
    "id": "BOA-REC-01"
  },
  "depositDate": "2022-01-23",
  "exchangeRate": {
    "date": "2022-01-23",
    "typeId": null,
    "rate": 1
  },
  "paymentMethod": "eft",
  "reversalDate": "2022-01-23",
  "reversedDate": "2022-01-23",
  "reversedVoidPaymentKey": "1400",
  "voidPaymentKey": "1923",
  "sourceModule": "cashManagement",
  "lines": [
    {
      "status": "active",
      "amount": "100.00",
      "txnAmount": "100.00",
      "description": "description",
      "lineNumber": 1,
      "baseCurrency": "USD",
      "currency": "USD",
      "isTax": false,
      "arAccountLabel": {
        "key": "35"
      },
      "glAccount": {
        "id": "5008"
      },
      "dimensions": {
        "location": {
          "id": "CAG"
        },
        "department": {
          "id": "OPEE"
        }
      }
    }
  ]
}
```
**Response 201 — Reference to the new other receipt:**
```json
{
  "ia::result": {
    "key": "500",
    "id": "500",
    "href": "/objects/cash-management/other-receipt/500"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/other-receipt-line
_List other receipt lines_

**Response 200 — List other receipt lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/other-receipt-line/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/other-receipt-line/3"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/cash-management/other-receipt-line/5"
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

## GET /objects/cash-management/other-receipt-line/{key}
_Get an other receipt line_

**Response 200 — Get an other receipt line:**
```json
{
  "ia::result": {
    "key": "821",
    "id": "821",
    "otherReceipts": {
      "key": "415",
      "id": "415",
      "recordType": "cr",
      "href": "/objects/cash-management/other-receipt/415"
    },
    "glAccount": {
      "key": "194",
      "id": "4000",
      "href": "/objects/general-ledger/account/194"
    },
    "arAccountLabel": {
      "key": "35",
      "id": "Bank charges",
      "href": "/objects/accounts-receivable/account-label/35"
    },
    "amount": "101.11",
    "txnAmount": "101.11",
    "dimensions": {
      "department": {
        "key": null,
        "id": null,
        "number": null,
        "name": null
      },
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
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
      "contract": {
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
    "description": "Refund for overpayment",
    "exchangeRate": {
      "date": "2025-01-15",
      "typeId": null,
      "rate": 1
    },
    "lineNumber": 1,
    "currency": "USD",
    "baseCurrency": "USD",
    "status": "active",
    "audit": {
      "createdDateTime": "2025-06-15T03:03:31Z",
      "modifiedDateTime": "2025-06-15T03:03:32Z",
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
    "isTax": false,
    "taxEntries": [],
    "href": "/objects/cash-management/other-receipt-line/821"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/other-receipt-tax-entry
_List other receipts tax entries_

**Response 200 — List other receipt tax entries:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "8",
      "href": "/objects/cash-management/other-receipt-tax-entry/8"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/cash-management/other-receipt-tax-entry/9"
    },
    {
      "key": "10",
      "id": "10",
      "href": "/objects/cash-management/other-receipt-tax-entry/10"
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

## GET /objects/cash-management/other-receipt-tax-entry/{key}
_Get other receipt tax entries_

**Response 200 — Get an other receipt tax entry:**
```json
{
  "ia::result": {
    "key": "300",
    "id": "300",
    "baseTaxAmount": "100",
    "txnTaxAmount": "100",
    "description": "Standard Rate for UK Import Services",
    "taxRate": 5.5,
    "taxDetail": {
      "id": "UK Export Reduced Rate",
      "key": "24",
      "href": "/objects/tax/order-entry-tax-detail/24"
    },
    "otherReceiptLine": {
      "id": "148",
      "key": "148",
      "href": "/objects/cash-management/other-receipt-line/148"
    },
    "href": "/objects/cash-management/tax/other-receipt-tax-entry/300"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/other-receipt/{key}
_Get an other receipt_

**Response 200 — Get an other receipt:**
```json
{
  "ia::result": {
    "id": "557",
    "key": "557",
    "txnDate": "2022-01-23",
    "payer": "Alan Smith-Jones",
    "txnPaidDate": "2022-01-23",
    "recordType": "cr",
    "paymentMethod": "creditCard",
    "txnNumber": "2251",
    "description": "Conference booth fee",
    "bankAccount": {
      "key": "45",
      "id": "BOA-REC-01",
      "name": "Bank of America Receipts Account",
      "currency": "USD",
      "href": "/objects/cash-management/bank-account/45"
    },
    "depositDate": "2022-01-23",
    "arSummary": {
      "key": "315",
      "id": "315",
      "href": "/objects/accounts-receivable/summary/315"
    },
    "baseCurrency": "USD",
    "currency": "USD",
    "exchangeRate": {
      "date": null,
      "typeId": null,
      "rate": null
    },
    "totalEntered": "150.00",
    "txnTotalEntered": "150.00",
    "reconciliationDate": null,
    "state": "approved",
    "reconciliationState": "cleared",
    "clearingDate": "2024-01-23",
    "parentDeposit": {
      "key": null,
      "id": null
    },
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
    "isInclusiveTax": false,
    "taxSolution": {
      "key": null,
      "id": null,
      "enableMultilineTax": null,
      "taxCalculationMethod": null
    },
    "voidPaymentKey": null,
    "reversalDate": null,
    "reversedVoidPaymentKey": null,
    "reversedDate": null,
    "sourceModule": "cashManagement",
    "entity": {
      "key": "1",
      "id": "1",
      "name": "United States of America",
      "href": "/objects/company-config/entity/1"
    },
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "lines": [
      {
        "key": "1101",
        "id": "1101",
        "otherReceipts": {
          "key": "557",
          "id": "557",
          "recordType": "cr",
          "href": "/objects/cash-management/other-receipt/557"
        },
        "glAccount": {
          "key": "222",
          "id": "5008",
          "href": "/objects/general-ledger/account/222"
        },
        "arAccountLabel": {
          "key": "35",
          "id": "35",
          "href": "/objects/accounts-receivable/account-label/35"
        },
        "amount": "150.00",
        "txnAmount": "150.00",
        "dimensions": {
          "department": {
            "number": "21",
            "id": "OPEE",
            "name": "Operations",
            "key": "21",
            "href": "/objects/company-config/department/21"
          },
          "location": {
            "id": "CAG",
            "name": "Calgary",
            "key": "30",
            "href": "/objects/company-config/location/30"
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
          "contract": {
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
        "description": "Bank interest earned",
        "exchangeRate": {
          "date": null,
          "typeId": null,
          "rate": 1
        },
        "lineNumber": 1,
        "currency": "USD",
        "baseCurrency": "USD",
        "status": "active",
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
        "isTax": false,
        "taxEntries": [],
        "href": "/objects/cash-management/other-receipt-line/1101"
      }
    ],
    "undepositedGLAccount": {
      "id": null
    },
    "href": "/objects/cash-management/other-receipt/557"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/other-receipt/{key}
_Update an other receipt_

**Request example — Update an other receipt:**
```json
{
  "description": "2025 Conference booth fee"
}
```
**Response 200 — Reference to updated other receipt:**
```json
{
  "ia::result": {
    "key": "500",
    "id": "500",
    "href": "/objects/cash-management/other-receipt/500"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/cash-management/other-receipt/{key}
_Delete an other receipt_


## GET /objects/cash-management/payment-provider
_List payment providers_

**Response 200 — List payment providers:**
```json
{
  "ia::result": [
    {
      "key": "3",
      "id": "CSI",
      "href": "/objects/cash-management/payment-provider/3"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "start": 1,
    "pageSize": 100,
    "next": 0,
    "previous": 0
  }
}
```

## GET /objects/cash-management/payment-provider-bank-account
_List payment provider bank accounts_

**Response 200 — List payment provider bank accounts:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/payment-provider-bank-account/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/cash-management/payment-provider-bank-account/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/payment-provider-bank-account/3"
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

## POST /objects/cash-management/payment-provider-bank-account
_Create a payment provider bank account_

**Request example — Create a payment provider bank account:**
```json
{
  "paymentProvider": {
    "id": "CSI"
  },
  "bankAccount": {
    "id": "WF"
  },
  "status": "active",
  "checkStartNumber": "111000",
  "remittanceEmail": "jsmith@example.com"
}
```
**Response 201 — New Payment Provider bank account:**
```json
{
  "ia::result": {
    "key": "22",
    "id": "22",
    "href": "/objects/cash-management/payment-provider-bank-account/22"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/payment-provider-bank-account/{key}
_Get a payment provider bank account_

**Response 200 — Get a payment provider bank account:**
```json
{
  "ia::result": {
    "key": "19",
    "id": "19",
    "paymentProvider": {
      "key": "1",
      "id": "CSI",
      "href": "/objects/cash-management/payment-provider/1"
    },
    "bankAccount": {
      "key": "72",
      "id": "BOA",
      "currency": "USD",
      "href": "/objects/cash-management/checking-account/72"
    },
    "state": "subscribed",
    "isRebateAccount": false,
    "providerReferenceNumber": "44397977-72-1643357336",
    "authenticationURL": "",
    "audit": {
      "createdDateTime": "2022-01-28T08:08:56Z",
      "modifiedDateTime": "2022-01-28T08:23:08Z",
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
    "status": "active",
    "checkStartNumber": "123456",
    "href": "/objects/cash-management/payment-provider-bank-account/19"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/cash-management/payment-provider-bank-account/{key}
_Update a payment provider bank account_

**Request example — Update a payment provider bank account:**
```json
{
  "isRebateAccount": false,
  "checkStartNumber": "111222"
}
```
**Response 200 — Updated payment provider bank account:**
```json
{
  "ia::result": {
    "key": "19",
    "id": "19",
    "href": "/objects/cash-management/payment-provider-bank-account/19"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/payment-provider/{key}
_Get a payment provider_

**Response 200 — Get a payment-provider:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "CSI",
    "name": "CSI",
    "contactInfo": {
      "email": "Jdoe@company.com",
      "firstName": "John",
      "lastName": "doe"
    },
    "paymentWithdrawalType": "perTransaction",
    "state": "subscribed",
    "audit": {
      "createdDateTime": "2021-07-28T11:07:33Z",
      "modifiedDateTime": "2021-09-06T05:17:26Z",
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
    "paymentMethods": [
      {
        "key": "453",
        "id": "453",
        "paymentProvider": {
          "id": "CSI",
          "name": "CSI",
          "key": "3",
          "href": "/objects/cash-management/payment-provider/3"
        },
        "paymentType": "VCARD",
        "audit": {
          "createdDateTime": "2021-07-30T03:29:20Z",
          "modifiedDateTime": "2021-09-06T05:17:26Z",
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
        "href": "/objects/cash-management/provider-payment-method/453"
      }
    ],
    "href": "/objects/cash-management/payment-provider/3"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/provider-payment-method
_List provider payment methods_

**Response 200 — List provider payment methods:**
```json
{
  "ia::result": [
    {
      "key": "453",
      "id": "453",
      "href": "/objects/cash-management/provider-payment-method/453"
    },
    {
      "key": "454",
      "id": "454",
      "href": "/objects/cash-management/provider-payment-method/454"
    },
    {
      "key": "455",
      "id": "455",
      "href": "/objects/cash-management/provider-payment-method/455"
    },
    {
      "key": "456",
      "id": "456",
      "href": "/objects/cash-management/provider-payment-method/456"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "start": 1,
    "pageSize": 100,
    "next": 0,
    "previous": 0
  }
}
```

## GET /objects/cash-management/provider-payment-method/{key}
_Get a provider payment method_

**Response 200 — Get a provider payment method:**
```json
{
  "ia::result": {
    "key": "454",
    "id": "454",
    "paymentProvider": {
      "id": "CSI",
      "name": "CSI",
      "key": "3",
      "href": "/objects/cash-management/payment-provider/3"
    },
    "paymentType": "CHECK",
    "audit": {
      "createdDateTime": "2021-07-30T03:29:20Z",
      "modifiedDateTime": "2021-09-06T05:17:26Z",
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
    "status": "active",
    "href": "/objects/cash-management/provider-payment-method/454"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/received-payment
_List received payments_

**Response 200 — List received payments:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/cash-management/received-payment/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/cash-management/received-payment/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/cash-management/received-payment/3"
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

## POST /objects/cash-management/received-payment
_Create a new received payment_

**Request example — Create a received payment:**
```json
{
  "paymentApplicationMethod": "matchToOpenAmount",
  "arPayment": {
    "paymentMethod": "printedCheck"
  },
  "paymentMemo": "Auto generated",
  "createAdvances": false,
  "isDraft": false,
  "arAdvanceTemplate": {
    "key": "23"
  },
  "receivedPaymentLine": [
    {
      "bankTxnRecord": {
        "key": "6213"
      }
    }
  ]
}
```
**Response 201 — Create a received payment:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/cash-management/received-payment/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/received-payment-line
_List received payment lines_

**Response 200 — List received payment lines:**
```json
{
  "ia::result": [
    {
      "key": "10",
      "id": "10",
      "href": "/objects/cash-management/received-payment-line/10"
    },
    {
      "key": "11",
      "id": "11",
      "href": "/objects/cash-management/received-payment-line/11"
    },
    {
      "key": "12",
      "id": "12",
      "href": "/objects/cash-management/received-payment-line/12"
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

## GET /objects/cash-management/received-payment-line/{key}
_Get a received payment line_

**Response 200 — Get a received payment line:**
```json
{
  "ia::result": {
    "id": "12",
    "key": "12",
    "receivedPayment": {
      "id": "1",
      "key": "1",
      "href": "/objects/cash-management/received-payment/1"
    },
    "bankTxnRecord": {
      "key": "6213",
      "id": "6213",
      "href": "/objects/cash-management/bank-transaction/6213"
    },
    "intacctTxnRecord": {
      "key": "645",
      "id": "645",
      "href": "/objects/accounts-payable/subledger-record/645"
    },
    "status": "success",
    "errorMessage": "Payment date cannot be before invoice creation date.",
    "audit": {
      "createdDateTime": "2025-04-29T15:26:00Z",
      "modifiedDateTime": "2025-04-29T15:26:00Z",
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
    "href": "/objects/cash-management/received-payment-line/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/received-payment/{key}
_Get a received payment_

**Response 200 — Get a received payment:**
```json
{
  "ia::result": {
    "id": "1",
    "key": "1",
    "paymentApplicationMethod": "matchToOpenAmount",
    "arPayment": {
      "paymentMethod": "printedCheck",
      "id": "10",
      "key": "10",
      "href": "/objects/accounts-receivable/payment/10"
    },
    "paymentMemo": "Auto generated",
    "createAdvances": false,
    "isDraft": false,
    "arAdvanceTemplate": {
      "key": "23",
      "id": "AR-advance-txn-template-023",
      "href": "/objects/cash-management/ar-advance-txn-template/23"
    },
    "audit": {
      "createdDateTime": "2025-04-29T15:26:00Z",
      "modifiedDateTime": "2025-04-29T15:26:00Z",
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
    "receivedPaymentLine": [
      {
        "id": "12",
        "key": "12",
        "receivedPayment": {
          "id": "1",
          "key": "1",
          "href": "/objects/cash-management/received-payment/1"
        },
        "bankTxnRecord": {
          "key": "6213",
          "id": "6213",
          "href": "/objects/cash-management/bank-transaction/6213"
        },
        "intacctTxnRecord": {
          "key": "645",
          "id": "645",
          "href": "/objects/accounts-payable/subledger-record/645"
        },
        "status": "success",
        "errorMessage": "Payment date cannot be before Invoice creation date.",
        "audit": {
          "createdDateTime": "2025-04-29T15:26:00Z",
          "modifiedDateTime": "2025-04-29T15:26:00Z",
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
        "href": "/objects/cash-management/received-payment-line/12"
      }
    ],
    "href": "/objects/cash-management/received-payment/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/cash-management/reconciliation-source-record
_List account reconciliation source records_

**Response 200 — List source records:**
```json
{
  "ia::result": [
    {
      "key": "515",
      "id": "515",
      "href": "/objects/cash-management/reconciliation-source-record/515"
    },
    {
      "key": "516",
      "id": "516",
      "href": "/objects/cash-management/reconciliation-source-record/516"
    },
    {
      "key": "517",
      "id": "517",
      "href": "/objects/cash-management/reconciliation-source-record/517"
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

## GET /objects/cash-management/reconciliation-source-record/{key}
_Get an account reconciliation source record_

**Response 200 — Get an account reconciliation source record:**
```json
{
  "ia::result": {
    "key": "2672",
    "id": "2672",
    "txnInformation": {
      "recordType": "fundsTransfer",
      "subledgerRecord": {
        "key": "2225",
        "id": "2225",
        "href": "/objects/accounts-payable/subledger-record/2225"
      },
      "journalEntryLine": {
        "key": "10",
        "id": "10"
      },
      "initialOpenItem": {
        "key": "234",
        "id": "234"
      },
      "txnType": "withdrawal",
      "documentNumber": "CHK100",
      "documentDate": "2020-10-23",
      "txnAmount": "1200.00",
      "baseAmount": "1200.00",
      "txnCurrency": "USD",
      "baseCurrency": "USD",
      "postingDate": "2020-10-23",
      "payee": "Business Software Inc.",
      "description": "Refund for overpayment of subscription fees.",
      "reconciliationState": "selectedToMatch",
      "postingState": "partiallyApproved"
    },
    "audit": {
      "createdDateTime": "2025-04-11T12:56:46Z",
      "modifiedDateTime": "2025-04-11T12:56:46Z",
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
    "href": "/objects/cash-management/reconciliation-source-record/2672"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/cash-management/savings-account
_List savings accounts_

**Response 200 — List savings accounts:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "AUDCHK",
      "href": "/objects/cash-management/savings-account/84"
    },
    {
      "key": "85",
      "id": "BDF",
      "href": "/objects/cash-management/savings-account/85"
    },
    {
      "key": "60",
      "id": "BOA",
      "href": "/objects/cash-management/savings-account/60"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/cash-management/savings-account
_Create a savings account_

**Request example — Create a savings account:**
```json
{
  "id": "SAVINGS455_6780",
  "bankAccountDetails": {
    "accountNumber": "",
    "bankName": "Savings Bank of America New",
    "routingNumber": "565676545",
    "branchId": "123456791",
    "phoneNumber": "6509876545",
    "bankAddress": {
      "addressLine1": "73466 Linkln St",
      "addressLine2": null,
      "addressLine3": null,
      "city": "Montaine View",
      "country": "United States",
      "postCode": "67898",
      "state": "CA"
    },
    "currency": "USD"
  },
  "accounting": {
    "glAccount": {
      "id": "2458.90.33--SAVINGS455 GL"
    },
    "apJournal": {
      "key": "18"
    },
    "arJournal": {
      "id": "ARJ--Accounts Receivable Journal"
    },
    "bankingTimeZone": "GMT+05:30 Bombay, Calcutta, Madras, New Delhi",
    "serviceChargeGLAccount": {
      "key": "417"
    },
    "interestGLAccount": {
      "key": "572"
    },
    "disableInterEntityTransfer": true
  },
  "reconciliation": {
    "matchingSequenceNumber": {
      "key": "48"
    },
    "useSequenceNumberForAutoMatch": false,
    "useMatchSequenceForManualMatch": true
  },
  "department": {
    "id": "11--Accounting"
  },
  "location": {
    "id": "1--United States of America"
  },
  "status": "active",
  "ruleSet": {
    "key": "53"
  }
}
```
**Response 201 — 201 response example:**
```json
{
  "ia::result": {
    "key": "12345",
    "id": "ID123",
    "href": "/objects/<application>/<name>/12345"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## GET /objects/cash-management/savings-account/{key}
_Get a savings account_

**Response 200 — Get a savings account:**
```json
{
  "ia::result": {
    "id": "SAVINGS455_6780",
    "bankAccountDetails": {
      "accountNumber": "789678988",
      "bankName": "Savings Bank of America New",
      "routingNumber": "565676545",
      "branchId": "123456791",
      "phoneNumber": "6509876545",
      "bankAddress": {
        "addressLine1": "73466 Linkln St",
        "addressLine2": null,
        "addressLine3": null,
        "city": "Montaine View",
        "country": "United States",
        "postCode": "67898",
        "state": "CA"
      },
      "currency": "USD"
    },
    "accounting": {
      "glAccount": {
        "id": "2458.90.33--SAVINGS455 GL",
        "key": "543",
        "href": "/objects/general-ledger/account/543"
      },
      "apJournal": {
        "id": "AP ADJ--AP Adjustment Journal",
        "key": "18",
        "href": "/objects/general-ledger/journal/18"
      },
      "arJournal": {
        "id": "ARJ--Accounts Receivable Journal",
        "key": "6",
        "href": "/objects/general-ledger/journal/6"
      },
      "bankingTimeZone": "GMT+05:30 Bombay, Calcutta, Madras, New Delhi",
      "serviceChargeGLAccount": {
        "key": "417",
        "id": "0009--My Ledger Account 39",
        "href": "/objects/general-ledger/account/417"
      },
      "serviceChargeAccountLabel": {
        "id": null,
        "key": null
      },
      "interestGLAccount": {
        "key": "572",
        "id": "0032--My Ledger Account 32",
        "href": "/objects/general-ledger/account/572"
      },
      "interestAccountLabel": {
        "key": null,
        "id": null
      },
      "disableInterEntityTransfer": true
    },
    "reconciliation": {
      "matchingSequenceNumber": {
        "key": "48",
        "id": "48--bankseq-1",
        "href": "/objects/company-config/document-sequence/48"
      },
      "useSequenceNumberForAutoMatch": false,
      "useMatchSequenceForManualMatch": true,
      "lastReconciledBalance": null,
      "lastReconciledDate": null,
      "cutOffDate": null,
      "inProgressBalance": null,
      "inProgressDate": null
    },
    "department": {
      "key": "9",
      "id": "11--Accounting",
      "href": "/objects/company-config/department/9"
    },
    "location": {
      "key": "1",
      "id": "1--United States of America",
      "href": "/objects/company-config/location/1"
    },
    "status": "active",
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "audit": {
      "createdDateTime": "2024-03-07T18:35:38Z",
      "modifiedDateTime": "2024-03-07T18:40:25Z",
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
    "key": "288",
    "bankingCloudConnection": {
      "status": "notConnected",
      "bankName": null,
      "name": null,
      "lastBankTxnDateTime": null,
      "lastRefreshedDateTime": null,
      "supportMultiAccountLinking": null
    },
    "financialInstitution": {
      "key": null,
      "id": null
    },
    "ruleSet": {
      "id": "53--MatchDateAmountGrpbyDateRuleSet",
      "key": "53",
      "href": "/objects/cash-management/bank-txn-rule-set/53"
    },
    "href": "/objects/cash-management/savings-account/288"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/cash-management/savings-account/{key}
_Update a savings account_

**Request example — Update a savings account:**
```json
{
  "bankAccountDetails": {
    "bankName": "Bank of America New"
  },
  "ruleSet": {
    "key": "53",
    "id": "MatchDateAmountGrpbyDateRuleSet"
  },
  "restrictions": {
    "restrictionType": "unrestricted",
    "locations": []
  },
  "reconciliation": {
    "matchingSequenceNumber": {
      "key": "48"
    },
    "useSequenceNumberForAutoMatch": true,
    "useMatchSequenceForManualMatch": true
  }
}
```
**Response 201 — 201 response example:**
```json
{
  "ia::result": {
    "key": "12345",
    "id": "ID123",
    "href": "/objects/<application>/<name>/12345"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## DELETE /objects/cash-management/savings-account/{key}
_Delete a savings account_

**Response 400 — Request Example:**
```json
{
  "ia::result": {
    "ia::error": {
      "code": "invalidRequest",
      "message": "A POST request requires a payload",
      "errorId": "REST-1028",
      "additionalInfo": {
        "messageId": "IA.REQUEST_REQUIRES_A_PAYLOAD",
        "placeholders": {
          "OPERATION": "POST"
        },
        "propertySet": {}
      },
      "supportId": "Kxi78%7EZuyXBDEGVHD2UmO1phYXDQAAAAo"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 0,
    "totalError": 1
  }
}
```

## GET /objects/cash-management/undeposited-fund
_List undeposited funds_

**Response 200 — List undeposited funds:**
```json
{
  "ia::result": [
    {
      "key": "182",
      "id": "182",
      "href": "/objects/cash-management/undeposited-fund/182"
    },
    {
      "key": "193",
      "id": "193",
      "href": "/objects/cash-management/undeposited-fund/193"
    },
    {
      "key": "501",
      "id": "501",
      "href": "/objects/cash-management/undeposited-fund/501"
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

## GET /objects/cash-management/undeposited-fund/{key}
_Get an undeposited fund_

**Response 200 — Get an undeposited fund:**
```json
{
  "ia::result": {
    "id": "587",
    "key": "587",
    "deposit": {
      "id": "291",
      "key": "291",
      "depositType": "cd",
      "href": "/objects/cash-management/deposit/291"
    },
    "glAccount": {
      "id": "33",
      "key": "33",
      "accountNumber": "1070",
      "name": "Undeposited Funds",
      "href": "/objects/general-ledger/account/33"
    },
    "arAccountLabel": {
      "label": null,
      "id": null,
      "key": null
    },
    "amount": "1002.00",
    "txnAmount": "1002.00",
    "department": {
      "key": null,
      "id": null,
      "name": null
    },
    "location": {
      "key": "1",
      "name": "United States of America",
      "href": "/objects/company-config/location/1"
    },
    "baseLocation": {
      "name": "United States of America",
      "key": null
    },
    "description": "Undeposited receipt from GoPro sales",
    "exchangeRate": {
      "date": "2022-01-23",
      "typeId": "-1",
      "rate": 1
    },
    "currency": "USD",
    "baseCurrency": "USD",
    "status": "active",
    "audit": {
      "createdDateTime": "2025-06-11T12:56:46Z",
      "modifiedDateTime": "2025-06-11T12:56:46Z",
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
    "href": "/objects/cash-management/undeposited-fund/587"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/cash-management/bank-file/generate
_Generate a bank file_

**Request example — Generate a bank file:**
```json
{
  "paymentKeys": [
    "977"
  ]
}
```
**Response 422 — Generate a bank file:**
```json
{
  "ia::result": [
    {
      "key": "1221",
      "href": "/objects/cash-management/bank-file/1221",
      "ia::status": 422,
      "ia::error": {
        "message": "1221: Please provide a valid value for 'Beneficiary name' to VENDOR 'BankfileTest001' must contain at least 1 character and no more than 18 characters. [Support ID: PMkdcWEB300%7EaLBE_P3a0-z8fYM-QmCD1wAAAAY]"
      }
    }
  ],
  "ia::meta": {
    "totalError": 1,
    "totalSuccess": 0,
    "totalCount": 1
  }
}
```

## POST /workflows/cash-management/bank-fee/reverse
_Reverse a bank fee_

**Request example — Request Example:**
```json
{
  "key": "518",
  "reversedDate": "2024-01-23",
  "notes": "Bank fee charged in error."
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "519",
  "id": "519",
  "href": "/objects/cash-management/bank-fee/519",
  "state": "reversed"
}
```

## POST /workflows/cash-management/bank-reconciliation/reopen
_Reopen a bank reconciliation_

**Request example — Request Example:**
```json
{
  "key": "12",
  "bankAccountId": "BOA",
  "reconciliationDate": "2025-01-23"
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "12",
  "bankAccountId": "BOA",
  "state": "reopened",
  "message": "Number of reconciliations to reopen and reconcile again - 1, from 05/31/2025 to 06/05/2025."
}
```

## POST /workflows/cash-management/bank-transaction/assign-customer
_Assign customer to a bank transaction_

**Request example — Request Example:**
```json
{
  "key": "12",
  "customerId": "US108"
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "12",
  "customerId": "US108"
}
```

## POST /workflows/cash-management/bank-transaction/ignore
_Ignore a bank transaction_

**Request example — Request Example:**
```json
{
  "key": "12"
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "12",
  "state": "ignored"
}
```

## POST /workflows/cash-management/bank-transaction/stop-ignoring
_Stop ignoring a bank transaction_

**Request example — Request Example:**
```json
{
  "key": "12"
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "12",
  "state": "unmatched"
}
```

## POST /workflows/cash-management/charge-payoff/reverse
_Reverse a charge payoff_

**Request example — Request Example:**
```json
{
  "key": "23",
  "reversedDate": "2025-01-23",
  "notes": "Charge payoff reversed due to duplicate entry."
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "24",
  "id": "24",
  "href": "/objects/cash-management/charge-payoff/24",
  "state": "voided"
}
```

## POST /workflows/cash-management/credit-card-fee/reverse
_Reverse a credit card fee_

**Request example — Request Example:**
```json
{
  "key": "518",
  "reversedDate": "2024-01-23",
  "notes": "Credit card fee charged in error."
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "519",
  "id": "519",
  "href": "/objects/cash-management/credit-card-fee/519",
  "state": "reversed"
}
```

## POST /workflows/cash-management/credit-card-reconciliation/reopen
_Reopen a credit card reconciliation_

**Request example — Request Example:**
```json
{
  "key": "12",
  "creditCardAccountId": "AMEX_CARD",
  "reconciliationDate": "2025-01-23"
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "12",
  "creditCardAccountId": "AMEX_CARD",
  "isReopened": false,
  "message": "Number of reconciliations to reopen and reconcile again - 1, from 05/31/2025 to 06/05/2025."
}
```

## POST /workflows/cash-management/credit-card-txn/reverse
_Reverse a credit card transaction_

**Request example — Request Example:**
```json
{
  "key": "49",
  "reversedDate": "2024-04-15",
  "memo": "Credit card transaction charged in error."
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "50",
  "id": "50",
  "href": "/objects/cash-management/credit-card-txn/50",
  "state": "reversed"
}
```

## POST /workflows/cash-management/deposit/reverse
_Reverse a deposit_

**Request example — Request Example:**
```json
{
  "key": "49",
  "reversedDate": "2025-04-15",
  "notes": "Deposit reversed due to duplicate entry."
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "50",
  "id": "50",
  "href": "/objects/cash-management/deposit/50",
  "state": "reversed"
}
```

## POST /workflows/cash-management/funds-transfer/reverse
_Reverse a funds transfer_

**Request example — Request Example:**
```json
{
  "key": "39",
  "reversedDate": "2025-05-07",
  "memo": "Reversed the fund transfer transaction to correct a duplicate entry."
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "305",
  "id": "305",
  "href": "/objects/cash-management/funds-transfer/305",
  "state": "reversed"
}
```

## POST /workflows/cash-management/other-receipt/reverse
_Reverse an other receipt_

**Request example — Request Example:**
```json
{
  "key": "49",
  "reversedDate": "2025-04-15",
  "notes": "Other receipt reversed due to duplicate entry."
}
```
**Response 200 — 200 response example:**
```json
{
  "key": "50",
  "id": "50",
  "href": "/objects/cash-management/other-receipt/50",
  "state": "reversed"
}
```
