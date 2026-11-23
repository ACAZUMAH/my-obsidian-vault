# Bora B10: staff transactions APIs and deposit reconciliation in the admin portal

Date: 2026-11-21
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`).
- The owner approved B10 on 2026-11-21 in [the decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md): "the admin should have a transactions section so see all transactions and the ones that needs reconcilation so let's work on those apis".
- The owner said staff reconcile in the admin portal ([decision](2026-11-21-bora-reconciliation-is-staff-work-in-admin-portal.md)), then answered "go ahead" to building B10.
- Nothing was committed.

## Owner decisions (2026-11-21, chosen on a question card in the session)

- When BCL confirms it does NOT hold a stuck deposit, staff choose between two actions:
  - "Send to BCL again": posts it once, after BCL confirms in writing;
  - "Mark refunded": the customer is refunded instead.
- Refunds happen in the Paystack dashboard. Staff then record the Paystack refund reference in the portal. Bora gets no refund code that moves money.
- The hourly per-deposit Sentry alert for deposits needing reconciliation is removed. Cases show only in the portal list and its count. Sentry keeps only the "BCL still not received" summary, which a developer must act on.
- When BCL confirms it DOES hold the deposit, staff mark it completed with BCL's reference. This was presented as a given, not a choice.

## Change (uncommitted)

- **Permissions:** `transactions.read` (view) and `transactions.reconcile` (close cases), in a new `transactions.*` group. The system Administrator role (`*`) gets them at once; other roles need them added in the role editor.
- **Queries** (`transactions.read`):
  - `getAdminDeposits(filters)`, newest first, filtered by:
    - search on reference, account number or customer email;
    - payment status, BCL status, `reconciliationState` and source;
    - creation date range;
  - `getAdminDeposit(id)`;
  - `getAdminWithdrawals(filters)`: search on account number, status and creation date range; sorted by creation, never by the stored date text;
  - `getAdminTransactionSummary`: real counts of deposits needing reconciliation and of deposits retrying.
- **What the queries return:**
  - Each row has the customer's name, email and phone only.
  - Deposits never return the Paystack checkout link, access code or raw Paystack answers.
  - A completed deposit hides any old failure reason.
- **Mutations** (`transactions.reconcile`), each taking a required staff note:
  - `completeDepositAtBcl`: checks Paystack again, then completes the deposit with BCL's reference (the one on record, or one staff enter; a different one is refused) and credits any goal, in one MongoDB transaction. It shares the normal finalize code.
  - `sendDepositToBclAgain`: checks Paystack again, claims the deposit with one guarded update, and replies at once. The post runs after the reply because BCL can take minutes, longer than the portal waits. The outcome lands as for any post: completed, sent again hourly, or back for staff with BCL's reply.
  - `markDepositRefunded`: needs Paystack's refund reference. It sets the deposit FAILED with the new BCL status `REFUNDED`, which nothing can claim or post again, and fails any goal contribution, in one MongoDB transaction.
- **What counts as a case** ("needs reconciliation"):
  - BCL status `RECONCILIATION_REQUIRED`, whatever the payment status;
  - BCL status `IN_PROGRESS` with the post started more than 10 minutes ago, because a live post ends within about five minutes.
  - `RETRY_PENDING` deposits show as "retrying" and are refused, because the hourly job owns them.
- **Concurrency guard:** each close is guarded on the stored BCL status and the exact last-change time. If the hourly job, a late BCL answer or another staff member changed the deposit, the close is refused with 409: "This deposit changed while you were closing it. Refresh it and check again."
- **Records of staff actions:**
  - Each action is kept on the deposit in `reconciliationHistory`: action, note, references, BCL status before, staff ID and name, time.
  - Each action is also written to the security audit log as `DEPOSIT_RECONCILED`.
- **Alerts:** the hourly job no longer alerts per reconciliation case. `alertBclReconciliation.ts` became `alertUnsentBclDeposits.ts`.
- **Indexes:**
  - deposits: `createdAt`, and `bclSync.status` with `bclSync.lastAttemptAt`;
  - withdrawals: `createdAt`, and `status` with `createdAt`.
  - Mongoose builds them when the app starts.
- **Shared code:**
  - `readPaystackConfirmationProblem` is used by the hourly retry and the staff actions;
  - `buildBclReclaimUpdate` is used by the hourly retry and send-again;
  - `markGoalContributionFailed` (goals) is used by the refund and by the auto top-up failure.
- **Side change:** finalize now removes an old failure reason with `$unset`. Before, `failureReason: undefined` was dropped and cleared nothing.

## Verification

- Full suite (205 suites, 1,871 tests), `tsc`, `yarn build` and Prettier pass.
- The GraphQL permission parity test and new authorization tests pass:
  - a customer and a holder of the other key are refused;
  - every close action is recorded against the signed-in staff member.
- Sift-backed tests run the real guards on stored shapes. They cover:
  - each case state, with the query filter and the reader agreeing;
  - legacy deposits with any status;
  - two staff sending at once, which gives one post and one 409;
  - a change between read and write;
  - a refund racing a completion.
- 18 mutations made tests fail with no type errors. They included:
  - a retrying deposit made closable;
  - the change-time guard dropped;
  - no 10-minute wait;
  - no attempt count;
  - no Paystack check;
  - read permission able to close;
  - the refund unguarded;
  - send-again waiting for BCL;
  - the "nothing to do" filter inverted.
- An independent review raised 11 findings. 6 were confirmed, all low, and 5 refuted.
  - **Fixed:**
    - the refund guard was not really tested;
    - audit events for send-again and refund were not asserted;
    - the contribution-failed write was duplicated outside the goals services;
    - new helpers took positional parameters;
    - the re-claim update was written twice.
  - **Left for the owner:** `scripts/deposits_production/README.md` line 5 and `constants/index.ts` line 1 still point to the removed Sentry alert. That folder is the owner's diagnostic script, which the agent had promised not to touch.
- **Refuted, with reasons:**
  - Blocking send-again or refund when BCL's reference is already stored: a stored reference does not prove BCL still holds the deposit after a reversal, and a refund is recorded after it happened.
  - A refund that later fails at Paystack: it is re-issued in the Paystack dashboard; reopening would risk both a refund and a BCL booking.
  - Pinning default sync guards to the claim: no live post outlasts the 10-minute cut-off.

## Incident during the build

- The agent overwrote `tests/unit/graphql/transactionAuthorization.spec.ts` without reading it first.
- It was restored the same session:
  - from HEAD plus the uncommitted 2026-11-19 `depositCash` removal edit, recovered from that session's transcript;
  - the transcript read was confirmed identical to HEAD;
  - the diff against HEAD is exactly that edit.
- The new staff tests went into `adminTransactionAuthorization.spec.ts`.
- A `git mv` also staged a rename in the index; it was unstaged at once, so nothing is staged.

## Needed elsewhere

- **Admin portal:** the `/finance` placeholder waits for these APIs. The portal must:
  - sync the schema;
  - add the two keys to its permission list `P`;
  - list the new operations in its operation permission table.
- A dated frontend handoff for the admin portal is written only when the owner asks.
