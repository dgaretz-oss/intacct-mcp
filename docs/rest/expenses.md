# Expenses

## GET /objects/expenses/electronic-receipt
_List electronic receipts_

**Response 200 — List electronic receipts:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "EXP-00001",
      "href": "/objects/expenses/electronic-receipt/84"
    },
    {
      "key": "85",
      "id": "EXP-00002",
      "href": "/objects/expenses/electronic-receipt/85"
    },
    {
      "key": "60",
      "id": "EXP-00003",
      "href": "/objects/expenses/electronic-receipt/60"
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

## POST /objects/expenses/electronic-receipt
_Create an electronic receipt_

**Request example — Create an electronic receipt:**
```json
{
  "state": "draft",
  "receiptNumber": "EXP-00001",
  "employee": {
    "key": "10"
  },
  "createdDate": "2021-03-11",
  "description": "Travel expense",
  "memo": "Paid to employee",
  "lines": [
    {
      "glAccount": {
        "id": "6775.30"
      },
      "paidTo": "Stella Johnson",
      "paidFor": "Hotel stay",
      "quantity": "10",
      "unitRate": "20",
      "currency": "INR",
      "txnAmount": "100",
      "dimensions": {
        "location": {
          "id": "1"
        },
        "department": {
          "id": "12"
        },
        "class": {
          "id": "REST_CLS_001"
        },
        "item": {
          "id": "Case 13"
        },
        "employee": {
          "key": "10"
        },
        "vendor": {
          "id": "1605212096809"
        },
        "customer": {
          "id": "113"
        },
        "project": {
          "id": "NET-XML30-2"
        },
        "warehouse": {
          "id": "WH01"
        },
        "task": {
          "id": "tet"
        }
      }
    }
  ]
}
```
**Response 201 — Reference to new electronic receipt:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/electronic-receipt/124"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/expenses/electronic-receipt-line
_List electronic receipt lines_

**Response 200 — List of electronic receipt lines:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "100",
      "href": "/objects/expenses/electronic-receipt-line/100"
    },
    {
      "key": "101",
      "id": "101",
      "href": "/objects/expenses/electronic-receipt-line/101"
    },
    {
      "key": "102",
      "id": "102",
      "href": "/objects/expenses/electronic-receipt-line/102"
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

## GET /objects/expenses/electronic-receipt-line/{key}
_Get an electronic receipt line_

**Response 200 — Get an electronic receipt line:**
```json
{
  "ia::result": {
    "key": "312",
    "id": "312",
    "electronic-receipt": {
      "id": "136",
      "key": "136",
      "href": "/objects/expenses/electronic-receipt/136"
    },
    "glAccount": {
      "key": "158",
      "id": "6775.30",
      "name": "Travel",
      "href": "/objects/gl-account/account/158"
    },
    "entryDate": "2025-03-11",
    "paidTo": "Stella Johnson",
    "paidFor": "Hotel stay",
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "USA",
        "href": "/objects/company-config/location/1"
      },
      "department": {
        "key": "12",
        "id": "12",
        "name": "IT",
        "href": "/objects/company-config/department/12"
      },
      "class": {
        "key": "731",
        "id": "REST_CLS_001",
        "name": "Education",
        "href": "/objects/company-config/class/731"
      },
      "item": {
        "key": "13",
        "id": "13",
        "name": "Support",
        "href": "/objects/inventory-control/item/13"
      },
      "employee": {
        "key": "10",
        "id": "10",
        "href": "/objects/company-config/employee/10"
      },
      "vendor": {
        "key": "357",
        "id": "1605212096809",
        "name": "Boston Properties",
        "href": "/objects/accounts-payable/vendor/357"
      },
      "customer": {
        "key": "13",
        "id": "113",
        "name": "Jack In the Box",
        "href": "/objects/accounts-payable/customer/13"
      },
      "project": {
        "key": "2",
        "id": "NET-XML30-2",
        "name": "Binford Implementation",
        "href": "/objects/projects/project/2"
      },
      "task": {
        "key": "2",
        "id": "tet",
        "name": "Implementation services",
        "href": "/objects/projects/task/2"
      },
      "warehouse": {
        "key": "6",
        "id": "WH01",
        "name": "WH01 Name",
        "href": "/objects/inventory-control/warehouse/6"
      }
    },
    "lineNumber": 1,
    "expenseType": {
      "key": "Meals",
      "id": "6000"
    },
    "state": "draft",
    "quantity": "5",
    "unitRate": "20",
    "currency": "USD",
    "txnAmount": "100",
    "href": "/objects/expenses/electronic-receipt-line/312"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/expenses/electronic-receipt/{key}
_Get an electronic receipt_

**Response 200 — Get an electronic receipt:**
```json
{
  "ia::result": {
    "receiptNumber": "ER-0152",
    "employee": {
      "id": "EMP8",
      "key": "10",
      "href": "/objects/company-config/employee/10"
    },
    "employeeContact": {
      "key": "977",
      "id": "Thomas, Glenn",
      "firstName": "Glenn",
      "lastName": "Thomas",
      "href": "/objects/company-config/employee/10"
    },
    "key": "124",
    "id": "124",
    "createdDate": "2021-03-11",
    "state": "draft",
    "totalAmount": "1000",
    "currency": "USD",
    "baseCurrency": "USD",
    "baseAmount": "120",
    "description": "Supplies for customer training",
    "lines": [
      {
        "key": "288",
        "id": "288",
        "electronicReceipt": {
          "id": "124",
          "key": "124",
          "href": "/objects/expenses/electronic-receipt/124"
        },
        "quantity": "10",
        "glAccount": {
          "key": "158",
          "id": "6775.30",
          "name": "Travel",
          "href": "/objects/general-ledger/account/158"
        },
        "entryDate": "2021-03-11",
        "paidTo": "Stella Johnson",
        "paidFor": "Hotel stay",
        "expenseType": {
          "key": "Meals",
          "id": "6000"
        },
        "state": "draft",
        "unitRate": "100",
        "lineNumber": 1,
        "currency": "INR",
        "txnAmount": "1000",
        "attachment": {
          "key": "1",
          "id": "1",
          "href": "/objects/company-config/attachment/12345"
        },
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "name": "USA",
            "href": "/objects/company-config/location/1"
          },
          "department": {
            "key": "12",
            "id": "12",
            "name": "IT",
            "href": "/objects/company-config/department/12"
          },
          "class": {
            "key": "731",
            "id": "REST_CLS_001",
            "name": "Education",
            "href": "/objects/company-config/class/731"
          },
          "item": {
            "key": "13",
            "id": "13",
            "name": "Support",
            "href": "/objects/inventory-control/item/13"
          },
          "employee": {
            "key": "10",
            "id": "EMP8",
            "name": "Thomas, Glenn",
            "href": "/objects/company-config/employee/10"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "Boston Properties",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "customer": {
            "key": "13",
            "id": "113",
            "name": "Jack In the Box",
            "href": "/objects/accounts-payable/customer/13"
          },
          "project": {
            "key": "2",
            "id": "NET-XML30-2",
            "name": "Binford Implementation",
            "href": "/objects/projects/project/2"
          },
          "task": {
            "key": "2",
            "id": "tet",
            "name": "Implementation services",
            "href": "/objects/projects/task/2"
          },
          "warehouse": {
            "key": "6",
            "id": "WH01",
            "name": "WH01 Name",
            "href": "/objects/inventory-control/warehouse/6"
          }
        },
        "href": "/objects/expenses/electronic-receipt-line/288"
      }
    ],
    "memo": "Covered by customer",
    "href": "/objects/expenses/electronic-receipt/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/expenses/electronic-receipt/{key}
_Update an electronic receipt_

**Request example — Updates an electronic receipt:**
```json
{
  "memo": "Covered by customer"
}
```
**Response 200 — Reference to updated electronic receipt:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/electronic-receipt/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/expenses/electronic-receipt/{key}
_Delete an electronic receipt_


## GET /objects/expenses/employee-expense
_List employee expenses_

**Response 200 — List employee expenses:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "EXP-00001",
      "href": "/objects/expenses/employee-expense/84"
    },
    {
      "key": "85",
      "id": "EXP-00002",
      "href": "/objects/expenses/employee-expense/85"
    },
    {
      "key": "60",
      "id": "EXP-00003",
      "href": "/objects/expenses/employee-expense/60"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0,
    "start": 1,
    "pageSize": 5,
    "next": 0,
    "previous": 0
  }
}
```

## POST /objects/expenses/employee-expense
_Create an employee expense_

**Request example — Create an employee expense:**
```json
{
  "state": "submitted",
  "expenseReportNumber": "EXP-00001",
  "employee": {
    "id": "10"
  },
  "createdDate": "2021-03-11",
  "expenseSummary": {
    "postingDate": "2021-01-31",
    "title": "Expenses - Q1 batch"
  },
  "basePaymentInformation": {
    "baseCurrency": "USD"
  },
  "reimbursementInformation": {
    "reimbursementCurrency": "EUR"
  },
  "description": "Travel expense",
  "memo": "Paid to employee",
  "lines": [
    {
      "account": null,
      "id": "6775.30",
      "paidTo": "paid To",
      "paidFor": "paid For",
      "isBillable": false,
      "form1099": {
        "isForm1099": "true",
        "type": "MISC",
        "box": "3"
      },
      "paymentType": {
        "key": "1",
        "name": "Non-reimburse",
        "isNonreimbursable": false
      },
      "quantity": "10",
      "unitrate": "20",
      "txnCurrency": "INR",
      "txnAmount": "100",
      "transactionToReimburseConversion": {
        "exchangeRateDate": "2021-03-11",
        "exchangeRateTypeId": "Intacct Daily Rate"
      },
      "dimensions": {
        "location": {
          "id": "1"
        },
        "department": {
          "id": "12"
        },
        "class": {
          "id": "REST_CLS_001"
        },
        "item": {
          "id": "Case 13"
        },
        "employee": {
          "id": "10"
        },
        "vendor": {
          "id": "1605212096809"
        },
        "customer": {
          "id": "113"
        },
        "project": {
          "id": "NET-XML30-2"
        },
        "warehouse": {
          "id": "WH01"
        },
        "task": {
          "id": "tet"
        }
      }
    }
  ]
}
```
**Response 201 — Reference to new employee expense:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/employee-expense/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/expenses/employee-expense-adjustment
_List employee expense adjustments_

**Response 200 — Get list of employee expense adjustments:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "EXP-00001",
      "href": "/objects/expenses/employee-expense-adjustment/84"
    },
    {
      "key": "85",
      "id": "EXP-00002",
      "href": "/objects/expenses/employee-expense-adjustment/85"
    },
    {
      "key": "60",
      "id": "EXP-00003",
      "href": "/objects/expenses/employee-expense-adjustment/60"
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

## POST /objects/expenses/employee-expense-adjustment
_Create an employee expense adjustment_

**Request example — Reference to new employee expense adjustment:**
```json
{
  "state": "submitted",
  "expenseAdjustmentReportNumber": "EXP-00001",
  "employee": {
    "id": "10"
  },
  "createdDate": "2025-03-11",
  "expenseSummary": {
    "postingDate": "2025-01-31",
    "title": "Expenses - Q1 batch",
    "state": "open",
    "preventGLPosting": false
  },
  "basePayment": {
    "baseCurrency": "USD"
  },
  "reimbursement": {
    "reimbursementCurrency": "EUR"
  },
  "description": "Travel expense",
  "memo": "Paid by employee.",
  "lines": [
    {
      "paidTo": "De Anza Hotel",
      "paidFor": "Not used",
      "isBillable": false,
      "form1099": {
        "isForm1099": "true",
        "type": "MISC",
        "box": "3"
      },
      "paymentType": {
        "key": "1",
        "name": "Non-reimburse",
        "isNonReimbursable": false
      },
      "quantity": "1",
      "unitRate": "20",
      "txnCurrency": "INR",
      "txnAmount": "100",
      "transactionToReimburseConversion": {
        "exchangeRateDate": "2025-03-11",
        "exchangeRateTypeId": "Intacct Daily Rate"
      },
      "dimensions": {
        "location": {
          "id": "1"
        },
        "department": {
          "id": "12"
        },
        "class": {
          "id": "REST_CLS_001"
        },
        "item": {
          "id": "Case 13"
        },
        "employee": {
          "id": "10"
        },
        "vendor": {
          "id": "1605212096809"
        },
        "customer": {
          "id": "113"
        },
        "project": {
          "id": "NET-XML30-2"
        },
        "warehouse": {
          "id": "WH01"
        },
        "task": {
          "id": "tet"
        }
      }
    }
  ]
}
```
**Response 201 — New employee expense adjustment:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/employee-expense-adjustment/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/expenses/employee-expense-adjustment-line
_List employee expense adjustment lines_

**Response 200 — List of employee expense adjustment line objects:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "100",
      "href": "/objects/expenses/employee-expense-adjustment-line/100"
    },
    {
      "key": "101",
      "id": "101",
      "href": "/objects/expenses/employee-expense-adjustment-line/101"
    },
    {
      "key": "102",
      "id": "102",
      "href": "/objects/expenses/employee-expense-adjustment-line/102"
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

## POST /objects/expenses/employee-expense-adjustment-line
_Create an employee expense adjustment line_

**Request example — Creates an employee expense adjustment line:**
```json
{
  "account": {
    "id": "6775.3"
  },
  "paidTo": "Hotel Westin",
  "paidFor": "Not used",
  "isBillable": false,
  "form1099": {
    "isForm1099": "true",
    "type": "MISC",
    "box": "3"
  },
  "paymentType": {
    "key": "1",
    "name": "Non-reimburse",
    "isNonreimbursable": false
  },
  "quantity": "10",
  "unitrate": "20",
  "txnCurrency": "INR",
  "txnAmount": "100",
  "transactionToReimburseConversion": {
    "exchangeRateDate": "2025-03-11",
    "exchangeRateTypeId": "Intacct Daily Rate"
  },
  "dimensions": {
    "location": {
      "id": "1"
    },
    "department": {
      "id": "12"
    },
    "class": {
      "id": "REST_CLS_001"
    },
    "item": {
      "id": "Case 13"
    },
    "employee": {
      "id": "10"
    },
    "vendor": {
      "id": "1605212096809"
    },
    "customer": {
      "id": "113"
    },
    "project": {
      "id": "NET-XML30-2"
    },
    "warehouse": {
      "id": "WH01"
    },
    "task": {
      "id": "tet"
    }
  }
}
```
**Response 201 — Reference to new employee expense adjustment line:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/employee-expense-adjustment-line/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/expenses/employee-expense-adjustment-line/{key}
_Get an employee expense adjustment line_

**Response 200 — Details of the employee expense adjustment line:**
```json
{
  "ia::result": {
    "key": "312",
    "id": "312",
    "employee-expense": {
      "id": "136",
      "key": "136",
      "href": "/objects/expenses/employee-expense/136"
    },
    "glAccount": {
      "key": "158",
      "id": "6775.30",
      "name": "Travel",
      "href": "/objects/account/158"
    },
    "entryDate": "2025-03-11",
    "paidTo": "Hotel Westin",
    "paidFor": "Not used",
    "reimburseToBase": {
      "baseAmount": "1.38",
      "exchangeRateDate": "2025-03-11",
      "exchangeRateTypeId": "-1",
      "exchangeRate": "1.1899"
    },
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "USA",
        "href": "/objects/company-config/location/1"
      },
      "department": {
        "key": "12",
        "id": "12",
        "name": "IT",
        "href": "/objects/company-config/department/12"
      },
      "class": {
        "key": "731",
        "id": "REST_CLS_001",
        "name": "Enterprises",
        "href": "/objects/company-config/class/731"
      },
      "item": {
        "key": "13",
        "id": "Case 13",
        "name": "Platform pack",
        "href": "/objects/inventory-control/item/13"
      },
      "employee": {
        "key": "10",
        "id": "10",
        "href": "/objects/company-config/employee/10"
      },
      "employeeContact": {
        "key": 20,
        "id": "Thomas, Glenn",
        "firstName": "Glenn",
        "lastName": "Thomas",
        "href": "/objects/company-config/contact/20"
      },
      "vendor": {
        "key": "357",
        "id": "1605212096809",
        "name": "GenLab",
        "href": "/objects/accounts-payable/vendor/357"
      },
      "customer": {
        "key": "13",
        "id": "113",
        "name": "Jack In the Box",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "project": {
        "key": "2",
        "id": "NET-XML30-2",
        "name": "Talcomp training",
        "href": "/objects/projects/project/2"
      },
      "task": {
        "key": "2",
        "id": "tet",
        "name": "Design",
        "href": "/objects/projects/task/2"
      },
      "warehouse": {
        "key": "6",
        "id": "WH01",
        "name": "WH01",
        "href": "/objects/inventory-control/warehouse/6"
      }
    },
    "lineNumber": 1,
    "expenseType": {
      "key": "Meals",
      "id": "6000"
    },
    "reimbursement": {
      "reimbursementAmount": "1.16",
      "totalSelected": "0",
      "totalPaid": "0"
    },
    "isBillable": false,
    "isBilled": false,
    "state": "approved",
    "form1099": {
      "isForm1099": "true",
      "type": "MISC",
      "box": "3"
    },
    "paymentType": {
      "key": "1",
      "name": "Non-reimburse",
      "isNonreimbursable": false
    },
    "quantity": "5",
    "unitRate": "20",
    "currency": {
      "txnCurrency": "INR",
      "txnAmount": "4444",
      "exchangeRateDate": "2025-03-11",
      "exchangeRateTypeId": "-1",
      "exchangeRate": "65",
      "userExchangeRate": "5"
    },
    "href": "/objects/expenses/employee-expense-adjustment-line/312"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/expenses/employee-expense-adjustment-line/{key}
_Update an employee expense adjustment line_

**Request example — Updates an employee expense adjustment line:**
```json
{
  "id": "100",
  "paidTo": "Hotel Westin"
}
```
**Response 200 — Updated employee expense adjustment line:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/employee-expense-adjustment-line/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/expenses/employee-expense-adjustment-line/{key}
_Delete an employee expense adjustment line_


## GET /objects/expenses/employee-expense-adjustment/{key}
_Get an employee expense adjustment_

**Response 200 — Details of the employee expense adjustment:**
```json
{
  "ia::result": {
    "expenseAdjustmentReportNumber": "ER-0152",
    "employee": {
      "id": "10",
      "key": "10",
      "href": "/objects/company-config/employee/10"
    },
    "employeeContact": {
      "key": "977",
      "id": "Thomas Glenn",
      "firstName": "Thomas",
      "lastName": "Glenn",
      "href": "/objects/company-config/contact/977"
    },
    "key": "124",
    "id": "124",
    "createdDate": "2025-03-11",
    "expenseSummary": {
      "postingDate": "2025-01-31",
      "title": "Expenses - Q1 batch",
      "key": "3",
      "id": "3",
      "href": "/objects/expenses/employee-expense-summary/3"
    },
    "basePaymentInformation": {
      "totalEntered": "1.38",
      "totalPaid": "0",
      "totalSelected": "0",
      "totalDue": "1.38",
      "baseCurrency": "USD"
    },
    "state": "approved",
    "reimbursementInformation": {
      "totalEntered": "1.16",
      "totalSelected": "0",
      "totalPaid": "0",
      "totalDue": "1.16",
      "reimbursementCurrency": "EUR"
    },
    "description": "Supplies for customer training",
    "nonReimbursable": {
      "baseTotalEntered": "0",
      "reimbursementTotalEntered": "0"
    },
    "lines": [
      {
        "key": "288",
        "id": "288",
        "employee-expense": {
          "id": "136",
          "key": "136",
          "href": "/objects/expenses/employee-expense/136"
        },
        "quantity": "0",
        "glAccount": {
          "key": "158",
          "id": "6775.30",
          "name": "Travel",
          "href": "/objects/account/158"
        },
        "entryDate": "2025-03-11",
        "paidTo": "Hotel Westin",
        "paidFor": "Not used",
        "baseAmount": "1.38",
        "reimburseToBase": {
          "exchangeRateDate": "2025-03-11",
          "exchangeRateTypeId": "-1",
          "exchangeRate": "1.1899"
        },
        "expenseType": {
          "key": "Hotel",
          "id": "5000"
        },
        "reimbursementInformation": {
          "reimbursementAmount": "700.16",
          "totalSelected": "0",
          "totalPaid": "0"
        },
        "isBillable": false,
        "isBilled": false,
        "state": "approved",
        "form1099": {
          "isForm1099": "true",
          "type": "MISC",
          "box": "3"
        },
        "paymentType": {
          "key": "1",
          "name": "Non-reimburse",
          "isNonreimbursable": false
        },
        "unitRate": "10",
        "lineNumber": 1,
        "currency": {
          "txnCurrency": "INR",
          "txnAmount": "100",
          "exchangeRateDate": "2025-03-11",
          "exchangeRateTypeId": "Intacct Daily Rate",
          "exchangeRate": "1"
        },
        "attachment": {
          "key": "1",
          "id": "1"
        },
        "dimensions": {
          "location": {
            "key": "11",
            "id": "1",
            "name": "USA",
            "href": "/objects/company-config/location/11"
          },
          "department": {
            "key": "12",
            "id": "12",
            "name": "IT",
            "href": "/objects/company-config/department/12"
          },
          "class": {
            "key": "731",
            "id": "REST_CLS_001",
            "name": "Education",
            "href": "/objects/company-config/class/731"
          },
          "item": {
            "key": "13",
            "id": "13",
            "name": "Support",
            "href": "/objects/inventory-control/item/13"
          },
          "employee": {
            "key": "10",
            "id": "10",
            "href": "/objects/company-config/employee/10"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "Boston Properties",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "customer": {
            "key": "13",
            "id": "113",
            "name": "Jack In the Box",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "project": {
            "key": "2",
            "id": "NET-XML30-2",
            "name": "Binford Implementation",
            "href": "/objects/projects/project/2"
          },
          "task": {
            "key": "2",
            "id": "tet",
            "name": "Implementation services",
            "href": "/objects/projects/task/2"
          },
          "warehouse": {
            "key": "6",
            "id": "WH01",
            "name": "WH01 Name",
            "href": "/objects/inventory-control/warehouse/6"
          }
        },
        "href": "/objects/expenses/employee-expense-adjustment-line/288"
      }
    ],
    "memo": "Covered by customer",
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "adjustmentType": "debit",
    "referenceEmployeeExpense": {
      "id": "124",
      "key": "124",
      "href": "/objects/expenses/employee-expense/124"
    },
    "href": "/objects/expenses/employee-expense-adjustment/124"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/expenses/employee-expense-adjustment/{key}
_Update an employee expense adjustment_

**Request example — Updates an employee expense adjustment:**
```json
{
  "memo": "Covered by customer"
}
```
**Response 200 — Updated employee expense adjustment:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/employee-expense-adjustment/124"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/expenses/employee-expense-adjustment/{key}
_Delete an employee expense adjustment_


## GET /objects/expenses/employee-expense-line
_List employee expense lines_

**Response 200 — List employee expense lines:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "100",
      "href": "/objects/expenses/employee-expense-line/100"
    },
    {
      "key": "101",
      "id": "101",
      "href": "/objects/expenses/employee-expense-line/101"
    },
    {
      "key": "102",
      "id": "102",
      "href": "/objects/expenses/employee-expense-line/102"
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

## POST /objects/expenses/employee-expense-line
_Create an employee expense line_

**Request example — Create an employee expense line:**
```json
{
  "account": {
    "id": "6775.3"
  },
  "paidTo": "Stella Johnson",
  "paidFor": "Hotel stay",
  "isBillable": false,
  "form1099": {
    "isForm1099": "true",
    "type": "MISC",
    "box": "3"
  },
  "paymentType": {
    "key": "1",
    "id": "Non-reimburse",
    "isNonreimbursable": false
  },
  "quantity": "10",
  "unitrate": "20",
  "txnCurrency": "INR",
  "txnAmount": "100",
  "transactionToReimburseConversion": {
    "exchangeRateDate": "2021-03-11",
    "exchangeRateType": {
      "id": "Intacct Daily Rate"
    },
    "creditCardTxnLine": {
      "key": "128"
    }
  },
  "dimensions": {
    "location": {
      "id": "1"
    },
    "department": {
      "id": "12"
    },
    "class": {
      "id": "REST_CLS_001"
    },
    "item": {
      "id": "Case 13"
    },
    "employee": {
      "id": "10"
    },
    "vendor": {
      "id": "1605212096809"
    },
    "customer": {
      "id": "113"
    },
    "project": {
      "id": "NET-XML30-2"
    },
    "warehouse": {
      "id": "WH01"
    },
    "task": {
      "id": "tet"
    }
  }
}
```
**Response 201 — Reference to new employee expense line:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/employee-expense-line/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/expenses/employee-expense-line/{key}
_Get an employee expense line_

**Response 200 — Get an employee expense line:**
```json
{
  "ia::result": {
    "key": "312",
    "id": "312",
    "employeeExpense": {
      "id": "136",
      "key": "136",
      "href": "/objects/expenses/employee-expense/136"
    },
    "glAccount": {
      "key": "158",
      "id": "6775.30",
      "name": "Travel",
      "href": "/objects/account/158"
    },
    "entryDate": "2021-03-11",
    "paidTo": "Stella Johnson",
    "paidFor": "Hotel stay",
    "reimburseToBase": {
      "baseAmount": "1.38",
      "exchangeRateDate": "2021-03-11",
      "exchangeRateTypeId": "-1",
      "exchangeRate": "1.1899"
    },
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "USA",
        "href": "/objects/company-config/location/1"
      },
      "department": {
        "key": "12",
        "id": "12",
        "name": "IT",
        "href": "/objects/company-config/department/12"
      },
      "class": {
        "key": "731",
        "id": "REST_CLS_001",
        "name": "Enterprises",
        "href": "/objects/company-config/class/731"
      },
      "item": {
        "key": "13",
        "id": "Case 13",
        "name": "Platform pack",
        "href": "/objects/inventory-control/item/13"
      },
      "employee": {
        "key": "10",
        "id": "10",
        "name": "Thomas, Glenn",
        "href": "/objects/company-config/employee/10"
      },
      "vendor": {
        "key": "357",
        "id": "1605212096809",
        "name": "GenLab",
        "href": "/objects/accounts-payable/vendor/357"
      },
      "customer": {
        "key": "13",
        "id": "113",
        "name": "Jack In the Box",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "project": {
        "key": "2",
        "id": "NET-XML30-2",
        "name": "Talcomp training",
        "href": "/objects/projects/project/2"
      },
      "task": {
        "key": "2",
        "id": "tet",
        "name": "Design",
        "href": "/objects/projects/task/2"
      },
      "warehouse": {
        "key": "6",
        "id": "WH01",
        "name": "WH01",
        "href": "/objects/inventory-control/warehouse/6"
      }
    },
    "lineNumber": 1,
    "expenseType": {
      "key": "Meals",
      "id": "6000"
    },
    "reimbursement": {
      "reimbursementAmount": "1.16",
      "totalSelected": "0",
      "totalPaid": "0"
    },
    "isBillable": false,
    "isBilled": false,
    "state": "approved",
    "form1099": {
      "isForm1099": "true",
      "type": "MISC",
      "box": "3"
    },
    "paymentType": {
      "key": "1",
      "id": "Non-reimburse",
      "isNonreimbursable": false
    },
    "quantity": "5",
    "unitRate": "20",
    "currency": {
      "txnCurrency": "INR",
      "txnAmount": "4444",
      "exchangeRateDate": "2021-03-11",
      "exchangeRateTypeId": "-1",
      "exchangeRate": "65",
      "userExchangeRate": "5"
    },
    "creditCardTxnLine": {
      "id": "128",
      "key": "128",
      "href": "/objects/cash-management/credit-card-txn-line/128"
    },
    "creditCardTxn": {
      "id": "124",
      "key": "124",
      "href": "/objects/cash-management/credit-card-txn/128"
    },
    "href": "/objects/expenses/employee-expense-line/312"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/expenses/employee-expense-line/{key}
_Update an employee expense line_

**Request example — Update an employee expense line:**
```json
{
  "paidTo": "Travel expense"
}
```
**Response 200 — Reference to updated employee expense line:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/employee-expense-line/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/expenses/employee-expense-line/{key}
_Delete an employee expense line_


## GET /objects/expenses/employee-expense-payment-type
_List employee expense payment types_

**Response 200 — List employee expense payment types:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "Non-reimburse",
      "href": "/objects/expenses/employee-expense-payment-type/100"
    },
    {
      "key": "101",
      "id": "Reimburse",
      "href": "/objects/expenses/employee-expense-payment-type/101"
    },
    {
      "key": "102",
      "id": "Billable",
      "href": "/objects/expenses/employee-expense-payment-type/102"
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

## POST /objects/expenses/employee-expense-payment-type
_Create an employee expense payment type_

**Request example — Create an employee expense payment type:**
```json
{
  "id": "Non Reimburse",
  "status": "active",
  "description": "Non reimbursable payment type",
  "offsetAccount": {
    "id": "2420"
  }
}
```
**Response 201 — Reference to new employee expense payment type:**
```json
{
  "ia::result": {
    "key": "18",
    "id": "Non Reimburse",
    "href": "/objects/expenses/employee-expense-payment-type/12345"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/expenses/employee-expense-payment-type/{key}
_Get an employee expense payment type_

**Response 200 — Get an employee expense payment type:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Non Reimburse",
    "description": "description",
    "isNonReimbursable": true,
    "offsetGLAccount": {
      "key": "70",
      "id": "2420",
      "name": "EE-Office Supplies",
      "href": "/objects/account/70"
    },
    "status": "active",
    "audit": {
      "createdDateTime": "2021-09-02T08:38:53Z",
      "modifiedDateTime": "2021-09-02T08:38:53Z",
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
    "href": "/objects/expenses/employee-expense-payment-type/10"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/expenses/employee-expense-payment-type/{key}
_Update an employee expense payment type_

**Request example — Update an employee expense payment type:**
```json
{
  "status": "active",
  "description": "Non reimbursable payment type"
}
```
**Response 200 — Reference to updated employee expense payment type:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Non Reimburse",
    "href": "/objects/expenses/employee-expense-payment-type/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/expenses/employee-expense-payment-type/{key}
_Delete an employee expense payment type_


## GET /objects/expenses/employee-expense-summary
_List employee expense summaries_

**Response 200 — List employee expense summaries:**
```json
{
  "ia::result": [
    {
      "key": "13",
      "id": "13",
      "href": "/objects/expenses/employee-expense-summary/13"
    },
    {
      "key": "15",
      "id": "15",
      "href": "/objects/expenses/employee-expense-summary/15"
    },
    {
      "key": "16",
      "id": "16",
      "href": "/objects/expenses/employee-expense-summary/16"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 3,
    "next": 0,
    "previous": 0
  }
}
```

## POST /objects/expenses/employee-expense-summary
_Create an employee expense summary_

**Request example — Create an employee expense summary:**
```json
{
  "name": "Expenses (USD) Q1 Batch",
  "title": "Expenses (USD) Q1 Batch",
  "postingDate": "2021-01-23",
  "totalAmount": "100",
  "recordType": "expense",
  "status": "active"
}
```
**Response 201 — Reference to new employee expense summary:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "10",
    "href": "/objects/expenses/employee-expense-summary/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/expenses/employee-expense-summary/{key}
_Get an employee expense summary_

**Response 200 — Get an employee expense summary:**
```json
{
  "ia::result": {
    "key": "18",
    "id": "18",
    "title": "Expense reports for week 03",
    "postingDate": "2023-01-20",
    "totalAmount": "100",
    "state": "open",
    "recordType": "expense",
    "summaryCreationType": "manual",
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "bankAccount": {
      "key": "1",
      "id": "BOA",
      "href": "/objects/cash-management/bank-account/1"
    },
    "preventGLPosting": false,
    "href": "/objects/expenses/employee-expense-summary/18"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/expenses/employee-expense-summary/{key}
_Update an employee expense summary_

**Request example — Update an employee expense summary:**
```json
{
  "name": "Expense report for January"
}
```
**Response 200 — Reference to updated employee expense summary:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/employee-expense-summary/124"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/expenses/employee-expense-summary/{key}
_Delete an employee expense summary_


## GET /objects/expenses/employee-expense-type
_List employee expense types_

**Response 200 — List employee expense types:**
```json
{
  "ia::result": [
    {
      "key": "46",
      "id": "Travel",
      "href": "/objects/expenses/employee-expense-type/46"
    },
    {
      "key": "44",
      "id": "Transportation",
      "href": "/objects/expenses/employee-expense-type/44"
    },
    {
      "key": "40",
      "id": "Compensation",
      "href": "/objects/expenses/employee-expense-type/40"
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

## POST /objects/expenses/employee-expense-type
_Create an employee expense type_

**Request example — Create an employee expense type:**
```json
{
  "id": "Travel",
  "status": "active",
  "description": "Travel fare",
  "unitCurrency": "USD",
  "glAccount": {
    "id": "Travel expenses"
  },
  "unitRates": [
    {
      "rate": "200",
      "startDate": "2021-01-23"
    },
    {
      "rate": "100",
      "startDate": "2021-03-23"
    }
  ]
}
```
**Response 201 — Reference to new employee expense type:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Travel",
    "href": "/objects/expenses/employee-expense-type/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/expenses/employee-expense-type/{key}
_Get an employee expense type_

**Response 200 — Get an employee expense type:**
```json
{
  "ia::result": {
    "key": "63",
    "audit": {
      "createdDateTime": "2023-12-21T08:40:05Z",
      "modifiedDateTime": "2023-12-21T08:47:08Z",
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
    "id": "Travel",
    "description": "Travel fare",
    "glAccount": {
      "key": "5500",
      "id": "Travel expenses",
      "name": "Automobile expenses",
      "href": "/objects/general-ledger/account/5500"
    },
    "status": "active",
    "offsetGLAccount": {
      "key": "6000",
      "id": "Offset travel expenses",
      "name": "Offset automobile expenses",
      "href": "/objects/general-ledger/account/6000"
    },
    "item": {
      "key": "311",
      "id": "10",
      "name": "Laptop",
      "href": "/objects/inventory-control/item/311"
    },
    "form1099": {
      "type": "W-2G",
      "box": "1"
    },
    "unitCurrency": "USD",
    "unitRates": [
      {
        "id": "28",
        "key": "28",
        "employeeExpenseType": {
          "id": "63",
          "key": "63",
          "href": "/objects/expenses/employee-expense-type/63"
        },
        "rate": "200",
        "startDate": "2021-01-23",
        "audit": {
          "createdDateTime": "2023-12-21T08:47:08Z",
          "modifiedDateTime": "2023-12-21T08:47:08Z",
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
        "href": "/objects/expenses/unit-rate/28"
      },
      {
        "id": "29",
        "key": "29",
        "employeeExpenseType": {
          "id": "63",
          "key": "63",
          "href": "/objects/expenses/employee-expense-type/63"
        },
        "rate": "100",
        "startDate": "2021-01-23",
        "audit": {
          "createdDateTime": "2023-12-21T08:47:08Z",
          "modifiedDateTime": "2023-12-21T08:47:08Z",
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
        "href": "/objects/expenses/unit-rate/29"
      }
    ],
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "href": "/objects/expenses/employee-expense-type/63"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/expenses/employee-expense-type/{key}
_Update an employee expense type_

**Request example — Update an employee expense type:**
```json
{
  "description": "Personal travel"
}
```
**Response 200 — Reference to updated employee expense type:**
```json
{
  "ia::result": {
    "key": "47",
    "id": "Travel",
    "href": "/objects/expenses/employee-expense-type/124"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/expenses/employee-expense-type/{key}
_Delete an employee expense type_


## GET /objects/expenses/employee-expense/{key}
_Get an employee expense_

**Response 200 — Get an employee expense:**
```json
{
  "ia::result": {
    "expenseReportNumber": "ER-0152",
    "employee": {
      "id": "10",
      "key": "10",
      "href": "/objects/company-config/employee/10"
    },
    "employeeContact": {
      "key": "977",
      "id": "Thomas Glenn",
      "firstName": "Thomas",
      "lastName": "Glenn",
      "href": "/objects/company-config/contact/977"
    },
    "key": "124",
    "id": "124",
    "createdDate": "2021-03-11",
    "expenseSummary": {
      "postingDate": "2021-01-31",
      "title": "Expenses - Q1 batch",
      "key": "3",
      "id": "3",
      "state": "open",
      "preventGLPosting": false,
      "href": "/objects/expenses/employee-expense-summary/3"
    },
    "basePaymentInformation": {
      "totalEntered": "1.38",
      "totalPaid": "0",
      "totalSelected": "0",
      "totalDue": "1.38",
      "baseCurrency": "USD"
    },
    "state": "approved",
    "reimbursementInformation": {
      "totalEntered": "1.16",
      "totalSelected": "0",
      "totalPaid": "0",
      "totalDue": "1.16",
      "reimbursementCurrency": "EUR"
    },
    "description": "Supplies for customer training",
    "nonReimbursable": {
      "baseTotalEntered": "0",
      "reimbursementTotalEntered": "0"
    },
    "lines": [
      {
        "key": "288",
        "id": "288",
        "employee-expense": {
          "id": "124",
          "key": "124",
          "href": "/objects/expenses/employee-expense/124"
        },
        "quantity": "0",
        "glAccount": {
          "key": "158",
          "id": "6775.30",
          "name": "Travel",
          "href": "/objects/account/158"
        },
        "entryDate": "2021-03-11",
        "paidTo": "paid To",
        "paidFor": "paid For",
        "baseAmount": "1.38",
        "reimburseToBase": {
          "exchangeRateDate": "2021-03-11",
          "exchangeRateTypeId": "-1",
          "exchangeRate": "1.1899"
        },
        "expenseType": {
          "key": "Meals",
          "id": "6000"
        },
        "reimbursementInformation": {
          "reimbursementAmount": "1.16",
          "totalSelected": "0",
          "totalPaid": "0"
        },
        "isBillable": false,
        "isBilled": false,
        "state": "approved",
        "form1099": {
          "isForm1099": "true",
          "type": "MISC",
          "box": "3"
        },
        "paymentType": {
          "isNonreimbursable": false
        },
        "unitrate": "10",
        "lineNumber": 1,
        "currency": {
          "txnCurrency": "INR",
          "txnAmount": "100",
          "exchangeRateDate": "2021-03-11",
          "exchangeRateTypeId": "Intacct Daily Rate",
          "exchangeRate": "1"
        },
        "attachment": {
          "key": "1",
          "id": "1"
        },
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "name": "USA",
            "href": "/objects/company-config/location/1"
          },
          "department": {
            "key": "12",
            "id": "12",
            "name": "IT",
            "href": "/objects/company-config/department/12"
          },
          "class": {
            "key": "731",
            "id": "REST_CLS_001",
            "name": "Education",
            "href": "/objects/company-config/class/731"
          },
          "item": {
            "key": "13",
            "id": "13",
            "name": "Support",
            "href": "/objects/inventory-control/item/13"
          },
          "employee": {
            "key": "10",
            "id": "10",
            "href": "/objects/company-config/employee/10"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "Boston Properties",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "customer": {
            "key": "13",
            "id": "113",
            "name": "Jack In the Box",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "project": {
            "key": "2",
            "id": "NET-XML30-2",
            "name": "Binford Implementation",
            "href": "/objects/projects/project/2"
          },
          "task": {
            "key": "2",
            "id": "tet",
            "name": "Implementation services",
            "href": "/objects/projects/task/2"
          },
          "warehouse": {
            "key": "6",
            "id": "WH01",
            "name": "WH01 Name",
            "href": "/objects/inventory-control/warehouse/6"
          }
        },
        "href": "/objects/expenses/employee-expense-line/288"
      }
    ],
    "memo": "Covered by customer",
    "entity": {
      "key": "46",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/46"
    },
    "href": "/objects/expenses/employee-expense/124"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/expenses/employee-expense/{key}
_Update an employee expense_

**Request example — Updates an employee expense:**
```json
{
  "memo": "Covered by customer"
}
```
**Response 200 — Reference to updated employee expense:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "href": "/objects/expenses/employee-expense/124"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/expenses/employee-expense/{key}
_Delete an employee expense_


## GET /objects/expenses/expense-to-approve
_List employee expenses to approve_

**Response 200 — List employee expenses to approve:**
```json
{
  "ia::result": [
    {
      "key": "101",
      "id": "101",
      "href": "/objects/expenses/expense-to-approve/101"
    },
    {
      "key": "102",
      "id": "102",
      "href": "/objects/expenses/expense-to-approve/102"
    },
    {
      "key": "103",
      "id": "103",
      "href": "/objects/expenses/expense-to-approve/103"
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

## GET /objects/expenses/expense-to-approve-line
_List employee expense lines to approve_

**Response 200 — List of expense to approve lines:**
```json
{
  "ia::result": [
    {
      "key": "101",
      "id": "101",
      "href": "/objects/expenses/expense-to-approve-line/101"
    },
    {
      "key": "102",
      "id": "102",
      "href": "/objects/expenses/expense-to-approve-line/102"
    },
    {
      "key": "103",
      "id": "103",
      "href": "/objects/expenses/expense-to-approve-line/103"
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

## GET /objects/expenses/expense-to-approve-line/{key}
_Get an approve employee expense line_

**Response 200 — Details of the approve employee expense line:**
```json
{
  "ia::result": {
    "key": "312",
    "id": "312",
    "entryDate": "2021-01-23",
    "baseCurrency": "USD",
    "baseAmount": "123.45",
    "reimbursementCurrency": "CAD",
    "reimbursementAmount": "123.45",
    "txnCurrency": "INR",
    "txnAmount": "123.45",
    "totalSelected": "123.45",
    "totalPaid": "123.45",
    "quantity": "5.75",
    "unitRate": "20.00",
    "paidTo": "Hotel Westin",
    "paidFor": "Attending conference",
    "glAccount": {
      "key": "158",
      "id": "6775.30",
      "name": "Travel",
      "href": "/objects/general-ledger/account/23"
    },
    "expenseType": {
      "key": "6000",
      "id": "Meals",
      "href": "/objects/expense-type/34"
    },
    "lineNumber": 1,
    "reimburseToBaseConversion": {
      "exchangeRateDate": "2021-01-23",
      "exchangeRateTypeId": "-1",
      "exchangeRate": "1.18999"
    },
    "transactionToReimburseConversion": {
      "exchangeRate": "65",
      "exchangeRateDate": "2021-01-23",
      "exchangeRateTypeId": "-1"
    },
    "state": "draft",
    "isBillable": false,
    "isBilled": false,
    "form1099": {
      "isForm1099": "true",
      "type": "MISC",
      "box": "3"
    },
    "paymentType": {
      "key": "1",
      "id": "1",
      "name": "Non-reimburse",
      "isNonReimbursable": false,
      "href": "string"
    },
    "audit": {
      "createdDateTime": "2022-04-20T16:20:00Z",
      "modifiedDateTime": "2022-04-20T16:20:00Z",
      "createdBy": "1",
      "modifiedBy": "95"
    },
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "USA"
      },
      "department": {
        "key": "12",
        "id": "12",
        "name": "IT"
      },
      "employee": {
        "key": "10",
        "id": "EMP-10",
        "href": "/objects/company-config/employee/10"
      },
      "employeeContact": {
        "key": 20,
        "id": "Thomas, Glenn",
        "href": "/objects/company-config/contact/20"
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
    "approveEmployeeExpense": {
      "id": "1",
      "key": "1"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/expenses/expense-to-approve/{key}
_Get an employee expense to approve_

**Response 200 — Details of the approve employee expense:**
```json
{
  "ia::result": {
    "key": "124",
    "id": "124",
    "createdDate": "2021-01-23",
    "employee": {
      "key": "12345",
      "id": "EMP-025",
      "href": "/objects/company-config/employee/12345"
    },
    "employeeContact": {
      "key": "20",
      "id": "Thomas, Glenn",
      "firstName": "Glenn",
      "lastName": "Thomas",
      "href": "/objects/company-config/contact/20"
    },
    "state": "draft",
    "basePayment": {
      "baseCurrency": "USD",
      "paidDate": "2021-01-23",
      "totalEntered": "123.45",
      "totalPaid": "123.45",
      "totalDue": "123.45",
      "totalSelected": "110.00"
    },
    "reimbursement": {
      "reimbursementCurrency": "EUR",
      "totalEntered": "123.16",
      "totalPaid": "123.16",
      "totalDue": "123.16",
      "totalSelected": "123.16"
    },
    "expenseReportNumber": "EXP-00001",
    "expenseSummary": {
      "key": "334",
      "id": "334",
      "title": "Expenses 2023/01/31 batch",
      "postingDate": "2021-01-23",
      "state": "open",
      "preventGLPosting": false,
      "href": "/objects/projects/employee-expense-summary/12345"
    },
    "nonReimbursable": {
      "baseTotalEntered": "123.45",
      "reimbursementTotalEntered": "123.45"
    },
    "memo": "Paid to employee",
    "description": "Supplies for customer training",
    "reclassificationNotes": "Classified as supplies, not travel expense",
    "attachment": {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/attachment/12345"
    },
    "audit": {
      "createdDateTime": "2014-01-08T11:28:12Z",
      "modifiedDateTime": "2022-04-20T16:20:00Z",
      "createdBy": "1",
      "modifiedBy": "95"
    },
    "lines": [
      {
        "key": "312",
        "id": "312",
        "entryDate": "2021-01-23",
        "baseCurrency": "USD",
        "baseAmount": "123.45",
        "reimbursementCurrency": "CAD",
        "reimbursementAmount": "123.45",
        "txnCurrency": "INR",
        "txnAmount": "123.45",
        "totalSelected": "123.45",
        "totalPaid": "123.45",
        "quantity": "5.75",
        "unitRate": "20.00",
        "paidTo": "Hotel Westin",
        "paidFor": "Attending conference",
        "glAccount": {
          "key": "158",
          "id": "6775.30",
          "name": "Travel",
          "href": "/objects/general-ledger/account/23"
        },
        "expenseType": {
          "key": "6000",
          "id": "Meals",
          "href": "/objects/expense-type/34"
        },
        "lineNumber": 1,
        "reimburseToBaseConversion": {
          "exchangeRateDate": "2021-01-23",
          "exchangeRateTypeId": "-1",
          "exchangeRate": "1.18999"
        },
        "transactionToReimburseConversion": {
          "exchangeRate": "65",
          "exchangeRateDate": "2021-01-23",
          "exchangeRateTypeId": "-1"
        },
        "state": "draft",
        "isBillable": false,
        "isBilled": false,
        "form1099": {
          "isForm1099": "true",
          "type": "MISC",
          "box": "3"
        },
        "paymentType": {
          "key": "1",
          "id": "1",
          "name": "Non-reimburse",
          "isNonReimbursable": false,
          "href": "string"
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
        },
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "name": "USA"
          },
          "department": {
            "key": "12",
            "id": "12",
            "name": "IT"
          },
          "employee": {
            "key": "10",
            "id": "EMP-10",
            "href": "/objects/company-config/employee/10"
          },
          "employeeContact": {
            "key": 20,
            "id": "Thomas, Glenn",
            "firstName": "Glenn",
            "lastName": "Thomas",
            "href": "/objects/company-config/contact/20"
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
        "approveEmployeeExpense": {
          "id": "1",
          "key": "1"
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

## GET /objects/expenses/unit-rate
_List unit rates_

**Response 200 — List unit rates:**
```json
{
  "ia::result": [
    {
      "key": "12345",
      "id": "Travel-rate",
      "href": "/objects/expenses/unit-rate/12345"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0,
    "start": 1,
    "pageSize": 100,
    "next": 101,
    "previous": null
  }
}
```

## GET /objects/expenses/unit-rate/{key}
_Get a unit rate_

**Response 200 — Get a unit rate:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "23",
    "href": "/objects/expenses/unit-rate/23",
    "rate": "10",
    "startDate": "2021-01-23",
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
    "employeeExpenseType": {
      "name": "Travel",
      "key": "47",
      "id": "47",
      "href": "/objects/expenses/employee-expense-type/47"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
