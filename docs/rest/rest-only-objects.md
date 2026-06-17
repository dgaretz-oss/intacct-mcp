# REST-Only Objects (No XML Equivalent)

These 173 objects exist **only in the REST API**. Attempting to access them
via `call_xml_gateway` or an XML `readByQuery` will fail. Always use
`call_intacct` or `common_query` for these.

If you receive a "not found" or "invalid object" error from the XML gateway
for one of the names below, the object does not exist in XML — switch to REST.

---

## Accounts Payable

| REST Path | Notes |
|---|---|
| `accounts-payable/adjustment-tax-entries` | REST-only; no XML APADJUSTMENTTAX |
| `accounts-payable/bill-tax-entry` | REST-only |
| `accounts-payable/check-run` | REST-only |
| `accounts-payable/recurring-bill-tax-entry` | REST-only |
| `accounts-payable/vendor-restricted-department` | REST-only |
| `accounts-payable/vendor-restricted-location` | REST-only |
| `accounts-payable/vendor-total` | REST-only |

## Accounts Receivable

| REST Path | Notes |
|---|---|
| `accounts-receivable/adjustment-tax-entry` | REST-only |
| `accounts-receivable/customer-message` | REST-only (map shows customer-type — likely a data error) |
| `accounts-receivable/customer-refund` | REST-only |
| `accounts-receivable/customer-refund-detail` | REST-only |
| `accounts-receivable/customer-refund-line` | REST-only |
| `accounts-receivable/customer-restricted-department` | REST-only |
| `accounts-receivable/customer-restricted-location` | REST-only |
| `accounts-receivable/customer-total` | REST-only |
| `accounts-receivable/delivery-history` | REST-only |
| `accounts-receivable/dunning-customer` | REST-only |
| `accounts-receivable/dunning-invoice` | REST-only |
| `accounts-receivable/dunning-notice` | REST-only |
| `accounts-receivable/invoice-tax-entry` | REST-only |
| `accounts-receivable/manual-deposit` | REST-only |
| `accounts-receivable/manual-deposit-line` | REST-only |
| `accounts-receivable/manual-deposit-summary` | REST-only |
| `accounts-receivable/payment-line` | REST-only |
| `accounts-receivable/recurring-invoice-tax-entry` | REST-only (map shows recurring-invoice-line — likely a data error) |
| `accounts-receivable/shipping-method` | REST-only |
| `accounts-receivable/territory-group` | REST-only |

## Cash Management

| REST Path | Notes |
|---|---|
| `cash-management/credit-card-txn-tax-entry` | REST-only |
| `cash-management/initial-open-item` | REST-only |
| `cash-management/other-receipt-tax-entry` | REST-only |
| `cash-management/received-payment` | REST-only |
| `cash-management/received-payment-line` | REST-only |
| `cash-management/reconciliation-source-record` | REST-only |

## Common Services

These use a `/services/…` URL pattern, not the standard `objects/module/name` pattern.

| REST Path | Notes |
|---|---|
| `/services/bulk/job/create` | REST-only |
| `/services/bulk/job/status` | REST-only |
| `/services/core/composite` | REST-only |
| `/services/core/operation` | REST-only |
| `/services/core/scheduled-operation` | REST-only |
| `/services/core/schedule` | REST-only |

## Company Configuration

| REST Path | Notes |
|---|---|
| `company-config/affiliate-entity` | REST-only |
| `company-config/affiliate-entity-group` | REST-only |
| `company-config/cloud-storage` | REST-only |
| `company-config/document-sequence-rollover` | REST-only |
| `company-config/email-delivery-record` | REST-only |
| `company-config/employee-bank-file-setup` | REST-only |
| `company-config/payment-provider-notification` | REST-only |
| `company-config/txn-currency` | REST-only |

## Consolidation

| REST Path | Notes |
|---|---|
| `consolidation/run-status` | REST-only |
| `consolidation/time-period` | REST-only |

## Construction

