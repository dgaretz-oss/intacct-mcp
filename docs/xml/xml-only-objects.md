# XML-Only Objects (No REST Equivalent)

These 366 objects exist **only in the XML API**. Attempting to access them via
`call_intacct` or `common_query` will return a 404 or "object not found" error.
Use `call_xml_gateway` with `readByQuery` or the appropriate legacy function.

If you receive a REST 404 for one of the XML object names below, the object
has not been ported to REST — switch to `call_xml_gateway`.

---

## Accounts Payable (25)

| Description | XML Object |
|---|---|
| AP advance | `APADVANCE` |
| AP advance detail | `APADVANCEITEM` |
| AP approval policy | `APAPPROVALPOLICY` |
| AP approval rule | `APAPPROVALRULE` |
| AP bill payment | `APBILLPAYMENT` |
| AP detail | `APDETAIL` |
| AP discount | `APDISCOUNT` |
| AP payment | `APPAYMENT` |
| AP payment detail | `APPAYMENTITEM` |
| AP payment history | `APPAYMENTHISTORYREPORT` |
| AP payment request | `APPAYMENTREQUEST` |
| AP payments (primary doc) | `PRIMARYDOCAPPAYMENTS` |
| AP posted advance | `APPOSTEDADVANCE` |
| AP posted advance line detail | `APPOSTEDADVANCEENTRY` |
| AP record | `APRECORD` |
| AP releasable retainage record | `APRELEASEABLERECORD` |
| AP summary (open) | `APOPENSUMMARY` |
| AP summary (closed) | `APCLOSESUMMARY` |
| Approval delegate | `APAPPROVALDELEGATE` |
| Deferred adjustments schedule | `APAMORTIZATIONSCHEDULE` |
| Deferred adjustments template | `APAMORTIZATIONTEMPLATE` |
| Joint payee | `APBILLJOINTPAYEE` |
| Manage delegates | `APAPPROVALDELEGATEDETAIL` |
| Primary document AP bills | `PRIMARYDOCAPBILLS` |
| Value approval rule set | `APAPPROVALRULESET` |

## Accounts Receivable (20)

| Description | XML Object |
|---|---|
| AR account label tax group | `ACCTLABELTAXGROUP` |
| AR detail | `ARDETAIL` |
| AR invoice payment | `ARINVOICEPAYMENT` |
| AR payment | `ARPAYMENT` |
| AR payment detail | `ARPAYMENTITEM` |
| AR payment history | `ARPAYMENTHISTORYREPORT` |
| AR payment summary | `ARPAYMENTBATCH` |
| AR posted overpayment | `ARPOSTEDOVERPAYMENT` |
| AR posted overpayment line detail | `ARPOSTEDOVERPAYMENTENTRY` |
| AR receivables payment line detail | `ARPYMTENTRY` |
| AR record | `ARRECORD` |
| AR releasable retainage record | `ARRELEASEABLERECORD` |
| AR setup | `ARSETUP` |
| AR summary (open) | `AROPENSUMMARY` |
| AR summary (closed) | `ARCLOSESUMMARY` |
| Deferred adjustments schedule | `ARAMORTIZATIONSCHEDULE` |
| Deferred adjustments template | `ARAMORTIZATIONTEMPLATE` |
| TPAR box | `IATPARBOX` |
| TPAR type | `IATPARTYPE` |
| Vendor TPAR initial balance | `VENDORTPARINITIALBALANCE` |

## Cash Management (5)

| Description | XML Object |
|---|---|
| Bank account | `BANKACCOUNT` |
| Bank account transaction feed records | `BANKACCTTXNRECORD` |
| Bank transaction rule attribute | `BANKTXNRULEATTR` |
| Cash Management detail | `CMDETAIL` |
| Cash Management record | `CMRECORD` |

## Company & Config (17)

| Description | XML Object |
|---|---|
| Close Assistant run | `COMPANYCLOSEASSISTANTRUN` |
| Company information | `COMPANY` |
| Company preference | `COMPANYPREF` |
| Custom role policy assignment | `CUSTOMROLEPOLASSIGNMENT` |
| Employee bank file detail | `EMPLOYEEBANKFILEDETAIL` |
| Employee entity contact | `EMPLOYEEENTITYCONTACTS` |
| Employee group | `EMPLOYEEGROUP` |
| Employee out of office | `EMPLOYEEOUTOFOFFICE` |
| Employee positions and skills | `EMPLOYEEPOSITIONSKILL` |
| Member user groups | `MEMBERUSERGROUP` |
| OAuth user | `OAUTHUSER` |
| Role assignments | `ROLEASSIGNMENT` |
| User permissions | `USERRIGHTS` |
| User permissions activity | `AUDUSERTRAIL` |
| User restriction | `USERRESTRICTION` |
| User role | `USERROLES` |
| User-defined book | `USERADJBOOK` |

