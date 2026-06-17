# Fixed Assets Management

## GET /objects/fixed-assets/asset
_List assets_

**Response 200 — List assets:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "CE_ASSET-2",
      "href": "/objects/fixed-assets/asset/2"
    },
    {
      "key": "3",
      "id": "CE_ASSET-3",
      "href": "/objects/fixed-assets/asset/3"
    },
    {
      "key": "4",
      "id": "VEH_ASSET-1",
      "href": "/objects/fixed-assets/asset/4"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0
  }
}
```

## POST /objects/fixed-assets/asset
_Create an asset_

**Request example — Create an asset:**
```json
{
  "id": "CE_ASSET-1",
  "name": "Laptop",
  "serialNumber": "CE_ASSET-1",
  "assetTag": "ASSET_TAG-0001",
  "state": "inService",
  "inServiceDate": "2021-03-15",
  "status": "active",
  "assetCost": "5000",
  "salvageValue": "200",
  "acquisitionDate": "2020-04-22",
  "isDepreciable": true,
  "description": "Lenovo ThinkPad",
  "dimensions": {
    "location": {
      "key": "1"
    }
  },
  "classification": {
    "key": "3"
  },
  "allocation": {
    "key": "1"
  },
  "depreciationRules": [
    {
      "postingRule": {
        "key": "1"
      },
      "depreciationMethod": {
        "key": "-1"
      },
      "usefulLife": 5
    }
  ]
}
```
**Response 201 — New asset:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "CE_ASSET-2",
    "href": "/objects/fixed-assets/asset/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/asset-classification
_List asset classifications_

**Response 200 — List asset classifications:**
```json
{
  "ia::result": [
    {
      "key": "101",
      "id": "Classification Id 101",
      "href": "/objects/fixed-assets/asset-classification/101"
    },
    {
      "key": "102",
      "id": "Classification Id 102",
      "href": "/objects/fixed-assets/asset-classification/102"
    },
    {
      "key": "103",
      "id": "Classification Id 103",
      "href": "/objects/fixed-assets/asset-classification/103"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0
  }
}
```

## POST /objects/fixed-assets/asset-classification
_Create an asset classification_

**Request example — Create an asset classification:**
```json
{
  "name": "Furniture & Fixtures",
  "id": "Classification Id 100",
  "status": "active",
  "assetGLAccount": {
    "key": "29",
    "id": "1014",
    "title": "Shared Banks"
  },
  "accumulatedDepreciationGLAccount": {
    "key": "9",
    "id": "1000",
    "title": "Bank of America A/c."
  },
  "depreciationExpenseGLAccount": {
    "key": "194",
    "id": "4000",
    "title": "Sales"
  },
  "disposalGLAccount": {
    "key": "101",
    "id": "1904",
    "title": "Computer Equipment"
  },
  "cipGLAccount": {
    "key": "207",
    "id": "5001",
    "title": "Construction"
  },
  "provisionDerogatoryGLAccount": {
    "name": "Provision Derogatory",
    "id": "2131",
    "key": "22"
  },
  "accumulatedProvisionDerogatoryGLAccount": {
    "name": "Accumulated Provision Derogatory",
    "id": "3676",
    "key": "13"
  },
  "reversalDerogatoryGLAccount": {
    "name": "Reversal Derogatory",
    "id": "9494",
    "key": "14"
  },
  "depreciationRules": [
    {
      "postingRule": {
        "key": "1"
      },
      "depreciationMethod": {
        "key": "-1"
      },
      "usefulLife": 60
    },
    {
      "postingRule": {
        "key": "2"
      },
      "depreciationMethod": {
        "key": "-2"
      },
      "usefulLife": 12
    }
  ]
}
```
**Response 201 — New asset classification:**
```json
{
  "ia::result": {
    "key": "981",
    "id": "Classification Id 100",
    "href": "/objects/fixed-assets/asset-classification/981"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/asset-classification/{key}
_Get an asset classification_

**Response 200 — Details of the asset classification:**
```json
{
  "ia::result": {
    "name": "Furniture & Fixtures",
    "id": "Classification Id 100",
    "key": "100",
    "status": "active",
    "assetGLAccount": {
      "key": "29",
      "id": "1014",
      "title": "Shared Banks"
    },
    "accumulatedDepreciationGLAccount": {
      "key": "9",
      "id": "1000",
      "title": "Bank of America A/c."
    },
    "depreciationExpenseGLAccount": {
      "key": "194",
      "id": "4000",
      "title": "Sales"
    },
    "disposalGLAccount": {
      "key": "101",
      "id": "1904",
      "title": "Computer Equipment"
    },
    "cipGLAccount": {
      "key": "207",
      "id": "5001",
      "title": "Construction"
    },
    "provisionDerogatoryGLAccount": {
      "name": "Provision Derogatory",
      "id": "2131",
      "key": "22"
    },
    "accumulatedProvisionDerogatoryGLAccount": {
      "name": "Accumulated Provision Derogatory",
      "id": "3676",
      "key": "13"
    },
    "reversalDerogatoryGLAccount": {
      "name": "Reversal Derogatory",
      "id": "9494",
      "key": "14"
    },
    "depreciationRules": [
      {
        "depreciationMethod": {
          "name": "Straight line",
          "id": "SL",
          "key": "-1"
        },
        "journal": {
          "id": "GAAP",
          "title": "GAAP Accrual Book",
          "key": "45"
        },
        "classification": {
          "id": "Classification Id 100",
          "key": "100"
        },
        "id": "818",
        "key": "818",
        "usefulLife": 60,
        "coefficient": "1.25"
      },
      {
        "depreciationMethod": {
          "name": "200% declining balance",
          "id": "200DB",
          "key": "-2"
        },
        "journal": {
          "id": "TAX",
          "title": "TAX Accrual Book",
          "key": "46"
        },
        "classification": {
          "id": "Classification Id 100",
          "key": "100"
        },
        "id": "824",
        "key": "824",
        "usefulLife": 12,
        "coefficient": "1.25"
      }
    ]
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/fixed-assets/asset-classification/{key}
_Update an asset classification_

**Request example — Update an asset classification:**
```json
{
  "name": "Updated Furniture",
  "id": "Classification Id 100",
  "accumulatedDepreciationGLAccount": {
    "key": "10"
  },
  "depreciationExpenseGLAccount": {
    "key": "11"
  },
  "provisionDerogatoryGLAccount": {
    "key": "12"
  },
  "accumulatedProvisionDerogatoryGLAccount": {
    "key": "13"
  },
  "reversalDerogatoryGLAccount": {
    "key": "14"
  }
}
```
**Response 200 — Updated asset classification:**
```json
{
  "ia::result": {
    "key": "981",
    "id": "Classification Id 100",
    "href": "/objects/fixed-assets/asset-classification/981"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/fixed-assets/asset-classification/{key}
_Delete an asset classification_


## GET /objects/fixed-assets/asset-depreciation-rule
_List asset depreciation rules_

**Response 200 — List asset depreciation rules:**
```json
{
  "ia::result": [
    {
      "id": "80",
      "key": "80",
      "href": "/objects/fixed-assets/asset-depreciation-rule/80"
    },
    {
      "id": "81",
      "key": "81",
      "href": "/objects/fixed-assets/asset-depreciation-rule/81"
    },
    {
      "id": "82",
      "key": "82",
      "href": "/objects/fixed-assets/asset-depreciation-rule/82"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0
  }
}
```

## POST /objects/fixed-assets/asset-depreciation-rule
_Create an asset depreciation rule_

**Request example — Create an asset depreciation rule:**
```json
{
  "key": "2",
  "id": "2",
  "depreciationMethod": {
    "name": "Straight line",
    "id": "SL",
    "key": "-1"
  },
  "postingRule": {
    "key": "1",
    "id": "1"
  },
  "asset": {
    "key": "2",
    "id": "CE_ASSET-1"
  },
  "usefulLife": 5
}
```
**Response 201 — New asset-depreciation-rule:**
```json
{
  "ia::result": {
    "key": "871",
    "id": "871",
    "href": "/objects/fixed-assets/asset-depreciation-rule/871"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/asset-depreciation-rule/{key}
_Get an asset depreciation rule_

**Response 200 — List details of the asset depreciation rule:**
```json
{
  "ia::result": {
    "depreciationMethod": {
      "name": "Straight line",
      "id": "SL",
      "key": "-1"
    },
    "asset": {
      "name": "Asset Name _~!@#$%^*()_+=-`1682315965",
      "id": "Asset Id 1682315965",
      "key": "860"
    },
    "depreciationSchedule": {
      "key": "387"
    },
    "postingRule": {
      "name": "NAME 1",
      "id": "ID1",
      "key": "1"
    },
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2023-04-24T05:59:27Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2023-04-24T05:59:27Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      }
    },
    "id": "1009",
    "key": "1009",
    "historicalAccumulatedDepreciationAmount": "100.00",
    "usefulLife": 5,
    "coefficient": "1.25"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/fixed-assets/asset-depreciation-rule/{key}
_Update an asset depreciation rule_

**Request example — Update an asset depreciation rule:**
```json
{
  "depreciationMethod": {
    "id": "DB",
    "key": "-2"
  }
}
```
**Response 200 — Updated asset depreciation rule:**
```json
{
  "ia::result": {
    "key": "1021",
    "id": "1021",
    "href": "/objects/fixed-assets/asset-depreciation-rule/1021"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/fixed-assets/asset-depreciation-rule/{key}
_Delete an asset depreciation rule_


## GET /objects/fixed-assets/asset/{key}
_Get an asset_

**Response 200 — Details of the asset:**
```json
{
  "ia::result": {
    "accumulatedDepreciationGLAccount": {
      "name": "Accumulated Depreciation",
      "id": "1901",
      "title": "Accumulated Depreciation",
      "key": "98"
    },
    "depreciationExpenseGLAccount": {
      "name": "Depreciation Expense",
      "id": "6350",
      "key": "270"
    },
    "assetGLAccount": {
      "name": "Computer Equipment",
      "id": "1500",
      "key": "93"
    },
    "provisionDerogatoryGLAccount": {
      "name": "Provision Derogatory",
      "id": "2131",
      "key": "22"
    },
    "accumulatedProvisionDerogatoryGLAccount": {
      "name": "Accumulated Provision Derogatory",
      "id": "3676",
      "key": "13"
    },
    "reversalDerogatoryGLAccount": {
      "name": "Reversal Derogatory",
      "id": "9494",
      "key": "14"
    },
    "classification": {
      "name": "Computer Equipment",
      "id": "CE-1",
      "key": "3"
    },
    "depreciationRules": [
      {
        "depreciationMethod": {
          "name": "Straight line",
          "id": "SL",
          "key": "-1"
        },
        "asset": {
          "name": "Laptop",
          "id": "CE_ASSET-1",
          "key": "2"
        },
        "depreciationSchedule": {
          "key": "1"
        },
        "postingRule": {
          "name": "NAME 3",
          "id": "ID3",
          "key": "3"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2022-11-02T05:12:15Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2022-11-02T05:12:19Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "id": "9",
        "key": "9",
        "historicalAccumulatedDepreciationAmount": "110.50",
        "usefulLife": 36,
        "coefficient": "1.25"
      },
      {
        "depreciationMethod": {
          "name": "Straight line",
          "id": "SL",
          "key": "-1"
        },
        "asset": {
          "name": "Laptop",
          "id": "CE_ASSET-1",
          "key": "2"
        },
        "depreciationSchedule": {
          "key": "2"
        },
        "postingRule": {
          "name": "NAME 2",
          "id": "ID2",
          "key": "2"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2022-11-02T05:12:15Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2022-11-02T05:12:19Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "id": "10",
        "key": "10",
        "historicalAccumulatedDepreciationAmount": "0",
        "usefulLife": 3,
        "coefficient": "1.25"
      }
    ],
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2022-11-02T05:12:15Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2022-11-02T05:12:19Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      }
    },
    "dimensions": {
      "item": {
        "name": "PC Computer",
        "id": "1",
        "key": "1"
      },
      "task": {
        "name": "Project coordination",
        "id": "01-041",
        "key": "8"
      },
      "vendor": {
        "name": "1099 Int",
        "id": "1099 Int",
        "key": "43"
      },
      "project": {
        "name": "Client Services - Power Aerospace Materials",
        "id": "8",
        "key": "8"
      },
      "location": {
        "name": "United States of America",
        "id": "1",
        "key": "1"
      },
      "department": {
        "name": "Engineering",
        "id": "3",
        "key": "3"
      },
      "employee": {
        "id": "1",
        "key": "1"
      },
      "warehouse": {
        "name": "WH01 Name",
        "id": "WH01",
        "key": "1"
      },
      "class": {
        "name": "Heath Care",
        "id": "3",
        "key": "1"
      },
      "customer": {
        "name": "Power Aerospace Materials",
        "id": "1",
        "key": "1"
      },
      "costType": {
        "name": "Labor",
        "id": "L",
        "key": "8"
      },
      "affiliateEntity": {
        "name": "United States of America",
        "id": "1",
        "key": "1"
      }
    },
    "splitParent": {
      "key": "1",
      "id": "1",
      "name": "Parent Asset (ROOT/USA)",
      "splitDate": "2022-04-1",
      "href": "/objects/fixed-assets/asset/1"
    },
    "splitDate": "2022-04-20",
    "splitAssets": [
      {
        "key": "626",
        "id": "ADJDEC0755",
        "name": "Child 17",
        "assetCost": "400",
        "salvageValue": "0",
        "href": "/objects/fixed-assets/asset/626"
      },
      {
        "key": "627",
        "id": "ADJDEC0756",
        "name": "Child 18",
        "assetCost": "200",
        "salvageValue": "0",
        "href": "/objects/fixed-assets/asset/627"
      }
    ],
    "acquisitionDate": "2020-01-01",
    "capitalizationDate": "2020-01-01",
    "assetCost": "3000",
    "quantity": 1,
    "serialNumber": "CE_ASSET-1",
    "assetTag": "ASSET_TAG-0001",
    "depreciableCost": "2700",
    "description": "Lenovo thinkpad",
    "type": "tangible",
    "name": "Laptop",
    "salvageValue": "300",
    "inServiceDate": "2020-01-01",
    "id": "CE_ASSET-1",
    "state": "inService",
    "isDepreciable": true,
    "key": "2",
    "status": "active"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/fixed-assets/asset/{key}
_Update an asset_

**Request example — Update an asset:**
```json
{
  "state": "inService",
  "inServiceDate": "2021-12-28"
}
```
**Response 200 — Updated asset:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "CE_ASSET-2",
    "href": "/objects/fixed-assets/asset/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/fixed-assets/asset/{key}
_Delete an asset_


## GET /objects/fixed-assets/classification-depreciation-rule
_List classification depreciation rules_

**Response 200 — List classification depreciation rules:**
```json
{
  "ia::result": [
    {
      "key": "81",
      "id": "81",
      "href": "objects/fixed-assets/classification-depreciation-rule/81"
    },
    {
      "key": "82",
      "id": "82",
      "href": "objects/fixed-assets/classification-depreciation-rule/82"
    },
    {
      "key": "83",
      "id": "83",
      "href": "objects/fixed-assets/classification-depreciation-rule/83"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0
  }
}
```

## POST /objects/fixed-assets/classification-depreciation-rule
_Create a classification depreciation rule_

**Request example — Create a classification depreciation rule:**
```json
{
  "id": "818",
  "journal": {
    "key": "45"
  },
  "depreciationMethod": {
    "key": "-1"
  },
  "classification": {
    "key": "100"
  },
  "usefulLife": 60
}
```
**Response 201 — New classification depreciation rule:**
```json
{
  "ia::result": {
    "key": "818",
    "id": "818",
    "href": "/objects/fixed-assets/classification-depreciation-rule/818"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/classification-depreciation-rule/{key}
_Get a classification depreciation rule_

**Response 200 — List details of the classification depreciation rule:**
```json
{
  "ia::result": {
    "depreciationMethod": {
      "name": "Straight line",
      "id": "SL",
      "key": "-1"
    },
    "journal": {
      "id": "GAAP",
      "title": "GAAP Accrual Book",
      "key": "45"
    },
    "classification": {
      "id": "Classification Id 100",
      "key": "100"
    },
    "id": "818",
    "key": "818",
    "usefulLife": 60,
    "coefficient": "1.25"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/fixed-assets/classification-depreciation-rule/{key}
_Update a classification depreciation rule_

**Request example — Update a classification depreciation rule:**
```json
{
  "depreciationMethod": {
    "id": "DB",
    "key": "-2"
  },
  "classification": {
    "key": "1023"
  },
  "usefulLife": 20
}
```
**Response 200 — Updated classification depreciation rule:**
```json
{
  "ia::result": {
    "key": "818",
    "id": "818",
    "href": "/objects/fixed-assets/classification-depreciation-rule/818"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/fixed-assets/classification-depreciation-rule/{key}
_Delete a classification depreciation rule_


## GET /objects/fixed-assets/depreciation-method
_List depreciation methods_

**Response 200 — List depreciation methods:**
```json
{
  "ia::result": [
    {
      "id": "CDB",
      "key": "-6",
      "href": "/objects/fixed-assets/depreciation-method/-6"
    },
    {
      "id": "CDBT",
      "key": "-5",
      "href": "/objects/fixed-assets/depreciation-method/-5"
    },
    {
      "id": "DR",
      "key": "-4",
      "href": "/objects/fixed-assets/depreciation-method/-4"
    },
    {
      "id": "150DB",
      "key": "-3",
      "href": "/objects/fixed-assets/depreciation-method/-3"
    },
    {
      "id": "200DB",
      "key": "-2",
      "href": "/objects/fixed-assets/depreciation-method/-2"
    },
    {
      "id": "SL",
      "key": "-1",
      "href": "/objects/fixed-assets/depreciation-method/-1"
    }
  ],
  "ia::meta": {
    "totalCount": 6,
    "totalSuccess": 6,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/depreciation-method/{key}
_Get a depreciation method_

**Response 200 — Details of the depreciation method:**
```json
{
  "ia::result": {
    "name": "Straight line",
    "id": "SL",
    "key": "-1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/depreciation-schedule
_List depreciation schedules_

**Response 200 — List depreciation schedules:**
```json
{
  "ia::result": [
    {
      "state": "inProgress",
      "key": "26",
      "href": "/objects/fixed-assets/depreciation-schedule/26"
    },
    {
      "state": "inProgress",
      "key": "27",
      "href": "/objects/fixed-assets/depreciation-schedule/27"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/depreciation-schedule-entry
_List depreciation schedule entries_

**Response 200 — List Depreciation Schedule Entries:**
```json
{
  "ia::result": [
    {
      "id": "11",
      "key": "11",
      "href": "/objects/fixed-assets/depreciation-schedule-entry/11"
    },
    {
      "id": "12",
      "key": "12",
      "href": "/objects/fixed-assets/depreciation-schedule-entry/12"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/depreciation-schedule-entry/{key}
_Get a depreciation schedule entry_

**Response 200 — Details of the depreciation schedule entry:**
```json
{
  "ia::result": {
    "depreciationSchedule": {
      "id": "389",
      "key": "389"
    },
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2023-04-24T07:58:45Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2023-04-24T07:58:45Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      }
    },
    "depreciationAmount": "960",
    "decliningAmount": "960",
    "derogatoryProvisionAmount": "0",
    "derogatoryReversalAmount": "1.11",
    "derogatoryBalance": "12",
    "period": 1,
    "parent": {
      "key": "1",
      "id": "1",
      "href": "/objects/fixed-assets/depreciation-schedule-entry/1"
    },
    "id": "5564",
    "scheduledPostingDate": "2021-12-31",
    "actualPostingDate": "2022-01-05",
    "state": "notPosted",
    "key": "5564"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/depreciation-schedule/{key}
_Get a depreciation schedule_

**Response 200 — Details of the depreciation schedule:**
```json
{
  "ia::result": {
    "asset": {
      "assetCost": "200",
      "name": "Asset Name _~!@#$%^*()_+=-`1682323123",
      "salvageValue": "10",
      "id": "ADJDEC1277",
      "key": "16"
    },
    "assetDepreciationRule": {
      "useSalvageValue": true,
      "id": "23",
      "key": "23"
    },
    "depreciationScheduleEntries": [
      {
        "depreciationSchedule": {
          "id": "14",
          "key": "14"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2025-01-21T05:27:36Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2025-01-21T05:27:53Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "period": 1,
        "depreciationAmount": "71.25",
        "id": "84",
        "state": "canceled",
        "scheduledPostingDate": "2025-12-31",
        "key": "84"
      },
      {
        "depreciationSchedule": {
          "id": "14",
          "key": "14"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2025-01-21T05:27:36Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2025-01-21T05:27:53Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "period": 2,
        "depreciationAmount": "44.53",
        "id": "85",
        "state": "canceled",
        "scheduledPostingDate": "2026-12-31",
        "key": "85"
      },
      {
        "depreciationSchedule": {
          "id": "14",
          "key": "14"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2025-01-21T05:27:36Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2025-01-21T05:27:53Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "period": 3,
        "depreciationAmount": "27.83",
        "id": "86",
        "state": "canceled",
        "scheduledPostingDate": "2027-12-31",
        "key": "86"
      },
      {
        "depreciationSchedule": {
          "id": "14",
          "key": "14"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2025-01-21T05:27:36Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2025-01-21T05:27:53Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "period": 4,
        "depreciationAmount": "46.39",
        "id": "87",
        "state": "canceled",
        "scheduledPostingDate": "2028-12-31",
        "key": "87"
      }
    ],
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2025-01-21T05:27:36Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2025-01-21T05:27:53Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      }
    },
    "depreciableCost": "190",
    "historicalAccumulatedDepreciationAmount": "0",
    "id": "14",
    "state": "canceled",
    "key": "14",
    "totalAccumulatedDepreciationAmount": "0",
    "remainingDepreciationAmount": "0"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/disposal
_List disposals_

**Response 200 — List disposals:**
```json
{
  "ia::result": [
    {
      "id": "80",
      "key": "80",
      "href": "/objects/fixed-assets/disposal/80"
    },
    {
      "id": "81",
      "key": "81",
      "href": "/objects/fixed-assets/disposal/81"
    },
    {
      "id": "82",
      "key": "82",
      "href": "/objects/fixed-assets/disposal/82"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/disposal-depreciation-schedule-map
_List disposal depreciation schedule maps_

**Response 200 — List Disposal Depreciation Schedule Maps:**
```json
{
  "ia::result": [
    {
      "id": "80",
      "key": "80",
      "href": "/objects/fixed-assets/disposal-depreciation-schedule-map/80"
    },
    {
      "id": "81",
      "key": "81",
      "href": "/objects/fixed-assets/disposal-depreciation-schedule-map/81"
    },
    {
      "id": "82",
      "key": "82",
      "href": "/objects/fixed-assets/disposal-depreciation-schedule-map/82"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/disposal-depreciation-schedule-map/{key}
_Get a disposal depreciation schedule map_

**Response 200 — List details of the disposal depreciation schedule map:**
```json
{
  "ia::result": {
    "partialAccumulatedDepreciationAmount": "100.00",
    "partialRemainingDepreciationAmount": "1425.00",
    "gainLossAmount": "300.00",
    "disposal": {
      "key": "387",
      "id": "387",
      "isPartial": false,
      "disposalAmount": "500.00",
      "disposalDate": "2025-08-08",
      "disposalType": "sale",
      "salePrice": "500.00",
      "comments": "Disposal comment",
      "href": "/objects/fixed-assets/disposal/387"
    },
    "disposalJournalEntry": {
      "key": "387",
      "id": "387",
      "txnNumber": "1009",
      "href": "/objects/general-ledger/journal-entry/387"
    },
    "depreciationSchedule": {
      "key": "387",
      "id": "387",
      "href": "/objects/fixed-assets/depreciation-schedule/387"
    },
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2023-04-24T05:59:27Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2023-04-24T05:59:27Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      }
    },
    "id": "1009",
    "key": "1009"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/disposal/{key}
_Get a disposal_

**Response 200 — Details of the disposal:**
```json
{
  "ia::result": {
    "asset": {
      "name": "Laptop",
      "id": "ADJDEC0207",
      "key": "2140"
    },
    "isPartial": false,
    "disposalAmount": "500",
    "disposalDate": "2023-04-24",
    "disposalType": "sale",
    "salePrice": "500",
    "comments": "Disposal comments",
    "gainLossAmount": "0.00",
    "disposalDepreciationSchedules": [
      {
        "disposalJournalEntry": {
          "key": "1009",
          "id": "1009",
          "txnNumber": 1,
          "href": "/objects/general-ledger/journal-entry/1009"
        },
        "key": "2053",
        "id": "2053",
        "depreciationRuleKey": "3",
        "gainLossAmount": "0.00",
        "href": "/objects/fixed-assets/disposal-depreciation-schedule-map/2053",
        "asset": {
          "key": "21",
          "id": "21",
          "href": "/objects/fixed-assets/asset/21"
        },
        "disposal": {
          "key": "1009",
          "id": "1009",
          "disposalDate": "2023-04-24",
          "disposalType": "sale",
          "disposalAmount": "500",
          "salePrice": "500",
          "comments": "Disposal comments",
          "href": "/objects/fixed-assets/disposal/1009"
        },
        "depreciationSchedule": {
          "key": "1046",
          "id": "1046",
          "href": "/objects/fixed-assets/depreciation-schedule/1046"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2022-11-02T05:12:15Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2022-11-02T05:12:19Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        }
      }
    ],
    "disposalJournalEntry": {
      "key": "1009",
      "id": "1009",
      "txnNumber": 1,
      "href": "/objects/general-ledger/journal-entry/1009"
    },
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2023-04-24T05:59:27Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2023-04-24T05:59:27Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      }
    },
    "id": "1009",
    "key": "1009"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/fixed-assets/disposal/{key}
_Delete a partial disposal_


## GET /objects/fixed-assets/setup
_List setups_

**Response 200 — List setups:**
```json
{
  "ia::result": {
    "id": "1",
    "key": "1",
    "href": "/objects/fixed-assets/setup/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /objects/fixed-assets/setup
_Create a setup_

**Request example — Create a setup:**
```json
{
  "enableAutoPosting": false,
  "enableCIP": false,
  "enableDepreciationSummary": false,
  "journal": {
    "key": "46"
  },
  "setupPostingRules": [
    {
      "journal": {
        "key": "46"
      },
      "usefulLifeUnits": "months",
      "convention": "fullMonth",
      "isTax": true,
      "useSalvageValue": false,
      "name": "Tax Accrual Book"
    },
    {
      "journal": {
        "key": "43"
      },
      "usefulLifeUnits": "years",
      "convention": "halfYear",
      "isTax": false
    }
  ]
}
```
**Response 201 — New setup:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "ID1",
    "href": "/objects/fixed-assets/setup/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/setup-posting-rule
_List setup posting rules_

**Response 200 — List of setup posting rules:**
```json
{
  "ia::result": [
    {
      "id": "ID1",
      "key": "1",
      "href": "/objects/fixed-assets/setup-posting-rule/1"
    },
    {
      "id": "ID2",
      "key": "2",
      "href": "/objects/fixed-assets/setup-posting-rule/2"
    },
    {
      "id": "ID3",
      "key": "3",
      "href": "/objects/fixed-assets/setup-posting-rule/3"
    },
    {
      "id": "ID4",
      "key": "4",
      "href": "/objects/fixed-assets/setup-posting-rule/4"
    }
  ],
  "ia::meta": {
    "totalCount": 4,
    "totalSuccess": 4,
    "totalError": 0
  }
}
```

## POST /objects/fixed-assets/setup-posting-rule
_Create a setup posting rule_

**Request example — Create a setup posting rule:**
```json
{
  "journal": {
    "key": "47"
  },
  "setup": {
    "key": "1"
  },
  "id": "ID5",
  "usefulLifeUnits": "months",
  "convention": "fullMonth",
  "isTax": false,
  "useSalvageValue": false,
  "name": "Tax Accrual Book"
}
```
**Response 201 — New setup posting rule:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "ID5",
    "href": "/objects/fixed-assets/setup-posting-rule/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/setup-posting-rule/{key}
_Get a setup posting rule_

**Response 200 — Details of the setup posting rule:**
```json
{
  "ia::result": {
    "setup": {
      "id": "1",
      "key": "1"
    },
    "journal": {
      "name": "IFRS-Australia",
      "id": "IFRS-AUS",
      "key": "43",
      "bookId": "IFRSACCRUAL"
    },
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2022-09-25T01:22:00Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2023-05-12T07:09:43Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      }
    },
    "convention": "fullMonth",
    "usefulLifeUnits": "months",
    "name": "NAME 2",
    "useSalvageValue": true,
    "id": "ID2",
    "isTax": false,
    "key": "2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/fixed-assets/setup-posting-rule/{key}
_Update a setup posting rule_

**Request example — Update a setup posting rule:**
```json
{
  "key": "42",
  "id": "ID42",
  "journal": {
    "key": "1"
  },
  "setup": {
    "key": "1"
  },
  "usefulLifeUnits": "months",
  "convention": "fullMonth",
  "isTax": false,
  "useSalvageValue": false,
  "name": "Tax Accrual Book"
}
```
**Response 200 — Updated setup posting rule:**
```json
{
  "ia::result": {
    "key": "42",
    "id": "ID42",
    "href": "/objects/fixed-assets/setup-posting-rule/42"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/fixed-assets/setup-posting-rule/{key}
_Delete a setup posting rule_


## GET /objects/fixed-assets/setup/{key}
_Get a setup_

**Response 200 — Details of the setup:**
```json
{
  "ia::result": {
    "journal": {
      "name": "TAX Accrual Book",
      "id": "TAX",
      "key": "46"
    },
    "gainLossGLAccount": {
      "name": "Investments in other Companies",
      "id": "1906",
      "key": "103"
    },
    "assetSequence": {
      "id": "ASSET",
      "printTitle": "ASSET",
      "key": "34"
    },
    "setupPostingRules": [
      {
        "setup": {
          "id": "117",
          "key": "117"
        },
        "journal": {
          "name": "TAX Accrual Book",
          "id": "TAX",
          "key": "46",
          "bookId": "TAXADJACCRUAL"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2022-09-25T01:21:35Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2023-04-06T06:15:48Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "convention": "fullMonth",
        "usefulLifeUnits": "months",
        "name": "NAME 1",
        "useSalvageValue": false,
        "isTax": true,
        "id": "ID1",
        "key": "1"
      },
      {
        "setup": {
          "id": "1",
          "key": "1"
        },
        "journal": {
          "name": "IFRS-Australia",
          "id": "IFRS-AUS",
          "key": "43",
          "bookId": "IFRSACCRUAL"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2022-09-25T01:22:00Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2023-04-06T06:15:48Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "convention": "fullMonth",
        "usefulLifeUnits": "months",
        "name": "NAME 2",
        "useSalvageValue": true,
        "isTax": true,
        "id": "ID2",
        "key": "2"
      },
      {
        "setup": {
          "id": "1",
          "key": "1"
        },
        "journal": {
          "name": "Accommodation Expenses",
          "id": "Others",
          "key": "39",
          "bookId": "CEACCRUAL"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2022-09-25T01:22:22Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2023-04-06T06:15:48Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "convention": "halfYear",
        "usefulLifeUnits": "years",
        "name": "NAME 3",
        "useSalvageValue": true,
        "isTax": true,
        "id": "ID3",
        "key": "3"
      },
      {
        "setup": {
          "id": "1",
          "key": "1"
        },
        "journal": {
          "name": "GAAP Accrual Book",
          "id": "GAAP",
          "key": "45",
          "bookId": "GAAPADJACCRUAL"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2023-01-06T23:29:55Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2023-04-06T06:15:48Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "convention": "fullYear",
        "usefulLifeUnits": "years",
        "name": "NAME 41",
        "useSalvageValue": true,
        "isTax": true,
        "id": "ID41",
        "key": "41"
      },
      {
        "setup": {
          "id": "1",
          "key": "1"
        },
        "journal": {
          "name": "Fixed Asset Journal",
          "id": "FAJ",
          "key": "47",
          "bookId": "ACCRUAL"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2023-04-06T06:15:48Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2023-04-06T06:15:48Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "convention": "fullYear",
        "usefulLifeUnits": "years",
        "name": "Tax Accrual Book",
        "useSalvageValue": true,
        "isTax": false,
        "key": "42"
      }
    ],
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2022-09-22T01:00:18Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2023-04-06T06:15:48Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      }
    },
    "enableAutoPosting": false,
    "enableAccountsPayable": false,
    "enablePurchasingTxns": false,
    "enableCIP": false,
    "enableDepreciationSummary": false,
    "goLiveDate": "2021-12-16",
    "historicalAccumulatedDepreciationType": "system",
    "journalEntryCorrectionOption": "reverse",
    "id": "117",
    "key": "117"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/fixed-assets/setup/{key}
_Update a setup_

**Request example — Update a setup:**
```json
{
  "setupPostingRules": [
    {
      "journal": {
        "key": "39"
      },
      "key": "1",
      "convention": "fullMonth",
      "usefulLifeUnits": "months",
      "isTax": false,
      "useSalvageValue": true,
      "name": "new name"
    }
  ]
}
```
**Response 200 — Updated setup:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/fixed-assets/setup/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/fixed-assets/setup/{key}
_Delete a setup_


## GET /objects/fixed-assets/transfer-history
_List transfer histories_

**Response 200 — List transfer histories:**
```json
{
  "ia::result": [
    {
      "id": "1",
      "key": "1",
      "href": "/objects/fixed-assets/transfer-history/1"
    },
    {
      "id": "2",
      "key": "2",
      "href": "/objects/fixed-assets/transfer-history/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## POST /objects/fixed-assets/transfer-history
_Create a transfer history_

**Request example — Create a transfer history:**
```json
{
  "asset": {
    "key": "3"
  },
  "transferDate": "2024-11-15",
  "dimensions": {
    "location": {
      "key": "1"
    },
    "department": {
      "key": "3"
    },
    "customer": {
      "key": "1"
    },
    "item": {
      "key": "177"
    }
  }
}
```
**Response 201 — Created transfer history:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "href": "/objects/fixed-assets/transfer-history/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/transfer-history/{key}
_Get a transfer history_

**Response 200 — Details of the transfer history:**
```json
{
  "ia::result": {
    "asset": {
      "name": "Laptop",
      "id": "ADJDEC0207",
      "state": "inService",
      "key": "2140"
    },
    "journalEntries": [
      {
        "journalEntry": {
          "id": "9",
          "key": "9",
          "txnNumber": 13
        },
        "transferHistory": {
          "id": "1",
          "key": "1"
        },
        "depreciationSchedule": {
          "id": "2",
          "key": "2"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2025-01-20T06:08:40Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2025-01-20T06:08:40Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "id": "25",
        "key": "25"
      },
      {
        "journalEntry": {
          "id": "7",
          "key": "7",
          "txnNumber": 15
        },
        "transferHistory": {
          "id": "2",
          "key": "2"
        },
        "depreciationSchedule": {
          "id": "3",
          "key": "3"
        },
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2025-01-20T06:08:40Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2025-01-20T06:08:40Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          },
          "modifiedByUser": {
            "key": "1",
            "id": "Admin",
            "href": "objects/company-config/user/1"
          }
        },
        "id": "27",
        "key": "27"
      }
    ],
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2024-11-19T18:41:01Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2024-11-19T18:41:01Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "objects/company-config/user/1"
      }
    },
    "dimensions": {
      "item": {
        "name": "Goods Zero Rate",
        "id": "VAT040",
        "key": "177"
      },
      "location": {
        "name": "United States of America",
        "id": "1",
        "key": "1"
      },
      "department": {
        "name": "Engineering",
        "id": "3",
        "key": "3"
      },
      "customer": {
        "name": "Power Aerospace Materials",
        "id": "1",
        "key": "1"
      }
    },
    "id": "3",
    "transferDate": "2024-11-15",
    "key": "3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/fixed-assets/transfer-history/{key}
_Update a transfer history_

**Request example — Update a transfer history:**
```json
{
  "state": "inService",
  "inServiceDate": "2021-12-28"
}
```
**Response 200 — Updated transfer history:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "href": "/objects/fixed-assets/transfer-history/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/fixed-assets/transfer-history/{key}
_Delete a transfer history_


## GET /objects/fixed-assets/transfer-journal-entry-map
_List transfer journal entry maps_

**Response 200 — List transfer journal entry maps:**
```json
{
  "ia::result": [
    {
      "id": "1",
      "key": "1",
      "href": "/objects/fixed-assets/transfer-journal-entry-map/1"
    },
    {
      "id": "2",
      "key": "2",
      "href": "/objects/fixed-assets/transfer-journal-entry-map/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## GET /objects/fixed-assets/transfer-journal-entry-map/{key}
_Get a transfer journal entry map_

**Response 200 — Get a transfer journal entry map:**
```json
{
  "ia::result": {
    "journalEntry": {
      "key": "57",
      "id": "57",
      "txnNumber": 6,
      "href": "/objects/general-ledger/journal-entry/57"
    },
    "transferHistory": {
      "key": "28",
      "id": "28",
      "href": "/objects/fixed-assets/transfer-history/28"
    },
    "journal": {
      "key": "46",
      "id": "TAX",
      "name": "TAX Accrual Book",
      "href": "/objects/general-ledger/journal/46"
    },
    "depreciationSchedule": {
      "key": "11",
      "id": "11",
      "href": "/objects/fixed-assets/depreciation-schedule/11"
    },
    "audit": {
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "createdDateTime": "2025-04-02T20:59:13Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2025-04-02T20:59:13Z"
    },
    "key": "15",
    "id": "15",
    "href": "/objects/fixed-assets/transfer-journal-entry-map/15"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
