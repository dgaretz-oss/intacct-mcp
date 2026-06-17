# Project and Resource Management

## GET /objects/construction/cost-type
_List cost types._

**Response 200 — List of cost types:**
```json
{
  "ia::result": [
    {
      "key": "101",
      "id": "LABOR",
      "href": "/objects/construction/cost-type/101"
    },
    {
      "key": "102",
      "id": "MATERIALS",
      "href": "/objects/construction/cost-type/102"
    },
    {
      "key": "103",
      "id": "EQUIPMENT",
      "href": "/objects/construction/cost-type/103"
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

## POST /objects/construction/cost-type
_Create a cost type_

**Request example — Create a cost type:**
```json
{
  "project": {
    "id": "PRJ-001"
  },
  "task": {
    "id": "T-100"
  },
  "name": "Concrete",
  "description": "Cost type for concrete materials",
  "accumulationType": {
    "id": "MAT"
  },
  "costUnitDescription": "Cubic Yards",
  "glAccount": {
    "id": "6000"
  },
  "item": {
    "id": "C-100"
  },
  "planned": {
    "startDate": "2024-10-31",
    "endDate": "2024-12-31"
  },
  "root": {
    "id": "ROOT-001"
  },
  "standardCostType": {
    "id": "STD-002"
  },
  "taxSchedule": {
    "id": "Sale Goods Standard"
  },
  "overridePurchasingTaxSchedule": true,
  "observedPercentCompleted": [
    {
      "id": "14",
      "asOfDate": "2024-11-15",
      "percentComplete": "50.00",
      "notes": "Mid-project review indicates 50% completion."
    },
    {
      "id": "15",
      "asOfDate": "2024-05-15",
      "percentComplete": "25.00",
      "notes": "Initial equipment setup completed."
    }
  ]
}
```
**Response 201 — Reference to new cost type:**
```json
{
  "ia::result": {
    "key": "40",
    "id": "40",
    "href": "/objects/construction/cost-type/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/cost-type/{key}
_Get a cost type_

**Response 200 — Cost type details:**
```json
{
  "ia::result": {
    "key": "5941",
    "project": {
      "key": "109",
      "id": "22-001",
      "name": "Wallula Heights Conference Center",
      "href": "/objects/projects/project/109"
    },
    "task": {
      "key": "690",
      "id": "2-050",
      "name": "Demolition",
      "href": "/objects/projects/task/690"
    },
    "id": "EQ",
    "name": "Equipment",
    "description": "Equipment Group",
    "accumulationType": {
      "id": "3",
      "key": "3",
      "name": "Equipment",
      "href": "/objects/construction/accumulation-type/3"
    },
    "costUnitDescription": null,
    "status": "active",
    "glAccount": {
      "key": "383",
      "id": "5001.07",
      "href": "/objects/general-ledger/account/383"
    },
    "parent": {
      "key": "490",
      "id": "1",
      "name": "EQ"
    },
    "item": {
      "key": "317",
      "id": "Equipment",
      "name": "Equipment",
      "href": "/objects/inventory-control/item/317"
    },
    "planned": {
      "startDate": "2022-04-30",
      "endDate": "2022-06-30"
    },
    "actual": {
      "startDate": "2022-04-30",
      "endDate": "2022-06-30"
    },
    "audit": {
      "createdDateTime": "2022-01-25T16:11:28Z",
      "modifiedDateTime": "2022-01-25T16:11:28Z",
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
    "root": {
      "key": "5941",
      "id": "EQ",
      "name": "Equipment",
      "href": "/objects/construction/cost-type/5941"
    },
    "standardCostType": {
      "key": "1",
      "id": "EQ",
      "name": "Equipment",
      "href": "/objects/construction/standard-cost-type/1"
    },
    "taxSolution": {
      "key": "5",
      "id": "Australia - GST",
      "href": "/objects/tax/tax-solution/5"
    },
    "taxSchedule": {
      "id": "Sale Goods Standard",
      "key": "19",
      "href": "/objects/tax/purchasing-tax-schedule/19"
    },
    "overridePurchasingTaxSchedule": true,
    "observedPercentCompleted": [
      {
        "id": "14",
        "asOfDate": "2024-11-15",
        "percentComplete": "50.00",
        "notes": "Mid-project review indicates 50% completion."
      },
      {
        "id": "15",
        "asOfDate": "2024-05-15",
        "percentComplete": "25.00",
        "notes": "Initial equipment setup completed."
      }
    ],
    "href": "/objects/construction/cost-type/5941"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/cost-type/{key}
_Update a cost type_

**Request example — Updates a cost type description:**
```json
{
  "description": "Updated to include additional equipment rental details."
}
```
**Response 200 — Reference to updated cost type:**
```json
{
  "ia::result": {
    "key": "40",
    "id": "40",
    "href": "/objects/construction/cost-type/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/cost-type/{key}
_Delete a cost type_


## GET /objects/construction/standard-cost-type
_List standard cost types_

**Response 200 — List of standard cost types:**
```json
{
  "ia::result": [
    {
      "key": "7",
      "id": "LAB",
      "href": "/objects/construction/standard-cost-type/7"
    },
    {
      "key": "1",
      "id": "EQ",
      "href": "/objects/construction/standard-cost-type/1"
    },
    {
      "key": "2",
      "id": "EQ-Rental",
      "href": "/objects/construction/standard-cost-type/2"
    },
    {
      "key": "3",
      "id": "EQ-Owned",
      "href": "/objects/construction/standard-cost-type/3"
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

## POST /objects/construction/standard-cost-type
_Create a standard cost type_

**Request example — Create a standard cost type:**
```json
{
  "id": "EQ-Owned",
  "name": "EQ Owned",
  "description": "EQ Owned",
  "accumulationType": {
    "id": "Equipment"
  },
  "glAccount": {
    "key": "208"
  },
  "parent": {
    "id": "EQ"
  },
  "item": {
    "id": "Equipment"
  }
}
```
**Response 201 — Reference to new standard cost type:**
```json
{
  "ia::result": {
    "key": "14",
    "id": "EQ-Owned",
    "href": "/objects/construction/standard-cost-type/14"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/standard-cost-type/{key}
_Get a standard cost type_

**Response 200 — Standard cost type details:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "LAB-REG",
    "name": "Labor Regular",
    "description": "Labor Regular",
    "accumulationType": {
      "key": "1",
      "id": "Labor",
      "href": "/objects/construction/accumulation-type/1"
    },
    "costUnitDescription": null,
    "status": "active",
    "glAccount": {
      "key": "208",
      "id": "5001.01",
      "name": "Construction Labor",
      "href": "/objects/general-ledger/account/208"
    },
    "parent": {
      "key": "7",
      "id": "LAB",
      "name": "Labor",
      "href": "/objects/construction/standard-cost-type/7"
    },
    "item": {
      "key": "320",
      "id": "Labor",
      "name": "Labor",
      "href": "/objects/inventory-control/item/320"
    },
    "audit": {
      "createdDateTime": "2022-10-14T15:45:22Z",
      "modifiedDateTime": "2022-10-14T15:46:44Z",
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
    "href": "/objects/construction/standard-cost-type/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/standard-cost-type/{key}
_Update a standard cost type_

**Request example — Update standard cost type fields:**
```json
{
  "description": "Owned equipment",
  "costUnitDescription": "each",
  "glAccount": {
    "id": "5001.05"
  },
  "item": {
    "id": "Equipment"
  },
  "parent": {
    "id": "OH"
  }
}
```
**Response 200 — Reference to updated standard cost type:**
```json
{
  "ia::result": {
    "key": "14",
    "id": "EQ-Owned",
    "href": "/objects/construction/standard-cost-type/14"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/standard-cost-type/{key}
_Delete a standard cost type_


## GET /objects/construction/standard-task
_List standard tasks_

**Response 200 — example-result-collection-of-standard-tasks:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1-000",
      "href": "/objects/construction/standard-task/1"
    },
    {
      "key": "2",
      "id": "3-010",
      "href": "/objects/construction/standard-task/2"
    },
    {
      "key": "3",
      "id": "1-020",
      "href": "/objects/construction/standard-task/3"
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

## POST /objects/construction/standard-task
_Create a standard task_

**Request example — Create a standard task:**
```json
{
  "id": "1-010",
  "name": "Summary of Work",
  "description": "Summary of Work",
  "status": "active",
  "isBillable": false,
  "isMilestone": false,
  "isUtilized": false,
  "parent": {
    "id": "1-000"
  },
  "standardCostTypes": [
    {
      "id": "EQ"
    },
    {
      "id": "EQ-Owned"
    },
    {
      "id": "EQ-Rental"
    },
    {
      "id": "LAB"
    },
    {
      "id": "LAB-OT"
    },
    {
      "id": "LAB-REG"
    },
    {
      "id": "LAB-SALARY"
    },
    {
      "id": "LAB-BURDEN"
    },
    {
      "id": "MAT"
    },
    {
      "id": "OH"
    },
    {
      "id": "OTH"
    }
  ]
}
```
**Response 201 — Reference to new standard task:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "1-010",
    "href": "/objects/construction/standard-task/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/standard-task/{key}
_Get a standard task_

**Response 200 — Details of the standard task:**
```json
{
  "ia::result": {
    "key": "312",
    "id": "1-010",
    "name": "Summary of Work",
    "description": "General Conditions: Summary of Work",
    "productionUnitDescription": "days",
    "status": "active",
    "item": {
      "key": "318",
      "id": "Other",
      "name": "Other",
      "href": "/objects/inventory-control/item/318"
    },
    "isBillable": false,
    "isMilestone": false,
    "isUtilized": true,
    "timeType": {
      "key": "11",
      "id": "Design",
      "href": "/objects/construction/time-type/11"
    },
    "wbsCode": "S",
    "parent": {
      "key": "1",
      "id": "1-000",
      "name": "GENERAL CONDITIONS",
      "href": "/objects/construction/standard-task/1"
    },
    "class": {
      "key": "8",
      "id": "CON",
      "name": "Construction",
      "href": "/objects/company-config/class/8"
    },
    "audit": {
      "createdDateTime": "2021-11-23T23:57:52Z",
      "modifiedDateTime": "2021-11-29T23:15:38Z",
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
    "standardCostTypes": [
      {
        "key": "1",
        "id": "EQ",
        "href": "/objects/construction/standard-cost-type/1"
      },
      {
        "key": "3",
        "id": "EQ-Owned",
        "href": "/objects/construction/standard-cost-type/3"
      }
    ],
    "href": "/objects/construction/standard-task/312"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/standard-task/{key}
_Update a standard task_

**Request example — Update standard task and add standard cost type:**
```json
{
  "description": "General Conditions: Summary of Work",
  "productionUnitDescription": "days",
  "isUtilized": true,
  "class": {
    "id": "3"
  },
  "standardCostTypes": [
    {
      "id": "SUB"
    }
  ]
}
```
**Request example — Delete a standard cost type:**
```json
{
  "standardCostTypes": [
    {
      "key": "13",
      "ia::operation": "delete"
    }
  ]
}
```
**Request example — Update standard cost type:**
```json
{
  "standardCostTypes": [
    {
      "key": "11",
      "id": "MAT"
    }
  ]
}
```
**Response 200 — Reference to updated standard task:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "1-010",
    "href": "/objects/construction/standard-task/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/standard-task/{key}
_Delete a standard task_


## GET /objects/projects/invoice-run
_List invoice runs_

**Response 200 — List invoice runs:**
```json
{
  "ia::result": [
    {
      "key": "6",
      "id": "6",
      "href": "/objects/projects/invoice-run/6"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/projects/invoice-run/5"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/projects/invoice-run/3"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/projects/invoice-run/4"
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

## GET /objects/projects/invoice-run/{key}
_Get an invoice run_

**Response 200 — Get an invoice run:**
```json
{
  "ia::result": {
    "id": "175",
    "key": "175",
    "invoiceTemplate": {
      "id": "146",
      "key": "146",
      "name": "Invoice Progress Billing",
      "href": "/objects/order-entry/txn-definition/146"
    },
    "priceList": {
      "key": null,
      "id": null
    },
    "expensePriceMarkup": null,
    "description": "Invoice run created at 2025-05-08 13:33:45 GMT",
    "isOffline": false,
    "state": "success",
    "errorData": null,
    "createdBy": {
      "key": "1",
      "id": "Admin",
      "href": "/objects/company-config/user/1"
    },
    "invoiceRunDateTime": "2025-05-08T13:33:45Z",
    "href": "/objects/projects/invoice-run/175",
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/15"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/position-skill
_List position skills_

**Response 200 — List of position skills:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Quantum Mechanic",
      "href": "/objects/projects/position-skill/1"
    },
    {
      "key": "2",
      "id": "Brick Layer",
      "href": "/objects/projects/position-skill/2"
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

## POST /objects/projects/position-skill
_Create a position skill_

**Request example — Creates a position skill:**
```json
{
  "id": "Quantum Mechanic",
  "description": "Scientist who works with very tiny wrenches."
}
```
**Response 201 — Reference to new position skill:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "Quantum Mechanic",
    "href": "/objects/projects/position-skill/23"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/position-skill/{key}
_Get a position skill_

**Response 200 — Details of the position skill:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Quantum Mechanic",
    "description": "Scientist who works with very tiny wrenches",
    "status": "active",
    "audit": {
      "createdDateTime": "2025-04-12T00:02:45Z",
      "modifiedDateTime": "2025-04-12T00:02:45Z",
      "createdByUser": {
        "key": "158",
        "id": "Hal",
        "href": "/objects/company-config/user/158"
      },
      "createdBy": "158",
      "modifiedByUser": {
        "key": "158",
        "id": "Hal",
        "href": "/objects/company-config/user/158"
      },
      "modifiedBy": "158"
    },
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "href": "/objects/projects/position-skill/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/projects/position-skill/{key}
_Update a position skill_

**Request example — Update a position skill:**
```json
{
  "description": "One who places bricks. Precisely."
}
```
**Response 200 — Reference to updated position skill:**
```json
{
  "ia::result": {
    "key": "22",
    "id": "Brick Layer",
    "href": "/objects/projects/position-skill/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/projects/position-skill/{key}
_Delete a position skill_


## GET /objects/projects/project
_List projects_

**Response 200 — List projects:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "P-040",
      "href": "/objects/projects/project/100"
    },
    {
      "key": "101",
      "id": "P-050",
      "href": "/objects/projects/project/101"
    },
    {
      "key": "102",
      "id": "P-060",
      "href": "/objects/projects/project/102"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 5,
    "next": 0,
    "previous": 0
  }
}
```

## POST /objects/projects/project
_Create a project_

**Request example — Create a project:**
```json
{
  "id": "P-0045",
  "name": "Implementation Project",
  "description": "Software Implementation Project",
  "projectCurrency": "USD",
  "category": "contract",
  "projectStatus": {
    "key": "1"
  },
  "startDate": "2025-01-23",
  "endDate": "2025-04-01",
  "budget": {
    "billingAmount": "10000.00",
    "budgetedDuration": "250.00",
    "budgetedCost": "10000.00"
  },
  "glBudget": {
    "key": "5"
  },
  "contractAmount": "15000.00",
  "actualAmount": "15000.00",
  "billingType": "timeAndMaterial",
  "salesOrderNumber": "SO-5478",
  "purchaseOrderNumber": "PO-7829",
  "purchaseOrderAmount": "4500.00",
  "purchaseQuoteNumber": "1453",
  "documentNumber": "1453",
  "parent": {
    "key": "9"
  },
  "invoiceWithParent": false,
  "customer": {
    "key": "13"
  },
  "salesContact": {
    "key": "10"
  },
  "projectType": {
    "key": "3"
  },
  "manager": {
    "key": "10"
  },
  "department": {
    "key": "10"
  },
  "location": {
    "key": "1"
  },
  "cipAsset": {
    "key": "1"
  },
  "customerUser": {
    "key": "1"
  },
  "class": {
    "key": "1"
  },
  "userRestrictions": "systemDefault",
  "isBillableEmployeeExpense": false,
  "isBillablePurchasingAPExpense": false,
  "ratesAndPricing": {
    "laborPricing": "billingRate",
    "laborMarkup": "10",
    "expensePricing": "billingRate",
    "expenseMarkup": "10",
    "defaultRate": "12"
  },
  "contacts": {
    "primary": {
      "key": "1"
    },
    "billTo": {
      "key": "2"
    }
  },
  "invoiceMessage": "Invoice for project",
  "invoiceCurrency": "USD",
  "billingOverMax": "preventBilling",
  "excludeExpenses": false,
  "grant": {
    "aln": "10.555",
    "fundedProjectName": "Undergraduate Programs",
    "agency": "US government",
    "payer": "federal",
    "otherId": "Other",
    "assistanceType": "cash",
    "revenueRestriction": "time",
    "restrictionExpiry": "1",
    "restrictionExpirationDate": "2021-01-23",
    "isTimeSatisfactionScheduled": false
  },
  "wipScheduleProject": {
    "key": "10"
  },
  "excludeFromWIPSchedule": false,
  "status": "active",
  "taxSolution": {
    "id": "Australia GST"
  },
  "taxSchedule": {
    "id": "Sale Goods Standard"
  }
}
```
**Response 201 — Reference to new project:**
```json
{
  "ia::result": {
    "key": "100",
    "id": "P-0045",
    "href": "/objects/projects/project/100"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/project-billing-template
_List billing templates_

**Response 200 — List project billing templates:**
```json
{
  "ia::result": [
    {
      "key": "12",
      "id": "12",
      "href": "/objects/projects/project-billing-template/12"
    },
    {
      "key": "13",
      "id": "13",
      "href": "/objects/projects/project-billing-template/13"
    },
    {
      "key": "14",
      "id": "14",
      "href": "/objects/projects/project-billing-template/14"
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

## POST /objects/projects/project-billing-template
_Create a project billing template_

**Request example — Create a project billing template:**
```json
{
  "name": "Project Estimated Hours",
  "description": "Template for billing by estimated project hours",
  "billingMethod": "percentCompleted",
  "calculateOn": "project",
  "basedOn": "plannedHours",
  "status": "active",
  "milestones": [
    {
      "percentCompleted": "0.1",
      "description": "Project Estimated Hours"
    }
  ]
}
```
**Response 201 — Reference to new project billing template:**
```json
{
  "ia::result": {
    "key": "15",
    "id": "15",
    "href": "/objects/projects/project-billing-template/15"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/project-billing-template-milestone
_List billing template milestones_

**Response 200 — List project billing template milestones:**
```json
{
  "ia::result": [
    {
      "key": "23",
      "id": "23'",
      "href": "/objects/projects/project-billing-template-milestone/23"
    },
    {
      "key": "24",
      "id": "24",
      "href": "/objects/projects/project-billing-template-milestone/24"
    },
    {
      "key": "25",
      "id": "25",
      "href": "/objects/projects/project-billing-template-milestone/25"
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

## GET /objects/projects/project-billing-template-milestone/{key}
_Get a Project billing template milestone_

**Response 200 — Get a project billing template milestone:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "23",
    "percentCompleted": "25.00",
    "percentToInvoice": "50.00",
    "description": "Invoice at 50%",
    "href": "/objects/projects/project-billing-template-milestone/23",
    "projectBillingTemplate": {
      "key": "12",
      "id": "12",
      "href": "/objects/projects/project-billing-template/12"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/project-billing-template/{key}
_Get a billing template_

**Response 200 — Get a project billing template:**
```json
{
  "ia::result": {
    "key": "15",
    "id": "15",
    "href": "/objects/projects/project-billing-template/15",
    "name": "Project Estimated Hours",
    "description": "Template for billing by estimated project hours",
    "billingMethod": "percentCompleted",
    "calculateOn": "project",
    "basedOn": "plannedHours",
    "status": "active",
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/15"
    },
    "milestones": [
      {
        "key": "23",
        "id": "23",
        "percentCompleted": "0.5",
        "percentToInvoice": "0.5",
        "description": "Bill at 50% completion",
        "href": "/objects/projects/project-billing-template-milestone/23",
        "projectBillingTemplate": {
          "key": "15",
          "id": "15",
          "href": "/objects/projects/project-billing-template/15"
        }
      },
      {
        "key": "24",
        "id": "24",
        "percentCompleted": "1",
        "percentToInvoice": "0.5",
        "description": "Bill at 100% completion",
        "href": "/objects/projects/project-billing-template-milestone/23",
        "projectBillingTemplate": {
          "key": "15",
          "id": "15",
          "href": "/objects/projects/project-billing-template/15"
        }
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

## PATCH /objects/projects/project-billing-template/{key}
_Update a billing template_

**Request example — Update a project billing template:**
```json
{
  "description": "Bill by actual project hours"
}
```
**Response 200 — Reference to updated project billing template:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "12",
    "href": "/objects/projects/project-billing-template/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/projects/project-billing-template/{key}
_Delete a billing template_


## GET /objects/projects/project-group
_List project groups_

**Response 200 — List project groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/projects/project-group/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/projects/project-group/3"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/projects/project-group/5"
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

## POST /objects/projects/project-group
_Create a project group_

**Request example — Create a project group where group type is set to all:**
```json
{
  "id": "P-GRP-01",
  "name": "Top Priority Projects",
  "description": "Group for top priority projects",
  "groupType": "all",
  "memberFilter": {
    "object": "projects/project",
    "filters": [
      {
        "$eq": {
          "status": "active"
        }
      },
      {
        "$in": {
          "projectStatus.id": [
            "In Progress",
            "Active"
          ]
        }
      }
    ],
    "filterExpression": "and",
    "orderBy": [
      {
        "id": "desc"
      }
    ]
  }
}
```
**Request example — Creates a project group where group type is set to specific:**
```json
{
  "id": "GLB-SER-GRP-OO1",
  "name": "Global Client Level 1 Project Group",
  "description": "Global Clients with Level 1 Projects",
  "groupType": "specific",
  "groupMembers": [
    {
      "id": "GLB SER - BTI"
    },
    {
      "id": "GLB SER - HCS"
    },
    {
      "id": "GLB SER - JHC"
    }
  ]
}
```
**Response 201 — Reference to new project group:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "GLB-SER-GRP-OO1",
    "href": "/objects/projects/project-group/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/project-group/{key}
_Get a project group_

**Response 200 — Get a project group:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "GLB-SER-GRP-OO1",
    "name": "Global Client Level 1 Project Group",
    "description": "Global Clients with Level 1 Projects",
    "groupType": "specific",
    "audit": {
      "createdDateTime": "2025-09-23T15:22:59Z",
      "modifiedDateTime": "2025-09-23T15:22:59Z",
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
    "isDimensionStructure": false,
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "groupMembers": [
      {
        "key": "32",
        "id": "GLB SER - BTI",
        "name": "Global Search - Berkeley Technology Inc",
        "status": "active",
        "href": "/objects/projects/project/32"
      },
      {
        "key": "33",
        "id": "GLB SER - HCS",
        "name": "Global Search - Hands Computer Systems",
        "status": "active",
        "href": "/objects/projects/project/33"
      },
      {
        "key": "34",
        "id": "GLB SER - JHC",
        "name": "Global Search - Jones Hogan Company",
        "status": "active",
        "href": "/objects/projects/project/34"
      }
    ],
    "memberFilter": {
      "object": "projects/project",
      "filterExpression": "and",
      "orderBy": [
        {
          "id": "asc"
        }
      ]
    },
    "href": "/objects/projects/project-group/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/projects/project-group/{key}
_Update a project group_

**Request example — Update a project group:**
```json
{
  "name": "Global Client Level 1 Project Group - Updated",
  "description": "Global Client Level 1 Project Group - Updated",
  "groupMembers": [
    {
      "id": "GLB SER - BTI"
    },
    {
      "id": "GLB SER - HCS"
    },
    {
      "id": "GLB SER - JHC"
    },
    {
      "id": "GLB SER - LGX"
    }
  ]
}
```
**Response 200 — Reference to updated project group:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "GLB-SER-GRP-OO1",
    "href": "/objects/projects/project-group/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/projects/project-group/{key}
_Delete a project group_


## GET /objects/projects/project-resource
_List project resources_

**Response 200 — List project resources:**
```json
{
  "ia::result": [
    {
      "key": "12345",
      "id": "12345",
      "href": "/objects/projects/project-resource/12345"
    },
    {
      "key": "85",
      "id": "EXP-00002",
      "href": "/objects/projects/employee-expense/85"
    },
    {
      "key": "60",
      "id": "EXP-00003",
      "href": "/objects/projects/employee-expense/60"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 5,
    "next": 0,
    "previous": 0
  }
}
```

## POST /objects/projects/project-resource
_Create a project resource_

**Request example — Creates a project resource:**
```json
{
  "description": "Hourly resource",
  "startDate": "2025-04-01",
  "employee": {
    "key": "17"
  },
  "item": {
    "key": "23"
  },
  "pricing": {
    "laborRate": 100,
    "expenseRate": 110,
    "apPurchasingRate": 120
  },
  "project": {
    "key": "9"
  }
}
```
**Response 201 — Reference to new project resource:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/projects/project-resource/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/project-resource/{key}
_Get a project resource_

**Response 200 — Get a project resource:**
```json
{
  "ia::result": {
    "id": "5",
    "key": "5",
    "audit": {
      "createdDateTime": "2025-09-23T15:59:32Z",
      "modifiedDateTime": "2025-09-23T15:59:32Z",
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
    "project": {
      "key": "9",
      "id": "9",
      "name": "Implementation - Logic Solutions",
      "href": "/objects/projects/project/9"
    },
    "employee": {
      "key": "17",
      "id": "EMP1-US",
      "href": "/objects/company-config/employee/17"
    },
    "employeeContact": {
      "id": "Restricted dept mgr's Hourly employee",
      "key": "24",
      "href": "/objects/company-config/contact/24"
    },
    "item": {
      "key": "23",
      "id": "Price_at_task",
      "name": "Price_at_task",
      "href": "/objects/inventory-control/item/23"
    },
    "description": "Hourly resource",
    "startDate": "2025-04-01",
    "pricing": {
      "laborPricingMethod": "billingRate",
      "laborRate": 100,
      "expensePricingMethod": "costPlusFee",
      "expenseRate": 110,
      "apPurchasingPricingMethod": "costPlusFee",
      "apPurchasingRate": 120
    },
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "href": "/objects/projects/project-resource/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/projects/project-resource/{key}
_Update a project resource_

**Request example — Update a project resource:**
```json
{
  "description": "Hourly Rate - Project Resource Updated"
}
```
**Response 200 — Reference to updated project resource:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/projects/project-resource/5"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## DELETE /objects/projects/project-resource/{key}
_Delete a project resource_


## GET /objects/projects/project-status
_List project statuses_

**Response 200 — List project statuses:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "In Progress",
      "href": "/objects/projects/project-status/100"
    },
    {
      "key": "101",
      "id": "Completed",
      "href": "/objects/projects/project-status/101"
    },
    {
      "key": "102",
      "id": "Started",
      "href": "/objects/projects/project-status/102"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 5,
    "next": 0,
    "previous": 0
  }
}
```

## POST /objects/projects/project-status
_Create a project status_

**Request example — Creates a project status:**
```json
{
  "id": "Pending Approval",
  "description": "Pending Project Manager approval",
  "disableTimesheetEntry": false,
  "disableExpenseEntry": false,
  "disablePurchasingAPEntry": false,
  "disableGenerateInvoice": false,
  "status": "active"
}
```
**Response 201 — Create a project status:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "Pending Approval",
    "href": "/objects/projects/project-status/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/project-status/{key}
_Get a project status_

**Response 200 — Get a project status:**
```json
{
  "ia::result": {
    "id": "Pending Approval",
    "description": "Pending Project Manager Approval",
    "disableTimesheetEntry": false,
    "disableExpenseEntry": false,
    "disablePurchasingAPEntry": false,
    "disableGenerateInvoice": false,
    "status": "active",
    "key": "6",
    "audit": {
      "createdDateTime": "2025-09-23T16:35:59Z",
      "modifiedDateTime": "2025-09-23T16:35:59Z",
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
      "key": null,
      "id": null,
      "name": null
    },
    "href": "/objects/projects/project-status/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/projects/project-status/{key}
_Update a project status_

**Request example — Update a project status:**
```json
{
  "disableTimesheetEntry": true
}
```
**Response 200 — Reference to updated project status:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "Pending Approval",
    "href": "/objects/projects/project-status/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/projects/project-status/{key}
_Delete a project status_


## GET /objects/projects/project-type
_List project types_

**Response 200 — List project types:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "Internal",
      "href": "/objects/projects/project-type/100"
    },
    {
      "key": "101",
      "id": "External",
      "href": "/objects/projects/project-type/101"
    },
    {
      "key": "102",
      "id": "Contract",
      "href": "/objects/projects/project-type/102"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 5,
    "next": 0,
    "previous": 0
  }
}
```

## POST /objects/projects/project-type
_Create a project type_

**Request example — Create a project type:**
```json
{
  "id": "Internal",
  "parent": {
    "key": "1"
  },
  "status": "active"
}
```
**Response 201 — Reference to new project type:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "Internal",
    "href": "/objects/projects/project-type/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/project-type/{key}
_Get a project type_

**Response 200 — Get a project type:**
```json
{
  "ia::result": {
    "id": "Internal",
    "parent": {
      "id": "Top Level Project",
      "key": "1",
      "href": "/objects/projects/project-type/1"
    },
    "status": "active",
    "key": "5",
    "audit": {
      "createdDateTime": "2025-09-23T16:47:30Z",
      "modifiedDateTime": "2025-09-23T16:47:30Z",
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
      "key": null,
      "id": null,
      "name": null
    },
    "href": "/objects/projects/project-type/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/projects/project-type/{key}
_Update a project type_

**Request example — Update a project type:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated project type:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "Internal",
    "href": "/objects/projects/project-type/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/projects/project-type/{key}
_Delete a project type_


## GET /objects/projects/project/{key}
_Get a project_

**Response 200 — Get a project:**
```json
{
  "ia::result": {
    "key": "106",
    "id": "P-0045",
    "name": "Implementation Project",
    "description": "Software Implementation Project",
    "projectCurrency": "USD",
    "category": "contract",
    "projectStatus": {
      "key": "1",
      "id": "In Progress",
      "disableTimesheetEntry": null,
      "disableExpenseEntry": null,
      "disablePurchasingAPEntry": null,
      "disableGenerateInvoice": null,
      "href": "/objects/projects/project-status/1"
    },
    "status": "active",
    "startDate": "2025-01-23",
    "endDate": "2025-04-01",
    "budget": {
      "billingAmount": "10000.00",
      "budgetedDuration": "250.00",
      "budgetedCost": "10000.00"
    },
    "contractAmount": "15000.00",
    "actualAmount": "15000.00",
    "progress": {
      "estimatedDuration": null,
      "actualDuration": null,
      "approvedDuration": null,
      "remainingDuration": null,
      "percentComplete": null,
      "observedPercentComplete": "0.00"
    },
    "billingType": "timeAndMaterial",
    "salesOrderNumber": "SO-5478",
    "purchaseOrderNumber": "PO-7829",
    "purchaseOrderAmount": "4500.00",
    "purchaseQuoteNumber": "1453",
    "salesforceKey": null,
    "parent": {
      "key": "9",
      "id": "9",
      "name": "Implementation - Logic Solutions",
      "href": "/objects/projects/project/9"
    },
    "invoiceWithParent": false,
    "customer": {
      "key": "13",
      "id": "OTC",
      "name": "One Time Customer",
      "href": "/objects/accounts-receivable/customer/13"
    },
    "salesContact": {
      "key": "10",
      "id": "MGR6",
      "name": "OPE Dept - Manager",
      "href": "/objects/company-config/employee/10"
    },
    "projectType": {
      "key": "3",
      "id": "2nd Level Project",
      "href": "/objects/projects/project-type/3"
    },
    "manager": {
      "key": "10",
      "id": "MGR6",
      "name": "OPE Dept - Manager",
      "href": "/objects/company-config/employee/10"
    },
    "department": {
      "key": "10",
      "id": "ACP",
      "name": "Accounts Payable",
      "href": "/objects/company-config/department/10"
    },
    "location": {
      "key": "1",
      "id": "1",
      "name": "United States of America",
      "href": "/objects/company-config/location/1"
    },
    "cipAsset": {
      "key": "1",
      "id": "CIP-COURSE-LAPTOP-001",
      "name": "Course Delivery Laptop - CIP Capital Equipment",
      "href": "/objects/fixed-assets/asset/1"
    },
    "contacts": {
      "primary": {
        "id": "Admin",
        "key": "1",
        "href": "/objects/company-config/contact/1"
      },
      "shipTo": {
        "id": null,
        "key": null
      },
      "billTo": {
        "id": "intacct",
        "key": "2",
        "href": "/objects/company-config/contact/2"
      }
    },
    "paymentTerm": {
      "key": null,
      "id": null
    },
    "documentNumber": "1453",
    "customerUser": {
      "key": "1",
      "id": "Admin",
      "href": "/objects/company-config/user/1"
    },
    "audit": {
      "createdDateTime": "2025-09-23T12:44:37Z",
      "modifiedDateTime": "2025-09-23T12:44:37Z",
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
    "class": {
      "id": "3",
      "name": "Heath Care",
      "key": "1",
      "href": "/objects/company-config/class/1"
    },
    "userRestrictions": "systemDefault",
    "isBillableEmployeeExpense": false,
    "isBillablePurchasingAPExpense": false,
    "glBudget": {
      "id": "Employee Expense Budget",
      "key": "5",
      "href": "/objects/general-ledger/budget/5"
    },
    "ratesAndPricing": {
      "laborMarkup": null,
      "laborPricing": "billingRate",
      "expenseMarkup": null,
      "expensePricing": "billingRate",
      "defaultRate": "12",
      "purchasingAPPricing": "costPlusFee"
    },
    "invoiceMessage": "Invoice for project",
    "invoiceCurrency": "USD",
    "billingOverMax": "preventBilling",
    "excludeExpenses": false,
    "contract": {
      "key": null,
      "id": null
    },
    "attachment": {
      "id": null,
      "key": null
    },
    "rootProject": {
      "key": "9",
      "id": "9",
      "name": "Implementation - Logic Solutions",
      "href": "/objects/projects/project/9"
    },
    "grant": {
      "aln": null,
      "fundedProjectName": null,
      "agency": null,
      "payer": null,
      "otherId": null,
      "assistanceType": null,
      "revenueRestriction": null,
      "restrictionExpiry": null,
      "restrictionExpirationDate": null,
      "isTimeSatisfactionScheduled": false
    },
    "wipScheduleProject": {
      "key": "10",
      "id": "SI",
      "name": "Support Incidents - Network Shift Corp",
      "href": "/objects/projects/project/10"
    },
    "excludeFromWIPSchedule": false,
    "multiEntityLocation": {
      "key": null,
      "id": null,
      "name": null
    },
    "scopeDetails": {
      "scope": null,
      "inclusions": null,
      "exclusions": null,
      "terms": null
    },
    "scheduleDetails": {
      "scheduledStartDate": null,
      "actualStartDate": null,
      "scheduledCompletionDate": null,
      "revisedCompletionDate": null,
      "substantialCompletionDate": null,
      "actualCompletionDate": null,
      "noticeToProceedDate": null,
      "responseDueDate": null,
      "executedOnDate": null,
      "scheduleImpactNotes": null
    },
    "taxSchedule": {
      "id": "Sale Goods Standard",
      "key": "19",
      "href": "/objects/tax/order-entry-tax-schedule/19"
    },
    "taxSolution": {
      "key": "9",
      "id": "Australia GST",
      "href": "/objects/tax/tax-solution/9"
    },
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "href": "/objects/projects/project/106"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/projects/project/{key}
_Update a project_

**Request example — Update a project:**
```json
{
  "name": "Global Implementation Project",
  "description": "Global Software Implementation Project",
  "projectCurrency": "USD",
  "category": "contract"
}
```
**Response 200 — Reference to updated project:**
```json
{
  "ia::result": {
    "key": "106",
    "id": "P-0345",
    "href": "/objects/projects/project/106"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/projects/project/{key}
_Delete a project_


## GET /objects/projects/task
_List tasks_

**Response 200 — List tasks:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "TASK-MERIDIAN-REQ-001",
      "href": "/objects/projects/task/1"
    },
    {
      "key": "2",
      "id": "TASK-NOVA-MIG-002",
      "href": "/objects/projects/task/2"
    },
    {
      "key": "3",
      "id": "TASK-TECHSOL-CONFIG-003",
      "href": "/objects/projects/task/3"
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

## POST /objects/projects/task
_Create a task_

**Request example — Creates a task:**
```json
{
  "id": "NET-XML30-1-REQ-001",
  "name": "Requirements Gathering",
  "project": {
    "id": "NET-XML30-1"
  },
  "taskStatus": "planned",
  "taxSchedule": {
    "id": "Sale Goods Standard"
  },
  "overridePurchasingTaxSchedule": true
}
```
**Response 201 — Reference to new task:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "NET-XML30-1-REQ-001",
    "href": "/objects/projects/task/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/task-group
_List task groups_

**Response 200 — List task groups:**
```json
{
  "ia::result": [
    {
      "key": "4",
      "id": "INDHCS",
      "href": "/objects/projects/task-group/4"
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

## POST /objects/projects/task-group
_Create a task group_

**Request example — Create a task group:**
```json
{
  "id": "INDHCS",
  "name": "India HCS",
  "description": "India DIM - HCS group",
  "groupType": "all",
  "memberFilter": {
    "object": "projects/task",
    "filterExpression": "and",
    "filters": [
      {
        "$eq": {
          "billable": true
        }
      },
      {
        "$eq": {
          "projectId": "DIM - HCS"
        }
      }
    ],
    "orderBy": [
      {
        "id": "asc"
      }
    ]
  },
  "isDimensionStructure": true
}
```
**Response 201 — Reference to new task group:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "INDHCS",
    "href": "/objects/projects/task-group/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/projects/task-group/{key}
_Get a task group_

**Response 200 — Get a task group:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "INDHCS",
    "name": "India HCS",
    "description": "India DIM - HCS group",
    "groupType": "all",
    "memberFilter": {
      "object": "projects/task",
      "filterExpression": "and",
      "filters": [
        {
          "$eq": {
            "billable": true
          }
        },
        {
          "$eq": {
            "projectId": "DIM - HCS"
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
      "createdDateTime": "2025-01-31T05:19:51Z",
      "modifiedDateTime": "2025-01-31T05:19:51Z",
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
    "href": "/objects/projects/task-group/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/projects/task-group/{key}
_Update a task group_

**Request example — Updates a task group:**
```json
{
  "memberFilter": {
    "object": "projects/task",
    "filterExpression": "and",
    "filters": [
      {
        "$eq": {
          "billable": true
        }
      },
      {
        "$eq": {
          "projectId": "DIM - HCS"
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
**Response 200 — Reference to updated task group:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "INDHCS",
    "href": "/objects/projects/task-group/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/projects/task-group/{key}
_Delete a task group_


## GET /objects/projects/task/{key}
_Get a task_

**Response 200 — Get a task:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "NET-XML30-1-REQ-001",
    "parent": {
      "key": "11",
      "id": "NET-XML30-1-IMPL-001",
      "name": "Implementation Phase",
      "href": "/objects/projects/task/11"
    },
    "name": "Requirements Gathering",
    "project": {
      "key": "1",
      "id": "NET-XML30-1",
      "name": "NetSuite XML Integration - Phase 1",
      "startDate": "2023-02-25",
      "endDate": "2023-04-25",
      "href": "/objects/projects/project/56"
    },
    "customer": {
      "key": "1",
      "id": "CUST-ATLAS-001",
      "name": "Corley Manufacturing Ltd",
      "href": "/objects/accounts-receivable/customer/41"
    },
    "productionUnits": {
      "estimate": 1200,
      "description": "Error Handling Rule Implemented."
    },
    "item": {
      "key": "311",
      "id": "SERV-INTEG-001",
      "name": "Professional Services - Integration Development",
      "href": "/objects/inventory-control/item/311"
    },
    "planned": {
      "startDate": "2023-02-25",
      "endDate": "2023-06-25"
    },
    "actual": {
      "startDate": "2023-02-25",
      "endDate": "2023-11-25"
    },
    "duration": {
      "planned": 100,
      "estimated": 100,
      "actual": 0,
      "remaining": null,
      "approved": 0,
      "plannedBillable": 0,
      "estimatedBillable": 0,
      "actualBillable": 0,
      "approvedBillable": 0
    },
    "percentComplete": "0.25",
    "observedPercentComplete": "0.30",
    "description": "Gather and document technical and business requirements for the NetSuite XML integration.",
    "isMilestone": false,
    "isUtilized": false,
    "isBillable": false,
    "wbsCode": "1",
    "priority": 1,
    "taskStatus": "inProgress",
    "timeType": {
      "key": "2",
      "id": "Overtime",
      "href": "/objects/time/time-type/2"
    },
    "class": {
      "key": "19",
      "id": "CLASS-PS-INTEG",
      "name": "Professional Services - Integration Projects",
      "href": "/objects/company-config/class/19"
    },
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
    "dependentOn": {
      "key": "1",
      "id": "NET-XML30-1-DESIGN-002",
      "name": "System Design",
      "href": "/objects/projects/task/1"
    },
    "root": {
      "key": "1",
      "id": "NET-XML30-1-ROOT-000",
      "name": "NetSuite Integration - Phase 1",
      "href": "/objects/projects/task/1"
    },
    "standardTask": {
      "key": "1",
      "id": "STD-INTEG-REQ-001",
      "name": "Requirements Gathering - Integration Projects",
      "href": "/objects/construction/standard-task/1"
    },
    "attachment": {
      "key": null,
      "id": null
    },
    "taxSolution": {
      "id": "Advanced Tax India",
      "key": "9",
      "href": "/objects/tax/tax-solution/9"
    },
    "taxSchedule": {
      "id": "Sale Goods Standard",
      "key": "19",
      "href": "/objects/tax/order-entry-tax-schedule/19"
    },
    "overridePurchasingTaxSchedule": true,
    "href": "/objects/projects/task/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/projects/task/{key}
_Update a task_

**Request example — Update a task:**
```json
{
  "taskStatus": "completed",
  "duration": {
    "estimated": 27
  }
}
```
**Response 200 — Reference to updated task:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "NET-XML30-1-REQ-001",
    "href": "/objects/projects/task/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/projects/task/{key}
_Delete a task_