## Consolidation (6)

| Description | XML Object |
|---|---|
| Consolidation account | `CNSACCOUNT` |
| Consolidation account balance | `CNSACCTBAL` |
| Consolidation entries | `GCCONSOLIDATIONENTRY` |
| Consolidation journal entry | `CONSGLBATCH` |
| Consolidation period | `CNSPERIOD` |
| Ownership structure entity | `GCOWNERSHIPENTITY` |

## Construction (14)

| Description | XML Object |
|---|---|
| Retainage release bills | `PRIMARYDOCRETAINAGERELEASE` |
| WIP actual detail | `WIPACTUALSDRILLDOWN` |
| WIP forecast detail | `WIPFORECASTDETAIL` |
| WIP project manager forecast | `WIPPROJECTMANAGERFORECAST` |
| WIP project setting | `WIPPROJECTSETTING` |
| WIP report account setup | `WIPSETUPACCOUNT` |
| WIP report setup | `WIPSETUP` |
| WIP target project | `WIPTARGETPROJECT` |
| Work order | `WORKORDER` |
| Work order call type | `WORKORDERCALLTYPE` |
| Work order group | `WORKORDERGROUP` |
| Work order problem code | `WORKORDERPROBLEMCODE` |
| Work order state | `WORKORDERSTATE` |
| Work order type | `WORKORDERTYPE` |

## Contracts & Revenue (43)

| Description | XML Object |
|---|---|
| Billing group | `BILLINGGROUP` |
| Billing schedule | `BILLINGSCHEDULE` |
| Billing template | `BILLINGTEMPLATE` |
| Billing group charges record | `BILLINGGROUPCHARGESRECORD` |
| Contract MEA allocation details | `CONTRACTALLOCATIONDETAIL` |
| Contract MEA allocation details (bundle) | `CONTRACTALLOCATIONFORBUNDLE` |
| Contract MEA bundle entry | `CONTRACTMEABUNDLEENTRY` |
| Contract MEA instruction | `CONTRACTMEAINSTRUCTION` |
| Contract MEA instruction part | `CONTRACTMEAINSTPART` |
| Contract MRR link | `CONTRACTMRRRESOLVE` |
| Contract billing template | `CONTRACTBILLINGTEMPLATE` |
| Contract billing template entry | `CONTRACTBILLINGTEMPLATEENTRY` |
| Contract compliance checklist | `CONTRACTCOMPLIANCETASK` |
| Contract compliance note | `CONTRACTCOMPLIANCENOTE` |
| Contract compliance task item | `CONTRACTCOMPLIANCETASKITEM` |
| Contract expense schedule 2 | `CONTRACTEXPENSE2SCHEDULE` |
| Contract line dimension | `CONTRACTDETAILDIMENSION` |
| Contract negative billing | `CONTRACTNEGATIVEBILLING` |
| Contract negative billing entry | `CONTRACTNEGATIVEBILLINGENTRY` |
| Contract posting config — revenue | `CONTRACTREVENUEGLCONFIG` |
| Contract posting config — expense | `CONTRACTEXPENSEGLCONFIG` |
| Contract resolve additional data | `CONTRACTRSLVADDLDATA` |
| Contract revenue schedule 2 | `CONTRACTREVENUE2SCHEDULE` |
| Contract revenue template entry | `CONTRACTREVENUETEMPLATEENTRY` |
| Contract schedule entry resolve | `CONTRACTSCHEDULESRESOLVE` |
| Contract schedule forecast | `CONTRACTSCHFORECAST` |
| Contract schedules processing results entry | `CONTRACTACPRUNENTRY` |
| Contract subledger links | `CONTRACTRESOLVE` |
| Contract usage billing | `CONTRACTUSAGEBILLING` |
| Process contract schedules | `CONTRACTACPRUN` |
| Project contract billing invoice detail | `PCBINVDETAIL` |
| Project contract billing invoice summary | `PCBINVSUMMARY` |
| Project contract line task | `PCLTASK` |
| Revenue recognition batch | `REVRECBATCH` |
| Revenue recognition change history | `REVRECCHANGELOG` |
| Revenue recognition schedule | `REVRECSCHEDULE` |
| Revenue recognition schedule entry | `REVRECSCHEDULEENTRY` |
| Revenue recognition schedule entry task detail | `REVRECSCHEDULEENTRYTASK` |
| Revenue recognition template entry | `REVRECTEMPLENTRY` |
| Revenue recognition template milestone | `REVRECTEMPLMILESTONE` |
| SaaS metrics change type | `SAASCHANGETYPE` |
| SaaS metrics schedule | `SAASSCHEDULE` |
| SaaS metrics schedule entry | `SAASSCHEDULEENTRY` |

