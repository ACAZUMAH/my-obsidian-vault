---
type: source
status: active
created: 2026-11-21
updated: 2026-11-23
tags: [bora-capital, backend, mobile, payments, paystack, bcl, withdrawals, notifications, security]
sources:
  - ../../raw/sources/2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md
  - ../../raw/sources/2026-11-21-bora-b7-deposit-double-post-guard-implementation.md
  - ../../raw/sources/2026-11-21-bora-a2-a3-deposit-alerts-implementation.md
  - ../../raw/sources/2026-11-21-bora-a6-withdrawal-date-implementation.md
  - ../../raw/sources/2026-11-21-bora-b14-withdrawal-refusal-messages-implementation.md
  - ../../raw/sources/2026-11-21-bora-b15-withdrawal-amount-format-implementation.md
  - ../../raw/sources/2026-11-21-bora-b12-bcl-reply-and-unsent-deposit-retry-implementation.md
  - ../../raw/sources/2026-11-21-bora-reconciliation-is-staff-work-in-admin-portal.md
  - ../../raw/sources/2026-11-21-bora-b10-staff-transactions-and-reconciliation-implementation.md
  - ../../raw/sources/2026-11-22-bora-b8-auto-top-up-unknown-charge-implementation.md
  - ../../raw/sources/2026-11-22-bora-b11-hourly-paystack-recheck-implementation.md
  - ../../raw/sources/2026-11-22-bora-b11-lookback-back-to-72-hours.md
  - ../../raw/sources/2026-11-22-bora-a1-customer-pays-paystack-fee-implementation.md
  - ../../raw/sources/2026-11-21-bora-handoff-decimal-comma-note.md
  - ../../raw/sources/2026-11-22-bora-frontend-handoff-2026-11-22.md
  - ../../raw/sources/2026-11-22-bora-linked-account-email-case-fix.md
  - ../../raw/sources/2026-11-22-bora-email-kept-as-typed-owner-correction.md
  - ../../raw/sources/2026-11-22-bora-email-as-typed-revert-and-handoff.md
  - ../../raw/sources/2026-11-22-bora-email-case-insensitive-matching.md
  - ../../raw/sources/2026-11-22-bora-remaining-fixes-and-handoff-ready.md
  - ../../raw/sources/2026-11-23-bora-a4-wording-approved-bcl-email-case-deferred.md
  - ../../raw/sources/2026-11-23-bora-bcl-sign-in-403-hang-fix.md
  - ../../raw/sources/2026-11-23-bora-email-matching-and-bcl-fix-committed-and-pushed.md
source_date: 2026-11-21
ingested: 2026-11-21
confidence: high
---

# Bora Deposit And Withdrawal Flow Decisions And Fix Backlog

## Source

