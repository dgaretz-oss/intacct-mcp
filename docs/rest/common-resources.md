# Common Resources

## GET /objects/core/operation
_List operations_

**Response 200 — 200 response example:**
```json
{
  "ia::result": [
    {
      "key": "12345",
      "id": "ID123",
      "href": "/objects/<application>/<name>/12345"
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

## POST /objects/core/operation
_Create an operation_

**Request example — Request Example:**
```json
{
  "id": "Monthly inventory check",
  "description": "Monthly inventory check for organic produce",
  "userKey": 23,
  "entity": "string",
  "action": "checkInventory",
  "bodyData": "Check inventory",
  "moduleKey": "orderEntry",
  "locationKey": "string",
  "contactEmail": "admin@company.org",
  "userInfo": "adminUser",
  "status": "active"
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

## GET /objects/core/operation/{key}
_Get an operation_

**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "Monthly inventory check",
    "description": "Monthly inventory check for organic produce",
    "userKey": 23,
    "entity": "string",
    "action": "checkInventory",
    "bodyData": "Check inventory",
    "moduleKey": "orderEntry",
    "locationKey": "string",
    "contactEmail": "admin@company.org",
    "userInfo": "adminUser",
    "href": "/objects/core/operation/23",
    "status": "active"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## PATCH /objects/core/operation/{key}
_Update an operation_

**Request example — Request Example:**
```json
{
  "description": "Monthly inventory check for organic produce",
  "userKey": 23,
  "entity": "string",
  "action": "checkInventory",
  "bodyData": "Check inventory",
  "moduleKey": "orderEntry",
  "locationKey": "string",
  "contactEmail": "admin@company.org",
  "userInfo": "adminUser",
  "status": "active"
}
```
**Response 200 — 200 response example:**
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

## DELETE /objects/core/operation/{key}
_Delete an operation_


## GET /objects/core/schedule
_List schedules_

**Response 200 — 200 response example:**
```json
{
  "ia::result": [
    {
      "key": "12345",
      "id": "ID123",
      "href": "/objects/<application>/<name>/12345"
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

## POST /objects/core/schedule
_Create a schedule_

**Request example — Request Example:**
```json
{
  "id": "Monthly installment billing",
  "description": "Monthly installment billing for organic produce",
  "executionType": "automatic",
  "startDate": "2024-06-01",
  "endDate": "2025-06-01",
  "repeatBy": "month",
  "repeatDate": 3,
  "repeatInterval": 2,
  "repeatCount": 5,
  "nextExecutionDate": "2025-04-01",
  "lastExecutionDate": "2025-06-01",
  "dueDate": "2025-06-01",
  "executionCount": 12,
  "cronID": "234",
  "startOn": 15,
  "endOn": 7,
  "userinfo": "Admin",
  "status": "active"
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

## GET /objects/core/schedule/{key}
_Get a schedule_

**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "34",
    "id": "Monthly installment billing",
    "description": "Monthly installment billing for organic produce",
    "executionType": "automatic",
    "startDate": "2024-06-01",
    "endDate": "2025-06-01",
    "repeatBy": "month",
    "repeatDate": 3,
    "repeatInterval": 2,
    "repeatCount": 5,
    "nextExecutionDate": "2025-04-01",
    "lastExecutionDate": "2025-06-01",
    "dueDate": "2025-06-01",
    "executionCount": 12,
    "cronID": "234",
    "startOn": 15,
    "endOn": 7,
    "userinfo": "Admin",
    "href": "/objects/core/schedule/234",
    "status": "active"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## PATCH /objects/core/schedule/{key}
_Update a schedule_

**Request example — Request Example:**
```json
{
  "description": "Monthly installment billing for organic produce",
  "executionType": "automatic",
  "startDate": "2024-06-01",
  "endDate": "2025-06-01",
  "repeatBy": "month",
  "repeatDate": 3,
  "repeatInterval": 2,
  "repeatCount": 5,
  "nextExecutionDate": "2025-04-01",
  "lastExecutionDate": "2025-06-01",
  "dueDate": "2025-06-01",
  "executionCount": 12,
  "cronID": "234",
  "startOn": 15,
  "endOn": 7,
  "userinfo": "Admin",
  "status": "active"
}
```
**Response 200 — 200 response example:**
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

## DELETE /objects/core/schedule/{key}
_Delete a schedule_


## GET /objects/core/scheduled-operation
_List scheduled operations_

**Response 200 — 200 response example:**
```json
{
  "ia::result": [
    {
      "key": "12345",
      "id": "ID123",
      "href": "/objects/<application>/<name>/12345"
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

## POST /objects/core/scheduled-operation
_Create a scheduled operation_

**Request example — Request Example:**
```json
{
  "id": "string",
  "scheduleKey": 83,
  "operationKey": 234,
  "description": "string",
  "operation": {
    "key": "234",
    "id": "Generate monthly invoice"
  },
  "schedule": {
    "key": "83",
    "id": "Monthly invoice generation",
    "nextScheduledDate": "2025-07-01"
  },
  "userinfo": "admin",
  "status": "active"
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

## GET /objects/core/scheduled-operation/{key}
_Get a scheduled operation_

**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "key": "string",
    "id": "string",
    "scheduleKey": 83,
    "operationKey": 234,
    "description": "string",
    "operation": {
      "key": "234",
      "id": "Generate monthly invoice",
      "href": "/objects/core/operation/234"
    },
    "schedule": {
      "key": "83",
      "id": "Monthly invoice generation",
      "nextScheduledDate": "2025-07-01",
      "href": "/objects/core/schedule/83"
    },
    "userinfo": "admin",
    "href": "/objects/core/scheduled-operation/234",
    "status": "active"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## PATCH /objects/core/scheduled-operation/{key}
_Update a scheduled operation_

**Request example — Request Example:**
```json
{
  "scheduleKey": 83,
  "operationKey": 234,
  "description": "string",
  "operation": {
    "key": "234",
    "id": "Generate monthly invoice"
  },
  "schedule": {
    "key": "83",
    "id": "Monthly invoice generation",
    "nextScheduledDate": "2025-07-01"
  },
  "userinfo": "admin",
  "status": "active"
}
```
**Response 200 — 200 response example:**
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

## DELETE /objects/core/scheduled-operation/{key}
_Delete a scheduled operation_


## GET /objects/core/system-view
_Get a system view_

**Response 200 — A single system view:**
```json
{
  "ia::result": {
    "contexts": [
      "__default"
    ],
    "description": "IA.ALL_ACTIVE_EMPLOYEE_EXPENSES",
    "id": "systemfw1",
    "key": "expenses/employee-expense::systemfw1",
    "name": "IA.ALL",
    "object": "expenses/employee-expense",
    "query": {
      "fields": [
        "id",
        "employeeContact.lastName",
        "employeeContact.firstName",
        "createdDate",
        "expenseReportNumber",
        "reimbursement.totalEntered",
        "nonReimbursable.reimbursementTotalEntered",
        "reimbursement.reimbursementCurrency",
        "basePayment.totalEntered",
        "state"
      ],
      "object": "expenses/employee-expense",
      "orderBy": [
        {
          "createdDate": "desc"
        }
      ]
    },
    "href": "/objects/core/system-view?name=expenses/employee-expense::systemfw1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — All views for an object:**
```json
{
  "ia::result": [
    {
      "contexts": [
        "__default"
      ],
      "description": "IA.ALL_ACTIVE_EMPLOYEE_EXPENSES",
      "id": "systemfw1",
      "key": "expenses/employee-expense::systemfw1",
      "name": "IA.ALL",
      "object": "expenses/employee-expense",
      "query": {
        "fields": [
          "id",
          "employeeContact.lastName",
          "employeeContact.firstName",
          "createdDate",
          "expenseReportNumber",
          "reimbursement.totalEntered",
          "nonReimbursable.reimbursementTotalEntered",
          "reimbursement.reimbursementCurrency",
          "basePayment.totalEntered",
          "state"
        ],
        "object": "expenses/employee-expense",
        "orderBy": [
          {
            "createdDate": "desc"
          }
        ]
      },
      "href": "/objects/core/system-view?name=expenses/employee-expense::systemfw1"
    },
    {
      "contexts": [
        "__default"
      ],
      "description": "IA.ALL_RECENTLY_MODIFIED",
      "id": "systemfw2",
      "key": "expenses/employee-expense::systemfw2",
      "name": "IA.RECENTLY_MODIFIED",
      "object": "expenses/employee-expense",
      "query": {
        "fields": [
          "id",
          "employeeContact.lastName",
          "employeeContact.firstName",
          "createdDate",
          "expenseReportNumber",
          "reimbursement.totalEntered",
          "nonReimbursable.reimbursementTotalEntered",
          "reimbursement.reimbursementCurrency",
          "basePayment.totalEntered",
          "state",
          "audit.modifiedDateTime",
          "audit.modifiedBy"
        ],
        "object": "expenses/employee-expense",
        "orderBy": [
          {
            "audit.modifiedDateTime": "desc"
          }
        ]
      },
      "href": "/objects/core/system-view?name=expenses/employee-expense::systemfw2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## GET /objects/core/txn-definition
_List transaction definitions_

**Response 200 — List transaction definitions:**
```json
{
  "ia::result": [
    {
      "key": "33",
      "id": "33",
      "href": "/objects/core/txn-definition/33"
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

## POST /objects/core/txn-definition
_Create a transaction definition_

**Request example — example-1:**
```json
{
  "id": "Sales Invoice"
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

## GET /objects/core/txn-definition/{key}
_Get a transaction definition_

**Response 200 — Get a transaction definition:**
```json
{
  "ia::result": {
    "key": "154",
    "id": "Sales Invoice",
    "href": "/objects/core/txn-definition/154"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/core/txn-definition/{key}
_Update a transaction definition_

**Request example — Update a transaction definition:**
```json
{
  "key": "154",
  "id": "true"
}
```
**Response 200 — Reference to updated transaction definition:**
```json
{
  "ia::result": {
    "key": "33",
    "id": "33",
    "href": "/objects/core/txn-definition/33"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/core/txn-definition/{key}
_Delete a transaction definition_


## GET /objects/core/user-view
_List user views_

**Response 200 — List of user views:**
```json
{
  "ia::result": [
    {
      "key": "9",
      "id": "9",
      "href": "/objects/core/user-view/9"
    },
    {
      "key": "6",
      "id": "6",
      "href": "/objects/core/user-view/6"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/core/user-view/5"
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

## POST /objects/core/user-view
_Create a user view_

**Request example — User view for vendor:**
```json
{
  "name": "Inactive vendors",
  "query": {
    "object": "accounts-payable/vendor",
    "fields": [
      "id",
      "name",
      "status",
      "href"
    ],
    "filters": [
      {
        "$eq": {
          "status": "inactive"
        }
      },
      {
        "$eq": {
          "billingType": "balanceForward"
        }
      }
    ],
    "filterExpression": "1 and 2",
    "orderBy": [
      {
        "id": "desc"
      }
    ]
  }
}
```
**Response 201 — Reference to new user view:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "9",
    "href": "/objects/core/user-view/9"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/core/user-view/{key}
_Get a user view_

**Response 200 — User view details:**
```json
{
  "ia::result": {
    "key": "262",
    "id": "262",
    "name": "Active vendors",
    "description": "Active vendors with open billing items",
    "category": null,
    "owner": {
      "key": "1",
      "id": "Admin",
      "href": "/objects/company-config/user/1"
    },
    "object": "accounts-payable/vendor",
    "query": {
      "object": "accounts-payable/vendor",
      "fields": [
        "id",
        "name",
        "status",
        "href"
      ],
      "filters": [
        {
          "$eq": {
            "status": "active"
          }
        },
        {
          "$eq": {
            "billingType": "openItem"
          }
        }
      ],
      "filterExpression": "1 and 2",
      "orderBy": [
        {
          "id": "asc"
        }
      ]
    },
    "status": "active",
    "viewVersion": "0",
    "audit": {
      "createdDateTime": "2025-05-16T17:41:55Z",
      "modifiedDateTime": "2025-05-17T17:41:55Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "href": "/objects/core/user-view/262"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/core/user-view/{key}
_Update a user view_

**Request example — Update query and metadata:**
```json
{
  "query": {
    "object": "company-config/employee",
    "fields": [
      "key",
      "primaryContact.lastName",
      "primaryContact.prefix",
      "primaryContact.firstName",
      "primaryContact.id",
      "startDate"
    ],
    "filters": [
      {
        "$eq": {
          "status": "active"
        }
      },
      {
        "$eq": {
          "startDate": "currentYear"
        }
      }
    ],
    "filterExpression": "and",
    "orderBy": [
      {
        "primaryContact.lastName": "asc"
      }
    ],
    "filterParameters": {
      "includeHierarchyFields": false
    }
  },
  "metadata": {
    "columns": [
      {
        "id": "primaryContact.lastName",
        "textFormat": "clip"
      },
      {
        "id": "primaryContact.prefix",
        "textFormat": "wrap"
      },
      {
        "id": "primaryContact.firstName",
        "textFormat": "clip"
      },
      {
        "id": "primaryContact.id",
        "textFormat": "wrap"
      },
      {
        "id": "status",
        "textFormat": "clip"
      }
    ],
    "frozenColumnCount": 1
  }
}
```
**Response 200 — Reference to updated user view:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "8",
    "href": "/objects/core/user-view/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/core/user-view/{key}
_Delete a user view_


## POST /services/bulk/job/create
_Send a bulk request_

**Request example — Request Example:**
```json
{
  "objectName": "vendor",
  "operation": "create",
  "jobFile": "vendor.csv",
  "fileContentType": "json",
  "callbackURL": "https://example.com/callback"
}
```
**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "jobId": "950bf10d-f119-41c9-a352-1b68b34498c3",
    "statusURL": "/services/bulk/job/status?jobId=950bf10d-f119-41c9-a352-1b68b34498c3",
    "createdDateTime": "2023-08-01T01:20:30"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## GET /services/bulk/job/status
_Get a bulk request status_

**Response 200 — 200 response example:**
```json
{
  "ia::result": {
    "jobId": "950bf10d-f119-41c9-a352-1b68b34498c3",
    "status": "completed",
    "percentComplete": 100,
    "downloadURL": "/services/bulk/job/status?jobId=950bf10d-f119-41c9-a352-1b68b34498c3&download=true",
    "jobStatusFile": "950bf10d-f119-41c9-a352-1b68b34498c3-response.json"
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## POST /services/core/allowed-operations/list
_Get allowed operations_

**Request example — Get allowed operations for specified vendors:**
```json
{
  "object": "accounts-payable/vendor",
  "keys": [
    "1",
    "6",
    "65"
  ],
  "operations": [
    "canView",
    "canEdit",
    "canDelete"
  ],
  "options": {
    "includePrivate": true
  },
  "additionalData": {
    "requestType": "vendor-list"
  }
}
```
**Response 200 — Vendor Allowed Operations Response:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "operations": [
        "canView",
        "canEdit",
        "canDelete"
      ],
      "additionalData": {
        "operationCode": 123
      }
    },
    {
      "key": "6",
      "operations": [
        "canView",
        "canEdit"
      ],
      "additionalData": {
        "operationCode": 0
      }
    },
    {
      "key": "65",
      "operations": [
        "canView"
      ],
      "additionalData": {
        "operationCode": 150
      }
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/core/composite
_Send a composite request_

**Request example — Multiple independent requests to change employee location:**
```json
[
  {
    "method": "PATCH",
    "path": "/objects/company-config/employee/26",
    "body": {
      "location": {
        "key": "6"
      }
    }
  },
  {
    "method": "PATCH",
    "path": "/objects/company-config/employee/33",
    "body": {
      "location": {
        "key": "6"
      }
    }
  },
  {
    "method": "PATCH",
    "path": "/objects/company-config/employee/62",
    "body": {
      "location": {
        "key": "6"
      }
    }
  }
]
```
**Request example — Multiple requests using data from previous:**
```json
[
  {
    "method": "GET",
    "path": "/objects/company-config/employee/52",
    "resultReference": "employee"
  },
  {
    "method": "POST",
    "path": "/services/core/query",
    "body": {
      "object": "employee",
      "fields": [
        "id",
        "jobTitle",
        "department.key",
        "employeeType.id"
      ],
      "filters": [
        {
          "$eq": {
            "department.key": "@{employee.department.key}"
          }
        },
        {
          "$eq": {
            "employeeType.id": "@{employee.employeeType.id}"
          }
        }
      ],
      "filterExpression": "1 and 2",
      "orderBy": [
        {
          "id": "asc"
        }
      ]
    }
  }
]
```
**Request example — Multi-status example:**
```json
[
  {
    "method": "GET",
    "path": "/services/core/async/job-status?jobId=NjQ2NTc2MzAzMVl1Ul9qVmd6M2t4M2pPdEJya2J5Y2dBQUFBQTE"
  },
  {
    "method": "GET",
    "path": "/objects/company-config/contact/2662"
  }
]
```
**Response 200 — Multiple independent requests to change employee location:**
```json
{
  "ia::result": [
    {
      "ia::result": {
        "key": "26",
        "id": "0014",
        "href": "/objects/company-config/employee/26"
      },
      "ia::meta": {
        "totalCount": 1
      },
      "ia::status": 200
    },
    {
      "ia::result": {
        "key": "33",
        "id": "1",
        "href": "/objects/company-config/employee/33"
      },
      "ia::meta": {
        "totalCount": 1
      },
      "ia::status": 200
    },
    {
      "ia::result": {
        "key": "62",
        "id": "2",
        "href": "/objects/company-config/employee/62"
      },
      "ia::meta": {
        "totalCount": 1
      },
      "ia::status": 200
    }
  ],
  "ia::meta": {
    "totalCount": 3
  }
}
```
**Response 200 — Multiple Requests using data from previous:**
```json
{
  "ia::result": [
    {
      "ia::result": {
        "key": "52",
        "id": "Emp2",
        "SSN": "100000001",
        "jobTitle": "Sr Software Eng",
        "location": {
          "id": "10",
          "key": "15",
          "name": "Indianapolis",
          "href": "/objects/company-config/location/15"
        },
        "department": {
          "id": "10",
          "key": "10",
          "name": "QA - II",
          "href": "/objects/company-config/department/10"
        },
        "manager": {
          "key": "11",
          "id": "10",
          "href": "/objects/company-config/employee/11"
        },
        "birthDate": "1984-04-14",
        "startDate": "2021-05-01",
        "endDate": "2025-04-02",
        "status": "active",
        "employeeType": {
          "id": "Part Time",
          "key": "2",
          "href": "/objects/company-config/employee-type/2"
        },
        "gender": "female",
        "terminationType": "involuntary",
        "primaryContact": {
          "id": "abc(C02)",
          "name": "abc(C02)",
          "key": "205",
          "href": "/objects/company-config/contact/205"
        },
        "defaultCurrency": "MXN",
        "earningType": {
          "key": "2",
          "id": "earningType2",
          "name": "earningType2",
          "href": "/objects/company-config/earning-type/2"
        },
        "class": {
          "id": "SW-Office",
          "name": "Office Software",
          "key": "9",
          "href": "/objects/company-config/class/9"
        },
        "href": "/objects/company-config/employee/52"
      },
      "ia::meta": {
        "totalCount": 1
      },
      "ia::status": 200
    },
    {
      "ia::result": [
        {
          "id": "Emp2",
          "jobTitle": "Sr Software Eng",
          "department.key": "10",
          "employeeType.id": "Part Time"
        },
        {
          "id": "Emp10",
          "jobTitle": "QA Engineer",
          "department.key": "10",
          "employeeType.id": "Part Time"
        },
        {
          "id": "Emp22",
          "jobTitle": "Architect",
          "department.key": "10",
          "employeeType.id": "Full Time"
        }
      ],
      "ia::meta": {
        "totalCount": 3,
        "start": 1,
        "pageSize": 100,
        "next": null,
        "previous": null
      },
      "ia::status": 200
    }
  ],
  "ia::meta": {
    "totalCount": 2
  }
}
```
**Response 207 — Multi-status example:**
```json
{
  "ia::result": [
    {
      "ia::error": {
        "code": "notFound",
        "message": "Asynchronous job 6465763031YSPy9lgWtJCMGZ6UkUbA6QAAAAY1 status could not be found",
        "supportId": "tqKR0%7EYsTZeDEdVao0_h01dZFQqgAAAAY"
      },
      "ia::status": 404
    },
    {
      "ia::error": {
        "code": "unprocessed",
        "message": "Operation skipped due to atomic transaction failure"
      },
      "ia::status": 422
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 0,
    "totalError": 2
  }
}
```

## POST /services/core/export
_Export objects_

**Request example — Export vendor objects:**
```json
{
  "fileType": "pdf",
  "query": {
    "object": "vendor",
    "fields": [
      "id",
      "name",
      "status",
      "key"
    ],
    "filters": [
      {
        "$eq": {
          "status": "active"
        }
      },
      {
        "$eq": {
          "billingType": "openItem"
        }
      }
    ],
    "filterExpression": "1 and 2",
    "orderBy": [
      {
        "id": "asc"
      }
    ]
  }
}
```

## GET /services/core/model
_Get an object model definition_

**Response 200 — Model for department:**
```json
{
  "ia::result": {
    "fields": {
      "id": {
        "mutable": false,
        "nullable": false,
        "type": "string",
        "readOnly": false,
        "writeOnly": false,
        "required": false
      },
      "key": {
        "readOnly": true,
        "type": "string",
        "writeOnly": false,
        "required": false,
        "nullable": true,
        "mutable": false
      },
      "name": {
        "nullable": false,
        "type": "string",
        "readOnly": false,
        "writeOnly": false,
        "required": false,
        "mutable": true
      },
      "reportTitle": {
        "nullable": true,
        "type": "string",
        "readOnly": false,
        "writeOnly": false,
        "required": false,
        "mutable": true
      },
      "status": {
        "enum": [
          "active",
          "activeNonPosting",
          "inactive"
        ],
        "type": "string",
        "readOnly": false,
        "writeOnly": false,
        "required": false,
        "nullable": false,
        "mutable": true
      }
    },
    "groups": {
      "audit": {
        "fields": {
          "createdBy": {
            "readOnly": true,
            "type": "string",
            "writeOnly": false,
            "required": false,
            "nullable": true,
            "mutable": false
          },
          "createdDateTime": {
            "format": "date-time",
            "readOnly": true,
            "type": "string",
            "writeOnly": false,
            "required": false,
            "nullable": true,
            "mutable": false
          },
          "modifiedBy": {
            "readOnly": true,
            "type": "string",
            "writeOnly": false,
            "required": false,
            "nullable": true,
            "mutable": false
          },
          "modifiedDateTime": {
            "format": "date-time",
            "readOnly": true,
            "type": "string",
            "writeOnly": false,
            "required": false,
            "nullable": true,
            "mutable": false
          }
        }
      }
    },
    "httpMethods": "OPTIONS,GET,POST,DELETE,PATCH",
    "refs": {
      "parent": {
        "apiObject": "company-config/department",
        "fields": {
          "id": {
            "type": "string",
            "readOnly": false,
            "writeOnly": false,
            "required": false,
            "nullable": true,
            "mutable": true
          },
          "key": {
            "nullable": true,
            "type": "string",
            "readOnly": false,
            "writeOnly": false,
            "required": false,
            "mutable": true
          },
          "name": {
            "readOnly": true,
            "type": "string",
            "writeOnly": false,
            "required": false,
            "nullable": true,
            "mutable": false
          }
        }
      },
      "supervisor": {
        "apiObject": "company-config/employee",
        "fields": {
          "id": {
            "type": "string",
            "readOnly": false,
            "writeOnly": false,
            "required": false,
            "nullable": true,
            "mutable": true
          },
          "key": {
            "nullable": true,
            "type": "string",
            "readOnly": false,
            "writeOnly": false,
            "required": false,
            "mutable": true
          },
          "name": {
            "readOnly": true,
            "type": "string",
            "writeOnly": false,
            "required": false,
            "nullable": true,
            "mutable": false
          }
        }
      }
    },
    "lists": [],
    "idempotenceSupported": true
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/core/query
_Query an object_

**Request example — Query vendor:**
```json
{
  "object": "accounts-payable/vendor",
  "fields": [
    "id",
    "name",
    "status",
    "href"
  ],
  "filters": [
    {
      "$eq": {
        "status": "active"
      }
    },
    {
      "$eq": {
        "billingType": "openItem"
      }
    }
  ],
  "filterExpression": "1 and 2",
  "filterParameters": {
    "caseSensitiveComparison": true,
    "includePrivate": true
  },
  "orderBy": [
    {
      "id": "asc"
    }
  ]
}
```
**Response 200 — Response - Query vendor:**
```json
{
  "ia::result": [
    {
      "id": "Vend-00002",
      "name": "Test vendor",
      "status": "active",
      "href": "/objects/accounts-payable/vendor/85"
    },
    {
      "id": "VEND-00010",
      "name": "Design Works",
      "status": "active",
      "href": "/objects/accounts-payable/vendor/111"
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

## GET /services/core/session/id
_Get an XML API session ID_

**Response 200 — success:**
```json
{
  "ia::result": {
    "sessionId": "Qw8RmZ3TnB5GyJ7Hq8UvFzE0Xr9PLK2K1D4YjC7V6qDkZxWfB3l-tgJ2",
    "expiresIn": 21600
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/core/view
_Execute a view_

**Request example — User view:**
```json
{
  "key": "540",
  "viewType": "user",
  "size": 3,
  "start": 7,
  "filterParameters": {
    "asOfDate": "2025-04-01",
    "caseSensitiveComparison": false
  }
}
```
**Request example — System view:**
```json
{
  "key": "expenses/employee-expense::systemfw1",
  "viewType": "system",
  "size": 3,
  "start": 4,
  "filterParameters": {
    "caseSensitiveComparison": true,
    "includePrivate": true
  }
}
```
**Response 200 — User view:**
```json
{
  "ia::result": [
    {
      "key": "61",
      "id": "Vend-00010",
      "name": "Design Works",
      "status": "active",
      "href": "/objects/accounts-payable/vendor/61"
    },
    {
      "key": "63",
      "id": "V1234555",
      "name": "North Fork Power",
      "status": "active",
      "href": "/objects/accounts-payable/vendor/63"
    },
    {
      "key": "38",
      "id": "V80863",
      "name": "Woodland Construction",
      "status": "active",
      "href": "/objects/accounts-payable/vendor/38"
    }
  ],
  "ia::meta": {
    "totalCount": 49,
    "start": 7,
    "pageSize": 3,
    "next": 10,
    "previous": 4
  }
}
```
**Response 200 — System view:**
```json
{
  "ia::result": [
    {
      "id": "5604",
      "employeeContact.lastName": "Belton",
      "employeeContact.firstName": "Michael",
      "createdDate": "2019-03-20",
      "expenseReportNumber": "EE-000050",
      "reimbursement.totalEntered": "378.00",
      "nonReimbursable.reimbursementTotalEntered": "0.00",
      "reimbursement.reimbursementCurrency": "USD",
      "basePayment.totalEntered": "378.00",
      "state": "approved"
    },
    {
      "id": "5339",
      "employeeContact.lastName": "Belton",
      "employeeContact.firstName": "Michael",
      "createdDate": "2019-03-20",
      "expenseReportNumber": "EE-000049",
      "reimbursement.totalEntered": "334.00",
      "nonReimbursable.reimbursementTotalEntered": "0.00",
      "reimbursement.reimbursementCurrency": "USD",
      "basePayment.totalEntered": "334.00",
      "state": "approved"
    },
    {
      "id": "5159",
      "employeeContact.lastName": "Lumbergh",
      "employeeContact.firstName": "Bill",
      "createdDate": "2019-03-19",
      "expenseReportNumber": "EE-000040",
      "reimbursement.totalEntered": "100.00",
      "nonReimbursable.reimbursementTotalEntered": "0.00",
      "reimbursement.reimbursementCurrency": "USD",
      "basePayment.totalEntered": "100.00",
      "state": "approved"
    }
  ],
  "ia::meta": {
    "totalCount": 45,
    "start": 4,
    "pageSize": 3,
    "next": 7,
    "previous": 1
  }
}
```