## Expenses (9)

| Description | XML Object |
|---|---|
| Employee expense | `EEXPENSES` |
| Employee expense detail (item) | `EEXPENSESITEM` |
| Employee expense detail | `EEDETAIL` |
| Employee expense record | `EERECORD` |
| Employee expense reimbursement | `EPPAYMENT` |
| Employee expenses payment | `EEXPENSESPAYMENT` |
| Employee payment detail | `EPPAYMENTITEM` |
| Expense approval | `EXPENSESAPPROVAL` |
| Pending reimbursement | `EPPAYMENTREQUEST` |

## General Ledger (32)

| Description | XML Object |
|---|---|
| Account groups hierarchy | `GLACCTGRPHIERARCHY` |
| Accounting sequence | `JOURNALSEQNUM` |
| Accounting sequence number entry | `JOURNALSEQNUMENTRY` |
| Budget | `BUDGETHEADER` |
| GAAP adjustment journal | `GAAPADJJRNL` |
| GL account allocation basis adjustment books | `GLACCTALLOCATIONBASISADJBOOKS` |
| GL account allocation source adjustment book | `GLACCTALLOCATIONSOURCEADJBOOKS` |
| GL account balance | `GLACCOUNTBALANCE` |
| GL account category | `GLCOACATMEMBER` |
| GL account group member | `GLACCTGRPMEMBER` |
| GL budget | `GLBUDGET` |
| GL computation group member | `GLCOMPGRPMEMBER` |
| GL definitions | `DOCUMENTPARPRGL` |
| GL entry resolve | `GLRESOLVE` |
| GL restriction release | `GLRESTRICTIONRELEASE` |
| General ledger detail | `GLDETAIL` |
| General ledger document detail | `GLDOCDETAIL` |
| Inventory GL definitions | `DOCUMENTPARINVGL` |
| Journal | `JOURNAL` |
| Link doc entry and GL entry | `DEGLPOSTING` |
| Link doc entry subtotal and GL entry | `DEGLSUBTOTALPOSTING` |
| Link PR and GL | `PRGLPOSTING` |
| Link PR and GL (IET) | `GLIETPOSTING` |
| Link prior periods COGS adjustments and GL entry | `PRIORPERIODCOGSPOSTING` |
| Recurring GL account allocation | `RECURGLACCTALLOCATION` |
| Recurring journal entry | `RECURGLBATCH` |
| Recurring journal entry details | `RECURGLENTRY` |
| Report audience | `GLREPORTAUDIENCE` |
| Report type | `GLREPORTTYPE` |
| Run object summary | `GLOBALRUNOBJECTSUMMARY` |
| Tax adjustment journal | `TAXADJJRNL` |
| User-defined journal | `USERADJJRNL` |

## Inventory Control (18)

| Description | XML Object |
|---|---|
| Available inventory | `AVAILABLEINVENTORY` |
| Build and disassemble kits transaction | `STKITDOCUMENT` |
| Build and disassemble kits transaction detail | `STKITDOCUMENTENTRY` |
| Document estimate landed cost entry | `PODOCUMENTLCESTENTRY` |
| Inv recurring subtotals | `INVRECURSUBTOTALS` |
| Inventory total detail | `INVENTORYTOTALDETAIL` |
| Invoice run | `INVOICERUN` |
| Kit costing | `KITCOSTING` |
| Landed cost history | `LANDEDCOSTHISTORY` |
| Lines in fulfillment | `INVENTORYWQDETAIL` |
| Maintain inventory valuation | `INVHLTHRUN` |
| Orders in fulfillment | `INVENTORYWQORDER` |
| Recurring inventory transaction | `INVRECURDOCUMENT` |
| Replenishment forecast | `REPLENISHFORECAST` |
| Replenishment forecast detail | `REPLENISHFORECASTDETAIL` |
| Replenishment report | `REPLENISHMENT` |
| Warehouse group | `WAREHOUSEGROUP` |
| Work queue | `INVENTORYWORKQUEUE` |

