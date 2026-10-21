---
type: source
status: active
created: 2026-09-28
updated: 2026-10-16
tags: [bora-capital, grow-wealth, bcl, graphql, portfolio]
sources:
  - ../../raw/sources/2026-09-28-bora-grow-wealth-existing-customer-valuations.md
  - ../../raw/sources/2026-10-16-bora-kyc-repost-and-cash-movement.md
---

# Bora Grow Wealth Existing Customer Valuations

## Source

- Raw file: [Direct requirement and provider contract](../../raw/sources/2026-09-28-bora-grow-wealth-existing-customer-valuations.md)
- Date: 2026-09-28
- Author: User and BCL
- Ingested: 2026-09-28
- Follow-up: [Cash movement statement](../../raw/sources/2026-10-16-bora-kyc-repost-and-cash-movement.md), BCL request and user decision on 2026-10-16.

## Core Claims

- Existing linked BCL customers can read Grow Wealth data after the backend resolves their portfolios through `LinkedPortfolio` and fetches each valuation through `LinkedPortfolioValuation`.
- The public GraphQL contract has two authenticated reads: a grouped dashboard summary and a separate detailed valuation report.
- The authenticated principal supplies customer identity. Public inputs expose only an optional value date; they do not expose user, identity, or portfolio selection.
- New-customer Grow Wealth onboarding and portfolio creation remain deferred.
- A third read, `getMyGrowWealthCashMovementStatement`, takes a linked `portfolioId` and an inclusive `YYYY-MM-DD` range. It calls `LinkedPortfolioCMS` and returns `openingBalance`, `closingBalance`, and `DEBIT`/`CREDIT` entries. Amounts such as "17,636.60" are parsed and dates are UTC midnight; an unlinked portfolio returns null.

## Useful Details

- The dashboard summary groups `MarketValuePortfolioCCY` by `AssetClass`, sums those values into total NAV, and reports each group's percentage of the total.
- The detailed report preserves holding-level product, pricing, purchase, exchange-rate, accrued-interest, and market-value data while normalizing provider names at the service boundary.
- The provider contract uses English `DD MMM YYYY` dates. The app API accepts the repository's established date-only formats and defaults an omitted value date to the current day.
- A customer without a linked local BCL identity receives an empty result while the new-customer flow remains unavailable.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-kyc-supervision-and-statement-update|Bora KYC Supervision And Statement Update]]
- [[bora-canonical-identity-authorization-hermes-chain|Bora Canonical Identity And Authorization Hermes Chain]]

## Contradictions Or Tensions

- Supersedes the earlier service-only Grow Wealth decision because the user has now supplied the valuation contract and explicitly authorized the existing-customer read APIs.
- Does not restore the previously rejected raw-JSON GraphQL design. Provider responses are normalized into typed summary and report contracts.
- The provider response names portfolio-currency market values but does not identify that portfolio currency separately.

## Open Questions

- What provider operations and product rules will support Grow Wealth onboarding and portfolio creation for new customers?
- What should the UI display when a linked portfolio has no valuation rows for the requested date?
