# Consolidation

## GET /objects/consolidation/adjustment-journal
_List adjustment journals_

**Response 200 — List adjustment journals:**
```json
{
  "ia::result": [
    {
      "key": "22",
      "id": "22",
      "href": "/objects/consolidation/adjustment-journal/22"
    },
    {
      "key": "53",
      "id": "53",
      "href": "/objects/consolidation/adjustment-journal/53"
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

## POST /objects/consolidation/adjustment-journal
_Create an adjustment journal_

**Request example — Create an adjustment journal:**
```json
{
  "consolidationBookId": "consol_book",
  "userDefinedBookType": "userDefined",
  "glJournal": {
    "id": "consol_book_api",
    "name": "consol_book useradj api"
  },
  "userDefinedBookId": "consol_book_userdef"
}
```
**Request example — Create an adjustment journal for a TAX adjustment:**
```json
{
  "consolidationBookId": "consol_book",
  "userDefinedBookType": "tax",
  "glJournal": {
    "id": "consol_book_tax",
    "name": "consol_book tax api"
  }
}
```
**Response 201 — Reference to adjustment journal:**
```json
{
  "ia::result": {
    "id": "55",
    "key": "55",
    "href": "/objects/consolidation/adjustment-journal/55"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/adjustment-journal/{key}
_Get an adjustment journal_

**Response 200 — Get an adjustment journal:**
```json
{
  "ia::result": {
    "id": "70",
    "key": "70",
    "consolidationBookId": "consol_book",
    "userDefinedBookType": "gaap",
    "glJournal": {
      "key": "139",
      "id": "consol_book_api",
      "name": "consol_book gaap api",
      "href": "/objects/general-ledger/journal/139"
    },
    "userDefinedBookId": "GAAPADJ",
    "audit": {
      "createdDateTime": "2025-03-20T15:01:23Z",
      "modifiedDateTime": "2025-03-20T15:05:17Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "href": "/objects/consolidation/adjustment-journal/70"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/consolidation/adjustment-journal/{key}
_Update an adjustment journal_

**Request example — Update an adjustment journal:**
```json
{
  "glJournal": {
    "name": "consol_book gaap api - updated"
  }
}
```
**Response 200 — Reference to adjustment journal:**
```json
{
  "ia::result": {
    "id": "70",
    "key": "70",
    "href": "/objects/consolidation/adjustment-journal/70"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/consolidation/adjustment-journal/{key}
_Delete an adjustment journal_


## GET /objects/consolidation/book
_List consolidation books_

**Response 200 — List consolidation books:**
```json
{
  "ia::result": [
    {
      "key": "49",
      "id": "consol_book_US_operations",
      "href": "/objects/consolidation/book/49"
    },
    {
      "key": "65",
      "id": "consol_book_holdings",
      "href": "/objects/consolidation/book/65"
    },
    {
      "key": "89",
      "id": "consolBookApi",
      "href": "/objects/consolidation/book/89"
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

## POST /objects/consolidation/book
_Create a consolidation book_

**Request example — Create a consolidation book:**
```json
{
  "id": "consol_book_US_entities",
  "description": "Consolidation book for US entities",
  "status": "active",
  "multiCurrency": {
    "currency": "USD",
    "cumulativeTranslationAdjustment": {
      "netAssetGLAccount": {
        "key": "9"
      },
      "netIncomeGLAccount": {
        "key": "10"
      }
    },
    "exchangeRateType": "intacctDailyRate",
    "translationMethod": {
      "balanceSheetTranslationMethod": "endingSpotRate",
      "incomeTranslationMethod": "weightedAverageRate"
    }
  },
  "statisticalJournal": {
    "id": "consol_book_SJ",
    "name": "consol_book statistical journal"
  },
  "budget": {
    "key": "1"
  },
  "department": {
    "key": "1"
  },
  "elimination": {
    "entity": "USDE",
    "enableInterEntityAutoElimination": true,
    "adjustmentGLAccount": {
      "key": "11"
    },
    "enableEliminationByAffiliateEntity": true
  },
  "accountingMethod": "accrual",
  "bookJournal": {
    "id": "consol_book_J",
    "name": "consol_book journal"
  },
  "isLegacyBook": false,
  "historicalRateDateType": "lineLevelExchangeRateDate",
  "consolidateDimensions": [
    "department",
    "location",
    "vendor"
  ]
}
```
**Response 201 — Reference to consolidation book:**
```json
{
  "ia::result": {
    "key": "105",
    "id": "consol_book_EMEA_entities",
    "href": "/objects/consolidation/book/105"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/book/{key}
_Get a consolidation book_

**Response 200 — Get a consolidation book:**
```json
{
  "ia::result": {
    "key": "89",
    "id": "consol_book",
    "description": "Consolidation book for US entities.",
    "status": "active",
    "multiCurrency": {
      "currency": "USD",
      "cumulativeTranslationAdjustment": {
        "netAssetGLAccount": {
          "id": "1000",
          "key": "9",
          "name": "Bank of America A/c.",
          "href": "/objects/general-ledger/account/9"
        },
        "netIncomeGLAccount": {
          "id": "1001",
          "key": "10",
          "name": "CitiBank",
          "href": "/objects/general-ledger/account/10"
        }
      },
      "exchangeRateType": "intacctDailyRate",
      "translationMethod": {
        "balanceSheetTranslationMethod": "endingSpotRate",
        "incomeTranslationMethod": "weightedAverageRate"
      }
    },
    "statisticalJournal": {
      "id": "consol_book_SJ",
      "name": "consol_book statistical journal"
    },
    "budget": {
      "id": "Std_Budget",
      "key": "1",
      "href": "/objects/general-ledger/budget/1"
    },
    "department": {
      "id": "OP",
      "key": "1",
      "name": "Operations",
      "href": "/objects/company-config/department/1"
    },
    "elimination": {
      "entity": "USDE",
      "enableInterEntityAutoElimination": true,
      "adjustmentGLAccount": {
        "id": "1002",
        "key": "11",
        "name": "HSBC - GBP",
        "href": "/objects/general-ledger/account/11"
      },
      "enableEliminationByAffiliateEntity": true
    },
    "bookType": "consolidation",
    "accountingMethod": "accrual",
    "bookJournal": {
      "id": "consol_book_J"
    },
    "isLegacyBook": false,
    "historicalRateDateType": "lineLevelExchangeRateDate",
    "consolidateDimensions": [
      "department",
      "location",
      "vendor"
    ],
    "ownershipStructure": {
      "key": null,
      "id": null,
      "description": null
    },
    "audit": {
      "modifiedDateTime": "2025-04-13T09:19:58Z",
      "modifiedBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdDateTime": "2025-04-13T09:05:08Z",
      "createdBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/consolidation/book/89"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get an advanced ownership consolidation book:**
```json
{
  "ia::result": {
    "key": "89",
    "id": "us_book",
    "description": "Advanced ownership consolidation book.",
    "status": "active",
    "multiCurrency": {
      "currency": "USD",
      "cumulativeTranslationAdjustment": {
        "netAssetGLAccount": {
          "id": "1000",
          "key": "9",
          "name": "Bank of America A/c.",
          "href": "/objects/general-ledger/account/9"
        },
        "netIncomeGLAccount": {
          "id": "1001",
          "key": "10",
          "name": "CitiBank",
          "href": "/objects/general-ledger/account/10"
        }
      },
      "exchangeRateType": "intacctDailyRate",
      "translationMethod": {
        "balanceSheetTranslationMethod": "endingSpotRate",
        "incomeTranslationMethod": "weightedAverageRate"
      }
    },
    "statisticalJournal": {
      "id": null,
      "name": null
    },
    "budget": {
      "id": "Std_Budget",
      "key": "1",
      "href": "/objects/general-ledger/budget/1"
    },
    "department": {
      "id": "OP",
      "key": "1",
      "name": "Operations",
      "href": "/objects/company-config/department/1"
    },
    "elimination": {
      "entity": "USDE",
      "enableInterEntityAutoElimination": true,
      "adjustmentGLAccount": {
        "id": "1002",
        "key": "11",
        "name": "HSBC - GBP",
        "href": "/objects/general-ledger/account/11"
      },
      "enableEliminationByAffiliateEntity": true
    },
    "bookType": "tierConsolidation",
    "accountingMethod": "accrual",
    "bookJournal": {
      "id": null,
      "name": null
    },
    "isLegacyBook": false,
    "historicalRateDateType": "lineLevelExchangeRateDate",
    "consolidateDimensions": [
      "department",
      "location",
      "vendor"
    ],
    "ownershipStructure": {
      "key": "1",
      "id": "North America",
      "description": "All entities in North America."
    },
    "audit": {
      "modifiedDateTime": "2025-04-13T09:19:58Z",
      "modifiedBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdDateTime": "2025-04-13T09:05:08Z",
      "createdBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/consolidation/book/89"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/consolidation/book/{key}
_Delete a consolidation book_


## PATCH /objects/consolidation/book/{key}
_Update a consolidation book_

**Request example — Update a consolidation book:**
```json
{
  "description": "Consolidation book for GBP entities - updated.",
  "status": "inactive",
  "statisticalJournal": {
    "id": "consol_book_SJ1",
    "name": "consol_book statistical journal-1"
  },
  "budget": {
    "key": "1"
  },
  "department": {
    "key": "1"
  },
  "elimination": {
    "entity": "GBPE",
    "enableInterEntityAutoElimination": true,
    "adjustmentGLAccount": {
      "key": "11"
    },
    "enableEliminationByAffiliateEntity": true
  },
  "historicalRateDateType": "transactionDate",
  "consolidateDimensions": [
    "department",
    "location"
  ]
}
```
**Response 200 — Reference to consolidation book:**
```json
{
  "ia::result": {
    "key": "89",
    "id": "consol_book",
    "href": "/objects/consolidation/book/89"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/elimination-account
_List elimination accounts_

**Response 200 — List elimination accounts:**
```json
{
  "ia::result": [
    {
      "key": "12",
      "id": "12",
      "href": "/objects/consolidation/elimination-account/12"
    },
    {
      "key": "16",
      "id": "16",
      "href": "/objects/consolidation/elimination-account/16"
    },
    {
      "key": "18",
      "id": "18",
      "href": "/objects/consolidation/elimination-account/18"
    },
    {
      "key": "19",
      "id": "19",
      "href": "/objects/consolidation/elimination-account/19"
    },
    {
      "key": "20",
      "id": "20",
      "href": "/objects/consolidation/elimination-account/20"
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

## POST /objects/consolidation/elimination-account
_Create an elimination account_

**Request example — Create an elimination account:**
```json
{
  "consolidationBook": {
    "key": "49"
  },
  "glAccount": {
    "key": "10"
  }
}
```
**Response 201 — Reference to elimination account:**
```json
{
  "ia::result": {
    "id": "22",
    "key": "22",
    "href": "/objects/consolidation/elimination-account/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/elimination-account/{key}
_Get an elimination account_

**Response 200 — Get an elimination account:**
```json
{
  "ia::result": {
    "id": "22",
    "key": "22",
    "consolidationBook": {
      "id": "consol_book",
      "key": "49",
      "href": "/objects/consolidation/book/49"
    },
    "glAccount": {
      "key": "10",
      "id": "1001",
      "name": "CitiBank",
      "href": "/objects/general-ledger/account/10"
    },
    "audit": {
      "modifiedDateTime": "2025-04-13T09:19:58Z",
      "modifiedBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdDateTime": "2025-04-13T09:05:08Z",
      "createdBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/consolidation/elimination-account/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/consolidation/elimination-account/{key}
_Update an elimination account_

**Request example — Update an elimination account:**
```json
{
  "glAccount": {
    "key": "11"
  }
}
```
**Response 200 — Reference to elimination account:**
```json
{
  "ia::result": {
    "id": "22",
    "key": "22",
    "href": "/objects/consolidation/elimination-account/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/consolidation/elimination-account/{key}
_Delete an elimination account_


## GET /objects/consolidation/entity
_List consolidation entities_

**Response 200 — List consolidation entities:**
```json
{
  "ia::result": [
    {
      "key": "73",
      "id": "73",
      "href": "/objects/consolidation/entity/73"
    },
    {
      "key": "74",
      "id": "74",
      "href": "/objects/consolidation/entity/74"
    },
    {
      "key": "75",
      "id": "75",
      "href": "/objects/consolidation/entity/75"
    },
    {
      "key": "76",
      "id": "76",
      "href": "/objects/consolidation/entity/76"
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

## POST /objects/consolidation/entity
_Create a consolidation entity_

**Request example — Create a consolidation entity:**
```json
{
  "consolidationBook": {
    "key": "49"
  },
  "consolidationEntity": {
    "key": "3"
  }
}
```
**Response 201 — Reference to consolidation entity:**
```json
{
  "ia::result": {
    "id": "93",
    "key": "93",
    "href": "/objects/consolidation/entity/93"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/entity/{key}
_Get a consolidation entity_

**Response 200 — Get a consolidation entity:**
```json
{
  "ia::result": {
    "id": "74",
    "key": "74",
    "consolidationBook": {
      "id": "consol_book",
      "key": "49",
      "href": "/objects/consolidation/book/49"
    },
    "consolidationEntity": {
      "id": "2",
      "name": "India",
      "key": "2",
      "href": "/objects/company-config/entity/2"
    },
    "audit": {
      "modifiedDateTime": "2025-04-13T09:19:58Z",
      "modifiedBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdDateTime": "2025-04-13T09:05:08Z",
      "createdBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/consolidation/entity/74"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/consolidation/entity/{key}
_Update a consolidation entity_

**Request example — Update a consolidation entity:**
```json
{
  "consolidationEntity": {
    "key": "5"
  }
}
```
**Response 200 — Reference to consolidation entity:**
```json
{
  "ia::result": {
    "id": "74",
    "key": "74",
    "href": "/objects/consolidation/entity/74"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/consolidation/entity/{key}
_Delete a consolidation entity_


## GET /objects/consolidation/override-account
_List override accounts_

**Response 200 — List override accounts:**
```json
{
  "ia::result": [
    {
      "key": "35",
      "id": "35",
      "href": "/objects/consolidation/override-account/35"
    },
    {
      "key": "36",
      "id": "36",
      "href": "/objects/consolidation/override-account/36"
    },
    {
      "key": "37",
      "id": "37",
      "href": "/objects/consolidation/override-account/37"
    },
    {
      "key": "40",
      "id": "40",
      "href": "/objects/consolidation/override-account/40"
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

## POST /objects/consolidation/override-account
_Create an override account_

**Request example — Create an override account:**
```json
{
  "consolidationBook": {
    "key": "49"
  },
  "glAccount": {
    "key": "11"
  },
  "exchangeRate": {
    "rateType": "endingSpotRate",
    "rate": "Intacct daily rate"
  }
}
```
**Response 201 — Reference to override account:**
```json
{
  "ia::result": {
    "id": "40",
    "key": "40",
    "href": "/objects/consolidation/override-account/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/override-account/{key}
_Get an override account_

**Response 200 — Get an override account:**
```json
{
  "ia::result": {
    "id": "40",
    "key": "40",
    "consolidationBook": {
      "id": "consol_book",
      "key": "49",
      "href": "/objects/consolidation/book/49"
    },
    "glAccount": {
      "key": "11",
      "id": "1002",
      "name": "HSBC - GBP",
      "href": "/objects/general-ledger/account/11"
    },
    "exchangeRate": {
      "rateType": "endingSpotRate",
      "rate": "IDR",
      "useUntilPeriod": null
    },
    "audit": {
      "modifiedDateTime": "2025-04-13T09:19:58Z",
      "modifiedBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdDateTime": "2025-04-13T09:05:08Z",
      "createdBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/consolidation/override-account/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/consolidation/override-account/{key}
_Update an override account_

**Request example — Update an override account:**
```json
{
  "glAccount": {
    "key": "16"
  },
  "exchangeRate": {
    "rateType": "historicalRate",
    "rate": "MXN-Rate",
    "useUntilPeriod": "2025-01-31"
  }
}
```
**Response 200 — Reference to override account:**
```json
{
  "ia::result": {
    "id": "40",
    "key": "40",
    "href": "/objects/consolidation/override-account/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/consolidation/override-account/{key}
_Delete an override account_


## GET /objects/consolidation/ownership-entity
_List ownership entities_

**Response 200 — List ownership entities:**
```json
{
  "ia::result": [
    {
      "key": "32",
      "id": "32",
      "href": "/objects/consolidation/ownership-entity/32"
    },
    {
      "key": "33",
      "id": "33",
      "href": "/objects/consolidation/ownership-entity/33"
    },
    {
      "key": "34",
      "id": "34",
      "href": "/objects/consolidation/ownership-entity/34"
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

## GET /objects/consolidation/ownership-entity/{key}
_Get an ownership entity_

**Response 200 — Get an ownership entity:**
```json
{
  "ia::result": {
    "key": "86",
    "id": "86",
    "ownershipStructurePeriod": {
      "id": "45",
      "key": "45",
      "href": "/objects/consolidation/ownership-structure-period/45"
    },
    "parentEntity": {
      "key": "1",
      "id": "1",
      "name": "United States of America",
      "href": "/objects/company-config/entity/1"
    },
    "consolidationBook": {
      "multiCurrency": {
        "cumulativeTranslationAdjustment": {
          "netAssetGLAccount": "1000",
          "netIncomeGLAccount": "1000"
        },
        "translationMethod": {
          "balanceSheetTranslationMethod": "endingSpotRate",
          "incomeTranslationMethod": "weightedAverageRate"
        },
        "currency": "USD"
      },
      "elimination": {
        "entity": "USDE",
        "adjustmentGLAccount": "1000"
      },
      "key": "140",
      "id": "sage62",
      "description": "sage62",
      "href": "/objects/consolidation/book/140"
    },
    "audit": {
      "createdDateTime": "2025-07-28T10:15:10Z",
      "modifiedDateTime": "2025-04-26T18:30:42Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "ownershipSubsidiaryEntities": [
      {
        "key": "223",
        "id": "223",
        "ownershipEntity": {
          "id": "86",
          "key": "86",
          "href": "/objects/consolidation/ownership-entity/86"
        },
        "subsidiaryEntity": {
          "id": "2",
          "name": "India",
          "key": "2",
          "href": "/objects/company-config/entity/2"
        },
        "ownershipPercentage": 44,
        "consolidationMethod": "consolidation",
        "allocateSubsidiaryIncome": true,
        "nonControllingInterestGLAccounts": {
          "investmentInSubsidiaryGLAccount": {
            "key": "10",
            "id": "1001",
            "name": "CitiBank",
            "href": "/objects/general-ledger/account/10"
          },
          "subsidiaryRevenueGLAccount": {
            "key": "11",
            "id": "1002",
            "name": "HSBC - GBP",
            "href": "/objects/general-ledger/account/11"
          },
          "netIncomeAttributableToNCIGLAccount": {
            "key": "380",
            "id": "1203.01",
            "name": "Billed Accounts Receivable",
            "href": "/objects/general-ledger/account/380"
          },
          "equityAttributableToNCIGLAccount": {
            "key": "76",
            "id": "1280.25",
            "name": "Germany (India) - Inter Entity Receivable",
            "href": "/objects/general-ledger/account/76"
          },
          "contributedCapitalGLAccount": {
            "key": "354",
            "id": "7516",
            "name": "Edit & Delete < Account > - !@#$%^&*()",
            "href": "/objects/general-ledger/account/354"
          }
        },
        "audit": {
          "createdDateTime": "2025-07-28T10:15:10Z",
          "modifiedDateTime": "2025-05-17T10:15:13Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/consolidation/ownership-subsidiary-entity/223"
      }
    ],
    "href": "/objects/consolidation/ownership-entity/86"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/consolidation/ownership-entity/{key}
_Delete an ownership entity_


## GET /objects/consolidation/ownership-structure
_List ownership structures_

**Response 200 — List ownership structures:**
```json
{
  "ia::result": [
    {
      "key": "41",
      "id": "global_corporate_structure",
      "href": "/objects/consolidation/ownership-structure/41"
    },
    {
      "key": "25",
      "id": "holding_company_subsidiaries",
      "href": "/objects/consolidation/ownership-structure/25"
    },
    {
      "key": "28",
      "id": "group_consolidation_structure",
      "href": "/objects/consolidation/ownership-structure/28"
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

## POST /objects/consolidation/ownership-structure
_Create an ownership structure_

**Request example — Create an ownership structure:**
```json
{
  "id": "struct_US_holding_subsidiaries",
  "description": "Ownership structure for US holding company subsidiaries.",
  "status": "active",
  "elimination": {
    "enableInterEntityAutoElimination": true,
    "enableEliminationByAffiliateEntity": true
  },
  "accountingMethod": "accrual",
  "userDefinedBookForEquityMethod": {
    "id": "CE"
  }
}
```
**Response 201 — Reference to ownership structure:**
```json
{
  "ia::result": {
    "key": "49",
    "id": "struct_US_holding_subsidiaries",
    "href": "/objects/consolidation/ownership-structure/49"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/ownership-structure-period
_List ownership structure periods_

**Response 200 — List ownership structure periods:**
```json
{
  "ia::result": [
    {
      "key": "11",
      "id": "11",
      "href": "/objects/consolidation/ownership-structure-period/11"
    },
    {
      "key": "12",
      "id": "12",
      "href": "/objects/consolidation/ownership-structure-period/12"
    },
    {
      "key": "13",
      "id": "13",
      "href": "/objects/consolidation/ownership-structure-period/13"
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

## POST /objects/consolidation/ownership-structure-period
_Create an ownership structure period_

**Request example — Create an ownership structure period:**
```json
{
  "ownershipStructure": {
    "key": "45"
  },
  "fromPeriod": {
    "id": "Apr 2025"
  },
  "comment": "Time period from April 2025.",
  "state": "draft",
  "status": "active",
  "ownershipEntities": [
    {
      "parentEntity": {
        "key": "1"
      },
      "consolidationBook": {
        "elimination": {
          "adjustmentGLAccount": "1000",
          "entity": "USDE"
        },
        "multiCurrency": {
          "cumulativeTranslationAdjustment": {
            "netAssetGLAccount": "1000",
            "netIncomeGLAccount": "1000"
          },
          "translationMethod": {
            "balanceSheetTranslationMethod": "endingSpotRate",
            "incomeTranslationMethod": "weightedAverageRate"
          },
          "currency": "USD"
        },
        "description": "Consolidation book for company holdings.",
        "id": "conso_book_holdings"
      },
      "ownershipSubsidiaryEntities": [
        {
          "ownershipEntity": {
            "key": "151"
          },
          "subsidiaryEntity": {
            "key": "2"
          },
          "ownershipPercentage": 44,
          "consolidationMethod": "consolidation",
          "allocateSubsidiaryIncome": false,
          "nonControllingInterestGLAccounts": {
            "investmentInSubsidiaryGLAccount": {
              "key": "10"
            },
            "subsidiaryRevenueGLAccount": {
              "key": "11"
            },
            "netIncomeAttributableToNCIGLAccount": {
              "key": "380"
            },
            "equityAttributableToNCIGLAccount": {
              "key": "76"
            },
            "contributedCapitalGLAccount": {
              "key": "354"
            }
          }
        }
      ]
    }
  ]
}
```
**Response 201 — Reference to ownership structure period:**
```json
{
  "ia::result": {
    "key": "125",
    "id": "125",
    "href": "/objects/consolidation/ownership-structure-period/125"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/ownership-structure-period/{key}
_Get an ownership structure period_

**Response 200 — Get an ownership structure period:**
```json
{
  "ia::result": {
    "key": "125",
    "id": "125",
    "ownershipStructure": {
      "id": "level10",
      "key": "45",
      "href": "/objects/consolidation/ownership-structure/45"
    },
    "fromPeriod": {
      "id": "Apr 2025"
    },
    "comment": "Time period from April 2025.",
    "state": "draft",
    "status": "active",
    "audit": {
      "createdDateTime": "2025-06-30T11:11:26Z",
      "modifiedDateTime": "2025-06-30T11:11:26Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "ownershipEntities": [
      {
        "key": "195",
        "id": "195",
        "ownershipStructurePeriod": {
          "id": "125",
          "key": "125",
          "href": "/objects/consolidation/ownership-structure-period/125"
        },
        "parentEntity": {
          "key": "1",
          "id": "1",
          "name": "United States of America",
          "href": "/objects/company-config/entity/1"
        },
        "consolidationBook": {
          "multiCurrency": {
            "cumulativeTranslationAdjustment": {
              "netAssetGLAccount": "1000",
              "netIncomeGLAccount": "1000"
            },
            "translationMethod": {
              "balanceSheetTranslationMethod": "endingSpotRate",
              "incomeTranslationMethod": "weightedAverageRate"
            },
            "currency": "USD"
          },
          "elimination": {
            "entity": "USDE",
            "adjustmentGLAccount": "1000"
          },
          "key": "222",
          "id": "conso_book_holdings",
          "description": "Consolidation book for company holdings.",
          "href": "/objects/consolidation/book/222"
        },
        "audit": {
          "createdDateTime": "2025-06-30T11:11:26Z",
          "modifiedDateTime": "2025-06-30T11:11:26Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "ownershipSubsidiaryEntities": [
          {
            "key": "343",
            "id": "343",
            "ownershipEntity": {
              "id": "195",
              "key": "195",
              "href": "/objects/consolidation/ownership-entity/195"
            },
            "subsidiaryEntity": {
              "id": "2",
              "name": "India",
              "key": "2",
              "href": "/objects/company-config/entity/2"
            },
            "ownershipPercentage": 44,
            "consolidationMethod": "consolidation",
            "allocateSubsidiaryIncome": false,
            "nonControllingInterestGLAccounts": {
              "investmentInSubsidiaryGLAccount": {
                "key": "380",
                "id": "1203.01",
                "name": "Billed Accounts Receivable",
                "href": "/objects/general-ledger/account/380"
              },
              "subsidiaryRevenueGLAccount": {
                "key": "380",
                "id": "1203.01",
                "name": "Billed Accounts Receivable",
                "href": "/objects/general-ledger/account/380"
              },
              "netIncomeAttributableToNCIGLAccount": {
                "key": "380",
                "id": "1203.01",
                "name": "Billed Accounts Receivable",
                "href": "/objects/general-ledger/account/380"
              },
              "equityAttributableToNCIGLAccount": {
                "key": "76",
                "id": "1280.25",
                "name": "Germany (India) - Inter Entity Receivable",
                "href": "/objects/general-ledger/account/76"
              },
              "contributedCapitalGLAccount": {
                "key": "380",
                "id": "1203.01",
                "name": "Billed Accounts Receivable",
                "href": "/objects/general-ledger/account/380"
              }
            },
            "audit": {
              "createdDateTime": "2025-06-30T11:11:26Z",
              "modifiedDateTime": "2025-06-30T11:11:26Z",
              "createdBy": "1",
              "modifiedBy": "1"
            },
            "href": "/objects/consolidation/ownership-subsidiary-entity/343"
          }
        ],
        "href": "/objects/consolidation/ownership-entity/195"
      }
    ],
    "href": "/objects/consolidation/ownership-structure-period/125"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/consolidation/ownership-structure-period/{key}
_Update an ownership structure period_

**Request example — Update an ownership structure period:**
```json
{
  "ownershipStructure": {
    "key": "45"
  },
  "fromPeriod": {
    "id": "Mar 2025"
  },
  "comment": "Time period from March 2025.",
  "state": "draft",
  "status": "active",
  "ownershipEntities": [
    {
      "key": "194",
      "ownershipStructurePeriod": {
        "key": "124"
      },
      "parentEntity": {
        "key": "1"
      },
      "ownershipSubsidiaryEntities": [
        {
          "key": "342",
          "ownershipEntity": {
            "key": "194"
          },
          "subsidiaryEntity": {
            "key": "2"
          },
          "ownershipPercentage": 44,
          "consolidationMethod": "consolidation",
          "allocateSubsidiaryIncome": true,
          "nonControllingInterestGLAccounts": {
            "investmentInSubsidiaryGLAccount": {
              "key": "380"
            },
            "subsidiaryRevenueGLAccount": {
              "key": "76"
            },
            "netIncomeAttributableToNCIGLAccount": {
              "key": "380"
            },
            "equityAttributableToNCIGLAccount": {
              "key": "76"
            },
            "contributedCapitalGLAccount": {
              "key": "380"
            }
          }
        }
      ]
    }
  ]
}
```
**Response 200 — Reference to ownership structure period:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/consolidation/ownership-structure-period/124"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/consolidation/ownership-structure-period/{key}
_Delete an ownership structure period_


## GET /objects/consolidation/ownership-structure/{key}
_Get an ownership structure_

**Response 200 — Get an ownership structure:**
```json
{
  "ia::result": {
    "key": "43",
    "id": "struct_US_holdings",
    "description": "Ownership structure for US company holdings.",
    "status": "active",
    "elimination": {
      "enableInterEntityAutoElimination": true,
      "enableEliminationByAffiliateEntity": true
    },
    "accountingMethod": "accrual",
    "userDefinedBookForEquityMethod": {
      "id": "CE",
      "key": "4",
      "href": "/objects/general-ledger/user-defined-book/4"
    },
    "audit": {
      "createdDateTime": "2025-03-14T15:32:47Z",
      "modifiedDateTime": "2025-03-14T15:32:47Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "href": "/objects/consolidation/ownership-structure/43"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/consolidation/ownership-structure/{key}
_Delete an ownership structure_


## PATCH /objects/consolidation/ownership-structure/{key}
_Update an ownership structure_

**Request example — Update an ownership structure:**
```json
{
  "description": "Ownership structure for new US company holdings.",
  "status": "active"
}
```
**Response 200 — Reference to ownership structure:**
```json
{
  "ia::result": {
    "key": "16",
    "id": "igc",
    "href": "/objects/consolidation/ownership-structure/16"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/ownership-subsidiary-entity
_List ownership subsidiary entity_

**Response 200 — List ownership subsidiary entities:**
```json
{
  "ia::result": [
    {
      "key": "102",
      "id": "102",
      "href": "/objects/consolidation/ownership-subsidiary-entity/102"
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

## GET /objects/consolidation/ownership-subsidiary-entity/{key}
_Get an ownership subsidiary entity_

**Response 200 — Get an ownership subsidiary entity:**
```json
{
  "ia::result": {
    "key": "340",
    "id": "340",
    "ownershipEntity": {
      "id": "192",
      "key": "192",
      "href": "/objects/consolidation/ownership-entity/192"
    },
    "subsidiaryEntity": {
      "id": "05",
      "name": "NY Bldg",
      "key": "104",
      "href": "/objects/company-config/entity/104"
    },
    "ownershipPercentage": 44,
    "consolidationMethod": "consolidation",
    "allocateSubsidiaryIncome": false,
    "nonControllingInterestGLAccounts": {
      "investmentInSubsidiaryGLAccount": {
        "key": null,
        "id": null,
        "name": null
      },
      "subsidiaryRevenueGLAccount": {
        "key": null,
        "id": null,
        "name": null
      },
      "netIncomeAttributableToNCIGLAccount": {
        "key": "380",
        "id": "1203.01",
        "name": "Billed Accounts Receivable",
        "href": "/objects/general-ledger/account/380"
      },
      "equityAttributableToNCIGLAccount": {
        "key": "76",
        "id": "1280.25",
        "name": "Germany (India) - Inter Entity Receivable",
        "href": "/objects/general-ledger/account/76"
      },
      "contributedCapitalGLAccount": {
        "key": "380",
        "id": "1203.01",
        "name": "Billed Accounts Receivable",
        "href": "/objects/general-ledger/account/380"
      }
    },
    "audit": {
      "createdDateTime": "2025-06-27T17:13:08Z",
      "modifiedDateTime": "2025-06-27T17:13:08Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "href": "/objects/consolidation/ownership-subsidiary-entity/340"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/consolidation/ownership-subsidiary-entity/{key}
_Delete an ownership subsidiary entity_


## GET /objects/consolidation/run-status
_List consolidation run statuses_

**Response 200 — List consolidation run statuses:**
```json
{
  "ia::result": [
    {
      "key": "22",
      "id": "22",
      "href": "/objects/consolidation/run-status/22"
    },
    {
      "key": "53",
      "id": "53",
      "href": "/objects/consolidation/run-status/53"
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

## GET /objects/consolidation/run-status/{key}
_Get a consolidation run-status_

**Response 200 — Get a consolidation run status:**
```json
{
  "ia::result": {
    "id": "78291",
    "key": "78291",
    "book": {
      "id": "CASE-1",
      "key": "373",
      "href": "/objects/consolidation/book/373"
    },
    "entity": {
      "key": "1",
      "id": "1",
      "name": "United States of America",
      "href": "/objects/company-config/entity/140"
    },
    "period": {
      "key": "600",
      "id": "Jan 2025",
      "href": "/objects/consolidation/time-period/600"
    },
    "consolidationDateTime": "2025-06-04T16:06:22Z",
    "runBy": {
      "key": "1",
      "id": "Admin",
      "href": "/objects/company-config/user/1"
    },
    "exchangeRate": {
      "weightedAverageRate": "71.311800000000",
      "endingSpotRate": "71.585300000000"
    },
    "status": "background",
    "statusMessage": "Offline consolidation in progress",
    "ownershipStructure": {
      "key": "44",
      "id": "struct_US_holdings",
      "description": "Ownership structure for US company holdings.",
      "href": "/objects/consolidation/ownership-structure/44"
    },
    "href": "/objects/consolidation/run-status/70"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/consolidation/time-period
_List time periods_

**Response 200 — List consolidation time periods:**
```json
{
  "ia::result": [
    {
      "key": "860",
      "id": "Sep 2041",
      "href": "/objects/consolidation/time-period/860"
    },
    {
      "key": "861",
      "id": "Oct 2041",
      "href": "/objects/consolidation/time-period/861"
    },
    {
      "key": "862",
      "id": "Nov 2041",
      "href": "/objects/consolidation/time-period/862"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 3,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/consolidation/time-period/{key}
_Get a consolidation time period_

**Response 200 — Get a consolidation time period:**
```json
{
  "ia::result": {
    "id": "Sep 2025",
    "key": "620",
    "periodName": "Sep 2025",
    "startDate": "2025-09-01",
    "endDate": "2025-09-30",
    "href": "/objects/consolidation/time-period/620"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/consolidation/book/consolidate
_Consolidate a book for a specified period_

**Request example — Consolidate a book for a new period:**
```json
{
  "consolidationBook": {
    "id": "consolBook"
  },
  "timePeriod": {
    "id": "Mar 2025"
  },
  "notificationEmail": "john.smith@TechSolutions.com"
}
```
**Request example — Consolidate a book for a new period online:**
```json
{
  "consolidationBook": {
    "id": "consolBook"
  },
  "timePeriod": {
    "id": "Apr 2025"
  },
  "runOffline": false
}
```
**Request example — Consolidate a book for a new period with custom rate:**
```json
{
  "consolidationBook": {
    "id": "consolBook"
  },
  "timePeriod": {
    "id": "May 2025"
  },
  "notificationEmail": "john.smith@TechSolutions.com",
  "entities": [
    {
      "entity": {
        "id": "US"
      },
      "endingSpotRate": "1.3303",
      "weightedAverageRate": "1.3534"
    },
    {
      "entity": {
        "id": "IN"
      },
      "endingSpotRate": "0.0199",
      "weightedAverageRate": "0.02008"
    },
    {
      "entity": {
        "id": "USDE"
      },
      "endingSpotRate": "1",
      "weightedAverageRate": "1"
    }
  ]
}
```
**Request example — Re-consolidate a book for the last period with net changes:**
```json
{
  "consolidationBook": {
    "id": "consolBook"
  },
  "timePeriod": {
    "id": "May 2025"
  },
  "notificationEmail": "john.smith@TechSolutions.com"
}
```
**Request example — Delete and re-consolidate a book for the last period:**
```json
{
  "consolidationBook": {
    "id": "consolBook"
  },
  "timePeriod": {
    "id": "May 2025"
  },
  "updateNetChanges": false,
  "notificationEmail": "john.smith@TechSolutions.com"
}
```
**Request example — Re-consolidate a book for a past period and update all subsequent periods:**
```json
{
  "consolidationBook": {
    "id": "consolBook"
  },
  "timePeriod": {
    "id": "Mar 2025"
  },
  "updateSubsequentPeriods": true,
  "notificationEmail": "john.smith@TechSolutions.com"
}
```
**Request example — Re-consolidate a book for a past period with net changes and delete all the subsequent period:**
```json
{
  "consolidationBook": {
    "id": "consolBook"
  },
  "timePeriod": {
    "id": "Mar 2025"
  },
  "notificationEmail": "john.smith@TechSolutions.com"
}
```
**Response 200 — Consolidate book online:**
```json
{
  "ia::result": {
    "status": "success",
    "message": "The consolidation completed successfully."
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Consolidate book offline:**
```json
{
  "ia::result": {
    "status": "success",
    "message": "A job has been queued to run an offline consolidation. Go to Company > Offline job queue to view the job status."
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/consolidation/ownership-structure/consolidate
_Consolidate an ownership structure_

**Request example — Consolidate an ownership structure:**
```json
{
  "ownershipStructure": {
    "id": "consolOwnershipStructure"
  },
  "timePeriod": {
    "id": "Apr 2025"
  },
  "notificationEmail": "tom.johnson@techsoma.com"
}
```
**Request example — Consolidate and override exchange rates for an ownership structure entities:**
```json
{
  "ownershipStructure": {
    "id": "consolOwnershipStructure"
  },
  "timePeriod": {
    "id": "Jan 2025"
  },
  "notificationEmail": "tom.johnson@techsoma.com",
  "overrideExchangeRate": [
    {
      "consolidationBook": {
        "id": "us_book"
      },
      "consolidationEntities": [
        {
          "entity": {
            "id": "USA"
          },
          "endingSpotRate": "1",
          "weightedAverageRate": "1"
        },
        {
          "entity": {
            "key": "IND"
          },
          "endingSpotRate": "0.01151",
          "weightedAverageRate": "0.01149"
        },
        {
          "entity": {
            "id": "UK"
          },
          "endingSpotRate": "1.2607",
          "weightedAverageRate": "1.2467"
        },
        {
          "entity": {
            "id": "USDE"
          },
          "endingSpotRate": "1",
          "weightedAverageRate": "1"
        }
      ]
    },
    {
      "consolidationBook": {
        "id": "ind_book"
      },
      "consolidationEntities": [
        {
          "entity": {
            "id": "IND"
          },
          "endingSpotRate": "0.01151",
          "weightedAverageRate": "0.01149"
        },
        {
          "entity": {
            "id": "AUS"
          },
          "endingSpotRate": "0.6352",
          "weightedAverageRate": "0.6279"
        },
        {
          "entity": {
            "id": "INDE"
          },
          "endingSpotRate": "1",
          "weightedAverageRate": "1"
        }
      ]
    }
  ]
}
```
**Response 200 — Consolidate an ownership structure:**
```json
{
  "ia::result": {
    "status": "success",
    "message": "A job has been queued to run an offline consolidation. Go to Company > Offline job queue to view the job status."
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