## Order Entry (4)

| Description | XML Object |
|---|---|
| SO recurring subtotals | `SORECURSUBTOTALS` |
| SO setup | `SOSETUP` |
| SO doc convert-to | `SODOCCONVERTTO` |
| Subtotal template detail | `SOSUBTOTALTEMPLATEDETAIL` |

## Payroll (29)

| Description | XML Object |
|---|---|
| Payroll report check | `PAYROLLREPORTCHECK` |
| Payroll report compensation table | `PAYROLLREPORTCOMPENSATIONTABLE` |
| Payroll report compensation trade | `PAYROLLREPORTCOMPENSATIONTRADE` |
| Payroll report compensation trade level | `PAYROLLREPORTCOMPENSATIONTRADELEVEL` |
| Payroll report compensation trade level rate | `PAYROLLREPORTCOMPENSATIONTRADELEVELRATES` |
| Payroll report employee | `PAYROLLREPORTEMPLOYEE` |
| Payroll report employee tax classification | `PAYROLLREPORTEMPLOYEETAXCLASSIFICATION` |
| Payroll report employee trade detail | `PAYROLLREPORTEMPLOYEETRADEDETAIL` |
| Payroll report gross pay | `PAYROLLREPORTGROSSPAY` |
| Payroll report hour type | `PAYROLLREPORTHOURTYPE` |
| Payroll report pay group | `PAYROLLREPORTPAYGROUP` |
| Payroll report pay modifier | `PAYROLLREPORTPAYMODIFIER` |
| Payroll report pay modifier basis | `PAYROLLREPORTPAYMODIFIERBASIS` |
| Payroll report pay modifier rate | `PAYROLLREPORTPAYMODIFIERRATES` |
| Payroll report pay modifier selection rules | `PAYROLLREPORTPAYMODIFIERSELECTIONRULES` |
| Payroll report pay modifier setup | `PAYROLLREPORTPAYMODIFIERSETUP` |
| Payroll report PTO accrual schedule | `PAYROLLREPORTPTOACCRUALSCHEDULE` |
| Payroll report PTO accrual schedule line | `PAYROLLREPORTPTOACCRUALSCHEDULELINE` |
| Payroll report PTO accrual schedule rate | `PAYROLLREPORTPTOACCRUALSCHEDULERATE` |
| Payroll report PTO activity | `PAYROLLREPORTPTOACTIVITY` |
| Payroll report PTO type | `PAYROLLREPORTPTOTYPE` |
| Payroll report tax | `PAYROLLREPORTTAX` |
| Payroll report tax setup | `PAYROLLREPORTTAXSETUP` |
| Payroll report time card | `PAYROLLREPORTTIMECARD` |
| Payroll report trade | `PAYROLLREPORTTRADE` |
| Payroll report trade level | `PAYROLLREPORTTRADELEVEL` |
| Payroll report trade tax classification | `PAYROLLREPORTTRADETAXCLASSIFICATION` |
| Payroll report union local | `PAYROLLREPORTUNIONLOCAL` |
| Payroll report union local reciprocity rule | `PAYROLLREPORTUNIONLOCALRECIPROCITYRULES` |

## Projects (7)

| Description | XML Object |
|---|---|
| Project totals | `PROJECTTOTALS` |
| Project transaction rule | `PROJECTTRANSACTIONRULE` |
| Task (pick) | `TASKPICK` |
| Task group | `TASKGROUP` |
| Task group (pick) | `TASKNGROUPPICK` |
| Task group members | `TASKGRPMEMBER` |
| Task resource | `TASKRESOURCES` |

## Purchasing (15)

