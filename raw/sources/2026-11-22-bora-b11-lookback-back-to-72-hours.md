# Bora B11: re-check look-back back to 72 hours

Date: 2026-11-22
Source: direct owner statement in a Claude Code session on `bora-capital-backend`, right after B11 was reported with a 30-day look-back.

## Owner statement (verbatim)

> You know what the 1 cides production was a test for send it back to 72 hours

## Meaning

- The GH¢1.00 production deposit of 16 Nov 2026 was a test. No real customer deposit from before the live webhook (2026-11-21) needs the hourly Paystack re-check to reach it.
- The owner reversed the earlier choice of 30 days ([B11 evidence](2026-11-22-bora-b11-hourly-paystack-recheck-implementation.md)). The re-check looks back 72 hours.

## Change (uncommitted)

- `RECHECK_FOR_MS` is 72 hours again in `recheckUnconfirmedDeposits.ts`, and its comment records why.
- The window tests are back to 2 days (checked) and 4 days (not checked). A mutation back to 30 days makes them fail.
- Full suite (209 suites, 1,930 tests), `tsc` and `yarn build` pass.
