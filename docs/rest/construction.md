# Construction

## GET /objects/construction-forecasting/wip-forecast-detail
_List WIP forecast details_

**Response 200 — List WIP forecast details:**
```json
{
  "ia::result": [
    {
      "id": "1",
      "key": "1",
      "href": "/objects/construction-forecasting/wip-forecast-detail/1"
    },
    {
      "id": "2",
      "key": "2",
      "href": "/objects/construction-forecasting/wip-forecast-detail/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-forecast-detail/{key}
_Get a WIP forecast detail_

**Response 200 — Details of a WIP forecast detail:**
```json
{
  "ia::result": {
    "id": "430300000000",
    "key": "430300000000",
    "wipPeriod": {
      "periodName": "Month Ended August 2023",
      "id": "4",
      "key": "4",
      "href": "/objects/construction-forecasting/wip-period/4"
    },
    "task": {
      "name": "Curb Gutters Sidewalks and Driveways",
      "id": "32 16 00",
      "key": "150",
      "href": "/objects/projects/task/150"
    },
    "taskComposite": "32 16 00--Curb Gutters Sidewalks and Driveways",
    "rootTask": {
      "name": "EXTERIOR IMPROVEMENTS",
      "id": "32 00 00",
      "key": "149",
      "href": "/objects/projects/task/149"
    },
    "rootTaskComposite": "32 00 00--EXTERIOR IMPROVEMENTS",
    "costType": {
      "name": "Subcontract",
      "id": "SUB",
      "key": "586",
      "href": "/objects/construction/cost-type/586"
    },
    "costTypeComposite": "SUB--Subcontract",
    "project": {
      "name": "Northside HS",
      "id": "23-010",
      "key": "10",
      "href": "/objects/projects/project/10"
    },
    "projectComposite": "23-010--Northside HS",
    "assignedEntity": {
      "name": "Timberline GC",
      "id": "TIMBGC",
      "key": "3",
      "href": "/objects/company-config/entity/3"
    },
    "wipProject": {
      "id": "12",
      "key": "12",
      "href": "/objects/construction-forecasting/wip-project/12"
    },
    "projectManagerForecast": {
      "key": "17",
      "id": "17",
      "costToComplete": "3000.00",
      "costAtCompletion": "9000.00",
      "percentComplete": "66.67",
      "notes": "This is a draft forecast from Project Manager.",
      "updatedDate": "2023-05-26T10:06:00Z",
      "updatedDateTime": "2023-05-26T10:06:00Z",
      "costToCompleteVariance": "500.00",
      "costAtCompletionVariance": "400.00",
      "href": "/objects/construction-forecasting/wip-project-manager-forecast/17"
    },
    "priorPeriodProjectManagerForecast": {
      "costToComplete": "3500.00",
      "costAtCompletion": "9400.00",
      "percentComplete": "62.77"
    },
    "costAndEstimateDetail": {
      "key": "4303",
      "id": "4303",
      "estimatedCostAtCompletion": "1500000.00",
      "jobToDateCosts": "1250000.00",
      "estimatedCostToDateAmount": "1000000.00",
      "pendingEstimatesAmount": "1010000.00",
      "estimatedCostToComplete": "500000.00",
      "estimatedPercentComplete": "66.67",
      "estimateVsForecastVariance": "500.00"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction-forecasting/wip-forecast-detail/{key}
_Update a WIP forecast detail_

**Request example — Update a WIP forecast detail:**
```json
{
  "projectManagerForecast": {
    "costToComplete": "2000.00",
    "costAtCompletion": "9000.00",
    "notes": "Update forecast",
    "updatedDateTime": "2024-11-26T10:06:00Z"
  }
}
```
**Response 200 — Reference to updated WIP forecast detail:**
```json
{
  "ia::result": {
    "key": "430300000000",
    "id": "430300000000",
    "href": "/objects/construction-forecasting/wip-forecast-detail/430300000000"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-period
_List WIP periods_

**Response 200 — List WIP periods:**
```json
{
  "ia::result": [
    {
      "id": "8",
      "key": "8",
      "href": "/objects/construction-forecasting/wip-period/8"
    },
    {
      "id": "9",
      "key": "9",
      "href": "/objects/construction-forecasting/wip-period/9"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## POST /objects/construction-forecasting/wip-period
_Create a WIP period_

**Request example — Create a WIP period:**
```json
{
  "periodEndDate": "2023-10-31",
  "notes": "WIP schedule for the month of Oct. 2023",
  "assignedEntity": {
    "id": "TIMBGC"
  }
}
```
**Response 201 — Reference to new WIP period:**
```json
{
  "ia::result": {
    "key": "41",
    "id": "41",
    "href": "/objects/construction-forecasting/wip-period/41"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-period/{key}
_Get a WIP period_

**Response 200 — Details of a WIP period:**
```json
{
  "ia::result": {
    "createdFromEntity": {
      "key": "3"
    },
    "endOfPriorYearPeriod": {
      "periodName": "Month Ended December 2022",
      "id": "65",
      "key": "65"
    },
    "assignedEntity": {
      "name": "Timberline GC",
      "id": "TIMBGC",
      "key": "3"
    },
    "wipProjects": [
      {
        "wipPeriod": {
          "periodName": "Month Ended October 2023",
          "id": "54",
          "key": "54"
        },
        "project": {
          "endDate": "2023-07-31",
          "name": "Quick Bowls - Portland1",
          "description": "Fast food restaurant with drive-thru",
          "id": "22-001",
          "key": "1",
          "startDate": "2022-01-03",
          "status": "active"
        },
        "forecastDetails": [
          {
            "wipPeriod": {
              "periodName": "Month Ended October 2023",
              "id": "54",
              "key": "54"
            },
            "task": {
              "name": "Finish Carpentry",
              "id": "06 20 00",
              "key": "538"
            },
            "costType": {
              "name": "Subcontract",
              "id": "SUB",
              "key": "1496"
            },
            "project": {
              "name": "Quick Bowls - Portland1",
              "id": "22-001",
              "key": "1"
            },
            "wipProject": {
              "id": "338",
              "key": "338"
            },
            "rootTask": {
              "name": "WOOD PLASTICS AND COMPOSITES",
              "id": "06 00 00",
              "key": "537"
            },
            "priorPeriodProjectManagerForecast": {
              "costAtCompletion": "900",
              "costToComplete": "500",
              "percentComplete": "80"
            },
            "costAndEstimateDetail": {
              "estimatedCostAtCompletion": "5200",
              "jobToDateCosts": "5200",
              "estimatedCostToDateAmount": "5200",
              "key": "7829"
            },
            "projectManagerForecast": {
              "costToCompleteVariance": "900",
              "costAtCompletionVariance": "500"
            },
            "id": "782900000000",
            "key": "782900000000"
          },
          {
            "wipPeriod": {
              "periodName": "Month Ended October 2023",
              "id": "54",
              "key": "54"
            },
            "task": {
              "name": "Fees",
              "id": "01 41 23",
              "key": "259"
            },
            "costType": {
              "name": "Other",
              "id": "OTH",
              "key": "835"
            },
            "project": {
              "name": "Quick Bowls - Portland1",
              "id": "22-001",
              "key": "1"
            },
            "wipProject": {
              "id": "338",
              "key": "338"
            },
            "rootTask": {
              "name": "GENERAL REQUIREMENTS",
              "id": "01 00 00",
              "key": "255"
            },
            "priorPeriodProjectManagerForecast": {
              "costAtCompletion": "900",
              "costToComplete": "500",
              "percentComplete": "80"
            },
            "costAndEstimateDetail": {
              "estimatedCostAtCompletion": "1100",
              "jobToDateCosts": "6590",
              "estimatedCostToDateAmount": "1100",
              "key": "7836"
            },
            "projectManagerForecast": {
              "costToCompleteVariance": "900",
              "costAtCompletionVariance": "500"
            },
            "id": "783600000000",
            "key": "783600000000"
          }
        ],
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2024-12-11T17:36:42Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2025-01-03T21:13:13Z",
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
        "projectManagerForecast": {
          "contractValue": "179610",
          "costAtCompletion": "900",
          "costToComplete": "-308235.95",
          "percentComplete": "-9999"
        },
        "cfoForecast": {
          "contractValue": "179610",
          "lastUpdatedDate": "2024-12-26T16:35:22Z",
          "costAtCompletion": "450000.6",
          "costToComplete": "140864.65",
          "percentComplete": "68.7"
        },
        "customer": {
          "name": "Trammel Crow",
          "id": "C00002",
          "key": "2"
        },
        "jobToDateUnderbillingAmount": "100490.07",
        "remainingProfit": "-84646.72",
        "currentPeriodEarnedProfitAmount": "0",
        "totalContractValue": "179610",
        "currentPeriodEarnedRevenueAmount": "0",
        "endOfPriorYearEarnedToDateAmount": "0",
        "earnedProfitToDateAmount": "-185743.88",
        "cfoForecastGrossProfitAtCompletion": "-270390.6",
        "costAtCompletionVariance": "21244.06",
        "currentPeriodBillingAmount": "0",
        "grossProfitPercentOfContract": "-150.54",
        "estimatedCostToComplete": "119620.59",
        "overUnderBillingAmount": "100490.07",
        "yearToDateBillingAmount": "0",
        "isFinalized": false,
        "grossProfitVarianceAmount": "-21244.06",
        "jobToDateOverbillingAmount": "0",
        "estimatedPercentComplete": "72.1",
        "yearToDateEarnedProfitAmount": "-185743.88",
        "jobToDateCosts": "309135.95",
        "endOfPriorYearEarnedProfit": "0",
        "grossProfitPercentOfCost": "-60.09",
        "remainingBacklogAmount": "56217.93",
        "id": "338",
        "estimatedCostToDateAmount": "428756.54",
        "contractVarianceAmount": "0",
        "key": "338",
        "currentPeriodCostAmount": "0",
        "yearToDateCostAmount": "0",
        "cfoForecastGrossProfitMarginPercent": "-150.54",
        "yearToDateEarnedRevenueAmount": "123392.07",
        "totalGrossProfitEstimatedAtCompletion": "-249146.54",
        "jobToDateBillings": "22902",
        "earnedToDateAmount": "123392.07",
        "estimatedCostAtCompletion": "428756.54",
        "pendingEstimatesAmount": "0",
        "hasAnomaly": false,
        "assignedEntity": {
          "key": "3",
          "id": "TIMBGC",
          "name": "Timberline GC",
          "href": "/objects/company-config/entity/3"
        }
      },
      {
        "wipPeriod": {
          "periodName": "Month Ended October 2023",
          "id": "54",
          "key": "54"
        },
        "project": {
          "endDate": "2023-05-31",
          "name": "The Crest",
          "description": "3-story hotel with 140 rooms",
          "id": "22-002",
          "key": "2",
          "startDate": "2022-05-23",
          "status": "active"
        },
        "forecastDetails": [
          {
            "wipPeriod": {
              "periodName": "Month Ended October 2023",
              "id": "54",
              "key": "54"
            },
            "task": {
              "name": "Curb Gutters Sidewalks and Driveways",
              "id": "32 16 00",
              "key": "139"
            },
            "costType": {
              "name": "Subcontract",
              "id": "SUB",
              "key": "562"
            },
            "project": {
              "name": "The Crest",
              "id": "22-002",
              "key": "2"
            },
            "wipProject": {
              "id": "339",
              "key": "339"
            },
            "assignedEntity": {
              "name": "Timberline GC",
              "id": "TIMBGC",
              "key": "3"
            },
            "rootTask": {
              "name": "EXTERIOR IMPROVEMENTS",
              "id": "32 00 00",
              "key": "138"
            },
            "costAndEstimateDetail": {
              "estimatedCostAtCompletion": "650000",
              "jobToDateCosts": "650000",
              "estimatedCostToDateAmount": "650000",
              "key": "7831"
            },
            "projectManagerForecast": {
              "costToCompleteVariance": "0",
              "costAtCompletionVariance": "0"
            },
            "id": "783100000000",
            "key": "783100000000"
          },
          {
            "wipPeriod": {
              "periodName": "Month Ended October 2023",
              "id": "54",
              "key": "54"
            },
            "task": {
              "name": "Finish Carpentry",
              "id": "06 20 00",
              "key": "544"
            },
            "costType": {
              "name": "Subcontract",
              "id": "SUB",
              "key": "1510"
            },
            "project": {
              "name": "The Crest",
              "id": "22-002",
              "key": "2"
            },
            "wipProject": {
              "id": "339",
              "key": "339"
            },
            "assignedEntity": {
              "name": "Timberline GC",
              "id": "TIMBGC",
              "key": "3"
            },
            "rootTask": {
              "name": "WOOD PLASTICS AND COMPOSITES",
              "id": "06 00 00",
              "key": "543"
            },
            "costAndEstimateDetail": {
              "estimatedCostAtCompletion": "850000",
              "jobToDateCosts": "850000",
              "estimatedCostToDateAmount": "850000",
              "key": "7842"
            },
            "projectManagerForecast": {
              "costToCompleteVariance": "0",
              "costAtCompletionVariance": "0"
            },
            "id": "784200000000",
            "key": "784200000000"
          }
        ],
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2024-12-11T17:36:42Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2025-01-03T21:13:13Z",
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
        "projectManagerForecast": {
          "contractValue": "26655280",
          "costAtCompletion": "22047033.42",
          "costToComplete": "1476700.07",
          "percentComplete": "93.3"
        },
        "cfoForecast": {
          "contractValue": "26655280",
          "costAtCompletion": "22047033.42",
          "costToComplete": "1476700.07",
          "percentComplete": "93.3"
        },
        "customer": {
          "name": "Star Enterprises",
          "id": "C00021",
          "key": "21"
        },
        "jobToDateUnderbillingAmount": "24869376.24",
        "remainingProfit": "309203.69",
        "currentPeriodEarnedProfitAmount": "0",
        "totalContractValue": "26655280",
        "currentPeriodEarnedRevenueAmount": "0",
        "endOfPriorYearEarnedToDateAmount": "0",
        "earnedProfitToDateAmount": "4299042.89",
        "cfoForecastGrossProfitAtCompletion": "4608246.58",
        "costAtCompletionVariance": "0",
        "currentPeriodBillingAmount": "0",
        "grossProfitPercentOfContract": "17.29",
        "estimatedCostToComplete": "1476700.07",
        "overUnderBillingAmount": "24869376.24",
        "yearToDateBillingAmount": "0",
        "isFinalized": false,
        "grossProfitVarianceAmount": "0",
        "jobToDateOverbillingAmount": "0",
        "estimatedPercentComplete": "93.3",
        "yearToDateEarnedProfitAmount": "4299042.89",
        "jobToDateCosts": "20570333.35",
        "endOfPriorYearEarnedProfit": "0",
        "grossProfitPercentOfCost": "20.9",
        "remainingBacklogAmount": "1785903.76",
        "id": "339",
        "estimatedCostToDateAmount": "22047033.42",
        "contractVarianceAmount": "0",
        "key": "339",
        "currentPeriodCostAmount": "0",
        "yearToDateCostAmount": "0",
        "cfoForecastGrossProfitMarginPercent": "17.29",
        "yearToDateEarnedRevenueAmount": "24869376.24",
        "totalGrossProfitEstimatedAtCompletion": "4608246.58",
        "jobToDateBillings": "0",
        "earnedToDateAmount": "24869376.24",
        "estimatedCostAtCompletion": "22047033.42",
        "pendingEstimatesAmount": "0",
        "hasAnomaly": false,
        "assignedEntity": {
          "key": "3",
          "id": "TIMBGC",
          "name": "Timberline GC",
          "href": "/objects/company-config/entity/3"
        }
      }
    ],
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2024-12-11T17:36:41Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2025-01-03T21:13:12Z",
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
    "lastRefreshDateTime": "2024-12-27T00:37:38Z",
    "wipCostBreakdownLevel": "costCodeAndCostType",
    "notes": "",
    "periodName": "Month Ended October 2023",
    "id": "54",
    "state": "unposted",
    "fiscalYear": "2023-01-01",
    "isHistoricalImport": false,
    "approveForExternalView": false,
    "key": "54",
    "periodEndDate": "2023-10-31"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction-forecasting/wip-period/{key}
_Update a WIP period_

**Request example — Update a WIP period:**
```json
{
  "state": "posted",
  "notes": "large under billing"
}
```
**Response 200 — Reference to updated WIP period:**
```json
{
  "ia::result": {
    "key": "41",
    "id": "41",
    "href": "/objects/construction-forecasting/wip-period/41"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction-forecasting/wip-period/{key}
_Delete a WIP period_


## GET /objects/construction-forecasting/wip-project
_List WIP projects_

**Response 200 — List of WIP projects:**
```json
{
  "ia::result": [
    {
      "id": "17",
      "key": "17",
      "href": "/objects/construction-forecasting/wip-project/17"
    },
    {
      "id": "23",
      "key": "23",
      "href": "/objects/construction-forecasting/wip-project/23"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## POST /objects/construction-forecasting/wip-project
_Create a WIP project_

**Request example — Create a WIP PM forecast:**
```json
{
  "id": "566",
  "periodEndDate": "2023-10-31",
  "assignedEntity": {
    "id": "TIMBGC"
  },
  "project": {
    "id": "22-001"
  },
  "projectManagerForecast": {
    "contractValue": "179610",
    "costAtCompletion": "900",
    "costToComplete": "-308235.95"
  },
  "cfoForecast": {
    "contractValue": "179610",
    "costAtCompletion": "450000.6",
    "costToComplete": "140864.65"
  },
  "forecastDetails": [
    {
      "project": {
        "id": "22-001"
      },
      "task": {
        "id": "06 20 00"
      },
      "costType": {
        "id": "SUB"
      },
      "projectManagerForecast": {
        "costToComplete": "900",
        "costAtCompletion": "500",
        "notes": "Updating a forecast."
      }
    }
  ]
}
```
**Response 201 — Reference to new WIP project manager forecast:**
```json
{
  "ia::result": {
    "key": "101",
    "id": "101",
    "href": "/objects/construction-forecasting/wip-project/101"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-project-manager-forecast
_List WIP project manager forecasts_

**Response 200 — List WIP project manager forecasts:**
```json
{
  "ia::result": [
    {
      "id": "17",
      "key": "17",
      "href": "/objects/construction-forecasting/wip-project-manager-forecast/17"
    },
    {
      "id": "18",
      "key": "18",
      "href": "/objects/construction-forecasting/wip-project-manager-forecast/18"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## POST /objects/construction-forecasting/wip-project-manager-forecast
_Create a WIP project manager forecast_

**Request example — Create a WIP project manager forecast:**
```json
{
  "wipPeriod": [
    {
      "id": "52"
    }
  ],
  "project": [
    {
      "id": "22-006"
    }
  ],
  "task": [
    {
      "id": "00 31 46"
    }
  ],
  "costType": [
    {
      "id": "OTH"
    }
  ],
  "assignedEntity": [
    {
      "id": "1"
    }
  ],
  "costToComplete": "1500.00",
  "costAtCompletion": "9000.00",
  "notes": "Initial work completed",
  "updatedDateTime": "2024-08-20T17:44:28Z"
}
```
**Response 201 — Reference to new WIP project manager forecast:**
```json
{
  "ia::result": {
    "key": "18",
    "id": "18",
    "href": "/objects/construction-forecasting/wip-project-manager-forecast/18"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-project-manager-forecast/{key}
_Get a WIP project manager forecast_

**Response 200 — Details of a WIP project manager forecast:**
```json
{
  "ia::result": {
    "task": {
      "name": "Permits",
      "id": "00 31 46",
      "key": "590",
      "href": "/objects/projects/task/590"
    },
    "costType": {
      "name": "Other DIM-BTI 0001",
      "id": "OTH",
      "key": "18",
      "href": "/objects/construction/cost-type/18"
    },
    "project": {
      "name": "The Sugar Shoppe",
      "id": "22-006",
      "key": "134",
      "href": "/objects/projects/project/134"
    },
    "wipPeriod": {
      "id": "92",
      "key": "92",
      "href": "/objects/construction-forecasting/wip-project/92"
    },
    "assignedEntity": {
      "id": "1",
      "key": "1",
      "name": "United States",
      "href": "/objects/company-config/entity/1"
    },
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2024-08-20T17:44:28Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2024-08-20T17:44:28Z",
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
    "periodEndDate": "2024-08-31",
    "costToComplete": "1500",
    "percentComplete": 90,
    "estimateVsForecastVariance": "200.11",
    "id": "18",
    "key": "18",
    "costAtCompletion": "9000",
    "notes": "Work completed",
    "updatedDateTime": "2024-08-20T17:44:28Z",
    "href": "/objects/construction-forecasting/wip-project-manager-forecast/18"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction-forecasting/wip-project-manager-forecast/{key}
_Update a WIP project manager forecast_

**Request example — Update a WIP project manager forecast:**
```json
{
  "notes": "Replaced the task ID.",
  "task": {
    "id": "00 31 46"
  },
  "updatedDateTime": "2024-08-20T17:44:28Z"
}
```
**Response 200 — Reference to updated WIP project manager forecast:**
```json
{
  "ia::result": {
    "key": "18",
    "id": "18",
    "href": "/objects/construction-forecasting/wip-project-manager-forecast/18"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction-forecasting/wip-project-manager-forecast/{key}
_Delete a WIP project manager forecast_


## GET /objects/construction-forecasting/wip-project-setting
_List WIP project settings_

**Response 200 — List WIP project settings:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "P-040",
      "href": "/objects/construction-forecasting/wip-project-setting/100"
    },
    {
      "key": "101",
      "id": "P-050",
      "href": "/objects/construction-forecasting/wip-project-setting/101"
    },
    {
      "key": "102",
      "id": "P-060",
      "href": "/objects/construction-forecasting/wip-project-setting/102"
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

## POST /objects/construction-forecasting/wip-project-setting
_Create a WIP project setting_

**Request example — Create a WIP project setting:**
```json
{
  "wipTargetProject": {
    "id": "106"
  },
  "costsCompleteDate": "2023-01-31",
  "billingsCompleteDate": "2023-04-30",
  "usePrimaryForecast": false
}
```
**Response 201 — Reference to new WIP project setting:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "11",
    "href": "/objects/construction-forecasting/wip-project-setting/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-project-setting/{key}
_Get a WIP project setting_

**Response 200 — Get a WIP project setting:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "10",
    "wipTargetProject": {
      "key": "106",
      "id": "P-0045",
      "name": "Implementation Project",
      "href": "/objects/construction-forecasting/wip-target-project/106"
    },
    "costsCompleteDate": "2023-01-31",
    "billingsCompleteDate": "2023-04-30",
    "usePrimaryForecast": false,
    "href": "/objects/construction-forecasting/wip-project-setting/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction-forecasting/wip-project-setting/{key}
_Update a WIP project setting_

**Request example — Update a WIP project setting:**
```json
{
  "costsCompleteDate": null,
  "billingsCompleteDate": "2023-01-31",
  "usePrimaryForecast": true
}
```
**Response 200 — Reference to an updated WIP project setting:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "10",
    "href": "/objects/construction-forecasting/wip-project-setting/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction-forecasting/wip-project-setting/{key}
_Delete a WIP project setting_


## GET /objects/construction-forecasting/wip-project/{key}
_Get a WIP project_

**Response 200 — Details of a WIP project:**
```json
{
  "ia::result": {
    "projectStatus": {
      "id": "In Progress",
      "key": "1",
      "href": "/objects/projects/project-status/1"
    },
    "manager": {
      "name": "Moffet; Doug W",
      "id": "EMP00025",
      "key": "25",
      "href": "/objects/company-config/employee/1"
    },
    "projectType": {
      "id": "Warehouse",
      "key": "3",
      "href": "/objects/projects/project-type/3"
    },
    "location": {
      "name": "Beaverton",
      "id": "BEAVERTON",
      "key": "8",
      "href": "/objects/company-config/location/8"
    },
    "class": {
      "name": "Construction class",
      "id": "Construction class",
      "key": "2",
      "href": "/objects/company-config/class/2"
    },
    "department": {
      "name": "Construction Operations",
      "id": "OPERATIONS",
      "key": "1",
      "href": "/objects/company-config/department/1"
    },
    "wipPeriod": {
      "periodName": "Month Ended October 2023",
      "wipCostBreakdownLevel": "costCodeAndCostType",
      "id": "54",
      "key": "54",
      "href": "/objects/construction-forecasting/wip-period/54"
    },
    "project": {
      "endDate": "2023-07-31",
      "projectCurrency": "USD",
      "name": "Quick Bowls - Portland1",
      "description": "Fast food restaurant with drive-thru",
      "id": "22-001",
      "key": "1",
      "startDate": "2022-01-03",
      "status": "active"
    },
    "forecastDetails": [
      {
        "wipPeriod": {
          "periodName": "Month Ended October 2023",
          "id": "54",
          "key": "54"
        },
        "task": {
          "name": "Finish Carpentry",
          "id": "06 20 00",
          "key": "538"
        },
        "costType": {
          "name": "Subcontract",
          "id": "SUB",
          "key": "1496"
        },
        "project": {
          "name": "Quick Bowls - Portland1",
          "id": "22-001",
          "key": "1"
        },
        "wipProject": {
          "id": "338",
          "key": "338"
        },
        "assignedEntity": {
          "name": "Timberline GC",
          "id": "TIMBGC",
          "key": "3"
        },
        "rootTask": {
          "name": "WOOD PLASTICS AND COMPOSITES",
          "id": "06 00 00",
          "key": "537"
        },
        "priorPeriodProjectManagerForecast": {
          "costAtCompletion": "900",
          "costToComplete": "500",
          "percentComplete": "80"
        },
        "costAndEstimateDetail": {
          "estimatedCostAtCompletion": "5200",
          "jobToDateCosts": "5200",
          "estimatedCostToDateAmount": "5200",
          "key": "7829"
        },
        "projectManagerForecast": {
          "costToCompleteVariance": "900",
          "costAtCompletionVariance": "500"
        },
        "id": "782900000000",
        "key": "782900000000"
      },
      {
        "wipPeriod": {
          "periodName": "Month Ended October 2023",
          "id": "54",
          "key": "54"
        },
        "task": {
          "name": "Fees",
          "id": "01 41 23",
          "key": "259"
        },
        "costType": {
          "name": "Other",
          "id": "OTH",
          "key": "835"
        },
        "project": {
          "name": "Quick Bowls - Portland1",
          "id": "22-001",
          "key": "1"
        },
        "wipProject": {
          "id": "338",
          "key": "338"
        },
        "assignedEntity": {
          "name": "Timberline GC",
          "id": "TIMBGC",
          "key": "3"
        },
        "rootTask": {
          "name": "GENERAL REQUIREMENTS",
          "id": "01 00 00",
          "key": "255"
        },
        "priorPeriodProjectManagerForecast": {
          "costAtCompletion": "900",
          "costToComplete": "500",
          "percentComplete": "80"
        },
        "costAndEstimateDetail": {
          "estimatedCostAtCompletion": "1100",
          "jobToDateCosts": "6590",
          "estimatedCostToDateAmount": "1100",
          "key": "7836"
        },
        "projectManagerForecast": {
          "costToCompleteVariance": "900",
          "costAtCompletionVariance": "500"
        },
        "id": "783600000000",
        "key": "783600000000"
      }
    ],
    "audit": {
      "createdBy": "1",
      "createdDateTime": "2024-12-11T17:36:42Z",
      "modifiedBy": "1",
      "modifiedDateTime": "2025-01-03T21:13:13Z",
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
    "projectManagerForecast": {
      "contractValue": "179610",
      "costAtCompletion": "900",
      "costToComplete": "-308235.95",
      "percentComplete": "-9999"
    },
    "cfoForecast": {
      "contractValue": "179610",
      "lastUpdatedDate": "2024-12-26T16:35:22Z",
      "costAtCompletion": "450000.6",
      "costToComplete": "140864.65",
      "percentComplete": "68.7"
    },
    "customer": {
      "name": "Trammel Crow",
      "id": "C00002",
      "key": "2",
      "href": "/objects/accounts-receivable/customer/2"
    },
    "jobToDateUnderbillingAmount": "100490.07",
    "remainingProfit": "-84646.72",
    "currentPeriodEarnedProfitAmount": "0",
    "totalContractValue": "179610",
    "currentPeriodEarnedRevenueAmount": "0",
    "endOfPriorYearEarnedToDateAmount": "0",
    "earnedProfitToDateAmount": "-185743.88",
    "cfoForecastGrossProfitAtCompletion": "-270390.6",
    "costAtCompletionVariance": "21244.06",
    "currentPeriodBillingAmount": "0",
    "grossProfitPercentOfContract": "-150.54",
    "estimatedCostToComplete": "119620.59",
    "overUnderBillingAmount": "100490.07",
    "yearToDateBillingAmount": "0",
    "isFinalized": false,
    "grossProfitVarianceAmount": "-21244.06",
    "jobToDateOverbillingAmount": "0",
    "estimatedPercentComplete": "72.1",
    "yearToDateEarnedProfitAmount": "-185743.88",
    "jobToDateCosts": "309135.95",
    "endOfPriorYearEarnedProfit": "0",
    "grossProfitPercentOfCost": "-60.09",
    "remainingBacklogAmount": "56217.93",
    "id": "338",
    "estimatedCostToDateAmount": "428756.54",
    "contractVarianceAmount": "0",
    "key": "338",
    "currentPeriodCostAmount": "0",
    "yearToDateCostAmount": "0",
    "cfoForecastGrossProfitMarginPercent": "-150.54",
    "yearToDateEarnedRevenueAmount": "123392.07",
    "totalGrossProfitEstimatedAtCompletion": "-249146.54",
    "jobToDateBillings": "22902",
    "earnedToDateAmount": "123392.07",
    "estimatedCostAtCompletion": "428756.54",
    "pendingEstimatesAmount": "0",
    "hasAnomaly": false,
    "isCostsComplete": false,
    "isBillingsComplete": false,
    "basedOnPrimaryForecast": false,
    "createdFromEntity": {
      "name": "Timberline GC",
      "id": "TIMBGC",
      "key": "3",
      "href": "/objects/company-config/entity/3"
    },
    "assignedEntity": {
      "name": "Timberline GC",
      "id": "TIMBGC",
      "key": "3",
      "href": "/objects/company-config/entity/3"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction-forecasting/wip-project/{key}
_Update a WIP project_

**Request example — Update a WIP project:**
```json
{
  "isFinalized": true,
  "notes": "Done with editing"
}
```
**Response 200 — Reference to updated WIP project:**
```json
{
  "ia::result": {
    "key": "41",
    "id": "41",
    "href": "/objects/construction-forecasting/wip-project/41"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-setup
_List WIP setups_

**Response 200 — List WIP setups:**
```json
{
  "ia::result": [
    {
      "id": "1",
      "key": "1",
      "href": "/objects/construction-forecasting/wip-setup/1"
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

## POST /objects/construction-forecasting/wip-setup
_Create a WIP setup_

**Request example — Creates a WIP setup:**
```json
{
  "wipSetupAccounts": [
    {
      "account": {
        "id": "5000"
      },
      "wipAccountType": "cost"
    },
    {
      "account": {
        "id": "5001"
      },
      "wipAccountType": "cost"
    },
    {
      "account": {
        "id": "4000"
      },
      "wipAccountType": "revenue"
    },
    {
      "account": {
        "id": "4001"
      },
      "wipAccountType": "revenue"
    },
    {
      "account": {
        "id": "4008"
      },
      "wipAccountType": "revenue"
    },
    {
      "account": {
        "id": "1002"
      },
      "wipAccountType": "underbillingOffset"
    },
    {
      "account": {
        "id": "1003"
      },
      "wipAccountType": "overbillingOffset"
    },
    {
      "account": {
        "id": "1000"
      },
      "wipAccountType": "overbilling"
    },
    {
      "account": {
        "id": "1001"
      },
      "wipAccountType": "underbilling"
    }
  ],
  "autoCreateNextPeriod": true,
  "postingJournal": {
    "id": "APJ"
  },
  "reconciliationMethod": "autoReverse",
  "wipCostBreakdownLevel": "costCodeAndCostType",
  "includeZeroJobToDateAmounts": true,
  "usePrimaryForecasts": false
}
```
**Response 201 — Reference to new WIP setup:**
```json
{
  "ia::result": {
    "key": "41",
    "id": "41",
    "href": "/objects/construction-forecasting/wip-setup/41"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-setup-account
_List WIP setup accounts_

**Response 200 — List WIP setup accounts:**
```json
{
  "ia::result": [
    {
      "id": "1",
      "key": "1",
      "href": "/objects/construction-forecasting/wip-setup-account/1"
    },
    {
      "id": "2",
      "key": "2",
      "href": "/objects/construction-forecasting/wip-setup-account/2"
    }
  ],
  "ia::meta": {
    "totalCount": 2,
    "totalSuccess": 2,
    "totalError": 0
  }
}
```

## POST /objects/construction-forecasting/wip-setup-account
_Create a WIP setup account_

**Request example — Creates a WIP setup account:**
```json
{
  "account": {
    "id": "5000"
  },
  "wipAccountType": "cost"
}
```
**Response 201 — Reference to new WIP setup account:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/construction-forecasting/wip-setup-account/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-setup-account/{key}
_Get a WIP setup account_

**Response 200 — Details of a WIP setup account:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "wipAccountType": "underbillingOffset",
    "account": {
      "key": 99,
      "id": "1001",
      "name": "CitiBank",
      "href": "/objects/general-ledger/account/99"
    },
    "audit": {
      "createdDateTime": "2023-06-02T20:29:28Z",
      "modifiedDateTime": "2023-06-02T20:29:28Z",
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
    "href": "/objects/construction-forecasting/wip-setup-account/1",
    "wipSetup": {
      "key": "123",
      "id": "123",
      "href": "/objects/construction-forecasting/wip-setup/123"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction-forecasting/wip-setup-account/{key}
_Update a WIP setup account_

**Request example — Update WIP setup account:**
```json
{
  "account": {
    "id": "1001"
  },
  "wipAccountType": "cost",
  "key": "1"
}
```
**Response 200 — Reference to updated WIP setup:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/construction-forecasting/wip-setup-account/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction-forecasting/wip-setup-account/{key}
_Delete a WIP setup account_


## GET /objects/construction-forecasting/wip-setup/{key}
_Get a WIP setup_

**Response 200 — Details of a WIP setup:**
```json
{
  "ia::result": {
    "wipSetupAccounts": [
      {
        "audit": {
          "createdDateTime": "2023-10-27T18:08:24Z",
          "modifiedDateTime": "2023-10-27T18:08:24Z",
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
        "account": {
          "key": 101,
          "id": "5000",
          "name": "Cost of Goods Sold",
          "href": "/objects/general-ledger/account/101"
        },
        "wipAccountType": "cost",
        "id": "123",
        "key": "123",
        "href": "/objects/construction-forecasting/wip-setup-account/123"
      },
      {
        "audit": {
          "createdDateTime": "2023-10-27T18:08:24Z",
          "modifiedDateTime": "2023-10-27T18:08:24Z",
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
        "account": {
          "key": 102,
          "id": "4000",
          "name": "Sales",
          "href": "/objects/general-ledger/account/102"
        },
        "wipAccountType": "revenue",
        "id": "125",
        "key": "125",
        "href": "/objects/construction-forecasting/wip-setup-account/125"
      },
      {
        "audit": {
          "createdDateTime": "2023-10-27T18:08:24Z",
          "modifiedDateTime": "2023-10-27T18:08:24Z",
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
        "account": {
          "key": 103,
          "id": "4001",
          "name": "Miscellaneous Sales",
          "href": "/objects/general-ledger/account/103"
        },
        "wipAccountType": "revenue",
        "id": "126",
        "key": "126",
        "href": "/objects/construction-forecasting/wip-setup-account/126"
      },
      {
        "audit": {
          "createdDateTime": "2023-10-27T18:08:24Z",
          "modifiedDateTime": "2023-10-27T18:08:24Z",
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
        "account": {
          "key": 104,
          "id": "1002",
          "name": "HSBC - GBP",
          "href": "/objects/general-ledger/account/104"
        },
        "wipAccountType": "offset",
        "id": "127",
        "key": "127",
        "href": "/objects/construction-forecasting/wip-setup-account/127"
      },
      {
        "audit": {
          "createdDateTime": "2023-10-27T18:08:24Z",
          "modifiedDateTime": "2023-10-27T18:08:24Z",
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
        "account": {
          "key": 98,
          "id": "1000",
          "name": "Bank of America A/c.",
          "href": "/objects/general-ledger/account/98"
        },
        "wipAccountType": "overbilling",
        "id": "128",
        "key": "128",
        "href": "/objects/construction-forecasting/wip-setup-account/128"
      },
      {
        "audit": {
          "createdDateTime": "2023-10-27T18:08:24Z",
          "modifiedDateTime": "2023-10-27T18:08:24Z",
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
        "account": {
          "key": 99,
          "id": "1001",
          "name": "CitiBank",
          "href": "/objects/general-ledger/account/99"
        },
        "wipAccountType": "underbilling",
        "id": "129",
        "key": "129",
        "href": "/objects/construction-forecasting/wip-setup-account/129"
      }
    ],
    "audit": {
      "createdDateTime": "2023-10-27T18:08:24Z",
      "modifiedDateTime": "2023-10-27T18:08:24Z",
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
    "autoCreateNextPeriod": true,
    "includeZeroJobToDateAmounts": true,
    "usePrimaryForecasts": false,
    "postingJournal": {
      "key": 9,
      "id": "APJ",
      "name": "Account payable journal",
      "href": "/objects/general-ledger/journal/9"
    },
    "wipCostBreakdownLevel": "costCode",
    "id": "27",
    "reconciliationMethod": "autoReverse",
    "key": "27",
    "href": "/objects/construction-forecasting/wip-setup/27"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction-forecasting/wip-setup/{key}
_Update a WIP setup_

**Request example — Update, delete, and add WIP setup accounts:**
```json
{
  "wipSetupAccounts": [
    {
      "account": {
        "id": "1001"
      },
      "wipAccountType": "cost",
      "key": "1"
    },
    {
      "key": "2",
      "ia::operation": "delete"
    },
    {
      "account": {
        "id": "1000"
      },
      "wipAccountType": "revenue"
    }
  ],
  "autoCreateNextPeriod": true,
  "includeZeroJobToDateAmounts": true,
  "usePrimaryForecasts": false,
  "postingJournal": {
    "id": "APJ"
  },
  "wipCostBreakdownLevel": "project",
  "reconciliationMethod": "autoReverse"
}
```
**Response 200 — Reference to updated WIP setup:**
```json
{
  "ia::result": {
    "key": "41",
    "id": "41",
    "href": "/objects/construction-forecasting/wip-setup/41"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction-forecasting/wip-target-project
_List WIP target projects_

**Response 200 — List WIP target projects:**
```json
{
  "ia::result": [
    {
      "key": "100",
      "id": "P-040",
      "href": "/objects/construction-forecasting/wip-target-project/100"
    },
    {
      "key": "101",
      "id": "P-050",
      "href": "/objects/construction-forecasting/wip-target-project/101"
    },
    {
      "key": "102",
      "id": "P-060",
      "href": "/objects/construction-forecasting/wip-target-project/102"
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

## GET /objects/construction-forecasting/wip-target-project/{key}
_Get a WIP target project_

**Response 200 — Get a WIP target project:**
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
    "entity": {
      "key": null,
      "id": null,
      "name": null
    },
    "wipProjectSetting": {
      "key": "10",
      "id": "10",
      "costsCompleteDate": "2023-01-31",
      "billingsCompleteDate": "2023-04-30",
      "usePrimaryForecast": false,
      "href": "/objects/construction-forecasting/wip-project-setting/10"
    },
    "href": "/objects/construction-forecasting/wip-target-project/106"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction-forecasting/wip-target-project/{key}
_Update a WIP target project_

**Request example — Update a WIP target project:**
```json
{
  "wipProjectSetting": {
    "costsCompleteDate": null,
    "billingsCompleteDate": "2023-01-31",
    "usePrimaryForecast": true
  }
}
```
**Response 200 — Reference to updated WIP target project:**
```json
{
  "ia::result": {
    "key": "106",
    "id": "P-0345",
    "href": "/objects/construction-forecasting/wip-target-project/106"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/accumulation-type
_List accumulation types_

**Response 200 — List of accumulation types:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "Direct cost",
      "href": "/objects/construction/accumulation-type/1"
    },
    {
      "key": "2",
      "id": "Indirect cost",
      "href": "/objects/construction/accumulation-type/2"
    },
    {
      "key": "3",
      "id": "Equipment cost",
      "href": "/objects/construction/accumulation-type/3"
    }
  ],
  "ia::meta": {
    "totalCount": 3,
    "start": 1,
    "pageSize": 50,
    "next": null,
    "previous": null
  }
}
```

## POST /objects/construction/accumulation-type
_Create an accumulation type_

**Request example — Creates an accumulation type:**
```json
{
  "id": "Direct cost",
  "status": "active",
  "costCategory": "material"
}
```
**Response 201 — Reference to new accumulation type:**
```json
{
  "ia::result": {
    "key": "40",
    "id": "40",
    "href": "/objects/construction/accumulation-type/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/accumulation-type/{key}
_Get an accumulation type_

**Response 200 — Details of the accumulation type:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "Direct cost",
    "status": "active",
    "audit": {
      "createdDateTime": "2023-10-14T15:12:40Z",
      "modifiedDateTime": "2023-10-14T15:12:40Z",
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
    "costCategory": "labor",
    "href": "/objects/construction/accumulation-type/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/accumulation-type/{key}
_Update an accumulation type_

**Request example — Updates the costCategory:**
```json
{
  "costCategory": "other"
}
```
**Response 200 — Reference to updated accumulation type:**
```json
{
  "ia::result": {
    "key": "40",
    "id": "Direct cost",
    "href": "/objects/construction/accumulation-type/40"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/accumulation-type/{key}
_Delete an accumulation type_


## GET /objects/construction/ap-releasable-retainage
_List AP releasable retainage_

**Response 200 — List of AP releasable retainage:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/ap-releasable-retainage/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/ap-releasable-retainage/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/ap-releasable-retainage/3"
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

## GET /objects/construction/ap-releasable-retainage/{key}
_Get an AP releasable retainage_

**Response 200 — Details of the AP releasable retainage:**
```json
{
  "ia::result": {
    "id": "1",
    "key": "1",
    "retainageBillLine": {
      "id": "1",
      "key": "1",
      "href": "/objects/accounts-payable/bill-line/1"
    },
    "retainageBill": {
      "id": "15",
      "key": "15",
      "href": "/objects/accounts-payable/bill/15"
    },
    "lineNumber": 1,
    "billLineAmount": "10000.00",
    "txnBillLineAmount": "10000.00",
    "amountRetained": "1000.00",
    "txnAmountRetained": "1000.00",
    "txnTotalReleased": "500.00",
    "txnAmountRemaining": "500.00",
    "documentLineKey": "14",
    "department": {
      "key": "9",
      "id": "Forecasting",
      "href": "/objects/company-config/department/9"
    },
    "primaryDocument": {
      "key": "2",
      "id": "Subcontract-SUB-00002",
      "href": "/objects/order-entry/document/2"
    },
    "primaryDocumentLine": {
      "key": "2",
      "id": "1--Subcontract",
      "href": "/objects/order-entry/document-line/2"
    },
    "href": "/objects/construction/ap-releasable-retainage/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/ap-retainage-release
_List AP retainage releases_

**Response 200 — List of AP retainage releases:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/ap-retainage-release/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/ap-retainage-release/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/ap-retainage-release/3"
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

## POST /objects/construction/ap-retainage-release
_Create an AP retainage release_

**Request example — Create an AP retainage release:**
```json
{
  "id": "19",
  "description": "AP ret rel desc 101",
  "releaseDate": "2025-03-02",
  "glPostingDate": "2025-03-02",
  "state": "draft",
  "apRetainageReleaseLines": [
    {
      "txnAmountReleased": "123.00",
      "retainageBill": {
        "key": "232"
      },
      "retainageBillLine": {
        "key": "803"
      }
    }
  ]
}
```
**Response 201 — Reference to new AP retainage release:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "4",
    "href": "/objects/construction/ap-retainage-release/4"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## GET /objects/construction/ap-retainage-release-line
_List AP retainage release lines_

**Response 200 — List of AP retainage release lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/ap-retainage-release-line/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/ap-retainage-release-line/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/ap-retainage-release-line/3"
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

## GET /objects/construction/ap-retainage-release-line/{key}
_Get an AP retainage release line_

**Response 200 — Details of the AP retainage release line:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "7",
    "apRetainageRelease": {
      "id": "2",
      "key": "2",
      "href": "/objects/construction/ap-retainage-release/2"
    },
    "purchasingDocument": {
      "key": "11",
      "id": "Subcontract Invoice-SUBINV#0106#doc",
      "href": "/objects/purchasing/document/11"
    },
    "retainageBill": {
      "key": "1",
      "id": "SUBINV#0106#doc",
      "href": "/objects/accounts-payable/bill/1"
    },
    "retainageBillLine": {
      "id": "1",
      "key": "1",
      "href": "/objects/accounts-payable/bill-line/1"
    },
    "txnAmountReleased": "500.00",
    "releasedBill": {
      "key": "11",
      "id": "APRET-00002",
      "href": "/objects/accounts-payable/bill/11"
    },
    "releasedBillLine": {
      "id": "45",
      "key": "45",
      "href": "/objects/accounts-payable/bill-line/45"
    },
    "audit": {
      "createdDateTime": "2025-04-04T00:00:00Z",
      "modifiedDateTime": "2025-04-04T00:00:00Z",
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
    "href": "/objects/construction/ap-retainage-release-line/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/ap-retainage-release/{key}
_Get an AP retainage release_

**Response 200 — Details of the AP retainage release:**
```json
{
  "ia::result": {
    "id": "2",
    "key": "2",
    "description": "Release A-1 Electric retainage",
    "releaseDate": "2025-03-21",
    "glPostingDate": "2025-03-21",
    "state": "released",
    "audit": {
      "createdDateTime": "2025-04-04T00:00:00Z",
      "modifiedDateTime": "2025-04-04T00:00:00Z",
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
      "id": "CORP",
      "name": "Corp",
      "href": "/objects/company-config/entity/46"
    },
    "apRetainageReleaseLines": [
      {
        "id": "2",
        "key": "2",
        "apRetainageRelease": {
          "id": "2",
          "key": "2",
          "href": "/objects/construction/ap-retainage-release/2"
        },
        "purchasingDocument": {
          "key": "11",
          "id": "Subcontract Invoice-SUBINV#0106#doc",
          "href": "/objects/purchasing/document/11"
        },
        "retainageBill": {
          "key": "1",
          "id": "SUBINV#0106#doc",
          "href": "/objects/accounts-payable/bill/1"
        },
        "retainageBillLine": {
          "id": "1",
          "key": "1",
          "href": "/objects/accounts-payable/bill-line/1"
        },
        "txnAmountReleased": "500.00",
        "releasedBill": {
          "key": "11",
          "id": "APRET-00002",
          "href": "/objects/accounts-payable/bill/11"
        },
        "releasedBillLine": {
          "id": "45",
          "key": "45",
          "href": "/objects/accounts-payable/bill-line/45"
        },
        "audit": {
          "createdDateTime": "2025-04-04T00:00:00Z",
          "modifiedDateTime": "2025-04-04T00:00:00Z",
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
        "href": "/objects/construction/ap-retainage-release-line/2"
      }
    ],
    "href": "/objects/construction/ap-retainage-release/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/ap-retainage-release/{key}
_Update an AP retainage release_

**Request example — Updates an AP retainage release:**
```json
{
  "releaseDate": "2025-04-01",
  "glPostingDate": "2025-04-01"
}
```
**Response 200 — Reference to updated AP retainage release:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "4",
    "href": "/objects/construction/ap-retainage-release/4"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/construction/ap-retainage-release/{key}
_Delete an AP retainage release_


## GET /objects/construction/ar-releasable-retainage
_List AR releasable retainage_

**Response 200 — List of AR releasable retainage:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/ar-releasable-retainage/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/ar-releasable-retainage/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/ar-releasable-retainage/3"
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

## GET /objects/construction/ar-releasable-retainage/{key}
_Get an AR releasable retainage_

**Response 200 — Details of the AR releasable retainage:**
```json
{
  "ia::result": {
    "id": "2902",
    "key": "2902",
    "retainageInvoiceLine": {
      "id": "2902",
      "key": "2902",
      "href": "/objects/accounts-receivable/invoice-line/2902"
    },
    "retainageInvoice": {
      "id": "450",
      "key": "450",
      "href": "/objects/accounts-receivable/invoice/450"
    },
    "lineNumber": 3,
    "invoiceLineAmount": "188220.00",
    "txnInvoiceLineAmount": "188220.00",
    "amountRetained": "18822.00",
    "txnAmountRetained": "18822.00",
    "txnTotalReleased": "0.00",
    "txnAmountRemaining": "18822.00",
    "documentLineKey": "1199",
    "department": {
      "key": "9",
      "id": "Maintenance",
      "href": "/objects/company-config/department/9"
    },
    "location": {
      "key": "1",
      "id": "1",
      "href": "/objects/company-config/location/1"
    },
    "projectContract": {
      "id": "ST-001",
      "key": "16",
      "href": "/objects/construction/project-contract/16"
    },
    "projectContractLine": {
      "id": "Concrete",
      "key": "29",
      "href": "/objects/construction/project-contract-line/29"
    },
    "href": "/objects/construction/ar-releasable-retainage/2902"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/ar-retainage-release
_List AR retainage releases_

**Response 200 — List of AR retainage releases:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/ar-retainage-release/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/ar-retainage-release/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/ar-retainage-release/3"
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

## POST /objects/construction/ar-retainage-release
_Create an AR retainage release_

**Request example — Creates an AR retainage release:**
```json
{
  "id": "19",
  "description": "AR ret rel desc 101",
  "releaseDate": "2025-03-02",
  "glPostingDate": "2025-03-02",
  "state": "draft",
  "arRetainageReleaseLines": [
    {
      "txnAmountReleased": "123.00",
      "retainageInvoice": {
        "key": "232"
      },
      "retainageInvoiceLine": {
        "key": "803"
      }
    }
  ]
}
```
**Response 201 — Reference to new AR retainage release:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "4",
    "href": "/objects/construction/ar-retainage-release/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/ar-retainage-release-line
_List AR retainage release lines_

**Response 200 — List of AR retainage release lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/ar-retainage-release-line/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/ar-retainage-release-line/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/ar-retainage-release-line/3"
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

## GET /objects/construction/ar-retainage-release-line/{key}
_Get an AR retainage release line_

**Response 200 — Details of the AR retainage release line:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "7",
    "arRetainageRelease": {
      "id": "60",
      "key": "60",
      "href": "/objects/construction/ar-retainage-release/60"
    },
    "salesOrderDocument": {
      "key": "490",
      "id": "Project contract invoice-PCI-00151",
      "href": "/objects/order-entry/document/490"
    },
    "retainageInvoice": {
      "key": "443",
      "id": "PCI-00151",
      "href": "/objects/accounts-receivable/invoice/443"
    },
    "retainageInvoiceLine": {
      "id": "2870",
      "key": "2870",
      "href": "/objects/accounts-receivable/invoice-line/2870"
    },
    "txnAmountReleased": "17500.00",
    "releasedInvoice": {
      "key": "451",
      "id": "ARRET-00040",
      "href": "/objects/accounts-receivable/invoice/451"
    },
    "releasedInvoiceLine": {
      "id": "2908",
      "key": "2908",
      "href": "/objects/accounts-receivable/invoice-line/2908"
    },
    "audit": {
      "createdDateTime": "2025-02-28T00:00:00Z",
      "modifiedDateTime": "2025-02-28T00:00:00Z",
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
    "projectContract": {
      "id": "ST-001",
      "key": "16",
      "href": "/objects/construction/project-contract/16"
    },
    "projectContractLine": {
      "id": "1",
      "key": "28",
      "href": "/objects/construction/project-contract-line/28"
    },
    "href": "/objects/construction/ar-retainage-release-line/178"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/ar-retainage-release/{key}
_Get an AR retainage release_

**Response 200 — Details of the AR retainage release:**
```json
{
  "ia::result": {
    "id": "60",
    "key": "60",
    "description": "Project contract invoice-PCI-00153",
    "releaseDate": "2024-03-31",
    "glPostingDate": "2024-03-31",
    "state": "released",
    "audit": {
      "createdDateTime": "2025-02-28T00:00:00Z",
      "modifiedDateTime": "2025-02-28T00:00:00Z",
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
      "id": "CORP",
      "name": "Corp",
      "href": "/objects/company-config/entity/46"
    },
    "arRetainageReleaseLines": [
      {
        "id": "178",
        "key": "178",
        "arRetainageRelease": {
          "id": "60",
          "key": "60",
          "href": "/objects/construction/ar-retainage-release/60"
        },
        "salesOrderDocument": {
          "key": "490",
          "id": "Project contract invoice-PCI-00151",
          "href": "/objects/order-entry/document/490"
        },
        "retainageInvoice": {
          "key": "443",
          "id": "PCI-00151",
          "href": "/objects/accounts-receivable/invoice/443"
        },
        "retainageInvoiceLine": {
          "id": "2870",
          "key": "2870",
          "href": "/objects/accounts-receivable/invoice-line/2870"
        },
        "txnAmountReleased": "17500.00",
        "releasedInvoice": {
          "key": "451",
          "id": "ARRET-00040",
          "href": "/objects/accounts-receivable/invoice/451"
        },
        "releasedInvoiceLine": {
          "id": "2908",
          "key": "2908",
          "href": "/objects/accounts-receivable/invoice-line/2908"
        },
        "audit": {
          "createdDateTime": "2025-02-28T00:00:00Z",
          "modifiedDateTime": "2025-02-28T00:00:00Z",
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
        "projectContract": {
          "id": "ST-001",
          "key": "16",
          "href": "/objects/construction/project-contract/16"
        },
        "projectContractLine": {
          "id": "1",
          "key": "28",
          "href": "/objects/construction/project-contract-line/28"
        },
        "href": "/objects/construction/ar-retainage-release-line/178"
      }
    ],
    "href": "/objects/construction/ar-retainage-release/60"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/ar-retainage-release/{key}
_Update an AR retainage release_

**Request example — Updates an AR retainage release:**
```json
{
  "description": "Updated"
}
```
**Response 200 — Updated AR retainage release:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "4",
    "href": "/objects/construction/ar-retainage-release/4"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/construction/ar-retainage-release/{key}
_Delete an AR retainage release_


## GET /objects/construction/change-request
_List change requests_

**Response 200 — List change requests:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "CR-1",
      "href": "/objects/construction/change-request/1"
    },
    {
      "key": "2",
      "id": "CR-2",
      "href": "/objects/construction/change-request/2"
    },
    {
      "key": "3",
      "id": "CR-3",
      "href": "/objects/construction/change-request/3"
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

## POST /objects/construction/change-request
_Create a change request_

**Request example — Creates a change request:**
```json
{
  "id": "CR-4",
  "changeRequestDate": "2021-11-11",
  "project": {
    "key": "12"
  }
}
```
**Response 201 — Reference to new change request:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "CR-4",
    "href": "/objects/construction/change-request/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/change-request-line
_List change request lines_

**Response 200 — List change request lines:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/change-request-line/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/change-request-line/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/change-request-line/3"
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

## GET /objects/construction/change-request-line/{key}
_Get a change request line_

**Response 200 — Details of the change request line:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "7",
    "changeRequest": {
      "key": "11",
      "id": "REST-CR-02",
      "href": "/objects/construction/change-request/11"
    },
    "workflowType": "none",
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
      },
      "department": {
        "key": "3",
        "id": "3",
        "name": "Engineering",
        "href": "/objects/company-config/department/3"
      },
      "project": {
        "key": "1",
        "id": "DIM - BTI",
        "name": "Dimensions - Berkeley Technology Inc",
        "href": "/objects/projects/project/1"
      },
      "customer": {
        "key": "14",
        "id": "BTI",
        "name": "Berkeley Technology Inc",
        "href": "/objects/accounts-receivable/customer/14"
      },
      "vendor": {
        "key": "43",
        "id": "1099 Int",
        "name": "1099 Int",
        "href": "/objects/accounts-payable/vendor/43"
      },
      "employee": {
        "key": "27",
        "id": "12",
        "name": "Eberhardt",
        "href": "/objects/company-config/employee/27"
      },
      "item": {
        "key": "240",
        "id": "3",
        "name": "Rebar #10",
        "href": "/objects/inventory-control/item/240"
      },
      "class": {
        "key": "6",
        "id": "4",
        "name": "Professional Services",
        "href": "/objects/company-config/class/6"
      },
      "task": {
        "key": "3",
        "id": "1020",
        "name": "Roofing",
        "href": "/objects/projects/task/3"
      },
      "costType": {
        "key": "8",
        "id": "L",
        "name": "Labor",
        "href": "/objects/costType/8"
      }
    },
    "numberOfProductionUnits": "1200",
    "productionUnitDescription": "sqft",
    "quantity": "5.00",
    "externalUOM": "each",
    "unitCost": "32.00",
    "cost": "160.00",
    "unitPrice": "40.00",
    "price": "200.00",
    "priceMarkupPercent": "10.00",
    "priceMarkupAmount": "20.00",
    "linePrice": "220.00",
    "projectChangeOrder": {
      "key": "2",
      "id": "PCO2-DIMBTI",
      "href": "/objects/construction/project-change-order/2"
    },
    "memo": "CR Line 02",
    "projectEstimate": {
      "key": "1",
      "id": "BTI-01",
      "href": "/objects/construction/project-estimate/1"
    },
    "glAccount": {
      "key": "35",
      "id": "5001",
      "name": "Construction",
      "href": "/objects/general-ledger/account/35"
    },
    "projectContract": {
      "key": "4",
      "id": "PCN-04",
      "name": "Construction",
      "href": "/objects/construction/project-contract/4"
    },
    "projectContractLine": {
      "key": "6",
      "id": "PCL-06",
      "name": "Construction",
      "href": "/objects/construction/project-contract-line/6"
    },
    "lineNo": "1",
    "audit": {
      "createdDateTime": "2023-06-14T13:56:42Z",
      "modifiedDateTime": "2023-06-14T13:56:43Z",
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
    "href": "/objects/construction/change-request-line/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/change-request-status
_List change request statuses_

**Response 200 — List of change request statuses:**
```json
{
  "ia::result": [
    {
      "key": "21",
      "id": "Not issued",
      "href": "/objects/construction/change-request-status/21"
    },
    {
      "key": "22",
      "id": "Approved",
      "href": "/objects/construction/change-request-status/22"
    },
    {
      "key": "23",
      "id": "Original",
      "href": "/objects/construction/change-request-status/23"
    },
    {
      "key": "24",
      "id": "Revised",
      "href": "/objects/construction/change-request-status/24"
    },
    {
      "key": "25",
      "id": "Future",
      "href": "/objects/construction/change-request-status/25"
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

## POST /objects/construction/change-request-status
_Create a change request status_

**Request example — Create a change request status:**
```json
{
  "id": "Pending",
  "workflowType": "pendingChange",
  "status": "active"
}
```
**Response 201 — Reference to new change request status:**
```json
{
  "ia::result": {
    "key": "111",
    "id": "Approved change",
    "href": "/objects/construction/change-request-status/111"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/change-request-status/{key}
_Get a change request status_

**Response 200 — Details of change request status:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "Pending",
    "workflowType": "pendingChange",
    "status": "active",
    "audit": {
      "createdDateTime": "2021-11-11T02:16:46Z",
      "modifiedDateTime": "2021-11-11T02:16:46Z",
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
    "href": "/objects/construction/change-request-status/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/change-request-status/{key}
_Update a change request status_

**Request example — Set a change request status as inactive:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated change request status:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "Pending",
    "href": "/objects/construction/change-request-status/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/change-request-status/{key}
_Delete a change request status_


## GET /objects/construction/change-request-type
_List change request types_

**Response 200 — List of change request types:**
```json
{
  "ia::result": [
    {
      "key": "21",
      "id": "CRType-21",
      "href": "/objects/construction/change-request-type/21"
    },
    {
      "key": "23",
      "id": "CRType-23",
      "href": "/objects/construction/change-request-type/23"
    },
    {
      "key": "24",
      "id": "CRType-24",
      "href": "/objects/construction/change-request-type/24"
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

## POST /objects/construction/change-request-type
_Create a change request type_

**Request example — Create a change request type:**
```json
{
  "id": "Internal",
  "status": "active"
}
```
**Response 201 — Reference to new change request type:**
```json
{
  "ia::result": {
    "key": "111",
    "id": "Internal",
    "href": "/objects/construction/change-request-type/111"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/change-request-type/{key}
_Get a change request type_

**Response 200 — Get a change request type:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "Internal",
    "status": "active",
    "audit": {
      "createdDateTime": "2021-11-11T02:16:46Z",
      "modifiedDateTime": "2021-11-11T02:16:46Z",
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
    "href": "/objects/construction/change-request-type/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/change-request-type/{key}
_Update a change request type_

**Request example — Set a change request type to inactive:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated change request type:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "Internal",
    "href": "/objects/construction/change-request-type/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/change-request-type/{key}
_Delete a change request type_


## GET /objects/construction/change-request/{key}
_Get a change request_

**Response 200 — Details of the change request:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "CR1-DIMBTI-CRHSrce",
    "changeRequestType": {
      "key": "12",
      "id": "CRType-12",
      "href": "/objects/construction/change-request-type/12"
    },
    "project": {
      "key": "1",
      "id": "DIM - BTI",
      "name": "Dimensions - Berkeley Technology Inc",
      "href": "/objects/projects/project/1"
    },
    "location": {
      "key": "1",
      "id": "1",
      "name": "United States of America",
      "href": "/objects/company-config/location/1"
    },
    "projectCustomer": {
      "key": "14",
      "id": "BTI",
      "name": "Berkeley Technology Inc",
      "href": "/objects/accounts-receivable/customer/14"
    },
    "changeRequestDate": "2021-02-07",
    "changeRequestState": "posted",
    "changeRequestStatus": {
      "key": "1",
      "id": "CRStatus_Original",
      "workflowType": "original",
      "href": "/objects/construction/change-request-status/1"
    },
    "description": "CR1 with Line Source set to change request header",
    "costEffectiveDate": "2021-02-02",
    "priceEffectiveDate": "2021-02-02",
    "totalCost": "100.00",
    "totalPrice": "200.00",
    "projectChangeOrder": {
      "key": "1",
      "id": "PCO1-DIMBTI",
      "href": "/objects/construction/project-change-order/1"
    },
    "scope": "change request scope",
    "inclusions": null,
    "exclusions": null,
    "terms": null,
    "schedule": {
      "scheduledStartDate": "2022-05-30",
      "actualStartDate": "2022-05-30",
      "scheduledCompletionDate": "2022-05-30",
      "revisedCompletionDate": "2022-05-30",
      "substantialCompletionDate": "2022-05-30",
      "actualCompletionDate": "2022-05-30",
      "noticeToProceedDate": "2022-05-30",
      "responseDueDate": "2022-05-30",
      "executedOnDate": "2022-05-30",
      "scheduleImpact": "None"
    },
    "internalReference": {
      "referenceNumber": "INT-01",
      "initiatedBy": {
        "key": "2",
        "id": "12",
        "name": "Hatcher",
        "href": "/objects/company-config/employee/2"
      },
      "verbalApprovalBy": {
        "key": "2",
        "id": "12",
        "name": "Hatcher",
        "href": "/objects/company-config/employee/2"
      },
      "issuedBy": {
        "key": "25",
        "id": "123",
        "name": "Marquess",
        "href": "/objects/company-config/employee/25"
      },
      "issuedOnDate": "2021-05-30",
      "approvedBy": {
        "key": "1",
        "id": "11",
        "name": "Reser",
        "href": "/objects/company-config/employee/1"
      },
      "approvedOnDate": "2021-10-02",
      "signedBy": {
        "key": "32",
        "id": "Robert",
        "name": "Robert",
        "href": "/objects/company-config/employee/32"
      },
      "signedOnDate": "2021-05-31",
      "source": "NA",
      "sourceReferenceNumber": "REF-01"
    },
    "externalReference": {
      "referenceNumber": "A23",
      "verbalApprovalBy": {
        "key": "6",
        "name": "Johnson",
        "href": "/objects/company-config/contact/6"
      },
      "approvedBy": {
        "key": "69",
        "name": "Jagadish",
        "href": "/objects/company-config/contact/69"
      },
      "approvedOnDate": "2021-11-03",
      "signedBy": {
        "key": "200",
        "name": "Modulus Industries",
        "href": "/objects/company-config/contact/200"
      },
      "signedOnDate": "2021-12-01"
    },
    "attachment": {
      "id": "1"
    },
    "projectContract": {
      "key": "1",
      "id": "PCN1-Top-DIMBTI",
      "name": "PCN1-Top-DIMBTI",
      "href": "/objects/construction/project-contract/1"
    },
    "projectContractLine": {
      "key": "1",
      "id": "01",
      "name": "01-Billable Labor",
      "href": "/objects/construction/project-contract-line/1"
    },
    "audit": {
      "modifiedDateTime": "2023-06-14T13:56:37Z",
      "createdDateTime": "2023-06-14T13:56:35Z",
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
      "id": "CORP",
      "name": "Corp",
      "href": "/objects/company-config/entity/46"
    },
    "projectContractLineSource": "changeRequest",
    "changeRequestLines": [
      {
        "key": "99",
        "id": "99",
        "changeRequest": {
          "key": "1",
          "id": "CR1-DIMBTI-CRHSrce",
          "href": "/objects/construction/change-request/1"
        },
        "workflowType": "approvedChange",
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "name": "United States of America",
            "href": "/objects/company-config/location/1"
          },
          "department": {
            "key": "9",
            "id": "11",
            "name": "Accounting",
            "href": "/objects/company-config/department/9"
          },
          "project": {
            "key": "1",
            "id": "DIM - BTI",
            "name": "Dimensions - Berkeley Technology Inc",
            "href": "/objects/projects/project/1"
          },
          "customer": {
            "key": "14",
            "id": "BTI",
            "name": "Berkeley Technology Inc",
            "href": "/objects/accounts-receivable/customer/14"
          },
          "vendor": {
            "key": "43",
            "id": "V101",
            "name": "NW Concrete",
            "href": "/objects/accounts-payable/vendor/43"
          },
          "employee": {
            "key": "1",
            "id": "1",
            "name": "Reser",
            "href": "/objects/company-config/employee/1"
          },
          "item": {
            "key": "1",
            "id": "1",
            "name": "PC Computer",
            "href": "/objects/inventory-control/item/1"
          },
          "class": {
            "key": "1",
            "id": "3",
            "name": "Heath Care",
            "href": "/objects/company-config/class/1"
          },
          "task": {
            "key": "690",
            "id": "2-050",
            "name": "Demolition",
            "href": "/objects/projects/task/690"
          },
          "costType": {
            "key": "8",
            "id": "L",
            "name": "Labor",
            "href": "/objects/costType/8"
          }
        },
        "numberOfProductionUnits": "0",
        "productionUnitDescription": "Hours",
        "quantity": "10",
        "externalUOM": null,
        "unitCost": "100.00",
        "cost": "200.00",
        "unitPrice": "100.00",
        "price": "200.00",
        "priceMarkupPercent": "0",
        "priceMarkupAmount": "0.00",
        "linePrice": "200.00",
        "projectChangeOrder": {
          "key": "1",
          "id": "PCO1-DIMBTI",
          "href": "/objects/construction/project-change-order/1"
        },
        "memo": "CR1L1",
        "projectEstimate": {
          "key": "1",
          "id": "PrimEst-DIMBTI",
          "href": "/objects/construction/project-estimate/1"
        },
        "glAccount": {
          "key": "222",
          "id": "5008",
          "name": "Salaries - Contract",
          "href": "/objects/general-ledger/account/222"
        },
        "projectContract": {
          "key": "1",
          "id": "PCN1-Top-DIMBTI",
          "name": "PCN1-Top-DIMBTI",
          "href": "/objects/construction/project-contract/1"
        },
        "projectContractLine": {
          "key": "1",
          "id": "01",
          "name": "01-Billable Labor",
          "href": "/objects/construction/project-contract-line/1"
        },
        "audit": {
          "modifiedDateTime": "2023-06-14T13:56:37Z",
          "createdDateTime": "2023-06-14T13:56:35Z",
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
        "href": "/objects/construction/change-request-line/99"
      }
    ],
    "href": "/objects/construction/change-request/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/change-request/{key}
_Update a change request_

**Request example — Updates a change request description:**
```json
{
  "description": "CR1 with Line Source set to change request header - updated by project manager"
}
```
**Response 200 — Reference to updated change request:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "CR-4",
    "href": "/objects/construction/change-request/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/change-request/{key}
_Delete a change request_


## GET /objects/construction/compliance-definition
_List compliance definitions_

**Response 200 — List compliance definitions:**
```json
{
  "ia::result": [
    {
      "key": "3",
      "id": "vendorins",
      "href": "/objects/construction/compliance-definition/3"
    },
    {
      "key": "4",
      "id": "vendormisc",
      "href": "/objects/construction/compliance-definition/4"
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

## POST /objects/construction/compliance-definition
_Create a compliance definition_

**Request example — Create a compliance definition:**
```json
{
  "id": "Workman-Comp-Insurance",
  "name": "Workman's Comp Insurance",
  "description": "This is a description for compliance definition",
  "category": "insurance",
  "status": "active",
  "trackBy": "vendor",
  "generateRule": "automaticByType",
  "validationRule": "expirationDate",
  "paymentNotification": "warning",
  "complianceDefinitionAssociations": [
    {
      "vendorType": {
        "id": "Retailer"
      }
    }
  ]
}
```
**Response 201 — Reference to new compliance definition:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "Workman-Comp-Insurance",
    "href": "/objects/construction/compliance-definition/39"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/compliance-definition-association
_List compliance definition associations_

**Response 200 — List compliance definition associations:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/compliance-definition-association/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/compliance-definition-association/2"
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

## GET /objects/construction/compliance-definition-association/{key}
_Get a compliance definition association_

**Response 200 — Details of a compliance definition association:**
```json
{
  "ia::result": {
    "id": "1",
    "key": "1",
    "complianceDefinition": {
      "key": "4",
      "href": "/objects/construction/compliance-definition/4"
    },
    "vendorType": {
      "key": null,
      "id": null,
      "name": null
    },
    "projectType": {
      "key": null,
      "id": null,
      "name": null
    },
    "documentType": "zPrim-PurchaseOrder",
    "audit": {
      "modifiedDateTime": "2025-12-13T00:00:00Z",
      "createdDateTime": "2025-12-13T00:00:00Z",
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
    "href": "/objects/construction/compliance-definition-association/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/compliance-definition/{key}
_Get a compliance definition_

**Response 200 — Details of a compliance definition:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "Workman-Comp-Insurance",
    "name": "Workman's Comp Insurance",
    "description": "This is a description for compliance definition",
    "category": "insurance",
    "status": "active",
    "trackBy": "vendor",
    "generateRule": "automaticByType",
    "validationRule": "expirationDate",
    "paymentNotification": "warning",
    "generateForEach": null,
    "minimumLienWaiverAmount": null,
    "minimumPrimaryDocAmount": null,
    "allowNegativeLienWaivers": true,
    "audit": {
      "modifiedDateTime": "2025-10-26T00:00:00Z",
      "createdDateTime": "2025-10-26T00:00:00Z",
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
    "complianceDefinitionAssociations": [
      {
        "vendorType": {
          "key": "3",
          "id": "Retailer",
          "name": "Retailer",
          "href": "/objects/accounts-payable/vendor-type/3"
        },
        "projectType": {
          "key": null,
          "id": null,
          "name": null
        },
        "documentType": null
      }
    ],
    "href": "/objects/construction/compliance-definition/32"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/compliance-definition/{key}
_Update a compliance definition_

**Request example — Update a compliance definition:**
```json
{
  "description": "Updated description for compliance definition",
  "generateRule": "doNotGenerate"
}
```
**Response 200 — Reference to updated compliance definition:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "Workman-Comp-Insurance",
    "href": "/objects/construction/compliance-definition/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/compliance-definition/{key}
_Delete a compliance definition._


## GET /objects/construction/compliance-record
_List compliance records_

**Response 200 — List compliance records:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "VENDCOMP0001",
      "href": "/objects/construction/compliance-record/1"
    },
    {
      "key": "2",
      "id": "VENDCOMP0002",
      "href": "/objects/construction/compliance-record/2"
    },
    {
      "key": "3",
      "id": "Employee-Health-Ins-003",
      "href": "/object/compliance-record/3"
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

## POST /objects/construction/compliance-record
_Create a compliance record_

**Request example — Create a compliance record:**
```json
{
  "name": "Employee Health Insurance",
  "description": "Record of employee health insurance in compliance with employee benefit laws.",
  "complianceType": {
    "id": "Vendor_Med_Ins"
  },
  "vendor": {
    "id": "VPACBELL"
  }
}
```
**Response 201 — Reference to new compliance record:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "Employee-Health-Ins-003",
    "href": "/objects/construction/compliance-record/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/compliance-record/{key}
_Get a compliance record_

**Response 200 — Get a compliance record:**
```json
{
  "ia:result": {
    "key": "3",
    "id": "Employee-Health-Ins-003",
    "name": "Employee Health Insurance",
    "description": "Record of employee health insurance in compliance with employee benefit laws.",
    "status": "active",
    "complianceType": {
      "key": "19",
      "id": "Vendor_Med_Ins",
      "href": "/objects/construction/compliance-type/19"
    },
    "complianceDefinition": {
      "key": "32",
      "id": "Workman-Comp-Insurance",
      "category": "insurance",
      "validationRule": "expirationDate",
      "paymentNotification": "warning",
      "href": "/objects/construction/compliance-definition/32"
    },
    "vendor": {
      "key": "43",
      "id": "VPACBELL",
      "href": "/objects/accounts-payable/vendor/43"
    },
    "project": {
      "key": "11",
      "id": "DIM - BTI",
      "href": "/objects/projects/project/11"
    },
    "documentHeader": {
      "key": null,
      "id": null
    },
    "contacts": {
      "primary": {
        "id": null,
        "key": null
      },
      "sendTo": {
        "key": null,
        "id": null
      }
    },
    "policyNumber": null,
    "referenceNumber": null,
    "effectiveDate": null,
    "expirationDate": null,
    "amount": null,
    "isAdditionallyInsured": false,
    "hasSubrogationWaiver": false,
    "documentType": null,
    "primaryDocument": {
      "key": null,
      "id": null
    },
    "bill": {
      "id": null,
      "key": null
    },
    "payment": {
      "key": null
    },
    "isVoided": false,
    "isFinalCompliance": false,
    "complianceTemplate": "compliance-template,",
    "finalComplianceTemplate": "null,",
    "secondaryVendorComplianceTemplate": "null,",
    "isDocumentReceived": false,
    "receivedDate": null,
    "receivedBy": {
      "key": null,
      "id": null,
      "name": null
    },
    "overrideNotification": false,
    "isSystemGenerated": false,
    "notes": null,
    "secondaryVendorName": "Westside Electric",
    "isSecondaryVendor": true,
    "attachment": {
      "id": null
    },
    "audit": {
      "createdDateTime": "2023-10-30T00:00:00Z",
      "modifiedDateTime": "2023-10-30T00:00:00Z",
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
      "id": "CORP",
      "name": "Corp",
      "href": "/objects/company-config/entity/46"
    },
    "href": "/objects/construction/compliance-record/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/compliance-record/{key}
_Update a compliance record_

**Request example — Update a compliance record:**
```json
{
  "name": "Employee Health Insurance",
  "contact": {
    "primary": {
      "id": "John Smith"
    }
  },
  "policyNumber": "443972001415",
  "amount": "5000.00"
}
```
**Response 200 — Reference to updated compliance record:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "Employee-Health-Ins-003",
    "href": "/objects/construction/compliance-record/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/compliance-record/{key}
_Delete a compliance record_


## GET /objects/construction/compliance-type
_List compliance types_

**Response 200 — List compliance types:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "vendmisctype",
      "href": "/objects/construction/compliance-type/2"
    },
    {
      "key": "1",
      "id": "vendorinstype",
      "href": "/objects/construction/compliance-type/1"
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

## POST /objects/construction/compliance-type
_Create a compliance type_

**Request example — Create a compliance type:**
```json
{
  "id": "Vendor_Med_Ins",
  "name": "Vendor Medical Insurance",
  "description": "Medical expenses for work-related injuries",
  "complianceDefinition": {
    "id": "Workman-Comp-Insurance"
  },
  "complianceRecordIdSequence": {
    "id": "EmployeeInsuranceRecordSequence"
  },
  "complianceRecordCustomFields": [
    "5",
    "3",
    "6",
    "7"
  ]
}
```
**Response 201 — Reference to new compliance type:**
```json
{
  "ia::result": {
    "key": "19",
    "id": "Vendor_Med_Ins",
    "href": "/objects/construction/compliance-type/19"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/compliance-type/{key}
_Get a compliance type_

**Response 200 — Get a compliance type:**
```json
{
  "ia::result": {
    "key": "19",
    "id": "Vendor_Med_Ins",
    "name": "Vendor Medical Insurance",
    "description": "Medical expenses for work-related injuries",
    "complianceDefinition": {
      "key": "32",
      "id": "Workman-Comp-Insurance",
      "href": "/objects/construction/compliance-definition/32"
    },
    "complianceRecordIdSequence": {
      "key": "41",
      "id": "ChangeRequest",
      "href": "/objects/company-config/document-sequence/41"
    },
    "complianceTemplate": "Document template",
    "finalComplianceTemplate": "Final document template",
    "secondaryVendorComplianceTemplate": "Secondary vendor document template",
    "complianceRecordCustomFields": [
      "5",
      "3",
      "6",
      "7"
    ],
    "status": "active",
    "audit": {
      "modifiedDateTime": "2025-10-30T00:00:00Z",
      "createdDateTime": "2025-10-30T00:00:00Z",
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
    "href": "/objects/construction/compliance-type/19"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/compliance-type/{key}
_Update a compliance type_

**Request example — Update a compliance type:**
```json
{
  "name": "Vendor Medical Insurance",
  "description": "Other medical expenses for work-related injuries",
  "complianceRecordIdSequence": {
    "id": "VendorInsuranceSequence"
  },
  "complianceRecordCustomFields": [
    "5",
    "3",
    "7"
  ]
}
```
**Response 200 — Reference to updated compliance type:**
```json
{
  "ia::result": {
    "key": "19",
    "id": "Vendor Medical Insurance",
    "href": "/objects/construction/compliance-type/19"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/compliance-type/{key}
_Delete a compliance type_


## GET /objects/construction/cost-type-observed-percent-completed
_List observed percent completed_

**Response 200 — List of cost type observed percent completed:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/cost-type-observed-percent-completed/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/cost-type-observed-percent-completed/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/cost-type-observed-percent-completed/3"
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

## POST /objects/construction/cost-type-observed-percent-completed
_Create a cost type observed percent completed_

**Request example — Creates a cost type observed percent completed:**
```json
{
  "costType": {
    "key": "14"
  },
  "asOfDate": "2024-06-21",
  "percentComplete": "20",
  "notes": "Initial work completed"
}
```
**Response 201 — Reference to new cost type observed percent completed:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/construction/cost-type-observed-percent-completed/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/cost-type-observed-percent-completed/{key}
_Get a cost type observed percent completed_

**Response 200 — Details of the cost type observed percent completed:**
```json
{
  "ia::result": {
    "key": "24",
    "id": "24",
    "href": "/objects/construction/cost-type-observed-percent-completed/24",
    "costType": {
      "id": "EQ-Rental",
      "key": "14",
      "name": "EQ-Rental",
      "href": "/objects/construction/cost-type/13"
    },
    "asOfDate": "2024-06-21",
    "percentComplete": "10",
    "notes": "Completion on 06/21/24",
    "audit": {
      "createdDateTime": "2023-11-11T16:20:00Z",
      "modifiedDateTime": "2023-11-11T16:20:00Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "95",
        "id": "John Smith",
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

## PATCH /objects/construction/cost-type-observed-percent-completed/{key}
_Update a cost type observed percent completed_

**Request example — Updates a cost type observed percent completed:**
```json
{
  "percentComplete": "35",
  "notes": "changed to 35%"
}
```
**Response 200 — Reference to updated cost type observed percent completed:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "href": "/objects/construction/cost-type-observed-percent-completed/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/cost-type-observed-percent-completed/{key}
_Delete a cost type observed percent completed_


## GET /objects/construction/employee-position
_List employee positions_

**Response 200 — List of employee positions:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "EP-001",
      "href": "/objects/construction/employee-position/1"
    },
    {
      "key": "2",
      "id": "EP-002",
      "href": "/objects/construction/employee-position/2"
    },
    {
      "key": "7",
      "id": "PLUM-001",
      "href": "/objects/construction/employee-position/7"
    },
    {
      "key": "8",
      "id": "FOR-001",
      "href": "/objects/construction/employee-position/8"
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

## POST /objects/construction/employee-position
_Create an employee position_

**Request example — Create an employee position:**
```json
{
  "id": "FOR-001",
  "name": "Foreman-01",
  "description": "Job site foreman",
  "status": "active"
}
```
**Response 201 — Reference to new employee position:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "FOR-001",
    "href": "/objects/construction/employee-position/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/employee-position/{key}
_Get an employee position_

**Response 200 — employee position details:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "FOR-001",
    "name": "Foreman-01",
    "description": "Job site foreman",
    "status": "active",
    "audit": {
      "createdDateTime": "2023-02-02T23:32:10Z",
      "modifiedDateTime": "2023-03-03T01:24:56Z",
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
      "id": "CORP",
      "name": "Corp",
      "href": "/objects/company-config/entity/46"
    },
    "href": "/objects/construction/employee-position/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/employee-position/{key}
_Update an employee position_

**Request example — Set a position to inactive:**
```json
{
  "description": "(deactivated) This employee is a foreman",
  "status": "inactive"
}
```
**Response 200 — Reference to updated employee position:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "FOR-001",
    "href": "/objects/construction/employee-position/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/employee-position/{key}
_Delete an employee position_


## GET /objects/construction/labor-class
_List labor classes_

**Response 200 — List of labor classes:**
```json
{
  "ia::result": [
    {
      "key": "6",
      "id": "LC001",
      "href": "/objects/construction/labor-class/6"
    },
    {
      "key": "7",
      "id": "LC002",
      "href": "/objects/construction/labor-class/7"
    },
    {
      "key": "8",
      "id": "LC003",
      "href": "/objects/construction/labor-class/8"
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

## POST /objects/construction/labor-class
_Create a labor class_

**Request example — Create a labor class:**
```json
{
  "id": "LC001",
  "name": "LC Skilled",
  "description": "Skilled laborer",
  "status": "active"
}
```
**Response 201 — Reference to new labor class:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "LC001",
    "href": "/objects/construction/labor-class/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/labor-class/{key}
_Get a labor class_

**Response 200 — Labor class details:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "LC001",
    "name": "LC Skilled",
    "description": "Skilled laborer",
    "status": "active",
    "audit": {
      "createdDateTime": "2023-11-21T22:42:02Z",
      "modifiedDateTime": "2023-11-21T22:42:02Z",
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
    "href": "/objects/construction/labor-class/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/labor-class/{key}
_Update a labor class_

**Request example — Change labor class description:**
```json
{
  "description": "Professional laborer (salaried)"
}
```
**Response 200 — Reference to updated labor class:**
```json
{
  "ia::result": {
    "key": "8",
    "id": "LC003",
    "href": "/objects/construction/labor-class/8"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/labor-class/{key}
_Delete a labor class_


## GET /objects/construction/labor-shift
_List labor shifts_

**Response 200 — example-1:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "LS-AM",
      "href": "/objects/construction/labor-shift/2"
    },
    {
      "key": "3",
      "id": "LS-PM",
      "href": "/objects/construction/labor-shift/3"
    },
    {
      "key": "4",
      "id": "LS-NT",
      "href": "/objects/construction/labor-shift/4"
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

## POST /objects/construction/labor-shift
_Create a labor shift_

**Request example — Create a labor shift:**
```json
{
  "id": "LS-AM",
  "name": "AM Shift",
  "description": "Morning shift (6am-2pm)",
  "status": "active"
}
```
**Response 201 — Reference to new labor shift:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "LS-AM",
    "href": "/objects/construction/labor-shift/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/labor-shift/{key}
_Get a labor shift_

**Response 200 — Details of a labor shift:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "LS-AM",
    "name": "AM Shift",
    "description": "Morning shift (6am-2pm)",
    "status": "active",
    "audit": {
      "createdDateTime": "2021-11-21T23:05:29Z",
      "modifiedDateTime": "2021-11-21T23:05:29Z",
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
    "href": "/objects/construction/labor-shift/2"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/labor-shift/{key}
_Update a labor shift_

**Request example — Update a labor shift:**
```json
{
  "description": "(unused) Graveyard shift (10pm-6am)",
  "status": "inactive"
}
```
**Response 200 — Reference to updated labor shift:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "LS-NT",
    "href": "/objects/construction/labor-shift/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/labor-shift/{key}
_Delete a labor shift_


## GET /objects/construction/labor-union
_List labor unions_

**Response 200 — List of labor unions:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "IBEW",
      "href": "/objects/construction/labor-union/1"
    },
    {
      "key": "2",
      "id": "Teamsters",
      "href": "/objects/construction/labor-union/2"
    },
    {
      "key": "3",
      "id": "BAC",
      "href": "/objects/construction/labor-union/3"
    },
    {
      "key": "4",
      "id": "IUEC",
      "href": "/objects/construction/labor-union/4"
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

## POST /objects/construction/labor-union
_Create a labor union_

**Request example — Create a labor union:**
```json
{
  "id": "BAC",
  "name": "International Union of Bricklayers and Allied Craftworkers",
  "description": "BAC represents all skilled trowel trades workers, including bricklayers, tile setters, plasterers, cement masons, marble masons, restoration workers, and terrazzo and mosaic workers.",
  "status": "active"
}
```
**Response 201 — Reference to new labor shift:**
```json
{
  "ia::result": {
    "key": "3",
    "id": "BAC",
    "href": "/objects/construction/labor-union/3"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/labor-union/{key}
_Get a labor union_

**Response 200 — example:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "IUEC",
    "name": "International Union of Elevator Constructors",
    "description": "The IUEC represent the most qualified and trained elevator constructors in the world. Members assemble, install and replace elevators, escalators, dumbwaiters, moving walkways and similar equipment in new and old buildings. Elevator constructors also maintain and repair this equipment and modernize older equipment.",
    "status": "active",
    "audit": {
      "createdDateTime": "2021-11-22T00:08:55Z",
      "modifiedDateTime": "2021-11-22T00:11:44Z",
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
    "href": "/objects/construction/labor-union/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/labor-union/{key}
_Update a labor union_

**Request example — Update labor union description:**
```json
{
  "description": "The IUEC represent the most qualified and trained elevator constructors in the world. Members assemble, install and replace elevators, escalators, dumbwaiters, moving walkways and similar equipment in new and old buildings. Elevator constructors also maintain and repair this equipment and modernize older equipment."
}
```
**Response 200 — Reference to updated labor union:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "IUEC",
    "href": "/objects/construction/labor-union/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/labor-union/{key}
_Delete a labor union_


## GET /objects/construction/primary-document-accounts-payable-bill
_List primary document AP bills_

**Response 200 — List primary document AP bills:**
```json
{
  "ia::result": [
    {
      "key": "184-28-456",
      "id": "184-28-456",
      "href": "/objects/construction/primary-document-accounts-payable-bill/184-28-456"
    },
    {
      "key": "185-28-456",
      "id": "185-28-456",
      "href": "/objects/construction/primary-document-accounts-payable-bill/185-28-456"
    },
    {
      "key": "188-28-456",
      "id": "188-28-456",
      "href": "/objects/construction/primary-document-accounts-payable-bill/188-28-456"
    },
    {
      "key": "151-123-123",
      "id": "151-123-123",
      "href": "/objects/construction/primary-document-accounts-payable-bill/151-123-123"
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

## GET /objects/construction/primary-document-accounts-payable-bill/{key}
_Get a primary document AP bill_

**Response 200 — Get a primary document accounts payable bill:**
```json
{
  "ia::result": {
    "id": "151-123-123",
    "key": "151-123-123",
    "sourceDocument": {
      "id": "3669",
      "key": "3669",
      "documentId": "PO-Source01-R2-81",
      "href": "/objects/purchasing/document/3669"
    },
    "primaryDocument": {
      "id": "4935",
      "key": "4935",
      "documentId": "PO-Invoice01-VI#0878#doc",
      "documentNumber": "PO-Invoice01-VI#0878#doc",
      "postingDate": "2026-09-12",
      "href": "/objects/purchasing/document/4935"
    },
    "apBill": {
      "state": "draft",
      "billNumber": "Bill-001",
      "id": "1692",
      "key": "1692",
      "createdDate": "2026-09-12",
      "href": "/objects/accounts-payable/bill/1692"
    },
    "invoiceTotals": {
      "totalAmountInvoiced": "56500.0000000000",
      "invoiceBalanceAmount": "56500.0000000000"
    },
    "retainageTotals": {
      "heldAmount": "8475.0000000000",
      "netAmountInvoiced": "48025.0000000000",
      "netAmountPaid": "100.0000000000",
      "releasedAmount": "100.0000000000",
      "netInvoiceBalanceAmount": "48025.0000000000"
    },
    "href": "/objects/construction/primary-document-accounts-payable-bill/151-123-123"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/primary-document-accounts-payable-payment
_List primary document AP payments_

**Response 200 — List primary document AP payments:**
```json
{
  "ia::result": [
    {
      "key": "127-111-109",
      "id": "127-111-109",
      "href": "/objects/construction/primary-document-accounts-payable-payment/127-111-109"
    },
    {
      "key": "149-121-119",
      "id": "149-121-119",
      "href": "/objects/construction/primary-document-accounts-payable-payment/149-121-119"
    },
    {
      "key": "150-123-120",
      "id": "150-123-120",
      "href": "/objects/construction/primary-document-accounts-payable-payment/150-123-120"
    },
    {
      "key": "151-123-123",
      "id": "151-123-123",
      "href": "/objects/construction/primary-document-accounts-payable-payment/151-123-123"
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

## GET /objects/construction/primary-document-accounts-payable-payment/{key}
_Get a primary document AP payment_

**Response 200 — Get a primary document accounts payable payment:**
```json
{
  "ia::result": {
    "id": "151-123-123",
    "key": "151-123-123",
    "primaryDocument": {
      "id": "6095",
      "key": "6095",
      "documentId": "PO-Source00-PO#1495#doc",
      "href": "/objects/purchasing/document/6095"
    },
    "apPayment": {
      "id": "3265",
      "key": "3265",
      "paymentMethod": "Cash",
      "documentNumber": "BILL-165",
      "paymentDate": "2025-04-21",
      "href": "/objects/accounts-payable/payment/3265"
    },
    "financialEntity": {
      "id": "BOA",
      "key": "1",
      "href": "/objects/cash-management/bank-account/1"
    },
    "paymentAmount": "150.0000000000",
    "href": "/objects/construction/primary-document-accounts-payable-payment/151-123-123"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/primary-document-detail
_List primary document details_

**Response 200 — List primary document details:**
```json
{
  "ia::result": [
    {
      "key": "256-165-201",
      "id": "256-165-201",
      "href": "/objects/construction/primary-document-detail/256-165-201"
    },
    {
      "key": "257-165-201",
      "id": "257-165-201",
      "href": "/objects/construction/primary-document-detail/257-165-201"
    },
    {
      "key": "265-165-201",
      "id": "265-165-201",
      "href": "/objects/construction/primary-document-detail/265-165-201"
    },
    {
      "key": "266-165-201",
      "id": "266-165-201",
      "href": "/objects/construction/primary-document-detail/266-165-201"
    },
    {
      "key": "267-165-201",
      "id": "267-165-201",
      "href": "/objects/construction/primary-document-detail/267-165-201"
    },
    {
      "key": "268-165-201",
      "id": "268-165-201",
      "href": "/objects/construction/primary-document-detail/268-165-201"
    },
    {
      "key": "151-123-123",
      "id": "151-123-123",
      "href": "/objects/construction/primary-document-detail/151-123-123"
    }
  ],
  "ia::meta": {
    "totalCount": 7,
    "start": 1,
    "pageSize": 100,
    "next": null,
    "previous": null
  }
}
```

## GET /objects/construction/primary-document-detail/{key}
_Get a primary document detail_

**Response 200 — Get a primary document detail:**
```json
{
  "ia::result": {
    "id": "151-123-123",
    "key": "151-123-123",
    "primaryDocument": {
      "id": "3669",
      "key": "3669",
      "documentNumber": "PO-Source01-R2-81",
      "href": "/objects/purchasing/document/3669"
    },
    "primaryDocumentLine": {
      "id": "9156",
      "key": "9156",
      "lineNumber": 2,
      "memo": "line 2",
      "href": "/objects/purchasing/document-line/9156"
    },
    "project": {
      "key": "1",
      "id": "DIM - BTI",
      "name": "Dimensions - Berkeley Technology Inc",
      "href": "/objects/projects/project/1"
    },
    "task": {
      "key": "7",
      "id": "TSK-RT-0002",
      "name": "DIM - BTI07",
      "href": "/objects/projects/task/7"
    },
    "costType": {
      "key": "65",
      "id": "LPM",
      "name": "Project Manager Labor DIM-BTI 0002",
      "href": "/objects/construction/cost-type/65"
    },
    "item": {
      "id": "Design",
      "key": "17",
      "name": "Design",
      "href": "/objects/inventory-control/item/17"
    },
    "location": {
      "key": "1",
      "id": "1",
      "name": "1--United States of America",
      "href": "/objects/company-config/location/1"
    },
    "department": {
      "key": "7",
      "id": "CS",
      "name": "CS--Client Services",
      "href": "/objects/company-config/department/7"
    },
    "documentTotals": {
      "txnTotals": {
        "originalAmount": "30500.0000000000",
        "pendingChangesAmount": "1500.0000000000",
        "postedChangesAmount": "14500.0000000000",
        "revisedAmount": "45000.0000000000"
      },
      "baseTotals": {
        "originalAmount": "30500.0000000000",
        "pendingChangesAmount": "1500.0000000000",
        "postedChangesAmount": "14500.0000000000",
        "revisedAmount": "45000.0000000000"
      }
    },
    "invoiceTotals": {
      "txnTotals": {
        "totalAmountInvoiced": "33000.0000000000",
        "invoiceBalanceAmount": "33000.0000000000",
        "remainingToInvoiceAmount": "12000.0000000000",
        "totalAmountPaid": "100.0000000000"
      },
      "baseTotals": {
        "totalAmountInvoiced": "33000.0000000000",
        "totalAmountPaid": "100.0000000000"
      }
    },
    "retainageTotals": {
      "txnTotals": {
        "heldAmount": "100.0000000000",
        "netAmountInvoiced": "33000.0000000000",
        "netAmountPaid": "100.0000000000",
        "netInvoiceBalanceAmount": "33000.0000000000",
        "releasedAmount": "100.0000000000",
        "heldBalanceAmount": "100.0000000000",
        "amountPaid": "100.0000000000",
        "invoiceBalanceAmount": "33000.0000000000"
      },
      "baseTotals": {
        "heldAmount": "100.0000000000",
        "netAmountInvoiced": "33000.0000000000",
        "netAmountPaid": "100.0000000000",
        "releasedAmount": "100.0000000000",
        "amountPaid": "100.0000000000"
      }
    },
    "href": "/objects/construction/primary-document-detail/151-123-123"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/primary-document-retainage-release
_List primary document retainage releases_

**Response 200 — List primary document retainage releases:**
```json
{
  "ia::result": [
    {
      "key": "133-014-567",
      "id": "133-014-567",
      "href": "/objects/construction/primary-document-retainage-release/133-014-567"
    },
    {
      "key": "134-567-890",
      "id": "134-567-890",
      "href": "/objects/construction/primary-document-retainage-release/134-567-890"
    },
    {
      "key": "135-890-123",
      "id": "135-890-123",
      "href": "/objects/construction/primary-document-retainage-release/135-890-123"
    },
    {
      "key": "152-145-678",
      "id": "152-145-678",
      "href": "/objects/construction/primary-document-retainage-release/152-145-678"
    },
    {
      "key": "151-123-123",
      "id": "151-123-123",
      "href": "/objects/construction/primary-document-retainage-release/151-123-123"
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

## GET /objects/construction/primary-document-retainage-release/{key}
_Get a primary document retainage release_

**Response 200 — Get a primary document retainage release:**
```json
{
  "ia::result": {
    "id": "151-123-123",
    "key": "151-123-123",
    "primaryDocument": {
      "id": "6081",
      "key": "6081",
      "documentId": "PO-Source01-R2-287",
      "postingDate": "2025-04-16",
      "href": "/objects/purchasing/document/6081"
    },
    "apBill": {
      "billNumber": "APReta-62",
      "id": "3254",
      "key": "3254",
      "state": "draft",
      "createdDate": "2025-04-16",
      "href": "/objects/accounts-payable/bill/3254"
    },
    "invoiceTotals": {
      "totalAmountInvoiced": "100.0000000000",
      "totalAmountPaid": "90.0000000000",
      "invoiceBalanceAmount": "10.0000000000"
    },
    "href": "/objects/construction/primary-document-retainage-release/151-123-123"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/primary-document-summary
_List primary document summaries_

**Response 200 — List primary document summaries:**
```json
{
  "ia::result": [
    {
      "key": "66",
      "id": "66",
      "href": "/objects/construction/primary-document-summary/66"
    },
    {
      "key": "72",
      "id": "72",
      "href": "/objects/construction/primary-document-summary/72"
    },
    {
      "key": "74",
      "id": "74",
      "href": "/objects/construction/primary-document-summary/74"
    },
    {
      "key": "90",
      "id": "90",
      "href": "/objects/construction/primary-document-summary/90"
    },
    {
      "key": "92",
      "id": "92",
      "href": "/objects/construction/primary-document-summary/92"
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

## GET /objects/construction/primary-document-summary/{key}
_Get a primary document summary_

**Response 200 — Get a primary document summary:**
```json
{
  "ia::result": {
    "id": "90",
    "key": "90",
    "primaryDocument": {
      "id": "6095",
      "key": "6095",
      "documentId": "PO-Source00-PO#1495#doc",
      "documentNumber": "PO#1495#doc",
      "state": "partiallyConverted",
      "txnDate": "2025-04-21",
      "dueDate": "2025-07-05",
      "postingDate": "2025-04-04",
      "txnCurrency": "USD",
      "baseCurrency": "USD",
      "href": "/objects/purchasing/document/6095"
    },
    "project": {
      "key": "125",
      "id": "DIM-BTI",
      "name": "Dimensions - Berkeley Technology Inc",
      "href": "/objects/projects/project/125"
    },
    "txnDefinition": {
      "key": "532",
      "id": "PO-Source00",
      "href": "/objects/purchasing/txn-definition::PO-Source00/532"
    },
    "documentTotals": {
      "txnTotals": {
        "originalAmount": "22500.0000000000",
        "pendingChangesAmount": "100.0000000000",
        "postedChangesAmount": "100.0000000000",
        "revisedAmount": "100.0000000000"
      },
      "baseTotals": {
        "originalAmount": "22500.0000000000",
        "pendingChangesAmount": "100.0000000000",
        "postedChangesAmount": "100.0000000000",
        "revisedAmount": "22500.0000000000"
      }
    },
    "invoiceTotals": {
      "txnTotals": {
        "totalAmountInvoiced": "45000.0000000000",
        "invoiceBalanceAmount": "25298.0000000000",
        "remainingToInvoiceAmount": "22500.0000000000",
        "totalAmountPaid": "19702.0000000000"
      },
      "baseTotals": {
        "totalAmountInvoiced": "45000.0000000000",
        "totalAmountPaid": "19702.0000000000"
      }
    },
    "retainageTotals": {
      "txnTotals": {
        "heldAmount": "3525.0000000000",
        "netAmountInvoiced": "41475.0000000000",
        "netAmountPaid": "19700.0000000000",
        "netInvoiceBalanceAmount": "21775.0000000000",
        "releasedAmount": "3.0000000000",
        "heldBalanceAmount": "3522.0000000000",
        "amountPaid": "2.0000000000",
        "invoiceBalanceAmount": "1.0000000000"
      },
      "baseTotals": {
        "heldAmount": "3525.0000000000",
        "netAmountInvoiced": "41475.0000000000",
        "netAmountPaid": "19700.0000000000",
        "releasedAmount": "3.0000000000",
        "amountPaid": "2.0000000000"
      }
    },
    "href": "/objects/construction/primary-document-summary/90"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-change-order
_List project change orders_

**Response 200 — List of project change orders:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "PCO-BTI-1",
      "href": "/objects/construction/project-change-order/1"
    },
    {
      "key": "2",
      "id": "PCO-BTI-2",
      "href": "/objects/construction/project-change-order/2"
    },
    {
      "key": "3",
      "id": "PCO-BTI-3",
      "href": "/objects/construction/project-change-order/3"
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

## POST /objects/construction/project-change-order
_Create a project change order_

**Request example — Change order to create:**
```json
{
  "id": "PCO-BTI-9",
  "project": {
    "id": "DIM - BTI"
  },
  "projectChangeOrderDate": "2023-12-09",
  "priceEffectiveDate": "2023-12-01",
  "changeRequestStatus": {
    "id": "Pending"
  },
  "state": "draft",
  "description": "Change Oder 9 for BTI Project",
  "sendToContact": {
    "id": "Aaron"
  },
  "item": {
    "id": "Development"
  },
  "scope": "Planning only",
  "inclusions": "Design scope",
  "exclusions": "Maintenance",
  "terms": "Standard",
  "schedule": {
    "scheduledStartDate": "2024-01-01",
    "scheduleImpact": "NA"
  },
  "attachment": {
    "id": "pco-bti-1-att1"
  }
}
```
**Response 201 — Reference to new project change order:**
```json
{
  "ia::result": {
    "key": "6",
    "id": "PCO-BTI-6",
    "href": "/objects/construction/project-change-order/6"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-change-order/{key}
_Get a project change order_

**Response 200 — Change order details:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "PCO-BTI-1",
    "project": {
      "key": "1",
      "id": "DIM - BTI",
      "name": "Dimensions - Berkeley Technology Inc",
      "href": "/objects/projects/project/1"
    },
    "location": {
      "key": "1",
      "id": 1,
      "name": "United States of America",
      "href": "/objects/company-config/location/1"
    },
    "customer": {
      "key": "14",
      "id": "BTI",
      "name": "Berkeley Technology Inc",
      "href": "/objects/accounts-receivable/customer/14"
    },
    "projectChangeOrderDate": "2021-12-15",
    "state": "posted",
    "changeRequestStatus": {
      "key": "2",
      "id": "Approved",
      "href": "/objects/change-request-status/2"
    },
    "description": "Change Oder 1 for BTI Project",
    "priceEffectiveDate": "2021-12-15",
    "projectContract": {
      "key": "3",
      "id": "BTI-02",
      "name": "BTI - 02",
      "href": "/objects/construction/project-contract/3"
    },
    "projectContractLine": {
      "key": "28",
      "id": "bti-02.1",
      "name": "bti-02.1",
      "href": "/objects/construction/project-contract-line/28"
    },
    "totalCost": "1000.00",
    "totalPrice": "1500.00",
    "sendToContact": {
      "key": "4",
      "id": "Chandler",
      "href": "/objects/company-config/contact/4"
    },
    "item": {
      "key": "21",
      "id": "Maintenance",
      "name": "Maintenance",
      "href": "/objects/inventory-control/item/21"
    },
    "scope": "scope",
    "inclusions": "incl",
    "exclusions": "excl",
    "terms": "terms",
    "schedule": {
      "scheduledStartDate": "2022-01-12",
      "actualStartDate": "2022-01-12",
      "scheduledCompletionDate": "2022-04-30",
      "revisedCompletionDate": "2022-05-30",
      "substantialCompletionDate": "2022-05-30",
      "actualCompletionDate": "2022-05-30",
      "noticeToProceedDate": "2022-05-30",
      "responseDueDate": "2022-05-30",
      "executedOnDate": "2022-05-30",
      "scheduleImpact": "None"
    },
    "internalReference": {
      "referenceNumber": "BTI-01-REF-034-M",
      "initiatedBy": {
        "key": "28",
        "id": "22",
        "name": "Chandler",
        "href": "/objects/company-config/employee/28"
      },
      "verbalApprovalBy": {
        "key": "28",
        "id": "22",
        "name": "Chandler",
        "href": "/objects/company-config/employee/28"
      },
      "issuedBy": {
        "key": "31",
        "id": "23",
        "name": "Jurasek",
        "href": "/objects/company-config/employee/31"
      },
      "issuedOnDate": "2021-12-08",
      "approvedBy": {
        "key": "30",
        "id": "2345",
        "name": "Johnson",
        "href": "/objects/company-config/employee/30"
      },
      "approvedOnDate": "2021-12-09",
      "signedBy": {
        "key": "30",
        "id": "2345",
        "name": "Johnson",
        "href": "/objects/company-config/employee/30"
      },
      "signedOnDate": "2021-12-09",
      "source": "NA",
      "sourceReferenceNumber": "NA"
    },
    "externalReference": {
      "referenceNumber": "NA",
      "verbalApprovalBy": {
        "key": "11",
        "id": "Baechtel",
        "href": "/objects/company-config/contact/11"
      },
      "approvedBy": {
        "key": "11",
        "id": "Baechtel",
        "href": "/objects/company-config/contact/11"
      },
      "approvedOnDate": "2021-12-10",
      "signedBy": {
        "key": "224",
        "id": "Able and Sons, Accountants",
        "href": "/objects/company-config/contact/224"
      },
      "signedOnDate": "2021-12-10"
    },
    "attachment": {
      "id": "pco-bti-1-att1",
      "key": "6",
      "href": "/objects/company-config/attachment/6"
    },
    "audit": {
      "modifiedDateTime": "2021-12-30T22:28:51Z",
      "createdDateTime": "2021-12-08T23:30:01Z",
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
    "href": "/objects/construction/project-change-order/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/project-change-order/{key}
_Update a project change order_

**Request example — Update a project change order:**
```json
{
  "project": {
    "id": "DIM - BTI"
  },
  "projectChangeOrderDate": "2021-12-15",
  "priceEffectiveDate": "2021-12-15",
  "state": "posted",
  "description": "Change Oder 1 for BTI Project",
  "changeRequestStatus": {
    "id": "Approved"
  },
  "sendToContact": {
    "id": "Chandler"
  },
  "item": {
    "id": "Maintenance"
  },
  "scope": "scope",
  "inclusions": "incl",
  "exclusions": "excl",
  "terms": "terms",
  "schedule": {
    "scheduledStartDate": "2022-01-12"
  },
  "attachment": {
    "id": "pco-bti-1-att2"
  }
}
```
**Response 200 — Reference to updated project change order:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "PCO-BTI-1",
    "href": "/objects/construction/project-change-order/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/project-change-order/{key}
_Delete a project change order_


## GET /objects/construction/project-contract
_List project contracts_

**Response 200 — example-result-collection-of-project-contracts:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "BTI-01",
      "href": "/objects/construction/project-contract/1"
    },
    {
      "key": "2",
      "id": "BTI-02",
      "href": "/objects/construction/project-contract/2"
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

## POST /objects/construction/project-contract
_Create a project contract_

**Request example — Details of project contract to create:**
```json
{
  "id": "BTI-05",
  "name": "Berkeley Technology Inc - Contract 05",
  "project": {
    "id": "DIM - BTI"
  },
  "customer": {
    "id": "BTI"
  },
  "contractDate": "2023-09-30",
  "description": "Project contract for Berkeley Technology Inc",
  "architect": {
    "id": "Eberhardt"
  },
  "projectContractType": {
    "id": "COM"
  },
  "attachment": {
    "id": "pc-att-2"
  },
  "isBillable": true,
  "scope": "Project scope only",
  "inclusions": "Per original contract",
  "exclusions": "Plumbing",
  "terms": "Per original contract",
  "schedule": {
    "scheduledStartDate": "2023-06-15",
    "actualStartDate": "2023-06-30",
    "scheduledCompletionDate": "2022-11-15",
    "revisedCompletionDate": "2023-12-15",
    "substantialCompletionDate": "2023-09-30",
    "actualCompletionDate": "2023-12-15",
    "noticeToProceedDate": "2023-05-30",
    "responseDueDate": "2023-06-05",
    "executedOnDate": "2023-06-01",
    "scheduleImpact": "NA"
  },
  "internalReference": {
    "referenceNumber": "INT-01",
    "initiatedBy": {
      "id": "2"
    },
    "verbalApprovalBy": {
      "id": "2"
    },
    "issuedBy": {
      "id": "123"
    },
    "issuedOnDate": "2023-05-30",
    "approvedBy": {
      "id": "1"
    },
    "approvedOnDate": "2023-10-02",
    "signedBy": {
      "id": "Robert"
    },
    "signedOnDate": "2023-05-31",
    "source": "NA",
    "sourceReferenceNumber": "REF-01"
  },
  "externalReference": {
    "referenceNumber": "A23",
    "verbalApprovalBy": {
      "id": "Johnson"
    },
    "approvedBy": {
      "id": "Jagadish"
    },
    "approvedOnDate": "2023-11-03",
    "signedBy": {
      "id": "Modulus Industries"
    },
    "signedOnDate": "2023-12-01"
  },
  "taxSolution": {
    "id": "Advanced Tax India"
  },
  "taxSchedule": {
    "id": "Sale Goods Standard"
  },
  "glBudgetPosting": {
    "isPosted": true,
    "postingPeriodBasedOn": "projectContractDate",
    "originalGLBudget": {
      "id": "KPI Original Budgets"
    },
    "revisionGLBudget": {
      "id": "KPI Revision Budgets"
    },
    "approvedGLBudget": {
      "id": "KPI Approved Budgets"
    },
    "pendingGLBudget": {
      "id": "KPI Pending Budgets"
    },
    "forecastGLBudget": {
      "id": "KPI Forecast Budgets"
    },
    "otherGLBudget": {
      "id": "KPI Other Budgets"
    }
  }
}
```
**Response 201 — Reference to new project contract:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "BTI-01",
    "href": "/objects/construction/project-contract/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-contract-billing-invoice-detail
_List project contract billing invoice details_

**Response 200 — List of project contract billing invoice details:**
```json
{
  "ia::result": [
    {
      "key": "3480",
      "id": "3480",
      "href": "/objects/construction/project-contract-billing-invoice-detail/3480"
    },
    {
      "key": "3483",
      "id": "3483",
      "href": "/objects/construction/project-contract-billing-invoice-detail/3483"
    },
    {
      "key": "3758",
      "id": "3758",
      "href": "/objects/construction/project-contract-billing-invoice-detail/3758"
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

## GET /objects/construction/project-contract-billing-invoice-detail/{key}
_Get a project contract billing invoice detail_

**Response 200 — Details of the project contract billing invoice detail:**
```json
{
  "ia::result": {
    "id": "3760",
    "key": "3760",
    "orderEntryDocument": {
      "key": "5143",
      "documentNumber": "Ord#0189#doc",
      "href": "/objects/order-entry/document/5143"
    },
    "accountsReceivableInvoice": {
      "id": "1913",
      "key": "1913",
      "href": "/objects/accounts-receivable/invoice/1913"
    },
    "projectContractBillingInvoiceSummary": {
      "id": "313",
      "key": "313",
      "href": "/objects/construction/project-contract-billing-invoice-summary/313"
    },
    "projectContract": {
      "key": "38",
      "id": "PC 08 Jun",
      "name": "PC 08 Jun",
      "href": "/objects/construction/project-contract/38"
    },
    "projectContractLine": {
      "key": "1568",
      "id": "L1",
      "name": "L1",
      "description": "PC08-L1",
      "isBillable": true,
      "href": "/objects/construction/project-contract-line/1568"
    },
    "externalReferenceNumber": "DIM-JHC-EX-8098",
    "internalReferenceNumber": "DIM-JHC-IN-6924",
    "project": {
      "key": "3",
      "id": "DIM - JHC",
      "name": "Dimensions - Jones Hogan Company",
      "href": "/objects/projects/project/3"
    },
    "task": {
      "key": "153",
      "id": "CS Services",
      "name": "Customer Support Services",
      "href": "/objects/projects/task/153"
    },
    "billingTotals": {
      "originalContractAmount": "150.0000000000",
      "changesApprovedPriorMonths": {
        "additionsAmount": "150.0000000000",
        "deductionsAmount": "0.0000000000"
      },
      "changesApprovedThisMonth": {
        "additionsAmount": "0.0000000000",
        "deductionsAmount": "0.0000000000"
      },
      "netApprovedChangesAmount": "150.0000000000",
      "revisedContractAmount": "300.0000000000",
      "completedFromPriorApplicationAmount": "177.0000000000",
      "completedThisPeriodAmount": "11.0000000000",
      "storedMaterialsAmount": "12.0000000000",
      "completedToDateAmount": "200.0000000000",
      "completedToDatePercent": "66.6700000000",
      "retainage": {
        "percentage": "11.00",
        "amountRetained": "2.5300000000",
        "billedAmount": "0.0000000000",
        "netChangeHeldAmount": "2.5300000000",
        "heldToDateAmount": "25.8500000000",
        "billedToDateAmount": "2.0000000000",
        "balanceToDateAmount": "23.8500000000",
        "previousBalanceAmount": "21.3200000000"
      },
      "billedAmount": "23.0000000000",
      "taxAmount": "0.0000000000",
      "chargeAmount": "0.0000000000",
      "discountAmount": "0.0000000000",
      "balanceToFinishAmount": "123.8500000000",
      "currentDueAmount": "22.4700000000"
    },
    "entity": {
      "key": "1",
      "name": "1",
      "id": "1",
      "href": "/objects/company-config/entity/1"
    },
    "audit": {
      "createdDateTime": "2024-12-01T00:00:00Z",
      "modifiedDateTime": "2025-01-19T00:00:00Z",
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
    "href": "/objects/construction/project-contract-billing-invoice-detail/3760"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-contract-billing-invoice-summary
_List Project contract billing invoice summaries_

**Response 200 — List of Project contract billing invoice summaries:**
```json
{
  "ia::result": [
    {
      "key": "310",
      "id": "310",
      "href": "/objects/construction/project-contract-billing-invoice-summary/310"
    },
    {
      "key": "311",
      "id": "311",
      "href": "/objects/construction/project-contract-billing-invoice-summary/311"
    },
    {
      "key": "313",
      "id": "313",
      "href": "/objects/construction/project-contract-billing-invoice-summary/313"
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

## GET /objects/construction/project-contract-billing-invoice-summary/{key}
_Get a Project contract billing invoice Summary_

**Response 200 — Details of the project contract billing invoice summary:**
```json
{
  "ia::result": {
    "id": "313",
    "key": "313",
    "orderEntryDocument": {
      "key": "5143",
      "id": "SO-AIA-Invoice01-Ord#0189#doc",
      "documentNumber": "Ord#0189#doc",
      "href": "/objects/order-entry/document/5143"
    },
    "accountsReceivableInvoice": {
      "key": "23",
      "id": "23",
      "number": "INV1",
      "href": "/objects/accounts-receivable/invoice/23"
    },
    "projectContract": {
      "key": "38",
      "id": "PC 08 Jun",
      "name": "PC 08 Jun",
      "href": "/objects/construction/project-contract/38"
    },
    "billingTotals": {
      "originalContractAmount": "150.0000000000",
      "changesApprovedPriorMonths": {
        "additionsAmount": "150.0000000000",
        "deductionsAmount": "0.0000000000"
      },
      "changesApprovedThisMonth": {
        "additionsAmount": "0.0000000000",
        "deductionsAmount": "0.0000000000"
      },
      "netApprovedChangesAmount": "150.0000000000",
      "revisedContractAmount": "300.0000000000",
      "completedFromPriorApplicationAmount": "177.0000000000",
      "completedToDateAmount": "200.0000000000",
      "retainage": {
        "amountRetained": "2.5300000000",
        "billedAmount": "0.0000000000",
        "netChangeHeldAmount": "2.5300000000",
        "heldToDateAmount": "25.8500000000",
        "billedToDateAmount": "2.0000000000",
        "balanceToDateAmount": "23.8500000000",
        "previousBalanceAmount": "21.3200000000",
        "totalEarnedLessAmount": "176.1500000000"
      },
      "lessPreviousBillingAmount": "155.6800000000",
      "currentDueAmount": "20.4700000000",
      "balanceToFinishAmount": "123.8500000000",
      "taxAmount": "0.0000000000",
      "discountAmount": "0.0000000000",
      "chargeAmount": "0.0000000000"
    },
    "billingThroughDate": "2024-05-29",
    "billingApplicationNumber": "4",
    "entity": {
      "key": "1",
      "name": "1",
      "id": "1",
      "href": "/objects/company-config/entity/1"
    },
    "project": {
      "key": "1",
      "id": "DIM - HCS",
      "name": "Dimensions - Hands Computer Systems",
      "href": "/objects/projects/project/1"
    },
    "audit": {
      "createdDateTime": "2024-12-01T00:00:00Z",
      "modifiedDateTime": "2025-01-19T00:00:00Z",
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
    "href": "/objects/construction/project-contract-billing-invoice-summary/313"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-contract-line
_List project contract lines_

**Response 200 — example-result-collection-of-project-contract-lines:**
```json
{
  "ia::result": [
    {
      "key": "7",
      "id": "7",
      "href": "/objects/construction/project-contract-line/7"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/construction/project-contract-line/4"
    },
    {
      "key": "6",
      "id": "6",
      "href": "/objects/construction/project-contract-line/6"
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

## POST /objects/construction/project-contract-line
_Create a project contract line_

**Request example — Create a project contract line:**
```json
{
  "projectContract": {
    "key": "5"
  },
  "id": "002",
  "name": "line 2",
  "description": "Contract:BTI-05 - Line 2",
  "contractLineDate": "2023-10-05",
  "glAccount": {
    "key": "26"
  },
  "billingSetup": {
    "billingType": "progressBill",
    "maximumBilling": "totalPrice",
    "summarizeBill": false
  },
  "status": "active",
  "dimensions": {
    "project": {
      "key": "11"
    },
    "item": {
      "key": "13"
    }
  },
  "scope": "Initial survey",
  "internalReference": {
    "referenceNumber": "Ref-BTI-05-004",
    "signedBy": {
      "key": "1"
    }
  },
  "isBillable": true,
  "taxSchedule": {
    "id": "Sale Goods Standard"
  }
}
```
**Request example — Create a project contract line with line entries:**
```json
{
  "projectContract": {
    "key": "5"
  },
  "id": "001",
  "name": "line 1",
  "description": "Contract:BTI-05 - Line 1",
  "contractLineDate": "2023-10-05",
  "glAccount": {
    "key": "26"
  },
  "billingSetup": {
    "billingType": "progressBill",
    "maximumBilling": "totalPrice",
    "summarizeBill": false
  },
  "status": "active",
  "dimensions": {
    "project": {
      "key": "11"
    },
    "item": {
      "key": "13"
    }
  },
  "scope": "Initial survey",
  "internalReference": {
    "referenceNumber": "Ref-BTI-03-003",
    "signedBy": {
      "key": "1"
    }
  },
  "isBillable": true,
  "taxSchedule": {
    "id": "Sale Goods Standard"
  },
  "projectContractLineEntries": [
    {
      "workflowType": "revision",
      "dimensions": {
        "project": {
          "key": "11"
        },
        "item": {
          "key": "13"
        }
      },
      "quantity": "1",
      "externalUOM": "each",
      "unitPrice": "97",
      "priceMarkupPercent": "5",
      "memo": "memo",
      "priceEffectiveDate": "2023-10-14"
    }
  ]
}
```
**Response 201 — Reference to new project contract line:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "7",
    "href": "/objects/construction/project-contract-line/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-contract-line-entry
_List project contract line entries_

**Response 200 — List of project contract line entries:**
```json
{
  "ia::result": [
    {
      "key": "44",
      "id": "44",
      "href": "/objects/construction/project-contract-line-entry/44"
    },
    {
      "key": "40",
      "id": "40",
      "href": "/objects/construction/project-contract-line-entry/40"
    },
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/project-contract-line-entry/1"
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

## GET /objects/construction/project-contract-line-entry/{key}
_Get a project contract line entry_

**Response 200 — Project contract line entry details:**
```json
{
  "ia::result": {
    "key": "5",
    "id": "5",
    "projectContractLine": {
      "key": "4",
      "id": "003",
      "href": "/objects/construction/project-contract-line/4"
    },
    "workflowType": "original",
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
      },
      "department": {
        "key": "3",
        "id": "3",
        "name": "Engineering",
        "href": "/objects/company-config/department/3"
      },
      "project": {
        "key": "1",
        "id": "DIM - BTI",
        "name": "Dimensions - Berkeley Technology Inc",
        "href": "/objects/projects/project/1"
      },
      "customer": {
        "key": "14",
        "id": "BTI",
        "name": "Berkeley Technology Inc",
        "href": "/objects/accounts-receivable/customer/14"
      },
      "vendor": {
        "key": "43",
        "id": "1099 Int",
        "name": "1099 Int",
        "href": "/objects/accounts-payable/vendor/43"
      },
      "employee": {
        "key": "27",
        "id": "12",
        "name": "Eberhardt",
        "href": "/objects/company-config/employee/27"
      },
      "item": {
        "key": "240",
        "id": "3",
        "name": "Rebar #10",
        "href": "/objects/inventory-control/item/240"
      },
      "class": {
        "key": "6",
        "id": "4",
        "name": "Professional Services",
        "href": "/objects/company-config/class/6"
      }
    },
    "quantity": "2.50",
    "externalUOM": "box",
    "unitPrice": "95.75",
    "price": "191.50",
    "priceMarkupPercent": "10.00",
    "priceMarkupAmount": "19.15",
    "linePrice": "210.65",
    "memo": "[updated]",
    "priceEffectiveDate": "2021-10-21",
    "audit": {
      "createdDateTime": "2021-10-21T21:26:38Z",
      "modifiedDateTime": "2021-10-22T00:08:31Z",
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
    "href": "/objects/construction/project-contract-line-entry/5"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/construction/project-contract-line-entry/{key}
_Delete a project contract line entry_


## GET /objects/construction/project-contract-line-task-map
_List project contract line task maps_

**Response 200 — List project contract line task maps:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/project-contract-line-task-map/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/project-contract-line-task-map/3"
    },
    {
      "key": "4",
      "id": "4",
      "href": "/objects/construction/project-contract-line-task-map/4"
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

## POST /objects/construction/project-contract-line-task-map
_Create a project contract line task map_

**Request example — Create a project contract line task map:**
```json
{
  "projectContractLine": {
    "key": "4"
  },
  "project": {
    "id": "BTI - 2019"
  },
  "task": {
    "id": "Customer Services"
  }
}
```
**Response 201 — Reference to project contract line task map:**
```json
{
  "ia::result": {
    "key": "7",
    "id": "7",
    "href": "/objects/construction/project-contract-line-task-map/7"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-contract-line-task-map/{key}
_Get a project contract line task map_

**Response 200 — Get a project contract line task map:**
```json
{
  "ia::result": {
    "key": "2",
    "id": "2",
    "project": {
      "key": "1",
      "id": "BTI - 2019",
      "href": "/objects/projects/project/4"
    },
    "task": {
      "key": "4",
      "id": "Customer Services",
      "href": "/objects/projects/task/4"
    },
    "projectContractLine": {
      "key": "4",
      "id": "003",
      "href": "/objects/construction/project-contract-line/4"
    },
    "audit": {
      "createdDateTime": "2025-01-05T00:00:00Z",
      "modifiedDateTime": "2025-01-19T00:00:00Z",
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
    "href": "/objects/construction/project-contract-line-task-map/2"
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## DELETE /objects/construction/project-contract-line-task-map/{key}
_Delete a project contract line task map_


## GET /objects/construction/project-contract-line/{key}
_Get a project contract line_

**Response 200 — Project contract line details:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "003",
    "projectContract": {
      "key": "1",
      "id": "BTI-01",
      "name": "Berkeley Technology Inc - Contract 01[Revised]",
      "href": "/objects/construction/project-contract/1"
    },
    "name": "BTI-01: line 3",
    "parent": {
      "key": "2",
      "id": "002",
      "name": "line 2",
      "href": "/objects/construction/project-contract-line/2"
    },
    "description": "additional services",
    "contractLineDate": "2023-10-05",
    "glAccount": {
      "key": "207",
      "id": "5001",
      "name": "Construction",
      "href": "/objects/general-ledger/account/207"
    },
    "retainagePercentage": "0.00",
    "isBillable": true,
    "billingSetup": {
      "billingType": "progressBill",
      "maximumBilling": "totalPrice",
      "maximumBillingAmount": "0.00",
      "summarizeBill": false
    },
    "billing": {
      "billedPrice": "2810.65",
      "billedNetRetainage": "2810.65",
      "percentBilled": "50.00",
      "percentBilledNetRetainage": "50.00",
      "retainageHeld": "0.00",
      "retainageReleased": "0.00",
      "retainageBalance": "0.00",
      "paymentsReceived": "1000.00",
      "previouslyAppliedPrice": "0.00"
    },
    "summary": {
      "originalPrice": "0.00",
      "revisionPrice": "0.00",
      "forecastPrice": "0.00",
      "approvedChangePrice": "0.00",
      "pendingChangePrice": "210.65",
      "otherPrice": "0.00",
      "totalPrice": "0.00"
    },
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
      },
      "customer": {
        "key": "14",
        "id": "BTI",
        "name": "Berkeley Technology Inc",
        "href": "/objects/accounts-receivable/customer/14"
      },
      "department": {
        "key": "3",
        "id": "3",
        "name": "Engineering",
        "href": "/objects/company-config/department/3"
      },
      "project": {
        "key": "1",
        "id": "DIM - BTI",
        "name": "Dimensions - Berkeley Technology Inc",
        "href": "/objects/projects/project/1"
      },
      "vendor": {
        "key": "43",
        "id": "1099 Int",
        "name": "1099 Int",
        "href": "/objects/accounts-payable/vendor/43"
      },
      "employee": {
        "key": "1",
        "id": "1",
        "name": "Reser",
        "href": "/objects/company-config/employee/1"
      },
      "item": {
        "key": "18",
        "id": "Implementation",
        "name": "Implimentation",
        "href": "/objects/inventory-control/item/18"
      },
      "class": {
        "key": "6",
        "id": "4",
        "name": "Professional Services",
        "href": "/objects/company-config/class/6"
      },
      "excludeFromGLBudget": false,
      "scope": "Initial survey",
      "inclusions": "NA",
      "exclusions": "NA",
      "terms": "Standard",
      "schedule": {
        "scheduledStartDate": "2023-06-12",
        "actualStartDate": "2023-06-15",
        "scheduledCompletionDate": "2023-06-21",
        "revisedCompletionDate": "2023-06-28",
        "substantialCompletionDate": "2023-06-20",
        "actualCompletionDate": "2023-06-28",
        "noticeToProceedDate": "2023-06-01",
        "responseDueDate": "2023-06-05",
        "executedOnDate": "2023-06-08",
        "scheduleImpact": "2 days"
      },
      "internalReference": {
        "referenceNumber": "Ref-BTI-03-003",
        "initiatedBy": {
          "key": "2",
          "id": "2",
          "name": "Hatcher",
          "href": "/objects/company-config/employee/2"
        },
        "verbalApprovalBy": {
          "key": "2",
          "id": "2",
          "name": "Hatcher",
          "href": "/objects/company-config/employee/2"
        },
        "issuedBy": {
          "key": "28",
          "id": "22",
          "name": "Chandler",
          "href": "/objects/company-config/employee/28"
        },
        "issuedOnDate": "2023-06-10",
        "approvedBy": {
          "key": "31",
          "id": "23",
          "name": "Jurasek",
          "href": "/objects/company-config/employee/31"
        },
        "approvedOnDate": "2023-06-11",
        "signedBy": {
          "key": "1",
          "id": "1",
          "name": "Reser",
          "href": "/objects/company-config/employee/1"
        },
        "signedOnDate": "2023-06-11",
        "source": "None",
        "sourceReferenceNumber": "NA"
      },
      "externalReference": {
        "referenceNumber": "E-REF-003",
        "verbalApprovalBy": {
          "key": "94",
          "name": "Aaron",
          "href": "/objects/company-config/contact/94"
        },
        "approvedBy": {
          "key": "115",
          "name": "Ashish",
          "href": "/objects/company-config/contact/115"
        },
        "approvedOnDate": "2023-06-12",
        "signedBy": {
          "key": "224",
          "name": "Able and Sons, Accountants",
          "href": "/objects/company-config/contact/224"
        },
        "signedOnDate": "2023-06-15"
      }
    },
    "attachment": {
      "id": "pc-att-1",
      "key": "6",
      "href": "/objects/company-config/attachment/6"
    },
    "status": "active",
    "audit": {
      "createdDateTime": "2023-12-07T21:26:38Z",
      "modifiedDateTime": "2023-12-18T00:08:31Z",
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
    "rateTables": {
      "default": {
        "key": "1",
        "id": "rt_main",
        "href": "/objects/construction/rate-table/1"
      },
      "timesheet": {
        "key": "1",
        "id": "rt_main",
        "href": "/objects/construction/rate-table/1"
      },
      "purchasing": {
        "key": "1",
        "id": "rt_main",
        "href": "/objects/construction/rate-table/1"
      },
      "ap": {
        "key": "1",
        "id": "rt_main",
        "href": "/objects/construction/rate-table/1"
      },
      "gl": {
        "key": "1",
        "id": "rt_main",
        "href": "/objects/construction/rate-table/1"
      },
      "creditCard": {
        "key": "1",
        "id": "rt_main",
        "href": "/objects/construction/rate-table/1"
      },
      "employeeExpense": {
        "key": "1",
        "id": "rt_main",
        "href": "/objects/construction/rate-table/1"
      }
    },
    "taxSchedule": {
      "id": "Sale Goods Standard",
      "key": "19",
      "href": "/objects/tax/order-entry-tax-schedule/19"
    },
    "taxSolution": {
      "key": "9",
      "id": "Advanced Tax India",
      "href": "/objects/tax/tax-solution/9"
    },
    "projectContractLineEntries": [
      {
        "key": "5",
        "id": "5",
        "projectContractLine": {
          "key": "4",
          "id": "003",
          "href": "/objects/construction/project-contract-line/4"
        },
        "workflowType": "original",
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "name": "United States of America",
            "href": "/objects/company-config/location/1"
          },
          "department": {
            "key": "3",
            "id": "3",
            "name": "Engineering",
            "href": "/objects/company-config/department/3"
          },
          "project": {
            "key": "1",
            "id": "DIM - BTI",
            "name": "Dimensions - Berkeley Technology Inc",
            "href": "/objects/projects/project/1"
          },
          "customer": {
            "key": "14",
            "id": "BTI",
            "name": "Berkeley Technology Inc",
            "href": "/objects/accounts-receivable/customer/14"
          },
          "vendor": {
            "key": "43",
            "id": "1099 Int",
            "name": "1099 Int",
            "href": "/objects/accounts-payable/vendor/43"
          },
          "employee": {
            "key": "27",
            "id": "12",
            "name": "Eberhardt",
            "href": "/objects/company-config/employee/27"
          },
          "item": {
            "key": "240",
            "id": "3",
            "name": "Rebar #10",
            "href": "/objects/inventory-control/item/240"
          },
          "class": {
            "key": "6",
            "id": "4",
            "name": "Professional Services",
            "href": "/objects/company-config/class/6"
          }
        },
        "quantity": "2.50",
        "externalUOM": "box",
        "unitPrice": "95.75",
        "price": "191.50",
        "priceMarkupPercent": "10.00",
        "priceMarkupAmount": "19.15",
        "linePrice": "210.65",
        "memo": "[updated]",
        "priceEffectiveDate": "2023-10-21",
        "href": "/objects/construction/project-contract-line-entry/5"
      }
    ],
    "changeRequestEntries": [
      {
        "key": "6",
        "id": "6",
        "changeRequest": {
          "key": "1",
          "id": "CR1-DIMBTI-CRHSrce",
          "href": "/objects/construction/change-request/1"
        },
        "workflowType": "pendingChange",
        "dimensions": {
          "location": {
            "key": "1",
            "id": "1",
            "name": "United States of America",
            "href": "/objects/company-config/location/1"
          },
          "department": {
            "key": "3",
            "id": "3",
            "name": "Engineering",
            "href": "/objects/company-config/department/3"
          },
          "project": {
            "key": "1",
            "id": "DIM - BTI",
            "name": "Dimensions - Berkeley Technology Inc",
            "href": "/objects/projects/project/1"
          },
          "customer": {
            "key": "14",
            "id": "BTI",
            "name": "Berkeley Technology Inc",
            "href": "/objects/accounts-receivable/customer/14"
          },
          "vendor": {
            "key": "43",
            "id": "1099 Int",
            "name": "1099 Int",
            "href": "/objects/accounts-payable/vendor/43"
          },
          "employee": {
            "key": "27",
            "id": "12",
            "name": "Eberhardt",
            "href": "/objects/company-config/employee/27"
          },
          "item": {
            "key": "240",
            "id": "3",
            "name": "Rebar #10",
            "href": "/objects/inventory-control/item/240"
          },
          "class": {
            "key": "6",
            "id": "4",
            "name": "Professional Services",
            "href": "/objects/company-config/class/6"
          }
        },
        "numberOfProductionUnits": "500",
        "productionUnitDescription": "sqft",
        "quantity": "2.50",
        "externalUOM": "box",
        "unitCost": "100.00",
        "cost": "1000.00",
        "unitPrice": "100.00",
        "price": "1000.00",
        "priceMarkupPercent": "10.00",
        "priceMarkupAmount": "100.00",
        "linePrice": "1100.00",
        "memo": "change request",
        "projectChangeOrder": {
          "key": "1",
          "id": "PCO1-DIMBTI",
          "href": "/objects/construction/project-change-order/1"
        },
        "projectEstimate": {
          "key": "1",
          "id": "PrimEst-DIMBTI",
          "href": "/objects/construction/project-estimate/1"
        },
        "glAccount": {
          "key": "222",
          "id": "5008",
          "name": "Salaries - Contract",
          "href": "/objects/general-ledger/account/222"
        },
        "projectContract": {
          "key": "1",
          "id": "BTI-01",
          "name": "Berkeley Technology Inc - Contract 01[Revised]",
          "href": "/objects/construction/project-contract/1"
        },
        "projectContractLine": {
          "key": "4",
          "id": "003",
          "name": "003-Billable Labor",
          "href": "/objects/construction/project-contract-line/4"
        },
        "href": "/objects/construction/change-request-line/6"
      }
    ],
    "href": "/objects/construction/project-contract-line/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/project-contract-line/{key}
_Update a project contract line_

**Request example — Update a line and a line entry:**
```json
{
  "name": "BTI-01: line 1",
  "description": "additional services",
  "dimensions": {
    "vendor": {
      "key": "24"
    },
    "department": {
      "key": "3"
    },
    "employee": {
      "key": "1"
    },
    "class": {
      "key": "4"
    },
    "item": {
      "key": "15"
    }
  },
  "projectContractLineEntries": [
    {
      "key": "1",
      "workflowType": "original",
      "dimensions": {
        "project": {
          "key": "11"
        },
        "item": {
          "key": "3"
        }
      },
      "quantity": "2.5",
      "externalUOM": "box",
      "unitPrice": "95.75",
      "priceMarkupPercent": "10",
      "price": "191.50",
      "priceMarkupAmount": "19.15",
      "linePrice": "210.65",
      "memo": "updated markup",
      "priceEffectiveDate": "2023-10-21"
    }
  ]
}
```
**Request example — Add a line entry:**
```json
{
  "projectContractLineEntries": [
    {
      "workflowType": "revision",
      "dimensions": {
        "project": {
          "key": "11"
        },
        "item": {
          "key": "3"
        }
      },
      "quantity": "2",
      "externalUOM": "each",
      "unitPrice": "46",
      "priceMarkupPercent": "10",
      "memo": "added new charge",
      "priceEffectiveDate": "2023-10-10"
    }
  ]
}
```
**Request example — Delete a line entry:**
```json
{
  "projectContractLineEntries": [
    {
      "ia::operation": "delete",
      "key": "2"
    }
  ]
}
```
**Response 200 — Reference to updated project contract line:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "003",
    "href": "/objects/construction/project-contract-line/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/project-contract-line/{key}
_Delete a project contract line_


## GET /objects/construction/project-contract-type
_List project contract types_

**Response 200 — List of project contract types:**
```json
{
  "ia::result": [
    {
      "key": "21",
      "id": "COM",
      "href": "/objects/construction/project-contract-type/21"
    },
    {
      "key": "22",
      "id": "RES",
      "href": "/objects/construction/project-contract-type/22"
    },
    {
      "key": "23",
      "id": "REST-CUST",
      "href": "/objects/construction/project-contract-type/23"
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

## POST /objects/construction/project-contract-type
_Create a project contract type_

**Request example — Create a project contract type:**
```json
{
  "id": "RES",
  "name": "Residential"
}
```
**Response 201 — Reference to new project contract type:**
```json
{
  "ia::result": {
    "key": "22",
    "id": "RES",
    "href": "/objects/construction/project-contract-type/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-contract-type/{key}
_Get a project contract type_

**Response 200 — Get a project contract type:**
```json
{
  "ia::result": {
    "key": "22",
    "id": "RES",
    "name": "Residential",
    "status": "active",
    "audit": {
      "createdDateTime": "2023-08-19T00:00:00Z",
      "modifiedDateTime": "2023-08-19T00:00:00Z",
      "createdByUser": {
        "key": "5",
        "id": "John Doe",
        "href": "/objects/company-config/user/5"
      },
      "createdBy": "5",
      "modifiedByUser": {
        "key": "43",
        "id": "Jane Smith",
        "href": "/objects/company-config/user/43"
      },
      "modifiedBy": "43"
    },
    "href": "/objects/construction/project-contract-type/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/project-contract-type/{key}
_Update a project contract type_

**Request example — Change the name of a project contract type:**
```json
{
  "name": "Temp contract"
}
```
**Response 200 — Reference to updated project contract type:**
```json
{
  "ia::result": {
    "key": "29",
    "id": "TEMP",
    "href": "/objects/construction/project-contract-type/29"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/project-contract-type/{key}
_Delete a project contract type_


## GET /objects/construction/project-contract/{key}
_Get a project contract_

**Response 200 — Project contract details:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "BTI-01",
    "name": "Berkeley Technology Inc - Contract 01",
    "project": {
      "id": "DIM - BTI",
      "name": "Dimensions - Berkeley Technology Inc",
      "key": "1",
      "href": "/objects/projects/project/1"
    },
    "location": {
      "id": "1",
      "name": "United States of America",
      "key": "1",
      "href": "/objects/company-config/location/1"
    },
    "customer": {
      "id": "BTI",
      "name": "Berkeley Technology Inc",
      "key": "14",
      "href": "/objects/accounts-receivable/customer/14"
    },
    "contractDate": "2023-05-15",
    "description": "BTI Project - Main lobby renovation contract",
    "projectContractType": {
      "id": "COM",
      "key": "2",
      "href": "/objects/construction/project-contract-type/2"
    },
    "architect": {
      "id": "Eberhardt",
      "key": "12",
      "href": "/objects/company-config/contact/12"
    },
    "isBillable": true,
    "attachment": {
      "id": "pc-att-2",
      "key": "7",
      "href": "/objects/company-config/attachment/7"
    },
    "status": "active",
    "summary": {
      "totalPrice": "2810.65",
      "originalPrice": "1100.00",
      "revisionPrice": "210.65",
      "approvedChangePrice": "1500.00",
      "pendingChangePrice": "311.85",
      "otherPrice": "900.00",
      "forecastPrice": "750.00"
    },
    "billing": {
      "billedPrice": "0.00",
      "totalBilledNetRetainage": "0.00",
      "percentBilled": "0.00",
      "percentBilledNetRetainage": "0.00",
      "totalRetainageHeld": "0.00",
      "totalRetainageReleased": "0.00",
      "retainageBalance": "0.00",
      "balanceToBill": "2810.65",
      "balanceToBillNetRetainage": "2810.65",
      "totalPaymentsReceived": "0.00",
      "netTotalBilled": "2810.65",
      "netTotalPaymentsReceived": "1000.00",
      "subtotalBilledAsTax": "0.00",
      "subtotalBilledAsDiscount": "0.00",
      "subtotalBilledAsCharge": "0.00",
      "lastApplicationNumber": "A-122"
    },
    "scope": "Project scope only",
    "inclusions": "Per original contract",
    "exclusions": "Plumbing",
    "terms": "Per original contract",
    "schedule": {
      "scheduledStartDate": "2023-06-15",
      "actualStartDate": "2023-06-30",
      "scheduledCompletionDate": "2022-11-15",
      "revisedCompletionDate": "2023-12-15",
      "substantialCompletionDate": "2023-09-30",
      "actualCompletionDate": "2023-12-15",
      "noticeToProceedDate": "2023-05-30",
      "responseDueDate": "2023-06-05",
      "executedOnDate": "2023-06-01",
      "scheduleImpact": "NA"
    },
    "internalReference": {
      "referenceNumber": "INT-01",
      "initiatedBy": {
        "key": "2",
        "id": "2",
        "name": "Hatcher",
        "href": "/objects/company-config/employee/2"
      },
      "verbalApprovalBy": {
        "key": "2",
        "id": "2",
        "name": "Hatcher",
        "href": "/objects/company-config/employee/2"
      },
      "issuedBy": {
        "key": "25",
        "id": "123",
        "name": "Marquess",
        "href": "/objects/company-config/employee/25"
      },
      "issuedOnDate": "2023-05-30",
      "approvedBy": {
        "key": "1",
        "id": "1",
        "name": "Reser",
        "href": "/objects/company-config/employee/1"
      },
      "approvedOnDate": "2023-10-02",
      "signedBy": {
        "key": "32",
        "id": "Robert",
        "name": "Robert",
        "href": "/objects/company-config/employee/32"
      },
      "signedOnDate": "2023-05-31",
      "source": "NA",
      "sourceReferenceNumber": "REF-01"
    },
    "externalReference": {
      "referenceNumber": "A23",
      "verbalApprovalBy": {
        "key": "6",
        "id": "Johnson",
        "href": "/objects/company-config/contact/6"
      },
      "approvedBy": {
        "key": "69",
        "href": "/objects/company-config/contact/69"
      },
      "approvedOnDate": "2023-11-03",
      "signedBy": {
        "key": "200",
        "id": "Modulus Industries",
        "href": "/objects/company-config/contact/200"
      },
      "signedOnDate": "2023-12-01"
    },
    "audit": {
      "modifiedDateTime": "2022-01-19T00:00:00Z",
      "createdDateTime": "2023-12-01T00:00:00Z",
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
    "glBudgetPosting": {
      "isPosted": true,
      "postingPeriodBasedOn": "projectContractDate",
      "originalGLBudget": {
        "key": "5",
        "id": "KPI Original Budgets",
        "href": "/objects/general-ledger/budget/5"
      },
      "revisionGLBudget": {
        "key": "6",
        "id": "KPI Revision Budgets",
        "href": "/objects/general-ledger/budget/6"
      },
      "approvedGLBudget": {
        "key": "8",
        "id": "KPI Approved Budgets",
        "href": "/objects/general-ledger/budget/8"
      },
      "pendingGLBudget": {
        "key": "7",
        "id": "KPI Pending Budgets",
        "href": "/objects/general-ledger/budget/7"
      },
      "forecastGLBudget": {
        "key": "9",
        "id": "KPI Forecast Budgets",
        "href": "/objects/general-ledger/budget/9"
      },
      "otherGLBudget": {
        "key": "10",
        "id": "KPI Other Budgets",
        "href": "/objects/general-ledger/budget/10"
      }
    },
    "excludeFromWIPReporting": false,
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
    "href": "/objects/construction/project-contract/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/project-contract/{key}
_Update a project contract_

**Request example — example-update-project-contract:**
```json
{
  "name": "Berkeley Technology Inc - Contract 05[Revised]",
  "contractDate": "2023-10-15",
  "description": "BTI Project - Main lobby renovation contract",
  "scope": "Project scope only [updated]",
  "inclusions": "Per original contract [updated]",
  "exclusions": "Plumbing [updated]",
  "terms": "Per revised contract",
  "schedule": {
    "scheduledStartDate": "2023-11-15",
    "scheduledCompletionDate": "2022-11-15"
  },
  "internalReference": {
    "signedBy": {
      "id": "Robert"
    },
    "signedOnDate": "2023-10-15"
  },
  "projectContractType": {
    "id": "COM"
  }
}
```
**Response 200 — Reference to updated project contract:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "BTI-01",
    "href": "/objects/construction/project-contract/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/project-contract/{key}
_Delete a project contract_


## GET /objects/construction/project-estimate
_List project estimates_

**Response 200 — Example 1:**
```json
{
  "ia::result": [
    {
      "key": "2",
      "id": "PJE-01-001",
      "href": "/objects/construction/project-estimate/2"
    },
    {
      "key": "1",
      "id": "PJE-00-01",
      "href": "/objects/construction/project-estimate/1"
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

## POST /objects/construction/project-estimate
_Create a project estimate_

**Request example — Create a new project that contains two project lines:**
```json
{
  "id": "PE-CB-BTI-003",
  "description": "PE-CB-BTI-003",
  "estimateDate": "2024-03-14",
  "isPrimary": false,
  "isPrimaryForecast": false,
  "status": "active",
  "postTo": "firstPeriod",
  "budget": {
    "key": "2"
  },
  "projectEstimateType": {
    "key": "7"
  },
  "project": {
    "key": "1"
  },
  "projectEstimateLines": [
    {
      "externalUOM": "Hour",
      "quantity": "10.00",
      "unitCost": "300.00",
      "amount": "3000.00",
      "numberOfProductionUnits": 0,
      "workflowType": "original",
      "glAccount": {
        "key": "210"
      },
      "dimensions": {
        "department": {
          "key": "3"
        },
        "project": {
          "key": "1"
        },
        "item": {
          "key": "17"
        },
        "costType": {
          "key": "17"
        },
        "class": {
          "key": "6"
        },
        "task": {
          "key": "1"
        }
      }
    },
    {
      "externalUOM": "Box",
      "quantity": "10.00",
      "unitCost": "300.00",
      "amount": "3000.00",
      "numberOfProductionUnits": 0,
      "workflowType": "original",
      "glAccount": {
        "key": "210"
      },
      "dimensions": {
        "department": {
          "key": "3"
        },
        "project": {
          "key": "1"
        },
        "item": {
          "key": "17"
        },
        "costType": {
          "key": "87"
        },
        "class": {
          "key": "6"
        },
        "task": {
          "key": "10"
        }
      }
    }
  ]
}
```
**Response 201 — Reference to new project estimate:**
```json
{
  "ia::result": {
    "key": "27",
    "id": "PE-CB-BTI-003",
    "href": "/objects/construction/project-estimate/27"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-estimate-line
_List project estimate lines_

**Response 200 — Get project estimate lines:**
```json
{
  "ia::result": [
    {
      "key": "32",
      "id": "32",
      "href": "/objects/construction/project-estimate-line/32"
    },
    {
      "key": "34",
      "id": "34",
      "href": "/objects/construction/project-estimate-line/34"
    },
    {
      "key": "31",
      "id": "31",
      "href": "/objects/construction/project-estimate-line/31"
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

## GET /objects/construction/project-estimate-line/{key}
_Get a project estimate line_

**Response 200 — Project estimate line details:**
```json
{
  "ia::result": {
    "key": "1",
    "id": "1",
    "amount": "2000.00",
    "quantity": "10",
    "unitCost": "1000.00",
    "currency": "USD",
    "memo": "service charges",
    "lineNumber": 1,
    "externalUOM": "Piece",
    "workflowType": "original",
    "isPosted": false,
    "effectiveDate": "2022-06-23",
    "numberOfProductionUnits": 200,
    "productionUnitDescription": "days",
    "projectEstimate": {
      "key": "1",
      "id": "Original",
      "href": "/objects/construction/project-estimate/1"
    },
    "glAccount": {
      "key": "144",
      "id": "1112",
      "name": "Employee Advances",
      "href": "/objects/general-ledger/account/144"
    },
    "changeRequest": {
      "key": "1",
      "id": "CR-TM-02",
      "href": "/objects/construction/change-request/1"
    },
    "changeRequestLine": {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/change-request-line/1"
    },
    "dimensions": {
      "location": {
        "key": "1",
        "id": "1",
        "name": "United States of America",
        "href": "/objects/company-config/location/1"
      },
      "department": {
        "key": "1",
        "id": "2",
        "name": "Engineering",
        "href": "/objects/company-config/department/1"
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
      }
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
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "modifiedBy": "1"
    },
    "href": "/objects/construction/project-estimate-line/1"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-estimate-type
_List project estimate types_

**Response 200 — Get project estimate types:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "ApprovedChange",
      "href": "/objects/construction/project-estimate-type/1"
    },
    {
      "key": "2",
      "id": "Original",
      "href": "/objects/construction/project-estimate-type/2"
    },
    {
      "key": "3",
      "id": "No SWFT",
      "href": "/objects/construction/project-estimate-type/3"
    },
    {
      "key": "4",
      "id": "Novaluesxml",
      "href": "/objects/construction/project-estimate-type/4"
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

## POST /objects/construction/project-estimate-type
_Create a project estimate type_

**Request example — Create a project estimate type:**
```json
{
  "id": "ApprovedChangeandOther",
  "workflowTypes": [
    "approvedChange",
    "other"
  ],
  "estimateCategory": "originalEstimate"
}
```
**Response 201 — Reference to new project estimate type:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "ApprovedChangeandOther",
    "href": "/objects/construction/project-estimate-type/9"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/project-estimate-type/{key}
_Get a project estimate type_

**Response 200 — Project estimate type details:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "ApprovedChangeandOther",
    "status": "active",
    "workflowTypes": [
      "approvedChange",
      "other"
    ],
    "audit": {
      "createdDateTime": "2024-02-19T07:32:40Z",
      "modifiedDateTime": "2024-02-19T07:32:40Z",
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
    "estimateCategory": "originalEstimate",
    "href": "/objects/construction/project-estimate-type/9"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/project-estimate-type/{key}
_Update a project estimate type_

**Request example — Set a project estimate type to inactive status:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to the updated project estimate type:**
```json
{
  "ia::result": {
    "key": "9",
    "id": "ApprovedChangeandOther",
    "href": "/objects/construction/project-estimate-type/9"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/project-estimate-type/{key}
_Delete a project estimate type_


## GET /objects/construction/project-estimate/{key}
_Get a project estimate_

**Response 200 — Project estimate details including project estimate lines:**
```json
{
  "ia::result": {
    "key": "27",
    "id": "PE-CB-BTI-003",
    "description": "PE-CB-BTI-003",
    "estimateDate": "2024-03-14",
    "isPrimary": false,
    "isPrimaryForecast": false,
    "status": "active",
    "isPosted": false,
    "budget": {
      "key": "2",
      "id": "Root PJ Estimates",
      "href": "/objects/general-ledger/budget/2"
    },
    "postTo": "firstPeriod",
    "project": {
      "key": "1",
      "id": "DIM - BTI",
      "name": "Dimensions - Berkeley Technology Inc",
      "startDate": "2000-01-01",
      "endDate": "2023-12-31",
      "href": "/objects/projects/project/1"
    },
    "projectEstimateType": {
      "key": "7",
      "id": "Original",
      "workflowTypes": [
        "original"
      ],
      "href": "/objects/construction/project-estimate-type/7"
    },
    "currency": "USD",
    "totalEstimateAmount": "6000.00",
    "location": {
      "key": "1",
      "id": "USA",
      "name": "United States of America"
    },
    "parentProject": {
      "key": "2",
      "id": "DIM",
      "name": "Dimensions"
    },
    "customer": {
      "key": "14",
      "id": "BTI",
      "name": "Berkeley Technology Inc",
      "href": "/objects/accounts-receivable/customer/14"
    },
    "attachment": {
      "id": "Doc001"
    },
    "audit": {
      "modifiedDateTime": "2023-03-14T06:25:35Z",
      "createdDateTime": "2023-03-14T06:25:35Z",
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
    "projectEstimateLines": [
      {
        "id": "68",
        "key": "68",
        "lineNumber": 1,
        "projectEstimate": {
          "id": "PE-CB-BTI-003",
          "key": "27",
          "href": "/objects/construction/project-estimate/27"
        },
        "externalUOM": "Hour",
        "quantity": "10",
        "unitCost": "300.00",
        "amount": "3000.00",
        "memo": "memo for item 1",
        "currency": "USD",
        "workflowType": "original",
        "isPosted": false,
        "glAccount": {
          "key": "210",
          "id": "5001.03",
          "name": "Construction Miscellaneous",
          "href": "/objects/general-ledger/account/210"
        },
        "dimensions": {
          "department": {
            "key": "3",
            "id": "3",
            "name": "Engineering",
            "href": "/objects/company-config/department/3"
          },
          "location": {
            "key": "1",
            "id": "1",
            "name": "United States of America",
            "href": "/objects/company-config/location/1"
          },
          "project": {
            "key": "1",
            "id": "DIM - BTI",
            "name": "Dimensions - Berkeley Technology Inc",
            "href": "/objects/projects/project/1"
          },
          "customer": {
            "key": "14",
            "id": "BTI",
            "name": "Berkeley Technology Inc",
            "href": "/objects/accounts-receivable/customer/14"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "GenLab"
          },
          "employee": {
            "key": "10",
            "id": "EMP-10",
            "name": "Thomas"
          },
          "item": {
            "key": "17",
            "id": "Design",
            "name": "Design",
            "href": "/objects/inventory-control/item/17"
          },
          "class": {
            "key": "6",
            "id": "4",
            "name": "Professional Services",
            "href": "/objects/company-config/class/6"
          },
          "task": {
            "key": "1",
            "id": "TSK-RT-0001",
            "name": "DIM - BTI01",
            "href": "/objects/projects/task/1"
          },
          "costType": {
            "key": "17",
            "id": "GNC",
            "name": "General Conditions  DIM-BTI 0001",
            "href": "/objects/construction/cost-type/17"
          }
        },
        "effectiveDate": "2022-06-23",
        "numberOfProductionUnits": 0,
        "productionUnitDescription": "days",
        "changeRequest": {
          "key": "1",
          "id": "CR-TM-02",
          "href": "/objects/construction/change-request/1"
        },
        "changeRequestLine": {
          "key": "1",
          "id": "1",
          "href": "/objects/construction/change-request-line/1"
        },
        "audit": {
          "modifiedDateTime": "2023-03-14T00:00:00Z",
          "createdDateTime": "2023-03-14T00:00:00Z",
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
        "href": "/objects/construction/project-estimate-line/68"
      },
      {
        "id": "69",
        "key": "69",
        "lineNumber": 2,
        "projectEstimate": {
          "id": "PE-CB-BTI-003",
          "key": "27",
          "href": "/objects/construction/project-estimate/27"
        },
        "externalUOM": "Box",
        "quantity": "10",
        "unitCost": "300.00",
        "amount": "3000.00",
        "memo": "memo for item 2",
        "currency": "USD",
        "workflowType": "original",
        "isPosted": false,
        "glAccount": {
          "key": "210",
          "id": "5001.03",
          "name": "Construction Miscellaneous",
          "href": "/objects/general-ledger/account/210"
        },
        "dimensions": {
          "department": {
            "key": "3",
            "id": "3",
            "name": "Engineering",
            "href": "/objects/company-config/department/3"
          },
          "location": {
            "key": "1",
            "id": "1",
            "name": "United States of America",
            "href": "/objects/company-config/location/1"
          },
          "project": {
            "key": "1",
            "id": "DIM - BTI",
            "name": "Dimensions - Berkeley Technology Inc",
            "href": "/objects/projects/project/1"
          },
          "customer": {
            "key": "14",
            "id": "BTI",
            "name": "Berkeley Technology Inc",
            "href": "/objects/accounts-receivable/customer/14"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "GenLab"
          },
          "employee": {
            "key": "10",
            "id": "EMP-10",
            "name": "Thomas"
          },
          "item": {
            "key": "17",
            "id": "Design",
            "name": "Design",
            "href": "/objects/inventory-control/item/17"
          },
          "class": {
            "key": "6",
            "id": "4",
            "name": "Professional Services",
            "href": "/objects/company-config/class/6"
          },
          "task": {
            "key": "10",
            "id": "TSK-RT-0022",
            "name": "DIM - BTI10",
            "href": "/objects/projects/task/10"
          },
          "costType": {
            "key": "87",
            "id": "LABOR",
            "name": "LABOR GROUP DIM-BTI 0022",
            "href": "/objects/construction/cost-type/87"
          }
        },
        "effectiveDate": "2022-06-23",
        "numberOfProductionUnits": 0,
        "productionUnitDescription": "days",
        "changeRequest": {
          "key": "1",
          "id": "CR-TM-02",
          "href": "/objects/construction/change-request/1"
        },
        "changeRequestLine": {
          "key": "1",
          "id": "1",
          "href": "/objects/construction/change-request-line/1"
        },
        "audit": {
          "modifiedDateTime": "2023-03-14T00:00:00Z",
          "createdDateTime": "2023-03-14T00:00:00Z",
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
        "href": "/objects/construction/project-estimate-line/69"
      }
    ],
    "href": "/objects/construction/project-estimate/27"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/project-estimate/{key}
_Update a project estimate_

**Request example — Update an existing line and add a new line:**
```json
{
  "description": "Project estimate for BUD BTI- update4",
  "estimateDate": "2022-06-24",
  "projectEstimateLines": [
    {
      "key": "70",
      "externalUOM": "Seconds",
      "quantity": "10.00",
      "unitCost": "500.00",
      "amount": "5000.00",
      "numberOfProductionUnits": 0,
      "workflowType": "original",
      "glAccount": {
        "key": "210"
      },
      "dimensions": {
        "department": {
          "key": "7"
        },
        "project": {
          "key": "1"
        },
        "item": {
          "key": "17"
        },
        "costType": {
          "key": "17"
        },
        "class": {
          "key": "2"
        },
        "task": {
          "key": "1"
        }
      }
    },
    {
      "externalUOM": "Seconds",
      "quantity": "10.00",
      "unitCost": "600.00",
      "amount": "6000.00",
      "numberOfProductionUnits": 0,
      "workflowType": "original",
      "glAccount": {
        "key": "210"
      },
      "dimensions": {
        "department": {
          "key": "7"
        },
        "project": {
          "key": "1"
        },
        "item": {
          "key": "17"
        },
        "costType": {
          "key": "17"
        },
        "class": {
          "key": "2"
        },
        "task": {
          "key": "1"
        }
      }
    }
  ]
}
```
**Request example — Update an existing line:**
```json
{
  "description": "Project estimate for BUD BTI- update3",
  "estimateDate": "2022-06-24",
  "projectEstimateLines": [
    {
      "key": "70",
      "externalUOM": "Seconds",
      "quantity": "10.00",
      "unitCost": "400.00",
      "amount": "4000.00",
      "numberOfProductionUnits": 0,
      "workflowType": "original",
      "glAccount": {
        "key": "210"
      },
      "dimensions": {
        "department": {
          "key": "7"
        },
        "project": {
          "key": "1"
        },
        "item": {
          "key": "17"
        },
        "costType": {
          "key": "17"
        },
        "class": {
          "key": "2"
        },
        "task": {
          "key": "1"
        }
      }
    }
  ]
}
```
**Request example — Delete a line:**
```json
{
  "projectEstimateLines": [
    {
      "ia::operation": "delete",
      "key": "67"
    }
  ]
}
```
**Response 200 — Reference to updated project estimate:**
```json
{
  "ia::result": {
    "key": "23",
    "id": "PE-GL-T001",
    "href": "/objects/construction/project-estimate/23"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/project-estimate/{key}
_Delete a project estimate_


## GET /objects/construction/rate-table
_List construction rate tables_

**Response 200 — List construction rate tables:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "RT-00001",
      "href": "/objects/construction/rate-table/84"
    },
    {
      "key": "85",
      "id": "RT-00002",
      "href": "/objects/construction/rate-table/85"
    },
    {
      "key": "60",
      "id": "RT-00003",
      "href": "/objects/construction/rate-table/60"
    },
    {
      "key": "78",
      "id": "RT-00004",
      "href": "/objects/construction/rate-table/78"
    },
    {
      "key": "79",
      "id": "RT-00005",
      "href": "/objects/construction/rate-table/79"
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

## POST /objects/construction/rate-table
_Create a construction rate table_

**Request example — Create a construction rate table:**
```json
{
  "id": "2025-LV2",
  "name": "2025 Level 2",
  "description": "2025 Level 2 Rate Table",
  "location": {
    "key": "1"
  },
  "status": "active",
  "timesheetLines": [
    {
      "lineNumber": 1,
      "description": "Labor Time - Overtime Pricing.",
      "startDate": "2025-08-03",
      "markupPercent": "8.250",
      "laborRate": "115.500",
      "accumulationType": {
        "key": "2"
      },
      "standardCostType": {
        "key": "33"
      },
      "standardTask": {
        "key": "3"
      },
      "employeePosition": {
        "key": "2"
      },
      "laborClass": {
        "key": "2"
      },
      "laborShift": {
        "key": "2"
      },
      "laborUnion": {
        "key": "2"
      },
      "timeType": {
        "key": "1"
      },
      "dimensions": {
        "employee": {
          "key": "10"
        },
        "project": {
          "key": "2"
        },
        "customer": {
          "key": "13"
        },
        "vendor": {
          "key": "357"
        },
        "item": {
          "key": "13"
        },
        "warehouse": {
          "key": "6"
        },
        "class": {
          "key": "731"
        },
        "task": {
          "key": "2"
        }
      }
    }
  ],
  "purchasingLines": [
    {
      "lineNumber": 1,
      "description": "Purchase Orders - Equipment Markup.",
      "startDate": "2025-08-03",
      "markupPercent": "15.900",
      "unitPrice": "112.560",
      "accumulationType": {
        "key": "2"
      },
      "standardCostType": {
        "key": "33"
      },
      "standardTask": {
        "key": "3"
      },
      "dimensions": {
        "employee": {
          "key": "10"
        },
        "project": {
          "key": "2"
        },
        "customer": {
          "key": "13"
        },
        "vendor": {
          "key": "357"
        },
        "item": {
          "key": "13"
        },
        "warehouse": {
          "key": "6"
        },
        "class": {
          "key": "731"
        },
        "task": {
          "key": "2"
        }
      }
    }
  ],
  "accountsPayableLines": [
    {
      "lineNumber": 1,
      "description": "Subcontractor costs - Standard Markup.",
      "startDate": "2025-08-01",
      "markupPercent": "25.500",
      "accumulationType": {
        "key": "2"
      },
      "standardCostType": {
        "key": "33"
      },
      "standardTask": {
        "key": "3"
      },
      "dimensions": {
        "employee": {
          "key": "10"
        },
        "project": {
          "key": "2"
        },
        "customer": {
          "key": "13"
        },
        "vendor": {
          "key": "357"
        },
        "item": {
          "key": "13"
        },
        "warehouse": {
          "key": "6"
        },
        "class": {
          "key": "731"
        },
        "task": {
          "key": "2"
        }
      }
    }
  ],
  "journalLines": [
    {
      "lineNumber": 1,
      "description": "Overhead Allocation - Project.",
      "startDate": "2025-08-01",
      "markupPercent": "12.500",
      "accumulationType": {
        "key": "2"
      },
      "standardCostType": {
        "key": "33"
      },
      "standardTask": {
        "key": "3"
      },
      "dimensions": {
        "employee": {
          "key": "10"
        },
        "project": {
          "key": "2"
        },
        "customer": {
          "key": "13"
        },
        "vendor": {
          "key": "357"
        },
        "item": {
          "key": "13"
        },
        "warehouse": {
          "key": "6"
        },
        "class": {
          "key": "731"
        },
        "task": {
          "key": "2"
        }
      }
    }
  ],
  "creditCardLines": [
    {
      "lineNumber": 1,
      "description": "Corporate Card - Supplies Pricing.",
      "startDate": "2025-08-03",
      "markupPercent": "15.900",
      "accumulationType": {
        "key": "2"
      },
      "standardCostType": {
        "key": "33"
      },
      "standardTask": {
        "key": "3"
      },
      "dimensions": {
        "employee": {
          "key": "10"
        },
        "project": {
          "key": "2"
        },
        "customer": {
          "key": "13"
        },
        "vendor": {
          "key": "357"
        },
        "item": {
          "key": "13"
        },
        "warehouse": {
          "key": "6"
        },
        "class": {
          "key": "731"
        },
        "task": {
          "key": "2"
        }
      }
    }
  ],
  "employeeExpenseLines": [
    {
      "lineNumber": 1,
      "description": "Employee Expenses - Standard Markup.",
      "startDate": "2025-08-02",
      "markupPercent": "14.800",
      "accumulationType": {
        "key": "2"
      },
      "standardCostType": {
        "key": "33"
      },
      "standardTask": {
        "key": "3"
      },
      "dimensions": {
        "employee": {
          "key": "10"
        },
        "project": {
          "key": "2"
        },
        "customer": {
          "key": "13"
        },
        "vendor": {
          "key": "357"
        },
        "item": {
          "key": "13"
        },
        "warehouse": {
          "key": "6"
        },
        "class": {
          "key": "731"
        },
        "task": {
          "key": "2"
        }
      }
    }
  ]
}
```
**Response 201 — Reference to construction rate table:**
```json
{
  "ia::result": {
    "key": "111",
    "id": "2025-LV2",
    "href": "/objects/construction/rate-table/111"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/rate-table-accounts-payable-line
_List rate table accounts payable lines_

**Response 200 — List rate table accounts payable lines:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/construction/rate-table-accounts-payable-line/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/construction/rate-table-accounts-payable-line/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/construction/rate-table-accounts-payable-line/60"
    },
    {
      "key": "78",
      "id": "78",
      "href": "/objects/construction/rate-table-accounts-payable-line/78"
    },
    {
      "key": "79",
      "id": "79",
      "href": "/objects/construction/rate-table-accounts-payable-line/79"
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

## GET /objects/construction/rate-table-accounts-payable-line/{key}
_Get a rate table accounts payable line_

**Response 200 — Get a rate table accounts payable line:**
```json
{
  "ia::result": {
    "key": "397",
    "id": "397",
    "rateTable": {
      "key": "145",
      "id": "2025-LV2",
      "name": "2025 Level 2",
      "href": "/objects/construction/rate-table/145"
    },
    "href": "/objects/construction/rate-table-credit-card-line/397",
    "lineNumber": 1,
    "description": "Subcontractor costs - Standard Markup.",
    "startDate": "2025-08-01",
    "markupPercent": "25.500",
    "accumulationType": {
      "key": "2",
      "id": "ACCT-2",
      "href": "/objects/construction/accumulation-type/2"
    },
    "standardCostType": {
      "key": "33",
      "id": "CT-RT-0010",
      "name": "CT-RT-0010 MATERIAL",
      "href": "/objects/construction/standard-cost-type/33"
    },
    "standardTask": {
      "key": "3",
      "id": "TSK-RT-0011",
      "name": "TSK-RT-0011 Name",
      "href": "/objects/construction/standard-task/3"
    },
    "dimensions": {
      "employee": {
        "key": "10",
        "id": "10",
        "name": "Glenn Thomson",
        "href": "/objects/company-config/employee/10"
      },
      "project": {
        "key": "2",
        "id": "TLC-XML30-2",
        "name": "TalComp Training Initiative",
        "href": "/objects/projects/project/2"
      },
      "customer": {
        "key": "13",
        "id": "113",
        "name": "TalComp Industries",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "vendor": {
        "key": "357",
        "id": "1605212096809",
        "name": "Industry Knowledge Consulting LLC",
        "href": "/objects/accounts-payable/vendor/357"
      },
      "item": {
        "key": "13",
        "id": "PTK-0013",
        "name": "Participant Training Kit",
        "href": "/objects/inventory-control/item/13"
      },
      "warehouse": {
        "key": "6",
        "id": "TSDC-006",
        "name": "Training Supplies Distribution Center",
        "href": "/objects/inventory-control/warehouse/6"
      },
      "class": {
        "key": "731",
        "id": "ETO_CLS_001",
        "name": "Enterprise Training Operations",
        "href": "/objects/company-config/class/731"
      },
      "task": {
        "key": "2",
        "id": "CPD-002",
        "name": "Course Preparation and Design",
        "href": "/objects/projects/task/2"
      }
    },
    "audit": {
      "createdDateTime": "2025-01-08T11:28:12Z",
      "modifiedDateTime": "2025-01-08T11:28:12Z",
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
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/rate-table-credit-card-line
_List rate table credit card lines_

**Response 200 — List rate table credit card lines:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/construction/rate-table-credit-card-line/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/construction/rate-table-credit-card-line/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/construction/rate-table-credit-card-line/60"
    },
    {
      "key": "78",
      "id": "78",
      "href": "/objects/construction/rate-table-credit-card-line/78"
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

## GET /objects/construction/rate-table-credit-card-line/{key}
_Get a rate table credit card line_

**Response 200 — Get a rate table credit card line:**
```json
{
  "ia::result": {
    "key": "145",
    "id": "145",
    "rateTable": {
      "key": "145",
      "id": "2025-LV2",
      "name": "2025 Level 2",
      "href": "/objects/construction/rate-table/145"
    },
    "href": "/objects/construction/rate-table-credit-card-line/145",
    "lineNumber": 1,
    "description": "Corporate Card - Supplies Pricing.",
    "startDate": "2025-08-03",
    "markupPercent": "15.900",
    "accumulationType": {
      "key": "2",
      "id": "ACCT-2",
      "href": "/objects/construction/accumulation-type/2"
    },
    "standardCostType": {
      "key": "33",
      "id": "CT-RT-0010",
      "name": "CT-RT-0010 MATERIAL",
      "href": "/objects/construction/standard-cost-type/33"
    },
    "standardTask": {
      "key": "3",
      "id": "TSK-RT-0011",
      "name": "TSK-RT-0011 Name",
      "href": "/objects/construction/standard-task/3"
    },
    "dimensions": {
      "employee": {
        "key": "10",
        "id": "10",
        "name": "Glenn Thomson",
        "href": "/objects/company-config/employee/10"
      },
      "project": {
        "key": "2",
        "id": "TLC-XML30-2",
        "name": "TalComp Training Initiative",
        "href": "/objects/projects/project/2"
      },
      "customer": {
        "key": "13",
        "id": "113",
        "name": "TalComp Industries",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "vendor": {
        "key": "357",
        "id": "1605212096809",
        "name": "Industry Knowledge Consulting LLC",
        "href": "/objects/accounts-payable/vendor/357"
      },
      "item": {
        "key": "13",
        "id": "PTK-0013",
        "name": "Participant Training Kit",
        "href": "/objects/inventory-control/item/13"
      },
      "warehouse": {
        "key": "6",
        "id": "TSDC-006",
        "name": "Training Supplies Distribution Center",
        "href": "/objects/inventory-control/warehouse/6"
      },
      "class": {
        "key": "731",
        "id": "ETO_CLS_001",
        "name": "Enterprise Training Operations",
        "href": "/objects/company-config/class/731"
      },
      "task": {
        "key": "2",
        "id": "CPD-002",
        "name": "Course Preparation and Design",
        "href": "/objects/projects/task/2"
      }
    },
    "audit": {
      "createdDateTime": "2025-01-08T11:28:12Z",
      "modifiedDateTime": "2025-01-08T11:28:12Z",
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
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/rate-table-employee-expense-line
_List rate table employee expense lines_

**Response 200 — List rate table employee expense lines:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/construction/rate-table-employee-expense-line/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/construction/rate-table-employee-expense-line/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/construction/rate-table-employee-expense-line/60"
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

## GET /objects/construction/rate-table-employee-expense-line/{key}
_Get a rate table employee expense line_

**Response 200 — Get a rate table employee expense line:**
```json
{
  "ia::result": {
    "key": "30",
    "id": "30",
    "rateTable": {
      "key": "145",
      "id": "2025-LV2",
      "name": "2025 Level 2",
      "href": "/objects/construction/rate-table/145"
    },
    "href": "/objects/construction/rate-table-employee-expense-line/30",
    "lineNumber": 1,
    "description": "Employee Expenses - Training Costs.",
    "startDate": "2025-08-02",
    "markupPercent": "14.800",
    "accumulationType": {
      "key": "2",
      "id": "ACCT-2",
      "href": "/objects/construction/accumulation-type/2"
    },
    "standardCostType": {
      "key": "33",
      "id": "CT-RT-0010",
      "name": "CT-RT-0010 MATERIAL",
      "href": "/objects/construction/standard-cost-type/33"
    },
    "standardTask": {
      "key": "3",
      "id": "TSK-RT-0011",
      "name": "TSK-RT-0011 Name",
      "href": "/objects/construction/standard-task/3"
    },
    "dimensions": {
      "employee": {
        "key": "10",
        "id": "10",
        "name": "Glenn Thomson",
        "href": "/objects/company-config/employee/10"
      },
      "project": {
        "key": "2",
        "id": "TLC-XML30-2",
        "name": "TalComp Training Initiative",
        "href": "/objects/projects/project/2"
      },
      "customer": {
        "key": "13",
        "id": "113",
        "name": "TalComp Industries",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "vendor": {
        "key": "357",
        "id": "1605212096809",
        "name": "Industry Knowledge Consulting LLC",
        "href": "/objects/accounts-payable/vendor/357"
      },
      "item": {
        "key": "13",
        "id": "PTK-0013",
        "name": "Participant Training Kit",
        "href": "/objects/inventory-control/item/13"
      },
      "warehouse": {
        "key": "6",
        "id": "TSDC-006",
        "name": "Training Supplies Distribution Center",
        "href": "/objects/inventory-control/warehouse/6"
      },
      "class": {
        "key": "731",
        "id": "ETO_CLS_001",
        "name": "Enterprise Training Operations",
        "href": "/objects/company-config/class/731"
      },
      "task": {
        "key": "2",
        "id": "CPD-002",
        "name": "Course Preparation and Design",
        "href": "/objects/projects/task/2"
      }
    },
    "audit": {
      "createdDateTime": "2025-01-08T11:28:12Z",
      "modifiedDateTime": "2025-01-08T11:28:12Z",
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
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/rate-table-journal-line
_List rate table journal lines_

**Response 200 — List rate table journal lines:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/construction/rate-table-journal-line/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/construction/rate-table-journal-line/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/construction/rate-table-journal-line/60"
    },
    {
      "key": "78",
      "id": "78",
      "href": "/objects/construction/rate-table-journal-line/78"
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

## GET /objects/construction/rate-table-journal-line/{key}
_Get a rate table journal line_

**Response 200 — Reference to rate table journal line:**
```json
{
  "ia::result": {
    "key": "64",
    "id": "64",
    "rateTable": {
      "key": "145",
      "id": "2025-LV2",
      "name": "2025 Level 2",
      "href": "/objects/construction/rate-table/145"
    },
    "href": "/objects/construction/rate-table-journal-line/64",
    "lineNumber": 1,
    "description": "Overhead Allocation - Markup.",
    "startDate": "2025-08-01",
    "markupPercent": "12.5",
    "accumulationType": {
      "key": "2",
      "id": "ACCT-2",
      "href": "/objects/construction/accumulation-type/2"
    },
    "standardCostType": {
      "key": "33",
      "id": "CT-RT-0010",
      "name": "CT-RT-0010 MATERIAL",
      "href": "/objects/construction/standard-cost-type/33"
    },
    "standardTask": {
      "key": "3",
      "id": "TSK-RT-0011",
      "name": "TSK-RT-0011 Name",
      "href": "/objects/construction/standard-task/3"
    },
    "dimensions": {
      "employee": {
        "key": "10",
        "id": "10",
        "name": "Glenn Thomson",
        "href": "/objects/company-config/employee/10"
      },
      "project": {
        "key": "2",
        "id": "TLC-XML30-2",
        "name": "TalComp Training Initiative",
        "href": "/objects/projects/project/2"
      },
      "customer": {
        "key": "13",
        "id": "113",
        "name": "TalComp Industries",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "vendor": {
        "key": "357",
        "id": "1605212096809",
        "name": "Industry Knowledge Consulting LLC",
        "href": "/objects/accounts-payable/vendor/357"
      },
      "item": {
        "key": "13",
        "id": "PTK-0013",
        "name": "Participant Training Kit",
        "href": "/objects/inventory-control/item/13"
      },
      "warehouse": {
        "key": "6",
        "id": "TSDC-006",
        "name": "Training Supplies Distribution Center",
        "href": "/objects/inventory-control/warehouse/6"
      },
      "class": {
        "key": "731",
        "id": "ETO_CLS_001",
        "name": "Enterprise Training Operations",
        "href": "/objects/company-config/class/731"
      },
      "task": {
        "key": "2",
        "id": "CPD-002",
        "name": "Course Preparation and Design",
        "href": "/objects/projects/task/2"
      }
    },
    "audit": {
      "createdDateTime": "2025-01-08T11:28:12Z",
      "modifiedDateTime": "2025-01-08T11:28:12Z",
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
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/rate-table-purchasing-line
_List rate table purchasing lines_

**Response 200 — List rate table purchasing lines:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/construction/rate-table-purchasing-line/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/construction/rate-table-purchasing-line/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/construction/rate-table-purchasing-line/60"
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

## GET /objects/construction/rate-table-purchasing-line/{key}
_Get a rate table purchasing line_

**Response 200 — Get a rate table purchasing line:**
```json
{
  "ia::result": {
    "key": "176",
    "id": "176",
    "rateTable": {
      "key": "145",
      "id": "2025-LV2",
      "name": "2025 Level 2",
      "href": "/objects/construction/rate-table/145"
    },
    "href": "/objects/construction/rate-table-purchasing-line/176",
    "lineNumber": 1,
    "description": "Purchase Overhead - Markup and Unit Price.",
    "startDate": "2025-08-03",
    "markupPercent": "15.900",
    "unitPrice": "112.560",
    "item": {
      "key": "319",
      "id": "Overhead",
      "name": "Overhead",
      "href": "/objects/inventory-control/item/319"
    },
    "accumulationType": {
      "key": "2",
      "id": "ACCT-2",
      "href": "/objects/construction/accumulation-type/2"
    },
    "standardCostType": {
      "key": "33",
      "id": "CT-RT-0010",
      "name": "CT-RT-0010 MATERIAL",
      "href": "/objects/construction/standard-cost-type/33"
    },
    "standardTask": {
      "key": "3",
      "id": "TSK-RT-0011",
      "name": "TSK-RT-0011 Name",
      "href": "/objects/construction/standard-task/3"
    },
    "dimensions": {
      "employee": {
        "key": "10",
        "id": "10",
        "name": "Glenn Thomson",
        "href": "/objects/company-config/employee/10"
      },
      "project": {
        "key": "2",
        "id": "TLC-XML30-2",
        "name": "TalComp Training Initiative",
        "href": "/objects/projects/project/2"
      },
      "customer": {
        "key": "13",
        "id": "113",
        "name": "TalComp Industries",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "vendor": {
        "key": "357",
        "id": "1605212096809",
        "name": "Industry Knowledge Consulting LLC",
        "href": "/objects/accounts-payable/vendor/357"
      },
      "item": {
        "key": "13",
        "id": "PTK-0013",
        "name": "Participant Training Kit",
        "href": "/objects/inventory-control/item/13"
      },
      "warehouse": {
        "key": "6",
        "id": "TSDC-006",
        "name": "Training Supplies Distribution Center",
        "href": "/objects/inventory-control/warehouse/6"
      },
      "class": {
        "key": "731",
        "id": "ETO_CLS_001",
        "name": "Enterprise Training Operations",
        "href": "/objects/company-config/class/731"
      },
      "task": {
        "key": "2",
        "id": "CPD-002",
        "name": "Course Preparation and Design",
        "href": "/objects/projects/task/2"
      }
    },
    "audit": {
      "createdDateTime": "2025-01-08T11:28:12Z",
      "modifiedDateTime": "2025-01-08T11:28:12Z",
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
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/rate-table-timesheet-line
_List rate table timesheet lines_

**Response 200 — List rate table timesheet lines:**
```json
{
  "ia::result": [
    {
      "key": "84",
      "id": "84",
      "href": "/objects/construction/rate-table-timesheet-line/84"
    },
    {
      "key": "85",
      "id": "85",
      "href": "/objects/construction/rate-table-timesheet-line/85"
    },
    {
      "key": "60",
      "id": "60",
      "href": "/objects/construction/rate-table-timesheet-line/60"
    },
    {
      "key": "78",
      "id": "78",
      "href": "/objects/construction/rate-table-timesheet-line/78"
    },
    {
      "key": "79",
      "id": "79",
      "href": "/objects/construction/rate-table-timesheet-line/79"
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

## GET /objects/construction/rate-table-timesheet-line/{key}
_Get a rate table timesheet line_

**Response 200 — Get a rate table timesheet line:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "12",
    "rateTable": {
      "key": "145",
      "id": "2025-LV2",
      "name": "Labor Time - Overtime Pricing.",
      "href": "/objects/construction/rate-table/145"
    },
    "href": "/objects/construction/rate-table-timesheet-line/12",
    "lineNumber": 1,
    "description": null,
    "startDate": "2025-08-03",
    "markupPercent": "8.250",
    "laborRate": "115.500",
    "accumulationType": {
      "key": "2",
      "id": "ACCT-2",
      "href": "/objects/construction/accumulation-type/2"
    },
    "standardCostType": {
      "key": "33",
      "id": "CT-RT-0010",
      "name": "CT-RT-0010 MATERIAL",
      "href": "/objects/construction/standard-cost-type/33"
    },
    "standardTask": {
      "key": "3",
      "id": "TSK-RT-0011",
      "name": "TSK-RT-0011 Name",
      "href": "/objects/construction/standard-task/3"
    },
    "employeePosition": {
      "key": "2",
      "id": "COO",
      "name": "Chief Executive Officer",
      "href": "/objects/construction/employee-position/2"
    },
    "laborClass": {
      "key": "2",
      "id": "CTS-002",
      "name": "Construction Training Specialist",
      "href": "/objects/construction/labor-class/2"
    },
    "laborShift": {
      "key": "2",
      "id": "LS-002",
      "name": "Day Shift - 10am to 6pm PST",
      "href": "/objects/construction/labor-shift/2"
    },
    "laborUnion": {
      "key": "2",
      "id": "IUOE-002",
      "name": "International Union of Operating Engineers (IUOE)",
      "href": "/objects/construction/labor-union/2"
    },
    "timeType": {
      "key": "1",
      "id": "Non-Billable",
      "href": "/objects/projects/time-type/1"
    },
    "dimensions": {
      "employee": {
        "key": "10",
        "id": "10",
        "name": "Glenn Thomson",
        "href": "/objects/company-config/employee/10"
      },
      "project": {
        "key": "2",
        "id": "TLC-XML30-2",
        "name": "TalComp Training Initiative",
        "href": "/objects/projects/project/2"
      },
      "customer": {
        "key": "13",
        "id": "113",
        "name": "TalComp Industries",
        "href": "/objects/accounts-receivable/customer/13"
      },
      "vendor": {
        "key": "357",
        "id": "1605212096809",
        "name": "Industry Knowledge Consulting LLC",
        "href": "/objects/accounts-payable/vendor/357"
      },
      "item": {
        "key": "13",
        "id": "PTK-0013",
        "name": "Participant Training Kit",
        "href": "/objects/inventory-control/item/13"
      },
      "warehouse": {
        "key": "6",
        "id": "TSDC-006",
        "name": "Training Supplies Distribution Center",
        "href": "/objects/inventory-control/warehouse/6"
      },
      "class": {
        "key": "731",
        "id": "ETO_CLS_001",
        "name": "Enterprise Training Operations",
        "href": "/objects/company-config/class/731"
      },
      "task": {
        "key": "2",
        "id": "CPD-002",
        "name": "Course Preparation and Design",
        "href": "/objects/projects/task/2"
      }
    },
    "audit": {
      "createdDateTime": "2025-01-08T11:28:12Z",
      "modifiedDateTime": "2025-01-18T11:28:12Z",
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
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/rate-table/{key}
_Get a construction rate table_

**Response 200 — Get a construction rate table:**
```json
{
  "ia::result": {
    "key": "145",
    "id": "2025-LV2",
    "name": "2025 Level 2",
    "description": "2025 Level 2 Rate Table",
    "location": {
      "key": "1",
      "id": "1",
      "name": "United States"
    },
    "audit": {
      "createdDateTime": "2025-01-08T11:28:12Z",
      "modifiedDateTime": "2025-01-09T11:28:12Z",
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
    "entity": {
      "id": "1",
      "key": "1",
      "name": "United States of America"
    },
    "timesheetLines": [
      {
        "key": "12",
        "id": "12",
        "rateTable": {
          "key": "145",
          "id": "2025-LV2",
          "name": "2025 Level 2",
          "href": "/objects/construction/rate-table/145"
        },
        "href": "/objects/construction/rate-table-timesheet-line/12",
        "lineNumber": 1,
        "description": "Labor Time - Overtime Pricing.",
        "startDate": "2025-08-03",
        "markupPercent": "8.250",
        "laborRate": "115.500",
        "accumulationType": {
          "key": "2",
          "id": "ACCT-2",
          "href": "/objects/construction/accumulation-type/2"
        },
        "standardCostType": {
          "key": "33",
          "id": "CT-RT-0010",
          "name": "CT-RT-0010 MATERIAL",
          "href": "/objects/construction/standard-cost-type/33"
        },
        "standardTask": {
          "key": "3",
          "id": "TSK-RT-0011",
          "name": "TSK-RT-0011 Name",
          "href": "/objects/construction/standard-task/3"
        },
        "employeePosition": {
          "key": "2",
          "id": "COO",
          "name": "Chief Executive Officer",
          "href": "/objects/construction/employee-position/2"
        },
        "laborClass": {
          "key": "2",
          "id": "LC-2",
          "name": "Labor class 2",
          "href": "/objects/construction/labor-class/2"
        },
        "laborShift": {
          "key": "2",
          "id": "LS-2",
          "name": "Day shift",
          "href": "/objects/construction/labor-shift/2"
        },
        "laborUnion": {
          "key": "2",
          "id": "LU-2",
          "name": "Labor union 2",
          "href": "/objects/construction/labor-union/2"
        },
        "timeType": {
          "key": "1",
          "id": "Salaries At Root",
          "href": "/objects/projects/time-type/1"
        },
        "dimensions": {
          "employee": {
            "key": "10",
            "id": "10",
            "name": "Glenn Thomson",
            "href": "/objects/company-config/employee/10"
          },
          "project": {
            "key": "2",
            "id": "TLC-XML30-2",
            "name": "TalComp Training Initiative",
            "href": "/objects/projects/project/2"
          },
          "customer": {
            "key": "13",
            "id": "113",
            "name": "TalComp Industries",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "Industry Knowledge Consulting LLC",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "item": {
            "key": "13",
            "id": "PTK-0013",
            "name": "Participant Training Kit",
            "href": "/objects/inventory-control/item/13"
          },
          "warehouse": {
            "key": "6",
            "id": "TSDC-006",
            "name": "Training Supplies Distribution Center",
            "href": "/objects/inventory-control/warehouse/6"
          },
          "class": {
            "key": "731",
            "id": "ETO_CLS_001",
            "name": "Enterprise Training Operations",
            "href": "/objects/company-config/class/731"
          },
          "task": {
            "key": "2",
            "id": "CPD-002",
            "name": "Course Preparation and Design",
            "href": "/objects/projects/task/2"
          }
        },
        "audit": {
          "createdDateTime": "2025-01-08T11:28:12Z",
          "modifiedDateTime": "2025-01-08T11:28:12Z",
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
        }
      }
    ],
    "purchasingLines": [
      {
        "key": "176",
        "id": "176",
        "rateTable": {
          "key": "145",
          "id": "2025-LV2",
          "name": "2025 Level 2",
          "href": "/objects/construction/rate-table/145"
        },
        "href": "/objects/construction/rate-table-purchasing-line/176",
        "lineNumber": 1,
        "description": "Purchase Orders - Equipment Markup.",
        "startDate": "2025-08-03",
        "markupPercent": "15.900",
        "unitPrice": "112.560",
        "accumulationType": {
          "key": "2",
          "id": "ACCT-2",
          "href": "/objects/construction/accumulation-type/2"
        },
        "standardCostType": {
          "key": "33",
          "id": "CT-RT-0010",
          "name": "CT-RT-0010 MATERIAL",
          "href": "/objects/construction/standard-cost-type/33"
        },
        "standardTask": {
          "key": "3",
          "id": "TSK-RT-0011",
          "name": "TSK-RT-0011 Name",
          "href": "/objects/construction/standard-task/3"
        },
        "dimensions": {
          "employee": {
            "key": "10",
            "id": "10",
            "name": "Glenn Thomson",
            "href": "/objects/company-config/employee/10"
          },
          "project": {
            "key": "2",
            "id": "TLC-XML30-2",
            "name": "TalComp Training Initiative",
            "href": "/objects/projects/project/2"
          },
          "customer": {
            "key": "13",
            "id": "113",
            "name": "TalComp Industries",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "Industry Knowledge Consulting LLC",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "item": {
            "key": "13",
            "id": "PTK-0013",
            "name": "Participant Training Kit",
            "href": "/objects/inventory-control/item/13"
          },
          "warehouse": {
            "key": "6",
            "id": "TSDC-006",
            "name": "Training Supplies Distribution Center",
            "href": "/objects/inventory-control/warehouse/6"
          },
          "class": {
            "key": "731",
            "id": "ETO_CLS_001",
            "name": "Enterprise Training Operations",
            "href": "/objects/company-config/class/731"
          },
          "task": {
            "key": "2",
            "id": "CPD-002",
            "name": "Course Preparation and Design",
            "href": "/objects/projects/task/2"
          }
        },
        "audit": {
          "createdDateTime": "2025-01-08T11:28:12Z",
          "modifiedDateTime": "2025-01-08T11:28:12Z",
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
        }
      }
    ],
    "accountsPayableLines": [
      {
        "key": "397",
        "id": "397",
        "rateTable": {
          "key": "145",
          "id": "2025-LV2",
          "name": "2025 Level 2",
          "href": "/objects/construction/rate-table/145"
        },
        "href": "/objects/construction/rate-table-credit-card-line/397",
        "lineNumber": 1,
        "description": "Subcontractor costs - Standard Markup.",
        "startDate": "2025-08-01",
        "markupPercent": "25.500",
        "accumulationType": {
          "key": "2",
          "id": "ACCT-2",
          "href": "/objects/construction/accumulation-type/2"
        },
        "standardCostType": {
          "key": "33",
          "id": "CT-RT-0010",
          "name": "CT-RT-0010 MATERIAL",
          "href": "/objects/construction/standard-cost-type/33"
        },
        "standardTask": {
          "key": "3",
          "id": "TSK-RT-0011",
          "name": "TSK-RT-0011 Name",
          "href": "/objects/construction/standard-task/3"
        },
        "dimensions": {
          "employee": {
            "key": "10",
            "id": "10",
            "name": "Glenn Thomson",
            "href": "/objects/company-config/employee/10"
          },
          "project": {
            "key": "2",
            "id": "TLC-XML30-2",
            "name": "TalComp Training Initiative",
            "href": "/objects/projects/project/2"
          },
          "customer": {
            "key": "13",
            "id": "113",
            "name": "TalComp Industries",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "Industry Knowledge Consulting LLC",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "item": {
            "key": "13",
            "id": "PTK-0013",
            "name": "Participant Training Kit",
            "href": "/objects/inventory-control/item/13"
          },
          "warehouse": {
            "key": "6",
            "id": "TSDC-006",
            "name": "Training Supplies Distribution Center",
            "href": "/objects/inventory-control/warehouse/6"
          },
          "class": {
            "key": "731",
            "id": "ETO_CLS_001",
            "name": "Enterprise Training Operations",
            "href": "/objects/company-config/class/731"
          },
          "task": {
            "key": "2",
            "id": "CPD-002",
            "name": "Course Preparation and Design",
            "href": "/objects/projects/task/2"
          }
        },
        "audit": {
          "createdDateTime": "2025-01-08T11:28:12Z",
          "modifiedDateTime": "2025-01-08T11:28:12Z",
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
        }
      }
    ],
    "journalLines": [
      {
        "key": "64",
        "id": "64",
        "rateTable": {
          "key": "145",
          "id": "2025-LV2",
          "name": "2025 Level 2",
          "href": "/objects/construction/rate-table/145"
        },
        "href": "/objects/construction/rate-table-journal-line/64",
        "lineNumber": 1,
        "description": "Overhead Allocation - Project.",
        "startDate": "2025-08-01",
        "markupPercent": "12.500",
        "accumulationType": {
          "key": "2",
          "id": "ACCT-2",
          "href": "/objects/construction/accumulation-type/2"
        },
        "standardCostType": {
          "key": "33",
          "id": "CT-RT-0010",
          "name": "CT-RT-0010 MATERIAL",
          "href": "/objects/construction/standard-cost-type/33"
        },
        "standardTask": {
          "key": "3",
          "id": "TSK-RT-0011",
          "name": "TSK-RT-0011 Name",
          "href": "/objects/construction/standard-task/3"
        },
        "dimensions": {
          "employee": {
            "key": "10",
            "id": "10",
            "name": null,
            "href": "/objects/company-config/employee/10"
          },
          "project": {
            "key": "2",
            "id": "TLC-XML30-2",
            "name": "TalComp Training Initiative",
            "href": "/objects/projects/project/2"
          },
          "customer": {
            "key": "13",
            "id": "113",
            "name": "TalComp Industries",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "Industry Knowledge Consulting LLC",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "item": {
            "key": "13",
            "id": "PTK-0013",
            "name": "Participant Training Kit",
            "href": "/objects/inventory-control/item/13"
          },
          "warehouse": {
            "key": "6",
            "id": "TSDC-006",
            "name": "Training Supplies Distribution Center",
            "href": "/objects/inventory-control/warehouse/6"
          },
          "class": {
            "key": "731",
            "id": "ETO_CLS_001",
            "name": "Enterprise Training Operations",
            "href": "/objects/company-config/class/731"
          },
          "task": {
            "key": "2",
            "id": "CPD-002",
            "name": "Course Preparation and Design",
            "href": "/objects/projects/task/2"
          }
        },
        "audit": {
          "createdDateTime": "2025-01-08T11:28:12Z",
          "modifiedDateTime": "2025-01-08T11:28:12Z",
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
        }
      }
    ],
    "creditCardLines": [
      {
        "key": "145",
        "id": "145",
        "rateTable": {
          "key": "145",
          "id": "2025-LV2",
          "name": "2025 Level 2",
          "href": "/objects/construction/rate-table/145"
        },
        "href": "/objects/construction/rate-table-credit-card-line/145",
        "lineNumber": 1,
        "description": "Corporate Card - Supplies Pricing.",
        "startDate": "2025-08-03",
        "markupPercent": "15.900",
        "accumulationType": {
          "key": "2",
          "id": "ACCT-2",
          "href": "/objects/construction/accumulation-type/2"
        },
        "standardCostType": {
          "key": "33",
          "id": "CT-RT-0010",
          "name": "CT-RT-0010 MATERIAL",
          "href": "/objects/construction/standard-cost-type/33"
        },
        "standardTask": {
          "key": "3",
          "id": "TSK-RT-0011",
          "name": "TSK-RT-0011 Name",
          "href": "/objects/construction/standard-task/3"
        },
        "dimensions": {
          "employee": {
            "key": "10",
            "id": "10",
            "name": "Glenn Thomson",
            "href": "/objects/company-config/employee/10"
          },
          "project": {
            "key": "2",
            "id": "TLC-XML30-2",
            "name": "TalComp Training Initiative",
            "href": "/objects/projects/project/2"
          },
          "customer": {
            "key": "13",
            "id": "113",
            "name": "TalComp Industries",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "Industry Knowledge Consulting LLC",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "item": {
            "key": "13",
            "id": "PTK-0013",
            "name": "Participant Training Kit",
            "href": "/objects/inventory-control/item/13"
          },
          "warehouse": {
            "key": "6",
            "id": "TSDC-006",
            "name": "Training Supplies Distribution Center",
            "href": "/objects/inventory-control/warehouse/6"
          },
          "class": {
            "key": "731",
            "id": "ETO_CLS_001",
            "name": "Enterprise Training Operations",
            "href": "/objects/company-config/class/731"
          },
          "task": {
            "key": "2",
            "id": "CPD-002",
            "name": "Course Preparation and Design",
            "href": "/objects/projects/task/2"
          }
        },
        "audit": {
          "createdDateTime": "2025-01-08T11:28:12Z",
          "modifiedDateTime": "2025-01-08T11:28:12Z",
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
        }
      }
    ],
    "employeeExpenseLines": [
      {
        "key": "30",
        "id": "30",
        "rateTable": {
          "key": "145",
          "id": "2025-LV2",
          "name": "2025 Level 2",
          "href": "/objects/construction/rate-table/145"
        },
        "href": "/objects/construction/rate-table-employee-expense-line/30",
        "lineNumber": 1,
        "description": "Employee Expenses - Training Costs.",
        "startDate": "2025-08-02",
        "markupPercent": "14.800",
        "accumulationType": {
          "key": "2",
          "id": "ACCT-2",
          "href": "/objects/construction/accumulation-type/2"
        },
        "standardCostType": {
          "key": "33",
          "id": "CT-RT-0010",
          "name": "CT-RT-0010 MATERIAL",
          "href": "/objects/construction/standard-cost-type/33"
        },
        "standardTask": {
          "key": "3",
          "id": "TSK-RT-0011",
          "name": "TSK-RT-0011 Name",
          "href": "/objects/construction/standard-task/3"
        },
        "dimensions": {
          "employee": {
            "key": "10",
            "id": "10",
            "name": "Glenn Thomson",
            "href": "/objects/company-config/employee/10"
          },
          "project": {
            "key": "2",
            "id": "TLC-XML30-2",
            "name": "TalComp Training Initiative",
            "href": "/objects/projects/project/2"
          },
          "customer": {
            "key": "13",
            "id": "113",
            "name": "TalComp Industries",
            "href": "/objects/accounts-receivable/customer/13"
          },
          "vendor": {
            "key": "357",
            "id": "1605212096809",
            "name": "Industry Knowledge Consulting LLC",
            "href": "/objects/accounts-payable/vendor/357"
          },
          "item": {
            "key": "13",
            "id": "PTK-0013",
            "name": "Participant Training Kit",
            "href": "/objects/inventory-control/item/13"
          },
          "warehouse": {
            "key": "6",
            "id": "TSDC-006",
            "name": "Training Supplies Distribution Center",
            "href": "/objects/inventory-control/warehouse/6"
          },
          "class": {
            "key": "731",
            "id": "ETO_CLS_001",
            "name": "Enterprise Training Operations",
            "href": "/objects/company-config/class/731"
          },
          "task": {
            "key": "2",
            "id": "CPD-002",
            "name": "Course Preparation and Design",
            "href": "/objects/projects/task/2"
          }
        },
        "audit": {
          "createdDateTime": "2025-01-08T11:28:12Z",
          "modifiedDateTime": "2025-01-08T11:28:12Z",
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
        }
      }
    ]
  },
  "ia::meta": {
    "totalCount": 1
  }
}
```

## PATCH /objects/construction/rate-table/{key}
_Update a construction rate table_

**Request example — Update construction rate table:**
```json
{
  "description": "2025 Level 2 Rate Table (August Update).",
  "timesheetLines": [
    {
      "key": "12",
      "lineNumber": 2,
      "description": "Labor Time - Overtime Pricing (August Update)."
    }
  ]
}
```
**Response 200 — Reference to construction rate table:**
```json
{
  "ia::result": {
    "key": "12",
    "id": "2025-LV2",
    "href": "/objects/construction/rate-table/12"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/rate-table/{key}
_Delete a construction rate table_


## GET /objects/construction/work-order
_List work orders_

**Response 200 — List work orders:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/work-order/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/work-order/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/work-order/3"
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

## POST /objects/construction/work-order
_Create a work order_

**Request example — Create a new work order:**
```json
{
  "id": "WO-0024",
  "name": "Root - No Location",
  "description": "25 R4"
}
```
**Response 201 — Reference to new work order:**
```json
{
  "ia::result": {
    "key": "22",
    "id": "WO-0024",
    "href": "/objects/construction/work-order/22"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/work-order-call-type
_List work order call types_

**Response 200 — List work order call types:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/work-order-call-type/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/work-order-call-type/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/work-order-call-type/3"
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

## POST /objects/construction/work-order-call-type
_Create a work order call type_

**Request example — Create a work order call type:**
```json
{
  "id": "Emergency Call-In"
}
```
**Response 201 — Reference to new work order call type:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "Emergency Call-In",
    "href": "/objects/construction/work-order-call-type/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/work-order-call-type/{key}
_Get a work order call type_

**Response 200 — Details of the work order call type:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "Emergency Call-In",
    "status": "active",
    "parent": {
      "key": "4",
      "id": "Inspection Follow-Up",
      "href": "/objects/construction/work-order-call-type/4"
    },
    "audit": {
      "createdDateTime": "2025-09-23T14:27:24Z",
      "modifiedDateTime": "2025-09-23T14:27:24Z",
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
      "id": "1",
      "key": "1",
      "name": "United States of America",
      "href": "/objects/company-config/entity/1"
    },
    "href": "/objects/construction/work-order-call-type/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/work-order-call-type/{key}
_Update a work order call type_

**Request example — Update a work order call type:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated work order call type:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "Emergency Call-In",
    "href": "/objects/construction/work-order-call-type/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/work-order-call-type/{key}
_Delete a work order call type_


## GET /objects/construction/work-order-problem-code
_List work order problem codes_

**Response 200 — List work order problem codes:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/work-order-problem-code/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/work-order-problem-code/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/work-order-problem-code/3"
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

## POST /objects/construction/work-order-problem-code
_Create a work order problem code_

**Request example — Creates a work order problem code:**
```json
{
  "id": "Control Failure"
}
```
**Response 201 — Reference to new work order problem code:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Control Failure",
    "href": "/objects/construction/work-order-problem-code/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/work-order-problem-code/{key}
_Get a work order problem code_

**Response 200 — Details of the work order problem code:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "Water Leak",
    "parent": {
      "key": "7",
      "id": "Routine Tune-Up",
      "href": "/objects/construction/work-order-problem-code/7"
    },
    "status": "active",
    "audit": {
      "createdDateTime": "2025-09-25T08:06:25Z",
      "modifiedDateTime": "2025-09-25T08:06:25Z",
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
      "id": "1",
      "key": "1",
      "name": "United States of America",
      "href": "/objects/company-config/entity/1"
    },
    "href": "/objects/construction/work-order-problem-code/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/work-order-problem-code/{key}
_Update a work order problem code_

**Request example — Update a work order problem code:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated work order problem code:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Control Failure",
    "href": "/objects/construction/work-order-problem-code/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/work-order-problem-code/{key}
_Delete a work order problem code_


## GET /objects/construction/work-order-state
_List work order states_

**Response 200 — List work order states:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/work-order-state/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/work-order-state/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/work-order-state/3"
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

## POST /objects/construction/work-order-state
_Create a work order state_

**Request example — Create a work order state:**
```json
{
  "id": "Active"
}
```
**Response 201 — Reference to new work order state:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Active",
    "href": "/objects/construction/work-order-state/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/work-order-state/{key}
_Get a work order state_

**Response 200 — Details of the work order state:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "Active",
    "status": "active",
    "parent": {
      "key": "4",
      "id": "Emergency Repair",
      "href": "/objects/construction/work-order-state/4"
    },
    "audit": {
      "createdDateTime": "2025-09-25T12:25:46Z",
      "modifiedDateTime": "2025-09-25T12:25:46Z",
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
      "id": "1",
      "key": "1",
      "name": "United States of America",
      "href": "/objects/company-config/entity/1"
    },
    "href": "/objects/construction/work-order-state/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/work-order-state/{key}
_Update a work order state_

**Request example — Update a work order state:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated work order state:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Active",
    "href": "/objects/construction/work-order-state/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/work-order-state/{key}
_Delete a work order state_


## GET /objects/construction/work-order-type
_List work order types_

**Response 200 — List work order types:**
```json
{
  "ia::result": [
    {
      "key": "1",
      "id": "1",
      "href": "/objects/construction/work-order-type/1"
    },
    {
      "key": "2",
      "id": "2",
      "href": "/objects/construction/work-order-type/2"
    },
    {
      "key": "3",
      "id": "3",
      "href": "/objects/construction/work-order-type/3"
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

## POST /objects/construction/work-order-type
_Create a work order type_

**Request example — Creates a work order type:**
```json
{
  "id": "Service Call"
}
```
**Response 201 — Reference to new work order type:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Service Call",
    "href": "/objects/construction/work-order-type/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## GET /objects/construction/work-order-type/{key}
_Get a work order type_

**Response 200 — Details of the work order type:**
```json
{
  "ia::result": {
    "key": "11",
    "id": "Preventive Maintenance",
    "status": "active",
    "parent": {
      "id": "2",
      "key": "Project Work",
      "href": "/objects/construction/work-order-type/2"
    },
    "audit": {
      "createdDateTime": "2025-09-25T12:16:41Z",
      "modifiedDateTime": "2025-09-25T12:16:41Z",
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
      "id": "1",
      "key": "1",
      "name": "United States of America",
      "href": "/objects/company-config/entity/1"
    },
    "href": "/objects/construction/work-order-type/11"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/work-order-type/{key}
_Update a work order type_

**Request example — Updates a work order type:**
```json
{
  "status": "inactive"
}
```
**Response 200 — Reference to updated work order type:**
```json
{
  "ia::result": {
    "key": "10",
    "id": "Service Call",
    "href": "/objects/construction/work-order-type/10"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/work-order-type/{key}
_Delete a work order type_


## GET /objects/construction/work-order/{key}
_Get a work order_

**Response 200 — Details of the work order:**
```json
{
  "ia::result": {
    "key": "18",
    "id": "WO-0017",
    "name": "WO-India",
    "description": "WO India Entity",
    "workOrderType": {
      "id": "4",
      "key": "4",
      "href": "/objects/construction/work-order-type/4"
    },
    "workOrderCallType": {
      "id": "7",
      "key": "7",
      "href": "/objects/construction/work-order-call-type/7"
    },
    "workOrderProblemCode": {
      "id": "1",
      "key": "1",
      "href": "/objects/construction/work-order-problem-code/1"
    },
    "workOrderState": {
      "id": "1",
      "key": "1",
      "href": "/objects/construction/work-order-state/1"
    },
    "customer": {
      "key": "14",
      "id": "BTI",
      "name": "Berkeley Technology Inc",
      "href": "/objects/accounts-receivable/customer/14"
    },
    "employee": {
      "key": "10",
      "id": "EMP-10",
      "name": "Thomas Glenn",
      "href": "/objects/company-config/employee/10"
    },
    "workOrderDate": "2025-01-01",
    "closedDate": "2025-03-01",
    "isComplete": false,
    "status": "active",
    "project": {
      "key": "1",
      "id": "DIM - BTI",
      "name": "Dimensions - Berkeley Technology Inc",
      "href": "/objects/projects/project/1"
    },
    "location": {
      "key": "1",
      "id": "1",
      "name": "United States of America",
      "href": "/objects/company-config/location/1"
    },
    "department": {
      "key": "7",
      "id": "CS",
      "name": "Client Services",
      "href": "/objects/company-config/department/7"
    },
    "salesperson": {
      "key": "256",
      "id": "10000",
      "name": "xktxa",
      "href": "/objects/company-config/employee/256"
    },
    "class": {
      "key": "1",
      "id": "10",
      "name": "Construction",
      "href": "/objects/company-config/class/1"
    },
    "externalDetails": {
      "workOrderNumber": "W0-5678",
      "workOrderNumber1": "A-WO-001",
      "workOrderNumber2": "B-WO-002",
      "serviceSite": "Site A",
      "agreementNumber": "AG-1234",
      "agreementSequence": "WO-1",
      "isAutoGenerated": false,
      "customerPurchaseOrder": "null",
      "isBillable": true,
      "estimatedHours": "300.00",
      "actualHours": "250.00",
      "estimatedCost": "500000.00",
      "actualCost": "400000.00",
      "notToExceedCost": "500000.00",
      "workOrderAmount": "499999.00",
      "billedAmount": "499999.00"
    },
    "recordURL": "null",
    "audit": {
      "createdDateTime": "2025-08-12T09:52:20Z",
      "modifiedDateTime": "2025-08-12T09:52:20Z",
      "createdByUser": {
        "key": "1",
        "id": "Admin",
        "href": "/objects/company-config/user/1"
      },
      "createdBy": "1",
      "modifiedByUser": {
        "key": "111",
        "id": "Admin",
        "href": "/objects/company-config/user/111"
      },
      "modifiedBy": "111"
    },
    "entity": {
      "key": "2",
      "id": "2",
      "name": "India",
      "href": "/objects/company-config/entity/2"
    },
    "href": "/objects/construction/work-order/18"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## PATCH /objects/construction/work-order/{key}
_Update a work order_

**Request example — Update a work order:**
```json
{
  "workOrderDate": "2025-08-24",
  "description": "25 R4"
}
```
**Response 200 — Reference to updated work order:**
```json
{
  "ia::result": {
    "key": "4",
    "id": "WO-1004",
    "href": "/objects/construction/work-order/4"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## DELETE /objects/construction/work-order/{key}
_Delete a work order_


## GET /services/construction-forecasting/wip-journal/entry-history
_List a WIP posting history_

**Response 200 — Posting history:**
```json
{
  "ia::result": {
    "entryHistory": [
      {
        "journalEntry": {
          "txnNumber": 48,
          "id": "97",
          "postingDate": "2023-08-01",
          "key": "97",
          "href": "/objects/general-ledger/journal-entry/97"
        },
        "journal": {
          "id": "APJ",
          "key": "5",
          "href": "/objects/general-ledger/journal/5"
        },
        "overbilling": {
          "debitAmount": "0",
          "creditAmount": "100.30"
        },
        "underbilling": {
          "debitAmount": "641.84",
          "creditAmount": "0"
        },
        "adjustment": {
          "debitAmount": "100.30",
          "creditAmount": "641.84"
        },
        "description": "Reversed - Reverting post: WIP end of month posting for Month Ended July 2023"
      },
      {
        "journalEntry": {
          "txnNumber": 47,
          "id": "96",
          "postingDate": "2023-07-31",
          "key": "96",
          "href": "/objects/general-ledger/journal-entry/96"
        },
        "reversedByJournalEntry": {
          "txnNumber": 48,
          "id": "97",
          "postingDate": "2023-08-01",
          "key": "97",
          "href": "/objects/general-ledger/journal-entry/97"
        },
        "journal": {
          "id": "APJ",
          "key": "5",
          "href": "/objects/general-ledger/journal/5"
        },
        "revertedByJournalEntry": {
          "txnNumber": 43,
          "id": "92",
          "postingDate": "2023-07-31",
          "key": "92",
          "href": "/objects/general-ledger/journal-entry/92"
        },
        "overbilling": {
          "debitAmount": "100.30",
          "creditAmount": "0"
        },
        "underbilling": {
          "debitAmount": "0",
          "creditAmount": "641.84"
        },
        "adjustment": {
          "debitAmount": "641.84",
          "creditAmount": "100.30"
        },
        "description": "Reverting post: WIP end of month posting for Month Ended July 2023"
      },
      {
        "journalEntry": {
          "txnNumber": 44,
          "id": "93",
          "postingDate": "2023-08-01",
          "key": "93",
          "href": "/objects/general-ledger/journal-entry/93"
        },
        "journal": {
          "id": "APJ",
          "key": "5",
          "href": "/objects/general-ledger/journal/5"
        },
        "overbilling": {
          "debitAmount": "0",
          "creditAmount": "100.30"
        },
        "underbilling": {
          "debitAmount": "641.84",
          "creditAmount": "0"
        },
        "adjustment": {
          "debitAmount": "100.30",
          "creditAmount": "641.84"
        },
        "description": "Reversed - WIP end of month posting for Month Ended July 2023"
      },
      {
        "journalEntry": {
          "txnNumber": 43,
          "id": "92",
          "postingDate": "2023-07-31",
          "key": "92",
          "href": "/objects/general-ledger/journal-entry/92"
        },
        "reversedByJournalEntry": {
          "txnNumber": 44,
          "id": "93",
          "postingDate": "2023-08-01",
          "key": "93",
          "href": "/objects/general-ledger/journal-entry/93"
        },
        "journal": {
          "id": "APJ",
          "key": "5",
          "href": "/objects/general-ledger/journal/5"
        },
        "overbilling": {
          "debitAmount": "100.30",
          "creditAmount": "0"
        },
        "underbilling": {
          "debitAmount": "0",
          "creditAmount": "641.84"
        },
        "adjustment": {
          "debitAmount": "641.84",
          "creditAmount": "100.30"
        },
        "description": "WIP end of month posting for Month Ended July 2023"
      }
    ]
  },
  "ia::meta": {
    "totalCount": 4,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/construction-forecasting/wip-journal/generate-preview
_Preview a WIP posting_

**Request example — Generate a preview for a WIP posting:**
```json
{
  "wipPeriodKey": "5",
  "wipProjects": [
    {
      "project": {
        "key": "1"
      },
      "customer": {
        "key": "14"
      },
      "key": "5",
      "cfoForecast": {
        "percentComplete": 70,
        "costToComplete": "4000.00",
        "contractValue": "10000.00",
        "costAtCompletion": "9500.00"
      },
      "projectManagerForecast": {
        "percentComplete": 90,
        "costAtCompletion": "9000.00",
        "costToComplete": "3000.00",
        "contractValue": "10000.00"
      },
      "cfoForecastGrossProfitAtCompletion": "26110.00",
      "grossProfitPercentOfContract": 0.99,
      "estimatedCostToComplete": "-5203.07",
      "overUnderBillingAmount": "76578540.49",
      "isFinalized": false,
      "grossProfitVarianceAmount": "0.00",
      "earnedProfitToDateAmount": "76578010.58",
      "remainingProfit": "0",
      "endOfPriorYearEarnedToDateAmount": "0",
      "endOfPriorYearEarnedProfit": "0",
      "estimatedPercentComplete": 29.12,
      "grossProfitPercentOfCost": 141.14,
      "remainingBacklogAmount": "-76557103.65",
      "contractVarianceAmount": "0",
      "cfoForecastGrossProfitMarginPercent": 0.99,
      "totalGrossProfitEstimatedAtCompletion": "26110.00",
      "jobToDateBillings": "4858.16",
      "jobToDateCosts": "5388.07",
      "estimatedCostToDateAmount": "185.00",
      "earnedToDateAmount": "76583398.65",
      "totalRevisedContract": "26295.00",
      "yearToDateCostAmount": "15000",
      "yearToDateBillingAmount": "15000",
      "yearToDateEarnedRevenueAmount": "15000",
      "jobToDateOverbillingAmount": "15000",
      "jobToDateUnderbillingAmount": "15000",
      "yearToDateEarnedProfitAmount": "15000",
      "currentPeriodBillingAmount": "15000",
      "currentPeriodCostAmount": "15000",
      "currentPeriodEarnedProfitAmount": "15000",
      "currentPeriodEarnedRevenueAmount": "15000"
    }
  ],
  "automaticReversalDate": "2023-10-01",
  "postingDate": "2023-09-30",
  "referenceNumber": "WipJournal_202309",
  "description": "Journal Entry for WIP Period ending 2023-09-30"
}
```
**Response 200 — Generated journal entry preview:**
```json
{
  "ia::result": {
    "cumulativeBillingsInExcessOfCostsCreditAmount": "10023.33",
    "cumulativeCostsInExcessOfBillingsDebitAmount": "2309.44",
    "description": "Journal Entry Sep 2023",
    "postingDate": "2023-09-30",
    "automaticReversalDate": "2023-10-01",
    "state": "posted",
    "referenceNumber": "WIP_202309",
    "glJournal": {
      "name": "WIP Journal",
      "id": "WIP",
      "key": 3
    },
    "overbillingAccount": {
      "name": "Billings in Excess of Cost",
      "id": 10030,
      "key": 58
    },
    "underbillingAccount": {
      "name": "Cost in Excess of Billings",
      "id": 10040,
      "key": 60
    },
    "underbillingOffsetAccount": {
      "name": "Net Over or Under Billings",
      "id": 10050,
      "key": 62
    },
    "overbillingOffsetAccount": {
      "name": "Net Over or Under Billings",
      "id": 10050,
      "key": 62
    },
    "lines": [
      {
        "department": {
          "name": "Client Services",
          "id": "CS",
          "key": "10"
        },
        "location": {
          "name": "United States",
          "id": "1",
          "key": "1"
        },
        "project": {
          "name": "sample",
          "id": "DIM - BTI",
          "key": "7"
        },
        "class": {
          "name": "PlanningPhase",
          "id": "4",
          "key": "13"
        },
        "transactionType": "Credit",
        "transactionAmount": "100.33",
        "glAccount": {
          "name": "chase",
          "id": "1003",
          "key": "6"
        }
      },
      {
        "department": {
          "name": "Client Services",
          "id": "CS",
          "key": "10"
        },
        "location": {
          "name": "United States",
          "id": "1",
          "key": "1"
        },
        "project": {
          "name": "sample",
          "id": "DIM - BTI",
          "key": "7"
        },
        "class": {
          "name": "PlanningPhase",
          "id": "4",
          "key": "13"
        },
        "transactionType": "Debit",
        "transactionAmount": "100.33",
        "glAccount": {
          "name": "chase",
          "id": "1003",
          "key": "6"
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

## POST /services/construction-forecasting/wip-journal/post-period
_Post a WIP period_

**Request example — Post a WIP period:**
```json
{
  "wipPeriodKey": "11",
  "wipProjects": [
    {
      "project": {
        "key": "1"
      },
      "customer": {
        "key": "14"
      },
      "key": "5",
      "cfoForecast": {
        "percentComplete": 70,
        "costToComplete": "4000.00",
        "contractValue": "10000.00",
        "costAtCompletion": "9500.00"
      },
      "projectManagerForecast": {
        "percentComplete": 90,
        "costAtCompletion": "9000.00",
        "costToComplete": "3000.00",
        "contractValue": "10000.00"
      },
      "cfoForecastGrossProfitAtCompletion": "26110.00",
      "grossProfitPercentOfContract": 0.99,
      "estimatedCostToComplete": "-5203.07",
      "overUnderBillingAmount": "76578540.49",
      "isFinalized": false,
      "grossProfitVarianceAmount": "0.00",
      "earnedProfitToDateAmount": "76578010.58",
      "remainingProfit": "0",
      "endOfPriorYearEarnedToDateAmount": "0",
      "endOfPriorYearEarnedProfit": "0",
      "estimatedPercentComplete": 29.12,
      "grossProfitPercentOfCost": 141.14,
      "remainingBacklogAmount": "-76557103.65",
      "contractVarianceAmount": "0",
      "cfoForecastGrossProfitMarginPercent": 0.99,
      "totalGrossProfitEstimatedAtCompletion": "26110.00",
      "jobToDateBillings": "4858.16",
      "jobToDateCosts": "5388.07",
      "estimatedCostToDateAmount": "185.00",
      "earnedToDateAmount": "76583398.65",
      "totalRevisedContract": "26295.00",
      "yearToDateCostAmount": "15000",
      "yearToDateBillingAmount": "15000",
      "yearToDateEarnedRevenueAmount": "15000",
      "jobToDateOverbillingAmount": "15000",
      "jobToDateUnderbillingAmount": "15000",
      "yearToDateEarnedProfitAmount": "15000",
      "currentPeriodBillingAmount": "15000",
      "currentPeriodCostAmount": "15000",
      "currentPeriodEarnedProfitAmount": "15000",
      "currentPeriodEarnedRevenueAmount": "15000"
    }
  ],
  "automaticReversalDate": "2023-10-01",
  "postingDate": "2023-09-30",
  "referenceNumber": "WipJournal_202309",
  "description": "Journal Entry for WIP Period ending 2023-09-30"
}
```

## POST /services/construction-forecasting/wip-journal/revert-post
_Revert a WIP journal posting_

**Request example — Revert posting for a WIP report:**
```json
{
  "wipPeriodKey": "11"
}
```

## POST /services/construction-forecasting/wip-period/can-post
_Preview a WIP period_

**Request example — Preview WIP period:**
```json
{
  "wipPeriodKey": "5"
}
```
**Response 200 — WIP period preview response:**
```json
{
  "ia::result": {
    "canPost": false,
    "error": "The WIP period cannot be posted"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/construction-forecasting/wip-period/generate
_Generate WIP projects_

**Request example — Generate WIP projects:**
```json
{
  "periodEndDate": "2023-01-01"
}
```
**Response 200 — List of generated WIP projects for a specified WIP schedule period:**
```json
{
  "ia::result": {
    "wipProjects": [
      {
        "project": {
          "name": "Dimensions - Berkeley Technology Inc",
          "id": "DIM - BTI",
          "key": "1"
        },
        "customer": {
          "name": "Berkeley Technology Inc",
          "id": "BTI",
          "key": "14"
        },
        "projectStatus": {
          "id": "In Progress"
        },
        "projectType": {
          "id": "Tenant Improvement"
        },
        "manager": {
          "name": "Sanford; Dennis G",
          "id": "EMP00002"
        },
        "class": {
          "name": "Project Class",
          "id": "Project Class"
        },
        "location": {
          "name": "Beaverton",
          "id": "BEAVERTON"
        },
        "department": {
          "name": "Construction Operations",
          "id": "OPERATIONS"
        },
        "cfoForecast": {
          "percentComplete": 70,
          "costToComplete": "4000.00",
          "contractValue": "10000.00",
          "costAtCompletion": "9500.00",
          "lastUpdatedDate": "2023-05-26T10:06:00Z"
        },
        "projectManagerForecast": {
          "percentComplete": 90,
          "costAtCompletion": "9000.00",
          "costToComplete": "3000.00",
          "contractValue": "10000.00",
          "lastUpdatedDate": "2023-05-26T10:06:00Z"
        },
        "cfoForecastGrossProfitAtCompletion": "26110.00",
        "grossProfitPercentOfContract": 0.99,
        "estimatedCostToComplete": "-5203.07",
        "overUnderBillingAmount": "76578540.49",
        "isFinalized": false,
        "grossProfitVarianceAmount": "0.00",
        "earnedProfitToDateAmount": "76578010.58",
        "remainingProfit": "0",
        "endOfPriorYearEarnedToDateAmount": "0",
        "endOfPriorYearEarnedProfit": "0",
        "estimatedPercentComplete": 29.12,
        "grossProfitPercentOfCost": 141.14,
        "remainingBacklogAmount": "-76557103.65",
        "contractVarianceAmount": "0",
        "cfoForecastGrossProfitMarginPercent": 0.99,
        "totalGrossProfitEstimatedAtCompletion": "26110.00",
        "jobToDateBillings": "4858.16",
        "jobToDateCosts": "5388.07",
        "estimatedCostToDateAmount": "185.00",
        "earnedToDateAmount": "76583398.65",
        "totalRevisedContract": "26295.00",
        "yearToDateCostAmount": "15000",
        "yearToDateBillingAmount": "15000",
        "yearToDateEarnedRevenueAmount": "15000",
        "jobToDateOverbillingAmount": "15000",
        "jobToDateUnderbillingAmount": "15000",
        "yearToDateEarnedProfitAmount": "15000",
        "currentPeriodBillingAmount": "15000",
        "currentPeriodCostAmount": "15000",
        "currentPeriodEarnedProfitAmount": "15000",
        "currentPeriodEarnedRevenueAmount": "15000"
      }
    ],
    "lastRefreshDateTime": "2023-06-02T14:47:14Z",
    "wipCostBreakdownLevel": "costCodeAndCostType"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/construction-forecasting/wip-period/get-warnings
_Get warnings_

**Request example — Get warnings for a WIP period:**
```json
{
  "periodName": "Month Ended May 2023",
  "periodEndDate": "2023-05-31",
  "notes": "Review with CFO",
  "state": "unposted",
  "lastRefreshDateTime": "2023-06-02T20:29:13Z",
  "wipCostBreakdownLevel": "wipScheduleProject",
  "wipProjects": [
    {
      "cfoForecastGrossProfitMarginPercent": 0.99,
      "cfoForecast": {
        "percentComplete": 70,
        "costToComplete": "4000.00",
        "contractValue": "10000.00",
        "costAtCompletion": "9500.00",
        "lastUpdatedDate": "2023-05-26T10:06:00Z"
      },
      "cfoForecastGrossProfitAtCompletion": "26110.00",
      "estimatedCostToComplete": "-5203.07",
      "overUnderBillingAmount": "76578540.49",
      "isFinalized": false,
      "projectManagerForecast": {
        "percentComplete": 90,
        "costAtCompletion": "9000.00",
        "costToComplete": "3000.00",
        "contractValue": "10000.00",
        "lastUpdatedDate": "2023-05-26T10:06:00Z"
      },
      "projectedProfitFutureYears": "0",
      "remainingBacklogAmount": "-76557103.65",
      "contractVarianceAmount": "0",
      "estimatedPercentComplete": 29.12,
      "totalGrossProfitEstimatedAtCompletion": "26110.00",
      "grossProfitVarianceAmount": "0.00",
      "jobToDateBillings": "4858.16",
      "jobToDateCosts": "5388.07",
      "estimatedCostToDateAmount": "185.00",
      "earnedProfitToDateAmount": "76578010.58",
      "earnedToDateAmount": "76583398.65",
      "grossProfitPercentOfContract": 0.99,
      "grossProfitPercentOfCost": 141.14,
      "totalRevisedContract": "26295.00",
      "project": {
        "key": "1"
      }
    }
  ]
}
```
**Response 200 — List WIP projects and warnings:**
```json
{
  "ia::result": {
    "wipProjects": [
      {
        "wipPeriod": {
          "isHistoricalImport": false,
          "state": "unposted",
          "key": "40"
        },
        "project": {
          "name": "Dimensions - Berkeley Technology Inc",
          "id": "DIM - BTI",
          "key": "1"
        },
        "customer": {
          "name": "Berkeley Technology Inc",
          "id": "BTI",
          "key": "14"
        },
        "projectStatus": {
          "id": "In Progress"
        },
        "projectType": {
          "id": "Tenant Improvement"
        },
        "manager": {
          "name": "Sanford; Dennis G",
          "id": "EMP00002"
        },
        "class": {
          "name": "Project Class",
          "id": "Project Class"
        },
        "location": {
          "name": "Beaverton",
          "id": "BEAVERTON"
        },
        "department": {
          "name": "Construction Operations",
          "id": "OPERATIONS"
        },
        "cfoForecast": {
          "percentComplete": 70,
          "costToComplete": "4000.00",
          "contractValue": "10000.00",
          "costAtCompletion": "9500.00",
          "lastUpdatedDate": "2023-05-26T10:06:00Z"
        },
        "projectManagerForecast": {
          "percentComplete": 90,
          "costAtCompletion": "9000.00",
          "costToComplete": "3000.00",
          "contractValue": "10000.00",
          "lastUpdatedDate": "2023-05-26T10:06:00Z"
        },
        "notes": "not ready",
        "cfoForecastGrossProfitAtCompletion": "26110",
        "grossProfitPercentOfContract": 0.99,
        "estimatedCostToComplete": "-5203.07",
        "overUnderBillingAmount": "76578540.49",
        "isFinalized": false,
        "grossProfitVarianceAmount": "0",
        "earnedProfitToDateAmount": "76578010.58",
        "projectedProfitFutureYears": "0",
        "estimatedPercentComplete": 29.12,
        "grossProfitPercentOfCost": 141.14,
        "remainingBacklogAmount": "-76557103.65",
        "id": "55",
        "contractVarianceAmount": "0",
        "key": "55",
        "cfoForecastGrossProfitMarginPercent": 0.99,
        "totalGrossProfitEstimatedAtCompletion": "26110",
        "jobToDateBillings": "4858.16",
        "jobToDateCosts": "5388.07",
        "estimatedCostToDateAmount": "185.00",
        "earnedToDateAmount": "76583398.65",
        "totalRevisedContract": "26295.00"
      }
    ],
    "warnings": {
      "warnings": [
        {
          "critical": false,
          "errorMessage": "Estimated percent complete must be between 0 and 100",
          "fieldNames": [
            "estimatedPercentComplete"
          ],
          "target": "1",
          "source": "wip-project"
        }
      ]
    },
    "wipProjectWarnings": {
      "warnings": [
        {
          "critical": false,
          "errorMessage": "Estimated percent complete must be between 0 and 100",
          "fieldNames": [
            "estimatedPercentComplete"
          ],
          "target": "1",
          "source": "wip-project"
        }
      ]
    },
    "wipForecastDetailWarnings": [
      {
        "key": 14415,
        "errorMessage": "Enter a positive amount in the field 'PM forecast cost to complete'. The field 'PM forecast cost to complete' cannot be negative.",
        "fieldNames": [
          "projectManagerForecastCostToComplete"
        ],
        "severity": "warning",
        "source": "objects/construction-forecasting/wip-forecast-detail",
        "target": "14415"
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

## POST /services/construction-forecasting/wip-period/prior-periods
_Prior WIP periods_

**Request example — WIP periods before specified date:**
```json
{
  "priorToPeriodEndDate": "2023-05-31",
  "priorPeriodCount": 1
}
```
**Response 200 — List prior WIP periods:**
```json
{
  "ia::result": {
    "wipPeriods": [
      {
        "wipProjects": [
          {
            "wipPeriod": {
              "periodName": "Month Ended July 2023",
              "id": "72",
              "key": "72"
            },
            "project": {
              "endDate": "2020-12-31",
              "name": "Dimensions - Berkeley Technology Inc",
              "description": "Project with all resources - At root - Time & Material - With Dept & Location",
              "id": "DIM - BTI",
              "key": "1",
              "startDate": "2000-01-01",
              "status": "active"
            },
            "audit": {
              "createdBy": "1",
              "createdDateTime": "2023-08-08T17:51:06Z",
              "modifiedBy": "1",
              "modifiedDateTime": "2023-08-21T22:40:37Z",
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
            "projectManagerForecast": {
              "costAtCompletion": "53880.7",
              "costToComplete": "48492.63",
              "contractValue": "50000",
              "percentComplete": 10,
              "lastUpdatedDate": "2023-05-26T10:06:00Z"
            },
            "cfoForecast": {
              "costAtCompletion": "53880.7",
              "costToComplete": "48492.63",
              "contractValue": "50000",
              "percentComplete": 10,
              "lastUpdatedDate": "2023-05-26T10:06:00Z"
            },
            "customer": {
              "name": "Berkeley Technology Inc",
              "id": "BTI",
              "key": "14"
            },
            "notes": "Updated based on timeline adjustment",
            "cfoForecastGrossProfitAtCompletion": "-3880.7",
            "costAtCompletionVariance": "0",
            "grossProfitPercentOfContract": -7.76,
            "estimatedCostToComplete": "-5203.07'",
            "overUnderBillingAmount": "141.84",
            "isFinalized": true,
            "grossProfitVarianceAmount": "-29990.7'",
            "earnedProfitToDateAmount": "-388.07",
            "remainingProfit": "0",
            "endOfPriorYearEarnedToDateAmount": "0",
            "endOfPriorYearEarnedProfit": "0",
            "estimatedPercentComplete": 29.12,
            "grossProfitPercentOfCost": -7.2,
            "remainingBacklogAmount": "45000",
            "id": "87",
            "contractVarianceAmount": "23705",
            "key": "87",
            "cfoForecastGrossProfitMarginPercent": -7.76,
            "totalGrossProfitEstimatedAtCompletion": "26110",
            "jobToDateBillings": "4858.16",
            "jobToDateCosts": "5388.07",
            "estimatedCostToDateAmount": "185",
            "earnedToDateAmount": "5000",
            "totalRevisedContract": "26295",
            "yearToDateCostAmount": "15000",
            "yearToDateBillingAmount": "15000",
            "yearToDateEarnedRevenueAmount": "15000",
            "jobToDateOverbillingAmount": "15000",
            "jobToDateUnderbillingAmount": "15000",
            "yearToDateEarnedProfitAmount": "15000",
            "currentPeriodBillingAmount": "15000",
            "currentPeriodCostAmount": "15000",
            "currentPeriodEarnedProfitAmount": "15000",
            "currentPeriodEarnedRevenueAmount": "15000"
          }
        ],
        "audit": {
          "createdBy": "1",
          "createdDateTime": "2023-08-08T17:51:06Z",
          "modifiedBy": "1",
          "modifiedDateTime": "2023-08-21T22:40:37Z",
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
        "historicalImport": false,
        "lastRefreshDateTime": "2023-08-09T14:49:21Z",
        "periodName": "Month Ended July 2023",
        "id": "72",
        "state": "unposted",
        "key": "72",
        "periodEndDate": "2023-07-31"
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

## POST /services/construction-forecasting/wip-period/refresh
_Refresh WIP projects_

**Request example — A WIP period with WIP projects to be refreshed with the GL actual amounts:**
```json
{
  "periodEndDate": "2023-05-31",
  "wipProjects": [
    {
      "key": "55",
      "wipPeriod": {
        "key": "40"
      },
      "project": {
        "key": "1"
      },
      "isFinalized": false,
      "glPostedDate": "2023-05-31",
      "estimatedCostToDateAmount": "185",
      "jobToDateCosts": "5388.07",
      "estimatedCostToComplete": "-5203.07",
      "estimatedPercentComplete": 29.12,
      "cfoForecast": {
        "percentComplete": 70,
        "costToComplete": "4000.00",
        "contractValue": "10000.00",
        "costAtCompletion": "9500.00",
        "lastUpdatedDate": "2023-05-26T10:06:00Z"
      },
      "projectManagerForecast": {
        "percentComplete": 90,
        "costAtCompletion": "9000.00",
        "costToComplete": "3000.00",
        "contractValue": "10000.00",
        "lastUpdatedDate": "2023-05-26T10:06:00Z"
      },
      "costAtCompletionVariance": "0.00",
      "totalRevisedContract": "26295",
      "contractVarianceAmount": "0",
      "jobToDateBillings": "4858.16",
      "earnedToDateAmount": "76583398.65",
      "remainingBacklogAmount": "-76557103.65",
      "overUnderBillingAmount": "76578540.49",
      "earnedProfitToDateAmount": "76578010.58",
      "grossProfitPercentOfContract": 0.99,
      "grossProfitPercentOfCost": 141.14,
      "totalGrossProfitEstimatedAtCompletion": "26110",
      "cfoForecastGrossProfitAtCompletion": "26110",
      "grossProfitVarianceAmount": "0",
      "cfoForecastGrossProfitMarginPercent": 0.99,
      "remainingProfit": "0",
      "endOfPriorYearEarnedToDateAmount": "0",
      "endOfPriorYearEarnedProfit": "0",
      "yearToDateCostAmount": "15000",
      "yearToDateBillingAmount": "15000",
      "yearToDateEarnedRevenueAmount": "15000",
      "jobToDateOverbillingAmount": "15000",
      "jobToDateUnderbillingAmount": "15000",
      "yearToDateEarnedProfitAmount": "15000",
      "currentPeriodBillingAmount": "15000",
      "currentPeriodCostAmount": "15000",
      "currentPeriodEarnedProfitAmount": "15000",
      "currentPeriodEarnedRevenueAmount": "15000",
      "notes": "not ready"
    }
  ],
  "key": "40"
}
```
**Response 200 — Refresh a list of WIP projects for a given WIP period:**
```json
{
  "ia::result": {
    "wipProjects": [
      {
        "wipPeriod": {
          "isHistoricalImport": false,
          "state": "unposted",
          "key": "40"
        },
        "project": {
          "name": "Dimensions - Berkeley Technology Inc",
          "id": "DIM - BTI",
          "key": "1"
        },
        "customer": {
          "name": "Berkeley Technology Inc",
          "id": "BTI",
          "key": "14"
        },
        "projectStatus": {
          "id": "In Progress"
        },
        "projectType": {
          "id": "Tenant Improvement"
        },
        "manager": {
          "name": "Sanford; Dennis G",
          "id": "EMP00002"
        },
        "class": {
          "name": "Project Class",
          "id": "Project Class"
        },
        "location": {
          "name": "Beaverton",
          "id": "BEAVERTON"
        },
        "department": {
          "name": "Construction Operations",
          "id": "OPERATIONS"
        },
        "cfoForecast": {
          "percentComplete": 70,
          "costToComplete": "4000.00",
          "contractValue": "10000.00",
          "costAtCompletion": "9500.00",
          "lastUpdatedDate": "2023-05-26T10:06:00Z"
        },
        "projectManagerForecast": {
          "percentComplete": 90,
          "costAtCompletion": "9000.00",
          "costToComplete": "3000.00",
          "contractValue": "10000.00",
          "lastUpdatedDate": "2023-05-26T10:06:00Z"
        },
        "notes": "not ready",
        "cfoForecastGrossProfitAtCompletion": "26110",
        "grossProfitPercentOfContract": 0.99,
        "estimatedCostToComplete": "-5203.07",
        "overUnderBillingAmount": "76578540.49",
        "isFinalized": false,
        "grossProfitVarianceAmount": "0",
        "earnedProfitToDateAmount": "76578010.58",
        "remainingProfit": "0",
        "endOfPriorYearEarnedToDateAmount": "0",
        "endOfPriorYearEarnedProfit": "0",
        "estimatedPercentComplete": 29.12,
        "grossProfitPercentOfCost": 141.14,
        "remainingBacklogAmount": "-76557103.65",
        "id": "55",
        "contractVarianceAmount": "0",
        "key": "55",
        "cfoForecastGrossProfitMarginPercent": 0.99,
        "totalGrossProfitEstimatedAtCompletion": "26110",
        "jobToDateBillings": "4858.16",
        "jobToDateCosts": "5388.07",
        "estimatedCostToDateAmount": "185.00",
        "earnedToDateAmount": "76583398.65",
        "totalRevisedContract": "26295.00",
        "yearToDateCostAmount": "15000",
        "yearToDateBillingAmount": "15000",
        "yearToDateEarnedRevenueAmount": "15000",
        "jobToDateOverbillingAmount": "15000",
        "jobToDateUnderbillingAmount": "15000",
        "yearToDateEarnedProfitAmount": "15000",
        "currentPeriodBillingAmount": "15000",
        "currentPeriodCostAmount": "15000",
        "currentPeriodEarnedProfitAmount": "15000",
        "currentPeriodEarnedRevenueAmount": "15000"
      }
    ],
    "lastRefreshDateTime": "2023-06-02T15:11:07Z",
    "wipCostBreakdownLevel": "costCodeAndCostType"
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/construction-forecasting/wip-project/calculate
_Calculate a WIP project_

**Request example — Calculate WIP project forecast for a new cfoForecastPercentComplete value:**
```json
{
  "calculationRequested": "projectManagerForecastPercentComplete",
  "wipProject": {
    "key": "8",
    "project": {
      "key": "3"
    },
    "isFinalized": false,
    "jobToDateCosts": "1134076.65",
    "jobToDateBillings": "0",
    "earnedToDateAmount": "0",
    "overUnderBillingAmount": "0",
    "cfoForecastGrossProfitAtCompletion": "0",
    "totalContractValue": "1270800",
    "estimatedCostToDateAmount": "1081591.99",
    "estimatedCostAtCompletion": "1081591.99",
    "pendingEstimatesAmount": "0",
    "totalGrossProfitEstimatedAtCompletion": "189208.01",
    "estimatedPercentComplete": 104.85,
    "estimatedCostToComplete": "-52484.66",
    "contractVarianceAmount": "0",
    "remainingBacklogAmount": "0",
    "earnedProfitToDateAmount": "0",
    "grossProfitVarianceAmount": "0",
    "remainingProfit": "0",
    "endOfPriorYearEarnedToDateAmount": "0",
    "endOfPriorYearEarnedProfit": "0",
    "currentPeriodBilledToDateAmount": "0",
    "jobToDateOverbillingAmount": "0",
    "jobToDateUnderbillingAmount": "0",
    "projectManagerForecast": {
      "costToComplete": "-52484.66",
      "costAtCompletion": "1081591.99",
      "percentComplete": 99,
      "contractValue": "1270800"
    },
    "cfoForecast": {
      "costToComplete": "0",
      "costAtCompletion": "0",
      "percentComplete": 0,
      "contractValue": "0"
    }
  }
}
```
**Response 200 — Calculated project manager WIP forecast:**
```json
{
  "ia::result": {
    "warnings": [
      {
        "severity": "error",
        "fieldNames": [
          "cfoForecastCostAtCompletion"
        ],
        "errorMessage": "The field 'CFO forecast cost at completion' cannot be zero if the field 'Job-to-date costs' is greater than zero. Enter a positive amount for field 'CFO forecast cost at completion'.",
        "target": "3"
      },
      {
        "severity": "warning",
        "fieldNames": [
          "projectManagerForecastCostToComplete"
        ],
        "errorMessage": "The field 'PM forecast cost to complete' will be rounded to two decimal places.",
        "target": "3"
      },
      {
        "severity": "warning",
        "fieldNames": [
          "projectManagerForecastCostAtCompletion"
        ],
        "errorMessage": "The field 'PM forecast cost at completion' will be rounded to two decimal places.",
        "target": "3"
      }
    ],
    "wipProject": {
      "project": {
        "key": "3"
      },
      "projectManagerForecast": {
        "contractValue": "1270800.00",
        "lastUpdatedDate": "2024-10-23T15:45:16Z",
        "costAtCompletion": "1145531.97",
        "costToComplete": "11455.32",
        "percentComplete": 99
      },
      "cfoForecast": {
        "contractValue": "0.00",
        "costAtCompletion": "0.00",
        "costToComplete": "0.00",
        "percentComplete": 0
      },
      "remainingProfit": "0.00",
      "totalContractValue": "1270800.00",
      "endOfPriorYearEarnedToDateAmount": "0.00",
      "earnedProfitToDateAmount": "0.00",
      "cfoForecastGrossProfitAtCompletion": "0.00",
      "estimatedCostToComplete": "-52484.66",
      "overUnderBillingAmount": "0.00",
      "grossProfitVarianceAmount": "0.00",
      "estimatedPercentComplete": 104.85,
      "jobToDateCosts": "1134076.65",
      "endOfPriorYearEarnedProfit": "0.00",
      "remainingBacklogAmount": "0.00",
      "id": "8",
      "currentPeriodBilledToDateAmount": "0.00",
      "estimatedCostToDateAmount": "1081591.99",
      "contractVarianceAmount": "0.00",
      "key": "8",
      "jobToDateUnderbillingAmount": "0.00",
      "totalGrossProfitEstimatedAtCompletion": "189208.01",
      "jobToDateBillings": "0.00",
      "earnedToDateAmount": "0.00",
      "jobToDateOverbillingAmount": "0.00",
      "estimatedCostAtCompletion": "1081591.99",
      "pendingEstimatesAmount": "0.00"
    }
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/construction-forecasting/wip-reporting-period/get-available
_Get available periods_

**Request example — Request available reporting periods for a given date:**
```json
{
  "periodEndDate": "2023-06-02"
}
```
**Response 200 — List available reporting periods for creating a WIP period:**
```json
{
  "ia::result": {
    "periods": [
      {
        "header2": "June",
        "header1": "Month Ended",
        "endDate": "2023-06-30",
        "name": "Month Ended June 2023",
        "id": "131",
        "key": "131",
        "startDate": "2023-06-01"
      },
      {
        "header2": "July",
        "header1": "Month Ended",
        "endDate": "2023-07-31",
        "name": "Month Ended July 2023",
        "id": "132",
        "key": "132",
        "startDate": "2023-07-01"
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

## POST /services/construction-forecasting/wip-reporting-period/get-next
_Get next period_

**Request example — Request the next reporting period that follows the specified date:**
```json
{
  "periodEndDate": "2023-06-02"
}
```
**Response 200 — Details of the next reporting period:**
```json
{
  "ia::result": {
    "period": {
      "endDate": "2023-06-30",
      "isBudgetable": true,
      "id": "Month Ended June 2023",
      "columnHeader1": "Month Ended",
      "columnHeader2": "June",
      "key": "116",
      "startDate": "2023-06-01",
      "status": "active"
    },
    "errors": []
  },
  "ia::meta": {
    "totalCount": 1,
    "totalSuccess": 1,
    "totalError": 0
  }
}
```

## POST /services/construction-forecasting/wip-rollup-project/exclude-from-wip
_Exclude projects from WIP schedule_

**Request example — Request body for bulk action request:**
```json
{
  "projectKeys": [
    "2408",
    "3219",
    "5",
    "10"
  ]
}
```

## POST /services/construction-forecasting/wip-rollup-project/find-rollup-projects
_Get rollup projects_

**Request example — Get rollup projects:**
```json
{
  "subprojectKeys": [
    "148",
    "149",
    "151"
  ]
}
```
**Response 200 — Rollup projects:**
```json
{
  "ia::result": {
    "targetProjects": [
      {
        "name": "Dimensions - Berkeley Technology Inc",
        "id": "DIM - BTI",
        "key": "1"
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

## POST /services/construction-forecasting/wip-rollup-project/include-as-wip
_Include in a WIP schedule project_

**Request example — Include in a WIP schedule project:**
```json
{
  "projectKeys": [
    "2408",
    "3219",
    "5",
    "10"
  ]
}
```

## POST /services/construction-forecasting/wip-rollup-project/include-in-project
_Include in a WIP project_

**Request example — Include subprojects in WIP project:**
```json
{
  "projectKeys": [
    "2408",
    "3219",
    "5",
    "10"
  ],
  "wipScheduleProjectKey": "14"
}
```

## POST /services/construction-forecasting/wip-rollup-project/include-in-root
_Include projects with root project_

**Request example — Request body for bulk action request:**
```json
{
  "projectKeys": [
    "2408",
    "3219",
    "5",
    "10"
  ]
}
```