| Description | XML Object |
|---|---|
| Approval delegate | `POAPPROVALDELEGATE` |
| Documents configuration | `PODOCUMENTCONFIGSETUP` |
| Manage delegates | `POAPPROVALDELEGATEDETAIL` |
| PO match doc type map setup | `POMATCHDOCTYPEMAPSETUP` |
| PO recurring subtotals | `PORECURSUBTOTALS` |
| PO setup | `POSETUP` |
| Purchasing approval history | `PODOCUMENTAPPROVAL` |
| Purchasing approval policy | `POAPPROVALPOLICY` |
| Purchasing approval policy details | `POAPPROVALPOLICYDETAIL` |
| Purchasing approval rule | `POAPPROVALRULE` |
| Purchasing approval rule details | `POAPPROVALRULEDETAIL` |
| Recurring purchasing transaction | `PORECURDOCUMENT` |
| SC purchasing doc | `SCPURCHASINGDOC` |
| Subtotal template detail | `POSUBTOTALTEMPLATEDETAIL` |
| Value approval rule set | `POAPPROVALRULESET` |

## Tax (9)

| Description | XML Object |
|---|---|
| PR tax entry | `PRTAXENTRY` |
| T5018 | `T5018` |
| TPAR | `TPAR` |
| Tax code | `TAXCODE` |
| Tax detail | `TAXDETAIL` |
| Tax detail box | `TAXDETAILBOX` |
| Tax filing definition | `TAXREPORTDEFINITION` |
| Tax setup | `TAXSETUP` |
| US tax service setup | `TAXSERVICESETUP` |

## Time (2)

| Description | XML Object |
|---|---|
| My timesheet | `MYTIMESHEET` |
| My timesheet entry | `MYTIMESHEETENTRY` |

## Miscellaneous (111)

Objects whose module is ambiguous or that span multiple modules.

