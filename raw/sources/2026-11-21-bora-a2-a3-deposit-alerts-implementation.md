# Bora A2 and A3: deposit alerts implemented

Date: 2026-11-21
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`). The owner approved A2 ("let's add that now the alert now going to payment received and awaiting confirmation") and A3 ("bcl sends alert so no need for us alert them again") on 2026-11-21, in [the decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md). After B7 the owner said "move to the next fix". The repository facts below come from the agent's change and its verification in that session. Nothing was committed.

## What the code did before

- No alert was sent when Paystack's success was claimed. `postDeposit` called `transferCash` with `notify: false`.
- After BCL accepted and the deposit was finalized, `syncSuccessfulDepositToBcl` sent `DEPOSIT_SUCCESSFUL` ("Deposit completed") by email, SMS, push and inbox.
- `DEPOSIT_PENDING` ("Deposit request received") existed only inside `transferCash`, which sent it after BCL accepted unless `notify` was false. Its only caller passed `notify: false`, so it was never sent.

## What changed (uncommitted)

- A2: `DEPOSIT_PENDING` is reused for the new alert, so the GraphQL type, inbox, push routing and app sounds stay as they are. Its copy is now:
  - title "Payment received, awaiting confirmation";
  - body "Your payment has been received and your deposit is awaiting confirmation.";
  - email subject "Payment received, awaiting confirmation | Bora Capital Advisors".
- `sendPaymentReceivedNotification` (`src/services/transactions/payment/`) loads the customer and sends that alert with the account, amount, currency and deposit reference. It never throws.
- `applyPaystackStatus` starts it with `Promise.all`, alongside `syncSuccessfulDepositToBcl`, only when this caller won the deposit's claim. It runs after the claim commits and outside the Mongo transaction, so a transaction retry cannot repeat it. The BCL post never waits for it, and its failure is only logged. The inbox item is deduplicated on `DEPOSIT_PENDING:<deposit reference>`.
- A3: `syncSuccessfulDepositToBcl` sends nothing after BCL.
  - `sendDepositSuccessfulNotification` and `payment/bclSync/sendNotification.ts` were deleted.
  - `DEPOSIT_SUCCESSFUL` was removed from `TransactionNotificationType` and the copy constants.
  - In the GraphQL `NotificationsType` it is marked `@deprecated` ("No longer sent; BCL confirms deposits to the customer."), the same way as `SIGNIN_WELCOME_BACK`, so stored inbox items still load.
- `transferCash`'s dead `notify` option and its `DEPOSIT_PENDING` send after BCL accepted were removed, together with `TransferCashOptions`. Bora can no longer send an alert after BCL from that path.
- Codegen changed only two comment lines in `src/common/interfaces/graphql/graphql.ts`.
- Customer app (`bora-frontend-mobile-app`): no change needed. It already routes both `DEPOSIT_PENDING` and `DEPOSIT_SUCCESSFUL` to `/deposit/history` with the branded sound, and refreshes nothing on either.

## Verification

- Full suite (199 suites, 1,704 tests), `yarn build` and Prettier pass. The rendered email was checked: two-line heading, the owner's phrase, then amount, masked account and reference.
- Tests pin that the alert goes out once for a won claim:
  - with the claim committed, outside the claim transaction;
  - while BCL has not answered;
  - never for a lost claim or a non-success answer;
  - never again after BCL;
  - and that its failure neither fails nor changes the deposit.
- The sift-backed race spec checks that three racing checks give one alert.
- Seven mutations each make tests fail with no type errors:
  - the alert awaited before the post;
  - its error escaping;
  - no alert;
  - a missing field;
  - the old wording;
  - the alert after BCL answers;
  - the alert inside the claim transaction.
- A three-lens review (alert semantics, contracts and clients, conventions and tests), with each finding checked by a skeptic, found no defect in the code. It confirmed one test gap: nothing pinned when the alert fires. That gap is now covered. The agent also corrected three doc comments that said "before" the BCL post when the alert runs alongside it.

## For the next frontend handoff (only if the owner wants it there)

- `DEPOSIT_PENDING` now arrives right after the payment is confirmed, titled "Payment received, awaiting confirmation".
- `DEPOSIT_SUCCESSFUL` is deprecated and no longer sent.
- No app change is needed.
