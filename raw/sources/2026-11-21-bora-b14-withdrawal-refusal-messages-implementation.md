# Bora B14: withdrawal refusal messages reach the customer, server errors stay hidden

Date: 2026-11-21
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`). The owner approved B14 on 2026-11-21: "any failed withdrawal message should go back to the frontend except the ones that are server errors" ([decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md)). The owner answered "Yes, B14" when asked whether to move on to it. The repository facts below come from the agent's change, three review rounds and verification. Nothing was committed.

## The gap

- BCL can refuse a withdrawal with HTTP 200 and a body of only `{"Message": ...}`. The backend read only `Status[0].Description`, so the customer got "Failed to withdraw cash".
- Server errors leaked as refusals:
  - BCL's documented refused sign-in (HTTP 400 `{"Message":"Login Failed"}`) and its documented token refusal (`{"Response":403,"Message":"Invalid token"}`) reached the customer as a 400 with that text.
  - BCL's explanation fields were not checked to be text.

## Change (uncommitted)

- New pure helpers in `src/services/bcl/replies.ts`, imported only by the withdrawal code. The shared BCL client is unchanged.
  - `readBclText`: trimmed text, or empty for blank or non-text values.
  - `readBclReason`: `Status[0].Description`, then a top-level `Message`, the same way whatever the HTTP status.
  - `isBclTokenRefusal`: a body with `Response` 403.
  - `isBclAuthFailure`: the sign-in request failed, or the body is BCL's token refusal.
- `verifyWithdrawal.ts`:
  - BCL's text, from either field and under any HTTP status, goes to the customer as a 400.
  - Our own sign-in or token failures, an HTTP 200 token refusal, unreadable replies, timeouts and dropped connections are a hidden 502, logged.
  - A reply with no BCL text keeps the existing 400 "Failed to withdraw cash" (commit cf9af45 design).
  - The record's `failureReason` is never blank; `||` replaced `??`.
- Tried and reverted: making the shared client turn every sign-in failure into a plain error. Verification showed it would strand a KYC submission as SUBMITTED for reconciliation when BCL refused the sign-in, where before it was released so the customer could resubmit. A rule that hid every HTTP 403 was also dropped, because it would hide a real BCL refusal sent with 403.

## Verification

- Full suite (200 suites, 1,751 tests), `yarn build` and Prettier pass.
- Fifteen mutations made tests fail with no type errors. They covered:
  - each helper rule;
  - the 200 token check;
  - text checks;
  - the Description reading on error replies;
  - field order;
  - the blank-reason fallback;
  - any-403 hiding.
- Three review rounds:
  - one reviewer;
  - a two-agent check of the client change, which found the KYC regression and led to the revert;
  - a final end-to-end check against a fake BCL, using the real client, Mongoose casting and the GraphQL error formatter across 47 scenarios.
- All findings in B14's scope were fixed. Two were left out:
  - a success reply with a non-text Description (older code; BCL's documented success is text);
  - a success without a Description skipping the alert (BCL's documented success always has one).

## Raised with the owner, undecided

- In `src/services/bcl/client.ts`, the "retry on 403" response interceptor also runs for the token request itself. A 403 from the token endpoint makes the client wait on its own token request, so every BCL call hangs until a restart. This needs BCL, or an address block in front of it, to answer the sign-in call with 403. BCL documents 400 for a refused sign-in. The reviewer reproduced the hang against a fake BCL. Suggested fix: skip the retry for the sign-in URL.
- Interaction with C23 (app item): once B14 ships, BCL's "Invalid Account Number" reaches the app. The app's current "invalid" match then shows "That verification code is incorrect" until the C23 handoff item ships.
