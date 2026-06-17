# Time

## GET /objects/time/time-type
_List time types_

**Response 200 — List time types:**
```json
{
  "ia::result": [
    {
      "key": "46",
      "id": "Overtime",
      "href": "/objects/time/time-type/46"
    },
    {
      "key": "44",
      "id": "Part time",
      "href": "/objects/time/time-type/44"
    },
    {
      "key": "40",
      "id": "Full time",
      "href": "/objects/time/time-type/40"
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

## POST /objects/time/time-type
_Create a time type_

**Request example — Create a time type:**
```json
{
  "id": "Overtime",
  "earningType": {
    "key": "22"
  },
  "glAccount": {
    "key": "12"
  },
  "offsetGLAccount": {
    "key": "15"
  },
  "status": "active"
}
```
**Response 201 — Reference to new time type:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "10",
    "href": "/objects/time/time-type/10"
  },
  "ia::meta": {
    "totalCount": 3
  }
}
```

## GET /objects/time/time-type/{key}
_Get a time type_

**Response 200 — Get a time type:**
```json
{
  "ia::result": {
    "key": "46",
    "id": "Overtime",
    "href": "/objects/time/time-type/46",
    "earningType": {
      "href": "/objects/company-config/earning-type/22",
      "key": "22",
      "id": "Salary"
    },
    "glAccount": {
      "href": "/objects/general-ledger/account/12",
      "key": "12",
      "id": "5001",
      "name": "Labor"
    },
    "offsetGLAccount": {
      "href": "/objects/general-ledger/account/15",
      "key": "15",
      "id": "5002",
      "name": "Labor Offset"
    },
    "status": "active",
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    }
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0
  }
}
```

## PATCH /objects/time/time-type/{key}
_Update a time type_

