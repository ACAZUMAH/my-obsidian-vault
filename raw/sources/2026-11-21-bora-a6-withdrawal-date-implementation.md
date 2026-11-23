# Bora A6: withdrawal date sent in BCL's format

Date: 2026-11-21
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`). The owner approved A6 ("let's fix that") on 2026-11-21 in [the decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md), and later answered "Yes, A6" when asked whether to move on to it. Withdrawal code was touched only because the owner asked for it explicitly. The repository facts below come from the agent's change and its verification in that session. Nothing was committed.

## Change (uncommitted)

- `src/services/transactions/bcl-transactions/verifyWithdrawal.ts` now builds the withdrawal `TransactionDate` as `dayjs().locale('en').format('DD MMM YYYY')` (for example "21 Nov 2026"), instead of `YYYY-MM-DD`. Deposits already send this format.
- The same value is posted to BCL's `addcicashwithdrawal_bcl` and stored on the withdrawal request record (`transactionDate`, a string) for both the SUBMITTED and FAILED outcomes.
- `tests/unit/services/transactions/transactions.spec.ts` now expects "01 Jan 2026" under fake timers at 2026-01-01T12:00Z. It also asserts that the stored SUBMITTED record keeps the date BCL was sent.

## Verification

- Withdrawal and transaction suites, the full suite (199 suites, 1,704 tests), `yarn build` and Prettier pass.
- Putting back the old format makes six withdrawal tests fail.
- One independent reviewer found no defects:
  - nothing in the backend, the customer app or the admin portal reads the stored withdrawal `transactionDate`;
  - `verifyWithdrawal` is the only caller of `addcicashwithdrawal_bcl`;
  - no global dayjs locale is set;
  - the server runs in UTC, which is Ghana's time;
  - `docs/API_DOC.MD` already shows "09 Jan 2026" for withdrawals.

## Notes

- Withdrawal records saved before the change keep `YYYY-MM-DD` dates. Nothing reads them, so that is harmless.
- B10 (admin transactions APIs) should sort and filter on `createdAt` or `submittedAt`, not on this text date, because "DD MMM YYYY" does not sort as text.