| Description | XML Object |
|---|---|
| 1099 e-file submission status | `FILE1099SUBMISSIONLOG` |
| 1099 e-file submissions | `FILE1099` |
| ACH bank | `ACHBANK` |
| Activity trail | `ACTIVITYLOG` |
| Affiliate entity | `AFFILIATEENTITY` |
| Affiliate entity group | `AFFILIATEENTITYGROUP` |
| API usage detail | `APIUSAGEDETAIL` |
| API usage summary | `APIUSAGESUMMARY` |
| Assign entity to bank transaction | `ASSIGNENTITYTOBANKTRANSACTION` |
| Billable expense | `BILLABLEEXPENSES` |
| Buy to order | `BUYTOORDERSETUP` |
| Buy-to-order history | `BUYTOORDERHISTORY` |
| COGS closed JE | `COGSCLOSEDJE` |
| Charge payoffs | `CHARGEPAYOFF` |
| Charge payoffs details | `CHARGEPAYOFFENTRY` |
| Check layout | `CHECKLAYOUT` |
| Class group | `CLASSGROUP` |
| Close book log | `CLOSEBOOKS` |
| Comment | `COMMENTS` |
| Compliance definition | `COMPLIANCEDEFINITION` |
| Compliance definition association | `COMPLIANCEDEFASSOCIATIONS` |
| Compliance record | `COMPLIANCERECORD` |
| Compliance record detail | `COMPLIANCERECORDDETAIL` |
| Compliance type | `COMPLIANCETYPE` |
| Cost change history | `COSTCHANGEHISTORY` |
| Cost history | `COSTHISTORY` |
| Cost type | `COSTTYPEPICK` |
| Cost type group | `COSTTYPEGROUP` |
| Cost type group members | `COSTTYPEGRPMEMBER` |
| Cost type or cost type group | `COSTTYPENGROUPPICK` |
| Currency and format setup | `TRXCURRENCIES` |
| Custom renewal amounts | `RENEWALPRICINGOVERRIDE` |
| Data Delivery Service job | `DDSJOB` |
| Doc recalls | `DOCRECALLS` |
| Document params subtotal | `DOCUMENTPARSUBTOTAL` |
| Drop ship | `DROPSHIPSETUP` |
| Drop ship history | `DROPSHIPHISTORY` |
| Dunning invoice | `DUNNINGINVOICE` |
| Dunning notice | `DUNNINGNOTICE` |
| Dunning payor | `DUNNINGCUSTOMER` |
| Electronic receipt | `ELECTRONICRECEIPTS` |
| Electronic receipt detail | `ELECTRONICRECEIPTSITEM` |
| Evergreen template | `EVERGREENMACRO` |
| Financial account | `FINANCIALACCOUNT` |
| Form 1099 box | `IAFORM1099BOX` |
| Form 1099 type | `IAFORM1099TYPE` |
| Generate invoices | `GENINVOICEPREVIEW` |
| Generate invoices preview header | `GENINVOICEPREVIEWHEADER` |
| Generate invoices preview line | `GENINVOICEPREVIEWLINE` |
| Generate invoices preview snapshot invoice | `GENINVOICEPREBILLHEADER` |
| Generate invoices preview snapshot line | `GENINVOICEPREBILLLINE` |
| Generate invoices preview snapshot run | `GENINVOICEPREBILL` |
| Generate invoices run | `GENINVOICERUN` |
| Initial open items | `INITOPENITEMS` |
| Inter-entity default account mapping | `ENTITYACCTDEFAULT` |
| Inter-entity relationship | `IERELATION` |
| Inter-entity relationship (override) | `ENTITYACCTOVERRIDE` |
| Inter-entity setup | `INTERENTITYSETUP` |
| Inter-entity transactions | `IETRECONCILIATIONS` |
| Interactive Custom Report | `CRW` |
| Invoice policy | `GENINVOICEPOLICY` |
| Line items | `TRANSTMPLENTRY` |
| Loan accounts | `LOANACCOUNT` |
| Lock closed period | `STATUTORYREPORTINGPERIOD` |
| Mandate | `MANDATE` |
| Match tolerance details | `THREEWAYMATCHSETUP` |
| Note | `NOTE` |
| Observed percent completed | `OBSPCTCOMPLETED` |
| Offline job queue | `JOBQUEUERECORD` |
| Open book log | `OPENBOOKS` |
| Out of office | `OUTOFOFFICE` |
| PR entry | `PRENTRY` |
| Partner field map | `PARTNERFIELDMAP` |
| Payor aging report | `CUSTAGING` |
| Payor refund | `CUSTOMERREFUND` |
| Payor refund detail | `CUSTOMERREFUNDDETAIL` |
| Payor refund line detail | `CUSTOMERREFUNDENTRY` |
| Payor visibility | `CUSTOMERVISIBILITY` |
| Platform application | `PTAPPLICATION` |
| Primary document details | `PRIMARYDOCDETAILS` |
| Primary document summary | `PRIMARYDOCSUMMARY` |
| Production units | `PRODUCTIONUNITS` |
| Receive payments from bank transactions | `GENERATERECEIPT` |
| Reconciliation match report | `RECONCILIATIONMATCHREPORT` |
| Recurring document entry | `RECURDOCUMENTENTRY` |
| Reporting accounts | `REPORTINGAC` |
| Reporting accounts header | `REPORTINGACHEADER` |
| Run object summary | `RUNOBJECTSUMMARY` |
| Run object summary (depreciation) | `DEPRSCHRUNSUMMARY` |
| Run object summary (GI) | `GIRUNSUMMARY` |
| Run object summary (loan) | `LOANSTATEMENTRUNSUMMARY` |
| Run object summary (revenue txn) | `REVENUETXNRUNSUMMARY` |
| SC item GL group | `SCITEMGLGROUP` |
| Schedule | `SCHEDULE` |
| Scheduled operation | `SCHEDULEDOPERATION` |
| Scheduled operation log | `SCHEDULEDOPERATIONLOG` |
| Standalone PO match doc type map setup | `STANDALONEPOMATCHDOCTYPEMAPSETUP` |
| Subsidiary | `SUBSIDIARY` |
| Subtotal template detail | `POSUBTOTALTEMPLATEDETAIL` |
| Summary by entity | `SUMMARYBYENTITY` |
| Territory group | `TERRITORYGROUP` |
| Territory group member | `TERRITORYGRPMEMBER` |
| Time period | `TIMEPERIOD` |
| TPAR | `TPAR` |
| Transaction rule | `TRANSACTIONRULE` |
| Transaction rule detail | `TRANSACTIONRULEDETAIL` |
| Transaction template | `TRANSTMPLBATCH` |
| Transfer journal entry map | `TRANSFERJOURNALENTRYMAP` |
| Transfers | `TRANSFERHISTORY` |
| Vendor aging report | `VENDAGING` |
| Vendor visibility | `VENDORVISIBILITY` |
| Wells Fargo Payment Manager summary | `WFPMBATCH` |
| Wells Fargo payment request | `WFPMPAYMENTREQUEST` |