| REST Path | Notes |
|---|---|
| `construction/ap-releasable-retainage` | REST-only |
| `construction/ar-releasable-retainage` | REST-only |
| `construction/compliance-definition` | REST-only |
| `construction/compliance-definition-association` | REST-only |
| `construction/compliance-record` | REST-only |
| `construction/compliance-type` | REST-only |
| `construction/cost-type-observed-percent-completed` | REST-only |
| `construction/primary-document-accounts-payable-bill` | REST-only |
| `construction/primary-document-accounts-payable-payment` | REST-only |
| `construction/primary-document-detail` | REST-only |
| `construction/primary-document-retainage-release` | REST-only |
| `construction/primary-document-summary` | REST-only |
| `construction/project-contract-billing-invoice-detail` | REST-only |
| `construction/project-contract-billing-invoice-summary` | REST-only |
| `construction/work-order` | REST-only |
| `construction/work-order-call-type` | REST-only |
| `construction/work-order-problem-code` | REST-only |
| `construction/work-order-state` | REST-only |
| `construction/work-order-type` | REST-only |

## Construction Forecasting

All WIP objects are REST-only and use the `construction-forecasting/` module prefix.

| REST Path | Notes |
|---|---|
| `construction-forecasting/wip-forecast-detail` | REST-only |
| `construction-forecasting/wip-period` | REST-only |
| `construction-forecasting/wip-project` | REST-only |
| `construction-forecasting/wip-project-manager-forecast` | REST-only |
| `construction-forecasting/wip-project-setting` | REST-only |
| `construction-forecasting/wip-setup` | REST-only |
| `construction-forecasting/wip-setup-account` | REST-only |
| `construction-forecasting/wip-target-project` | REST-only |

## Contracts and Revenue Management

| REST Path | Notes |
|---|---|
| `contracts/bulk-action-run-summary` | REST-only |
| `contracts/compliance-checklist-task` | REST-only |
| `contracts/compliance-note` | REST-only |
| `contracts/compliance-task` | REST-only |
| `contracts/contract-group-member` | REST-only |
| `contracts/contract-txn-history` | REST-only |
| `contracts/evergreen-template` | REST-only |
| `contracts/historical-schedule-run` | REST-only |

## Expenses

| REST Path | Notes |
|---|---|
| `expenses/electronic-receipt` | REST-only |
| `expenses/electronic-receipt-lines` | REST-only |
| `expenses/employee-expense-to-approve` | REST-only — approval workflow |
| `expenses/expense-to-approve-line` | REST-only — approval workflow |
| `expenses/unit-rate` | REST-only |

## Fixed Assets Management

**Entire module is REST-only** — no XML equivalents exist for any Fixed Assets object.

| REST Path | Notes |
|---|---|
| `fixed-assets/asset` | REST-only |
| `fixed-assets/asset-classification` | REST-only |
| `fixed-assets/depreciation-method` | REST-only |
| `fixed-assets/depreciation-rule` | REST-only |
| `fixed-assets/depreciation-schedule` | REST-only |
| `fixed-assets/depreciation-schedule-entry` | REST-only |
| `fixed-assets/disposal` | REST-only |
| `fixed-assets/disposal-depreciation-schedule-map` | REST-only |
| `fixed-assets/setup` | REST-only |
| `fixed-assets/setup-posting-rule` | REST-only |
| `fixed-assets/transfer-history` | REST-only |
| `fixed-assets/transfer-journal-entry-map` | REST-only |

## General Ledger

| REST Path | Notes |
|---|---|
| `general-ledger/account-category` | REST-only |
| `general-ledger/account-group-category-member` | REST-only |
| `general-ledger/account-group-computation` | REST-only |
| `general-ledger/account-group-map` | REST-only |
| `general-ledger/account-group-member` | REST-only |
| `general-ledger/accounting-sequence` | REST-only |
| `general-ledger/accounting-sequence-line` | REST-only |
| `general-ledger/adjustment-journal` | REST-only |
| `general-ledger/financial-graph` | REST-only |
| `general-ledger/gaap-adjustment-journal` | REST-only |
| `general-ledger/journal-entry-tax-entry` | REST-only |
| `general-ledger/journal-entry-txn-template` | REST-only |
| `general-ledger/journal-entry-txn-template-line` | REST-only |
| `general-ledger/report-audience` | REST-only |
| `general-ledger/report-type` | REST-only |
| `general-ledger/reporting-account` | REST-only |
| `general-ledger/reporting-account-map` | REST-only |
| `general-ledger/reporting-account-set` | REST-only |
| `general-ledger/reporting-account-set-permission` | REST-only |
| `general-ledger/statistical-adjustment-journal` | REST-only |
| `general-ledger/tax-adjustment-journal` | REST-only |
| `general-ledger/user-defined-book` | REST-only |
| `general-ledger/user-defined-journal` | REST-only |

