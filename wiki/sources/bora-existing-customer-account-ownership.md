---
type: source
status: active
created: 2026-10-12
updated: 2026-10-12
tags: [bora-capital, backend, accounts, bcl, authorization]
sources:
  - ../../raw/sources/2026-10-12-bora-existing-customer-account-ownership.md
source_date: 2026-10-12
ingested: 2026-10-12
confidence: high
---

# Bora Existing-Customer Account Ownership

## Source

- Raw file: [Review item, inspection, and user decision](../../raw/sources/2026-10-12-bora-existing-customer-account-ownership.md)
- Date: 2026-10-12
- Author: User-supplied review item (CAL-05), repository inspection, and the user's design approval
- Ingested: 2026-10-12

## Core Claims

- Account ownership for transactions (`userOwnsAccount`) is a local check against `User.portfolioAccountNumbers`. That list is a cache of accounts BCL has confirmed for the user's `identityId`.
- The cache fills when an account is opened in the app, at existing-customer onboarding, and on every BCL account read (`getCISPortfolioAccounts`, `getCISPortfolioAccountsWithNav`, `getCISPortfolioAccount`). Reads use `rememberPortfolioAccountNumbers`, which only adds and never fails the read.
- Before this, existing clients could list their accounts but were blocked from deposits, transfers, withdrawals, goals, and transaction history.

## Useful Details

- Saving on reads covers customers who onboarded earlier and accounts opened outside the app, with no extra BCL calls and no backfill script.
- `resetPasswordWithCode` was split: `setPasswordWithCode` returns the updated user and is used by existing-customer onboarding.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]

## Contradictions Or Tensions

- The review asked to merge a CAL-05 fix, but no such fix existed in any branch, stash, or worktree; it was built instead.

## Open Questions

- Should accounts BCL no longer returns ever be removed from the cache? The current choice is add-only, relying on BCL to reject transactions on closed accounts.