- Raw file: [Direct user evidence](../../raw/sources/2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md)
- Raw file: [B7 implementation evidence](../../raw/sources/2026-11-21-bora-b7-deposit-double-post-guard-implementation.md) (repository change and verification, 2026-11-21)
- Raw file: [A2 and A3 implementation evidence](../../raw/sources/2026-11-21-bora-a2-a3-deposit-alerts-implementation.md) (repository change and verification, 2026-11-21)
- Raw file: [A6 implementation evidence](../../raw/sources/2026-11-21-bora-a6-withdrawal-date-implementation.md) (repository change and verification, 2026-11-21)
- Raw file: [B14 implementation evidence](../../raw/sources/2026-11-21-bora-b14-withdrawal-refusal-messages-implementation.md) (repository change and verification, 2026-11-21)
- Raw file: [B15 implementation evidence](../../raw/sources/2026-11-21-bora-b15-withdrawal-amount-format-implementation.md) (repository change and verification, 2026-11-21)
- Raw file: [B12 implementation evidence](../../raw/sources/2026-11-21-bora-b12-bcl-reply-and-unsent-deposit-retry-implementation.md) (repository change and verification, 2026-11-21)
- Raw file: [Reconciliation owner decision](../../raw/sources/2026-11-21-bora-reconciliation-is-staff-work-in-admin-portal.md) (direct owner statement, 2026-11-21)
- Raw file: [B10 implementation evidence and close-action decisions](../../raw/sources/2026-11-21-bora-b10-staff-transactions-and-reconciliation-implementation.md) (owner choices and repository change, 2026-11-21)
- Raw file: [B8 implementation evidence](../../raw/sources/2026-11-22-bora-b8-auto-top-up-unknown-charge-implementation.md) (repository change and verification, 2026-11-22)
- Raw file: [B11 implementation evidence and look-back decision](../../raw/sources/2026-11-22-bora-b11-hourly-paystack-recheck-implementation.md) (owner choice and repository change, 2026-11-22)
- Raw file: [B11 look-back back to 72 hours](../../raw/sources/2026-11-22-bora-b11-lookback-back-to-72-hours.md) (direct owner statement, 2026-11-22)
- Raw file: [A1 implementation evidence and fee decisions](../../raw/sources/2026-11-22-bora-a1-customer-pays-paystack-fee-implementation.md) (owner choices and repository change, 2026-11-22)
- Raw file: [Decimal-comma handoff note](../../raw/sources/2026-11-21-bora-handoff-decimal-comma-note.md) (direct owner statement, 2026-11-21)
- Raw file: [The 2026-11-22 frontend handoff and its check](../../raw/sources/2026-11-22-bora-frontend-handoff-2026-11-22.md) (owner request and repository change, 2026-11-22)
- Raw file: [Linked-account email letter case fix](../../raw/sources/2026-11-22-bora-linked-account-email-case-fix.md) (owner approval and repository change, 2026-11-22)
- Raw file: [Emails kept exactly as typed](../../raw/sources/2026-11-22-bora-email-kept-as-typed-owner-correction.md) (direct owner correction, 2026-11-22)
- Raw file: [Lowercasing reverted, lookups left exact](../../raw/sources/2026-11-22-bora-email-as-typed-revert-and-handoff.md) (direct owner decision and repository change, 2026-11-22)
- Raw file: [Emails matched ignoring letter case](../../raw/sources/2026-11-22-bora-email-case-insensitive-matching.md) (owner reversal, approval and repository change, 2026-11-22)
- Raw file: [Remaining fixes and the handoff made ready](../../raw/sources/2026-11-22-bora-remaining-fixes-and-handoff-ready.md) (owner instruction and repository change, 2026-11-22)
- Raw file: [A4 wording approved, BCL email case deferred, sign-in 403 hang reproduced](../../raw/sources/2026-11-23-bora-a4-wording-approved-bcl-email-case-deferred.md) (direct owner decisions and agent reproduction, 2026-11-23)
- Raw file: [BCL sign-in 403 hang fixed](../../raw/sources/2026-11-23-bora-bcl-sign-in-403-hang-fix.md) (owner approval and repository change, 2026-11-23)
- Raw file: [Email matching and BCL sign-in fix committed and pushed](../../raw/sources/2026-11-23-bora-email-matching-and-bcl-fix-committed-and-pushed.md) (owner instructions and Git results, 2026-11-23)
- Date: 2026-11-19 to 2026-11-21
- Author: Direct user (repository owner) statements in a Claude Code session; repository facts from a read-only, double-checked review of the backend, mobile app and admin portal on 2026-11-20/21
- Ingested: 2026-11-21

## Core Claims

