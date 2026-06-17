# Reports

## GET /objects/reports/interactive-custom-report
_List interactive custom reports_

**Response 200 — List interactive custom reports:**
```json
{
  "ia::result": [
    {
      "key": "1838",
      "id": "1838",
      "href": "/objects/reports/interactive-custom-report/1838"
    },
    {
      "key": "1901",
      "id": "1901",
      "href": "/objects/reports/interactive-custom-report/1901"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "start": 1,
    "pageSize": 100,
    "next": 101,
    "previous": null
  }
}
```

## POST /objects/reports/interactive-custom-report
_Create an interactive custom report_

**Request example — Creates a interactive custom report:**
```json
{
  "createFromExistingReport": true,
  "name": "GL Detail with PO No",
  "isStandardPeriodIncluded": false,
  "moduleName": "accountsPayable",
  "reportType": "interactiveCustomReport",
  "addReportToMenu": false,
  "status": "active",
  "fromLibrary": false,
  "reportingAreas": [
    "apPayments"
  ],
  "glReportType": {
    "key": "1"
  },
  "glReportAudience": {
    "key": "3"
  }
}
```
**Response 201 — Reference to new interactive custom report:**
```json
{
  "ia::result": {
    "id": "1771",
    "key": "1771",
    "href": "/objects/reports/interactive-custom-report/1771"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/reports/interactive-custom-report/{key}
_Get an interactive custom report_

**Response 200 — Details of the interactive custom report:**
```json
{
  "ia::result": {
    "id": "1838",
    "key": "1838",
    "moduleName": "accountsPayable",
    "reportType": "interactiveCustomReport",
    "reportPath": "shared/Traders/Contracts Expenses",
    "addReportToMenu": false,
    "status": "active",
    "fromLibrary": false,
    "audit": {
      "createdDateTime": "2025-06-02T14:33:01Z",
      "modifiedDateTime": "2025-06-02T14:36:05Z",
      "createdByUser": {
        "key": "1",
        "id": "Jane Smith",
        "href": "/objects/company-config/user/1"
      },
      "modifiedByUser": {
        "key": "1",
        "id": "Jane Smith",
        "href": "/objects/company-config/user/1"
      }
    },
    "reportingAreas": [
      "apPayments"
    ],
    "glReportAudience": {
      "id": "2",
      "key": "2",
      "name": "RA",
      "href": "/objects/general-ledger/report-audience/2"
    },
    "glReportType": {
      "id": "1",
      "key": "1",
      "name": "RT",
      "href": "/objects/general-ledger/report-type/1"
    },
    "href": "/objects/reports/interactive-custom-report/1838"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/reports/interactive-custom-report/{key}
_Update an interactive custom report_

**Request example — Update an interactive custom report:**
```json
{
  "status": "active",
  "glReportType": {
    "key": "2"
  },
  "glReportAudience": {
    "key": "1"
  }
}
```
**Response 200 — Reference to updated interactive custom report:**
```json
{
  "ia::result": {
    "id": "1838",
    "key": "1838",
    "href": "/objects/reports/interactive-custom-report/1838"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/reports/interactive-custom-report/{key}
_Delete an interactive custom report_


## GET /objects/reports/stored-report
_List stored reports_

**Response 200 — List stored reports:**
```json
{
  "ia::result": [
    {
      "key": "121",
      "id": "121",
      "href": "/objects/reports/stored-report/121"
    },
    {
      "key": "122",
      "id": "122",
      "href": "/objects/reports/stored-report/122"
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

## GET /objects/reports/stored-report-error-record
_List stored report error records_

**Response 200 — List stored report error records:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/reports/stored-report-error-record/1"
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

## GET /objects/reports/stored-report-error-record/{key}
_Get a stored report error record_

**Response 200 — Get a stored report error record:**
```json
{
  "ia::result": {
    "id": "2",
    "key": "2",
    "storedReport": {
      "id": "128",
      "key": "128",
      "href": "/objects/reports/stored-report/128"
    },
    "reportType": "_csv",
    "createdDateTime": "2025-03-19T00:00:00Z",
    "errorCode": "BL03002028",
    "errorDescription": "No Data Found",
    "href": "/objects/reports/stored-report-error-record/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/reports/stored-report/{key}
_Get a stored report_

**Response 200 — Get a stored report:**
```json
{
  "ia::result": {
    "id": "124",
    "key": "124",
    "reportType": "gl_tb",
    "reportTitle": "TB Memorized",
    "audit": {
      "createdDateTime": "2025-03-04T06:28:48Z",
      "modifiedDateTime": "2025-03-04T06:28:48Z"
    },
    "user": {
      "key": "1",
      "id": "Admin",
      "href": "/objects/company-config/user/1"
    },
    "moduleKey": "2.GL",
    "localStore": {
      "html": {
        "status": null
      },
      "pdf": {
        "status": "success"
      },
      "csv": {
        "status": null
      },
      "excel": {
        "status": null
      },
      "text": {
        "status": null
      }
    },
    "cloudStore": {
      "status": null
    },
    "href": "/objects/reports/stored-report/124"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/reports/stored-report/{key}
_Delete a stored report_


## POST /services/reports/cancel
_Cancel a report_

**Request example — Cancel a queued report:**
```json
{
  "reportId": "123",
  "outputType": "pdf",
  "outputLocation": "intacct"
}
```
**Response 200 — Cancel report response:**
```json
{
  "ia::result": {
    "reportId": "1",
    "status": "canceled",
    "outputType": "pdf",
    "outputLocation": "intacct",
    "name": "Customer Report",
    "href": "/services/reports/status?reportId=1&outputType=pdf&outputLocation=intacct"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /services/reports/download
_Download a report_

**Response 200 — 200 response example:**
```json
"string"
```
**Response 200 — 200 response example:**
```json
"string"
```
**Response 200 — 200 response example:**
```json
"string"
```
**Response 200 — 200 response example:**
```json
"string"
```
**Response 200 — 200 response example:**
```json
"string"
```
**Response 200 — 200 response example:**
```json
"string"
```
**Response 200 — 200 response example:**
```json
"string"
```

## GET /services/reports/status
_Report status_

**Response 200 — Completed cloud store report status:**
```json
{
  "ia::result": {
    "reportId": 1,
    "status": "completed",
    "outputType": "pdf",
    "outputLocation": "cloud",
    "cloudStore": {
      "target": "s3",
      "path": "/"
    },
    "name": "Customer Report",
    "href": "/services/reports/status?reportId=1&outputType=pdf&outputLocation=cloud"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
**Response 303 — Completed Intacct report status:**
```json
{
  "ia::result": {
    "reportId": 1,
    "status": "completed",
    "outputType": "pdf",
    "outputLocation": "intacct",
    "name": "Customer Report",
    "downloadURL": "/services/reports/download?reportId=1&outputType=pdf"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/reports/stored-reports
_Retrieve a stored report_

**Request example — Request a report in different format:**
```json
{
  "reportId": "123",
  "outputType": "pdf",
  "outputLocation": "intacct"
}
```
**Response 200 — Report request response:**
```json
{
  "ia::result": {
    "reportId": 1,
    "status": "submitted",
    "outputType": "pdf",
    "outputLocation": "intacct",
    "name": "Customer Report",
    "href": "/services/reports/status?reportId=1&outputType=pdf&outputLocation=intacct"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```
