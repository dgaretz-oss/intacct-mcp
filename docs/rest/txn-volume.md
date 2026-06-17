# API Transaction Volume, Concurrency, and Scaling

The Sage Intacct REST API is built on a modern cloud platform that supports elastic scaling to accommodate integrations of varying volumes. To provide predictable throughput, Sage Intacct offers **performance tiers**, each defining entitlements for API transaction volume, concurrent API requests, and concurrent offline processes.

## API Transaction Entitlement

The API transaction entitlements are designed to operationally support anticipated API transaction volume by assigning server resources to companies according to their needs.

- Entitlements apply **only to a company's own integrations and usage**. Transactions from authorized Marketplace Partners, ISV solutions, and Sage Intacct's own applications do **not** count against the entitlement.
- Companies that exceed their monthly entitlement are charged an **overage fee**. Sage Intacct does not block transactions that exceed the entitlement.
- To gain insights about transaction volume, access REST API metrics from your workspace (see REST developer API metrics).

## API Concurrency Entitlement

Sage Intacct implements concurrency limits on REST API calls to prevent any one customer from consuming server resources at the expense of others.

Concurrency does not equate to the number of integrations:
- A single integration can exceed concurrency limits if it supports multiple parallel processes.
- Multiple integrations may safely operate within limits if their requests do not overlap for more than two seconds.

Concurrency is expressed as **application/company**. For example, `6/8` means any single application can use up to 6 API processes at one time, while the company can use up to 8 concurrent API processes total.

## Offline Processes

Sage Intacct limits the number of offline processes per company (used for scheduled transactions, offline reports, etc.). At Performance Tier 1, each company is limited to **1 concurrent offline process**.

Queues for offline processes are shared with other companies. Premium performance tiers offer more offline process concurrency and isolation from other companies, eliminating waits.

## Performance Tiers

| Performance Tier | API Transactions | API Concurrency (app/company) | Offline Process Concurrency |
|-----------------|-----------------|------------------------------|-----------------------------|
| Tier 1 | 100,000 | 6/8 | 1 |
| Tier 2 | 250,000 | 8/10 | 2 |
| Tier 2-500k | 500,000 | 8/10 | 2 |
| Tier 3 | 1,000,000 | 12/15 | 3 |
| Tier 4 | 2,500,000 | 15/20 | 4 |
| Tier 5 (Custom) | >2,500,000 | Custom | Custom |

To learn more about performance tiers and which tier best suits your needs, contact your Sage Intacct account manager.
