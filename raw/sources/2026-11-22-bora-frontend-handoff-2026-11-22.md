# Bora: the 2026-11-22 frontend handoff and what checking it found

Date: 2026-11-22
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`).
- The owner answered "Yes, write it" when asked whether to write the dated frontend handoff for the app and the admin portal.
- The handoff file is uncommitted and has not been sent.
- No backend code was changed.

## The handoff

File: `docs/frontend-handoff-2026-11-22.md` in `bora-capital-backend`. It is a new dated file, as the handoff rules require; the 2026-11-12 file was not touched.

**Scope.** Every backend change since the 2026-11-12 handoff that the customer app or the admin portal can see. That includes the uncommitted 2026-11-19/20 audit fixes (sign-up, account linking, Oye limits, request limits, the `depositCash` removal), which had never been handed off.

**Code references.** App line numbers refer to `develop` at `3438237`, and portal line numbers to `develop` at `b2ed428`. Both local checkouts were stale (the app 15 commits behind, the portal 8), so they were read with `git show` and never changed.

**Sections:**

1. **The customer pays the Paystack fee (A1).** Covers:
   - `getDepositFeeQuote`;
   - amount, fee and total on the checkout, top-up and payment-check replies and on `AutoTopUp`;
   - where the app shows a payment: deposit review, goal top-up, auto top-up setup and list, the goal screens' "Next payment", and Home's pending deposit card.

   "Total Investment" stays the deposit.
2. **Deposit result wording (A4).** Covers:
   - the `SUCCESSFUL` and server-returned `PROCESSING` copy;
   - keeping the neutral copy for the `PROCESSING` the app sets itself;
   - Home's pending deposit card;
   - a paid deposit that ends `FAILED` after staff record a refund.

   The wording is the agent's proposal; the owner had not answered the A4 wording question.
3. **Withdrawal refusals show BCL's reason (B14, C23).** Covers:
   - "That verification code is incorrect" only for the server's own three code errors;
   - BCL's reason shown as written, with the code checked before the text;
   - after a BCL refusal, the customer starts a new withdrawal.
4. **Oye limits** (2026-11-20 decision): 10 a minute, 100 a day, 2,000 characters.
5. **Admin portal: the B10 staff transactions and reconciliation APIs.** Covers:
   - permissions and schema;
   - paging, date and search rules;
   - the three close actions and their refusals;
   - the portal's `/finance` placeholders.

   It replaces the different contract in the portal's own `docs/backend-handoff.md`.
6. **Changes that need no client change:**
   - the deposit alerts (A2, A3);
   - sign-up refusing a BCL investor;
   - "Link your account";
   - code cooldowns;
   - request limits;
   - the `depositCash` removal;
   - the withdrawal amount format (B15) and date (A6);
   - auto top-up charges whose outcome is unclear (B8).

**Also included:** the owner's decimal-comma side note, near-verbatim. The figures were corrected: the amount screen shows 50,050 and the confirm screen 50050.

**Release order stated in the handoff:**
- The fee starts when the backend deploys.
- Current builds misword some BCL refusals until section 3 ships.
- Oye breaks on current builds until section 4 ships.
- The portal ships after the backend.

**Left out:** the payout step (A5), because it is not built and waits on BCL's payout fields.

## Verification

Two read-only subagents checked client impact (app and portal). A seven-agent workflow then checked the handoff:
- six checkers tried to disprove every claim (306 claims), one of them for completeness against the full uncommitted diff;
- a skeptic re-checked every finding marked wrong or incomplete.

**Results:**
- 20 findings were upheld and fixed in the handoff, including:
  - the mutation is `verifyWithdrawal`, not `withdrawCash`;
  - server failures used to arrive as `BAD_REQUEST` `Login Failed`;
  - the auto top-up schedule summary never renders;
  - missing app types and the fee quote query;
  - the "Next payment" and pending deposit card amounts;
  - the withdrawal code screen strands the customer after a BCL refusal;
  - missing staff refusal messages;
  - time zones in date filters;
  - search rules.
- 5 findings were rejected.
- 14 minor corrections were applied.

## Findings for the owner (not in the handoff; undecided)

- **Oye cap and app history.** The backend refuses a `prompt` over 2,000 characters. The app sends the conversation history inside the prompt (`MAX_PROMPT_CHARS = 6_000`), so on current builds a typical conversation fails from about its third message, showing "Unable to reach Bora Assistant". The handoff tells the app to fit 2,000. The alternative is a higher backend cap.
- **Email letter case breaks password recovery for linked investors.** This comes from the uncommitted 2026-11-19/20 linking change.
  - Accounts opened by "Link your account" now store BCL's `PrimaryEmail` with its capitals.
  - `forgetPassword` finds the account by exact email (`getUserByEmail`, no collation), and the app lowercases the email.
  - So a linked customer whose BCL email has capitals gets "account not found" and cannot recover their password.
  - Fix in the backend: store the email lowercased, or look it up ignoring case.
- **Refund reason shown to customers (B10).** `markDepositRefunded` writes "Refunded to the customer; not booked at BCL" to the goal contribution's `failureReason`. The customer app shows that text in the goal history. The suggested fix is customer wording on the contribution, keeping the BCL wording only on the staff-side deposit; the alternative is a handoff line telling the app not to show it.
- **`limit: null` returns 1 row.** The shared `getSanitizeLimit` turns `null` into 1. This is older code. The handoff tells the portal to leave `limit` out.
