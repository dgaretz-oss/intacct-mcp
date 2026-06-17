# Order Entry

## GET /objects/order-entry/customer-gl-group
_List customer GL groups_

**Response 200 — List customer GL groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Auto VGL Group",
      "href": "/objects/order-entry/customer-gl-group/1"
    },
    {
      "key": "13",
      "id": "VGL Group",
      "href": "/objects/order-entry/customer-gl-group/13"
    },
    {
      "key": "147",
      "id": "Stationary VGL Group",
      "href": "/objects/order-entry/customer-gl-group/147"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/order-entry/customer-gl-group
_Create a customer GL group_

**Request example — Create a customer GL group:**
```json
{
  "id": "Stationary VGL Group",
  "status": "active"
}
```
**Response 201 — Reference to new customer GL group:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "VGL Group",
    "href": "/objects/order-entry/customer-gl-group/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/customer-gl-group/{key}
_Get a customer GL group_

**Response 200 — Get a customer GL group:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "VGL Group",
    "status": "active",
    "audit": {
      "createdDateTime": "2024-10-22T07:37:32Z",
      "modifiedDateTime": "2024-10-22T07:37:32Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "href": "/objects/order-entry/customer-gl-group/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/customer-gl-group/{key}
_Update a customer GL group_

**Request example — Update a customer GL group:**
```json
{
  "status": "active"
}
```
**Response 200 — Reference to updated customer GL group:**
```json
{
  "ia::result": {
    "id": "6",
    "status": "active",
    "href": "/objects/order-entry/customer-gl-group/18"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/customer-gl-group/{key}
_Delete a customer GL group_


## GET /objects/order-entry/document
_List Order Entry documents_

**Response 200 — List documents:**
```json
{
  "ia::result": [
    {
      "key": "453",
      "id": "Sales Invoice-SUBINV#0182#doc",
      "href": "/objects/order-entry/document::Sales%20Invoice/453"
    },
    {
      "key": "442",
      "id": "Sales Order-SO0023",
      "href": "/objects/order-entry/document::Sales%20Order/442"
    },
    {
      "key": "446",
      "id": "Sales Order-SO0024",
      "href": "/objects/order-entry/document::Sales%20Order/446"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/order-entry/document-configuration-preference
_List document configuration preferences_

**Response 200 — List document configuration preferences:**
```json
{
  "ia::result": [
    {
      "key": "531",
      "id": "531",
      "href": "/objects/order-entry/document-configuration-preference/531"
    },
    {
      "key": "532",
      "id": "532",
      "href": "/objects/order-entry/document-configuration-preference/532"
    },
    {
      "key": "530",
      "id": "530",
      "href": "/objects/order-entry/document-configuration-preference/530"
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

## GET /objects/order-entry/document-configuration-preference/{key}
_Get a document configuration preference_

**Response 200 — Get a document configuration preference:**
```json
{
  "ia::result": {
    "id": "530",
    "key": "530",
    "moduleName": "orderEntry",
    "documentType": {
      "id": "27",
      "key": "27",
      "name": "SUB Activation RevRec",
      "status": "active",
      "href": "/objects/order-entry/txn-definition::SUB%20Activation%20RevRec/27"
    },
    "summaryFrequency": "eachDocument",
    "inventoryJournal": {
      "key": "2",
      "id": "ICJ",
      "name": "Inventory Journal",
      "href": "/objects/general-ledger/journal/2"
    },
    "revenueRecognitionJournal": {
      "key": "16",
      "id": "RRJ",
      "name": "Revenue Recognition Journal",
      "href": "/objects/general-ledger/journal/16"
    },
    "defaultDeferredRevenueGLAccount": {
      "key": "163",
      "id": "2300.05",
      "name": "Deferred Revenue Account- Other",
      "href": "/objects/general-ledger/account/163"
    },
    "additionalPostingJournal": {
      "key": null,
      "id": null,
      "name": null
    },
    "salesJournal": {
      "key": "3",
      "id": "SOJ",
      "name": "Sales Journal",
      "href": "/objects/general-ledger/journal/3"
    },
    "emailTemplate": {
      "id": null,
      "key": null,
      "name": null
    },
    "audit": {
      "createdDateTime": "2026-09-13T05:23:35Z",
      "modifiedDateTime": "2026-09-13T05:23:35Z",
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
    "href": "/objects/order-entry/document-configuration-preference/530"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/document-configuration-preference/{key}
_Update a document configuration preference_

**Request example — Update a document configuration preference:**
```json
{
  "additionalPostingJournal": {
    "key": "58"
  }
}
```
**Response 200 — Reference to updated document configuration preference:**
```json
{
  "ia::result": {
    "key": "530",
    "id": "530",
    "href": "/objects/order-entry/document-configuration-preference/530"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/document-history
_List document histories_

**Response 200 — List document histories:**
```json
{
  "ia::result": [
    {
      "key": "15",
      "id": "15",
      "href": "/objects/order-entry/document-history/15"
    },
    {
      "key": "16",
      "id": "16",
      "href": "/objects/order-entry/document-history/16"
    },
    {
      "key": "17",
      "id": "17",
      "href": "/objects/order-entry/document-history/17"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/order-entry/document-history/{key}
_Get a document history_

**Response 200 — Get a document history:**
```json
{
  "ia::result": {
    "id": "411",
    "key": "411",
    "convertedTo": {
      "key": "483",
      "id": "Sales Invoice-SUBINV#0200#doc",
      "documentType": "Sales Invoice",
      "href": "/objects/order-entry-document::Sales%20Invoice/483"
    },
    "convertedFrom": {
      "key": "482",
      "id": "Sales Order-SO0037",
      "documentType": "Sales Order",
      "href": "/objects/order-entry-document::Sales%20Order/482"
    },
    "orderEntryDocument": {
      "key": "482",
      "id": "Sales Order-SO0037",
      "documentType": "Sales Order",
      "href": "/objects/order-entry-document::Sales%20Order/482"
    },
    "href": "/objects/order-entry/document-history/411"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/document-line
_List document lines_

**Response 200 — List document lines:**
```json
{
  "ia::result": [
    {
      "key": "19",
      "id": "19",
      "href": "/objects/order-entry/document-line::Sales%20Invoice/19"
    },
    {
      "key": "24",
      "id": "24",
      "href": "/objects/order-entry/document-line::Sales%20Invoice/24"
    },
    {
      "key": "25",
      "id": "25",
      "href": "/objects/order-entry/document-line::Sales%20Quote/25"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/order-entry/document-line-detail
_List document line detail objects_

**Response 200 — List document line detail objects:**
```json
{
  "value": {
    "ia::result": [
      {
        "key": "1",
        "id": "1",
        "href": "/objects/order-entry/document-line-detail/1"
      },
      {
        "key": "2",
        "id": "2",
        "href": "/objects/order-entry/document-line-detail/2"
      },
      {
        "key": "3",
        "id": "3",
        "href": "/objects/order-entry/document-line-detail/3"
      }
    ],
    "ia::meta": {
      "totalCount": 3,
      "start": 1,
      "pageSize": 100
    }
  }
}
```

## GET /objects/order-entry/document-line-detail/{key}
_Get a document line detail object_

**Response 200 — Get a document line detail object:**
```json
{
  "ia::result": {
    "id": "15",
    "key": "15",
    "orderEntryDocumentLine": {
      "id": "772",
      "key": "772",
      "documentType": "Sales Order",
      "href": "/objects/order-entry-document-line::Sales%20Order/772"
    },
    "item": {
      "id": "Hose Clamp",
      "key": "147",
      "href": "/objects/item/147"
    },
    "quantity": "1",
    "serialNumber": "SMR 617",
    "lotNumber": "1890",
    "aisle": {
      "key": "2",
      "id": "A2",
      "href": "/objects/inventory-control/aisle/2"
    },
    "row": {
      "key": "3",
      "id": "R3",
      "href": "/objects/inventory-control/row/3"
    },
    "bin": {
      "key": "12",
      "id": "B12",
      "href": "/objects/inventory-control/bin/12"
    },
    "expirationDate": "2024-12-31",
    "audit": {
      "createdDateTime": "2024-06-13T00:00:00Z",
      "modifiedDateTime": "2024-06-26T05:51:05Z",
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
    "href": "/objects/order-entry/document-line-detail/15"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/document-line-subtotal
_List document line subtotals_

**Response 200 — List document line subtotals:**
```json
{
  "ia::result": [
    {
      "key": "23",
      "id": "23",
      "href": "/objects/order-entry/document-line-subtotal/23"
    },
    {
      "key": "22",
      "id": "22",
      "href": "/objects/order-entry/document-line-subtotal/22"
    },
    {
      "key": "21",
      "id": "21",
      "href": "/objects/order-entry/document-line-subtotal/21"
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

## GET /objects/order-entry/document-line-subtotal/{key}
_Get a document line subtotal_

**Response 200 — Get a document line subtotal:**
```json
{
  "ia::result": {
    "id": "22",
    "key": "22",
    "document": {
      "id": "24",
      "key": "24",
      "href": "/objects/order-entry/document/24"
    },
    "description": "G1 Goods and Services Tax",
    "absoluteValue": "11.00000000",
    "percentValue": "10.00000000",
    "total": null,
    "status": "active",
    "taxDetail": {
      "key": "20",
      "id": "G1 Goods and Services Tax",
      "href": "/objects/tax/tax-detail/20"
    },
    "dimensions": {
      "location": {
        "key": "4",
        "id": "4",
        "name": "Australia",
        "href": "/objects/company-config/location/4"
      },
      "department": {
        "key": null,
        "id": null,
        "name": null
      }
    },
    "txnAbsoluteValue": "11.00000000",
    "txnTotal": null,
    "documentLine": {
      "id": "10",
      "key": "10",
      "href": "/objects/order-entry/document-line/10"
    },
    "enableOverrideTax": false,
    "systemTaxDetail": {
      "key": null,
      "id": null
    },
    "href": "/objects/order-entry/document-line-subtotal/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/document-line/{key}
_Get a document line_

**Response 200 — Get a document line:**
```json
{
  "ia::result": {
    "id": "925",
    "key": "925",
    "documentHeader": {
      "key": "599",
      "id": "Sales Order-SO0066",
      "documentType": "Sales Order",
      "href": "/objects/order-entry-document::Sales%20Order/599"
    },
    "documentType": "Sales Order",
    "lineNumber": 0,
    "dimensions": {
      "item": {
        "key": "1",
        "id": "1",
        "name": "PC Computer",
        "href": "/objects/inventory-control/item/1"
      },
      "warehouse": {
        "id": "12",
        "key": "12",
        "href": "/objects/inventory-control/warehouse/12"
      },
      "location": {
        "id": "21",
        "key": "21",
        "href": "/objects/company-config/location/21"
      },
      "customer": {
        "key": "23",
        "id": "23",
        "name": "Power Aerospace Materials",
        "href": "/objects/accounts-receivable/customer/23"
      }
    },
    "item": {
      "key": "6",
      "id": "6",
      "href": "/objects/inventory-control/item/6"
    },
    "lineDescription": "Computer",
    "unit": "Each",
    "quantity": "10",
    "quantityConverted": "1",
    "retailPrice": "222",
    "price": "333",
    "audit": {
      "createdDateTime": "2024-12-18T00:00:00Z",
      "modifiedDateTime": "2024-12-18T10:27:15Z",
      "createdBy": "5",
      "modifiedBy": "5"
    },
    "status": "active",
    "unitQuantity": "1",
    "multiplier": 1,
    "unitPrice": "333",
    "txnCurrency": "USD",
    "baseCurrency": "USD",
    "priceInTxnCurrency": "333",
    "conversionType": "quantity",
    "allowDropShip": false,
    "allowBuyToOrder": false,
    "quantityRemaining": "10",
    "trackingDetail": [],
    "lineSubtotals": [],
    "timesheetNotes": "Worked extra hours on project",
    "timeType": {
      "id": "Design",
      "key": 11,
      "href": "/objects/time/time-type/11"
    },
    "employeeExpenseType": {
      "id": "Meals",
      "key": 4,
      "href": "/objects/expenses/employee-expense-type/4"
    },
    "href": "/objects/order-entry/document-line::Sales%20Order/925"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a document line (Construction):**
```json
{
  "ia::result": {
    "key": "44",
    "id": "44",
    "href": "/objects/order-entry/document-line::Sales%20Invoice/44",
    "documentType": "Sales Invoice",
    "lineNumber": 1,
    "item": {
      "key": "10",
      "id": "MX001",
      "href": "/objects/inventory-control/item/10"
    },
    "itemAlias": {
      "key": "6",
      "id": "IXN",
      "href": "/objects/accounts-receivable/customer-item-cross-reference/6"
    },
    "lineDescription": null,
    "memo": "Payment ACH",
    "priceCalculationMemo": "Fair value price list",
    "unit": "Each",
    "quantity": "40.10",
    "unitQuantity": "10.10",
    "unitPrice": "10.50",
    "price": "33.66",
    "quantityConverted": "5.10",
    "retailPrice": "10.44",
    "audit": {
      "createdDateTime": "2024-04-20T16:20:00Z",
      "modifiedDateTime": "2024-04-20T16:20:00Z",
      "createdBy": "9",
      "modifiedBy": "95"
    },
    "status": "active",
    "costMethod": "average",
    "discountPercent": "10.50",
    "multiplier": 1,
    "sourceDocument": {
      "key": "77",
      "id": "Sales Order-SO0022",
      "documentType": "Sales Order",
      "href": "/objects/order-entry-document::Sales%20Order/77"
    },
    "sourceDocumentLine": {
      "key": "2234",
      "id": "2234",
      "documentType": "Sales Order",
      "href": "/objects/order-entry/document-line::Sales%20Order/2234"
    },
    "isPriceProrated": true,
    "discountMemo": "Festival discount",
    "baseCurrency": "USD",
    "txnCurrency": "CAD",
    "priceInTxnCurrency": "10.00",
    "isBillable": true,
    "isBilled": true,
    "taxRate": "10.05",
    "taxInBaseCurrency": "10.50",
    "taxInTxnCurrency": "40.50",
    "discount": "10.25",
    "enableTax": false,
    "quantityRemaining": "10.10",
    "conversionType": "quantity",
    "dimensions": {
      "location": {
        "key": "22",
        "id": "LOC-22",
        "name": "California",
        "href": "/objects/company-config/location/22"
      },
      "department": {
        "key": "9",
        "id": "Sales",
        "name": "Sales and Marketing",
        "href": "/objects/company-config/department/9"
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
        "name": "Rancho Nuevo",
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
        "id": "TSK01",
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
        "name": "Laptop 1"
      },
      "contract": {
        "id": "CON-0045-1",
        "key": "12",
        "name": "ACME Widgets - Service",
        "href": "/objects/contracts/contract/12"
      }
    },
    "itemRenewalTemplate": {
      "key": "45",
      "id": "Sales Renewal Template",
      "href": "/objects/order-entry/renewal-template/45"
    },
    "revenueRecognitionStartDate": "2024-01-01",
    "revenueRecognitionEndDate": "2024-12-31",
    "revenueRecognitionTemplate": {
      "id": "MilestoneUserspecified",
      "key": "2",
      "href": "/objects/accounts-receivable/revenue-recognition-template/2"
    },
    "requestedShippingDate": "2024-04-04",
    "shipByDate": "2024-04-04",
    "pickTicketPrintedDate": "2024-04-04",
    "cancelAfterDate": "2024-04-15",
    "doNotShipBeforeDate": "2024-04-04",
    "doNotShipAfterDate": "2024-04-15",
    "shippedDate": "2024-04-04",
    "servicePeriodStartDate": "2024-04-01",
    "servicePeriodEndDate": "2024-04-01",
    "allowDropShip": true,
    "allowBuyToOrder": true,
    "revision": {
      "unitQuantity": "10",
      "quantity": "10",
      "unitValue": "8.00",
      "value": "8.00",
      "valueInTxnCurrency": "10.00",
      "price": "10.00",
      "unitPrice": "10.00",
      "priceInTxnCurrency": "10.00"
    },
    "draft": {
      "unitQuantity": "10",
      "quantity": "10",
      "price": "20.00",
      "basePrice": "20.00"
    },
    "posted": {
      "quantity": "10.00",
      "price": "20.00",
      "basePrice": "20.00"
    },
    "addedByChangeDocument": false,
    "projectContractBilling": {
      "externalReferenceNumber": "HGS-1024",
      "description": "Construction of clubhouse and offices",
      "billingType": "timeAndMaterial",
      "contractLineValue": "1000.00",
      "priorApplicationAmount": "1000.00",
      "completedThisPeriodAmount": "1000.00",
      "storedMaterialsAmount": "1000.00",
      "completedToDateAmount": "1000.00",
      "completedToDatePercent": "10.00",
      "balanceRemaining": "1000.00",
      "totalConvertedAmount": "1000.00",
      "totalRemainingAmount": "1000.00",
      "isSummarized": false
    },
    "retainage": {
      "percentage": "10.00",
      "baseAmountRetained": "10.00",
      "txnAmountRetained": "10.00",
      "isReleaseLine": true,
      "previousBalanceAmount": "1000.00",
      "billAmount": "1000.00",
      "balanceAmount": "1000.00",
      "extendedPriceNetAmount": "1000.00",
      "extendedBasePriceNetAmount": "1000.00"
    },
    "isReverseConversion": true,
    "reverseConversion": {
      "price": "100.00",
      "quantity": "100",
      "standardPrice": "100.00",
      "standardQuantity": "100"
    },
    "relatedDocument": {
      "id": "5151",
      "key": "5151",
      "documentNumber": "Sales Order-SD-SO0550",
      "href": "/objects/order-entry/document/5151"
    },
    "relatedDocumentLine": {
      "key": "13965",
      "id": "1--0001",
      "href": "/objects/order-entry/document-line/13965"
    },
    "projectContract": {
      "key": "1",
      "id": "BTI-01",
      "name": "Berkeley Technology Inc - Contract 01",
      "href": "/objects/construction/project-contract/1"
    },
    "projectContractLine": {
      "key": "4",
      "id": "Project-Contract-Line-04",
      "name": "Project contract line 04",
      "href": "/objects/construction/project-contract-line/4"
    },
    "taxSchedule": {
      "key": "1",
      "id": "Sale Goods Standard",
      "href": "/objects/tax/order-entry-tax-schedule/1"
    },
    "buyToOrderContact": {
      "key": "13",
      "id": "contact"
    },
    "trackingDetail": [
      {
        "key": "55",
        "id": "55",
        "href": "/objects/order-entry/document-line-detail/55",
        "quantity": "10",
        "serialNumber": "S1001",
        "lotNumber": "L1001",
        "expirationDate": "2023-04-04",
        "aisle": {
          "href": "/objects/inventory-control/aisle/10",
          "key": "10",
          "id": "AISLE1"
        },
        "bin": {
          "href": "/objects/inventory-control/bin/20",
          "key": "20",
          "id": "BIN1"
        },
        "row": {
          "href": "/objects/inventory-control/row/15",
          "key": "15",
          "id": "ROW1"
        },
        "item": {
          "key": "10",
          "id": "Battery",
          "href": "/objects/inventory-control/item/10"
        },
        "audit": {
          "createdDateTime": "2024-04-20T16:20:00Z",
          "modifiedDateTime": "2024-04-20T16:20:00Z",
          "createdBy": "1",
          "modifiedBy": "95"
        },
        "orderEntryDocumentLine": {
          "key": "23",
          "id": "23",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document-line::Sales%20Order/23"
        }
      }
    ],
    "lineSubtotals": [],
    "timesheetNotes": "Worked extra hours on project",
    "timeType": {
      "id": "Design",
      "key": 11,
      "href": "/objects/time/time-type/11"
    },
    "employeeExpenseType": {
      "id": "Meals",
      "key": 4,
      "href": "/objects/expenses/employee-expense-type/4"
    },
    "documentHeader": {
      "key": "55",
      "id": "Sales Invoice-SO0066",
      "documentType": "Sales Invoice",
      "href": "/objects/order-entry-document::Sales%20Invoice/55"
    }
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## GET /objects/order-entry/document-line::{documentName}
_List lines for named documents_

**Response 200 — List document lines:**
```json
{
  "ia::result": [
    {
      "key": "19",
      "id": "19",
      "href": "/objects/order-entry/document-line::Sales%20Invoice/19"
    },
    {
      "key": "24",
      "id": "24",
      "href": "/objects/order-entry/document-line::Sales%20Invoice/24"
    },
    {
      "key": "25",
      "id": "25",
      "href": "/objects/order-entry/document-line::Sales%20Invoice/25"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/order-entry/document-line::{documentName}
_Create a document line_

**Request example — Create a document line:**
```json
{
  "documentHeader": {
    "key": "469"
  },
  "dimensions": {
    "item": {
      "id": "1"
    },
    "warehouse": {
      "id": "42'"
    },
    "location": {
      "id": "5"
    }
  },
  "unit": "Each",
  "unitQuantity": "1",
  "unitPrice": "650"
}
```
**Response 201 — Reference to new document line:**
```json
{
  "ia::result": {
    "key": "807",
    "href": "/objects/order-entry/document-line::Sales%20Invoice/807"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/document-line::{documentName}/{key}
_Get a line in a named document_

**Response 200 — Get a document line:**
```json
{
  "ia::result": {
    "id": "925",
    "key": "925",
    "documentHeader": {
      "key": "599",
      "id": "Sales Order-SO0066",
      "documentType": "Sales Order",
      "href": "/objects/order-entry-document::Sales%20Order/599"
    },
    "documentType": "Sales Order",
    "lineNumber": 1,
    "dimensions": {
      "item": {
        "key": "11",
        "id": "11",
        "name": "PC Computer",
        "href": "/objects/inventory-control/item/11"
      },
      "warehouse": {
        "id": "6",
        "key": "6",
        "href": "/objects/inventory-control/warehouse/6"
      },
      "location": {
        "id": "13",
        "key": "13",
        "href": "/objects/company-config/location/13"
      },
      "customer": {
        "key": "9",
        "id": "9",
        "name": "Power Aerospace Materials",
        "href": "/objects/accounts-receivable/customer/9"
      }
    },
    "item": {
      "key": "11",
      "id": "11",
      "href": "/objects/inventory-control/item/11"
    },
    "lineDescription": "PC Computer",
    "unit": "Each",
    "quantity": "1",
    "quantityConverted": "1",
    "retailPrice": "222",
    "price": "333",
    "audit": {
      "createdDateTime": "2024-12-18T00:00:00Z",
      "modifiedDateTime": "2024-12-18T10:27:15Z",
      "createdBy": "4",
      "modifiedBy": "4"
    },
    "status": "active",
    "unitQuantity": "1",
    "multiplier": 1,
    "unitPrice": "333",
    "txnCurrency": "USD",
    "baseCurrency": "USD",
    "priceInTxnCurrency": "333",
    "conversionType": "quantity",
    "allowDropShip": false,
    "allowBuyToOrder": false,
    "quantityRemaining": "16",
    "trackingDetail": [],
    "lineSubtotals": [],
    "timesheetNotes": "Worked extra hours on project",
    "timeType": {
      "id": "Design",
      "key": 11,
      "href": "/objects/time/time-type/11"
    },
    "employeeExpenseType": {
      "id": "Meals",
      "key": 4,
      "href": "/objects/expenses/employee-expense-type/4"
    },
    "href": "/objects/order-entry/document-line::Sales%20Order/925"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a document line - Construction:**
```json
{
  "ia::result": {
    "key": "44",
    "id": "44",
    "href": "/objects/order-entry/document-line::Sales%20Invoice/44",
    "documentType": "Sales Invoice",
    "lineNumber": 1,
    "item": {
      "key": "10",
      "id": "MX001",
      "href": "/objects/inventory-control/item/10"
    },
    "itemAlias": {
      "key": "10",
      "id": "IXN",
      "href": "/objects/accounts-receivable/customer-item-cross-reference/10"
    },
    "memo": "Payment ACH",
    "priceCalculationMemo": "Fair value price list",
    "lineDescription": "Payment ACH",
    "unit": "Each",
    "quantity": "40.10",
    "unitQuantity": "10.10",
    "unitPrice": "10.50",
    "price": "33.66",
    "quantityConverted": "5.10",
    "retailPrice": "10.44",
    "audit": {
      "createdDateTime": "2022-07-14T09:18:50Z",
      "modifiedDateTime": "2024-07-08T10:32:03Z",
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
    "costMethod": "average",
    "discountPercent": "10.50",
    "multiplier": 1,
    "sourceDocument": {
      "key": "77",
      "id": "Sales Order-SO0022",
      "documentType": "Sales Order",
      "href": "/objects/order-entry-document::Sales%20Order/77"
    },
    "sourceDocumentLine": {
      "key": "2234",
      "id": "2234",
      "documentType": "Sales Order",
      "href": "/objects/order-entry/document-line::Sales%20Order/2234"
    },
    "isPriceProrated": true,
    "discountMemo": "Festival discount",
    "baseCurrency": "USD",
    "txnCurrency": "CAD",
    "priceInTxnCurrency": "10.00",
    "isBillable": true,
    "isBilled": true,
    "taxRate": "10.05",
    "taxInBaseCurrency": "10.50",
    "taxInTxnCurrency": "40.50",
    "discount": "10.25",
    "enableTax": false,
    "quantityRemaining": "10.10",
    "conversionType": "quantity",
    "dimensions": {
      "location": {
        "key": "22",
        "id": "LOC-22",
        "name": "California",
        "href": "/objects/company-config/location/22"
      },
      "department": {
        "key": "9",
        "id": "Sales",
        "name": "Sales and Marketing",
        "href": "/objects/company-config/department/9"
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
        "id": "TSK01",
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
        "name": "Laptop 1"
      },
      "contract": {
        "id": "CON-0045-1",
        "key": "12",
        "name": "ACME Widgets - Service",
        "href": "/objects/contracts/contract/12"
      }
    },
    "itemRenewalTemplate": {
      "key": "45",
      "id": "Sales Renewal Template",
      "href": "/objects/order-entry/renewal-template/45"
    },
    "revenueRecognitionStartDate": "2024-01-01",
    "revenueRecognitionEndDate": "2024-12-31",
    "revenueRecognitionTemplate": {
      "id": "MilestoneUserspecified",
      "key": "2",
      "href": "/objects/accounts-receivable/revenue-recognition-template/2"
    },
    "requestedShippingDate": "2024-04-04",
    "shipByDate": "2024-04-04",
    "pickTicketPrintedDate": "2024-04-04",
    "cancelAfterDate": "2024-04-04",
    "doNotShipBeforeDate": "2024-04-04",
    "doNotShipAfterDate": "2024-04-04",
    "shippedDate": "2024-04-04",
    "servicePeriodStartDate": null,
    "servicePeriodEndDate": null,
    "allowDropShip": true,
    "allowBuyToOrder": true,
    "revision": {
      "unitQuantity": "10",
      "quantity": "10",
      "unitValue": "8.00",
      "value": "8.00",
      "valueInTxnCurrency": "10.00",
      "price": "10.00",
      "unitPrice": "10.00",
      "priceInTxnCurrency": "10.00"
    },
    "draft": {
      "unitQuantity": "15",
      "quantity": "15",
      "price": "10.00",
      "basePrice": "10.00"
    },
    "posted": {
      "quantity": "10.00",
      "price": "10.00",
      "basePrice": "10.00"
    },
    "addedByChangeDocument": false,
    "projectContractBilling": {
      "externalReferenceNumber": "HGS-1024",
      "description": "Construction of clubhouse and offices",
      "billingType": "timeAndMaterial",
      "contractLineValue": "1000.00",
      "priorApplicationAmount": "1000.00",
      "completedThisPeriodAmount": "1000.00",
      "storedMaterialsAmount": "1000.00",
      "completedToDateAmount": "1000.00",
      "completedToDatePercent": "10.00",
      "balanceRemaining": "1000.00",
      "totalConvertedAmount": "1000.00",
      "totalRemainingAmount": "1000.00",
      "isSummarized": false
    },
    "retainage": {
      "percentage": "10.00",
      "baseAmountRetained": "10.00",
      "txnAmountRetained": "10.00",
      "isReleaseLine": true,
      "previousBalanceAmount": "1000.00",
      "billAmount": "1000.00",
      "balanceAmount": "1000.00",
      "extendedPriceNetAmount": "1000.00",
      "extendedBasePriceNetAmount": "1000.00"
    },
    "isReverseConversion": true,
    "reverseConversion": {
      "price": "100.00",
      "quantity": "100",
      "standardPrice": "100.00",
      "standardQuantity": "100"
    },
    "relatedDocument": {
      "id": "5151",
      "key": "5151",
      "documentNumber": "Sales Order-SD-SO0550",
      "href": "/objects/order-entry/document/5151"
    },
    "relatedDocumentLine": {
      "key": "13965",
      "id": "1--0001",
      "href": "/objects/order-entry/document-line/13965"
    },
    "projectContract": {
      "key": "1",
      "id": "BTI-01",
      "name": "Berkeley Technology Inc - Contract 01",
      "href": "/objects/construction/project-contract/1"
    },
    "projectContractLine": {
      "key": "4",
      "id": "Project-Contract-Line-04",
      "name": "Project contract line 04",
      "href": "/objects/construction/project-contract-line/4"
    },
    "taxSchedule": {
      "key": "1",
      "id": "Sale Goods Standard",
      "href": "/objects/tax/order-entry-tax-schedule/1"
    },
    "buyToOrderContact": {
      "key": "13",
      "id": "contact"
    },
    "trackingDetail": [
      {
        "key": "55",
        "id": "55",
        "href": "/objects/order-entry/document-line-detail/55",
        "quantity": "10",
        "serialNumber": "S1001",
        "lotNumber": "L1001",
        "expirationDate": "2023-04-04",
        "aisle": {
          "href": "/objects/inventory-control/aisle/10",
          "key": "10",
          "id": "AISLE1"
        },
        "bin": {
          "href": "/objects/inventory-control/bin/20",
          "key": "20",
          "id": "BIN1"
        },
        "row": {
          "href": "/objects/inventory-control/row/15",
          "key": "15",
          "id": "ROW1"
        },
        "item": {
          "key": "10",
          "id": "Battery",
          "href": "/objects/inventory-control/item/10"
        },
        "audit": {
          "createdDateTime": "2024-04-20T16:20:00Z",
          "modifiedDateTime": "2024-04-20T16:20:00Z",
          "createdBy": "1",
          "modifiedBy": "95"
        },
        "orderEntryDocumentLine": {
          "key": "23",
          "id": "23",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document-line::Sales%20Order/23"
        }
      }
    ],
    "lineSubtotals": [],
    "timesheetNotes": "Worked extra hours on project",
    "timeType": {
      "id": "Design",
      "key": 11,
      "href": "/objects/time/time-type/11"
    },
    "employeeExpenseType": {
      "id": "Meals",
      "key": 4,
      "href": "/objects/expenses/employee-expense-type/4"
    },
    "documentHeader": {
      "key": "55",
      "id": "Sales Invoice-SO0066",
      "documentType": "Sales Invoice",
      "href": "/objects/order-entry-document::Sales%20Invoice/55"
    }
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## PATCH /objects/order-entry/document-line::{documentName}/{key}
_Update a document line_

**Request example — Update a document line:**
```json
{
  "unitQuantity": "10"
}
```
**Response 200 — Reference to updated document line:**
```json
{
  "ia::result": {
    "key": "52",
    "href": "/objects/order-entry/document-line::Sales%20Invoice/52"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/document-line::{documentName}/{key}
_Delete a document line_


## GET /objects/order-entry/document-subtotal
_List document subtotals_

**Response 200 — List document subtotals:**
```json
{
  "ia::result": [
    {
      "key": "13",
      "id": "13",
      "href": "/objects/order-entry/document-subtotal/13"
    },
    {
      "key": "14",
      "id": "14",
      "href": "/objects/order-entry/document-subtotal/14"
    },
    {
      "key": "15",
      "id": "15",
      "href": "/objects/order-entry/document-subtotal/15"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## GET /objects/order-entry/document-subtotal/{key}
_Get a document subtotal_

**Response 200 — Get a document subtotal:**
```json
{
  "ia::result": {
    "id": "307",
    "key": "307",
    "description": "Sales Discount",
    "absoluteValue": "14.5",
    "percentValue": "1.45",
    "total": "-14.5",
    "dimensions": {
      "location": {
        "key": "36",
        "id": "YNK",
        "href": "/objects/company-config/location/36"
      },
      "department": {
        "key": "38",
        "id": "Accounting",
        "href": "/objects/company-config/department/38"
      },
      "customer": {
        "key": "1",
        "id": "1",
        "name": "Power Aerospace Materials",
        "href": "/objects/accounts-receivable/customer/1"
      }
    },
    "txnAbsoluteValue": "14.5",
    "txnTotal": "-14.5",
    "documentLine": {
      "id": "233",
      "key": "233",
      "documentType": "Sales Invoice",
      "href": "/objects/order-entry-document-line::Sales%20Invoice/233"
    },
    "documentHeader": {
      "key": "21",
      "id": "Sales Invoice-SUBINV#0100#doc",
      "documentType": "Sales Invoice",
      "href": "/objects/order-entry-document::Sales%20Invoice/21"
    },
    "audit": {
      "createdDateTime": "2022-07-14T09:18:50Z",
      "modifiedDateTime": "2024-07-08T10:32:03Z",
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
    "href": "/objects/order-entry/document-subtotal/307"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/document/{key}
_Get an Order Entry document_

**Response 200 — Get a document:**
```json
{
  "ia::result": {
    "key": "453",
    "documentNumber": "SUBINV#0182#doc",
    "id": "Sales Invoice-SUBINV#0182#doc",
    "sourceDocument": {
      "id": "Sales Order-SO0026",
      "key": "451",
      "documentType": "Sales Order",
      "href": "/objects/order-entry/document::Sales%20Order/451"
    },
    "state": "pending",
    "txnDate": "2024-03-29",
    "audit": {
      "createdDateTime": "2024-11-10T18:36:30Z",
      "createdBy": "1",
      "modifiedBy": "1",
      "modifiedDateTime": "2024-11-10T18:36:32Z"
    },
    "invoiceType": "invoice",
    "invoiceMode": "b1",
    "eInvoiceStatus": "paymentReceived",
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "entity": {
      "key": "46",
      "id": "CORP",
      "name": "Corp",
      "href": "/objects/company-config/entity/46"
    },
    "status": "active",
    "dueDate": "2024-10-28",
    "documentType": "Sales Invoice",
    "txnDefinition": {
      "id": "Sales Invoice",
      "key": "188",
      "href": "/objects/order-entry-txn-definition::Sales%20Invoice/188"
    },
    "contacts": {
      "primary": {
        "key": "304",
        "id": "Power Aerospace Materials(C1)"
      },
      "shipTo": {
        "key": "304",
        "id": "Power Aerospace Materials(C1)"
      },
      "billTo": {
        "key": "304",
        "id": "Power Aerospace Materials(C1)"
      }
    },
    "isPrinted": false,
    "isBackordered": false,
    "subtotal": "750.44",
    "total": "742.54",
    "txnCurrency": "USD",
    "exchangeRate": {
      "date": "2024-03-29",
      "rate": "1"
    },
    "subtotalInTxnCurrency": "750.55",
    "totalInTxnCurrency": "742.5",
    "baseCurrency": "USD",
    "isSystemGeneratedDocument": false,
    "invoiceRun": {
      "key": "88",
      "id": "88"
    },
    "postingDate": "2024-03-29",
    "paymentStatus": "open",
    "customer": {
      "key": "1",
      "id": "1",
      "name": "Power Aerospace Materials",
      "href": "/objects/accounts-receivable/customer/1"
    },
    "attachment": {
      "key": "42",
      "id": "Supporting doc",
      "href": "/objects/company-config/attachment/42"
    },
    "sourceModule": "orderEntry",
    "lines": [
      {
        "id": "790",
        "key": "790",
        "documentHeader": {
          "key": "453",
          "id": "Sales Invoice-SUBINV#0182#doc",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document::Sales%20Invoice/453"
        },
        "documentType": "Sales Invoice",
        "lineNumber": 0,
        "dimensions": {
          "item": {
            "key": "1",
            "id": "1--PC Computer",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/1"
          },
          "warehouse": {
            "id": "1",
            "key": "1",
            "href": "/objects/inventory-control/warehouse/1"
          },
          "location": {
            "id": "1",
            "key": "1",
            "href": "/objects/company-config/location/1"
          },
          "customer": {
            "key": "1",
            "id": "1--Power Aerospace Materials",
            "name": "Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          }
        },
        "item": {
          "key": "1",
          "id": "1--PC Computer",
          "href": "/objects/inventory-control/item/1"
        },
        "lineDescription": "PC Computer",
        "memo": null,
        "unit": "Each",
        "quantity": "1",
        "quantityConverted": "0",
        "retailPrice": "750",
        "price": "742.5",
        "audit": {
          "createdDateTime": "2024-05-27T06:22:06Z",
          "modifiedDateTime": "2024-05-27T06:22:09Z",
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
        "costMethod": "standard",
        "unitQuantity": "1",
        "multiplier": 1,
        "unitPrice": "750",
        "txnCurrency": "USD",
        "baseCurrency": "USD",
        "priceInTxnCurrency": "750",
        "conversionType": "quantity",
        "allowDropShip": false,
        "allowBuyToOrder": false,
        "quantityRemaining": "1",
        "trackingDetail": [],
        "lineSubtotals": [],
        "timesheetNotes": "Worked extra hours on project",
        "timeType": {
          "id": "Design",
          "key": 11,
          "href": "/objects/time/time-type/11"
        },
        "employeeExpenseType": {
          "id": "Meals",
          "key": 4,
          "href": "/objects/expenses/employee-expense-type/4"
        },
        "href": "/objects/order-entry/document-line::Sales%20Invoice/790"
      }
    ],
    "history": [
      {
        "id": "382",
        "key": "382",
        "convertedTo": {
          "key": "453",
          "id": "Sales Invoice-SUBINV#0182#doc",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document::Sales%20Invoice/453"
        },
        "convertedFrom": {
          "id": "Sales Order-SO0026",
          "key": "451",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document::Sales%20Order/451"
        },
        "orderEntryDocument": {
          "key": "451",
          "id": "Sales Order-SO0026",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document::Sales%20Order/451"
        },
        "href": "/objects/order-entry/document-history/382"
      },
      {
        "id": "380",
        "key": "380",
        "convertedTo": {
          "key": "451",
          "id": "Sales Order-SO0026",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document::Sales%20Order/451"
        },
        "orderEntryDocument": {
          "key": "451",
          "id": "Sales Order-SO0026",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document::Sales%20Order/451"
        },
        "href": "/objects/order-entry/document-history/380"
      }
    ],
    "subtotals": [
      {
        "id": "1204",
        "key": "1204",
        "description": "Sales Discount",
        "absoluteValue": "0",
        "total": "0",
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "href": "/objects/company-config/location/1"
          },
          "customer": {
            "key": "1",
            "id": "1--Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          }
        },
        "txnAbsoluteValue": "0",
        "txnTotal": "0",
        "documentLine": {
          "id": "790",
          "key": "790",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document-line::Sales%20Invoice/790"
        },
        "audit": {
          "createdDateTime": "2024-11-10T18:36:31Z",
          "modifiedDateTime": "2024-11-10T18:36:31Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/order-entry/document-subtotal/1204"
      },
      {
        "id": "1205",
        "key": "1205",
        "description": "Discounted Totals",
        "absoluteValue": "7.5",
        "percentValue": "1",
        "total": "7.5",
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "href": "/objects/company-config/location/1"
          },
          "customer": {
            "key": "1",
            "id": "1--Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          }
        },
        "txnAbsoluteValue": "7.5",
        "txnTotal": "-7.5",
        "documentLine": {
          "id": "790",
          "key": "790",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document-line::Sales%20Invoice/790"
        },
        "audit": {
          "createdDateTime": "2024-11-10T18:36:31Z",
          "modifiedDateTime": "2024-11-10T18:36:31Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/order-entry/document-subtotal/1205"
      },
      {
        "id": "1206",
        "key": "1206",
        "description": "Sales Tax",
        "absoluteValue": "0",
        "total": "0",
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "href": "/objects/company-config/location/1"
          },
          "customer": {
            "key": "1",
            "id": "1",
            "href": "/objects/accounts-receivable/customer/1"
          }
        },
        "txnAbsoluteValue": "0",
        "txnTotal": "0",
        "documentLine": {
          "id": "790",
          "key": "790",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document-line::Sales%20Invoice/790"
        },
        "audit": {
          "createdDateTime": "2024-11-10T18:36:31Z",
          "modifiedDateTime": "2024-11-10T18:36:31Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/order-entry/document-subtotal/1206"
      }
    ],
    "href": "/objects/order-entry/document::Sales%20Invoice/453"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a document - Construction subscription:**
```json
{
  "ia::result": {
    "key": "55",
    "id": "Sales Invoice-SI-O122",
    "href": "/objects/order-entry/document::Sales%20Invoice/55",
    "documentNumber": "SI-O122",
    "documentType": "Sales Invoice",
    "state": "draft",
    "isPrinted": true,
    "isBackordered": false,
    "subtotal": "50.10",
    "subtotalInTxnCurrency": "51.10",
    "total": "100.10",
    "totalInTxnCurrency": "100.11",
    "baseCurrency": "USD",
    "txnCurrency": "USD",
    "exchangeRate": {
      "date": "2023-01-23",
      "rate": "1.0789",
      "typeId": "1",
      "typeName": "Intacct Daily Rate"
    },
    "txnDate": "2024-04-04",
    "dueDate": "2024-04-04",
    "isSystemGeneratedDocument": true,
    "postingDate": "2024-04-04",
    "referenceNumber": "SALES-100",
    "notes": "Fast order",
    "memo": "Lowry solutions",
    "contractId": "CN100123",
    "contractDescription": "Sales & Service",
    "paymentStatus": "paid",
    "invoiceDate": "2024-04-04",
    "customerPONumber": "ABOTT-1001",
    "trackingNumber": "TK-1002",
    "shipByDate": "2024-04-04",
    "shippedDate": "2024-04-04",
    "serviceDeliveryDate": "2024-04-04",
    "cancelAfterDate": "2024-04-15",
    "doNotShipBeforeDate": "2024-04-03",
    "doNotShipAfterDate": "2024-04-15",
    "requestedShippingDate": "2024-04-04",
    "retainagePercent": 10,
    "scope": "Subcontractor agrees to provide labor and materials for utility trenching for Five Oaks Storage facilities according to contract.",
    "inclusions": "Includes drive through building",
    "exclusions": "Excludes additional purchase",
    "terms": "Follow all safety rules and security procedure that are in force and applicable during execution of work.",
    "schedule": {
      "scheduledStartDate": "2024-05-07",
      "scheduledCompletionDate": "2024-10-07",
      "actualStartDate": "2024-05-07",
      "actualCompletionDate": "2024-10-10",
      "revisedCompletionDate": "2024-11-01",
      "substantialCompletionDate": "2024-10-10",
      "noticeToProceedDate": "2024-10-10",
      "responseDueDate": "2024-10-10",
      "executedOnDate": "2024-10-10",
      "scheduleImpactNotes": "None"
    },
    "internalReference": {
      "referenceNumber": "INT-01",
      "initiatedBy": {
        "key": "2",
        "id": "dhatchet",
        "name": "David Hatcher",
        "href": "/objects/company-config/employee/2"
      },
      "verbalApprovalBy": {
        "key": "2",
        "id": "sdye",
        "name": "Sara Dye",
        "href": "/objects/company-config/employee/2"
      },
      "issuedBy": {
        "key": "25",
        "id": "amarquess",
        "name": "Adam Marquess",
        "href": "/objects/company-config/employee/25"
      },
      "issuedOnDate": "2023-05-30",
      "approvedBy": {
        "key": "1",
        "id": "treser",
        "name": "Tim Reser",
        "href": "/objects/company-config/employee/1"
      },
      "approvedOnDate": "2023-10-02",
      "signedBy": {
        "key": "32",
        "id": "broberts",
        "name": "Bob Roberts",
        "href": "/objects/company-config/employee/32"
      },
      "signedOnDate": "2023-05-31",
      "source": "Internal",
      "sourceReferenceNumber": "REF-INT-01"
    },
    "externalReference": {
      "referenceNumber": "A23",
      "verbalApprovalBy": {
        "key": "6",
        "id": "Johnson",
        "href": "/objects/company-config/contact/6"
      },
      "approvedBy": {
        "key": "51",
        "id": "Jagadish",
        "href": "/objects/company-config/contact/51"
      },
      "approvedOnDate": "2023-11-03",
      "signedBy": {
        "key": "200",
        "id": "Modulus Industries",
        "href": "/objects/company-config/contact/200"
      },
      "signedOnDate": "2023-12-01"
    },
    "performanceBond": {
      "isRequired": false,
      "isReceived": false,
      "amount": "1000.00",
      "vendor": {
        "key": "1",
        "id": "VND-IND-0081",
        "name": "Vendor-India-0081",
        "href": "/objects/accounts-payable/vendor/1"
      }
    },
    "paymentBond": {
      "isRequired": false,
      "isReceived": false,
      "amount": "1000.00",
      "vendor": {
        "key": "1",
        "id": "VND-IND-0081",
        "name": "Vendor-India-0081",
        "href": "/objects/accounts-payable/vendor/1"
      }
    },
    "revision": {
      "isDocumentChanged": false,
      "revisedTotal": "1000.00",
      "revisedSubTotal": "1000.00",
      "revisedTotalInTxnCurrency": "1000.00",
      "revisedSubTotalInTxnCurrency": "1000.00",
      "changeLogNumber": 1
    },
    "relatedDocumentNumber": "Sales Invoice-Sal#0140#inv",
    "postedChangesTotal": "1000.00",
    "projectContractBilling": {
      "externalReferenceNumber": "HGS-1024",
      "description": "Construction of clubhouse and offices",
      "contractDate": "2024-05-08",
      "billingThroughDate": "2024-05-08",
      "billingApplicationNumber": "IA-89115"
    },
    "billingSummary": {
      "originalContractAmount": "1000.00",
      "netChangesAmount": "1000.00",
      "revisedContractAmount": "1000.00",
      "balanceToFinishAmount": "1000.00",
      "lessPriorApplicationAmount": "1000.00",
      "currentDueAmount": "1000.00",
      "retainage": {
        "previousBalanceAmount": "1000.00",
        "balanceAmount": "1000.00",
        "billedAmount": "1000.00",
        "heldAmount": "1000.00",
        "completedAmount": "1000.00",
        "storedMaterialsAmount": "1000.00"
      },
      "billingTotals": {
        "completedToDateAmount": "1000.00",
        "storedMaterialsAmount": "1000.00",
        "heldAmount": "1000.00",
        "heldToDateAmount": "1000.00",
        "retainageOnThisInvoiceAmount": "1000.00",
        "earnedLessRetainageAmount": "1000.00",
        "lessRetainageHeldAmount": "1000.00",
        "netChangesAmount": "1000.00",
        "netChangesAdditionAmount": "1000.00",
        "netChangesDeductionAmount": "1000.00"
      },
      "totalChangesApprovedPriorMonth": {
        "additionsAmount": "1000.00",
        "deductionsAmount": "1000.00"
      },
      "totalChangesApprovedThisMonth": {
        "additionsAmount": "1000.00",
        "deductionsAmount": "1000.00"
      }
    },
    "architect": {
      "key": "1",
      "id": "Eberhardt",
      "href": "/objects/company-config/contact/12"
    },
    "projectContract": {
      "key": "1",
      "id": "BTI-01",
      "name": "Berkeley Technology Inc - Contract 01",
      "href": "/objects/construction/project-contract/1"
    },
    "contacts": {
      "primary": {
        "key": "13",
        "id": "contact"
      },
      "shipTo": {
        "key": "33",
        "id": "contact"
      },
      "billTo": {
        "key": "44",
        "id": "contact"
      }
    },
    "shippingMethod": {
      "key": "77",
      "id": "Air",
      "href": "/objects/accounts-receivable/shipping-method/77"
    },
    "printedByUser": {
      "key": "21",
      "id": "John",
      "href": "/objects/company-config/user/21"
    },
    "txnDefinition": {
      "key": "11",
      "id": "Sales Invoice",
      "href": "/objects/order-entry/txn-definition/11"
    },
    "sourceDocument": {
      "key": "44",
      "id": "Sales Order-SO0022",
      "documentType": "Sales Order",
      "href": "/objects/order-entry/document::Sales%20Order/44"
    },
    "customer": {
      "key": "1",
      "id": "1",
      "name": "Power Aerospace Materials",
      "href": "/objects/accounts-receivable/customer/15"
    },
    "contract": {
      "key": "46",
      "id": "CNRT1001",
      "href": "/objects/contracts/contract/46"
    },
    "project": {
      "key": "2",
      "id": "NET-XML30-2",
      "name": "Talcomp training",
      "href": "/objects/projects/project/2"
    },
    "paymentTerm": {
      "href": "/objects/term/75",
      "key": "75",
      "id": "10 Days"
    },
    "audit": {
      "createdDateTime": "2014-01-08T11:28:12Z",
      "modifiedDateTime": "2022-04-20T16:20:00Z",
      "createdBy": "1",
      "modifiedBy": "95"
    },
    "invoiceType": "invoice",
    "invoiceMode": "b1",
    "eInvoiceStatus": "paymentReceived",
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "entity": {
      "key": "46",
      "id": "CORP",
      "name": "Corp",
      "href": "/objects/company-config/entity/46"
    },
    "status": "active",
    "taxSolution": {
      "key": "44",
      "id": "Avalara",
      "href": "/objects/tax/tax-solution/44",
      "taxCalculationMethod": "noTax",
      "showMultilineTax": true
    },
    "projectContractBillingInvoiceSummary": {
      "originalContractAmount": "1000.0000000000",
      "netApprovedChangesAmount": "1000.0000000000",
      "revisedContractAmount": "1000.0000000000",
      "completedFromPriorApplicationAmount": "1000.0000000000",
      "completedToDateAmount": "1000.0000000000",
      "lessPreviousBillingAmount": "1000.0000000000",
      "currentDueAmount": "1000.0000000000",
      "balanceToFinishAmount": "1000.0000000000",
      "taxAmount": "1000.0000000000",
      "chargeAmount": "1000.0000000000",
      "discountAmount": "1000.0000000000",
      "changesApprovedPriorMonth": {
        "additionsAmount": "1000.0000000000",
        "deductionsAmount": "1000.0000000000"
      },
      "changesApprovedThisMonth": {
        "additionsAmount": "1000.0000000000",
        "deductionsAmount": "1000.0000000000"
      },
      "retainage": {
        "amountRetained": "1000.0000000000",
        "billedAmount": "1000.0000000000",
        "netChangeHeldAmount": "1000.0000000000",
        "heldToDateAmount": "1000.0000000000",
        "billedToDateAmount": "1000.0000000000",
        "balanceToDateAmount": "1000.0000000000",
        "previousBalanceAmount": "1000.0000000000",
        "totalEarnedLessAmount": "1000.0000000000"
      },
      "accountsReceivableInvoiceNumber": "INV1",
      "orderEntryDocumentId": "SO-AIA-Invoice01-Ord#0011#doc",
      "projectId": "DIM - HCS",
      "projectName": "Dimensions - Hands Computer Systems"
    },
    "lines": [
      {
        "key": "44",
        "id": "44",
        "href": "/objects/order-entry/document-line::Sales%20Invoice/44",
        "documentType": "Sales Invoice",
        "lineNumber": 1,
        "item": {
          "key": "10",
          "id": "MX001",
          "href": "/objects/inventory-control/item/10"
        },
        "itemAlias": {
          "key": "10",
          "id": "IXN",
          "href": "/objects/accounts-receivable/customer-item-cross-reference/10"
        },
        "lineDescription": "MX001",
        "memo": "Payment ACH",
        "priceCalculationMemo": "Fair value price list",
        "unit": "Each",
        "quantity": "40.10",
        "unitQuantity": "10.10",
        "unitPrice": "10.50",
        "price": "33.66",
        "quantityConverted": "5.10",
        "retailPrice": "10.44",
        "audit": {
          "createdDateTime": "2022-04-20T16:20:00Z",
          "modifiedDateTime": "2022-04-20T16:20:00Z",
          "createdBy": "1",
          "modifiedBy": "95"
        },
        "status": "active",
        "costMethod": "average",
        "discountPercent": "10.50",
        "multiplier": 1,
        "sourceDocument": {
          "key": "77",
          "id": "Sales Order-SO0022",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document::Sales%20Order/77"
        },
        "sourceDocumentLine": {
          "key": "2234",
          "id": "2234",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document-line::Sales%20Order/2234"
        },
        "isPriceProrated": true,
        "discountMemo": "Festival discount",
        "baseCurrency": "USD",
        "txnCurrency": "CAD",
        "priceInTxnCurrency": "10.00",
        "isBillable": true,
        "isBilled": true,
        "taxRate": "10.05",
        "taxInBaseCurrency": "10.50",
        "taxInTxnCurrency": "40.50",
        "discount": "10.25",
        "enableTax": false,
        "quantityRemaining": "10.10",
        "conversionType": "quantity",
        "dimensions": {
          "location": {
            "key": "22",
            "id": "LOC-22",
            "name": "California",
            "href": "/objects/company-config/location/22"
          },
          "department": {
            "key": "9",
            "id": "Sales",
            "name": "Sales and Marketing",
            "href": "/objects/company-config/department/9"
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
            "id": "TSK01",
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
            "name": "Laptop 1"
          },
          "contract": {
            "id": "CON-0045-1",
            "key": "12",
            "name": "ACME Widgets - Service",
            "href": "/objects/contracts/contract/12"
          }
        },
        "itemRenewalTemplate": {
          "key": "45",
          "id": "Sales Renewal Template",
          "href": "/objects/order-entry/renewal-template/45"
        },
        "revenueRecognitionStartDate": "2024-04-04",
        "revenueRecognitionEndDate": "2024-04-04",
        "requestedShippingDate": "2024-04-04",
        "shipByDate": "2024-04-15",
        "pickTicketPrintedDate": "2024-04-04",
        "cancelAfterDate": "2024-04-15",
        "doNotShipBeforeDate": "2024-04-03",
        "doNotShipAfterDate": "2024-04-15",
        "shippedDate": "2024-04-04",
        "servicePeriodStartDate": "2024-04-01",
        "servicePeriodEndDate": "2024-04-30",
        "allowDropShip": true,
        "allowBuyToOrder": true,
        "revision": {
          "unitQuantity": "10",
          "quantity": "10",
          "unitValue": "8.00",
          "value": "8.00",
          "valueInTxnCurrency": "10.00",
          "price": "10.00",
          "unitPrice": "10.00",
          "priceInTxnCurrency": "10.00"
        },
        "draft": {
          "unitQuantity": "10",
          "quantity": "10",
          "price": "10.00",
          "basePrice": "10.00"
        },
        "posted": {
          "quantity": "10.00",
          "price": "10.00",
          "basePrice": "10.00"
        },
        "addedByChangeDocument": false,
        "projectContractBilling": {
          "externalReferenceNumber": "HGS-1024",
          "description": "Construction of clubhouse and offices",
          "billingType": "timeAndMaterial",
          "contractLineValue": "1000.00",
          "priorApplicationAmount": "1000.00",
          "completedThisPeriodAmount": "1000.00",
          "storedMaterialsAmount": "1000.00",
          "completedToDateAmount": "1000.00",
          "completedToDatePercent": "10.00",
          "balanceRemaining": "1000.00",
          "totalConvertedAmount": "1000.00",
          "totalRemainingAmount": "1000.00",
          "isSummarized": false
        },
        "retainage": {
          "percentage": "10.00",
          "baseAmountRetained": "10.00",
          "txnAmountRetained": "10.00",
          "isReleaseLine": true,
          "previousBalanceAmount": "1000.00",
          "billAmount": "1000.00",
          "balanceAmount": "1000.00",
          "extendedPriceNetAmount": "1000.00",
          "extendedBasePriceNetAmount": "1000.00"
        },
        "reverseConversion": {
          "isReverseConversion": true,
          "price": "100.00",
          "quantity": "100",
          "standardPrice": "100.00",
          "standardQuantity": "100"
        },
        "relatedDocument": {
          "id": "5151",
          "key": "5151",
          "documentNumber": "Sales Order-SD-SO0550",
          "href": "/objects/order-entry/document/5151"
        },
        "relatedDocumentLine": {
          "key": "13965",
          "id": "1--0001",
          "href": "/objects/order-entry/document-line/13965"
        },
        "projectContract": {
          "key": "1",
          "id": "BTI-01",
          "name": "Berkeley Technology Inc - Contract 01",
          "href": "/objects/construction/project-contract/1"
        },
        "projectContractLine": {
          "key": "4",
          "id": "Project-Contract-Line-04",
          "name": "Project contract line 04",
          "href": "/objects/construction/project-contract-line/4"
        },
        "taxSchedule": {
          "key": "1",
          "id": "Sale Goods Standard",
          "href": "/objects/tax/order-entry-tax-schedule/1"
        },
        "buyToOrderContact": {
          "key": "13",
          "id": "contact"
        },
        "trackingDetail": [
          {
            "key": "55",
            "id": "55",
            "href": "/objects/order-entry/document-line-detail/55",
            "quantity": "10",
            "serialNumber": "S1001",
            "lotNumber": "L1001",
            "expirationDate": "2024-04-04",
            "aisle": {
              "href": "/objects/inventory-control/aisle/10",
              "key": "10",
              "id": "AISLE1"
            },
            "bin": {
              "href": "/objects/inventory-control/bin/20",
              "key": "20",
              "id": "BIN1"
            },
            "row": {
              "href": "/objects/inventory-control/row/15",
              "key": "15",
              "id": "ROW1"
            },
            "item": {
              "key": "10",
              "id": "Battery",
              "href": "/objects/inventory-control/item/10"
            },
            "audit": {
              "createdDateTime": "2022-04-20T16:20:00Z",
              "modifiedDateTime": "2022-04-20T16:20:00Z",
              "createdBy": "1",
              "modifiedBy": "95"
            },
            "orderEntryDocumentLine": {
              "key": "23",
              "id": "23",
              "documentType": "Sales Order",
              "href": "/objects/order-entry-document-line::Sales%20Order/23"
            }
          }
        ],
        "lineSubtotals": [],
        "timesheetNotes": "Worked extra hours on project",
        "timeType": {
          "id": "Design",
          "key": 11,
          "href": "/objects/time/time-type/11"
        },
        "employeeExpenseType": {
          "id": "Meals",
          "key": 4,
          "href": "/objects/expenses/employee-expense-type/4"
        },
        "documentHeader": {
          "key": "55",
          "id": "Sales Invoice-SO0066",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry-document::Sales%20Invoice/55"
        }
      }
    ],
    "subtotals": [
      {
        "key": "12",
        "id": "12",
        "href": "/objects/order-entry/document-subtotal/12",
        "description": "Tax",
        "percentValue": "10.50",
        "absoluteValue": "40.50",
        "txnAbsoluteValue": "44.78",
        "total": "500.10",
        "txnTotal": "400.10",
        "documentLine": {
          "key": "10",
          "documentType": "Sales Order",
          "id": "10",
          "href": "/objects/order-entry-document-line::Sales%20Order/10"
        },
        "audit": {
          "createdDateTime": "2022-04-20T16:20:00Z",
          "modifiedDateTime": "2022-04-20T16:20:00Z",
          "createdBy": "1",
          "modifiedBy": "95"
        },
        "dimensions": {
          "location": {
            "key": "22",
            "id": "LOC-22",
            "name": "California",
            "href": "/objects/company-config/location/22"
          },
          "department": {
            "key": "9",
            "id": "Accounting",
            "name": "Sales and Marketing",
            "href": "/objects/company-config/department/9"
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
            "name": "Laptop 1"
          },
          "contract": {
            "id": "CON-0045-1",
            "key": "12",
            "name": "ACME Widgets - Service",
            "href": "/objects/contracts/contract/12"
          }
        },
        "documentHeader": {
          "key": "23",
          "id": "23",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document::Sales%20Order/23"
        }
      }
    ],
    "history": [
      {
        "key": "11",
        "id": "11",
        "href": "/objects/order-entry/document-history/11",
        "convertedFrom": {
          "key": "22",
          "id": "Sales Order-ORINV#0182#doc",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document::Sales%20Order/22"
        },
        "convertedTo": {
          "key": "14",
          "id": "Sales Invoice-SUBINV#0182#doc",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry-document::Sales%20Invoice/14"
        },
        "orderEntryDocument": {
          "key": "23",
          "id": "Sales Order-ORINV#0182#doc",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document::Sales%20Order/22"
        }
      }
    ]
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## GET /objects/order-entry/document::{documentName}
_List named Order Entry documents_

**Response 200 — List named 'Sales Invoice' documents:**
```json
{
  "ia::result": [
    {
      "key": "171",
      "id": "Sales Invoice-SUBINV#0147#doc",
      "href": "/objects/order-entry/document::Sales%20Invoice/171"
    },
    {
      "key": "172",
      "id": "Sales Invoice-SUBINV#0148#doc",
      "href": "/objects/order-entry/document::Sales%20Invoice/172"
    },
    {
      "key": "155",
      "id": "Sales Invoice-SUBINV#0144#doc",
      "href": "/objects/order-entry/document::Sales%20Invoice/155"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/order-entry/document::{documentName}
_Create an Order Entry document_

**Request example — Create a document:**
```json
{
  "customer": {
    "id": "1"
  },
  "state": "submitted",
  "txnDate": "2024-11-01",
  "dueDate": "2024-12-12",
  "txnCurrency": "USD",
  "baseCurrency": "USD",
  "sourceModule": "orderEntry",
  "lines": [
    {
      "dimensions": {
        "item": {
          "id": "1"
        },
        "warehouse": {
          "id": "1"
        },
        "location": {
          "id": "1"
        }
      },
      "unit": "Each",
      "unitQuantity": "1",
      "unitPrice": "650"
    }
  ]
}
```
**Request example — Create a document for Construction:**
```json
{
  "customer": {
    "id": "BTI"
  },
  "project": {
    "id": "DIM - BTI--Dimensions - Berkeley Technology Inc"
  },
  "state": "pending",
  "txnDate": "2024-05-21",
  "dueDate": "2024-12-12",
  "txnCurrency": "USD",
  "baseCurrency": "USD",
  "notes": "additional info order 01",
  "scope": "Subcontractor agrees to provide labor and materials for utility trenching for Five Oaks Storage facilities according to contract",
  "inclusions": "Includes drive through building",
  "exclusions": "Excludes additional purchase",
  "terms": "Follow all safety rules and security procedure that are in force and applicable during execution of work",
  "schedule": {
    "scheduledStartDate": "2024-05-01",
    "actualStartDate": "2024-05-03",
    "scheduledCompletionDate": "2024-05-31",
    "revisedCompletionDate": "2024-06-01",
    "substantialCompletionDate": "2024-05-20",
    "actualCompletionDate": "2024-05-30",
    "noticeToProceedDate": "2024-05-25",
    "responseDueDate": "2024-05-30",
    "executedOnDate": "2024-05-05",
    "scheduleImpactNotes": "NA"
  },
  "internalReference": {
    "referenceNumber": "INT-01",
    "initiatedBy": {
      "id": "10001"
    },
    "verbalApprovalBy": {
      "id": "10001"
    },
    "issuedBy": {
      "id": "10001"
    },
    "issuedOnDate": "2024-05-24",
    "approvedBy": {
      "id": "10001"
    },
    "approvedOnDate": "2024-05-24",
    "signedBy": {
      "id": "10001"
    },
    "signedOnDate": "2024-05-30",
    "source": "BTI-089",
    "sourceReferenceNumber": "88009890"
  },
  "externalReference": {
    "referenceNumber": "EXT-01",
    "verbalApprovalBy": {
      "id": "Berkeley Technology Inc"
    },
    "approvedBy": {
      "id": "Berkeley Technology Inc"
    },
    "approvedOnDate": "2024-05-24",
    "signedBy": {
      "id": "Berkeley Technology Inc"
    },
    "signedOnDate": "2024-05-30"
  },
  "performanceBond": {
    "isRequired": true,
    "isReceived": true,
    "amount": "4500.00",
    "vendor": {
      "id": "CITI"
    }
  },
  "paymentBond": {
    "isRequired": true,
    "isReceived": true,
    "amount": "5000.00",
    "vendor": {
      "id": "CITI"
    }
  },
  "lines": [
    {
      "dimensions": {
        "item": {
          "id": "0001--Design"
        },
        "warehouse": {
          "id": "1"
        },
        "location": {
          "id": "1"
        }
      },
      "unit": "Each",
      "unitQuantity": "1",
      "unitPrice": "650"
    }
  ]
}
```
**Request example — Create a project contract billing document:**
```json
{
  "customer": {
    "id": "HC"
  },
  "project": {
    "id": "DIM - BTI--Dimensions - Berkeley Technology Inc"
  },
  "state": "pending",
  "txnDate": "2024-05-21",
  "txnCurrency": "USD",
  "baseCurrency": "USD",
  "paymentTerm": {
    "id": "N15"
  },
  "dueDate": "2024-06-06",
  "retainagePercent": 15,
  "projectContract": {
    "id": "04 Sep A"
  },
  "projectContractBilling": {
    "externalReferenceNumber": "EXT_01",
    "description": "Contract 04 Sep A",
    "contractDate": "2024-05-30",
    "billingThroughDate": "2024-06-30",
    "billingApplicationNumber": "A1002"
  },
  "architect": {
    "id": "Berkeley Technology Inc"
  },
  "lines": [
    {
      "dimensions": {
        "item": {
          "id": "Design--Design"
        },
        "location": {
          "id": "1"
        },
        "warehouse": {
          "id": "1"
        }
      },
      "conversionType": "price",
      "unit": "Seconds",
      "unitQuantity": "1",
      "unitPrice": "200",
      "projectContract": {
        "id": "04 Sep A"
      },
      "projectContractLine": {
        "id": "L1 PB"
      },
      "projectContractBilling": {
        "completedThisPeriodAmount": "100.0000000000",
        "storedMaterialsAmount": "100.0000000000"
      }
    }
  ]
}
```
**Response 201 — Reference to new document:**
```json
{
  "ia::result": {
    "key": "13977",
    "id": "Sales Invoice-SUBINV#0193#doc",
    "documentType": "Sales Invoice",
    "href": "/objects/order-entry/document::Sales%20Invoice/469"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 201 — Reference to new Construction document:**
```json
{
  "ia::result": {
    "key": "5150",
    "id": "SO-Order02-SO0549",
    "href": "/objects/order-entry/document::SO-Order02/5150"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 201 — Reference to new project contract billing document:**
```json
{
  "ia::result": {
    "key": "5156",
    "id": "SO-AIA-Invoice01-Ord#0191#doc",
    "href": "/objects/order-entry/document::SO-AIA-Invoice01/5156"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/document::{documentName}/{key}
_Get a named Order Entry document_

**Response 200 — Get a named document:**
```json
{
  "ia::result": {
    "key": "453",
    "documentNumber": "SUBINV#0182#doc",
    "id": "Sales Invoice-SUBINV#0182#doc",
    "sourceDocument": {
      "id": "Sales Order-SO0026",
      "key": "451",
      "documentType": "Sales Order",
      "href": "/objects/order-entry/document::Sales Order/451"
    },
    "state": "pending",
    "txnDate": "2024-03-29",
    "audit": {
      "createdDateTime": "2024-11-10T18:36:30Z",
      "createdBy": "1",
      "modifiedBy": "1",
      "modifiedDateTime": "2024-11-10T18:36:32Z"
    },
    "invoiceType": "invoice",
    "invoiceMode": "b1",
    "eInvoiceStatus": "paymentReceived",
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "entity": {
      "key": "46",
      "id": "CORP",
      "name": "Corp",
      "href": "/objects/company-config/entity/46"
    },
    "status": "active",
    "dueDate": "2024-10-28",
    "documentType": "Sales Invoice",
    "txnDefinition": {
      "id": "Sales Invoice",
      "key": "188",
      "href": "/objects/order-entry-txn-definition::Sales%20Invoice/188"
    },
    "contacts": {
      "primary": {
        "key": "304",
        "id": "Power Aerospace Materials(C1)"
      },
      "shipTo": {
        "key": "304",
        "id": "Power Aerospace Materials(C1)"
      },
      "billTo": {
        "key": "304",
        "id": "Power Aerospace Materials(C1)"
      }
    },
    "isPrinted": false,
    "isBackordered": false,
    "subtotal": "750.66",
    "total": "742.54",
    "txnCurrency": "USD",
    "exchangeRate": {
      "date": "2024-03-29",
      "rate": "1"
    },
    "subtotalInTxnCurrency": "750.55",
    "totalInTxnCurrency": "742.5",
    "baseCurrency": "USD",
    "isSystemGeneratedDocument": false,
    "postingDate": "2024-03-29",
    "paymentStatus": "open",
    "customer": {
      "key": "1",
      "id": "1",
      "name": "Power Aerospace Materials",
      "href": "/objects/accounts-receivable/customer/1"
    },
    "lines": [
      {
        "id": "790",
        "key": "790",
        "documentHeader": {
          "key": "453",
          "id": "Sales Invoice-SUBINV#0182#doc",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document::Sales%20Invoice/453"
        },
        "documentType": "Sales Invoice",
        "lineNumber": 0,
        "dimensions": {
          "item": {
            "key": "1",
            "id": "1--PC Computer",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/1"
          },
          "warehouse": {
            "id": "1",
            "key": "1",
            "href": "/objects/inventory-control/warehouse/1"
          },
          "location": {
            "id": "1",
            "key": "1",
            "href": "/objects/company-config/location/1"
          },
          "customer": {
            "key": "1",
            "id": "1--Power Aerospace Materials",
            "name": "Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          }
        },
        "item": {
          "key": "1",
          "id": "1--PC Computer",
          "href": "/objects/inventory-control/item/1"
        },
        "lineDescription": "PC Computer",
        "memo": "PC Computer",
        "unit": "Each",
        "quantity": "1",
        "quantityConverted": "0",
        "retailPrice": "750",
        "price": "742.5",
        "audit": {
          "createdDateTime": "2024-03-29T00:00:00Z",
          "modifiedDateTime": "2024-11-10T18:36:30Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "status": "active",
        "costMethod": "standard",
        "unitQuantity": "1",
        "multiplier": 1,
        "unitPrice": "750",
        "txnCurrency": "USD",
        "baseCurrency": "USD",
        "priceInTxnCurrency": "750",
        "conversionType": "quantity",
        "servicePeriodStartDate": null,
        "servicePeriodEndDate": null,
        "allowDropShip": false,
        "allowBuyToOrder": false,
        "quantityRemaining": "1",
        "trackingDetail": [],
        "lineSubtotals": [],
        "timesheetNotes": "Worked extra hours on project",
        "timeType": {
          "id": "Design",
          "key": 11,
          "href": "/objects/time/time-type/11"
        },
        "employeeExpenseType": {
          "id": "Meals",
          "key": 4,
          "href": "/objects/expenses/employee-expense-type/4"
        },
        "href": "/objects/order-entry/document-line::Sales%20Invoice/790"
      }
    ],
    "history": [
      {
        "id": "382",
        "key": "382",
        "convertedTo": {
          "key": "453",
          "id": "Sales Invoice-SUBINV#0182#doc",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document::Sales%20Invoice/453"
        },
        "convertedFrom": {
          "id": "Sales Order-SO0026",
          "key": "451",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document::Sales%20Order/451"
        },
        "orderEntryDocument": {
          "key": "451",
          "id": "Sales Order-SO0026",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document::Sales%20Order/451"
        },
        "href": "/objects/order-entry/document-history/382"
      },
      {
        "id": "380",
        "key": "380",
        "convertedTo": {
          "key": "451",
          "id": "Sales Order-SO0026",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document::Sales%20Order/451"
        },
        "orderEntryDocument": {
          "key": "451",
          "id": "Sales Order-SO0026",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document::Sales%20Order/451"
        },
        "href": "/objects/order-entry/document-history/380"
      }
    ],
    "subtotals": [
      {
        "id": "1204",
        "key": "1204",
        "description": "Sales Discount",
        "absoluteValue": "0",
        "total": "0",
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "href": "/objects/company-config/location/1"
          },
          "customer": {
            "key": "1",
            "id": "1--Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          }
        },
        "txnAbsoluteValue": "0",
        "txnTotal": "0",
        "documentLine": {
          "id": "790",
          "key": "790",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document-line::Sales%20Invoice/790"
        },
        "audit": {
          "createdDateTime": "2024-11-10T18:36:31Z",
          "modifiedDateTime": "2024-11-10T18:36:31Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/order-entry/document-subtotal/1204"
      },
      {
        "id": "1205",
        "key": "1205",
        "description": "Discounted Totals",
        "absoluteValue": "7.5",
        "percentValue": "1",
        "total": "7.5",
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "href": "/objects/company-config/location/1"
          },
          "customer": {
            "key": "1",
            "id": "1--Power Aerospace Materials",
            "href": "/objects/accounts-receivable/customer/1"
          }
        },
        "txnAbsoluteValue": "7.5",
        "txnTotal": "7.5",
        "documentLine": {
          "id": "790",
          "key": "790",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document-line::Sales%20Invoice/790"
        },
        "audit": {
          "createdDateTime": "2024-11-10T18:36:31Z",
          "modifiedDateTime": "2024-11-10T18:36:31Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/order-entry/document-subtotal/1205"
      },
      {
        "id": "1206",
        "key": "1206",
        "description": "Sales Tax",
        "absoluteValue": "0",
        "total": "0",
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "href": "/objects/company-config/location/1"
          },
          "customer": {
            "key": "1",
            "id": "1",
            "href": "/objects/accounts-receivable/customer/1"
          }
        },
        "txnAbsoluteValue": "0",
        "txnTotal": "0",
        "documentLine": {
          "id": "790",
          "key": "790",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/document-line::Sales%20Invoice/790"
        },
        "audit": {
          "createdDateTime": "2024-11-10T18:36:31Z",
          "modifiedDateTime": "2024-11-10T18:36:31Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/order-entry/document-subtotal/1206"
      }
    ],
    "href": "/objects/order-entry/document::Sales%20Invoice/453"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a named document - Construction subscription:**
```json
{
  "ia::result": {
    "key": "55",
    "id": "Sales Invoice-SI-O122",
    "href": "/objects/order-entry/document::Sales%20Invoice/55",
    "documentNumber": "SI-O122",
    "documentType": "Sales Invoice",
    "state": "draft",
    "isPrinted": true,
    "isBackordered": false,
    "subtotal": "50.10",
    "subtotalInTxnCurrency": "51.10",
    "total": "100.10",
    "totalInTxnCurrency": "100.11",
    "baseCurrency": "USD",
    "txnCurrency": "USD",
    "exchangeRate": {
      "date": "2023-01-23",
      "rate": "1.0789",
      "typeId": "1",
      "typeName": "Intacct Daily Rate"
    },
    "txnDate": "2024-04-04",
    "dueDate": "2024-04-04",
    "isSystemGeneratedDocument": true,
    "postingDate": "2024-04-04",
    "referenceNumber": "SALES-100",
    "notes": "Fast order",
    "memo": "Lowry solutions",
    "contractId": "CN100123",
    "contractDescription": "Sales & Service",
    "paymentStatus": "paid",
    "invoiceDate": "2024-04-04",
    "customerPONumber": "ABOTT-1001",
    "trackingNumber": "TK-1002",
    "shipByDate": "2024-04-15",
    "shippedDate": "2024-04-04",
    "serviceDeliveryDate": "2024-04-04",
    "cancelAfterDate": "2024-04-15",
    "doNotShipBeforeDate": "2024-04-03",
    "doNotShipAfterDate": "2024-04-15",
    "requestedShippingDate": "2024-04-04",
    "retainagePercent": 10,
    "scope": "Subcontractor agrees to provide labor and materials for utility trenching for Five Oaks Storage facilities according to contract.",
    "inclusions": "Includes drive through building",
    "exclusions": "Excludes additional purchase",
    "terms": "Follow all safety rules and security procedure that are in force and applicable during execution of work.",
    "schedule": {
      "scheduledStartDate": "2024-05-07",
      "scheduledCompletionDate": "2024-10-07",
      "actualStartDate": "2024-05-07",
      "actualCompletionDate": "2024-10-10",
      "revisedCompletionDate": "2024-11-01",
      "substantialCompletionDate": "2024-10-10",
      "noticeToProceedDate": "2024-10-10",
      "responseDueDate": "2024-10-10",
      "executedOnDate": "2024-10-10",
      "scheduleImpactNotes": "None"
    },
    "internalReference": {
      "referenceNumber": "INT-01",
      "initiatedBy": {
        "key": "2",
        "id": "dhatchet",
        "name": "David Hatcher",
        "href": "/objects/company-config/employee/2"
      },
      "verbalApprovalBy": {
        "key": "2",
        "id": "sdye",
        "name": "Sara Dye",
        "href": "/objects/company-config/employee/2"
      },
      "issuedBy": {
        "key": "25",
        "id": "amarquess",
        "name": "Adam Marquess",
        "href": "/objects/company-config/employee/25"
      },
      "issuedOnDate": "2023-05-30",
      "approvedBy": {
        "key": "1",
        "id": "treser",
        "name": "Tim Reser",
        "href": "/objects/company-config/employee/1"
      },
      "approvedOnDate": "2023-10-02",
      "signedBy": {
        "key": "32",
        "id": "broberts",
        "name": "Bob Roberts",
        "href": "/objects/company-config/employee/32"
      },
      "signedOnDate": "2023-05-31",
      "source": "Internal",
      "sourceReferenceNumber": "REF-INT-01"
    },
    "externalReference": {
      "referenceNumber": "A23",
      "verbalApprovalBy": {
        "key": "6",
        "id": "Johnson",
        "href": "/objects/company-config/contact/6"
      },
      "approvedBy": {
        "key": "51",
        "id": "Jagadish",
        "href": "/objects/company-config/contact/51"
      },
      "approvedOnDate": "2023-11-03",
      "signedBy": {
        "key": "200",
        "id": "Modulus Industries",
        "href": "/objects/company-config/contact/200"
      },
      "signedOnDate": "2023-12-01"
    },
    "performanceBond": {
      "isRequired": false,
      "isReceived": false,
      "amount": "1000.00",
      "vendor": {
        "key": "1",
        "id": "VND-IND-0081",
        "name": "Vendor-India-0081",
        "href": "/objects/accounts-payable/vendor/1"
      }
    },
    "paymentBond": {
      "isRequired": false,
      "isReceived": false,
      "amount": "1000.00",
      "vendor": {
        "key": "1",
        "id": "VND-IND-0081",
        "name": "Vendor-India-0081",
        "href": "/objects/accounts-payable/vendor/1"
      }
    },
    "revision": {
      "isDocumentChanged": false,
      "revisedTotal": "1000.00",
      "revisedSubTotal": "1000.00",
      "revisedTotalInTxnCurrency": "1000.00",
      "revisedSubTotalInTxnCurrency": "1000.00",
      "changeLogNumber": 1
    },
    "relatedDocumentNumber": "Sales Invoice-Sal#0140#inv",
    "postedChangesTotal": "1000.00",
    "projectContractBilling": {
      "externalReferenceNumber": "HGS-1024",
      "description": "Construction of clubhouse and offices",
      "contractDate": "2024-05-08",
      "billingThroughDate": "2024-05-08",
      "billingApplicationNumber": "IA-89115"
    },
    "billingSummary": {
      "originalContractAmount": "1000.00",
      "netChangesAmount": "1000.00",
      "revisedContractAmount": "1000.00",
      "balanceToFinishAmount": "1000.00",
      "lessPriorApplicationAmount": "1000.00",
      "currentDueAmount": "1000.00",
      "retainage": {
        "previousBalanceAmount": "1000.00",
        "balanceAmount": "1000.00",
        "billedAmount": "1000.00",
        "heldAmount": "1000.00",
        "completedAmount": "1000.00",
        "storedMaterialsAmount": "1000.00"
      },
      "billingTotals": {
        "completedToDateAmount": "1000.00",
        "storedMaterialsAmount": "1000.00",
        "heldAmount": "1000.00",
        "heldToDateAmount": "1000.00",
        "retainageOnThisInvoiceAmount": "1000.00",
        "earnedLessRetainageAmount": "1000.00",
        "lessRetainageHeldAmount": "1000.00",
        "netChangesAmount": "1000.00",
        "netChangesAdditionAmount": "1000.00",
        "netChangesDeductionAmount": "1000.00"
      },
      "totalChangesApprovedPriorMonth": {
        "additionsAmount": "1000.00",
        "deductionsAmount": "1000.00"
      },
      "totalChangesApprovedThisMonth": {
        "additionsAmount": "1000.00",
        "deductionsAmount": "1000.00"
      }
    },
    "architect": {
      "key": "1",
      "id": "Eberhardt",
      "href": "/objects/company-config/contact/12"
    },
    "projectContract": {
      "key": "1",
      "id": "BTI-01",
      "name": "Berkeley Technology Inc - Contract 01",
      "href": "/objects/construction/project-contract/1"
    },
    "contacts": {
      "primary": {
        "key": "13",
        "id": "contact"
      },
      "shipTo": {
        "key": "33",
        "id": "contact"
      },
      "billTo": {
        "key": "44",
        "id": "contact"
      }
    },
    "shippingMethod": {
      "key": "77",
      "id": "Air",
      "href": "/objects/accounts-receivable/shipping-method/77"
    },
    "printedByUser": {
      "key": "21",
      "id": "John",
      "href": "/objects/company-config/user/21"
    },
    "txnDefinition": {
      "key": "11",
      "id": "Sales Invoice",
      "href": "/objects/order-entry/txn-definition/11"
    },
    "sourceDocument": {
      "key": "44",
      "id": "Sales Order-SO0022",
      "documentType": "Sales Order",
      "href": "/objects/order-entry/document::Sales%20Order/44"
    },
    "customer": {
      "key": "1",
      "id": "1",
      "name": "Power Aerospace Materials",
      "href": "/objects/accounts-receivable/customer/15"
    },
    "project": {
      "key": "2",
      "id": "NET-XML30-2",
      "name": "Talcomp training",
      "href": "/objects/projects/project/2"
    },
    "contract": {
      "key": "46",
      "id": "CNRT1001",
      "href": "/objects/contracts/contract/46"
    },
    "paymentTerm": {
      "href": "/objects/term/75",
      "key": "75",
      "id": "10 Days"
    },
    "audit": {
      "createdDateTime": "2014-01-08T11:28:12Z",
      "modifiedDateTime": "2022-04-20T16:20:00Z",
      "createdBy": "1",
      "modifiedBy": "95"
    },
    "invoiceType": "invoice",
    "invoiceMode": "b1",
    "eInvoiceStatus": "paymentReceived",
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "entity": {
      "key": "46",
      "id": "CORP",
      "name": "Corp",
      "href": "/objects/company-config/entity/46"
    },
    "status": "active",
    "taxSolution": {
      "key": "44",
      "id": "Avalara",
      "href": "/objects/tax/tax-solution/44",
      "taxCalculationMethod": "noTax",
      "showMultilineTax": true
    },
    "projectContractBillingInvoiceSummary": {
      "originalContractAmount": "1000.0000000000",
      "netApprovedChangesAmount": "1000.0000000000",
      "revisedContractAmount": "1000.0000000000",
      "completedFromPriorApplicationAmount": "1000.0000000000",
      "completedToDateAmount": "1000.0000000000",
      "lessPreviousBillingAmount": "1000.0000000000",
      "currentDueAmount": "1000.0000000000",
      "balanceToFinishAmount": "1000.0000000000",
      "taxAmount": "1000.0000000000",
      "chargeAmount": "1000.0000000000",
      "discountAmount": "1000.0000000000",
      "changesApprovedPriorMonth": {
        "additionsAmount": "1000.0000000000",
        "deductionsAmount": "1000.0000000000"
      },
      "changesApprovedThisMonth": {
        "additionsAmount": "1000.0000000000",
        "deductionsAmount": "1000.0000000000"
      },
      "retainage": {
        "amountRetained": "1000.0000000000",
        "billedAmount": "1000.0000000000",
        "netChangeHeldAmount": "1000.0000000000",
        "heldToDateAmount": "1000.0000000000",
        "billedToDateAmount": "1000.0000000000",
        "balanceToDateAmount": "1000.0000000000",
        "previousBalanceAmount": "1000.0000000000",
        "totalEarnedLessAmount": "1000.0000000000"
      },
      "accountsReceivableInvoiceNumber": "INV1",
      "orderEntryDocumentId": "SO-AIA-Invoice01-Ord#0011#doc",
      "projectId": "DIM - HCS",
      "projectName": "Dimensions - Hands Computer Systems"
    },
    "lines": [
      {
        "key": "44",
        "id": "44",
        "href": "/objects/order-entry/document-line::Sales%20Invoice/44",
        "documentType": "Sales Invoice",
        "lineNumber": 1,
        "item": {
          "key": "10",
          "id": "MX001",
          "href": "/objects/inventory-control/item/10"
        },
        "itemAlias": {
          "key": "10",
          "id": "IXN",
          "href": "/objects/accounts-receivable/customer-item-cross-reference/10"
        },
        "lineDescription": "MX001",
        "memo": "Payment ACH",
        "priceCalculationMemo": "Fair value price list",
        "unit": "Each",
        "quantity": "40.10",
        "unitQuantity": "10.10",
        "unitPrice": "10.50",
        "price": "33.66",
        "quantityConverted": "5.10",
        "retailPrice": "10.44",
        "audit": {
          "createdDateTime": "2022-04-20T16:20:00Z",
          "modifiedDateTime": "2022-04-20T16:20:00Z",
          "createdBy": "1",
          "modifiedBy": "95"
        },
        "status": "active",
        "costMethod": "average",
        "discountPercent": "10.50",
        "multiplier": 1,
        "sourceDocument": {
          "key": "77",
          "id": "Sales Order-SO0022",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document::Sales%20Order/77"
        },
        "sourceDocumentLine": {
          "key": "2234",
          "id": "2234",
          "documentType": "Sales Order",
          "href": "/objects/order-entry/document-line::Sales%20Order/2234"
        },
        "isPriceProrated": true,
        "discountMemo": "Festival discount",
        "baseCurrency": "USD",
        "txnCurrency": "CAD",
        "priceInTxnCurrency": "10.00",
        "isBillable": true,
        "isBilled": true,
        "taxRate": "10.05",
        "taxInBaseCurrency": "10.50",
        "taxInTxnCurrency": "40.50",
        "discount": "10.25",
        "enableTax": false,
        "quantityRemaining": "10.10",
        "conversionType": "quantity",
        "dimensions": {
          "location": {
            "key": "22",
            "id": "LOC-22",
            "name": "California",
            "href": "/objects/company-config/location/22"
          },
          "department": {
            "key": "9",
            "id": "Sales",
            "name": "Sales and Marketing",
            "href": "/objects/company-config/department/9"
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
            "id": "TSK01",
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
            "name": "Laptop 1"
          },
          "contract": {
            "id": "CON-0045-1",
            "key": "12",
            "name": "ACME Widgets - Service",
            "href": "/objects/contracts/contract/12"
          }
        },
        "itemRenewalTemplate": {
          "key": "45",
          "id": "Sales Renewal Template",
          "href": "/objects/order-entry/renewal-template/45"
        },
        "revenueRecognitionStartDate": "2024-04-04",
        "revenueRecognitionEndDate": "2024-04-04",
        "requestedShippingDate": "2024-04-04",
        "shipByDate": "2024-04-15",
        "pickTicketPrintedDate": "2024-04-04",
        "cancelAfterDate": "2024-04-15",
        "doNotShipBeforeDate": "2024-04-03",
        "doNotShipAfterDate": "2024-04-15",
        "shippedDate": "2024-04-04",
        "servicePeriodStartDate": "2024-04-01",
        "servicePeriodEndDate": "2024-04-30",
        "allowDropShip": true,
        "allowBuyToOrder": true,
        "revision": {
          "unitQuantity": "10",
          "quantity": "10",
          "unitValue": "8.00",
          "value": "8.00",
          "valueInTxnCurrency": "10.00",
          "price": "10.00",
          "unitPrice": "10.00",
          "priceInTxnCurrency": "10.00"
        },
        "draft": {
          "unitQuantity": "10",
          "quantity": "10",
          "price": "10.00",
          "basePrice": "10.00"
        },
        "posted": {
          "quantity": "10.00",
          "price": "10.00",
          "basePrice": "10.00"
        },
        "addedByChangeDocument": false,
        "projectContractBilling": {
          "externalReferenceNumber": "HGS-1024",
          "description": "Construction of clubhouse and offices",
          "billingType": "timeAndMaterial",
          "contractLineValue": "1000.00",
          "priorApplicationAmount": "1000.00",
          "completedThisPeriodAmount": "1000.00",
          "storedMaterialsAmount": "1000.00",
          "completedToDateAmount": "1000.00",
          "completedToDatePercent": "10.00",
          "balanceRemaining": "1000.00",
          "totalConvertedAmount": "1000.00",
          "totalRemainingAmount": "1000.00",
          "isSummarized": false
        },
        "retainage": {
          "percentage": "10.00",
          "baseAmountRetained": "10.00",
          "txnAmountRetained": "10.00",
          "isReleaseLine": true,
          "previousBalanceAmount": "1000.00",
          "billAmount": "1000.00",
          "balanceAmount": "1000.00",
          "extendedPriceNetAmount": "1000.00",
          "extendedBasePriceNetAmount": "1000.00"
        },
        "reverseConversion": {
          "isReverseConversion": true,
          "price": "100.00",
          "quantity": "100",
          "standardPrice": "100.00",
          "standardQuantity": "100"
        },
        "relatedDocument": {
          "id": "5151",
          "key": "5151",
          "documentNumber": "Sales Order-SD-SO0550",
          "href": "/objects/order-entry/document/5151"
        },
        "relatedDocumentLine": {
          "key": "13965",
          "id": "1--0001",
          "href": "/objects/order-entry/document-line/13965"
        },
        "projectContract": {
          "key": "1",
          "id": "BTI-01",
          "name": "Berkeley Technology Inc - Contract 01",
          "href": "/objects/construction/project-contract/1"
        },
        "projectContractLine": {
          "key": "4",
          "id": "Project-Contract-Line-04",
          "name": "Project contract line 04",
          "href": "/objects/construction/project-contract-line/4"
        },
        "taxSchedule": {
          "key": "1",
          "id": "Sale Goods Standard",
          "href": "/objects/tax/order-entry-tax-schedule/1"
        },
        "buyToOrderContact": {
          "key": "13",
          "id": "contact"
        },
        "trackingDetail": [
          {
            "key": "55",
            "id": "55",
            "href": "/objects/order-entry/document-line-detail/55",
            "quantity": "10",
            "serialNumber": "S1001",
            "lotNumber": "L1001",
            "expirationDate": "2024-04-04",
            "aisle": {
              "href": "/objects/inventory-control/aisle/10",
              "key": "10",
              "id": "AISLE1"
            },
            "bin": {
              "href": "/objects/inventory-control/bin/20",
              "key": "20",
              "id": "BIN1"
            },
            "row": {
              "href": "/objects/inventory-control/row/15",
              "key": "15",
              "id": "ROW1"
            },
            "item": {
              "key": "10",
              "id": "Battery",
              "href": "/objects/inventory-control/item/10"
            },
            "audit": {
              "createdDateTime": "2022-04-20T16:20:00Z",
              "modifiedDateTime": "2022-04-20T16:20:00Z",
              "createdBy": "1",
              "modifiedBy": "95"
            },
            "orderEntryDocumentLine": {
              "key": "23",
              "id": "23",
              "documentType": "Sales Order",
              "href": "/objects/order-entry-document-line::Sales%20Order/23"
            }
          }
        ],
        "lineSubtotals": [],
        "timesheetNotes": "Worked extra hours on project",
        "timeType": {
          "id": "Design",
          "key": 11,
          "href": "/objects/time/time-type/11"
        },
        "employeeExpenseType": {
          "id": "Meals",
          "key": 4,
          "href": "/objects/expenses/employee-expense-type/4"
        },
        "documentHeader": {
          "key": "55",
          "id": "Sales Invoice-SO0066",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry-document::Sales%20Invoice/55"
        }
      }
    ],
    "subtotals": [
      {
        "key": "12",
        "id": "12",
        "href": "/objects/order-entry/document-subtotal/12",
        "description": "Tax",
        "percentValue": "10.50",
        "absoluteValue": "40.50",
        "txnAbsoluteValue": "44.78",
        "total": "500.10",
        "txnTotal": "400.10",
        "documentLine": {
          "key": "10",
          "documentType": "Sales Order",
          "id": "10",
          "href": "/objects/order-entry-document-line::Sales%20Order/10"
        },
        "audit": {
          "createdDateTime": "2022-04-20T16:20:00Z",
          "modifiedDateTime": "2022-04-20T16:20:00Z",
          "createdBy": "1",
          "modifiedBy": "95"
        },
        "dimensions": {
          "location": {
            "key": "22",
            "id": "LOC-22",
            "name": "California",
            "href": "/objects/company-config/location/22"
          },
          "department": {
            "key": "9",
            "id": "Accounting",
            "name": "Sales and Marketing",
            "href": "/objects/company-config/department/9"
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
            "name": "Laptop 1"
          },
          "contract": {
            "id": "CON-0045-1",
            "key": "12",
            "name": "ACME Widgets - Service",
            "href": "/objects/contracts/contract/12"
          }
        },
        "documentHeader": {
          "key": "23",
          "id": "23",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document::Sales%20Order/23"
        }
      }
    ],
    "history": [
      {
        "key": "11",
        "id": "11",
        "href": "/objects/order-entry/document-history/11",
        "convertedFrom": {
          "key": "22",
          "id": "Sales Order-ORINV#0182#doc",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document::Sales%20Order/22"
        },
        "convertedTo": {
          "key": "14",
          "id": "Sales Invoice-SUBINV#0182#doc",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry-document::Sales%20Invoice/14"
        },
        "orderEntryDocument": {
          "key": "23",
          "id": "Sales Order-ORINV#0182#doc",
          "documentType": "Sales Order",
          "href": "/objects/order-entry-document::Sales%20Order/22"
        }
      }
    ]
  },
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 2,
    "totalError": 1
  }
}
```

## PATCH /objects/order-entry/document::{documentName}/{key}
_Update an Order Entry document_

**Request example — Update a document:**
```json
{
  "referenceNumber": "1012",
  "lines": [
    {
      "dimensions": {
        "item": {
          "key": "15"
        },
        "warehouse": {
          "key": "4"
        },
        "location": {
          "key": "6"
        }
      },
      "item": {
        "key": "15"
      },
      "unit": "10 Pack"
    },
    {
      "key": "22",
      "unitQuantity": "9",
      "price": "750"
    },
    {
      "key": "59",
      "ia::operation": "delete"
    }
  ]
}
```
**Request example — Update a document - Construction subscription:**
```json
{
  "exclusions": "Excludes additional purchase for materials.",
  "schedule": {
    "revisedCompletionDate": "2024-08-02",
    "DueDate": "2024-05-31",
    "scheduleImpactNotes": "Revised completion date to 2024-08-02"
  },
  "internalReference": {
    "sourceReferenceNumber": "7649851"
  }
}
```
**Request example — Update a project contract billing document:**
```json
{
  "retainagePercent": 16,
  "lines": [
    {
      "key": "13968",
      "projectContractBilling": {
        "completedThisPeriodAmount": "175.00",
        "storedMaterialsAmount": "25.00"
      }
    }
  ]
}
```
**Request example — Update service period dates of a document line:**
```json
{
  "lines": [
    {
      "key": "994",
      "servicePeriodStartDate": "2024-08-01",
      "servicePeriodEndDate": "2024-08-31"
    }
  ]
}
```
**Response 200 — Reference to updated document:**
```json
{
  "ia::result": {
    "key": "52",
    "id": "Sales Invoice-SUBINV#0182#doc",
    "documentType": "Sales Invoice",
    "href": "/objects/order-entry/document::Sales%20Invoice/52"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Reference to updated Construction document:**
```json
{
  "ia::result": {
    "key": "5150",
    "id": "SO-Order02-SO0549",
    "href": "/objects/order-entry/document::SO-Order02/5150"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Reference to updated project contract billing document:**
```json
{
  "ia::result": {
    "key": "5156",
    "id": "SO-AIA-Invoice01-Ord#0191#doc",
    "href": "/objects/order-entry/document::SO-AIA-Invoice01/5156"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/document::{documentName}/{key}
_Delete an Order Entry document_


## GET /objects/order-entry/price-list
_List price lists_

**Response 200 — List price lists:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Base Price List",
      "href": "/objects/order-entry/price-list/1"
    },
    {
      "key": "2",
      "id": "West Coast Price List",
      "href": "/objects/order-entry/price-list/2"
    },
    {
      "key": "3",
      "id": "Midwest Price List",
      "href": "/objects/order-entry/price-list/3"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/order-entry/price-list
_Create a price list_

**Request example — Create a price list:**
```json
{
  "id": "Base Price List Sales",
  "startDate": "2023-01-01",
  "endDate": "2030-12-31",
  "status": "active"
}
```
**Response 201 — New price list:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "Base Price List Sales",
    "href": "/objects/order-entry/price-list/5"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/order-entry/price-list-entry
_List price list entries_

**Response 200 — List price list entries:**
```json
{
  "ia::result": [
    {
      "key": "145",
      "id": "145",
      "href": "/objects/order-entry/price-list-entry/145"
    },
    {
      "key": "82",
      "id": "82",
      "href": "/objects/order-entry/price-list-entry/82"
    },
    {
      "key": "86",
      "id": "86",
      "href": "/objects/order-entry/price-list-entry/86"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "totalSuccess": 3,
    "totalError": 0
  }
}
```

## POST /objects/order-entry/price-list-entry
_Create a price list entry_

**Request example — Create a price list entry:**
```json
{
  "startDate": "2025-07-01",
  "endDate": "2025-09-31",
  "minimumQuantity": "1",
  "maximumQuantity": "9999999",
  "value": "10.00",
  "valueType": "actual",
  "isFixedPrice": "true",
  "status": "active",
  "item": {
    "key": "90"
  },
  "currency": "USD"
}
```
**Response 201 — Reference to new price list entry:**
```json
{
  "ia::result": {
    "id": "421",
    "key": "421",
    "href": "/objects/order-entry/price-list-entry/421"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/price-list-entry/{key}
_Get a price list entry_

**Response 200 — Get a price list entry:**
```json
{
  "ia::result": {
    "id": "451",
    "key": "451",
    "priceList": {
      "id": "Base Price List",
      "key": "1",
      "href": "/objects/order-entry/price-list/1"
    },
    "item'": {
      "key": "89",
      "id": "Car_Battery",
      "name": "Battery for Car",
      "href": "/objects/inventory-control/item/89"
    },
    "productLine": {
      "key": null,
      "id": null
    },
    "startDate": "2025-07-01",
    "endDate": "2025-07-31",
    "minimumQuantity": "1",
    "maximumQuantity": "999999999",
    "value": "10.00000000",
    "valueType": "actual",
    "isFixedPrice": "true",
    "status": "active",
    "currency": "USD",
    "employee": {
      "key": null,
      "id": null
    },
    "audit": {
      "createdDateTime": "2025-12-12T04:46:56Z",
      "modifiedDateTime": "2025-12-12T04:46:56Z",
      "createdByUser": {
        "key": "111",
        "id": "Admin",
        "href": "/objects/company-config/user/111"
      },
      "createdBy": "Admin",
      "modifiedByUser": {
        "key": "111",
        "id": "Admin",
        "href": "/objects/company-config/user/111"
      },
      "modifiedBy": "Admin"
    },
    "href": "/objects/order-entry/price-list-entry/451"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/price-list-entry/{key}
_Update a price list entry_

**Request example — Update a price list entry:**
```json
{
  "startDate": "2025-02-01"
}
```
**Response 200 — Reference to updated price list entry:**
```json
{
  "ia::result": {
    "id": "435",
    "key": "435",
    "href": "/objects/order-entry/price-list-entry/435"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/price-list-entry/{key}
_Delete a price list entry_


## GET /objects/order-entry/price-list/{key}
_Get a price list_

**Response 200 — Get a price list:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "Base Price List Sales",
    "startDate": "2023-01-01",
    "endDate": "2030-12-31",
    "status": "active",
    "href": "/objects/order-entry/price-list/5"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/order-entry/price-list/{key}
_Update a price list_

**Request example — Update a single value:**
```json
{
  "startDate": "2021-01-01"
}
```
**Response 200 — Updated price list:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "Base Price List Sales",
    "href": "/objects/order-entry/price-list/5"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/order-entry/price-list/{key}
_Delete a price list_


## GET /objects/order-entry/price-schedule
_List price schedules_

**Response 200 — List price schedules:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "M100",
      "href": "/objects/order-entry/price-schedule/1"
    },
    {
      "key": "2",
      "id": "10 Percent",
      "href": "/objects/order-entry/price-schedule/2"
    },
    {
      "key": "3",
      "id": "5 Percent",
      "href": "/objects/order-entry/price-schedule/3"
    }
  ],
  "ia::meta": {
    "pageSize": 100,
    "start": 1,
    "totalCount": 3
  }
}
```

## POST /objects/order-entry/price-schedule
_Create a price schedule_

**Request example — Create a price schedule:**
```json
{
  "id": "Acme Price",
  "description": "Acme Discount Schedule",
  "discountPercent": "10"
}
```
**Response 201 — New order entry price schedule:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "Acme Price",
    "href": "/objects/order-entry/price-schedule/9"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalError": 0,
    "totalSuccess": 1
  }
}
```

## GET /objects/order-entry/price-schedule/{key}
_Get a price schedule_

**Response 200 — Get a price schedule:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "Acme Price",
    "href": "/objects/order-entry/price-schedule/9",
    "description": "Acme Discount Schedule",
    "discountPercent": "10.00",
    "entity": {
      "id": null,
      "key": null,
      "name": null
    },
    "priceList": {
      "id": null,
      "key": null
    },
    "status": "active",
    "audit": {
      "createdBy": "1",
      "createdByUser": {
        "href": "/objects/company-config/user/1",
        "id": "Admin",
        "key": "1"
      },
      "createdDateTime": "2025-05-07T06:49:22Z",
      "modifiedBy": "1",
      "modifiedByUser": {
        "href": "/objects/company-config/user/1",
        "id": "Admin",
        "key": "1"
      },
      "modifiedDateTime": "2025-05-07T06:49:22Z"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalError": 0,
    "totalSuccess": 1
  }
}
```

## PATCH /objects/order-entry/price-schedule/{key}
_Update a price schedule_

**Request example — Update a price schedule:**
```json
{
  "discountPercent": "15"
}
```
**Response 200 — Updated price schedule:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "Acme Price",
    "href": "/objects/order-entry/price-schedule/9"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalError": 0,
    "totalSuccess": 1
  }
}
```

## DELETE /objects/order-entry/price-schedule/{key}
_Delete a price schedule_


## GET /objects/order-entry/recurring-document
_List recurring documents_

**Response 200 — List recurring documents:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "2",
      "href": "/objects/order-entry/recurring-document::Sales%20Invoice/2"
    },
    {
      "key": "6",
      "id": "6",
      "href": "/objects/order-entry/recurring-document::Sales%20Invoice/6"
    },
    {
      "key": "14",
      "id": "14",
      "href": "/objects/order-entry/recurring-document::Sales%20Order/14"
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

## GET /objects/order-entry/recurring-document-line
_List recurring document lines_

**Response 200 — List recurring document lines:**
```json
{
  "ia::result": [
    {
      "key": "19",
      "id": "19",
      "href": "/objects/order-entry/recurring-document-line/19"
    },
    {
      "key": "24",
      "id": "24",
      "href": "/objects/order-entry/recurring-document-line/24"
    },
    {
      "key": "25",
      "id": "25",
      "href": "/objects/order-entry/recurring-document-line/25"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/order-entry/recurring-document-line
_Create a recurring document line_

**Request example — Create a recurring document line:**
```json
{
  "recurringDocumentHeader": {
    "key": "469"
  },
  "dimensions": {
    "item": {
      "id": "1"
    },
    "warehouse": {
      "id": "1"
    },
    "location": {
      "id": "1"
    }
  },
  "unit": "Each",
  "unitQuantity": "1",
  "unitPrice": "650"
}
```
**Response 201 — Reference to new recurring document line:**
```json
{
  "ia::result": {
    "key": "807",
    "href": "/objects/order-entry/recurring-document-line::Sales%20Invoice/807"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/recurring-document-line/{key}
_Get a recurring document line_

**Response 200 — Get a recurring document line:**
```json
{
  "ia::result": {
    "id": "735",
    "key": "735",
    "recurringDocumentHeader": {
      "id": "6",
      "key": "6",
      "documentType": "Sales Invoice",
      "href": "/objects/order-entry/recurring-document::Sales%20Invoice/6"
    },
    "lineNumber": 1,
    "item": {
      "key": "15",
      "id": "Car_Battery",
      "href": "/objects/inventory-control/item/15"
    },
    "dimensions": {
      "item": {
        "id": "Car_Battery"
      },
      "warehouse": {
        "id": "WareHouse10004",
        "key": "4",
        "href": "/objects/inventory-control/warehouse/4"
      },
      "location": {
        "id": "1",
        "key": "6",
        "href": "/objects/company-config/location/6"
      },
      "department": {
        "id": "3",
        "key": "3",
        "href": "/objects/company-config/department/3"
      },
      "customer": {
        "key": "36",
        "id": "C-00045--MetroAtlantix, Inc.",
        "name": "MetroAtlantix, Inc.",
        "href": "/objects/accounts-receivable/customer/36"
      },
      "vendor": {
        "key": "510",
        "id": "V-00006--HPD Inc",
        "name": "HPD Inc",
        "href": "/objects/accounts-payable/vendor/510"
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
    "itemAlias": {
      "key": null,
      "id": null
    },
    "unit": "10 Pack",
    "memo": null,
    "status": "inactive",
    "recurringStatus": "active",
    "unitQuantity": "10.0000000000",
    "unitPrice": "1000.1200000000",
    "revenueRecognitionStartDate": null,
    "revenueRecognitionEndDate": null,
    "isPriceProrated": null,
    "retailPrice": "0.0000000000",
    "discountMemo": null,
    "currency": "USD",
    "priceInTxnCurrency": "1000.1200000000",
    "discountPercent": null,
    "isBillable": null,
    "conversionType": "quantity",
    "enableTax": false,
    "href": "/objects/order-entry/recurring-document-line/735"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/recurring-document-line/{key}
_Delete a recurring document line_


## GET /objects/order-entry/recurring-document-subtotal
_List recurring document subtotals_

**Response 200 — List of Order Entry recurring document subtotals:**
```json
{
  "ia::result": [
    {
      "key": "7",
      "id": "7",
      "href": "/objects/order-entry/recurring-document-subtotal/7"
    },
    {
      "key": "8",
      "id": "8",
      "href": "/objects/order-entry/recurring-document-subtotal/8"
    },
    {
      "key": "1520",
      "id": "1520",
      "href": "/objects/order-entry/recurring-document-subtotal/15"
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

## GET /objects/order-entry/recurring-document-subtotal/{key}
_Get a recurring document subtotal_

**Response 200 — Details of the Order Entry recurring document subtotal:**
```json
{
  "ia::result": {
    "id": "1520",
    "key": "1520",
    "recurringDocumentHeader": {
      "key": "6",
      "id": "6",
      "documentType": "Sales Invoice",
      "href": "/objects/order-entry/recurring-document::Sales%20Invoice/6"
    },
    "description": "Sales Tax",
    "absoluteValue": "80.45",
    "percentValue": "8.25",
    "total": "80.45000000000000",
    "dimensions": {
      "location": {
        "key": "Chicago",
        "id": "1",
        "href": "/objects/company-config/location/Chicago"
      },
      "customer": {
        "key": "22",
        "id": "CAR",
        "name": "CAR",
        "href": "/objects/accounts-receivable/customer/22"
      }
    },
    "txnAbsoluteValue": "80.45",
    "txnTotal": "80.45000000000000",
    "href": "/objects/order-entry/recurring-document-subtotal/1520"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/recurring-document/{key}
_Get a recurring document_

**Response 200 — Get a recurring document:**
```json
{
  "ia::result": {
    "id": "14",
    "key": "14",
    "txnDefinition": {
      "key": "86",
      "id": "Sales Invoice",
      "href": "/objects/order-entry/txn-definition::Sales%20Invoice/86"
    },
    "status": "active",
    "contacts": {
      "primary": {
        "key": "108",
        "id": "CAR(CCAR)",
        "href": "/objects/company-config/contact-version/108"
      },
      "shipTo": {
        "key": "108",
        "id": "CAR(CCAR)",
        "href": "/objects/company-config/contact-version/108"
      },
      "billTo": {
        "key": "108",
        "id": "CAR(CCAR)",
        "href": "/objects/company-config/contact-version/108"
      }
    },
    "referenceNumber": "1012",
    "paymentTerm": {
      "key": "5",
      "id": "N15",
      "href": "/objects/accounts-receivable/term/5"
    },
    "shippingMethod": {
      "id": "Air",
      "key": "2",
      "href": "/objects/accounts-receivable/shipping-method/2"
    },
    "memo": "Recurring subscription",
    "contractId": null,
    "contractDescription": null,
    "notes": null,
    "subtotal": "11001.32000000000000",
    "total": "11611.21000000000000",
    "recurringSchedule": {
      "id": "15",
      "key": "15",
      "href": "/objects/core/schedule/15"
    },
    "documentType": "Sales Invoice",
    "schedule": {
      "startDate": "2025-01-18",
      "endDate": null,
      "nextExecutionDate": "2025-01-18",
      "lastExecutionDate": null,
      "recurringDueDate": "2025-01-18",
      "frequency": "weeks",
      "executionCount": "0",
      "repeatCount": null,
      "repeatBy": "weeks",
      "repeatInterval": "4"
    },
    "customer": {
      "key": "22",
      "id": "CAR",
      "name": "Bernley Technology Inc",
      "href": "/objects/accounts-receivable/customer/22"
    },
    "baseCurrency": "USD",
    "txnCurrency": "USD",
    "exchangeRate": {
      "date": "2025-08-08",
      "typeName": null,
      "rate": "1.0000000000",
      "typeId": null
    },
    "subtotalInTxnCurrency": "11001.32000000000000",
    "totalInTxnCurrency": "11611.21000000000000",
    "state": "active",
    "audit": {
      "createdDateTime": "2024-08-08T09:19:34Z",
      "modifiedDateTime": "2024-08-08T10:46:15Z",
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
      "modifiedBy": "1",
      "customerPONumber": null,
      "entity": {
        "key": null,
        "id": null,
        "name": null
      }
    },
    "lines": [
      {
        "id": "814",
        "key": "814",
        "recurringDocumentHeader": {
          "id": "14",
          "key": "14",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
        },
        "lineNumber": 1,
        "item": {
          "key": "15",
          "id": "Car_Battery",
          "href": "/objects/inventory-control/item/15"
        },
        "dimensions": {
          "item": {
            "id": "Car_Battery"
          },
          "warehouse": {
            "id": "WareHouse10004",
            "key": "4",
            "href": "/objects/inventory-control/warehouse/4"
          },
          "location": {
            "id": "1",
            "key": "6",
            "href": "/objects/company-config/location/6"
          },
          "department": {
            "id": "3",
            "key": "3",
            "href": "/objects/company-config/department/3"
          },
          "customer": {
            "key": "36",
            "id": "C-00045--MetroAtlantix, Inc.",
            "name": "MetroAtlantix, Inc.",
            "href": "/objects/accounts-receivable/customer/36"
          },
          "vendor": {
            "key": "510",
            "id": "V-00006--HPD Inc",
            "name": "HPD Inc",
            "href": "/objects/accounts-payable/vendor/510"
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
        "itemAlias": {
          "key": null,
          "id": null
        },
        "unit": "10 Pack",
        "status": "inactive",
        "recurringStatus": "active",
        "unitQuantity": "9.0000000000",
        "isPriceProrated": null,
        "unitPrice": "1000.1200000000",
        "retailPrice": "0.0000000000",
        "discountMemo": null,
        "currency": "USD",
        "priceInTxnCurrency": "1000.1200000000",
        "conversionType": "quantity",
        "enableTax": false,
        "href": "/objects/order-entry/recurring-document-line/814"
      },
      {
        "id": "815",
        "key": "815",
        "recurringDocumentHeader": {
          "id": "14",
          "key": "14",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
        },
        "lineNumber": 2,
        "item": {
          "key": "157",
          "id": "Car_Battery_D",
          "href": "/objects/inventory-control/item/17"
        },
        "dimensions": {
          "item": {
            "id": "Car_Battery_D"
          },
          "warehouse": {
            "id": "WareHouse10004",
            "key": "4",
            "href": "/objects/inventory-control/warehouse/4"
          },
          "location": {
            "id": "1",
            "key": "6",
            "href": "/objects/company-config/location/6"
          },
          "department": {
            "id": "3",
            "key": "3",
            "href": "/objects/company-config/department/3"
          },
          "customer": {
            "key": "36",
            "id": "C-00045--MetroAtlantix, Inc.",
            "name": "MetroAtlantix, Inc.",
            "href": "/objects/accounts-receivable/customer/36"
          },
          "vendor": {
            "key": "510",
            "id": "V-00006--HPD Inc",
            "name": "HPD Inc",
            "href": "/objects/accounts-payable/vendor/510"
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
        "itemAlias": {
          "key": null,
          "id": null
        },
        "unit": "10 Pack",
        "status": "inactive",
        "recurringStatus": "active",
        "unitQuantity": "6.0000000000",
        "isPriceProrated": null,
        "unitPrice": "1500.1200000000",
        "retailPrice": "0.0000000000",
        "discountMemo": null,
        "currency": "USD",
        "priceInTxnCurrency": "1500.1200000000",
        "conversionType": "quantity",
        "enableTax": false,
        "href": "/objects/order-entry/recurring-document-line/815"
      }
    ],
    "subtotals": [
      {
        "id": "1627",
        "key": "1627",
        "recurringDocumentHeader": {
          "key": "14",
          "id": "14",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
        },
        "description": "Sales Discount",
        "absoluteValue": "275.03",
        "percentValue": "2.50",
        "total": "-275.03000000000000",
        "dimensions": {
          "department": {
            "id": "1",
            "key": "2",
            "href": "/objects/company-config/department/2"
          },
          "location": {
            "key": "1--Chicago",
            "id": "1",
            "href": "/objects/company-config/location/1--Chicago"
          },
          "customer": {
            "key": "22",
            "id": "CAR",
            "name": "CAR",
            "href": "/objects/accounts-receivable/customer/22"
          }
        },
        "txnAbsoluteValue": "275.03",
        "txnTotal": "-275.03000000000000",
        "href": "/objects/order-entry/recurring-document-subtotal/1627"
      },
      {
        "id": "1628",
        "key": "1628",
        "recurringDocumentHeader": {
          "key": "14",
          "id": "14",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
        },
        "description": "Sales Tax",
        "absoluteValue": "884.92",
        "percentValue": "8.25",
        "total": "884.92000000000000",
        "dimensions": {
          "department": {
            "id": "1",
            "key": "2",
            "href": "/objects/company-config/department/2"
          },
          "location": {
            "key": "1--Chicago",
            "id": "1",
            "href": "/objects/company-config/location/1--Chicago"
          },
          "customer": {
            "key": "22",
            "id": "CAR",
            "name": "CAR",
            "href": "/objects/accounts-receivable/customer/22"
          }
        },
        "txnAbsoluteValue": "884.92",
        "txnTotal": "884.92000000000000",
        "href": "/objects/order-entry/recurring-document-subtotal/1628"
      }
    ],
    "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/recurring-document::{documentName}
_List named recurring documents_

**Response 200 — List named recurring documents:**
```json
{
  "ia::result": [
    {
      "key": "171",
      "id": "171",
      "href": "/objects/order-entry/recurring-document::Sales%20Invoice/171"
    },
    {
      "key": "172",
      "id": "172",
      "href": "/objects/order-entry/recurring-document::Sales%20Invoice/172"
    },
    {
      "key": "155",
      "id": "155",
      "href": "/objects/order-entry/recurring-document::Sales%20Invoice/155"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/order-entry/recurring-document::{documentName}
_Create a recurring document_

**Request example — Create a recurring document:**
```json
{
  "referenceNumber": "RMF-001",
  "memo": "Discounted order",
  "txnCurrency": "USD",
  "baseCurrency": "USD",
  "shippingMethod": {
    "id": "Air"
  },
  "paymentTerm": {
    "id": "N15"
  },
  "customer": {
    "id": "22"
  },
  "schedule": {
    "startDate": "2024-07-01",
    "repeatBy": "weeks",
    "repeatInterval": "2",
    "endDate": "2025-12-01'"
  },
  "lines": [
    {
      "unit": "10 Pack",
      "unitQuantity": "1",
      "unitPrice": "1000.12",
      "dimensions": {
        "item": {
          "id": "Car_Battery"
        },
        "warehouse": {
          "id": "WareHouse10004"
        },
        "location": {
          "id": "1"
        }
      }
    }
  ]
}
```
**Response 201 — Reference to new recurring document:**
```json
{
  "ia::result": {
    "key": "13977",
    "id": "13977",
    "documentType": "Sales Invoice",
    "href": "/objects/order-entry/recurring-document::Sales%20Invoice/13977"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/recurring-document::{documentName}/{key}
_Get a named recurring document_

**Response 200 — Get a named recurring document:**
```json
{
  "ia::result": {
    "id": "14",
    "key": "14",
    "txnDefinition": {
      "key": "86",
      "id": "Sales Invoice",
      "href": "/objects/order-entry/txn-definition::Sales%20Invoice/86"
    },
    "status": "active",
    "contacts": {
      "primary": {
        "key": "108",
        "id": "CAR(CCAR)",
        "href": "/objects/company-config/contact-version/108"
      },
      "shipTo": {
        "key": "108",
        "id": "CAR(CCAR)",
        "href": "/objects/company-config/contact-version/108"
      },
      "billTo": {
        "key": "108",
        "id": "CAR(CCAR)",
        "href": "/objects/company-config/contact-version/108"
      }
    },
    "referenceNumber": "1012",
    "paymentTerm": {
      "key": "5",
      "id": "N15",
      "href": "/objects/accounts-receivable/term/5"
    },
    "shippingMethod": {
      "id": "Air",
      "key": "2",
      "href": "/objects/accounts-receivable/shipping-method/2"
    },
    "memo": "Recurring subscription",
    "contractId": null,
    "contractDescription": null,
    "notes": null,
    "subtotal": "11001.32000000000000",
    "total": "11611.21000000000000",
    "recurringSchedule": {
      "id": "15",
      "key": "15",
      "href": "/objects/core/schedule/15"
    },
    "documentType": "Sales Invoice",
    "schedule": {
      "startDate": "2025-01-18",
      "endDate": null,
      "nextExecutionDate": "2025-01-18",
      "lastExecutionDate": null,
      "recurringDueDate": "2025-01-18",
      "frequency": "weeks",
      "executionCount": "0",
      "repeatCount": null,
      "repeatBy": "weeks",
      "repeatInterval": "4"
    },
    "customer": {
      "key": "22",
      "id": "CAR",
      "name": "Bernley Technology Inc",
      "href": "/objects/accounts-receivable/customer/22"
    },
    "baseCurrency": "USD",
    "txnCurrency": "USD",
    "exchangeRate": {
      "date": "2025-08-08",
      "typeName": null,
      "rate": "1.0000000000",
      "typeId": null
    },
    "subtotalInTxnCurrency": "11001.32000000000000",
    "totalInTxnCurrency": "11611.21000000000000",
    "state": "active",
    "audit": {
      "createdDateTime": "2024-08-08T09:19:34Z",
      "modifiedDateTime": "2024-08-08T10:46:15Z",
      "createdByUser": {
        "key": "1",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "1",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1",
      "customerPONumber": null,
      "entity": {
        "key": null,
        "id": null,
        "name": null
      }
    },
    "lines": [
      {
        "id": "814",
        "key": "814",
        "recurringDocumentHeader": {
          "id": "14",
          "key": "14",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
        },
        "lineNumber": 1,
        "item": {
          "key": "15",
          "id": "Car_Battery",
          "href": "/objects/inventory-control/item/15"
        },
        "dimensions": {
          "item": {
            "id": "Car_Battery"
          },
          "warehouse": {
            "id": "WareHouse10004",
            "key": "4",
            "href": "/objects/inventory-control/warehouse/4"
          },
          "location": {
            "id": "1",
            "key": "6",
            "href": "/objects/company-config/location/6"
          },
          "department": {
            "id": "3",
            "key": "3",
            "href": "/objects/company-config/department/3"
          },
          "customer": {
            "key": "36",
            "id": "C-00045--MetroAtlantix, Inc.",
            "name": "MetroAtlantix, Inc.",
            "href": "/objects/accounts-receivable/customer/36"
          },
          "vendor": {
            "key": "510",
            "id": "V-00006--HPD Inc",
            "name": "HPD Inc",
            "href": "/objects/accounts-payable/vendor/510"
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
        "itemAlias": {
          "key": null,
          "id": null
        },
        "unit": "10 Pack",
        "status": "inactive",
        "recurringStatus": "active",
        "unitQuantity": "9.0000000000",
        "isPriceProrated": null,
        "unitPrice": "1000.1200000000",
        "retailPrice": "0.0000000000",
        "discountMemo": null,
        "currency": "USD",
        "priceInTxnCurrency": "1000.1200000000",
        "conversionType": "quantity",
        "enableTax": false,
        "href": "/objects/order-entry/recurring-document-line/814"
      },
      {
        "id": "815",
        "key": "815",
        "recurringDocumentHeader": {
          "id": "14",
          "key": "14",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
        },
        "lineNumber": 2,
        "item": {
          "key": "157",
          "id": "Car_Battery_D",
          "href": "/objects/inventory-control/item/17"
        },
        "dimensions": {
          "item": {
            "id": "Car_Battery_D"
          },
          "warehouse": {
            "id": "WareHouse10004",
            "key": "4",
            "href": "/objects/inventory-control/warehouse/4"
          },
          "location": {
            "id": "1",
            "key": "6",
            "href": "/objects/company-config/location/6"
          },
          "department": {
            "id": "3",
            "key": "3",
            "href": "/objects/company-config/department/3"
          },
          "customer": {
            "key": "36",
            "id": "C-00045--MetroAtlantix, Inc.",
            "name": "MetroAtlantix, Inc.",
            "href": "/objects/accounts-receivable/customer/36"
          },
          "vendor": {
            "key": "510",
            "id": "V-00006--HPD Inc",
            "name": "HPD Inc",
            "href": "/objects/accounts-payable/vendor/510"
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
        "itemAlias": {
          "key": null,
          "id": null
        },
        "unit": "10 Pack",
        "status": "inactive",
        "recurringStatus": "active",
        "unitQuantity": "6.0000000000",
        "isPriceProrated": null,
        "unitPrice": "1500.1200000000",
        "retailPrice": "0.0000000000",
        "discountMemo": null,
        "currency": "USD",
        "priceInTxnCurrency": "1500.1200000000",
        "conversionType": "quantity",
        "enableTax": false,
        "href": "/objects/order-entry/recurring-document-line/815"
      }
    ],
    "subtotals": [
      {
        "id": "1627",
        "key": "1627",
        "recurringDocumentHeader": {
          "key": "14",
          "id": "14",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
        },
        "description": "Sales Discount",
        "absoluteValue": "275.03",
        "percentValue": "2.50",
        "total": "-275.03000000000000",
        "dimensions": {
          "department": {
            "id": "1",
            "key": "2",
            "href": "/objects/company-config/department/2"
          },
          "location": {
            "key": "1--Chicago",
            "id": "1",
            "href": "/objects/company-config/location/1--Chicago"
          },
          "customer": {
            "key": "22",
            "id": "CAR",
            "name": "CAR",
            "href": "/objects/accounts-receivable/customer/22"
          }
        },
        "txnAbsoluteValue": "275.03",
        "txnTotal": "-275.03000000000000",
        "href": "/objects/order-entry/recurring-document-subtotal/1627"
      },
      {
        "id": "1628",
        "key": "1628",
        "recurringDocumentHeader": {
          "key": "14",
          "id": "14",
          "documentType": "Sales Invoice",
          "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
        },
        "description": "Sales Tax",
        "absoluteValue": "884.92",
        "percentValue": "8.25",
        "total": "884.92000000000000",
        "dimensions": {
          "department": {
            "id": "1",
            "key": "2",
            "href": "/objects/company-config/department/2"
          },
          "location": {
            "key": "1--Chicago",
            "id": "1",
            "href": "/objects/company-config/location/1--Chicago"
          },
          "customer": {
            "key": "22",
            "id": "CAR",
            "name": "CAR",
            "href": "/objects/accounts-receivable/customer/22"
          }
        },
        "txnAbsoluteValue": "884.92",
        "txnTotal": "884.92000000000000",
        "href": "/objects/order-entry/recurring-document-subtotal/1628"
      }
    ],
    "href": "/objects/order-entry/recurring-document::Sales%20Invoice/14"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/recurring-document::{documentName}/{key}
_Update a recurring document_

**Request example — Update a recurring document:**
```json
{
  "value": {
    "referenceNumber": "Recur-1012",
    "lines": [
      {
        "dimensions": {
          "item": {
            "key": "15"
          },
          "warehouse": {
            "key": "4"
          },
          "location": {
            "key": "6"
          }
        },
        "item": {
          "key": "15"
        },
        "unit": "10 Pack"
      }
    ]
  }
}
```
**Response 200 — Reference to updated recurring document:**
```json
{
  "ia::result": {
    "key": "52",
    "id": "52",
    "documentType": "Sales Invoice",
    "href": "/objects/order-entry/recurring-document::Sales%20Invoice/52"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/recurring-document::{documentName}/{key}
_Delete a recurring document_


## GET /objects/order-entry/recurring-schedule
_List recurring schedule_

**Response 200 — List recurring schedule:**
```json
{
  "ia::result": [
    {
      "key": "17",
      "id": "Daily",
      "href": "/objects/order-entry/recurring-schedule/17"
    },
    {
      "key": "19",
      "id": "Monthly",
      "href": "/objects/order-entry/recurring-schedule/19"
    },
    {
      "key": "20",
      "id": "Biweekly",
      "href": "/objects/order-entry/recurring-schedule/20"
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

## POST /objects/order-entry/recurring-schedule
_Create a recurring schedule_

**Request example — Create a recurring schedule:**
```json
{
  "id": "Weekly",
  "description": "Weekly schedule 2026",
  "repeatBy": "weeks",
  "repeatInterval": 1,
  "startDateType": "transactionDate"
}
```
**Response 201 — Reference to new recurring schedule:**
```json
{
  "ia::result": {
    "key": "17",
    "id": "Daily",
    "href": "/objects/order-entry/recurring-schedule/17"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/recurring-schedule/{key}
_Get a recurring schedule_

**Response 200 — Get a recurring schedule:**
```json
{
  "ia::result": {
    "key": "17",
    "id": "Daily",
    "description": "Daily schedule 2025",
    "createdByUser": {
      "key": "1",
      "id": "Admin",
      "href": "/objects/company-config/user/1"
    },
    "repeatBy": "days",
    "repeatInterval": 1,
    "startDateType": "transactionDate",
    "status": "active",
    "enableInstallmentPricing": false,
    "endDate": "2025-12-31",
    "repeatCount": null,
    "audit": {
      "createdDateTime": "2024-05-27T06:22:06Z",
      "modifiedDateTime": "2024-05-27T06:22:09Z",
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
    "href": "/objects/order-entry/recurring-schedule/17"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/recurring-schedule/{key}
_Update a recurring schedule_

**Request example — Update a recurring schedule:**
```json
{
  "startDateType": "userSpecified",
  "repeatInterval": 2
}
```
**Response 200 — Reference to updated recurring schedule:**
```json
{
  "ia::result": {
    "key": "17",
    "id": "Daily",
    "href": "/objects/order-entry/recurring-schedule/17"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/recurring-schedule/{key}
_Delete a recurring schedule_


## GET /objects/order-entry/renewal-template
_List renewal templates_

**Response 200 — List renewal templates:**
```json
{
  "ia::result": [
    {
      "key": "15",
      "id": "15",
      "href": "/objects/order-entry/renewal-template/19"
    },
    {
      "key": "16",
      "id": "16",
      "href": "/objects/order-entry/renewal-template/20"
    },
    {
      "key": "17",
      "id": "17",
      "href": "/objects/order-entry/renewal-template/21"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/order-entry/renewal-template
_Create a renewal template_

**Request example — Create a renewal template:**
```json
{
  "name": "Sales Subscription Renewal Template 2025",
  "description": "Template for 2025 subscription renewals",
  "salesTxnCreation": {
    "enableTxnCreation": true,
    "transactionDefinition": {
      "id": null,
      "key": null
    },
    "daysBeforeAfter": 9,
    "beforeOrAfterDateOfRenewal": "after",
    "txnDateOnRenewedDocument": "contractEndDatePlusOneDay",
    "txnLineItemStartDate": "sameAsDocumentDate"
  },
  "contractPricing": {
    "pricingType": "defaultPricing",
    "markup": "percentageMarkup",
    "markupValue": 10
  },
  "renewalNotifications": {
    "customerEmail": {
      "enableNotification": true,
      "from": null,
      "to": null,
      "daysBeforeAfter": 1,
      "beforeOrAfterContractRenewal": "before",
      "emailTemplate": {
        "key": 15
      }
    },
    "internalEmail": {
      "enableNotification": true,
      "from": null,
      "to": null,
      "daysBeforeAfter": 1,
      "beforeOrAfterContractRenewal": "before",
      "emailTemplate": {
        "key": 10
      }
    }
  },
  "salesforceOpportunity": {
    "enableSalesforceOpportunity": true,
    "daysBeforeAfter": 10,
    "beforeOrAfterContractRenewal": "before"
  },
  "status": "active",
  "transactionType": "contract",
  "defaultTerm": {
    "length": 2,
    "period": "months"
  },
  "renewalState": "inProgress"
}
```
**Response 201 — Reference to new renewal template:**
```json
{
  "ia::result": {
    "key": "30",
    "id": "30",
    "href": "/objects/order-entry/renewal-template/30"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/renewal-template/{key}
_Get a renewal template_

**Response 200 — Get a renewal template:**
```json
{
  "ia::result": {
    "id": 24,
    "key": 24,
    "name": "Sales Subscription Renewal Template 2025",
    "description": "Template for 2025 subscription renewals",
    "salesTxnCreation": {
      "enableTxnCreation": true,
      "transactionDefinition": {
        "id": null,
        "key": null
      },
      "daysBeforeAfter": 9,
      "beforeOrAfterDateOfRenewal": "after",
      "txnDateOnRenewedDocument": "contractEndDatePlusOneDay",
      "txnLineItemStartDate": "sameAsDocumentDate"
    },
    "contractPricing": {
      "pricingType": "defaultPricing",
      "markup": "percentageMarkup",
      "markupValue": 10
    },
    "renewalNotifications": {
      "customerEmail": {
        "enableNotification": true,
        "from": null,
        "to": "customerContact",
        "daysBeforeAfter": 0,
        "beforeOrAfterContractRenewal": "before",
        "emailTemplate": {
          "key": 15
        }
      },
      "internalEmail": {
        "enableNotification": true,
        "from": null,
        "to": null,
        "daysBeforeAfter": 10,
        "beforeOrAfterContractRenewal": "before",
        "emailTemplate": {
          "key": 9
        }
      }
    },
    "salesforceOpportunity": {
      "enableSalesforceOpportunity": true,
      "daysBeforeAfter": 10,
      "beforeOrAfterContractRenewal": "before",
      "renewalName": null,
      "inheritProductsFromParent": false,
      "stage": "qualification"
    },
    "latestVersion": 1,
    "status": "active",
    "transactionType": "contract",
    "defaultTerm": {
      "length": 2,
      "period": "months"
    },
    "renewalState": "inProgress",
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "href": "/objects/order-entry/renewal-template/24"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/renewal-template/{key}
_Update a renewal template_

**Request example — Update a renewal template:**
```json
{
  "description": "Subscription Invoice RevRec Creation Markup price - New 2026"
}
```
**Response 200 — Reference to updated renewal template:**
```json
{
  "ia::result": {
    "key": "30",
    "id": "30",
    "href": "/objects/order-entry/renewal-template/30"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/renewal-template/{key}
_Delete a renewal template_


## GET /objects/order-entry/subtotal-template
_List subtotal templates_

**Response 200 — List subtotal templates:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "UK VAT",
      "href": "/objects/order-entry/subtotal-template/1"
    },
    {
      "key": "2",
      "id": "InvoiceTax",
      "href": "/objects/order-entry/subtotal-template/2"
    },
    {
      "key": "3",
      "id": "SalesInvoiceCharges",
      "href": "/objects/order-entry/subtotal-template/3"
    },
    {
      "key": "4",
      "id": "Avalara",
      "href": "/objects/order-entry/subtotal-template/4"
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

## POST /objects/order-entry/subtotal-template
_Create a subtotal template_

**Request example — Creates a subtotal template:**
```json
{
  "id": "SalesInvoiceCharges",
  "lines": [
    {
      "description": "FreightCharge",
      "subtotalType": "discount",
      "lineNumber": 0,
      "valueType": "amount",
      "defaultValue": "10.00",
      "glAccount": {
        "id": "6850.03"
      },
      "offsetGLAccount": {
        "id": "1200"
      },
      "txnType": "debit"
    },
    {
      "description": "Discount",
      "subtotalType": "discount",
      "lineNumber": 1,
      "valueType": "percent",
      "defaultValue": "5",
      "isApportioned": false,
      "glAccount": {
        "id": "2000.00"
      },
      "offsetGLAccount": {
        "id": "1500.00"
      },
      "txnType": "debit"
    },
    {
      "description": "CASTax",
      "subtotalType": "charge",
      "lineNumber": 2,
      "valueType": "percent",
      "defaultValue": "6",
      "isApportioned": false,
      "glAccount": {
        "id": "2000.00"
      },
      "offsetGLAccount": {
        "id": "1500.00"
      },
      "txnType": "debit"
    }
  ]
}
```
**Response 201 — New order entry subtotal template:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "SalesInvoiceCharges",
    "href": "/objects/order-entry/subtotal-template/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/subtotal-template-line
_List subtotal template lines_

**Response 200 — List subtotal template lines:**
```json
{
  "ia::result": [
    {
      "key": "4",
      "id": "4",
      "href": "/objects/order-entry/subtotal-template-line/4"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/order-entry/subtotal-template-line/5"
    },
    {
      "key": "6",
      "id": "6",
      "href": "/objects/order-entry/subtotal-template-line/6"
    },
    {
      "key": "7",
      "id": "7",
      "href": "/objects/order-entry/subtotal-template-line/7"
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

## POST /objects/order-entry/subtotal-template-line
_Create a subtotal template line_

**Request example — Create a subtotal template line:**
```json
{
  "description": "FreightCharge",
  "subtotalTemplate": {
    "key": "3"
  },
  "subtotalType": "discount",
  "valueType": "amount",
  "defaultValue": "10.00",
  "isApportioned": false,
  "glAccount": {
    "id": "6850.03"
  },
  "offsetGLAccount": {
    "id": "1200"
  },
  "txnType": "debit",
  "applyToLineNumber": 0,
  "isTax": false,
  "isAvalaraTax": false
}
```
**Response 201 — Reference to new subtotal template line:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "4",
    "href": "/objects/order-entry/subtotal-template-line/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/subtotal-template-line/{key}
_Get a subtotal template line_

**Response 200 — Get a subtotal template line:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "4",
    "description": "FreightCharge",
    "subtotalTemplate": {
      "key": "3",
      "id": "3",
      "href": "/objects/order-entry/subtotal-template/3"
    },
    "subtotalType": "discount",
    "lineNumber": 0,
    "valueType": "amount",
    "defaultValue": "10.00",
    "isApportioned": false,
    "glAccount": {
      "key": "297",
      "id": "6850.03",
      "href": "/objects/general-ledger/account/297"
    },
    "offsetGLAccount": {
      "key": "36",
      "id": "1200",
      "href": "/objects/general-ledger/account/36"
    },
    "txnType": "debit",
    "applyToLineNumber": 0,
    "isTax": false,
    "isAvalaraTax": false,
    "href": "/objects/order-entry/subtotal-template-line/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/subtotal-template-line/{key}
_Update a subtotal template line_

**Request example — Update a subtotal template line:**
```json
{
  "subtotalType": "discount",
  "defaultValue": "15.00"
}
```
**Response 200 — Reference to updated subtotal template line:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "4",
    "href": "/objects/order-entry/subtotal-template-line/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/subtotal-template-line/{key}
_Delete a subtotal template line_


## GET /objects/order-entry/subtotal-template/{key}
_Get a subtotal template_

**Response 200 — Get a subtotal template:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "SalesInvoiceCharges",
    "moduleKey": "8.SO",
    "lines": [
      {
        "id": "4",
        "key": "4",
        "description": "FreightCharge",
        "subtotalType": "discount",
        "lineNumber": 0,
        "valueType": "amount",
        "defaultValue": "10.00",
        "isApportioned": false,
        "glAccount": {
          "key": "297",
          "id": "6850.03",
          "href": "/objects/general-ledger/account/297"
        },
        "offsetGLAccount": {
          "key": "36",
          "id": "1200",
          "href": "/objects/general-ledger/account/36"
        },
        "txnType": "debit",
        "applyToLineNumber": 0,
        "isTax": false,
        "isAvalaraTax": false,
        "href": "/objects/order-entry/subtotal-template-line/4"
      },
      {
        "id": "5",
        "key": "5",
        "description": "Discount",
        "subtotalType": "discount",
        "lineNumber": 1,
        "valueType": "percent",
        "defaultValue": "5",
        "isApportioned": false,
        "glAccount": {
          "key": "121",
          "id": "2000.00",
          "href": "/objects/general-ledger/account/121"
        },
        "offsetGLAccount": {
          "key": "122",
          "id": "1500.00",
          "href": "/objects/general-ledger/account/122"
        },
        "txnType": "debit",
        "applyToLineNumber": 0,
        "isTax": false,
        "isAvalaraTax": false,
        "href": "/objects/order-entry/subtotal-template-line/5"
      },
      {
        "id": "7",
        "key": "7",
        "description": "CASTax",
        "subtotalType": "charge",
        "lineNumber": 2,
        "valueType": "percent",
        "defaultValue": "6",
        "isApportioned": false,
        "glAccount": {
          "key": "121",
          "id": "2000.00",
          "href": "/objects/general-ledger/account/121"
        },
        "offsetGLAccount": {
          "key": "122",
          "id": "1500.00",
          "href": "/objects/general-ledger/account/122"
        },
        "txnType": "debit",
        "applyToLineNumber": 0,
        "isTax": false,
        "isAvalaraTax": false,
        "href": "/objects/order-entry/subtotal-template-line/7"
      }
    ],
    "audit": {
      "createdDateTime": "2024-12-04T00:00:00Z",
      "modifiedDateTime": "2024-12-04T00:00:00Z",
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
    "href": "/objects/order-entry/subtotal-template/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/subtotal-template/{key}
_Update a subtotal template_

**Request example — Update a subtotal template:**
```json
{
  "lines": [
    {
      "key": "4",
      "glAccount": {
        "id": "6850.03"
      }
    }
  ]
}
```
**Response 200 — Updated subtotal template:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "SalesInvoiceCharges",
    "href": "/objects/order-entry/subtotal-template/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/subtotal-template/{key}
_Delete a subtotal template_


## GET /objects/order-entry/txn-buy-to-order-preference
_List transaction buy to order preferences_

**Response 200 — List transaction buy to order preferences:**
```json
{
  "ia::result": [
    {
      "key": "5",
      "id": "5",
      "href": "/objects/order-entry/txn-buy-to-order-preference/5"
    },
    {
      "key": "6",
      "id": "6",
      "href": "/objects/order-entry/txn-buy-to-order-preference/6"
    },
    {
      "key": "7",
      "id": "7",
      "href": "/objects/order-entry/txn-buy-to-order-preference/7"
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

## GET /objects/order-entry/txn-buy-to-order-preference/{key}
_Get a transaction buy to order preference_

**Response 200 — Get a transaction buy to order preference:**
```json
{
  "ia::result": {
    "id": "5",
    "key": "5",
    "salesTxnDefinition": {
      "id": "44",
      "key": "44",
      "name": "Sales Order-CENTRAL",
      "href": "/objects/order-entry/txn-definition::Sales%20Order-CENTRAL/44"
    },
    "purchasingTxnDefinition": {
      "id": "45",
      "key": "45",
      "name": "Purchase Order-CENTRAL",
      "href": "/objects/purchasing/txn-definition::Purchase%20Order-CENTRAL/45"
    },
    "status": "active",
    "moduleName": "orderEntry",
    "audit": {
      "createdDateTime": "2026-09-26T13:13:31Z",
      "modifiedDateTime": "2026-09-26T14:21:49Z",
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
    "entity": {
      "key": "4",
      "id": "Central Region",
      "name": "Central Region",
      "href": "/objects/company-config/entity/4"
    },
    "href": "/objects/order-entry/txn-buy-to-order-preference/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-buy-to-order-preference/{key}
_Update a transaction buy to order preference_

**Request example — Update a transaction buy to order preference:**
```json
{
  "salesTxnDefinition": {
    "key": "30"
  }
}
```
**Response 200 — Reference to updated transaction buy to order preference:**
```json
{
  "ia::result": {
    "id": "24",
    "key": "24",
    "href": "/objects/order-entry/txn-buy-to-order-preference/24"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-buy-to-order-preference/{key}
_Delete a transaction buy to order preference_


## GET /objects/order-entry/txn-definition
_List transaction definitions_

**Response 200 — List transaction definitions:**
```json
{
  "ia::result": [
    {
      "key": "35",
      "id": "Sales Return",
      "href": "/objects/order-entry/txn-definition/35"
    },
    {
      "key": "37",
      "id": "Sales Invoice",
      "href": "/objects/order-entry/txn-definition/37"
    },
    {
      "key": "40",
      "id": "Shipper",
      "href": "/objects/order-entry/txn-definition/40"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 100
  }
}
```

## POST /objects/order-entry/txn-definition
_Create a transaction definition_

**Request example — Create a transaction definition:**
```json
{
  "id": "Sales Invoice",
  "docClass": "invoice",
  "workflowCategory": "invoice",
  "description": "Sales Invoice",
  "editPolicy": "all",
  "deletePolicy": "all",
  "enableNumberingSequence": true,
  "preserveNumberingSequence": true,
  "inheritDocumentNumber": false,
  "inventoryUpdateType": "no",
  "increaseOrDecreaseInventory": "decrease",
  "txnPostingMethod": "noPosting",
  "disableTax": false,
  "enableFulfillment": false,
  "enableReservingAndPicking": false,
  "partialConvertMethod": "closeOriginalAndCreateBackOrder",
  "affectsCost": false,
  "overrideExchangeRateType": true,
  "overridePrice": true,
  "trackDiscountAndSurcharge": false,
  "allowDiscountOnExtendedPrice": false,
  "requireMemoForDiscount": false,
  "enableSubtotals": false,
  "showExpandedTaxDetails": false,
  "enableOverrideTax": false,
  "revrecEnablementType": "none",
  "revenueRecognitionType": "none",
  "renewalEnablementType": "generate",
  "enableLineItemConversion": true,
  "allowRenewConvertedLineOnly": false,
  "allowLocationOverride": true,
  "allowDepartmentOverride": true,
  "xslTemplate": "Intacct Sales Invoice",
  "fixedMessage": "Sales Transaction",
  "contactOneTitle": "Bill to",
  "printBillToContact": true,
  "allowEditingBillToContact": false,
  "printShipToContact": true,
  "contactTwoTitle": "Ship to",
  "allowEditingShipToContact": false,
  "enableWarnOnLowQuantity": false,
  "enableCreditLimitCheck": false,
  "warehouseSelectionMethod": "useTheDefaultWarehouse",
  "displayDraftsOnRevenueTxnEntriesPage": false
}
```
**Response 201 — Reference to new transaction definition:**
```json
{
  "ia::result": {
    "key": "53",
    "id": "53",
    "href": "/objects/order-entry/txn-definition/53"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/txn-definition-additional-gl-detail
_List additional GL detail objects_

**Response 200 — List additional GL detail objects:**
```json
{
  "ia::result": [
    {
      "key": "195",
      "id": "195",
      "href": "/objects/order-entry/txn-definition-additional-gl-detail/195"
    },
    {
      "key": "196",
      "id": "196",
      "href": "/objects/order-entry/txn-definition-additional-gl-detail/196"
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

## GET /objects/order-entry/txn-definition-additional-gl-detail/{key}
_Get an additional GL detail object_

**Response 200 — Get an additional GL detail object:**
```json
{
  "ia::result": {
    "key": "195",
    "id": "195",
    "order-entry-txn-definition": {
      "key": "64",
      "id": "Sales Order",
      "href": "/objects/order-entry/txn-definition/64"
    },
    "itemGLGroup": {
      "key": "6",
      "id": "Auto GL Group",
      "href": "/objects/inventory-control/item-gl-group/6"
    },
    "isOffset": false,
    "txnType": "debit",
    "moduleType": "additional",
    "glAccount": {
      "id": "1000",
      "key": "3",
      "href": "/objects/general-ledger/account/3"
    },
    "lineNumber": 10,
    "href": "/objects/order-entry/txn-definition-additional-gl-detail/195"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-definition-additional-gl-detail/{key}
_Update an additional GL detail object_

**Request example — Update an additional GL account detail object:**
```json
{
  "isOffset": true
}
```
**Response 200 — Reference to updated additional GL account detail object:**
```json
{
  "ia::result": {
    "key": "195",
    "id": "195",
    "href": "/objects/order-entry/txn-definition-additional-gl-detail/195"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-definition-additional-gl-detail/{key}
_Delete an additional GL detail object_


## GET /objects/order-entry/txn-definition-ar-direct-gl-detail
_List Accounts Receivable or direct GL account detail objects_

**Response 200 — List Accounts Receivable or direct GL account detail objects:**
```json
{
  "ia::result": [
    {
      "key": "98",
      "id": "98",
      "href": "/objects/order-entry/txn-definition-ar-direct-gl-detail/98"
    },
    {
      "key": "163",
      "id": "163",
      "href": "/objects/order-entry/txn-definition-ar-direct-gl-detail/163"
    },
    {
      "key": "164",
      "id": "164",
      "href": "/objects/order-entry/txn-definition-ar-direct-gl-detail/164"
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

## GET /objects/order-entry/txn-definition-ar-direct-gl-detail/{key}
_Get an Accounts Receivable or direct GL account detail object_

**Response 200 — Get an Accounts Receivable or direct GL account detail object:**
```json
{
  "ia::result": {
    "key": "167",
    "id": "167",
    "order-entry-txn-definition": {
      "key": "43",
      "id": "Sales Invoice",
      "href": "/objects/order-entry/txn-definition/43"
    },
    "itemGLGroup": {
      "key": "2",
      "id": "OS GL Group",
      "href": "/objects/inventory-control/item-gl-group/2"
    },
    "isOffset": false,
    "txnType": "credit",
    "moduleType": "subledger",
    "glAccount": {
      "id": "4030",
      "key": "69",
      "href": "/objects/general-ledger/account/69"
    },
    "lineNumber": 1,
    "href": "/objects/order-entry/txn-definition-ar-direct-gl-detail/167"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-definition-ar-direct-gl-detail/{key}
_Update an Accounts Receivable or direct GL account detail object_

**Request example — Update an Accounts Receivable or direct GL account detail object:**
```json
{
  "isOffset": true
}
```
**Response 200 — Reference to updated Accounts Receivable or direct GL account detail object:**
```json
{
  "ia::result": {
    "key": "193",
    "id": "193",
    "href": "/objects/order-entry/txn-definition-ar-direct-gl-detail/193"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-definition-ar-direct-gl-detail/{key}
_Delete an Accounts Receivable or direct GL account detail object_


## GET /objects/order-entry/txn-definition-cogs-gl-detail
_List transaction definition COGS detail objects_

**Response 200 — List transaction definition COGS detail objects:**
```json
{
  "ia::result": [
    {
      "key": "159",
      "id": "159",
      "href": "/objects/order-entry/txn-definition-cogs-gl-detail/159"
    },
    {
      "key": "160",
      "id": "160",
      "href": "/objects/order-entry/txn-definition-cogs-gl-detail/160"
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

## GET /objects/order-entry/txn-definition-cogs-gl-detail/{key}
_Get a transaction definition COGS detail object_

**Response 200 — Get a transaction definition COGS detail object:**
```json
{
  "ia::result": {
    "key": "160",
    "id": "160",
    "order-entry-txn-definition": {
      "key": "43",
      "id": "Sales Invoice",
      "href": "/objects/order-entry/txn-definition/43"
    },
    "itemGLGroup": {
      "key": "16",
      "id": "HW GL Group",
      "href": "/objects/inventory-control/item-gl-group/16"
    },
    "txnType": "debit",
    "moduleType": "inventory",
    "glAccount": {
      "id": "5000",
      "key": "72",
      "href": "/objects/general-ledger/account/72"
    },
    "lineNumber": 11,
    "href": "/objects/order-entry/txn-definition-cogs-gl-detail/160"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-definition-cogs-gl-detail/{key}
_Update a transaction definition COGS detail object_

**Request example — Updates a transaction definition COGS detail object:**
```json
{
  "txnType": "credit",
  "isOffset": true
}
```
**Response 200 — Reference to updated transaction definition COGS detail object:**
```json
{
  "ia::result": {
    "key": "191",
    "id": "191",
    "href": "/objects/order-entry/txn-definition-cogs-gl-detail/191"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-definition-cogs-gl-detail/{key}
_Delete a transaction definition COGS detail object_


## GET /objects/order-entry/txn-definition-entity-setting-detail
_List transaction definition entity detail objects_

**Response 200 — List transaction definition entity detail objects:**
```json
{
  "ia::result": [
    {
      "key": "160",
      "id": "160",
      "href": "/objects/order-entry/txn-definition-entity-setting-detail/160"
    },
    {
      "key": "161",
      "id": "161",
      "href": "/objects/order-entry/txn-definition-entity-setting-detail/161"
    },
    {
      "key": "162",
      "id": "162",
      "href": "/objects/order-entry/txn-definition-entity-setting-detail/162"
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

## POST /objects/order-entry/txn-definition-entity-setting-detail
_Create a transaction definition entity detail object_

**Request example — Create a transaction definition entity detail object:**
```json
{
  "order-entry-txn-definition": {
    "key": "50"
  },
  "entity": {
    "id": "Mountain Region"
  },
  "enableNumberingSequence": false,
  "documentSequence": {
    "id": "AR Inv"
  },
  "preserveNumberingSequence": true,
  "canInheritSourceDocumentNumber": true,
  "showExpandedTaxDetail": false,
  "enableOverrideTax": true,
  "enableLineLevelSimpleTax": false
}
```
**Response 201 — Reference to new transaction definition entity detail object:**
```json
{
  "ia::result": {
    "key": "170",
    "id": "170",
    "href": "/objects/order-entry/txn-definition-entity-setting-detail/170"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/txn-definition-entity-setting-detail/{key}
_Get a transaction definition entity detail object_

**Response 200 — Get a transaction definition entity detail object:**
```json
{
  "ia::result": {
    "key": "162",
    "id": "162",
    "order-entry-txn-definition": {
      "key": "50",
      "id": "Sales Return",
      "href": "/objects/order-entry/txn-definition/50"
    },
    "entity": {
      "key": "3",
      "id": "Mountain Region",
      "href": "/objects/company-config/entity/3"
    },
    "enableNumberingSequence": true,
    "documentSequence": {
      "key": "11",
      "id": "AR Inv",
      "href": "/objects/company-config/document-sequence/11"
    },
    "preserveNumberingSequence": true,
    "canInheritSourceDocumentNumber": true,
    "enableCreateTransactionRule": true,
    "showExpandedTaxDetail": false,
    "enableOverrideTax": true,
    "enableLineLevelSimpleTax": false,
    "href": "/objects/order-entry/txn-definition-entity-setting-detail/162"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-definition-entity-setting-detail/{key}
_Update a transaction definition entity detail object_

**Request example — Update a transaction definition entity detail object:**
```json
{
  "showExpandedTaxDetail": true,
  "enableLineLevelSimpleTax": true
}
```
**Response 200 — Reference to updated transaction definition entity detail object:**
```json
{
  "ia::result": {
    "key": "174",
    "id": "174",
    "href": "/objects/order-entry/txn-definition-entity-setting-detail/174"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-definition-entity-setting-detail/{key}
_Delete a transaction definition entity detail object_


## GET /objects/order-entry/txn-definition-inventory-total-detail
_List transaction definition inventory total detail objects_

**Response 200 — List transaction definition inventory total detail objects:**
```json
{
  "ia::result": [
    {
      "key": "9",
      "id": "9",
      "href": "/objects/order-entry/txn-definition-inventory-total-detail/9"
    },
    {
      "key": "12",
      "id": "12",
      "href": "/objects/order-entry/txn-definition-inventory-total-detail/12"
    },
    {
      "key": "14",
      "id": "14",
      "href": "/objects/order-entry/txn-definition-inventory-total-detail/14"
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

## POST /objects/order-entry/txn-definition-inventory-total-detail
_Create a transaction definition inventory total detail object_

**Request example — Create a transaction definition inventory total detail object:**
```json
{
  "order-entry-txn-definition": {
    "key": "64"
  },
  "maintainType": "quantity",
  "inventoryTotal": {
    "id": "DAMAGED"
  },
  "operation": "add"
}
```
**Response 201 — Reference to new transaction definition inventory total detail object:**
```json
{
  "order-entry-txn-definition": {
    "key": "96"
  },
  "inventoryTotal": {
    "id": "DAMAGED"
  },
  "maintainType": "quantity",
  "operation": "add"
}
```

## GET /objects/order-entry/txn-definition-inventory-total-detail/{key}
_Get a transaction definition inventory total detail object_

**Response 200 — Get a transaction definition inventory total detail object:**
```json
{
  "ia::result": {
    "key": "125",
    "id": "125",
    "order-entry-txn-definition": {
      "key": "64",
      "id": "Sales Order",
      "href": "/objects/order-entry-txn-definition/64"
    },
    "maintainType": "quantity",
    "inventoryTotal": {
      "id": "DAMAGED"
    },
    "operation": "add",
    "href": "/objects/order-entry/txn-definition-inventory-total-detail/125"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-definition-inventory-total-detail/{key}
_Update a transaction definition inventory total detail object_

**Request example — Update a transaction definition inventory total detail object:**
```json
{
  "maintainType": "quantityAndValue",
  "operation": "subtract"
}
```
**Response 200 — Reference to updated transaction definition inventory total detail object:**
```json
{
  "ia::result": {
    "key": "128",
    "id": "128",
    "href": "/objects/order-entry/txn-definition-inventory-total-detail/128"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-definition-inventory-total-detail/{key}
_Delete a transaction definition inventory total detail object_


## GET /objects/order-entry/txn-definition-source-document-detail
_List transaction definition source document detail objects_

**Response 200 — List transaction definition source document detail objects:**
```json
{
  "ia::result": [
    {
      "key": "23",
      "id": "23",
      "href": "/objects/order-entry/txn-definition-source-document-detail/23"
    },
    {
      "key": "19",
      "id": "19",
      "href": "/objects/order-entry/txn-definition-source-document-detail/19"
    },
    {
      "key": "61",
      "id": "61",
      "href": "/objects/order-entry/txn-definition-source-document-detail/61"
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

## POST /objects/order-entry/txn-definition-source-document-detail
_Create a transaction definition source document detail object_

**Request example — Create a transaction definition source document detail object:**
```json
{
  "order-entry-txn-definition": {
    "key": "64"
  },
  "sourceDocument": {
    "id": "Sales Invoice"
  },
  "isDefault": false
}
```
**Response 201 — Reference to new transaction definition source document detail object:**
```json
{
  "ia::result": {
    "key": "70",
    "id": "70",
    "href": "/objects/order-entry/txn-definition-source-document-detail/70"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/txn-definition-source-document-detail/{key}
_Get a transaction definition source document detail object_

**Response 200 — Get a transaction definition source document detail object:**
```json
{
  "ia::result": {
    "key": "70",
    "id": "70",
    "order-entry-txn-definition": {
      "key": "64",
      "id": "Sales Order",
      "href": "/objects/order-entry/txn-definition/64"
    },
    "sourceDocument": {
      "key": "43",
      "id": "Sales Invoice",
      "href": "/objects/order-entry/txn-definition/43"
    },
    "isDefault": true,
    "href": "/objects/order-entry/txn-definition/source-document-detail/70"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-definition-source-document-detail/{key}
_Update a transaction definition source document detail object_

**Request example — Update a transaction definition source document detail object:**
```json
{
  "sourceDocument": {
    "key": "55"
  },
  "isDefault": true
}
```
**Response 200 — Reference to updated transaction definition source document detail object:**
```json
{
  "ia::result": {
    "key": "70",
    "id": "70",
    "href": "/objects/order-entry/txn-definition-source-document-detail/70"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-definition-source-document-detail/{key}
_Delete a transaction definition source document detail object_


## GET /objects/order-entry/txn-definition-subtotal-detail
_List transaction definition subtotal detail objects_

**Response 200 — List transaction definition subtotal detail objects:**
```json
{
  "ia::result": [
    {
      "key": "15",
      "id": "15",
      "href": "/objects/order-entry/txn-definition-subtotal-detail/15"
    },
    {
      "key": "19",
      "id": "19",
      "href": "/objects/order-entry/txn-definition-subtotal-detail/19"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/order-entry/txn-definition-subtotal-detail/3"
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

## POST /objects/order-entry/txn-definition-subtotal-detail
_Create a transaction definition subtotal detail object_

**Request example — Create a new transaction definition subtotal detail object:**
```json
{
  "order-entry-txn-definition": {
    "key": "64"
  },
  "subtotalType": "discount",
  "description": "discount",
  "appliedToLineNumber": 1,
  "isApportioned": false,
  "glAccount": {
    "id": "1000"
  },
  "offsetGLAccount": {
    "id": "1000.01"
  },
  "valueType": "percent",
  "txnType": "debit",
  "isTax": false
}
```
**Response 201 — Reference to new transaction definition subtotal detail object:**
```json
{
  "ia::result": {
    "key": "113",
    "id": "113",
    "href": "/objects/order-entry/txn-definition-subtotal-detail/113"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/order-entry/txn-definition-subtotal-detail/{key}
_Get a transaction definition subtotal detail object_

**Response 200 — Get a transaction definition subtotal detail object:**
```json
{
  "ia::result": {
    "key": "98",
    "id": "98",
    "order-entry-txn-definition": {
      "key": "64",
      "id": "Sales Order",
      "href": "/objects/order-entry-txn-definition/64"
    },
    "subtotalType": "discount",
    "lineNumber": 0,
    "description": "Discount",
    "valueType": "amount",
    "isApportioned": false,
    "txnType": "debit",
    "appliedToLineNumber": 1,
    "isTax": false,
    "glAccount": {
      "key": "3",
      "id": "1000",
      "href": "/objects/general-ledger/account/3"
    },
    "offsetGLAccount": {
      "key": "160",
      "id": "1000.01",
      "href": "/objects/general-ledger/account/160"
    },
    "enableAvalaraTax": false
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-definition-subtotal-detail/{key}
_Update a transaction definition subtotal detail object_

**Request example — Update a transaction definition subtotal detail object:**
```json
{
  "subtotalType": "discount",
  "txnType": "credit"
}
```
**Response 200 — Reference to updated transaction definition subtotal detail object:**
```json
{
  "ia::result": {
    "key": "94",
    "id": "94",
    "href": "/objects/order-entry/txn-definition-subtotal-detail/94"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-definition-subtotal-detail/{key}
_Delete a transaction definition subtotal detail object_


## GET /objects/order-entry/txn-definition/{key}
_Get a transaction definition_

**Response 200 — Get a transaction definition:**
```json
{
  "ia::result": {
    "key": "63",
    "id": "Sales Invoice",
    "docClass": "invoice",
    "workflowCategory": "invoice",
    "description": "Sales Invoice",
    "enableUserOrGroupPermmission": false,
    "enableUserOrGroupPermission": false,
    "editPolicy": "all",
    "deletePolicy": "all",
    "enableNumberingSequence": true,
    "documentSequence": {
      "id": "OE-Doc",
      "printTitle": "Sales Invoice"
    },
    "preserveNumberingSequence": true,
    "inheritDocumentNumber": false,
    "inventoryUpdateType": "no",
    "increaseOrDecreaseInventory": "decrease",
    "txnPostingMethod": "noPosting",
    "disableTax": false,
    "enableFulfillment": false,
    "enableReservingAndPicking": false,
    "partialConvertMethod": "closeOriginalAndCreateBackOrder",
    "affectsCost": false,
    "exchangeRateType": {
      "id": "Intacct Daily Rate",
      "key": "-1"
    },
    "overrideExchangeRateType": true,
    "showBaseCurrency": false,
    "initialPriceList": {
      "id": "Base Price List",
      "key": "1",
      "href": "/objects/order-entry-price-list/1"
    },
    "overridePrice": true,
    "trackDiscountAndSurcharge": false,
    "allowDiscountOnExtendedPrice": false,
    "requireMemoForDiscount": false,
    "freezeRecallValue": false,
    "enableSubtotals": false,
    "showExpandedTaxDetails": false,
    "enableOverrideTax": false,
    "revrecEnablementType": "none",
    "revenueRecognitionType": "none",
    "renewalEnablementType": "generate",
    "enableLineItemConversion": true,
    "allowRenewConvertedLineOnly": false,
    "allowLocationOverride": true,
    "allowDepartmentOverride": true,
    "xslTemplate": "Intacct Sales Invoice",
    "fixedMessage": "Sales Transaction",
    "contactOneTitle": "Bill to",
    "printBillToContact": true,
    "allowEditingBillToContact": false,
    "printShipToContact": true,
    "contactTwoTitle": "Ship to",
    "allowEditingShipToContact": false,
    "enableWarnOnLowQuantity": false,
    "enableCreditLimitCheck": false,
    "warehouseSelectionMethod": "useTheDefaultWarehouse",
    "warehouse": {
      "id": "WH02"
    },
    "status": "active",
    "enablePayments": false,
    "postToGL": false,
    "requireSupplyOfPrices": false,
    "enableCosting": false,
    "audit": {
      "modifiedDateTime": "2024-08-02T00:00:00Z",
      "createdDateTime": "2024-08-02T00:00:00Z",
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
    "documentConversionPolicy": "newDocumentOrConvert",
    "multiEntityRuleForTransaction": "topLevelOrEntity",
    "enableProjectActualBillings": false,
    "lineLevelSimpleTax": false,
    "customerVendorEditRule": "never",
    "enableRetainage": false,
    "enableAdditionalInformationScope": false,
    "enableAdditionalInformationSchedule": false,
    "enableInternalReference": false,
    "enableExternalReference": false,
    "enableBond": false,
    "documentChangeType": "noChange",
    "reportingCategory": "salesOrderInvoices",
    "enableContractBilling": false,
    "arPostingMethod": "none",
    "displayDraftsOnRevenueTxnEntriesPage": false,
    "href": "/objects/order-entry/txn-definition/63"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-definition/{key}
_Update a transaction definition_

**Request example — Update a transaction definition:**
```json
{
  "showBasecurrency": false,
  "canOverridePrice": true,
  "sourceDocumentDetail": [
    {
      "isDefault": true,
      "sourceDocument": {
        "id": "Vendor Invoice"
      }
    },
    {
      "key": "57",
      "isDefault": false
    },
    {
      "key": "59",
      "ia::operation": "delete"
    }
  ]
}
```
**Response 200 — Reference to updated transaction definition:**
```json
{
  "ia::result": {
    "key": "52",
    "href": "/objects/order-entry/txn-definition/52"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-definition/{key}
_Delete a transaction definition_


## GET /objects/order-entry/txn-drop-ship-preference
_List transaction drop ship preferences_

**Response 200 — List transaction drop ship preferences:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "8",
      "href": "/objects/order-entry/txn-drop-ship-preference/8"
    },
    {
      "key": "9",
      "id": "9",
      "href": "/objects/order-entry/txn-drop-ship-preference/9"
    },
    {
      "key": "10",
      "id": "10",
      "href": "/objects/order-entry/txn-drop-ship-preference/10"
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

## GET /objects/order-entry/txn-drop-ship-preference/{key}
_Get a transaction drop ship preference_

**Response 200 — Get a transaction drop ship preference:**
```json
{
  "ia::result": {
    "id": "8",
    "key": "8",
    "salesTxnDefinition": {
      "id": "43",
      "key": "43",
      "name": "Sales Invoice",
      "href": "/objects/order-entry/txn-definition::Sales%20Invoice/43"
    },
    "purchasingTxnDefinition": {
      "id": "4",
      "key": "4",
      "name": "Purchase Order",
      "href": "/objects/purchasing/txn-definition::Purchase%20Order/4"
    },
    "status": "active",
    "moduleName": "orderEntry",
    "audit": {
      "createdDateTime": "2026-09-26T13:12:58Z",
      "modifiedDateTime": "2026-10-09T05:48:41Z",
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
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "href": "/objects/order-entry/txn-drop-ship-preference/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/order-entry/txn-drop-ship-preference/{key}
_Update a transaction drop ship preference_

**Request example — Update a transaction drop ship preference:**
```json
{
  "salesTxnDefinition": {
    "key": "30"
  }
}
```
**Response 200 — Reference to updated transaction drop ship preference:**
```json
{
  "ia::result": {
    "id": "24",
    "key": "24",
    "href": "/objects/order-entry/txn-drop-ship-preference/24"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/order-entry/txn-drop-ship-preference/{key}
_Delete a transaction drop ship preference_

