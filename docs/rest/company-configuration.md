# Company Configuration

## GET /objects/company-config/advanced-audit-history
_List advanced audit histories_

**Response 200 — List advanced audit histories:**
```json
{
  "ia::result": [
    {
      "key": "OTA6MjgwOTU4",
      "id": "103:305:DISPLAYCONTACT.INITIAL:JohnDoe",
      "href": "/objects/company-config/advanced-audit-history/OTA6MjgwOTU4"
    },
    {
      "key": "OTA6MjgwOTYz",
      "id": "101:306::",
      "href": "/objects/company-config/advanced-audit-history/OTA6MjgwOTYz"
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

## GET /objects/company-config/advanced-audit-history/{key}
_Get an advanced audit history_

**Response 200 — Get an advanced audit history:**
```json
{
  "ia::result": {
    "key": "MzEwMDEwMDEwNjM5NDYtMTAzOjk",
    "id": "103:305:DISPLAYCONTACT.INITIAL:JohnDoe",
    "accessDetails": {
      "objectName": "accounts-receivable/customer",
      "objectId": "CUST001"
    },
    "accessSource": {
      "completedBy": "Admin",
      "accessDateTime": "2024-06-12T11:28:45Z",
      "actionPerformed": "personalData",
      "workflowAction": "2",
      "clientIPAddress": "10.226.2.142",
      "source": "userInterface"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/advanced-consolidation-preference/setup
_Get advanced consolidation preferences_


## PATCH /objects/company-config/advanced-consolidation-preference/setup
_Update advanced consolidation preferences_

**Request example — Update advanced consolidation preferences:**
```json
{
  "notificationEmail": "john.smith@company.com",
  "consolidatingLocation": {
    "key": "19"
  },
  "minorityInterestGLAccounts": {
    "interestLiabilityGLAccount": {
      "key": "13"
    },
    "incomeOrExpenseGLAccount": {
      "key": "23"
    }
  }
}
```
**Response 200 — Reference to advanced consolidation preferences:**
```json
{
  "ia::result": {
    "href": "/services/company-config/preferences/advanced-consolidation"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /objects/company-config/advanced-consolidation-preference/setup
_Create advanced consolidation preferences_

**Request example — Create advanced consolidation preferences:**
```json
{
  "notificationEmail": "john.smith@company.com",
  "consolidatingLocation": {
    "key": "19"
  },
  "minorityInterestGLAccounts": {
    "interestLiabilityGLAccount": {
      "key": "13"
    },
    "incomeOrExpenseGLAccount": {
      "key": "23"
    }
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

## GET /objects/company-config/affiliate-entity
_List affiliate entities_

**Response 200 — List affiliate entities:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/affiliate-entity/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/company-config/affiliate-entity/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/company-config/affiliate-entity/3"
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

## GET /objects/company-config/affiliate-entity-group
_List affiliate entity groups_

**Response 200 — List affiliate entity groups:**
```json
{
  "ia::result": [
    {
      "key": "3",
      "id": "u",
      "href": "/objects/company-config/affiliate-entity-group/3"
    },
    {
      "key": "1",
      "id": "Aff_Grp_USA",
      "href": "/objects/company-config/affiliate-entity-group/1"
    },
    {
      "key": "2",
      "id": "Aff_Group_Other",
      "href": "/objects/company-config/affiliate-entity-group/2"
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

## POST /objects/company-config/affiliate-entity-group
_Create an affiliate entity group_

**Request example — Create an affiliate entity group:**
```json
{
  "id": "Aff_3M",
  "name": "Aff_Grp_specific",
  "description": "affiliate group with 3 members",
  "groupType": "specific",
  "groupMembers": [
    {
      "key": "2"
    },
    {
      "key": "1"
    },
    {
      "id": "GM"
    }
  ]
}
```
**Response 201 — Reference to new affiliate entity group:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "Aff_3M",
    "href": "/objects/company-config/affiliate-entity-group/9"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/affiliate-entity-group/{key}
_Get an affiliate entity group_

**Response 200 — Get an affiliate entity group:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "Aff_3M",
    "name": "Aff_Grp_specific",
    "description": "affiliate group with 3 members",
    "groupType": "specific",
    "audit": {
      "createdDateTime": "2025-02-13T19:12:14Z",
      "modifiedDateTime": "2025-02-13T19:12:14Z",
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
    "groupMembers": [
      {
        "key": "2",
        "id": "E200",
        "name": "India",
        "href": "/objects/company-config/affiliate-entity/2"
      },
      {
        "key": "1",
        "id": "E100",
        "name": "United States of America",
        "href": "/objects/company-config/affiliate-entity/1"
      },
      {
        "key": "11",
        "id": "E111",
        "name": "Gulf of Mexico",
        "href": "/objects/company-config/affiliate-entity/11"
      }
    ],
    "isDimensionStructure": true,
    "memberFilter": {
      "object": "company-config/affiliate-entity",
      "filterExpression": "and",
      "orderBy": [
        {
          "name": "asc"
        }
      ]
    },
    "href": "/objects/company-config/affiliate-entity-group/9"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/affiliate-entity-group/{key}
_Update an affiliate entity group_

**Request example — Update an affiliate entity group:**
```json
{
  "name": "Aff_Grp_specific",
  "description": "Affiliate entity group updated to member 1 only",
  "groupType": "specific",
  "groupMembers": [
    {
      "key": "1",
      "id": "1"
    }
  ]
}
```
**Response 200 — Reference to updated affiliate entity group:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "Aff_3M",
    "href": "/objects/company-config/affiliate-entity-group/9"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/affiliate-entity-group/{key}
_Delete an affiliate entity group_


## GET /objects/company-config/affiliate-entity/{key}
_Get an affiliate entity_

**Response 200 — Get an affiliate entity:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "name": "Mariposa LLC",
    "status": "active",
    "audit": {
      "modifiedDateTime": "2023-04-13T09:19:58Z",
      "modifiedBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdDateTime": "2023-04-13T09:05:08Z",
      "createdBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/company-config/affiliate-entity/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/attachment
_List attachments_

**Response 200 — List attachments:**
```json
{
  "ia::result": [
    {
      "key": "8",
      "id": "PROJ-159",
      "href": "/objects/company-config/attachment/8"
    },
    {
      "key": "1",
      "id": "INVOICES",
      "href": "/objects/company-config/attachment/1"
    },
    {
      "key": "2",
      "id": "2024 Taxes",
      "href": "/objects/company-config/attachment/2"
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

## POST /objects/company-config/attachment
_Create an attachment_

**Request example — Create an empty attachment:**
```json
{
  "id": "2024 Tax",
  "name": "2024 Tax Forms",
  "folder": {
    "key": "27"
  }
}
```
**Request example — Create an attachment that contains a file:**
```json
{
  "id": "attach-02",
  "name": "Short text file",
  "folder": {
    "key": "1"
  },
  "files": [
    {
      "name": "short file.txt",
      "data": "aGVsbG8gd29ybGQhIHRoaXMgaXMgYmFzZTY0IGVuY29kZWQgZGF0YQ=="
    }
  ]
}
```
**Response 201 — Reference to new attachment:**
```json
{
  "ia::result": {
    "key": "17",
    "id": "2022 Tax",
    "href": "/objects/company-config/attachment/17"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/attachment/{key}
_Get an attachment_

**Response 200 — Get an attachment:**
```json
{
  "ia::result": {
    "key": "17",
    "id": "INV-V1",
    "name": "Vendor 1 Invoices",
    "folder": {
      "id": "Invoices",
      "key": "1",
      "href": "/objects/company-config/folder/1"
    },
    "description": "Invoices for Vendor 1",
    "audit": {
      "createdBy": "matthew.mikawber",
      "modifiedBy": "matthew.mikawber",
      "modifiedDate": "2023-05-25",
      "createdDate": "2023-05-25"
    },
    "files": [
      {
        "id": "29",
        "key": "29",
        "attachment": {
          "key": "17"
        },
        "data": "aGVsbG8gd29ybGQhIHRoaXMgaXMgYmFzZTY0IGVuY29kZWQgZGF0YQ==",
        "name": "short file.txt",
        "size": 40
      }
    ],
    "href": "/objects/company-config/attachment/17"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/attachment/{key}
_Update an attachment_

**Request example — Add a file to an attachment:**
```json
{
  "files": [
    {
      "name": "short file 2.txt",
      "data": "aGVsbG8gd29ybGQhIHRoaXMgaXMgYmFzZTY0IGVuY29kZWQgZGF0YQ=="
    }
  ]
}
```
**Request example — Delete a file from an attachment:**
```json
{
  "files": [
    {
      "key": "29",
      "ia::operation": "delete"
    }
  ]
}
```
**Response 200 — Reference to updated attachment:**
```json
{
  "ia::result": {
    "key": "17",
    "id": "attach-02",
    "href": "/objects/company-config/attachment/17"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/attachment/{key}
_Delete an attachment_


## GET /objects/company-config/audit-history
_List audit histories_

**Response 200 — List audit histories:**
```json
{
  "ia::result": [
    {
      "key": "OTA6MjgwOTU4",
      "id": "103:9",
      "href": "/objects/company-config/audit-history/OTA6MjgwOTU4"
    },
    {
      "key": "OTA6MjgwOTYz",
      "id": "103:10",
      "href": "/objects/company-config/audit-history/OTA6MjgwOTYz"
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

## GET /objects/company-config/audit-history/{key}
_Get an audit history_

**Response 200 — Get an audit history:**
```json
{
  "ia::result": {
    "key": "MzEwMDEwMDEwNjM5NDYtMTAzOjktRElTUExBWUNPTlRBQ1QuTEFTVE5BTUU",
    "id": "103:9",
    "changeDetails": {
      "objectName": "accounts-payable/vendor",
      "objectId": "a_vendor_id",
      "fieldName": "contacts.default.firstName",
      "previousValue": "John",
      "newValue": "Johnatan"
    },
    "changeSource": {
      "completedBy": "Admin",
      "accessDateTime": "2024-11-01T14:44:11Z",
      "actionPerformed": "modify",
      "workflowAction": "4",
      "clientIPAddress": "10.226.2.89",
      "source": "userInterface"
    },
    "notes": "NAME:a_vendor_name | VENDORID:a_vendor_id",
    "href": "/objects/company-config/audit-history/MzEwMDEwMDEwNjM5NDYtMTAzOjktRElTUExBWUNPTlRBQ1QuTEFTVE5BTUU"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/class
_List classes_

**Response 200 — list classes:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Class_1",
      "href": "/objects/company-config/class/1"
    },
    {
      "key": "2",
      "id": "Class_2",
      "href": "/objects/company-config/class/2"
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

## POST /objects/company-config/class
_Create a class_

**Request example — Create a single class:**
```json
{
  "id": "SW",
  "name": "Software",
  "description": "All software titles",
  "status": "active"
}
```
**Request example — Create a child class:**
```json
{
  "id": "SW-Office",
  "name": "Office Software",
  "description": "Office productivity software",
  "status": "active",
  "parent": {
    "key": "1"
  }
}
```
**Response 201 — Reference to new class:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "SW",
    "href": "/objects/company-config/class/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/company-config/class/{key}
_Get a class_

**Response 200 — Get a class:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "SS",
    "name": "Software & Services",
    "description": "Software & Services",
    "status": "active",
    "parent": {
      "key": "1",
      "id": "3",
      "name": "Heath Care",
      "href": "/objects/company-config/class/1"
    },
    "audit": {
      "createdDateTime": "2024-06-28T18:11:36Z",
      "modifiedDateTime": "2024-06-28T18:11:36Z",
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
    "locationKey": null,
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "href": "/objects/company-config/class/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/class/{key}
_Update a class_

**Request example — Update a single value:**
```json
{
  "name": "Root one"
}
```
**Response 200 — Reference to updated class:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Class1",
    "href": "/objects/company-config/class/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/class/{key}
_Delete a class_


## GET /objects/company-config/cloud-storage
_List cloud storage_

**Response 200 — List cloud storage:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "AWS cloud Storage A1",
      "href": "/objects/company-config/cloud-storage/1"
    },
    {
      "key": "2",
      "id": "AWS cloud Storage A2",
      "href": "/objects/company-config/cloud-storage/2"
    },
    {
      "key": "3",
      "id": "AWS cloud Storage A3",
      "href": "/objects/company-config/cloud-storage/3"
    },
    {
      "key": "4",
      "id": "AWS cloud Storage A4",
      "href": "/objects/company-config/cloud-storage/4"
    },
    {
      "key": "5",
      "id": "AWS cloud Storage A5",
      "href": "/objects/company-config/cloud-storage/5"
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

## POST /objects/company-config/cloud-storage
_Create a cloud storage_

**Request example — Creates a cloud storage object:**
```json
{
  "id": "Amazon Storage Plan",
  "storageType": "aws",
  "status": "active",
  "errorNotificationEmail": "john.doe@sage.com",
  "path": "/",
  "awsStorage": {
    "s3Bucket": "S3",
    "restrictFileAccess": "bucketOwnerOnly"
  },
  "owner": {
    "id": "Admin"
  }
}
```
**Response 201 — Reference to new cloud storage object:**
```json
{
  "ia::result": {
    "key": "44",
    "id": "AWS Cloud Storage1",
    "href": "/objects/company-config/cloud-storage/44"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/cloud-storage/{key}
_Get a cloud storage_

**Response 200 — Details of cloud storage object:**
```json
{
  "ia::result": {
    "key": "44",
    "id": "Amazon Storage Plan",
    "status": "active",
    "storageType": "aws",
    "state": "active",
    "audit": {
      "createdDateTime": "2023-11-30T10:19:22Z",
      "modifiedDateTime": "2023-11-30T10:19:22Z",
      "createdBy": "34",
      "modifiedBy": "1",
      "createdByUser": {
        "key": "34",
        "id": "Admin",
        "href": "/objects/company-config/user/34"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Aman",
        "href": "/objects/company-config/user/1"
      }
    },
    "errorNotificationEmail": "john.doe@sage.com",
    "queuedCount": 2,
    "isPrivate": true,
    "path": "/",
    "lastDeliveryDateTime": "2023-01-12T18:08:58Z",
    "lastDeliveryStatus": "Delivery error",
    "owner": {
      "key": "1",
      "id": "Admin",
      "userName": "ADMIN",
      "href": "/objects/company-config/user/1"
    },
    "awsStorage": {
      "s3Bucket": "S3",
      "enableEncryption": false,
      "restrictFileAccess": "bucketOwnerOnly"
    },
    "href": "/objects/company-config/cloud-storage/44"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/cloud-storage/{key}
_Update a cloud storage_

**Request example — Update a cloud storage object:**
```json
{
  "errorNotificationEmail": "john11.doe@sage.com"
}
```
**Response 200 — Reference to updated cloud storage object:**
```json
{
  "ia::result": {
    "key": "44",
    "id": "Amazon Storage Plan",
    "href": "/objects/company-config/cloud-storage/44"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/cloud-storage/{key}
_Delete a cloud storage_


## GET /objects/company-config/company-preference/{key}
_Get company preferences_

**Response 200 — Company preferences:**
```json
{
  "ia::result": {
    "accounting": null,
    "firstFiscalMonth": "march",
    "firstTaxMonth": "january",
    "reportingMethod": "cashBasis",
    "primaryAccountNumberLength": 4,
    "accountFieldSeparator": "period",
    "subAccountNumberLength": 2,
    "accountingPeriods": "standard",
    "weekBeginsOn": "sunday",
    "enableCustomCurrency": true,
    "operatingCountry": "france",
    "internationalTaxId": "123",
    "legalCategory": "24 Fiduciary",
    "mainActivity": "10.3 Transformation and conservation of fruits and vegetables",
    "typeOfCompany": "03 Intermediate sized enterprises",
    "registeredCapital": 500,
    "valueAddedTaxRegime": "Monthly"
  },
  "branding": {
    "messageText": "Superior financial Applications. Real-time business visibility. Open on-demand platform.",
    "marketingText": "This is a maketing text",
    "entityColor": "FF0000"
  },
  "id": "Example-Company-Id",
  "contractCustomerId": "C1234",
  "name": "Example-Company-Name"
}
```

## PATCH /objects/company-config/company-preference/{key}
_Update company preferences_

**Request example — Change security timeouts:**
```json
{
  "userSessionSettings": {
    "sessionTimeoutMinutes": 10,
    "inactivityTimeOutMinutes": 60
  }
}
```
**Response 200 — Company preferences updated:**
```json
{
  "ia::result": {
    "href": "/services/company-config/preferences/company"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/company-config/consolidation-preference/setup
_Get consolidation preferences_


## PATCH /objects/company-config/consolidation-preference/setup
_Update consolidation preferences_

**Request example — Update consolidation preferences:**
```json
{
  "consolidationSubscriptionSelection": "advancedOwnershipConsolidation"
}
```
**Response 200 — Reference to updated consolidation preferences:**
```json
{
  "ia::result": {
    "href": "/services/company-config/preferences/consolidation"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/contact
_List contacts_

**Response 200 — List contacts:**
```json
{
  "ia::result": [
    {
      "key": "265",
      "id": "Larry Spencer",
      "href": "/objects/company-config/contact/265"
    },
    {
      "key": "263",
      "id": "John Doe",
      "href": "/objects/company-config/contact/263"
    },
    {
      "key": "264",
      "id": "Alfred Mike",
      "href": "/objects/company-config/contact/264"
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

## POST /objects/company-config/contact
_Create a contact_

**Request example — Create a contact:**
```json
{
  "id": "AMoore",
  "prefix": "Mr",
  "firstName": "Andy",
  "lastName": "Moore",
  "middleName": "Robert",
  "printAs": "Andy Moore",
  "companyName": "Sage",
  "phone1": "9134598676",
  "mobile": "9133132299",
  "fax": "9134598677",
  "email1": "andy.moore@mycompany.com",
  "URL1": "http://andy.exampledomain.com",
  "mailingAddress": {
    "addressLine1": "744 Edgewater Blvd",
    "city": "Kansas City",
    "state": "KS",
    "postCode": "66104",
    "isoCountryCode": "us"
  },
  "tax": {
    "isTaxable": true,
    "taxId": "123-12-1234",
    "group": {
      "id": "New York"
    }
  },
  "status": "active"
}
```
**Response 201 — Reference to new contact:**
```json
{
  "ia::result": {
    "key": "312",
    "id": "AMoore",
    "href": "/objects/company-config/contact/312"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/contact-version
_List contact versions_

**Response 200 — List contact versions:**
```json
{
  "ia::result": [
    {
      "key": "4",
      "id": "4",
      "href": "/objects/company-config/contact-version/4"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/company-config/contact-version/5"
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

## GET /objects/company-config/contact-version/{key}
_Get a contact version_

**Response 200 — Details of the contact version:**
```json
{
  "ia::result": {
    "id": "340",
    "key": "340",
    "contact": {
      "id": "Kumar, Pradeep",
      "key": "253",
      "href": "/objects/company-config/contact/253"
    },
    "companyName": "Gen",
    "prefix": "Mr.",
    "firstName": "Kumar",
    "lastName": "Pradeep",
    "middleName": "P.",
    "printAs": "Kumar P. Pradeep",
    "phone1": "757-628-1429",
    "phone2": "518-627-4622",
    "mobile": "518-866-1291",
    "pager": "518-866-1222",
    "fax": "518-866-1211",
    "email1": "kumar.pradeep@mycompany.com",
    "email2": "pradeep.kumar@mycompany.com",
    "URL1": "www.mycompany.com",
    "URL2": "www.newbeginnings.com",
    "showInContactList": true,
    "tax": {
      "isTaxable": true,
      "group": {
        "id": "HW Contact Tax",
        "key": "1",
        "href": "/objects/tax/contact-tax-group/1"
      },
      "taxSchedule": {
        "id": null
      },
      "taxSolution": {
        "id": "Simple Tax",
        "key": "2",
        "href": "/objects/tax/tax-solution/2"
      },
      "taxId": "23144-1234",
      "taxIdValidationDate": "2025-02-20",
      "taxCompanyName": "Oasis",
      "taxAddress": "1896 Oak Drive"
    },
    "mailingAddress": {
      "addressLine1": "406 Allison Avenue",
      "addressLine2": "Suite 3",
      "addressLine3": "North campus",
      "city": "Boston",
      "country": "United States",
      "isoCountryCode": "us",
      "postCode": "12010",
      "state": "NY"
    },
    "status": "active",
    "priceSchedule": {
      "id": "5 Percent",
      "key": "1",
      "href": "/objects/purchasing/price-schedule/1"
    },
    "discountPercent": "1.00",
    "discount": "1",
    "priceList": {
      "id": "Initial Purchase Cost",
      "key": "2",
      "href": "/objects/order-entry/price-list/2"
    },
    "isGSTRegistered": true,
    "href": "/objects/company-config/contact-version/340"
  },
  "ia::meta": {
    "totalCount": 1,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/company-config/contact/{key}
_Get a contact_

**Response 200 — Contact details:**
```json
{
  "ia::result": {
    "key": "1257",
    "id": "AMoore",
    "companyName": "Sage",
    "prefix": "Mr",
    "firstName": "Andy",
    "lastName": "Moore",
    "middleName": "Robert",
    "printAs": "Andy Moore",
    "tax": {
      "isTaxable": true,
      "group": {
        "id": "New York",
        "key": "6",
        "href": "/objects/company-config/contact-tax-group/6"
      },
      "taxId": "123-12-1234"
    },
    "phone1": "9134598676",
    "phone2": null,
    "mobile": "9133132299",
    "pager": null,
    "fax": "9134598677",
    "email1": "andy.moore@mycompany.com",
    "email2": null,
    "URL1": "http://andy.exampledomain.com",
    "URL2": null,
    "showInContactList": true,
    "mailingAddress": {
      "addressLine1": "744 Edgewater Blvd",
      "addressLine2": null,
      "addressLine3": null,
      "city": "Kansas City",
      "country": "United States",
      "isoCountryCode": "us",
      "postCode": "66104",
      "state": "KS"
    },
    "status": "active",
    "priceSchedule": {
      "id": null,
      "key": null
    },
    "discount": null,
    "priceList": {
      "id": null,
      "key": null
    },
    "entity": {
      "key": "54",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/54"
    },
    "href": "/objects/company-config/contact/1257"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/contact/{key}
_Update a contact_

**Request example — Assign a price list and set a contact as non-taxable:**
```json
{
  "priceList": {
    "id": "Best customer pricing"
  },
  "tax": {
    "isTaxable": false
  }
}
```
**Response 200 — Reference to updated contact:**
```json
{
  "ia::result": {
    "key": "312",
    "id": "JohnD",
    "href": "/objects/company-config/contact/312"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/company-config/contact/{key}
_Delete a contact_


## GET /objects/company-config/department
_List departments_

**Response 200 — List of departments:**
```json
{
  "ia::result": [
    {
      "key": "11",
      "id": "Eng",
      "href": "/objects/company-config/department/1"
    },
    {
      "key": "2",
      "id": "Fin",
      "href": "/objects/company-config/department/2"
    },
    {
      "key": "3",
      "id": "HR",
      "href": "/objects/company-config/department/3"
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

## POST /objects/company-config/department
_Create a department_

**Request example — Create a department:**
```json
{
  "id": "ENG",
  "name": "Engineering",
  "reportTitle": "Engineering",
  "status": "active",
  "supervisor": {
    "key": "16"
  }
}
```
**Request example — Create a child department:**
```json
{
  "id": "SW",
  "name": "Software",
  "reportTitle": "Software Development",
  "status": "active",
  "parent": {
    "key": "28"
  },
  "supervisor": {
    "key": "5"
  }
}
```
**Response 201 — New department created:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "ENG",
    "href": "/objects/company-config/department/12"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/company-config/department-group
_List department groups_

**Response 200 — List of department groups:**
```json
{
  "ia::result": [
    {
      "key": "3",
      "id": "Accounting",
      "href": "/objects/company-config/department-group/3"
    },
    {
      "key": "1",
      "id": "Finance",
      "href": "/objects/company-config/department-group/1"
    },
    {
      "key": "2",
      "id": "HR",
      "href": "/objects/company-config/department-group/2"
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

## POST /objects/company-config/department-group
_Create a department group_

**Request example — Create a department group type all:**
```json
{
  "id": "HR",
  "name": "Human Resources",
  "groupType": "all",
  "memberFilter": {
    "object": "company-config/department",
    "filterExpression": "and",
    "filters": [
      {
        "$eq": {
          "name": "Accounting"
        }
      }
    ],
    "orderBy": [
      {
        "name": "asc"
      }
    ]
  }
}
```
**Response 201 — Reference to new department group:**
```json
{
  "ia::result": {
    "key": "19",
    "id": "HR",
    "href": "/objects/company-config/department-group/19"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/department-group-member
_List department group members_

**Response 200 — List of Department group Members:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/department-group-member/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/company-config/department-group-member/3"
    },
    {
      "key": "13",
      "id": "13",
      "href": "/objects/company-config/department-group-member/13"
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

## GET /objects/company-config/department-group-member/{key}
_Get a department group member_

**Response 200 — Details of the department group member:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "departmentGroup": {
      "key": "1",
      "href": "/objects/company-config/department-group/1"
    },
    "department": {
      "id": "8",
      "key": "8",
      "name": "Finance",
      "href": "/objects/company-config/department/8"
    },
    "sortOrder": 0,
    "audit": {
      "createdDateTime": "2016-10-26T17:28:33Z",
      "modifiedDateTime": "2016-10-26T17:28:33Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "href": "/objects/company-config/department-group-member/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/department-group/{key}
_Get a department group_

**Response 200 — Details of the department group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Top Departments",
    "name": "Top Level Departments",
    "description": "Top Level Departments",
    "groupType": "specific",
    "memberFilter": {
      "object": "company-config/department",
      "filterExpression": "and",
      "orderBy": [
        {
          "name": "asc"
        }
      ]
    },
    "audit": {
      "createdDateTime": "2023-10-26T00:00:00Z",
      "modifiedDateTime": "2023-10-26T00:00:00Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1",
        "createdBy": "1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1",
        "modifiedBy": "1"
      }
    },
    "groupMembers": [
      {
        "key": "32",
        "id": 1004,
        "name": 1004,
        "href": "/objects/company-config/department/32"
      },
      {
        "key": "33",
        "id": 1009,
        "name": 1009,
        "href": "/objects/company-config/department/33"
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

## PATCH /objects/company-config/department-group/{key}
_Update a department group_

**Request example — Update a department group:**
```json
{
  "description": "My Top departments America",
  "memberFilter": {
    "object": "company-config/department",
    "filterExpression": "and",
    "filters": [
      {
        "$eq": {
          "name": "Accounting"
        }
      }
    ],
    "orderBy": [
      {
        "name": "asc"
      }
    ]
  }
}
```
**Response 200 — Reference to updated department group:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "my top department",
    "href": "/objects/company-config/department-group/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/department-group/{key}
_Delete a department group_


## GET /objects/company-config/department/{key}
_Get a department_

**Response 200 — Department details:**
```json
{
  "ia::result": {
    "id": "PS",
    "key": "28",
    "name": "Professional Services",
    "parent": {
      "key": "7",
      "id": "CS--Client Services",
      "name": "Client Services",
      "href": "/objects/company-config/department/7"
    },
    "supervisor": {
      "key": "5",
      "id": "MGR1--PS Dept - Manager",
      "name": "PS Dept - Manager",
      "href": "/objects/company-config/employee/5"
    },
    "audit": {
      "createdDateTime": "2023-01-08T11:28:12Z",
      "modifiedDateTime": "2023-01-08T11:28:12Z",
      "createdBy": "1",
      "modifiedBy": "95",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "95",
        "id": "Aman",
        "href": "/objects/company-config/user/95"
      }
    },
    "status": "active",
    "reportTitle": "Professional Services",
    "href": "/objects/company-config/department/28"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/department/{key}
_Update a department_

**Request example — Change department supervisor:**
```json
{
  "supervisor": {
    "key": "99"
  }
}
```
**Response 200 — Department updated:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "SW",
    "href": "/objects/company-config/department/1"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/company-config/department/{key}
_Delete a department_


## GET /objects/company-config/document-sequence
_List document sequences_

**Response 200 — List of document sequences:**
```json
{
  "ia::result": [
    {
      "key": "37",
      "id": "BOA_ACH_BatchNo",
      "href": "/objects/company-config/document-sequence/37"
    },
    {
      "key": "27",
      "id": "Purchase Order",
      "href": "/objects/company-config/document-sequence/27"
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

## POST /objects/company-config/document-sequence
_Create a document sequence_

**Request example — Creates a numeric document sequence:**
```json
{
  "id": "Vendor Invoice",
  "printTitle": "Vendor Invoice",
  "type": "numeric",
  "fixedPrefix": "P",
  "fixedSuffix": "S",
  "prefixSeparator": "-",
  "suffixSeparator": "-",
  "startingNumber": 1,
  "endingNumber": null,
  "nextNumber": 1,
  "fixedLength": "4",
  "rollover": {
    "isEnabled": true,
    "fiscalYearAffixPosition": "prefix",
    "separator": "-",
    "fiscalYears": [
      {
        "fiscalYear": 2025,
        "nextNumber": 2025
      },
      {
        "fiscalYear": 2026,
        "nextNumber": 2026
      }
    ]
  }
}
```
**Request example — Creates an alphabetic document sequence:**
```json
{
  "id": "Vendor Invoice",
  "printTitle": "Vendor Invoice",
  "type": "alpha",
  "fixedPrefix": "P",
  "fixedSuffix": "S",
  "prefixSeparator": "-",
  "suffixSeparator": "-",
  "startingSequence": "a",
  "endingSequence": "c",
  "nextSequence": "a",
  "rollover": {
    "isEnabled": true,
    "fiscalYears": [
      {
        "fiscalYear": 2023,
        "nextSequence": "a"
      },
      {
        "fiscalYear": 2024,
        "nextSequence": "a"
      }
    ]
  }
}
```
**Response 201 — New document sequence:**
```json
{
  "ia::result": {
    "key": "107",
    "id": "Vendor Invoice",
    "href": "/objects/company-config/document-sequence/107"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/document-sequence-rollover
_List document sequence rollovers_

**Response 200 — List document sequence rollover objects:**
```json
{
  "ia::result": [
    {
      "key": "651",
      "id": "651",
      "href": "/objects/company-config/document-sequence-rollover/651"
    },
    {
      "key": "652",
      "id": "652",
      "href": "/objects/company-config/document-sequence-rollover/652"
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

## GET /objects/company-config/document-sequence-rollover/{key}
_Get a document sequence rollover_

**Response 200 — Get a document sequence rollover:**
```json
{
  "ia::result": {
    "id": "651",
    "key": "651",
    "documentSequence": {
      "key": "107",
      "id": "BOA_ACH_BatchNo",
      "href": "/objects/company-config/document-sequence/107"
    },
    "fiscalYear": 2026,
    "nextNumber": 1,
    "nextSequence": null,
    "audit": {
      "createdDateTime": "2025-01-15T21:58:11Z",
      "modifiedDateTime": "2025-01-15T21:58:11Z",
      "createdByUser": {
        "key": "158",
        "href": "/objects/company-config/user/158"
      },
      "createdBy": "158",
      "modifiedByUser": {
        "key": "158",
        "href": "/objects/company-config/user/158"
      },
      "modifiedBy": "158"
    },
    "href": "/objects/company-config/document-sequence-rollover/651"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/document-sequence/{key}
_Get a document sequence_

**Response 200 — Details of the document sequence:**
```json
{
  "ia::result": {
    "key": "107",
    "id": "BOA_ACH_BatchNo",
    "printTitle": "BOA_ACH_BatchNo",
    "fixedPrefix": "P",
    "fixedSuffix": "S",
    "prefixSeparator": "-",
    "suffixSeparator": "-",
    "startingNumber": 1,
    "endingNumber": null,
    "nextNumber": 1,
    "whenModified": "2014-01-08T11:28:12Z",
    "fixedLength": null,
    "status": "active",
    "type": "numeric",
    "startingSequence": null,
    "endingSequence": null,
    "nextSequence": null,
    "entity": {
      "key": "54",
      "id": "Western Region",
      "name": "Western Region",
      "href": "/objects/company-config/entity/54"
    },
    "rollover": {
      "isEnabled": true,
      "enabledDate": "2024-02-14",
      "fiscalYearAffixPosition": "prefix",
      "separator": "-"
    },
    "audit": {
      "createdDateTime": "2014-01-08T11:28:12Z",
      "modifiedDateTime": "2014-01-08T11:28:12Z",
      "createdBy": "109",
      "modifiedBy": "109"
    },
    "fiscalYears": [
      {
        "id": "646",
        "key": "646",
        "documentSequence": {
          "key": "405"
        },
        "fiscalYear": 2026,
        "nextNumber": 2026,
        "nextSequence": null,
        "audit": {
          "createdDateTime": "2024-02-14T12:34:02Z",
          "modifiedDateTime": "2024-02-14T12:34:02Z",
          "createdBy": "109",
          "modifiedBy": "109"
        }
      },
      {
        "id": "645",
        "key": "645",
        "documentSequence": {
          "key": "405"
        },
        "fiscalYear": 2025,
        "nextNumber": 2025,
        "nextSequence": null,
        "audit": {
          "createdDateTime": "2024-02-14T12:34:02Z",
          "modifiedDateTime": "2024-02-14T12:34:02Z",
          "createdBy": "109",
          "modifiedBy": "109"
        }
      }
    ],
    "href": "/objects/company-config/document-sequence/107"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/document-sequence/{key}
_Update a document sequence_

**Request example — Change the prefix separator:**
```json
{
  "prefixSeparator": "-"
}
```
**Response 200 — Updated document sequence:**
```json
{
  "ia::result": {
    "key": "107",
    "id": "BOA_ACH_BatchNo",
    "href": "/objects/company-config/document-sequence/107"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/document-sequence/{key}
_Delete a document sequence_


## GET /objects/company-config/earning-type
_List earning types_

**Response 200 — List earning types:**
```json
{
  "ia::result": [
    {
      "key": "46",
      "id": "Overtime",
      "href": "/objects/time/earning-type/46"
    },
    {
      "key": "44",
      "id": "Part time",
      "href": "/objects/time/earning-type/44"
    },
    {
      "key": "40",
      "id": "Full time",
      "href": "/objects/time/earning-type/40"
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

## POST /objects/company-config/earning-type
_Create an earning type_

**Request example — Create an earning type:**
```json
{
  "id": "Overtime",
  "billableGLAccount": {
    "key": "158"
  },
  "nonBillableGLAccount": {
    "key": "159"
  },
  "calculationMethod": "hourly",
  "rateMultiplier": "2"
}
```
**Response 201 — Reference to new earning type:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "10",
    "href": "/objects/time/earning-type/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/earning-type/{key}
_Get an earning type_

**Response 200 — Get an earning type:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Overtime",
    "billableGLAccount": {
      "key": "158",
      "id": "6775.30",
      "name": "Travel",
      "href": "/objects/general-ledger/account/23"
    },
    "nonBillableGLAccount": {
      "key": "158",
      "id": "6774.30",
      "name": "Expense",
      "href": "/objects/general-ledger/account/23"
    },
    "rateMultiplier": "2",
    "calculationMethod": "hourly",
    "audit": {
      "createdDateTime": "2024-04-20T16:20:00Z",
      "modifiedDateTime": "2025-04-20T16:20:00Z",
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
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/earning-type/{key}
_Update an earning type_

**Request example — Update an earning type:**
```json
{
  "rateMultiplier": "1.5"
}
```
**Response 200 — Reference to updated earning type:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Overtime",
    "href": "/objects/time/earning-type/10"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/company-config/earning-type/{key}
_Delete an earning type_


## GET /objects/company-config/email-delivery-record
_List email delivery records_

**Response 200 — List email delivery records:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/email-delivery-record/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/company-config/email-delivery-record/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/company-config/email-delivery-record/3"
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

## GET /objects/company-config/email-delivery-record/{key}
_Get an email delivery record_

**Response 200 — Details of the email delivery record:**
```json
{
  "ia::result": {
    "id": "1",
    "key": "1",
    "status": "queued",
    "tenantContext": "WDIjad73gE8Q8aNLYEkv2zJn/CO3rAUxt3ia1wLRKFGeqC+4lSp48iFoYJ5LJLf36toGA7faZAVS/J5H1xHDfB8NQwyCi2HUtQNrWsE176jr7vRb",
    "from": "Support <support@intacct.com>",
    "to": "emailsender@intacct.com",
    "subject": "dev01: Document due on 09/30/2023 for Customer - Associated Research Inc",
    "failureStatus": null,
    "failureReason": null,
    "sentDateTime": "2024-01-15T11:29:15Z",
    "lastUpdatedDateTime": null,
    "emailMessage": {
      "FROM": "Support <support@intacct.com>",
      "SENDERNAME": "Support",
      "SENDEREMAIL": "support@intacct.com",
      "REPLY_TO": "Support <support@intacct.com>",
      "TO": [
        "emailsender@intacct.com"
      ],
      "CC": [],
      "BCC": [],
      "SUBJECT": "dev01: Document due on 09/30/2023 for Customer - Associated Research Inc",
      "BODY": "Dear Customer,<br><br>A document is attached to this email as a PDF file.<br>    Document No. Sales Invoice-Sal#0175#inv<br>    Due Date: 09/30/2023<br><br>If you have any questions, please reply to this email.<br><br>To view this, click on the attachment. Adobe Acrobat should launch. If you do not have Acrobat installed on your computer, you can download it from <a href='http://www.adobe.com/products/acrobat/readstep2.html'>here</a><br><br>Sincerely,<br>Punji Chandrashekhar<br>AL_Prod_GL-main (support@intacct.com)<br/><br/><br/><br/><br/><hr/><img width=\"120\" src=\"https://intacct-ops-prod-public-assets.s3.us-west-2.amazonaws.com/logo.png\" alt=\"\"/>"
    },
    "emailProviderId": "dt2FGrVFSNO0JQXAGSxTag",
    "deliveryHistory": [
      {
        "key": "390",
        "sendTo": "john.deo@company.com",
        "status": "delivered",
        "dateTime": "2025-07-15T07:57:05Z",
        "additionalInfo": "TSL: 1"
      },
      {
        "key": "389",
        "sendTo": "john.deo@company.com",
        "status": "processed",
        "dateTime": "2025-07-15T07:57:07Z",
        "additionalInfo": "TSL: 1"
      }
    ],
    "replyTo": "Support <support@intacct.com>",
    "cc": "",
    "bcc": "",
    "body": "Dear Customer,<br><br>A document is attached to this email as a PDF file.<br>    Document No. Sales Invoice-Sal#0175#inv<br>    Due Date: 09/30/2023<br><br>If you have any questions, please reply to this email.<br><br>To view this, click on the attachment. Adobe Acrobat should launch. If you do not have Acrobat installed on your computer, you can download it from here<br><br>Sincerely,<br>Support<br>AL_Prod_GL-main (support@intacct.com)<br/><br/><br/><br/><br/>",
    "href": "/objects/company-config/email-delivery-record/1",
    "ia::meta": {
      "totalCount": 1,
      "totalSuccess": 1,
      "totalError": 0
    }
  }
}
```

## GET /objects/company-config/email-template
_List email templates_

**Response 200 — List email templates:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/email-template/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/company-config/email-template/2"
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

## POST /objects/company-config/email-template
_Create an email template_

**Request example — Create an email template:**
```json
{
  "name": "New Customer Email Template",
  "description": "Email template for new customers",
  "templateType": "purchasingTxn",
  "sender": {
    "approvedSenderEmailId": "11"
  },
  "recipients": {
    "to": "yourEmail@customer.com"
  },
  "subject": "Welcome!",
  "body": "New customers receive a 10% discount on their first subscription order."
}
```
**Request example — Create an email template using own email address:**
```json
{
  "name": "New Customer Email Template - Own Email",
  "description": "Email template using the sender's own email address",
  "templateType": "purchasingTxn",
  "sender": {
    "useOwnEmailAddress": true
  },
  "recipients": {
    "to": "yourEmail@customer.com"
  },
  "subject": "Welcome!",
  "body": "New customers receive a 10% discount on their first subscription order."
}
```
**Request example — Create a budgetVariance email template:**
```json
{
  "name": "BvA Controller 1AA",
  "description": "BvA Controller 1A",
  "templateType": "budgetVariance",
  "status": "active",
  "budgetVarianceNotification": {
    "notificationType": "exceedOperatingExpense",
    "recipients": "unrestrictedUsers"
  },
  "sender": {
    "senderName": "Abhijit",
    "approvedSenderEmailId": "11"
  },
  "recipients": {
    "to": "{!BVASETUP.INSIGHT_USER_EMAIL_ID!}"
  },
  "subject": "{!COMPANY.TITLE!} - Sage Copilot notification: Budget variance detected",
  "body": "Hi {!BVASETUP.INSIGHT_USER_CONTACT_NAME!},\n\nYou have insights available in Sage Copilot. We've included a preview in this email, but there's more information available.\n\nLog into <a href='{!BVASETUP.COPILOT_LOGIN_TO_SAGE_INTACCT_LINK!}'>Sage Intacct</a> and access Copilot to see more.\n{!BVASETUP.ALL_RUN_TIME_INSIGHT_IMAGES!}\n\nThank you,\nSage Intacct\nBvA Controller 1A",
  "logo": {
    "isLogoIncluded": false,
    "verticalPosition": "bottom",
    "horizontalPosition": "left"
  },
  "includeTxnAttachments": false,
  "includeProjectInvoiceTxnAttachments": false,
  "combineAttachmentsToZip": "none"
}
```
**Response 201 — Reference to new budgetVariance email template:**
```json
{
  "ia::result": {
    "id": "12",
    "key": "12",
    "href": "/objects/company-config/email-template/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 201 — Reference to new email template:**
```json
{
  "ia::result": {
    "id": "19",
    "key": "19",
    "href": "/objects/company-config/email-template/19"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/email-template/{key}
_Get an email template_

**Response 200 — Get an email template:**
```json
{
  "ia::result": {
    "id": "2",
    "key": "2",
    "audit": {
      "createdDateTime": "2014-08-22T18:45:25Z",
      "modifiedDateTime": "2014-05-19T06:12:46Z",
      "createdByUser": {
        "key": "1",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "82",
        "href": "/objects/company-config/user/82"
      },
      "modifiedBy": "82"
    },
    "status": "active",
    "name": "Email Template for Customer",
    "description": "Email Template for Customer",
    "templateType": "contract",
    "sender": {
      "senderName": "Lester B",
      "approvedSenderEmailId": "5"
    },
    "recipients": {
      "to": "{!CONTRACT.DISPLAYCONTACT.EMAIL1}",
      "cc": "'{!CONTRACT.DISPLAYCONTACT.EMAIL2!};{!CONTRACT.BILLTO.EMAIL1!}'",
      "bcc": null
    },
    "subject": "Renewal notification for contract: {!CONTRACT.CONTRACTID!}",
    "body": "'Hi {!CONTRACT.CUSTOMERNAME!},\n\nThis is a friendly reminder that the contract {!CONTRACT.CONTRACTID!}--{!CONTRACT.NAME!} is renewing {!CONTRACT.ENDDATE!}. The renewal contract is {!CONTRACT.BASECURR!}.\nPlease contact your sales representative if you have any questions.\nRegards,\nContract Team.'",
    "logo": {
      "isLogoIncluded": true,
      "verticalPosition": "top",
      "horizontalPosition": "left"
    },
    "includeTxnAttachments": false,
    "includeProjectInvoiceTxnAttachments": false,
    "combineAttachmentsToZip": "none",
    "href": "/objects/company-config/email-template/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a budgetVariance email template:**
```json
{
  "ia::result": {
    "id": "19",
    "key": "19",
    "audit": {
      "createdDateTime": "2025-09-11T06:52:30Z",
      "modifiedDateTime": "2025-09-11T07:09:11Z",
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
    "name": "BvA Controller 1A",
    "description": "BvA Controller 1A",
    "templateType": "budgetVariance",
    "budgetVarianceNotification": {
      "notificationType": "exceedOperatingExpense",
      "recipients": "unrestrictedUsers"
    },
    "sender": {
      "senderName": "Abhijit",
      "approvedSenderEmailId": "11"
    },
    "recipients": {
      "to": "{!BVASETUP.INSIGHT_USER_EMAIL_ID!}"
    },
    "subject": "{!COMPANY.TITLE!} - Sage Copilot notification: Budget variance detected",
    "body": "Hi {!BVASETUP.INSIGHT_USER_CONTACT_NAME!},\n\nYou have insights available in Sage Copilot. We've included a preview in this email, but there's more information available.\n\nLog into <a href='{!BVASETUP.COPILOT_LOGIN_TO_SAGE_INTACCT_LINK!}'>Sage Intacct</a> and access Copilot to see more.\n{!BVASETUP.ALL_RUN_TIME_INSIGHT_IMAGES!}\n\nThank you,\nSage Intacct\nBvA Controller 1A",
    "logo": {
      "isLogoIncluded": false,
      "verticalPosition": "bottom",
      "horizontalPosition": "left"
    },
    "includeTxnAttachments": false,
    "includeProjectInvoiceTxnAttachments": false,
    "combineAttachmentsToZip": "none",
    "href": "/objects/company-config/email-template/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/email-template/{key}
_Update an email template_

**Request example — Update an email template:**
```json
{
  "name": "New Customer Email SW",
  "recipients": {
    "to": "someEmail@co.com"
  },
  "includeTxnAttachments": true
}
```
**Request example — Update approved sender email:**
```json
{
  "sender": {
    "approvedSenderEmailId": "14"
  }
}
```
**Request example — Update a budgetVariance email template:**
```json
{
  "budgetVarianceNotification": {
    "recipients": "managers"
  }
}
```
**Response 200 — Reference to updated email template:**
```json
{
  "ia::result": {
    "id": "6",
    "key": "6",
    "href": "/objects/company-config/email-template/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Reference to updated budgetVariance email template:**
```json
{
  "ia::result": {
    "id": "19",
    "key": "19",
    "href": "/objects/company-config/email-template/19"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/email-template/{key}
_Delete an email template_


## GET /objects/company-config/employee
_List employees_

**Response 200 — List employees:**
```json
{
  "ia::result": [
    {
      "key": "32",
      "id": "jsmith",
      "href": "/objects/company-config/employee/32"
    },
    {
      "key": "52",
      "id": "rdas",
      "href": "/objects/company-config/employee/52"
    },
    {
      "key": "17",
      "id": "ajones",
      "href": "/objects/company-config/employee/17"
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

## POST /objects/company-config/employee
_Create an employee_

**Request example — Create a new employee:**
```json
{
  "id": "mVanitha",
  "SSN": "650125932",
  "jobTitle": "Accountants",
  "startDate": "2021-04-30",
  "birthDate": "1984-04-01",
  "name": "Mary Vanitha",
  "defaultCurrency": "USD",
  "manager": {
    "id": "MGR-CS"
  },
  "location": {
    "id": "1"
  },
  "department": {
    "id": "TS"
  },
  "earningType": {
    "id": "Salaries"
  },
  "postActualCostWithVariance": false,
  "employeeType": {
    "id": "Full Time"
  },
  "primaryContact": {
    "id": "Mary"
  },
  "attachmentFolder": {
    "key": "10"
  },
  "preferredPaymentMethod": "cash"
}
```
**Response 201 — Reference to new employee:**
```json
{
  "ia::result": {
    "key": "59",
    "id": "mVanitha",
    "href": "/objects/company-config/employee/59"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/employee-bank-file-setup
_List employee bank file setups_

**Response 200 — List employee bank file setups:**
```json
{
  "ia::result": [
    {
      "key": "25",
      "id": "25",
      "href": "/objects/company-config/employee-bank-file-setup/25"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/company-config/employee-bank-file-setup/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/company-config/employee-bank-file-setup/60"
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

## GET /objects/company-config/employee-bank-file-setup/{key}
_Get an employee bank file setup_

**Response 200 — Get a South African (ZA) bank file setup:**
```json
{
  "ia::result": {
    "key": "25",
    "id": "25",
    "employee": {
      "key": "202",
      "id": "SAEmployee",
      "href": "/objects/company-config/employee/202"
    },
    "paymentReference": "Expenses-019567",
    "branchCode": "123433",
    "bankAccountType": "1",
    "bankAccountCode": "345678",
    "bankAccountNumber": "87402896",
    "bankAccountName": "Jane Robertson",
    "href": "/objects/company-config/employee-bank-file-setup/25"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get an Australian (AU) bank file setup:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "employee": {
      "key": "162",
      "id": "AUEmployee",
      "href": "/objects/company-config/employee/162"
    },
    "bsbNumber": "163-821",
    "paymentReference": "Salary July 2025",
    "bankAccountNumber": "87402896",
    "bankAccountName": "Janice Smith",
    "href": "/objects/company-config/employee-bank-file-setup/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a UK bank file setup:**
```json
{
  "ia::result": {
    "key": "26",
    "id": "26",
    "employee": {
      "key": "203",
      "id": "UKEmployee",
      "href": "/objects/company-config/employee/203"
    },
    "bsbNumber": null,
    "paymentReference": "Week 32 Payment",
    "sortCode": "849571",
    "bankAccountNumber": "87402896",
    "bankAccountName": "Colleen Watson",
    "href": "/objects/company-config/employee-bank-file-setup/26"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Get a US bank file setup:**
```json
{
  "ia::result": {
    "key": "78",
    "id": "78",
    "employee": {
      "key": "389",
      "id": "tsmith",
      "href": "/objects/company-config/employee/389"
    },
    "bsbNumber": null,
    "paymentReference": "Expenses-019545",
    "sortCode": null,
    "branchCode": null,
    "bankAccountType": "32",
    "bankAccountCode": null,
    "bankAccountNumber": "4534455667",
    "bankAccountName": "Jacqui Thompson",
    "businessIdCode": "564534456",
    "accountClassification": "ccd",
    "href": "/objects/company-config/employee-bank-file-setup/78"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/employee-group
_List employee groups_

**Response 200 — List employee groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/employee-group/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/company-config/employee-group/3"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/company-config/employee-group/5"
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

## POST /objects/company-config/employee-group
_Create an employee group_

**Request example — Create an employee group of type all:**
```json
{
  "id": "E 01",
  "name": "my top 01 employee",
  "description": "my top 01 employee",
  "groupType": "all",
  "memberFilter": {
    "object": "company-config/employee",
    "filterExpression": "and",
    "filters": [
      {
        "$eq": {
          "id": 8
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
**Response 201 — Reference to new employee group:**
```json
{
  "ia::result": {
    "key": "21",
    "id": "E 01",
    "href": "/objects/company-config/employee-group/19"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/employee-group/{key}
_Get an employee group_

**Response 200 — Details of an employee group:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "MGR",
    "href": "/objects/company-config/employee-group/23",
    "name": "Sr. Managers",
    "description": "Managers G10 and above",
    "groupType": "specific",
    "isDimensionStructure": false,
    "memberFilter": {
      "object": "company-config/employee",
      "filterExpression": "and",
      "filters": [
        {
          "$in": {
            "status": "inactive"
          }
        }
      ],
      "orderBy": [
        {
          "status": "asc"
        }
      ]
    },
    "groupMembers": [
      {
        "key": "1",
        "id": "jsmith",
        "href": "/objects/company-config/employee/23",
        "status": "active"
      }
    ],
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
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/employee-group/{key}
_Update an employee group_

**Request example — Update an employee group:**
```json
{
  "description": "My Top 001 employee"
}
```
**Response 200 — Reference to updated employee group:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "E 01",
    "href": "/objects/company-config/employee-group/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/employee-group/{key}
_Delete an employee group_


## GET /objects/company-config/employee-rate
_List employee rates_

**Response 200 — List employee rates:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/employee-rate/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/company-config/employee-rate/3"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/company-config/employee-rate/5"
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

## GET /objects/company-config/employee-rate/{key}
_Get an employee rate_

**Response 200 — Get an employee rate:**
```json
{
  "ia::result": {
    "id": "11",
    "key": "11",
    "employee": {
      "key": "14",
      "id": "EM 1",
      "name": "Aman",
      "href": "/objects/company-config/employee/14"
    },
    "hourlyRate": null,
    "annualSalary": "160000",
    "startDate": "2011-01-01",
    "endDate": "2011-12-31",
    "audit": {
      "createdDateTime": "2016-06-28T20:44:36Z",
      "modifiedDateTime": "2016-06-28T20:44:36Z",
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
    "href": "/objects/company-config/employee-rate/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/employee-rate/{key}
_Delete an employee rate_


## GET /objects/company-config/employee-type
_List employee types_

**Response 200 — List employee types:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "Part-time",
      "href": "/objects/company-config/employee-type/100"
    },
    {
      "key": "101",
      "id": "Full-time",
      "href": "/objects/company-config/employee-type/101"
    },
    {
      "key": "102",
      "id": "Contractor",
      "href": "/objects/company-config/employee-type/102"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 5,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/company-config/employee-type
_Create an employee type_

**Request example — Create an employee type:**
```json
{
  "id": "Temporary Worker",
  "parent": {
    "key": "1"
  },
  "status": "active"
}
```
**Response 201 — Reference to new employee type:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "Temporary Worker",
    "href": "/objects/company-config/employee-type/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/employee-type/{key}
_Get an employee type_

**Response 200 — Get an employee type:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "Temporary Worker",
    "parent": {
      "id": "Full Time",
      "key": "1",
      "href": "/objects/company-config/employee-type/1"
    },
    "status": "active",
    "form1099": {
      "type": null,
      "box": null
    },
    "audit": {
      "createdDateTime": "2025-09-25T10:15:52Z",
      "modifiedDateTime": "2025-09-25T10:15:52Z",
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
    "href": "/objects/company-config/employee-type/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/employee-type/{key}
_Update an employee type_

**Request example — Update an employee type:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated employee type:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "Temporary Worker",
    "href": "/objects/company-config/employee-type/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/employee-type/{key}
_Delete an employee type_


## GET /objects/company-config/employee/{key}
_Get an employee_

**Response 200 — Get an employee:**
```json
{
  "ia::result": {
    "key": "59",
    "id": "mVanitha",
    "SSN": "650125932",
    "jobTitle": "Accountants",
    "location": {
      "id": "1",
      "key": "1",
      "name": "United States of America",
      "href": "/objects/company-config/location/1"
    },
    "department": {
      "id": "TS",
      "key": "29",
      "name": "Technical Services",
      "href": "/objects/company-config/department/29"
    },
    "manager": {
      "key": "4",
      "id": "MGR-CS",
      "name": "CS Dept - Manager",
      "href": "/objects/company-config/employee/4"
    },
    "birthDate": "1984-04-01",
    "startDate": "2021-04-30",
    "endDate": null,
    "status": "active",
    "employeeType": {
      "id": "Full Time",
      "key": "1",
      "href": "/objects/company-config/employee-type/1"
    },
    "gender": null,
    "terminationType": null,
    "name": "Mary",
    "primaryContact": {
      "mailingAddress": {
        "addressLine1": null,
        "addressLine2": null,
        "addressLine3": null,
        "city": null,
        "country": "United States",
        "isoCountryCode": "US",
        "postCode": null,
        "state": null
      },
      "URL1": null,
      "URL2": null,
      "companyName": null,
      "email1": "mvanitha@intacct.com",
      "email2": null,
      "fax": null,
      "firstName": "Mary",
      "id": "Mary",
      "lastName": "Vanitha",
      "middleName": null,
      "mobile": null,
      "pager": null,
      "phone1": null,
      "phone2": null,
      "prefix": null,
      "printAs": "Vanitha, Mary",
      "key": "270",
      "href": "/objects/company-config/contact/270"
    },
    "attachmentFolder": {
      "id": "JSmithEmployee",
      "key": "10",
      "href": "/objects/company-config/folder/10"
    },
    "defaultCurrency": "USD",
    "form1099": {
      "name": null,
      "type": null,
      "box": null
    },
    "earningType": {
      "key": "1",
      "id": "Salaries",
      "href": "/objects/company-config/earning-type/1"
    },
    "postActualCostWithVariance": false,
    "audit": {
      "createdDateTime": "2025-09-24T17:21:13Z",
      "modifiedDateTime": "2025-09-24T17:21:13Z",
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
      "id": 3,
      "name": "Health Care",
      "key": "1",
      "href": "/objects/company-config/class/1"
    },
    "defaultCustomer": {
      "id": null,
      "name": null,
      "key": null
    },
    "defaultItem": {
      "id": null,
      "name": null,
      "key": null
    },
    "defaultVendor": {
      "id": null,
      "name": null,
      "key": null
    },
    "defaultTimeAllocation": {
      "id": null,
      "key": null
    },
    "defaultExpenseDistribution": {
      "id": null,
      "key": null
    },
    "preferredPaymentMethod": "cash",
    "bankFile": {
      "paymentCountryCode": null,
      "paymentCurrency": null
    },
    "filePaymentService": "none",
    "ach": {
      "enabled": false,
      "bankRoutingNumber": null,
      "accountNumber": null,
      "accountType": null,
      "remittanceType": null
    },
    "sendAutomaticPaymentNotification": false,
    "isPlaceholderResource": false,
    "mergePaymentRequests": true,
    "employeePosition": {
      "key": null,
      "id": null
    },
    "webURL": "https://intacct.com/acct/ur.phtml?.r=ijVqUVXUX3TzexR2EcQNU3U7RuBoTavvJ5Pvp9qZZG0",
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "employeeRates": {
      "key": "116",
      "id": "116",
      "employee": {
        "key": "57",
        "id": "AllFields",
        "name": "Fields, All",
        "href": "/objects/company-config/employee/57"
      },
      "hourlyRate": "50.00",
      "annualSalary": null,
      "startDate": "2025-01-02",
      "endDate": null,
      "audit": {
        "createdDateTime": "2025-11-06T16:55:43Z",
        "modifiedDateTime": "2025-11-06T16:55:43Z",
        "createdByUser": {
          "key": "138",
          "id": "Admin2",
          "href": "/objects/company-config/user/138"
        },
        "createdBy": "138",
        "modifiedByUser": {
          "key": "138",
          "id": "Admin2",
          "href": "/objects/company-config/user/138"
        },
        "modifiedBy": "138"
      },
      "href": "/objects/company-config/employee-rate/116"
    },
    "positionSkills": {
      "key": "1",
      "id": "Surfer",
      "href": "/objects/projects/position-skill/1"
    },
    "bankFileSetup": [],
    "href": "/objects/company-config/employee/59"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalError": 0,
    "totalSuccess": 1
  }
}
```

## PATCH /objects/company-config/employee/{key}
_Update an employee_

**Request example — Update an employee:**
```json
{
  "status": "inactive",
  "endDate": "2023-04-01",
  "terminationType": "voluntary"
}
```
**Response 200 — Reference to updated employee:**
```json
{
  "ia::result": {
    "key": "52",
    "id": "Emp2",
    "href": "/objects/company-config/employee/52"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/company-config/employee/{key}
_Delete an employee_


## GET /objects/company-config/entity
_List entities_

**Response 200 — List entities:**
```json
{
  "ia::result": [
    {
      "key": "195",
      "id": "entity1692705208",
      "href": "/objects/company-config/entity/195"
    },
    {
      "key": "196",
      "id": "entity21692704288",
      "href": "/objects/company-config/entity/196"
    },
    {
      "key": "197",
      "id": "entity11692704288",
      "href": "/objects/company-config/entity/196"
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

## POST /objects/company-config/entity
_Create an entity_

**Request example — Create an entity:**
```json
{
  "id": "Hungary",
  "name": "Hungary",
  "defaultCountryForAddresses": "hungary",
  "operatingCountry": "hungary",
  "reportPrintAs": "Hungary",
  "weekStart": "monday",
  "contacts": {
    "primary": {
      "id": "-1-13S(V1-13S)"
    },
    "shipTo": {
      "id": "0000-1S(V0000-1S)"
    }
  },
  "manager": {
    "key": "14"
  },
  "texts": {
    "message": "Superior financial Applications. Real-time business visibility. Open, on-demand platform.",
    "marketing": "Intacct. A Better Way to Run Your Business",
    "footnote": "Hungary",
    "customTitle": "Hungary"
  },
  "isRoot": true,
  "businessDays": [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday"
  ],
  "weekendDays": [
    "saturday",
    "sunday"
  ],
  "taxId": "192354308",
  "startDate": "2023-01-12",
  "openBooksStartDate": "2023-10-01",
  "isLimitedEntity": false,
  "branding": {
    "logo": "UEsDBBQABgAIAAAAIQDfpNJsWgE"
  }
}
```
**Response 201 — Reference to new entity:**
```json
{
  "ia::result": {
    "key": "184",
    "id": "Hungary",
    "href": "/objects/company-config/entity/184"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/entity/{key}
_Get an entity_

**Response 200 — Get an entity:**
```json
{
  "ia::result": {
    "id": "entity1693567215",
    "key": "601",
    "name": "entity1693567215",
    "manager": {
      "name": "Supervisor",
      "id": "b.ruth",
      "key": "81",
      "href": "/objects/company-config/employee/81"
    },
    "contacts": {
      "primary": {
        "mailingAddress": {
          "addressLine1": "744 Edgewater Blvd",
          "addressLine2": "Suite 10",
          "addressLine3": "Industrial area",
          "city": "Kansas City",
          "state": "KS",
          "postCode": "66104",
          "country": "United States"
        },
        "id": "AMoore",
        "lastName": "Moore",
        "firstName": "Andy",
        "middleName": "Robert",
        "prefix": "Mr.",
        "printAs": "Andy Moore",
        "email1": "andy.moore@mycompany.com",
        "email2": "andy.moore@personal.com",
        "phone1": "9134598676",
        "phone2": "9133459867",
        "mobile": "9133132299",
        "pager": "9133132299",
        "fax": "9134598677",
        "URL1": "http://andy.exampledomain.com",
        "URL2": "http://andy.exampledomainsecond.com",
        "companyName": "Ecology Corp",
        "key": "237",
        "href": "/objects/company-config/contact/237"
      },
      "shipTo": {
        "mailingAddress": {
          "addressLine1": "300 Park Avenue",
          "addressLine2": "Suite 1400",
          "addressLine3": "Western industrial area",
          "city": "San Jose",
          "state": "California",
          "postCode": "95110",
          "country": "United States"
        },
        "id": "Vendor_A0000001",
        "lastName": "Smith",
        "firstName": "Sara",
        "middleName": "Sue",
        "prefix": "Ms.",
        "printAs": "Sara Smith",
        "email1": "ssmith@example.com",
        "email2": "sara@home.com",
        "phone1": "14085551212",
        "phone2": "14123321255",
        "mobile": "14085554420",
        "pager": "14085559987",
        "fax": "14085555309",
        "URL1": "https://smith.example.com",
        "URL2": "https://sarasue.example.com",
        "companyName": null,
        "key": "198",
        "href": "/objects/company-config/contact/198"
      },
      "legalCategory": "24 Fiduciary",
      "mainActivity": "10.3 Transformation and conservation of fruits and vegetables",
      "typeOfCompany": "03 Intermediate sized enterprises",
      "registeredCapital": 500,
      "valueAddedTaxRegime": "Monthly"
    },
    "startDate": "2020-01-01",
    "endDate": null,
    "status": "active",
    "audit": {
      "createdDateTime": "2023-09-01T11:20:19Z",
      "modifiedDateTime": "2023-09-01T11:20:19Z",
      "createdBy": "99",
      "modifiedBy": "99",
      "createdByUser": {
        "key": "99",
        "id": "Admin",
        "href": "/objects/company-config/user/99"
      },
      "modifiedByUser": {
        "key": "99",
        "id": "Admin",
        "href": "/objects/company-config/user/99"
      }
    },
    "federalId": "123456789",
    "firstFiscalMonth": "april",
    "baseCurrency": {
      "key": "24",
      "id": "AUD",
      "href": "/objects/company-config/txn-currency/24"
    },
    "weekStart": "monday",
    "interEntityPayableGLAccount": {
      "id": null,
      "accountNumber": null,
      "key": null
    },
    "interEntityReceivableGLAccount": {
      "id": "1",
      "accountNumber": 123436,
      "key": "1"
    },
    "texts": {
      "message": "Superior financial Applications. Real-time business visibility. Open, on-demand platform.",
      "marketing": "Intacct. A Better Way to Run Your Business",
      "footnote": "Net 30 days",
      "reportPrintAs": "California"
    },
    "isRoot": false,
    "vendor": {
      "name": "Pac bell",
      "id": "V-00014"
    },
    "customer": {
      "id": "15",
      "name": "Logic Solutions"
    },
    "enableInterEntityRelationships": false,
    "customTitle": "California",
    "businessDays": [
      "SUNDAY",
      "MONDAY",
      "TUESDAY",
      "WEDNESDAY",
      "THURSDAY"
    ],
    "weekendDays": [
      "FRIDAY",
      "SATURDAY"
    ],
    "firstTaxMonth": "january",
    "taxId": "192354308",
    "siret": "01234567890123456789",
    "defaultCountryForAddresses": "westernSahara",
    "openBooksStartDate": "1990-01-01",
    "legalContact": {
      "enableOnTaxForms": false,
      "name": "Expert Sage Intacct LTD",
      "address": {
        "address1": "300 Park Avenue",
        "address2": "Suite 1400",
        "address3": "Western industrial area",
        "city": "San Jose",
        "state": "California",
        "zipCode": "95110",
        "country": "United States",
        "countryCode": "us"
      },
      "tpar": {
        "contact": {
          "name": "John Doe",
          "phone": "1022223333",
          "fax": "1009288888",
          "email": "contact@example.com"
        },
        "branchNumber": "001"
      },
      "enableOnTPAR": false
    },
    "operatingCountry": "france",
    "taxSolution": {
      "key": "23",
      "id": "23",
      "taxMethod": "Advanced tax",
      "href": "/objects/tax/tax-solution/23"
    },
    "isPartialExempt": false,
    "isDefaultPartialExempt": false,
    "unrecoverableTaxAccount": {
      "id": null
    },
    "accountingType": "entity",
    "statutoryReportingPeriodDate": "2021-01-01",
    "isLimitedEntity": false,
    "branding": {
      "logo": "UEsDBBQABgAIAAAAIQDfpNJsWgE"
    },
    "href": "/objects/company-config/entity/601"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/entity/{key}
_Update an entity_

**Request example — Update an entity:**
```json
{
  "endDate": "2023-12-31",
  "status": "inactive"
}
```
**Response 200 — Reference to updated entity:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "entity1693567215",
    "href": "/objects/company-config/entity/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/entity/{key}
_Delete an entity_


## GET /objects/company-config/exchange-rate
_List exchange rates_

**Response 200 — List exchange rates:**
```json
{
  "ia::result": [
    {
      "key": "40",
      "id": "40",
      "href": "/objects/company-config/exchange-rate/40"
    },
    {
      "key": "41",
      "id": "41",
      "href": "/objects/company-config/exchange-rate/41"
    },
    {
      "key": "42",
      "id": "42",
      "href": "/objects/company-config/exchange-rate/42"
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

## POST /objects/company-config/exchange-rate
_Create an exchange rate_

**Request example — Create an exchange rate:**
```json
{
  "exchangeRateType": {
    "key": "4"
  },
  "fromCurrency": "USD",
  "toCurrency": "CAD",
  "lines": [
    {
      "effectiveStartDate": "2025-08-15",
      "rate": 2
    },
    {
      "effectiveStartDate": "2025-09-16",
      "rate": 3,
      "reciprocalRate": 0.55
    }
  ]
}
```
**Response 201 — Reference to new exchange rate:**
```json
{
  "ia::result": {
    "id": "40",
    "key": "40",
    "href": "/objects/company-config/exchange-rate/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/exchange-rate-line
_List exchange rate lines_

**Response 200 — List exchange rate lines:**
```json
{
  "ia::result": [
    {
      "key": "85",
      "id": "85",
      "href": "/objects/company-config/exchange-rate-line/85"
    },
    {
      "key": "86",
      "id": "86",
      "href": "/objects/company-config/exchange-rate-line/86"
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

## POST /objects/company-config/exchange-rate-line
_Create an exchange rate line_

**Request example — Create an exchange rate line:**
```json
{
  "exchangeRate": {
    "key": "4"
  },
  "effectiveStartDate": "2025-01-30",
  "rate": 1.555
}
```
**Response 201 — Reference to new exchange rate line:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "23",
    "href": "/objects/company-config/exchange-rate-line/23"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/exchange-rate-line/{key}
_Get an exchange rate line_

**Response 200 — Get an exchange rate line:**
```json
{
  "ia::result": {
    "id": "23",
    "key": "23",
    "exchangeRate": {
      "id": "4",
      "key": "4",
      "href": "/objects/company-config/exchange-rate/4"
    },
    "effectiveStartDate": "2025-01-30",
    "rate": 1.555,
    "reciprocalRate": 0.64308682,
    "audit": {
      "createdDateTime": "2025-09-25T17:05:44Z",
      "modifiedDateTime": "2025-09-25T17:05:44Z",
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
    "href": "/objects/company-config/exchange-rate-line/23"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/exchange-rate-line/{key}
_Update an exchange rate line_

**Request example — Update an exchange rate line:**
```json
{
  "rate": 1,
  "reciprocalRate": 0.5
}
```
**Response 200 — Reference to updated exchange rate line:**
```json
{
  "ia::result": {
    "key": "87",
    "id": "87",
    "href": "/objects/company-config/exchange-rate-line/87"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/exchange-rate-line/{key}
_Delete an exchange rate line_


## GET /objects/company-config/exchange-rate-type
_List exchange rate types_

**Response 200 — List exchange rate types:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/exchange-rate-type/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/company-config/exchange-rate-type/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/company-config/exchange-rate-type/3"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/company-config/exchange-rate-type/4"
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

## POST /objects/company-config/exchange-rate-type
_Create an exchange rate type_

**Request example — Create an exchange rate type:**
```json
{
  "name": "CUS-Rate",
  "isDefault": true
}
```
**Response 201 — Reference to new exchange rate type:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/company-config/exchange-rate-type/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/exchange-rate-type/{key}
_Get an exchange rate type_

**Response 200 — Get an exchange rate type:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "name": "CUS-Rate",
    "isDefault": false,
    "audit": {
      "createdDateTime": "2025-06-28T20:54:10Z",
      "modifiedDateTime": "2025-06-28T20:54:10Z",
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
    "href": "/objects/company-config/exchange-rate-type/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/exchange-rate-type/{key}
_Update an exchange rate type_

**Request example — Update an exchange rate type:**
```json
{
  "isDefault": true
}
```
**Response 200 — Reference to updated exchange rate type:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "href": "/objects/company-config/exchange-rate-type/5"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/exchange-rate-type/{key}
_Delete an exchange rate type_


## GET /objects/company-config/exchange-rate/{key}
_Get an exchange rate_

**Response 200 — Get an exchange rate:**
```json
{
  "ia::result": {
    "id": "40",
    "key": "40",
    "exchangeRateType": {
      "key": "4",
      "id": "4",
      "name": "USD TO CAD",
      "href": "/objects/company-config/exchange-rate-type/4"
    },
    "fromCurrency": "USD",
    "toCurrency": "CAD",
    "audit": {
      "createdDateTime": "2025-09-16T17:16:09Z",
      "modifiedDateTime": "2025-09-16T17:16:09Z",
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
    "lines": [
      {
        "id": "84",
        "key": "84",
        "exchangeRate": {
          "id": "40",
          "key": "40",
          "href": "/objects/company-config/exchange-rate/40"
        },
        "effectiveStartDate": "2025-08-15",
        "rate": 2,
        "reciprocalRate": 0.5,
        "audit": {
          "createdDateTime": "2025-09-16T17:16:09Z",
          "modifiedDateTime": "2025-09-16T17:16:09Z",
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
          }
        },
        "href": "/objects/company-config/exchange-rate-line/84"
      },
      {
        "id": "85",
        "key": "85",
        "exchangeRate": {
          "id": "40",
          "key": "40",
          "href": "/objects/company-config/exchange-rate/40"
        },
        "effectiveStartDate": "2025-09-16",
        "rate": 3,
        "reciprocalRate": 0.55,
        "audit": {
          "createdDateTime": "2025-09-16T17:16:09Z",
          "modifiedDateTime": "2025-09-16T17:16:09Z",
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
          }
        },
        "href": "/objects/company-config/exchange-rate-line/85"
      }
    ],
    "href": "/objects/company-config/exchange-rate/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/exchange-rate/{key}
_Update an exchange rate_

**Request example — Update an exchange rate:**
```json
{
  "fromCurrency": "INR",
  "lines": [
    {
      "key": "85",
      "rate": 4,
      "reciprocalRate": 2.5555
    },
    {
      "effectiveStartDate": "2025-11-18",
      "rate": 5.5
    }
  ]
}
```
**Response 200 — Reference to updated exchange rate:**
```json
{
  "ia::result": {
    "id": "40",
    "key": "40",
    "href": "/objects/company-config/exchange-rate/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/exchange-rate/{key}
_Delete an exchange rate_


## GET /objects/company-config/folder
_List folders_

**Response 200 — List folders:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Bills",
      "href": "/objects/company-config/folder/1"
    },
    {
      "key": "2",
      "id": "Credits",
      "href": "/objects/company-config/folder/2"
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

## POST /objects/company-config/folder
_Create a folder_

**Request example — Create a folder:**
```json
{
  "id": "2024 Bills",
  "description": "Annual bills folder",
  "status": "active"
}
```
**Response 201 — Reference to new folder:**
```json
{
  "ia::result": {
    "key": "28",
    "id": "2024 Bills",
    "href": "/objects/company-config/folder/28"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/folder/{key}
_Get a folder_

**Response 200 — Get a folder:**
```json
{
  "ia::result": {
    "key": "28",
    "id": "2024 Bills",
    "parent": {
      "id": "Bills",
      "key": "2",
      "href": "/objects/company-config/folder/2"
    },
    "description": "Annual bills folder",
    "audit": {
      "createdDate": "2023-04-01",
      "createdBy": "Admin",
      "modifiedBy": "Admin",
      "modifiedDate": "2023-04-01"
    },
    "status": "active",
    "hasSubfolders": false,
    "hasAttachments": true,
    "href": "/objects/company-config/folder/28"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/folder/{key}
_Update a folder_

**Request example — Update folder description:**
```json
{
  "description": "2024 bills and dunning notices"
}
```
**Response 200 — Reference to updated folder:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Bills",
    "href": "/objects/company-config/folder/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/folder/{key}
_Delete a folder_


## GET /objects/company-config/inter-entity-account-mapping
_List inter-entity account mappings_

**Response 200 — List inter-entity account mappings:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/inter-entity-account-mapping/1"
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

## GET /objects/company-config/inter-entity-account-mapping/{key}
_Get an inter-entity account mapping_

**Response 200 — Get an inter-entity account mapping:**
```json
{
  "ia::result": {
    "id": "1",
    "key": "1",
    "interEntityAccountMappingPlan": "advanced",
    "interEntityAdvancedMaps": [
      {
        "interEntityAccountMapping": {
          "id": "1",
          "key": "1",
          "href": "/objects/company-config/inter-entity-account-mapping/1"
        },
        "id": "21",
        "key": "21",
        "sourceEntity": {
          "id": "1",
          "key": "1",
          "name": "United States of America",
          "status": "active",
          "href": "/objects/company-config/entity/1"
        },
        "targetEntity": {
          "id": "2",
          "key": "2",
          "name": "India",
          "status": "active",
          "href": "/objects/company-config/entity/2"
        },
        "interEntityPayableGLAccount": {
          "key": "10",
          "id": "1001",
          "name": "CitiBank",
          "href": "/objects/general-ledger/account/10"
        },
        "interEntityReceivableGLAccount": {
          "key": "9",
          "id": "1000",
          "name": "Bank of America A/c.",
          "href": "/objects/general-ledger/account/9"
        },
        "href": "/objects/company-config/inter-entity-advanced-map/21"
      },
      {
        "interEntityAccountMapping": {
          "id": "1",
          "key": "1",
          "href": "/objects/company-config/inter-entity-account-mapping/1"
        },
        "id": "22",
        "key": "22",
        "sourceEntity": {
          "id": "2",
          "key": "2",
          "name": "India",
          "status": "active",
          "href": "/objects/company-config/entity/2"
        },
        "targetEntity": {
          "id": "1",
          "key": "1",
          "name": "United States of America",
          "status": "active",
          "href": "/objects/company-config/entity/1"
        },
        "interEntityPayableGLAccount": {
          "key": "11",
          "id": "1002",
          "name": "HSBC - GBP",
          "href": "/objects/general-ledger/account/11"
        },
        "interEntityReceivableGLAccount": {
          "key": "11",
          "id": "1002",
          "name": "HSBC - GBP",
          "href": "/objects/general-ledger/account/11"
        },
        "href": "/objects/company-config/inter-entity-advanced-map/22"
      }
    ],
    "href": "/objects/company-config/inter-entity-account-mapping/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/inter-entity-account-mapping/{key}
_Update an inter-entity account mapping_

**Request example — Update an inter-entity account mapping:**
```json
{
  "key": "1",
  "interEntityAdvancedMaps": [
    {
      "key": "21",
      "sourceEntity": {
        "key": "1"
      },
      "targetEntity": {
        "key": "2"
      },
      "interEntityPayableGLAccount": {
        "key": "10"
      },
      "interEntityReceivableGLAccount": {
        "key": "11"
      }
    },
    {
      "key": "22",
      "sourceEntity": {
        "key": "2"
      },
      "targetEntity": {
        "key": "1"
      },
      "interEntityPayableGLAccount": {
        "key": "13"
      },
      "interEntityReceivableGLAccount": {
        "key": "12"
      }
    }
  ]
}
```
**Response 200 — Reference to the inter-entity account mapping:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/company-config/inter-entity-account-mapping/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/inter-entity-advanced-map
_List inter-entity advanced maps_

**Response 200 — List inter-entity advanced maps:**
```json
{
  "ia::result": [
    {
      "key": "21",
      "id": "21",
      "href": "/objects/company-config/inter-entity-advanced-map/21"
    },
    {
      "key": "22",
      "id": "22",
      "href": "/objects/company-config/inter-entity-advanced-map/22"
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

## GET /objects/company-config/inter-entity-advanced-map/{key}
_Get an inter-entity advanced map._

**Response 200 — Get an inter-entity advanced map:**
```json
{
  "ia::result": {
    "interEntityAccountMapping": {
      "id": "1",
      "key": "1",
      "href": "/objects/company-config/inter-entity-account-mapping/1"
    },
    "id": "21",
    "key": "21",
    "sourceEntity": {
      "id": "1",
      "key": "1",
      "name": "United States of America",
      "status": "active",
      "href": "/objects/company-config/entity/1"
    },
    "targetEntity": {
      "id": "2",
      "key": "2",
      "name": "India",
      "status": "active",
      "href": "/objects/company-config/entity/2"
    },
    "interEntityPayableGLAccount": {
      "key": "10",
      "id": "1001",
      "name": "CitiBank",
      "href": "/objects/general-ledger/account/10"
    },
    "interEntityReceivableGLAccount": {
      "key": "11",
      "id": "1002",
      "name": "HSBC - GBP",
      "href": "/objects/general-ledger/account/11"
    },
    "href": "/objects/company-config/inter-entity-advanced-map/21"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/inter-entity-advanced-map/{key}
_Delete an inter-entity advanced map_


## GET /objects/company-config/inter-entity-basic-map
_List inter-entity basic maps_

**Response 200 — List inter-entity basic maps:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/inter-entity-basic-map/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/company-config/inter-entity-basic-map/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/company-config/inter-entity-basic-map/3"
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

## GET /objects/company-config/inter-entity-basic-map/{key}
_Get an inter-entity basic map_

**Response 200 — Get an inter-entity basic map:**
```json
{
  "ia::result": {
    "interEntityAccountMapping": {
      "id": "1",
      "key": "1",
      "href": "/objects/company-config/inter-entity-account-mapping/1"
    },
    "key": "1",
    "id": "1",
    "entity": {
      "id": "1",
      "key": "1",
      "name": "United States of America",
      "status": "active",
      "href": "/objects/company-config/entity/1"
    },
    "interEntityPayableGLAccount": {
      "key": "10",
      "id": "1001",
      "name": "CitiBank",
      "href": "/objects/general-ledger/account/10"
    },
    "interEntityReceivableGLAccount": {
      "key": "9",
      "id": "1000",
      "name": "Bank of America A/c.",
      "href": "/objects/general-ledger/account/9"
    },
    "href": "/objects/company-config/inter-entity-basic-map/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/inter-entity-basic-map/{key}
_Delete an inter-entity basic map_


## GET /objects/company-config/location
_List locations_

**Response 200 — List locations:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "US-PNW",
      "href": "/objects/company-config/location/1"
    },
    {
      "key": "96",
      "id": "US-EAST",
      "href": "/objects/company-config/location/96"
    },
    {
      "key": "21",
      "id": "US-SOUTH",
      "href": "/objects/company-config/location/21"
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

## POST /objects/company-config/location
_Create a location_

**Request example — Create a single location:**
```json
{
  "id": "loc22",
  "name": "22-India",
  "description": "All India offices",
  "status": "active"
}
```
**Request example — Create a child location:**
```json
{
  "id": "loc227",
  "name": "Bangalore",
  "description": "Bangalore sales office",
  "status": "active",
  "parent": {
    "id": "loc22"
  }
}
```
**Response 201 — New location created:**
```json
{
  "ia::result": {
    "key": "234",
    "id": "22-India",
    "href": "/objects/company-config/location/234"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/company-config/location-group
_List location groups_

**Response 200 — List of location groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "CO",
      "href": "/objects/company-config/location-group/1"
    },
    {
      "key": "2",
      "id": "CA",
      "href": "/objects/company-config/location-group/2"
    },
    {
      "key": "3",
      "id": "CT",
      "href": "/objects/company-config/location-group/3"
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

## POST /objects/company-config/location-group
_Create a Location group_

**Request example — Creates a location group of type all:**
```json
{
  "id": "WA",
  "name": "Washington",
  "description": "Washington State",
  "groupType": "all",
  "memberFilter": {
    "object": "company-config/location",
    "filterExpression": "and",
    "filters": [
      {
        "$contains": {
          "id": "WA"
        }
      }
    ],
    "orderBy": [
      {
        "name": "asc"
      }
    ]
  }
}
```
**Request example — Creates a location group of type specific:**
```json
{
  "id": "IN",
  "name": "India",
  "description": "India offices",
  "groupType": "specific",
  "groupMembers": [
    {
      "location": {
        "id": "New Delhi"
      }
    }
  ]
}
```
**Response 201 — Reference to new location group:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "IN",
    "href": "/objects/company-config/location-group/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/location-group-member
_List location group members_

**Response 200 — List of Location group Members:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/location-group-member/1"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/company-config/location-group-member/3"
    },
    {
      "key": "13",
      "id": "13",
      "href": "/objects/company-config/location-group-member/13"
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

## GET /objects/company-config/location-group-member/{key}
_Get a location group member_

**Response 200 — Details of the location group member:**
```json
{
  "ia::result": {
    "key": "13",
    "id": "13",
    "locationGroup": {
      "id": "6",
      "key": "6",
      "href": "/objects/company-config/location-group/6"
    },
    "location": {
      "key": "1",
      "id": "1",
      "name": "United States of America",
      "href": "/objects/company-config/location/1"
    },
    "sortOrder": 0,
    "audit": {
      "createdDateTime": "2018-05-01T22:37:18Z",
      "modifiedDateTime": "2018-05-01T22:37:18Z",
      "createdBy": "1",
      "modifiedBy": "1"
    },
    "href": "/objects/company-config/location-group-member/13"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/location-group/{key}
_Get a location group_

**Response 200 — Details of the location group:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Top Locations",
    "name": "Top Level Locations",
    "description": "Top Level Locations",
    "groupType": "specific",
    "primaryContact": {
      "key": "211",
      "id": "1099 Int",
      "href": "/objects/company-config/contact/211"
    },
    "memberFilter": {
      "object": "company-config/location",
      "filterExpression": "and",
      "orderBy": [
        {
          "name": "asc"
        }
      ]
    },
    "audit": {
      "createdDateTime": "2023-08-16T13:26:56Z",
      "modifiedDateTime": "2023-08-16T13:26:56Z",
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
    "groupMembers": [
      {
        "key": "1",
        "id": "1",
        "locationGroup": {
          "key": "1",
          "href": "/objects/company-config/location-group/1"
        },
        "location": {
          "id": "1",
          "key": "1",
          "name": "United States of America",
          "href": "/objects/company-config/location/1"
        },
        "audit": {
          "createdDateTime": "2023-08-21T09:54:05Z",
          "modifiedDateTime": "2023-08-21T09:54:05Z",
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
        "href": "/objects/company-config/location-group-member/1"
      },
      {
        "key": "2",
        "id": "2",
        "locationGroup": {
          "key": "2",
          "href": "/objects/company-config/location-group/2"
        },
        "location": {
          "id": "3",
          "key": "3",
          "name": "United Kingdom",
          "href": "/objects/company-config/location/3"
        },
        "audit": {
          "createdDateTime": "2023-08-21T09:54:05Z",
          "modifiedDateTime": "2023-08-21T09:54:05Z",
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
        "href": "/objects/company-config/location-group-member/2"
      }
    ],
    "href": "/objects/company-config/location-group/15"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/location-group/{key}
_Update a Location group_

**Request example — Updates a Location group:**
```json
{
  "description": "My Top Locations america",
  "memberFilter": {
    "object": "company-config/location",
    "filterExpression": "and",
    "filters": [
      {
        "$eq": {
          "name": "United States of America"
        }
      }
    ],
    "orderBy": [
      {
        "name": "asc"
      }
    ]
  }
}
```
**Response 200 — Reference to updated location group:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "My Locations new",
    "href": "/objects/company-config/location-group/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/location-group/{key}
_Delete a Location group_


## GET /objects/company-config/location/{key}
_Get a location_

**Response 200 — Get a location:**
```json
{
  "ia::result": {
    "id": "WEN",
    "key": "6",
    "name": "Wenatchee",
    "parent": {
      "id": "PNW--Pacific Northwest",
      "key": "5",
      "name": "Pacific Northwest",
      "locationType": "location",
      "href": "/objects/company-config/location/5"
    },
    "manager": {
      "name": "miller, dan",
      "id": "EE-0000123--miller, dan",
      "key": "2",
      "href": "/objects/company-config/employee/2"
    },
    "contacts": {
      "primary": {
        "mailingAddress": {
          "addressLine1": "900 Cherry Avenue, #300",
          "addressLine2": "Suite 1400",
          "addressLine3": "East industrial area",
          "city": "Seattle",
          "country": "United States",
          "postCode": "98066",
          "state": "WA"
        },
        "URL1": "https://myinsideoutcompany.com",
        "URL2": "https://anotherinsideoutcompany.com",
        "companyName": "InsideOut Technologies, Inc",
        "email1": "smith.john@sage.com",
        "email2": "smith@sage.com",
        "fax": "14085555309",
        "firstName": "John",
        "id": "InsideOut Technologies, Inc",
        "lastName": "Smith",
        "middleName": "Archibald",
        "mobile": "14085554420",
        "pager": "14085559987",
        "phone1": "14085551212",
        "phone2": "14085559876",
        "prefix": "Mr",
        "printAs": "InsideOut Technologies, Inc",
        "key": "984",
        "href": "/objects/company-config/contact/984"
      },
      "shipTo": {
        "mailingAddress": {
          "addressLine1": "Rose Avenue",
          "addressLine2": "Suite 1405",
          "addressLine3": "Western industrial area",
          "city": "Seattle",
          "country": "United States",
          "postCode": "98066",
          "state": "WA"
        },
        "URL1": "https://mycompany.com",
        "URL2": "https://anothercompany.com",
        "companyName": "AlcoSoft Inc",
        "email1": "john.smith@sage.com",
        "email2": "john@sage.com",
        "fax": "14085555309",
        "firstName": "John",
        "id": "AlcoSoft Inc",
        "lastName": "Smith",
        "middleName": "Archibald",
        "mobile": "14085554420",
        "pager": "14085559987",
        "phone1": "14085551212",
        "phone2": "14085559876",
        "prefix": "Mr",
        "printAs": "AlcoSoft Inc",
        "key": "985"
      }
    },
    "startDate": "2021-01-01",
    "endDate": "2021-04-01",
    "status": "active",
    "audit": {
      "createdDateTime": "2022-02-11T09:07:07Z",
      "modifiedDateTime": "2022-02-11T09:07:07Z",
      "createdBy": "110",
      "modifiedBy": "110",
      "createdByUser": {
        "key": "110",
        "id": "Admin",
        "href": "/objects/company-config/user/110"
      },
      "modifiedByUser": {
        "key": "110",
        "id": "Admin",
        "href": "/objects/company-config/user/110"
      }
    },
    "reportTitle": "Seattle Sales Office",
    "printAs": "Lyon-France",
    "entity": {
      "id": "GM",
      "key": "11",
      "name": "Gulf of Mexico",
      "href": "/objects/company-config/entity/11"
    },
    "baseCurrency": "GBP",
    "taxId": "US4321112",
    "businessId": "874563210",
    "href": "/objects/company-config/location/102"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/location/{key}
_Update a location_

**Request example — Update location contacts:**
```json
{
  "manager": {
    "key": "12"
  },
  "contacts": {
    "primary": {
      "id": "john.doe"
    },
    "shipTo": {
      "id": "jane.daw"
    }
  }
}
```
**Response 200 — Location updated:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "SW",
    "href": "/objects/company-config/location/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/location/{key}
_Delete a location_


## GET /objects/company-config/multi-entity-preference/{key}
_Get multi-entity preferences_

**Response 200 — Get multi-entity preferences:**
```json
{
  "ia::result": {
    "enableMultipleBaseCurrency": true,
    "approvalCurrency": "CAD",
    "isForm1099": false,
    "restrictions": {
      "disableEntitySlideIn": false,
      "restrictSubledgerTxnToEntity": false,
      "restrictGLTxnToEntity": false,
      "enableCustomerRestrictions": true,
      "enableVendorRestrictions": true,
      "enableCheckingAccountRestrictions": false,
      "enableSavingsAccountRestrictions": false
    },
    "interEntityAccountMappingPlan": "basic",
    "interEntityTxns": {
      "enableForJournalEntry": true,
      "manuallyBalanceSubledgerTxns": false,
      "manuallyBalanceSubledgerCredits": true,
      "creditsJournal": {
        "key": "10",
        "id": "IEP",
        "name": "Inter Entity Payable",
        "href": "/objects/general-ledger/journal/10"
      }
    },
    "balanceJournalEntryBy": "entity",
    "limitAPCredit": true,
    "limitARCredit": false,
    "isModuleConfigured": true,
    "enableAffiliateEntity": true,
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
    "key": "setup",
    "href": "/services/company-config/preferences/multi-entity"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/multi-entity-preference/{key}
_Update multi-entity preferences_

**Request example — Update multi-entity preferences:**
```json
{
  "restrictions": {
    "enableCheckingAccountRestrictions": true
  }
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

## GET /objects/company-config/order-entry-preference/{key}
_Get an Order Entry preference_


## PATCH /objects/company-config/order-entry-preference/{key}
_Update an Order Entry preference_

**Request example — Enable display payment status on transaction:**
```json
{
  "displayPaymentStatus": true,
  "enableDraftMode": false
}
```
**Response 200 — Reference to updated Order Entry preference:**
```json
{
  "ia::result": {
    "key": "setup",
    "href": "/objects/company-config/order-entry-preference/setup"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/payment-provider-notification
_List payment provider notifications_

**Response 200 — List payment provider notifications:**
```json
{
  "ia::result": [
    {
      "key": "29",
      "id": "29",
      "href": "/objects/company-config/payment-provider-notification/29"
    },
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/payment-provider-notification/1"
    },
    {
      "key": "28",
      "id": "28",
      "href": "/objects/company-config/payment-provider-notification/28"
    },
    {
      "key": "5",
      "id": "5",
      "href": "/objects/company-config/payment-provider-notification/5"
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

## GET /objects/company-config/payment-provider-notification/{key}
_Get a payment provider notification_

**Response 200 — Details of the payment-provider-notification:**
```json
{
  "ia::result": [
    {
      "key": "449",
      "id": "449",
      "notificationGUID": "c391804c-d1ab-4527-bafc-0086788d9ee7",
      "notificationType": "BatchPatched",
      "notificationBody": "{\\\"type\\\":\\\"BatchPatched\\\",\\\"notificationParties\\\":{\\\"organisationId\\\":\\\"32574d23-8181-4bef-904a-85338044fedd\\\",\\\"companyId\\\":\\\"be368f13-41dd-4ac5-bf34-1b17910a5db5\\\",\\\"applicationId\\\":\\\"sage.intacct\\\",\\\"subscriptionId\\\":\\\"46f2cc63-3f68-484e-8ecd-535abb4a2c11\\\",\\\"externalOrganisationId\\\":\\\"08978319B0B7EF5BE0637610E20A576E\\\",\\\"externalCompanyId\\\":\\\"0\\\"},\\\"resource\\\":{\\\"id\\\":\\\"c391804c-d1ab-4527-bafc-0086788d9ee7\\\",\\\"type\\\":\\\"batchpayments\\\",\\\"batchpayment\\\":{\\\"data\\\":{\\\"status\\\":\\\"Processing\\\",\\\"extendedStatus\\\":\\\"Reconcile\\\",\\\"extendedStatusDetail\\\":\\\"Payment.\\\",\\\"providerReference\\\":\\\"16488223\\\",\\\"creditorLocalInstrument\\\":\\\"ACH\\\",\\\"fundingId\\\":\\\"1336062\\\",\\\"payments\\\":[{\\\"paymentId\\\":\\\"c391804c-d1ab-4527-bafc-0086788d9ee7-00000\\\",\\\"status\\\":\\\"None\\\",\\\"providerReference\\\":\\\"16488223\\\",\\\"creditorLocalInstrument\\\":\\\"ACH\\\",\\\"fundingId\\\":\\\"1336062\\\",\\\"paymentCompletedDate\\\":\\\"2024-05-18T01:05:16Z\\\"}]}}}}",
      "status": "failed",
      "errorDescription": "Unable to update the payment request record, RECORDNO:75310",
      "audit": {
        "createdDateTime": "2024-05-24T03:09:21Z",
        "modifiedDateTime": "2024-05-24T06:31:58Z",
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
      "href": "/objects/company-config/payment-provider-notification/449"
    }
  ],
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess\"": 1,
    "totalError\"": 0
  }
}
```

## GET /objects/company-config/permission
_List permissions_

**Response 200 — List permissions:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/permission/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/company-config/permission/2"
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

## GET /objects/company-config/permission/{key}
_Get a permission_

**Response 200 — Get a permission:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "module": "myAccounting",
    "name": "switchToMyAccounting",
    "permissionGroup": "activitiesAndLists",
    "allowedAccessRights": [
      "list"
    ],
    "href": "/objects/company-config/permission/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/purchasing-preference/{key}
_Get a Purchasing preference_


## PATCH /objects/company-config/purchasing-preference/{key}
_Update a Purchasing preference_

**Request example — Enable display payments status on transaction:**
```json
{
  "displayPaymentStatus": true
}
```
**Response 200 — Reference to updated purchasing preference:**
```json
{
  "ia::result": {
    "key": "setup",
    "href": "/objects/company-config/purchasing-preference/setup"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/role
_List roles_

**Response 200 — List roles:**
```json
{
  "ia::result": [
    {
      "key": "470",
      "id": "::SYS::Multi Entity Shared-ROLE-FOR - Admin",
      "href": "/objects/company-config/role/470"
    },
    {
      "key": "471",
      "id": "::SYS::Multi Entity Shared-ROLE-FOR - BTI",
      "href": "/objects/company-config/role/471"
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

## POST /objects/company-config/role
_Create a role_

**Request example — Create a role:**
```json
{
  "id": "Admins",
  "description": "Administrator role with permissions",
  "roleType": "enterprise",
  "applyTo": "loginAndSlideIn",
  "rolePermissionAssignments": [
    {
      "permission": {
        "id": "253"
      },
      "accessRights": [
        "list",
        "readonly"
      ]
    },
    {
      "permission": {
        "id": "207"
      },
      "accessRights": [
        "list",
        "readonly",
        "add",
        "modify",
        "delete"
      ]
    }
  ],
  "customRolePermissionAssignments": [
    {
      "application": {
        "key": "10004",
        "permissions": [
          {
            "name": "Org Department",
            "group": "objects"
          }
        ]
      },
      "allowedAccessRights": [
        "list",
        "readonly",
        "modify"
      ]
    }
  ],
  "agentRolePermissionAssignments": [
    {
      "agent": {
        "key": "9030801000000002",
        "permissions": [
          {
            "name": "Convert an SCM document to the specified transaction type",
            "group": "agents"
          }
        ]
      },
      "allowedAccessRights": [
        "run"
      ]
    }
  ]
}
```
**Response 201 — Reference to new role:**
```json
{
  "ia::result": {
    "key": "470",
    "id": "Admins",
    "href": "/objects/company-config/role/470"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/role-permission-assignment
_List role permission assignments_

**Response 200 — List role permission assignments:**
```json
{
  "ia::result": [
    {
      "key": "156434",
      "id": "156434",
      "href": "/objects/company-config/role-permission-assignment/156434"
    },
    {
      "key": "156435",
      "id": "156435",
      "href": "/objects/company-config/role-permission-assignment/156435"
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

## GET /objects/company-config/role-permission-assignment/{key}
_Get a role permission assignment_

**Response 200 — Get a role permission assignment:**
```json
{
  "ia::result": {
    "key": "1748",
    "id": "1748",
    "role": {
      "key": "528",
      "id": "::SYS::Multi Entity Shared-ROLE-FOR - EMP4-US",
      "href": "/objects/company-config/role/528"
    },
    "permission": {
      "key": "3295",
      "id": "3295",
      "name": "coverLetters",
      "module": "company",
      "href": "/objects/company-config/permission/3295"
    },
    "accessRights": [
      "list",
      "readonly",
      "add",
      "modify",
      "delete"
    ],
    "audit": {
      "createdDateTime": "2024-02-15T11:39:04Z",
      "modifiedDateTime": "2024-02-15T11:39:04Z",
      "createdBy": "51",
      "modifiedBy": "51",
      "createdByUser": {
        "key": "51",
        "id": "Admin",
        "href": "/objects/company-config/user/51"
      },
      "modifiedByUser": {
        "key": "51",
        "id": "Admin",
        "href": "/objects/company-config/user/51"
      }
    },
    "href": "/objects/company-config/role-permission-assignment/1748"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/role-permission-assignment/{key}
_Update a role permission assignment_

**Request example — Updates a role-permission-assignment:**
```json
{
  "permission": {
    "key": "3295"
  },
  "accessRights": [
    "list",
    "readonly",
    "add",
    "modify"
  ]
}
```
**Response 200 — Reference to updated role-permission-assignment:**
```json
{
  "ia::result": {
    "key": "470",
    "id": "470",
    "href": "/objects/company-config/role/470"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/role-user-group-map
_List role user group maps_

**Response 200 — List role user group maps:**
```json
{
  "ia::result": [
    {
      "key": "761",
      "id": "761",
      "href": "/objects/company-config/role-user-group-map/761"
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

## GET /objects/company-config/role-user-group-map/{key}
_Get a role user group map_

**Response 200 — Role user group map details:**
```json
{
  "ia::result": {
    "key": "761",
    "id": "761",
    "role": {
      "key": "805",
      "id": "::SYS::Multi Entity Shared-ROLE",
      "href": "/objects/company-config/role/805"
    },
    "userGroup": {
      "key": "1",
      "id": "Bypass group",
      "href": "/objects/company-config/user-group/1"
    },
    "audit": {
      "createdDateTime": "2024-02-15T11:39:04Z",
      "modifiedDateTime": "2024-02-15T11:39:04Z",
      "createdBy": "51",
      "modifiedBy": "51",
      "createdByUser": {
        "key": "51",
        "id": "Admin",
        "href": "/objects/company-config/user/51"
      },
      "modifiedByUser": {
        "key": "51",
        "id": "Admin",
        "href": "/objects/company-config/user/51"
      }
    },
    "href": "/objects/company-config/role-user-group-map/761"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/role-user-map
_List role user maps_

**Response 200 — List role user maps:**
```json
{
  "ia::result": [
    {
      "key": "618",
      "id": "618",
      "href": "/objects/company-config/role-user-map/618"
    },
    {
      "key": "621",
      "id": "621",
      "href": "/objects/company-config/role-user-map/621"
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

## GET /objects/company-config/role-user-map/{key}
_Get a role user map_

**Response 200 — Get a role user map:**
```json
{
  "ia::result": {
    "key": "618",
    "id": "618",
    "role": {
      "key": "740",
      "id": "::SYS::Multi Entity Shared-ROLE-FOR - BTI",
      "href": "/objects/company-config/role/740"
    },
    "user": {
      "key": "4",
      "id": "BTI",
      "href": "/objects/company-config/user/4"
    },
    "audit": {
      "createdDateTime": "2024-02-15T11:39:04Z",
      "modifiedDateTime": "2024-02-15T11:39:04Z",
      "createdBy": "51",
      "modifiedBy": "51",
      "createdByUser": {
        "key": "51",
        "id": "Admin",
        "href": "/objects/company-config/user/51"
      },
      "modifiedByUser": {
        "key": "51",
        "id": "Admin",
        "href": "/objects/company-config/user/51"
      }
    },
    "href": "/objects/company-config/role-user-map/618"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/role/{key}
_Get a role_

**Response 200 — Get a role:**
```json
{
  "ia::result": {
    "key": "470",
    "id": "Admins",
    "description": "Administrator role with permissions",
    "roleType": "enterprise",
    "applyTo": "loginAndSlideIn",
    "audit": {
      "createdDateTime": "2020-11-16T14:27:51Z",
      "modifiedDateTime": "2020-11-16T14:28:11Z",
      "createdBy": "1",
      "modifiedBy": "1",
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
    "rolePermissionAssignments": [
      {
        "key": "30",
        "id": "30",
        "role": {
          "key": "470",
          "id": "Admins",
          "href": "/objects/company-config/role/470"
        },
        "permission": {
          "key": "253",
          "id": "253",
          "name": "taxScheduleMap",
          "module": "purchasing",
          "href": "/objects/company-config/permission/253"
        },
        "accessRights": [
          "list",
          "readonly",
          "add",
          "modify",
          "delete"
        ],
        "audit": {
          "createdDateTime": "2020-11-16T14:27:51Z",
          "modifiedDateTime": "2020-11-16T14:28:11Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/company-config/role-permission-assignment/30"
      }
    ],
    "customRolePermissionAssignments": [
      {
        "application": {
          "key": "10004",
          "id": "Custom Application",
          "href": "/objects/platform/custom-application/10004",
          "permission": [
            {
              "name": "Org Department",
              "group": "objects"
            }
          ],
          "permissions": [
            {
              "name": "Org Department",
              "group": "objects"
            }
          ]
        },
        "accessRights": [
          "list",
          "readonly",
          "modify"
        ],
        "allowedAccessRights": [
          "list",
          "readonly",
          "modify"
        ]
      },
      {
        "application": {
          "key": "10004",
          "id": "Custom Application",
          "href": "/objects/platform/custom-application/10004",
          "permissions": [
            {
              "name": "Org Department",
              "group": "objects"
            }
          ]
        },
        "allowedAccessRights": [
          "list",
          "readonly",
          "modify"
        ]
      }
    ],
    "agentRolePermissionAssignments": [
      {
        "agent": {
          "key": "9030801000000002",
          "id": "scm-to-transaction-converter",
          "permissions": [
            {
              "name": "Convert an SCM document to the specified transaction type",
              "group": "agents"
            }
          ]
        },
        "allowedAccessRights": [
          "run"
        ]
      }
    ],
    "roleUsers": [
      {
        "key": "472",
        "id": "472",
        "role": {
          "key": "470",
          "id": "Admins",
          "href": "/objects/company-config/role/470"
        },
        "user": {
          "key": "189",
          "id": "Admin",
          "href": "/objects/company-config/user/189"
        },
        "audit": {
          "createdDateTime": "2020-11-16T14:27:51Z",
          "modifiedDateTime": "2020-11-16T14:28:11Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/company-config/role-user-map/472"
      }
    ],
    "roleGroups": [
      {
        "key": "761",
        "id": "761",
        "role": {
          "key": "470",
          "id": "Admins",
          "href": "/objects/company-config/role/470"
        },
        "userGroup": {
          "key": "1",
          "id": "Bypass group",
          "href": "/objects/company-config/user-group/1"
        },
        "audit": {
          "createdDateTime": "2020-11-16T14:27:51Z",
          "modifiedDateTime": "2020-11-16T14:28:11Z",
          "createdBy": "1",
          "modifiedBy": "1"
        },
        "href": "/objects/company-config/role-user-group-map/761"
      }
    ],
    "href": "/objects/company-config/role/470"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/role/{key}
_Update a role_

**Request example — Update a role:**
```json
{
  "description": "Administrator role with permissions",
  "rolePermissionAssignments": [
    {
      "key": "30",
      "accessRights": [
        "list"
      ]
    },
    {
      "permission": {
        "key": "274"
      },
      "accessRights": [
        "add"
      ]
    }
  ],
  "customRolePermissionAssignments": [
    {
      "application": {
        "key": "10004",
        "id": "SaaS Subscription Management",
        "permissions": [
          {
            "name": "Org Department",
            "group": "objects"
          }
        ]
      },
      "allowedAccessRights": [
        "list",
        "readonly",
        "modify"
      ]
    }
  ],
  "agentRolePermissionAssignments": [
    {
      "agent": {
        "key": "9030801000000002",
        "id": "scm-to-transaction-converter",
        "permissions": [
          {
            "name": "Convert an SCM document to the specified transaction type",
            "group": "agents"
          }
        ]
      },
      "allowedAccessRights": [
        "run"
      ]
    }
  ]
}
```
**Response 200 — Reference to updated role:**
```json
{
  "ia::result": {
    "key": "470",
    "id": "Admins",
    "href": "/objects/company-config/role/470"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/role/{key}
_Delete a role_


## GET /objects/company-config/txn-currency
_List transaction currencies_

**Response 200 — List transaction currencies:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "AUD",
      "href": "/objects/company-config/txn-currency/1"
    },
    {
      "key": "2",
      "id": "EUR",
      "href": "/objects/company-config/txn-currency/2"
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

## POST /objects/company-config/txn-currency
_Create a transaction currency_

**Request example — Create an ISO transaction currency:**
```json
{
  "id": "USD",
  "currencyFormat": "unitedStates",
  "currencyType": "iso"
}
```
**Request example — Create a custom transaction currency with custom currency format:**
```json
{
  "id": "CUS",
  "name": "Custom currency",
  "symbol": "$",
  "currencyFormat": "custom",
  "unit": "Dollars",
  "subUnit": "Cents",
  "decimalSeparator": ".",
  "thousandSeparator": ",",
  "alignment": "left",
  "currencyType": "custom"
}
```
**Response 201 — Create an ISO transaction currency:**
```json
{
  "ia::result": {
    "key": "235",
    "id": "USD",
    "href": "/objects/company-config/txn-currency/235"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 201 — Create a custom transaction currency:**
```json
{
  "ia::result": {
    "key": "236",
    "id": "CUS",
    "href": "/objects/company-config/txn-currency/236"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/txn-currency/{key}
_Get a transaction currency_

**Response 200 — Get a transaction currency:**
```json
{
  "ia::result": {
    "key": "235",
    "id": "USD",
    "name": "US Dollar",
    "symbol": "$",
    "isoCode": "840",
    "currencyFormat": "unitedStates",
    "unit": "Dollars",
    "subUnit": "Cents",
    "decimalSeparator": ".",
    "thousandSeparator": ",",
    "alignment": "left",
    "currencyType": "iso",
    "audit": {
      "modifiedDateTime": "2023-04-13T09:19:58Z",
      "modifiedBy": "1",
      "modifiedByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdDateTime": "2023-04-13T09:05:08Z",
      "createdBy": "1",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      }
    },
    "href": "/objects/company-config/txn-currency/235"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/txn-currency/{key}
_Update a transaction currency_

**Request example — Update a transaction currency:**
```json
{
  "currencyFormat": "indian"
}
```
**Response 200 — Reference to transaction currency:**
```json
{
  "ia::result": {
    "key": "235",
    "id": "USD",
    "href": "/objects/company-config/txn-currency/235"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/txn-currency/{key}
_Delete a transaction currency_


## GET /objects/company-config/user
_List users_

**Response 200 — List users:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Admin",
      "href": "/objects/company-config/user/1"
    },
    {
      "key": "2",
      "id": "Jane Doe",
      "href": "/objects/company-config/user/2"
    },
    {
      "key": "4",
      "id": "Larry Smith",
      "href": "/objects/company-config/user/4"
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

## POST /objects/company-config/user
_Create a user_

**Request example — Create a new admin user:**
```json
{
  "id": "Admin",
  "userName": "Admin",
  "userType": "business",
  "accountEmail": "user_17@sage.com",
  "adminPrivileges": "full",
  "contact": {
    "id": "jsmith",
    "permissionAssignments": [
      {
        "permission": {
          "key": "404"
        },
        "accessRights": [
          "list",
          "delete"
        ]
      },
      {
        "permission": {
          "key": "253"
        },
        "accessRights": [
          "list"
        ]
      }
    ]
  },
  "customPermissionAssignments": [
    {
      "application": {
        "key": "10002",
        "permissions": [
          {
            "name": "Product Lines",
            "group": "objects"
          }
        ]
      },
      "allowedAccessRights": [
        "list",
        "readonly",
        "template"
      ]
    }
  ],
  "agentPermissionAssignments": [
    {
      "agent": {
        "key": "9030801000000002",
        "permissions": [
          {
            "name": "Convert an SCM document to the specified transaction type",
            "group": "agents"
          }
        ]
      },
      "allowedAccessRights": [
        "run"
      ]
    }
  ]
}
```
**Response 201 — Reference to new user:**
```json
{
  "ia::result": {
    "key": "102",
    "id": "Admin",
    "href": "/objects/company-config/user/102"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/user-group
_List user groups_

**Response 200 — List user groups:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Warehouse users",
      "href": "/objects/company-config/user-group/1"
    },
    {
      "key": "96",
      "id": "AP users",
      "href": "/objects/company-config/user-group/96"
    },
    {
      "key": "21",
      "id": "Administrators",
      "href": "/objects/company-config/user-group/21"
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

## POST /objects/company-config/user-group
_Create a user group_

**Request example — Create a user group:**
```json
{
  "id": "GL users",
  "description": "General Ledger account managers",
  "roles": [
    {
      "key": "7"
    },
    {
      "key": "65"
    },
    {
      "key": "72"
    }
  ]
}
```
**Response 201 — Reference to new user group:**
```json
{
  "ia::result": {
    "key": "41",
    "id": "GL users",
    "href": "/objects/company-config/user-group/41"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/company-config/user-group/{key}
_Get a user group_

**Response 200 — Get a user group:**
```json
{
  "ia::result": {
    "key": "41",
    "id": "GL users",
    "description": "General Ledger managers",
    "audit": {
      "createdDateTime": "2024-02-15T11:39:04Z",
      "modifiedDateTime": "2024-02-15T11:39:04Z",
      "createdBy": "51",
      "modifiedBy": "51",
      "createdByUser": {
        "key": "51",
        "id": "Admin",
        "href": "/objects/company-config/user/51"
      },
      "modifiedByUser": {
        "key": "51",
        "id": "Admin",
        "href": "/objects/company-config/user/51"
      }
    },
    "roles": [
      {
        "key": "27",
        "id": "::SYS::Enterprise-ROLE-FOR - Module: Create Class",
        "href": "/objects/company-config/role/27"
      },
      {
        "key": "61",
        "id": "::SYS::Enterprise-ROLE-FOR - Module: Test App",
        "href": "/objects/company-config/role/61"
      },
      {
        "key": "65",
        "id": "platform",
        "href": "/objects/company-config/role/65"
      }
    ],
    "href": "/objects/company-config/user-group/41"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/user-group/{key}
_Update a user group_

**Request example — Update a user group:**
```json
{
  "description": "Who can manage GL accounts"
}
```
**Response 200 — Reference to updated user group:**
```json
{
  "ia::result": {
    "key": "41",
    "id": "GL users",
    "href": "/objects/company-config/user-group/41"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/user-group/{key}
_Delete a user group_


## GET /objects/company-config/user/{key}
_Get a user_

**Response 200 — Get a user:**
```json
{
  "ia::result": {
    "id": "Admin",
    "userName": "Admin",
    "accountEmail": "user_17@sage.com",
    "contact": {
      "mailingAddress": {
        "addressLine1": "744 Edgewater Blvd",
        "addressLine2": "Apt 104",
        "addressLine3": "Western industrial area",
        "city": "San Jose",
        "state": "CA",
        "postCode": "95110",
        "country": "United States"
      },
      "id": "contact01650967341",
      "lastName": "John",
      "firstName": "E.",
      "middleName": "Doe",
      "prefix": "Mr",
      "printAs": "John E. Doe",
      "email1": "john.doe@example.com",
      "email2": "john.doe@example.co",
      "phone1": "6692248123",
      "phone2": null,
      "mobile": "1222455566",
      "pager": null,
      "fax": "1222455566",
      "URL1": "http://john.example.com",
      "URL2": null,
      "companyName": "Sage Inc",
      "key": "3446",
      "href": "/objects/company-config/contact/3446"
    },
    "adminPrivileges": "off",
    "userType": "business",
    "webServices": {
      "isEnabled": true,
      "isRestricted": false
    },
    "status": "active",
    "entityAccess": {
      "allowUnrestrictedAccess": true,
      "allowTopLevelAccess": false
    },
    "password": {
      "neverExpires": true,
      "requiresReset": false,
      "disablePassword": false
    },
    "audit": {
      "createdDateTime": "2022-04-26T10:17:12Z",
      "modifiedDateTime": "2022-04-26T11:05:26Z",
      "createdBy": "12",
      "modifiedBy": "13",
      "createdByUser": {
        "key": "12",
        "id": "Admin",
        "href": "/objects/company-config/user/12"
      },
      "modifiedByUser": {
        "key": "13",
        "id": "Aman",
        "href": "/objects/company-config/user/13"
      }
    },
    "key": "65",
    "isChatterDisabled": false,
    "hideOtherDepartmentTransactions": false,
    "entity": {
      "key": "54",
      "id": "313131",
      "name": "Central Region",
      "href": "/objects/company-config/entity/54"
    },
    "locations": [
      {
        "key": "87",
        "id": "London",
        "href": "/objects/company-config/location/87"
      },
      {
        "key": "92",
        "id": "Paris",
        "href": "/objects/company-config/location/92"
      }
    ],
    "departments": [
      {
        "key": "55",
        "id": "Sales",
        "href": "/objects/company-config/department/55"
      },
      {
        "key": "65",
        "id": "Accounting",
        "href": "/objects/company-config/department/65"
      }
    ],
    "territories": [
      {
        "key": "22",
        "id": "South",
        "href": "/objects/accounts-receivable/territory/22"
      },
      {
        "key": "32",
        "id": "West",
        "href": "/objects/accounts-receivable/territory/32"
      }
    ],
    "roles": [
      {
        "key": "2",
        "id": "::SYS::Multi Entity Shared-ROLE-FOR - Admin",
        "href": "/objects/company-config/role/2"
      },
      {
        "key": "23",
        "id": "::SYS::Multi Entity Shared-ROLE-FOR - User",
        "href": "/objects/company-config/role/23"
      }
    ],
    "permissionAssignments": [
      {
        "permission": {
          "id": "404",
          "key": "404",
          "href": "/objects/company-config/permission/404"
        },
        "accessRights": [
          "list",
          "delete"
        ]
      },
      {
        "permission": {
          "id": "253",
          "key": "253",
          "href": "/objects/company-config/permission/253"
        },
        "accessRights": [
          "list",
          "delete"
        ]
      }
    ],
    "customPermissionAssignments": [
      {
        "application": {
          "key": "10002",
          "id": "Intacct Database Services",
          "href": "/objects/platform/custom-application/10002",
          "permission": [
            {
              "name": "Product Lines",
              "group": "objects"
            }
          ],
          "permissions": [
            {
              "name": "Product Lines",
              "group": "objects"
            }
          ]
        },
        "accessRights": [
          "list",
          "readonly"
        ],
        "allowedAccessRights": [
          "list",
          "readonly"
        ]
      }
    ],
    "agentPermissionAssignments": [
      {
        "agent": {
          "key": "9030801000000002",
          "id": "scm-to-transaction-converter",
          "permissions": [
            {
              "name": "Convert an SCM document to the specified transaction type",
              "group": "agents"
            }
          ]
        },
        "allowedAccessRights": [
          "run"
        ]
      }
    ],
    "sso": {
      "isSSOEnabled": true,
      "federatedSSOId": "john.doe"
    },
    "trustedDevices": "never",
    "href": "/objects/company-config/user/65"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/company-config/user/{key}
_Update a user_

**Request example — Update a user:**
```json
{
  "userName": "Admin",
  "status": "inactive",
  "permissionAssignments": [
    {
      "permission": {
        "key": "404"
      },
      "accessRights": [
        "list"
      ]
    }
  ],
  "customPermissionAssignments": [
    {
      "application": {
        "key": "10002",
        "permissions": [
          {
            "name": "Custom Dimensions",
            "group": "objects"
          }
        ]
      },
      "allowedAccessRights": [
        "list",
        "readonly",
        "template"
      ]
    }
  ],
  "agentPermissionAssignments": [
    {
      "agent": {
        "key": "9030801000000002",
        "permissions": [
          {
            "name": "Convert an SCM document to the specified transaction type",
            "group": "agents"
          }
        ]
      },
      "allowedAccessRights": [
        "run"
      ]
    }
  ]
}
```
**Response 200 — Reference to updated user:**
```json
{
  "ia::result": {
    "key": "65",
    "id": "Admin",
    "href": "/objects/company-config/user/65"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/company-config/user/{key}
_Delete a user_


## GET /services/company-config/dimensions/list
_List dimensions_

**Response 200 — Response:**
```json
{
  "ia::result": [
    {
      "dimensionName": "DEPARTMENT",
      "dimensionLabel": "Department",
      "termName": "Department",
      "isUserDefinedDimension": false,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/company-config/department"
    },
    {
      "dimensionName": "LOCATION",
      "dimensionLabel": "Location",
      "termName": "Loc",
      "isUserDefinedDimension": false,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/company-config/location"
    },
    {
      "dimensionName": "PROJECT",
      "dimensionLabel": "Project",
      "termName": "Project",
      "isUserDefinedDimension": false,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/projects/project"
    },
    {
      "dimensionName": "CUSTOMER",
      "dimensionLabel": "Customer",
      "termName": "Customer",
      "isUserDefinedDimension": false,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/accounts-receivable/customer"
    },
    {
      "dimensionName": "VENDOR",
      "dimensionLabel": "Vendor",
      "termName": "Vendor",
      "isUserDefinedDimension": false,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/accounts-payable/vendor"
    },
    {
      "dimensionName": "EMPLOYEE",
      "dimensionLabel": "Employee",
      "termName": "Employee",
      "isUserDefinedDimension": false,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/company-config/employee"
    },
    {
      "dimensionName": "ITEM",
      "dimensionLabel": "Item",
      "termName": "Item",
      "isUserDefinedDimension": false,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/inventory-control/item"
    },
    {
      "dimensionName": "CLASS",
      "dimensionLabel": "Class",
      "termName": "Class",
      "isUserDefinedDimension": false,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/company-config/class"
    },
    {
      "dimensionName": "CONTRACT",
      "dimensionLabel": "Contract",
      "termName": "Contract",
      "isUserDefinedDimension": false,
      "isEnabledInGL": false,
      "dimensionEndpoint": "/objects/contracts/contract"
    },
    {
      "dimensionName": "TASK",
      "dimensionLabel": "Task",
      "termName": "Task",
      "isUserDefinedDimension": false,
      "isEnabledInGL": false,
      "dimensionEndpoint": "/objects/projects/task"
    },
    {
      "dimensionName": "WAREHOUSE",
      "dimensionLabel": "Warehouse",
      "termName": "Warehouse",
      "isUserDefinedDimension": false,
      "isEnabledInGL": false,
      "dimensionEndpoint": "/objects/inventory-control/warehouse"
    },
    {
      "dimensionName": "COSTTYPE",
      "dimensionLabel": "Cost type",
      "termName": "Cost type",
      "isUserDefinedDimension": false,
      "isEnabledInGL": false,
      "dimensionEndpoint": "/objects/construction/cost-type"
    },
    {
      "dimensionName": "AFFILIATEENTITY",
      "dimensionLabel": "Affiliate entity",
      "termName": "Affiliate entity",
      "isUserDefinedDimension": false,
      "isEnabledInGL": false,
      "dimensionEndpoint": "/objects/company-config/affiliate-entity"
    },
    {
      "dimensionName": "FIXEDASSET",
      "dimensionLabel": "Asset",
      "termName": "Asset",
      "isUserDefinedDimension": false,
      "isEnabledInGL": false,
      "dimensionEndpoint": "/objects/fixed-assets/asset"
    },
    {
      "dimensionName": "CHANNEL",
      "dimensionLabel": "Channel",
      "termName": "Channel",
      "isUserDefinedDimension": true,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/platform-apps/nsp::channel"
    },
    {
      "dimensionName": "DACIA",
      "dimensionLabel": "dacia",
      "termName": "dacia",
      "isUserDefinedDimension": true,
      "isEnabledInGL": true,
      "dimensionEndpoint": "/objects/platform-apps/nsp::dacia"
    }
  ],
  "ia::meta": {
    "totalCount": "15",
    "totalSuccess": "15",
    "totalError": "0"
  }
}
```

## POST /services/company-config/document-sequence/generate-next-value
_Generate next value_

**Request example — Generate next value by ID:**
```json
{
  "id": "AR Inv"
}
```
**Request example — Generate next value by ID and fiscal year:**
```json
{
  "id": "AR Inv",
  "fiscalYear": 2024
}
```
**Request example — Generate next value by key:**
```json
{
  "key": "307"
}
```
**Request example — Generate next value by key and fiscal year:**
```json
{
  "key": "307",
  "fiscalYear": 2024
}
```
**Response 200 — Generate next value without fiscal year:**
```json
{
  "ia::result": {
    "id": "AR Inv",
    "nextValue": "INV-16"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 200 — Generate next value with fiscal year:**
```json
{
  "ia::result": {
    "key": "307",
    "id": "AR Inv",
    "nextValue": "P-0001-S-2024",
    "fiscalYear": 2024
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