- **Flow (owner decisions, 2026-11-20).** The customer bears the Paystack fee. Bora alerts "payment received, awaiting confirmation" once Paystack confirms and before the BCL post; BCL alerts that the deposit is confirmed and when it reflects on the portfolio; Bora sends nothing after that. For withdrawals Bora alerts "withdrawal initiated" and BCL sends the confirmation and payment alerts. The customer chooses a bank account or Mobile Money wallet for the payout; the owner asked BCL to add payout fields to `addcicashwithdrawal_bcl`, and Bora waits for them. Withdrawal limits belong to BCL.
- **Approved to build (2026-11-21), in the backend unless noted:**
  - customer-pays-fee: surcharge on top of the deposit, the fund settles the exact amount, and the app shows amount, fee and total (needs an app build) (A1), implemented 2026-11-22, uncommitted; the fee is on at deploy and card auto top-ups add it too (owner choices, 2026-11-22);
  - the "payment received, awaiting confirmation" alert after a won claim (A2), implemented 2026-11-21, uncommitted;
  - removing Bora's `DEPOSIT_SUCCESSFUL` "Deposit completed" alert (A3), implemented 2026-11-21, uncommitted;
  - the withdrawal `TransactionDate` in `DD MMM YYYY` (A6), implemented 2026-11-21, uncommitted;
  - the double-post guard (B7), implemented 2026-11-21, uncommitted;
  - verify-before-recharge for auto top-ups (B8), implemented 2026-11-22, uncommitted;
  - admin transactions APIs: all transactions plus a "needs reconciliation" view with a way to close each case (B10), for staff in the admin portal, implemented 2026-11-21, uncommitted;
  - an hourly Paystack re-check of unconfirmed deposits, after B7 (B11), implemented 2026-11-22, uncommitted;
  - storing BCL's reply and retrying requests that never reached BCL (B12), implemented 2026-11-21, uncommitted;
  - passing every failed-withdrawal message to the frontend except server errors (B14), implemented 2026-11-21, uncommitted;
  - format-only validation of withdrawal amounts (B15), implemented 2026-11-21, uncommitted.
