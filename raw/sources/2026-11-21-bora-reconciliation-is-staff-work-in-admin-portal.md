# Bora: deposit reconciliation is staff work in the admin portal

Date: 2026-11-21
Source: direct owner statement in a Claude Code session on `bora-capital-backend`, right after B12 was reported.

## Context

The agent's B12 report described the hourly Sentry alerts for deposits in `RECONCILIATION_REQUIRED`. It also described `scripts/deposits_production/inspectDeposit.ts` and its README as the current way to decide a case, and said that closing a case meant editing MongoDB by hand. Across B7 and B12, the agent had also added lines to that README about how to correct deposits.

## Owner statement (verbatim, expletives removed)

> wtf are you doing? so you want to send reconciliation issue to sentry and I will have to be the one to do the reconciliation or what? the [...] admin portal should be use for that by the staff not [...] me and this scripts/deposits_production/inspectDeposit.ts. was written for us to figure what was causing the bcl deposit failing not to use it for reconciliation

## Decision

- Staff reconcile deposits in the admin portal. The owner does not, and neither Sentry nor a script is the way to do it.
- Sentry is not where reconciliation cases go.
- `scripts/deposits_production/inspectDeposit.ts` is a diagnostic script. It was written to find out why BCL deposits were failing, not to reconcile deposits.