**Request example — Update a time type:**
```json
{
  "status": "active"
}
```
**Response 200 — Reference to updated time type:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Overtime",
    "href": "/objects/time/time-type/10"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0
  }
}
```

## DELETE /objects/time/time-type/{key}
_Delete a time type_


## GET /objects/time/timesheet
_List timesheets_

**Response 200 — List of timesheets:**
```json
{
  "ia::result": [
    {
      "key": "101",
      "id": "101",
      "href": "/objects/time/timesheet/101"
    },
    {
      "key": "102",
      "id": "102",
      "href": "/objects/time/timesheet/102"
    },
    {
      "key": "103",
      "id": "103",
      "href": "/objects/time/timesheet/103"
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

## POST /objects/time/timesheet
_Create a timesheet_

**Request example — Create a timesheet:**
```json
{
  "beginDate": "2024-01-01",
  "state": "submitted",
  "description": "Week of 01/01/24",
  "employee": {
    "key": "973"
  },
  "attachment": {
    "key": "8420"
  },
  "lines": [
    {
      "dimensions": {
        "department": {
          "key": "11"
        },
        "location": {
          "key": "22"
        },
        "project": {
          "key": "1"
        },
        "costType": {
          "key": "2"
        },
        "task": {
          "key": "1"
        },
        "customer": {
          "key": "13"
        },
        "item": {
          "key": "13"
        }
      },
      "entryDate": "2024-04-01",
      "quantity": 6,
      "description": "Week of 04/01/24",
      "notes": "Talked to client regarding project",
      "timeType": {
        "key": "1"
      },
      "isBillable": true
    }
  ]
}
```
**Response 201 — Reference to new timesheet:**
```json
{
  "ia::result": {
    "key": "40",
    "id": "40",
    "href": "/objects/time/timesheet/40"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/time/timesheet-approval-record
_List timesheet approval records_

**Response 200 — List timesheet approval records:**
```json
{
  "ia::result": [
    {
      "key": "46",
      "id": "46",
      "href": "/objects/time/timesheet-approval-record/46"
    },
    {
      "key": "44",
      "id": "44",
      "href": "/objects/time/timesheet-approval-record/44"
    },
    {
      "key": "40",
      "id": "40",
      "href": "/objects/time/timesheet-approval-record/40"
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

## GET /objects/time/timesheet-approval-record/{key}
_Get a timesheet approval record_

**Response 200 — Get a timesheet approval record:**
```json
{
  "ia::result": {
    "key": "200",
    "id": "200",
    "href": "/objects/time/timesheet-approval-record/200",
    "approvalStage": 1,
    "approvalType": "Department Approval",
    "approvalLevel": "2",
    "comments": "Approved by Admin",
    "recordDate": "2021-01-23",
    "state": "submitted",
    "timesheet": {
      "key": "101",
      "id": "101",
      "href": "/objects/time/timesheet/101"
    },
    "timesheetLine": {
      "key": "142",
      "id": "142",
      "lineNumber": 3,
      "href": "/objects/time/timesheet-line/142"
    },
    "approvedBy": {
      "key": "202",
      "id": "cjackson",
      "href": "/objects/company-config/user/202"
    },
    "approver": {
      "key": "203",
      "id": "jlee",
      "href": "/objects/company-config/user/203"
    },
    "completedBy": {
      "key": "204",
      "id": "gadams",
      "href": "/objects/company-config/user/204"
    },
    "initiatedBy": {
      "key": "205",
      "id": "vluce",
      "href": "/objects/company-config/user/205"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/time/timesheet-line
_List timesheet lines_

**Response 200 — List of timesheet lines:**
```json
{
  "ia::result": [
    {
      "key": "4101",
      "id": "4101",
      "href": "/objects/time/timesheet-line/4101"
    },
    {
      "key": "4102",
      "id": "4102",
      "href": "/objects/time/timesheet-line/4102"
    },
    {
      "key": "4103",
      "id": "4103",
      "href": "/objects/time/timesheet-line/4103"
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

## POST /objects/time/timesheet-line
_Create a timesheet line_

**Request example — Creates a timesheet line:**
```json
{
  "timesheet": {
    "key": "11"
  },
  "dimensions": {
    "department": {
      "key": "11"
    },
    "location": {
      "key": "22"
    },
    "project": {
      "key": "1"
    },
    "costType": {
      "key": "2"
    },
    "task": {
      "key": "1"
    },
    "customer": {
      "key": "13"
    },
    "item": {
      "key": "13"
    }
  },
  "entryDate": "2024-04-01",
  "quantity": 6,
  "description": "Week of 04/01/24",
  "notes": "Talked to client regarding project",
  "timeType": {
    "key": "1"
  },
  "isBillable": true
}
```
**Response 201 — Reference to new timesheet line:**
```json
{
  "ia::result": {
    "key": "4108",
    "id": "4108",
    "href": "/objects/time/timesheet-line/4108"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/time/timesheet-line/{key}
_Get a timesheet line_

**Response 200 — Get a timesheet line:**
```json
{
  "ia::result": {
    "key": "1411",
    "id": "1411",
    "href": "/objects/time/timesheet-line/1411",
    "timesheet": {
      "key": "11",
      "id": "11",
      "href": "/objects/time/timesheet/11"
    },
    "dimensions": {
      "employee": {
        "key": "10",
        "id": "EMP-10",
        "name": "Thomas, Glenn",
        "href": "/objects/company-config/employee/10"
      },
      "department": {
        "key": "11",
        "id": "DEP-11",
        "name": "Sales and Marketing",
        "href": "/objects/company-config/department/11"
      },
      "location": {
        "key": "22",
        "id": "LOC-22",
        "name": "California",
        "href": "/objects/company-config/location/22"
      },
      "project": {
        "key": "1",
        "id": "Proj-001",
        "name": "Implementation",
        "href": "/objects/projects/project/1"
      },
      "costType": {
        "key": "2",
        "id": "2",
        "name": "Project Expense",
        "href": "/objects/construction/cost-type/2"
      },
      "task": {
        "id": "1",
        "key": "1",
        "name": "Project Task",
        "href": "/objects/projects/task/1"
      },
      "customer": {
        "key": "13",
        "id": "CUST-13",
        "name": "Jack In the Box",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "item": {
        "key": "13",
        "id": "Case 13",
        "name": "Platform pack",
        "href": "/objects/inventory-control/item/13"
      }
    },
    "entryDate": "2024-04-01",
    "quantity": 6,
    "lineNumber": 1,
    "description": "Week of 04/01/24",
    "notes": "Talked to client regarding project",
    "state": "approved",
    "timeType": {
      "key": "1",
      "id": "Salaries At Root",
      "href": "/objects/time/time-type/1"
    },
    "isBillable": true,
    "isBilled": "false",
    "statisticalJournal": {
      "key": "7483",
      "id": "TSSJ",
      "href": "/objects/general-ledger/statistical-account/10"
    },
    "billableUtilizedAccount": {
      "key": "8293",
      "id": "9293",
      "href": "/objects/general-ledger/statistical-account/8293"
    },
    "nonBbillableUtilizedAccount": {
      "key": "8294",
      "id": "9294",
      "href": "/objects/general-ledger/statistical-account/8294"
    },
    "billableNonUtilizedAccount": {
      "key": "8295",
      "id": "9295",
      "href": "/objects/general-ledger/statistical-account/8295"
    },
    "nonBillableNonUtilizedAccount": {
      "key": "8296",
      "id": "9296",
      "href": "/objects/general-ledger/statistical-account/8296"
    },
    "hours": {
      "billable": 8,
      "nonBillable": 2,
      "approved": 10,
      "approvedBillable": 8,
      "approvedNonBillable": 2,
      "utilized": 10,
      "nonUtilized": 4,
      "approvedUtilized": 3,
      "approvedNonUtilized": 2
    },
    "externalPayroll": {
      "costRate": 1,
      "billingRate": 1,
      "amount": "90",
      "employerTaxes": 15,
      "fringes": 10,
      "cashFringes": 2
    },
    "laborClass": {
      "key": "15",
      "id": "LC001",
      "name": "Labor Class",
      "href": "/objects/construction/labor-class/15"
    },
    "laborShift": {
      "key": "18",
      "id": "LS001",
      "name": "Labor Shift",
      "href": "/objects/construction/labor-class/18"
    },
    "laborUnion": {
      "key": "20",
      "id": "LU001",
      "name": "Labor Union",
      "href": "/objects/construction/labor-class/20"
    },
    "audit": {
      "createdDateTime": "2022-04-20T16:20:00Z",
      "modifiedDateTime": "2022-04-20T16:20:00Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "95",
        "id": "Hal",
        "href": "/objects/company-config/user/95"
      },
      "modifiedBy": "95"
    }
  },
  "ia::meta": {
    "totalCount": 3
  }
}
```

## PATCH /objects/time/timesheet-line/{key}
_Update a timesheet line_

**Request example — Updates a timesheet line:**
```json
{
  "key": "40",
  "description": "Week of 04/01/24",
  "notes": "Talked to client regarding project"
}
```
**Response 200 — Reference to updated timesheet line:**
```json
{
  "ia::result": {
    "key": "40",
    "id": "40",
    "href": "/objects/time/timesheet-line/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalFailure": 0
  }
}
```

## DELETE /objects/time/timesheet-line/{key}
_Delete a timesheet line_


## GET /objects/time/timesheet-rule
_List timersheet rules_

**Response 200 — List timesheet rule:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/time/timesheet-rule/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/time/timesheet-rule/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/time/timesheet-rule
_Create a timesheet rule_

**Request example — Create a new timesheet rule:**
```json
{
  "name": "Holiday schedule 2022",
  "businessDays": [
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY"
  ],
  "weekends": [
    "SATURDAY",
    "SUNDAY"
  ],
  "startDate": "2022-01-01",
  "endDate": "2022-12-31",
  "requireNotes": false,
  "doNotAllowOnHolidays": false,
  "timesheetRuleEmployees": [
    {
      "key": "22"
    },
    {
      "key": "27"
    },
    {
      "id": "JSmith"
    }
  ]
}
```
**Response 201 — Reference to new timesheet rule:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "3",
    "href": "/objects/time/timesheet-rule/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/time/timesheet-rule/{key}
_Get a timesheet rule_

**Response 200 — Details of the timesheet rule:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "name": "Time sheet of my company",
    "businessDays": [
      "MONDAY",
      "TUESDAY",
      "WEDNESDAY",
      "THURSDAY",
      "FRIDAY"
    ],
    "weekends": [
      "SATURDAY",
      "SUNDAY"
    ],
    "startDate": "2024-02-01",
    "endDate": "2024-10-01",
    "minHoursPerWorkDay": "2.5",
    "maxHoursPerWorkDay": "8",
    "minHoursForApproval": "1.5",
    "maxHoursForApproval": "8",
    "minHoursPerWeekend": "2",
    "maxHoursPerWeekend": "4",
    "requireNotes": false,
    "doNotAllowOnHolidays": false,
    "status": "active",
    "href": "/objects/time/timesheet-rule/2",
    "timesheetRuleEmployees": [
      {
        "key": "23",
        "id": "jsmith",
        "name": "Smith, John",
        "href": "/objects/company-config/employee/23"
      },
      {
        "key": "25",
        "id": "abrown",
        "name": "Brown, Angela",
        "href": "/objects/company-config/employee/25"
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

## PATCH /objects/time/timesheet-rule/{key}
_Update a timesheet rule_

**Request example — Update a timesheet rule:**
```json
{
  "name": "Time Schedule for 2024",
  "timesheetRuleEmployees": [
    {
      "key": "24"
    },
    {
      "id": "MGR1"
    }
  ]
}
```
**Response 200 — Reference to updated timesheet rule:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/time/timesheet-rule/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/time/timesheet-rule/{key}
_Delete a timesheet rule_


## GET /objects/time/timesheet-to-approve
_List timesheets to approve_

**Response 200 — List timesheets to approve:**
```json
{
  "ia::result": [
    {
      "key": "101",
      "id": "101",
      "href": "/objects/time/timesheet-to-approve/101"
    },
    {
      "key": "102",
      "id": "102",
      "href": "/objects/time/timesheet-to-approve/102"
    },
    {
      "key": "103",
      "id": "103",
      "href": "/objects/time/timesheet-to-approve/103"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0,
    "start": 1,
    "pageSize": 100,
    "next": 0,
    "previous": 0
  }
}
```

## GET /objects/time/timesheet-to-approve/{key}
_Get a timesheet to approve_

**Response 200 — Details of the timesheet to approve:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "23",
    "href": "/objects/projects/timesheet/23",
    "beginDate": "2025-01-01",
    "endDate": "2025-01-07",
    "postingDate": "2025-01-07",
    "state": "submitted",
    "unitOfMeasure": "Hours",
    "hoursInDay": 8,
    "billableQuantity": 40,
    "nonBillableQuantity": 2,
    "description": "Week of 2025-01-01",
    "calculationMethod": "hourly",
    "postActualLaborCost": false,
    "employee": {
      "key": "973",
      "id": "E-001",
      "href": "/objects/company-config/employee/973"
    },
    "employeeContact": {
      "key": "973",
      "name": "John Smith",
      "firstName": "John",
      "lastName": "Smith",
      "href": "/objects/company-config/contact/973"
    },
    "attachment": {
      "key": "8420",
      "id": "Attach-01",
      "href": "string"
    },
    "lines": [
      {
        "key": "1411",
        "id": "1411",
        "href": "/objects/time/timesheet-to-approve-line/1411",
        "timesheetToApprove": {
          "key": "11",
          "id": "11",
          "href": "/objects/time/timesheet-to-approve/11"
        },
        "entryDate": "2025-04-01",
        "quantity": 6,
        "lineNumber": 1,
        "description": "Week of 04/01/23",
        "notes": "Talked to client regarding project",
        "state": "approved",
        "timeType": {
          "key": "1",
          "id": "Salaries At Root",
          "name": "Salaries At Root",
          "href": "/objects/projects/time-type/1"
        },
        "isBillable": true,
        "isBilled": "false",
        "statisticalJournal": {
          "key": "7483",
          "id": "TSSJ",
          "href": "/objects/general-ledger/statistical-journal/7483"
        },
        "billableUtilizedGLAccount": {
          "key": "8293",
          "id": "9293",
          "href": "/objects/general-ledger/statistical-account/8293"
        },
        "nonBillableUtilizedGLAccount": {
          "key": "8294",
          "id": "9294",
          "href": "/objects/general-ledger/statistical-account/8294"
        },
        "billableNonUtilizedGLAccount": {
          "key": "8295",
          "id": "9295",
          "href": "/objects/general-ledger/statistical-account/8295"
        },
        "nonBillableNonUtilizedGLAccount": {
          "key": "8296",
          "id": "9296",
          "href": "/objects/general-ledger/statistical-account/8296"
        },
        "hours": {
          "billable": 8,
          "nonBillable": 2,
          "approved": 10,
          "approvedBillable": 8,
          "approvedNonBillable": 2,
          "utilized": 10,
          "nonUtilized": 4,
          "approvedUtilized": 3,
          "approvedNonUtilized": 2
        },
        "externalPayroll": {
          "costRate": 1,
          "billingRate": 1,
          "amount": "90",
          "employerTaxes": 15,
          "fringes": 10,
          "cashFringes": 2
        },
        "laborClass": {
          "key": "15",
          "id": "LC001",
          "name": "Labor Class",
          "href": "/objects/construction/labor-class/15"
        },
        "laborShift": {
          "key": "18",
          "id": "LS001",
          "name": "Labor Shift",
          "href": "/objects/construction/labor-shift/18"
        },
        "laborUnion": {
          "key": "20",
          "id": "LU001",
          "name": "Labor Union",
          "href": "/objects/construction/labor-union/20"
        },
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "name": "USA"
          },
          "department": {
            "key": "1",
            "id": "1",
            "name": "IT"
          },
          "employee": {
            "key": "10",
            "id": "EMP-10",
            "name": "Thomas, Glenn",
            "href": "/objects/company-config/employee/10"
          },
          "project": {
            "key": "2",
            "id": "NET-XML30-2",
            "name": "Talcomp training",
            "href": "/objects/projects/project/2"
          },
          "customer": {
            "key": "13",
            "id": "CUST-13",
            "name": "Jack In the Box",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "GenLab",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "item": {
            "key": "13",
            "id": "Case 13",
            "name": "Platform pack",
            "href": "/objects/inventory-control/item/13"
          },
          "warehouse": {
            "key": "6",
            "id": "WH01",
            "name": "WH01",
            "href": "/objects/inventory-control/warehouse/6"
          },
          "class": {
            "key": "731",
            "id": "REST_CLS_001",
            "name": "Enterprises",
            "href": "/objects/company-config/class/731"
          },
          "task": {
            "id": "1",
            "key": "1",
            "name": "Project Task",
            "href": "/objects/projects/task/1"
          },
          "costType": {
            "id": "2",
            "key": "2",
            "name": "Project Expense",
            "href": "/objects/construction/cost-type/2"
          },
          "asset": {
            "id": "A001",
            "key": "1",
            "name": "Laptop 1",
            "href": "/objects/asset/1"
          },
          "contract": {
            "id": "CON-0045-1",
            "key": "12",
            "name": "ACME Widgets - Service",
            "href": "/objects/contracts/contract/12"
          }
        },
        "audit": {
          "createdDateTime": "2022-04-20T16:20:00Z",
          "modifiedDateTime": "2022-04-20T16:20:00Z",
          "createdBy": "1",
          "modifiedBy": "95"
        },
        "entity": {
          "key": "46",
          "id": "Western Region",
          "name": "Western Region",
          "href": "/objects/company-config/entity/46"
        }
      }
    ],
    "audit": {
      "createdDateTime": "2022-04-20T16:20:00Z",
      "modifiedDateTime": "2022-04-20T16:20:00Z",
      "createdBy": "1",
      "modifiedBy": "95"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/time/timesheet/{key}
_Get a timesheet_

**Response 200 — Get a timesheet:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "23",
    "href": "/objects/time/timesheet/23",
    "beginDate": "2024-01-01",
    "endDate": "2024-12-31",
    "postingDate": "2024-01-01",
    "state": "submitted",
    "unitOfMeasure": "Hours",
    "hoursInDay": 8,
    "description": "Week of 01/01/24",
    "calculationMethod": "hourly",
    "postActualLaborCost": false,
    "employee": {
      "key": "973",
      "id": "E-001",
      "href": "/objects/company-config/employee/973"
    },
    "employeeContact": {
      "key": "977",
      "id": "John Smith",
      "firstName": "John",
      "lastName": "Smith",
      "href": "/objects/company-config/contact/977"
    },
    "attachment": {
      "key": "8420",
      "id": "Attach-01",
      "href": "/objects/company-config/attachment/973"
    },
    "employeeClassId": "EMP_CLS_001",
    "employeeDepartmentId": "DEP-11",
    "employeeLocation": {
      "key": "22",
      "id": "LOC-22",
      "href": "/objects/company-config/location/22"
    },
    "employeePositionId": "MGR",
    "lines": [
      {
        "key": "1411",
        "id": "1411",
        "href": "/objects/time/timesheet-line/1411",
        "timesheet": {
          "key": "11",
          "id": "11",
          "href": "/objects/time/timesheet/11"
        },
        "dimensions": {
          "department": {
            "key": "11",
            "id": "DEP-11",
            "name": "Sales and Marketing",
            "href": "/objects/company-config/department/11"
          },
          "location": {
            "key": "22",
            "id": "LOC-22",
            "name": "California",
            "href": "/objects/company-config/location/22"
          },
          "employee": {
            "key": "10",
            "id": "EMP-10",
            "name": "Garcia, John",
            "href": "/objects/company-config/employee/10"
          },
          "project": {
            "key": "1",
            "id": "Proj-001",
            "name": "Implementation",
            "href": "/objects/projects/project/1"
          },
          "costType": {
            "id": "2",
            "key": "2",
            "name": "Project Expense",
            "href": "/objects/construction/cost-type/2"
          },
          "task": {
            "id": "1",
            "key": "1",
            "name": "Project Task",
            "href": "/objects/projects/task/1"
          },
          "customer": {
            "key": "13",
            "id": "CUST-13",
            "name": "Jack In the Box",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "item": {
            "key": "13",
            "id": "Case 13",
            "name": "Platform pack",
            "href": "/objects/inventory-control/item/13"
          }
        },
        "entryDate": "2024-04-01",
        "quantity": 6,
        "lineNumber": 1,
        "description": "Week of 04/01/24",
        "notes": "Talked to client regarding project",
        "state": "approved",
        "timeType": {
          "key": "1",
          "id": "Salaries At Root",
          "name": "Salaries At Root",
          "href": "/objects/time/time-type/1"
        },
        "isBillable": true,
        "isBilled": "false",
        "statisticalJournal": {
          "key": "7483",
          "id": "7483",
          "href": "/objects/company-config/employee/10"
        },
        "billableUtilizedAccount": {
          "key": "8293",
          "id": "8293",
          "href": "/objects/general-ledger/statistical-account/8293"
        },
        "nonBbillableUtilizedAccount": {
          "key": "8294",
          "id": "8294",
          "href": "/objects/general-ledger/statistical-account/8294"
        },
        "billableNonUtilizedAccount": {
          "key": "8295",
          "id": "8295",
          "href": "/objects/general-ledger/statistical-account/8295"
        },
        "nonBillableNonUtilizedAccount": {
          "key": "8296",
          "id": "8296",
          "href": "/objects/general-ledger/statistical-account/8296"
        },
        "hours": {
          "billable": 8,
          "nonBillable": 2,
          "approved": 10,
          "approvedBillable": 8,
          "approvedNonBillable": 2,
          "utilized": 10,
          "nonUtilized": 4,
          "approvedUtilized": 3,
          "approvedNonUtilized": 2
        },
        "externalPayroll": {
          "costRate": 1,
          "billingRate": 1,
          "amount": "90",
          "employerTaxes": 15,
          "fringes": 10,
          "cashFringes": 2
        },
        "laborClass": {
          "key": "15",
          "id": "15",
          "name": "Labor Class",
          "href": "/objects/construction/labor-class/15"
        },
        "audit": {
          "createdDateTime": "2022-04-20T16:20:00Z",
          "modifiedDateTime": "2022-04-20T16:20:00Z",
          "createdByUser": {
            "key": "1",
            "id": "Admin",
            "href": "/objects/company-config/user/1"
          },
          "createdBy": "1",
          "modifiedByUser": {
            "key": "95",
            "id": "Hal",
            "href": "/objects/company-config/user/95"
          },
          "modifiedBy": "95"
        },
        "entity": {
          "key": "46",
          "id": "Western Region",
          "name": "Western Region",
          "href": "/objects/company-config/entity/46"
        }
      }
    ],
    "audit": {
      "createdDateTime": "2022-04-20T16:20:00Z",
      "modifiedDateTime": "2022-04-20T16:20:00Z",
      "createdBy": "1",
      "modifiedBy": "95"
    }
  },
  "ia::meta": {
    "totalCount": 3
  }
}
```

## PATCH /objects/time/timesheet/{key}
_Update a timesheet_

**Request example — Updates a timesheet:**
```json
{
  "state": "submitted",
  "description": "Week of 01/01/24"
}
```
**Response 200 — Reference to updated timesheet:**
```json
{
  "ia::result": {
    "key": "40",
    "id": "40",
    "href": "/objects/time/timesheet/40"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/time/timesheet/{key}
_Delete a timesheet_