- **Who reconciles (owner decision, 2026-11-21).** Staff reconcile deposits in the admin portal (B10), not the owner. Sentry is not a reconciliation channel. `scripts/deposits_production/inspectDeposit.ts` is a diagnostic script written to find out why BCL deposits failed, not a reconciliation tool ([owner's words](../../raw/sources/2026-11-21-bora-reconciliation-is-staff-work-in-admin-portal.md)).
- **Closing a stuck deposit (owner choices, 2026-11-21).** BCL holds it: staff complete it with BCL's reference. BCL does not hold it: staff choose to send it to BCL again (after BCL confirms in writing) or mark it refunded. Refunds are made in the Paystack dashboard and only recorded in Bora with Paystack's refund reference. The hourly per-deposit Sentry alert is removed; cases show only in the portal ([evidence](../../raw/sources/2026-11-21-bora-b10-staff-transactions-and-reconciliation-implementation.md)).
- **Frontend handoff items** (next dated handoff): the deposit result copy (A4); show "That verification code is incorrect" only for the server's own code errors, and BCL's refusal text otherwise (C23); the fee breakdown (A1); later, the payout step (A5). For the admin portal: the B10 APIs for its `/finance` page (schema sync, the `transactions.read` and `transactions.reconcile` keys, and the new operations). Owner decision (2026-11-21): also tell the frontend developer, as an app-only side note, that on a decimal-comma keyboard the withdrawal amount "500,50" becomes 50050, which the confirm screen shows as 50,050 before the customer confirms ([owner's wording](../../raw/sources/2026-11-21-bora-handoff-decimal-comma-note.md)). Written on 2026-11-22 as `docs/frontend-handoff-2026-11-22.md` (uncommitted, not sent). It covers A1, A4, C23 with B14, the Oye limits, the B10 portal APIs and the no-change items, but not A5, which is not built. It also covers the 2026-11-19/20 audit fixes clients can see, which had never been handed off. The A4 wording in it is the agent's proposal ([evidence](../../raw/sources/2026-11-22-bora-frontend-handoff-2026-11-22.md)).
- **Decided, never re-raise:**
  - deploys happen in an announced maintenance window with customer actions blocked (B9);
  - BCL always answers a withdrawal, so "BCL recorded it but never replied" is noise (B13);
  - failed and finished withdrawals are covered by the mini statement and transactions (B16);
  - support staff reading customer KYC through the API is accepted, because the same staff verify KYC and answer customers about it (C17);
  - the support-case API exposing staff fields is accepted while the app does not show them (C18);
  - Sentry quota (C20) skipped;
  - log redaction (C21) dropped, because logs the owner has seen show no sensitive data;
  - Docker: the project does not use it, so never raise Docker items (C22).
- **Earlier owner decisions (2026-11-19/20), implemented in the uncommitted backend working tree:**
  - one shared signup code;
  - existing-investor linking only after the emailed code is used, with matching BCL email and phone;
  - the BCL check at signup;
  - GraphQL depth 5 with the in-house counter and size caps, and GET operations refused;
  - WebSocket messages capped at 64 KB;
  - Oye limited to 10 a minute, 100 a day and 2,000 characters;
  - separate recovery-code cooldown, no cooldown for withdrawal and wallet codes;
  - sign-in kept at 5 attempts per phone per 15 minutes.

## Useful Details

- B7 fix shape: a non-success Paystack answer may change only a deposit that was never claimed. The claim requires `bclSync.status` to be absent; checking `bclSync` alone is not enough, because `bclSync.attemptCount: 0` is created by default. Finalize requires `PROCESSING` with `bclSync IN_PROGRESS`, and auto top-up `recordFailure` gets the same guard.
- B7 as built (2026-11-21, uncommitted): one shared `unclaimedDepositFilter`; a missed guarded write re-reads the stored deposit so the app sees `PROCESSING`, not a stale `PENDING`; finalize answers 409 when the claim no longer stands; `recordFailure` fails the goal contribution only after failing an unclaimed deposit, never over `SUCCESS`; one shared `getDepositByReference` read. Sift-backed specs replay the race through the real services and fail on the pre-B7 code. See [the B7 evidence](../../raw/sources/2026-11-21-bora-b7-deposit-double-post-guard-implementation.md).
- B10 design note: the "needs reconciliation" view should also list deposits left `PROCESSING` with `bclSync IN_PROGRESS` past the 100-second BCL timeout, because a crash or platform restart can leave them there even outside deploys. Since B7 (agent inference from the B7 review), it should list every deposit whose `bclSync.status` has been `IN_PROGRESS` past that timeout whatever its `status`, which also covers any deposit the old bug reopened: B7 never claims such a deposit again, and the hourly alert selects only `RECONCILIATION_REQUIRED`. Withdrawal lists should sort and filter on `createdAt` or `submittedAt`, never on the stored `transactionDate` text: since A6 it is "DD MMM YYYY", which does not sort as text, and older records hold `YYYY-MM-DD` (agent inference from the A6 review).
- B10 and B12 (agent inference from the B12 build): the view should show `RETRY_PENDING` deposits apart from manual cases, as "being sent again every hour", with BCL's stored reply (`bclSync.lastReply`) and the attempt count. Closing a case by hand must never touch a `RETRY_PENDING` deposit, because the hourly job may post it.
- A2 and A3 as built (2026-11-21, uncommitted): the existing `DEPOSIT_PENDING` type carries the new alert, so the app needs no change; its title is "Payment received, awaiting confirmation" (the exact wording stays the owner's to change). It is started with `Promise.all` alongside the BCL post, only when the caller won the claim, outside the Mongo transaction, and never throws. Nothing is sent after BCL: `DEPOSIT_SUCCESSFUL` is deprecated in the schema (old inbox items still load), its senders are deleted, and `transferCash`'s dead after-BCL `notify` path is gone. See [the A2 and A3 evidence](../../raw/sources/2026-11-21-bora-a2-a3-deposit-alerts-implementation.md).
- B14 as built (2026-11-21, uncommitted): BCL's own text (`Status[0].Description`, then `Message`, trimmed, whatever the HTTP status) reaches the customer as a 400. BCL refusing our sign-in or access token, unreadable replies, timeouts and dropped connections are a hidden 502. The pure helpers live in `src/services/bcl/replies.ts` and only the withdrawal code uses them; the shared BCL client is unchanged. An attempt to change the client was reverted because it would have stranded KYC submissions. See [the B14 evidence](../../raw/sources/2026-11-21-bora-b14-withdrawal-refusal-messages-implementation.md).
- B15 as built (2026-11-21, uncommitted): `requestWithdrawal` first checks the amount format with `validateWithdrawalAmount`. It accepts a plain number greater than zero with up to two decimal places, and refuses anything else with a 400 before saving or sending anything. It checks the format only; limits stay with BCL. Every amount the app can produce passes. See [the B15 evidence](../../raw/sources/2026-11-21-bora-b15-withdrawal-amount-format-implementation.md).
- B12 as built (2026-11-21, uncommitted): every BCL deposit failure now stores BCL's reply in `bclSync.lastReply` (HTTP status, body up to 2,000 characters, or the error), and a finalize failure after BCL accepted also stores BCL's ERP reference. A post BCL certainly never received (refused connection, unknown host, no access token, BCL refusing our sign-in or token) waits in the new `RETRY_PENDING` status, still claimed, and the hourly reconciliation job checks it with Paystack again and posts it, up to 25 posts in all (about a day); then it becomes a manual case. Timeouts, dropped connections and every other BCL answer stay manual cases. One hourly summary alert names deposits still waiting after 3 posts, with BCL's last reply; they must never be posted by hand. See [the B12 evidence](../../raw/sources/2026-11-21-bora-b12-bcl-reply-and-unsent-deposit-retry-implementation.md).
- B10 as built (2026-11-21, uncommitted): `transactions.read` gives `getAdminDeposits`, `getAdminDeposit`, `getAdminWithdrawals` and `getAdminTransactionSummary`; `transactions.reconcile` gives `completeDepositAtBcl`, `sendDepositToBclAgain` and `markDepositRefunded`, each with a required staff note. A case is a deposit with BCL status `RECONCILIATION_REQUIRED`, or `IN_PROGRESS` started more than 10 minutes ago, whatever its payment status; `RETRY_PENDING` shows as retrying and cannot be closed. Completing and sending again check Paystack first; every close is guarded on the stored BCL status and exact last-change time (409 if anything changed), kept on the deposit in `reconciliationHistory` and audited as `DEPOSIT_RECONCILED`. A refund sets FAILED with the new BCL status `REFUNDED`, which can never be posted. Send again replies at once and posts after. See [the B10 evidence](../../raw/sources/2026-11-21-bora-b10-staff-transactions-and-reconciliation-implementation.md).
- B8 as built (2026-11-22, uncommitted): an auto top-up charge whose outcome is unknown (request error or timeout after sending, an error after Paystack answered, a pending-type answer, or a rerun of an opened period) is never failed. The auto top-up waits on it (`pendingChargeReference`, "Waiting for Paystack to confirm the last charge") and settles it with Paystack before any new charge: taken means booked like a webhook and the wait ends; failed, abandoned, reversed, or no Paystack transaction 15 minutes after the charge means a real failure and a retry; anything else keeps waiting. The review also fixed an older bug: a duplicate period swallowed inside the MongoDB transaction made the driver retry for 120 s, then the period was charged again. Only due or waiting auto top-ups are selected and claimed; leaving ACTIVE drops a waiting charge. See [the B8 evidence](../../raw/sources/2026-11-22-bora-b8-auto-top-up-unknown-charge-implementation.md).
- B11 as built (2026-11-22, uncommitted): the hourly reconciliation job asks Paystack about deposits still PENDING or ABANDONED and never claimed, started between 72 hours and 15 minutes ago (the owner first chose 30 days, then reversed it on 2026-11-22: the only pre-webhook production deposit, GH¢1.00 on 16 Nov, was a test; [owner's words](../../raw/sources/2026-11-22-bora-b11-lookback-back-to-72-hours.md)), 50 per run, least recently checked first. A payment Paystack took is booked exactly as the webhook books it (one BCL post through the B7 claim, one customer alert); a final failed or abandoned answer is recorded once; anything else changes nothing. See [the B11 evidence](../../raw/sources/2026-11-22-bora-b11-hourly-paystack-recheck-implementation.md).
- A1 as built (2026-11-22, uncommitted): one quote for every path, fee = ceil(deposit × 195 ÷ 9805) + 1 pesewa (GH¢100 is charged GH¢102.00, GH¢1,000 is charged GH¢1,019.90). Checkout, goal top-ups and card auto top-ups ask Paystack for the total with `bearer: 'account'` and `transaction_charge` = fee, so Bora's main account pays Paystack out of the fee and the fund settles exactly the deposit; BCL and goals get the deposit. Paystack's amount is checked against `chargedAmountInSubunit` (older deposits against their amount), Paystack's own fee is kept, the app gets `getDepositFeeQuote` and amount/fee/total on the checkout and payment-check replies and on `AutoTopUp`, and staff see the fee and total. The owner confirms settlement with one small live deposit after deploy. See [the A1 evidence](../../raw/sources/2026-11-22-bora-a1-customer-pays-paystack-fee-implementation.md).
- Raised with the owner, undecided (2026-11-21): a 403 on BCL's sign-in call makes the BCL client wait on its own token request, so every BCL call hangs until a restart. The suggested fix is to skip the 403 retry for the sign-in URL. Reproduced on 2026-11-23 (two calls still waiting after 3 s, one request sent; with the fix both fail at once and each signs in afresh) ([evidence](../../raw/sources/2026-11-23-bora-a4-wording-approved-bcl-email-case-deferred.md)). Approved and fixed the same day, committed as `6f053be` and pushed: the retry skips the sign-in request ([evidence](../../raw/sources/2026-11-23-bora-bcl-sign-in-403-hang-fix.md)). Once B14 ships, BCL's "Invalid Account Number" reaches the app, which shows "That verification code is incorrect" until C23 ships.
- Possible frontend handoff line (in the 2026-11-22 handoff's no-change section): `DEPOSIT_PENDING` now arrives right after payment as "Payment received, awaiting confirmation", and `DEPOSIT_SUCCESSFUL` is deprecated and no longer sent. The app needs no change.
- A4 proposal (the sent handoff's fuller wording was approved by the owner on 2026-11-23, [evidence](../../raw/sources/2026-11-23-bora-a4-wording-approved-bcl-email-case-deferred.md)):
  - `SUCCESSFUL`: "Deposit successful. You'll get a confirmation message when it reflects on your portfolio."
  - server-returned `PROCESSING`: "Payment received, awaiting confirmation".
  - Keep the neutral "checking your payment, do not pay again" wording for the `PROCESSING` the app invents after client errors.
  - Avoid the word "BCL", because the app hides backend messages that contain it.
- The withdrawal `Comment` is always the literal "Withdrawal" (the app has no note box); the BCL flow document must say so.
- Fee math: with surcharge `S = ceil(A·r/(1−r))` on deposit `A` (in pesewas), `S ≥ r·(A+S)`, so Bora's share always covers Paystack's fee. At `r = 0.0195`, GH¢1.00 is charged GH¢1.02 and GH¢100.00 is charged GH¢101.99.
- C19, owner questioned, not approved. Explanation given: Express reads and parses up to 5 MB of body before any login check, so a logged-out request is refused only after it has been read.
- The Paystack live webhook URL is now configured (owner, 2026-11-21).

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]: deposit and withdrawal processing, alerts, reconciliation, admin transactions APIs, and the audit decisions.
- [[../projects/bora-capital-mobile-app|Bora Capital Advisors Mobile App]]: fee display, deposit result copy, withdrawal error mapping, and the future payout step.
- [[bora-accepted-risks-deposit-path-and-api-domain|Bora Accepted Risks, Deposit Path, And API Domain]]: the 2026-11-19 accepted risks this record extends; its open webhook item is now resolved.

## Contradictions Or Tensions

- Supersedes the backend page's "deposit initialization must always route through the real configured subaccount with the subaccount as fee bearer". The customer now bears the fee; the subaccount routing itself stays.
- Supersedes the 2026-08-28 choice to send the withdrawal `TransactionDate` as `YYYY-MM-DD`; the owner approved BCL's `DD MMM YYYY`, built on 2026-11-21 (uncommitted; [evidence](../../raw/sources/2026-11-21-bora-a6-withdrawal-date-implementation.md)). Withdrawal records saved before it keep `YYYY-MM-DD` dates; nothing reads the field.
- Supersedes the backend page's "Separate signup channel codes prove ownership of both registered contacts". The owner chose one shared code on 2026-11-19.
- The BCL flow document lists a "Payout account" field that BCL's API does not yet accept; it depends on BCL adding the fields.

## Open Questions

- ~~What exact deposit result wording does the owner want in the app (A4)?~~ Answered 2026-11-23: the wording in `docs/frontend-handoff-2026-11-22.md` section 2 is approved ([evidence](../../raw/sources/2026-11-23-bora-a4-wording-approved-bcl-email-case-deferred.md)).
- Undecided (found while checking the 2026-11-22 handoff):
  - The Oye cap of 2,000 characters breaks current app builds, which send up to 6,000 characters of history in the prompt. Settled: the cap stays, and the app fits its prompt to it (handoff section 4).
  - Linked accounts store BCL's email letter case, so password recovery fails for a BCL email with capitals. The agent's lowercasing fix ([evidence](../../raw/sources/2026-11-22-bora-linked-account-email-case-fix.md)) was rejected by the owner ([owner correction](../../raw/sources/2026-11-22-bora-email-kept-as-typed-owner-correction.md)). BCL keeps emails exactly as typed, and neither Bora nor the app may change their case. Resolved the owner's way ([decision and revert](../../raw/sources/2026-11-22-bora-email-as-typed-revert-and-handoff.md)): the lowercasing is reverted (uncommitted), lookups stay exact, and the handoff tells the app to stop lowercasing emails. Reversed later the same day ([evidence](../../raw/sources/2026-11-22-bora-email-case-insensitive-matching.md)): emails stay stored as typed, but every lookup ignores letter case through the `email_ci_1` collation index, because production stored every customer email lowercase. Committed as `1ab2559` and pushed 2026-11-23 ([evidence](../../raw/sources/2026-11-23-bora-email-matching-and-bcl-fix-committed-and-pushed.md)); `docs/frontend-handoff-2026-11-22-emails.md` times the app change after this backend.
  - A refunded goal top-up showed "Refunded to the customer; not booked at BCL" in the customer's goal history. Fixed, uncommitted: it now shows "Refunded to you. This top-up was not invested." ([evidence](../../raw/sources/2026-11-22-bora-remaining-fixes-and-handoff-ready.md)).
  - `limit: null` returned 1 row. Fixed, uncommitted: it now gives the default page size.

  See [the evidence](../../raw/sources/2026-11-22-bora-frontend-handoff-2026-11-22.md).
- When will BCL enable production deposits and withdrawals, explain the stuck 16 Nov deposit (a GH¢1.00 test, owner 2026-11-22), and add the payout fields?
- Undecided: the admin portal's broken fund pages (`navHistory`, `SetFundVisibility`), the portal's missing fact-sheet PDF upload and journey editor, the withdrawal alert without "GHS", and a withdrawal code SMS that states what it approves.
