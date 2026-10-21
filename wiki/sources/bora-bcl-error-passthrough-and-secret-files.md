---
type: source
status: active
created: 2026-10-11
updated: 2026-10-11
tags: [bora-capital, bcl, error-handling, graphql, currencies, secrets]
sources:
  - ../../raw/sources/2026-10-11-bora-bcl-error-passthrough-and-secret-files.md
source_date: 2026-10-11
ingested: 2026-10-11
confidence: high
---

# Bora BCL Error Passthrough And Secret-File Boundary

## Source

- Raw file: [Direct user direction and implementation](../../raw/sources/2026-10-11-bora-bcl-error-passthrough-and-secret-files.md)
- Date: 2026-10-11
- Author: User, with agent implementation notes
- Ingested: 2026-10-11

## Core Claims

- Agents must not read `.env` or other secret-bearing files, even to make a live provider call. The user runs credentialed calls (cross-project preference).
- BCL `fetchdata` status codes are unreliable; BCL's `Description` (or `Message`) explains the failure. The backend does not need to model BCL's error shape; it passes that text to the frontend.
- The same rule applies to Grow Wealth.

## Useful Details

- One shared `fetchBclData` (`src/services/bcl/fetchData.ts`) now handles every `/api/partner/fetchdata` call. A BCL rejection becomes a 400 `BAD_REQUEST` that carries BCL's text to the client. A 502 `BAD_GATEWAY` with a hidden message is reserved for an unreachable BCL or an unreadable envelope or rows.
- Grow Wealth `LinkedPortfolio` and `LinkedPortfolioValuation` were moved onto it.
- New authenticated lookups `getCurrencies` (RequestID `Currency`) and `getCurrencyRates` (RequestID `CurrencyRate`, `MM/DD/YYYY` request dates, `DD MMM YYYY` response dates) also use it.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-grow-wealth-existing-customer-valuations|Bora Grow Wealth Existing Customer Valuations]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/personal-operating-manual|Personal Operating Manual]]

## Contradictions Or Tensions

- The project rule that BCL services "retain endpoint-specific success-field handling" still holds across BCL endpoints. Within `fetchdata`, the success and error envelope is now handled in one place, while each domain still owns its request and row shapes.

## Open Questions

- Which direction is the BCL currency rate quoted in? (User is asking BCL.)
- Must rate requests match the customer's KYC currency? (User is asking BCL.)
