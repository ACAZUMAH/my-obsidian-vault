# Bora B7: deposit double-post guard implemented

Date: 2026-11-21
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`). The owner approved B7 on 2026-11-21 ("7. fix it", in [the decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md)) and later that day asked the agent to load the vault and continue the fixes. The repository facts below come from the agent's change and its verification in that session. Nothing was committed; the owner commits and deploys the backend.

## The bug, as verified in the code before the change

- `applyPaystackStatus` wrote a non-success Paystack answer, and a payment mismatch, with the filter `status != SUCCESSFUL`. That filter also matched a deposit already claimed for BCL posting (`PROCESSING`, `bclSync.status IN_PROGRESS`) while its BCL post was in flight, and set it back to `PENDING`, `ABANDONED` or `FAILED`.
- The claim (`processSuccessfulPaystackDeposit`) matched any `PENDING`, `FAILED` or `ABANDONED` deposit and never checked `bclSync.status`, so the next "success" answer claimed the reopened deposit and posted it to BCL a second time.
- Finalize (`finalizeSuccessfulBclDeposit`) updated by `_id` only. The auto top-up `recordFailure` failed the deposit with `status != SUCCESSFUL`, and failed its goal contribution with no guard at all.

## What changed (uncommitted)

- `src/services/transactions/helpers/index.ts`: `unclaimedDepositFilter` is `status` in `PENDING`, `FAILED` or `ABANDONED` and `bclSync.status` absent. A new deposit is stored with `bclSync: { attemptCount: 0 }`, so `bclSync` itself is never the check.
- The claim, the non-success write, the mismatch write (both through a private `updateUnclaimedDeposit` in `applyPaystackStatus.ts`) and the auto top-up `recordFailure` all use that filter.
- When a guarded write misses, `applyPaystackStatus` re-reads the stored deposit, so the app's status check answers `PROCESSING` instead of the stale `PENDING` it started from. The app shows "Payment not finished" and a Pay button for `PENDING`.
- Finalize matches only `PROCESSING` with `bclSync.status IN_PROGRESS`. Otherwise it throws 409 Conflict, so no goal credit and no customer alert follow, and the existing reconciliation path logs the error.
- `recordFailure` fails the deposit only while it is unclaimed. Only then does it fail the goal contribution, and never over `SUCCESS`.
- One deposit-by-reference read, `getDepositByReference` in `src/services/transactions/transactions/`, replaces four identical queries: the claim miss, `updateUnclaimedDeposit`, the webhook and the webhook retry cron. It is not scoped to an owner, so only trusted payment flows use it.
- `scripts/deposits_production/README.md` (local, untracked): the closing warning now also says never to remove `bclSync.status`. A deposit without it can be claimed and posted to BCL again; one set back to `PENDING` with `bclSync.status` kept is never posted, but the app shows it as unpaid.

## Verification

- Focused suites, the full suite (199 suites, 1,702 tests), `yarn build`, and Prettier on the changed files pass.
- Two new specs match queries with sift, the matcher Mongoose uses, following the existing `otpClientBinding.spec.ts` pattern:
  - `unclaimedDepositFilter.spec.ts` checks the filter against documents built by the real Transaction model.
  - `depositDoublePost.spec.ts` replays the race through the real services. A slow "abandoned" answer lands while the webhook's BCL post is in flight, then the next check gets "success". On the pre-change code the spec fails with two BCL posts and also re-posts a deposit the old bug reopened. On the new code it passes.
- Seven mutations each make tests fail with no type errors: each guard removed in turn, and `bclSync` checked instead of `bclSync.status`.
- A three-lens review (money safety, callers and the app, conventions and tests), with each finding checked by a skeptic, found no defect in the change. The agent still acted on three points: tests on real document shapes, JSDoc accuracy, and one shared read.

## Left to other backlog items

- A deposit left with `bclSync.status IN_PROGRESS` is never claimed again and is not in the hourly alert, which selects only `RECONCILIATION_REQUIRED`. This covers a crash during the BCL post, and any deposit the old bug reopened before this change. B10's "needs reconciliation" view should list every deposit whose `bclSync.status` has been `IN_PROGRESS` longer than the BCL timeout, whatever its `status`.
- B8 is unchanged: an auto top-up can charge again on its next run after a timeout. B11, the hourly Paystack re-check, was blocked on B7 and can now be built.
