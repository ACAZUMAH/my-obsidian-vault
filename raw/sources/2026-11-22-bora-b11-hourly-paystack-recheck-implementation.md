# Bora B11: hourly Paystack re-check of deposits never confirmed

Date: 2026-11-22
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`).
- The owner approved B11 on 2026-11-21 ("let's fix it then, I have already added the webhook to paystack", in [the decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md)).
- The item as written: nothing re-checks PENDING or ABANDONED deposits with Paystack, and auto top-ups rely on the webhook alone. A sweep is safe only after B7, which is built.
- The owner answered "Yes, B11" when asked to move on to it.
- Nothing was committed.

## Owner decision (2026-11-22, chosen on a question card)

- **Question asked:** the re-check first looked back 72 hours. Before the live webhook (set 2026-11-21), a paid deposit stayed PENDING unless the app finished checking, so an older one would never be found. Widening is safe unless someone credited a deposit at BCL by hand while Bora still showed it pending, because it would then be posted again.
- **Answer:** "30 days (Recommended)". That option was offered for the case where nothing was credited at BCL by hand while Bora still showed it pending. The other options were keeping 72 hours, or a read-only production count first.

## Change (uncommitted)

- **New stage.** `recheckUnconfirmedDeposits` runs in the hourly reconciliation job (minute 15). The order is: Paystack webhook retries, then this re-check, then the BCL retry, then the "BCL still not received" alert.
- **What it selects:** deposits still PENDING or ABANDONED, never claimed for BCL (no `bclSync.status`), started between 30 days and 15 minutes ago. It takes 50 per run, least recently checked first (new `paystackCheckedAt`).
- **Paystack took the payment:** the deposit is booked through `applyPaystackStatus`, exactly as the webhook books it. The atomic claim (B7) lets one caller post it to BCL even if the webhook or the customer's check arrives at the same time. The customer gets the "payment received" alert once.
- **Final "failed" or "abandoned"** that the deposit does not show yet: recorded once, so a failed deposit leaves the list.
- **Anything else** (in progress, pending, reversed): nothing changes.
- **Errors:**
  - Paystack errors and booking errors are logged as warnings, and the run carries on with the next deposit.
  - A deposit with a different amount is failed and reported by `applyPaystackStatus`, as before.
- **Marking a deposit checked:** applies only to a deposit still unclaimed, with `timestamps: false`, so its last-change time and any claim or staff guard are untouched.

## Verification

- Full suite (209 suites, 1,931 tests), `tsc`, `yarn build` and Prettier pass.
- **Filter tests** match the real model documents for:
  - PENDING or ABANDONED, inside the window;
  - 10 minutes old, 31 days old, failed, completed, claimed and refunded, all excluded.
- **Behaviour tests:**
  - booking a success;
  - success on a checkout first seen as abandoned;
  - which answers get recorded;
  - carrying on after errors;
  - rotating the batch.
- **End-to-end tests on the real claim and BCL code:**
  - a lost webhook, booked once while the webhook arrives during the BCL post;
  - an abandoned checkout paid later, posted once.
- **Job order:** the re-check runs after the webhook retries and before the BCL retry.
- **Mutations:** 16 made tests fail with no type errors, all running the full test set. Two were first run from zsh, which passed the test paths as one argument and found no tests; they were re-run from bash.
- **Independent review:** 6 findings, 2 confirmed:
  - the 72-hour window could not reach deposits paid before the webhook existed; the owner chose 30 days;
  - a missing test for success on an abandoned checkout; added.
  - 4 were refuted.

## Open, not B11

- A deposit Paystack reports as failed for an auto top-up whose waiting charge was dropped leaves its goal contribution PENDING. This is an older gap in the shared `applyPaystackStatus`; B11 does not make it worse.