## Inventory Control

| REST Path | Notes |
|---|---|
| `inventory-control/document-history` | REST-only |
| `inventory-control/document-line-detail` | REST-only |
| `inventory-control/document-line-supplies-detail` | REST-only |
| `inventory-control/item-tax-group-item-map` | REST-only |
| `inventory-control/item-warehouse-available-inventory` | REST-only |
| `inventory-control/landed-cost-category` | REST-only |
| `inventory-control/lot-category` | REST-only |
| `inventory-control/posting-summary` | REST-only |
| `inventory-control/replenishment-forecast` | REST-only |
| `inventory-control/replenishment-forecast-line` | REST-only |
| `inventory-control/replenishment-run` | REST-only |
| `inventory-control/replenishment-run-line` | REST-only |
| `inventory-control/serial-mask` | REST-only |
| `inventory-control/stockable-kit-document` | REST-only |
| `inventory-control/stockable-kit-document-line` | REST-only |
| `inventory-control/supplies-document` | REST-only |
| `inventory-control/supplies-document-detail` | REST-only |

## Order Entry

| REST Path | Notes |
|---|---|
| `order-entry/customer-gl-group` | REST-only |
| `order-entry/document-configuration-preference` | REST-only |
| `order-entry/price-schedule` | REST-only |
| `order-entry/recurring-schedule` | REST-only |
| `order-entry/subtotal-template-line` | REST-only |
| `order-entry/txn-buy-to-order-preference` | REST-only |
| `order-entry/txn-drop-ship-preference` | REST-only |

## Project and Resource Management

| REST Path | Notes |
|---|---|
| `projects/invoice-run` | REST-only |
| `projects/project-billing-template` | REST-only |
| `projects/project-billing-template-milestone` | REST-only |
| `projects/task-group` | REST-only (note: correct path is `projects/task-group`, not `projets/`) |

## Purchasing

| REST Path | Notes |
|---|---|
| `purchasing/document-configuration-preference` | REST-only |
| `purchasing/document-history` | REST-only |
| `purchasing/document-line-detail` | REST-only |
| `purchasing/recurring-document` | REST-only |
| `purchasing/recurring-document-line` | REST-only |
| `purchasing/recurring-document-subtotal` | REST-only |
| `purchasing/subtotal-template-line` | REST-only |
| `purchasing/txn-automation-preference` | REST-only |
| `purchasing/txn-automation-without-match-preference` | REST-only |
| `purchasing/txn-definition-additional-gl-detail` | REST-only |
| `purchasing/txn-definition-ap-direct-gl-detail` | REST-only |
| `purchasing/txn-definition-entity-setting-detail` | REST-only |
| `purchasing/txn-definition-inventory-total-detail` | REST-only |
| `purchasing/txn-definition-source-document-detail` | REST-only |
| `purchasing/txn-definition-subtotal-detail` | REST-only |
| `purchasing/txn-match-tolerance-preference` | REST-only |
| `purchasing/vendor-gl-group` | REST-only |

## Reports

**Entire module is REST-only.**

| REST Path | Notes |
|---|---|
| `reports/stored-report` | REST-only |
| `reports/stored-report-error-record` | REST-only |

## Tax

| REST Path | Notes |
|---|---|
| `tax/account-label-tax-group` | REST-only |
| `tax/tax-detail` | REST-only |

## Time

| REST Path | Notes |
|---|---|
| `time/timesheet-to-approve` | REST-only — approval workflow |
| `timesheet/timesheet-rule` | REST-only (note: uses `timesheet/` prefix, not `time/`) |
