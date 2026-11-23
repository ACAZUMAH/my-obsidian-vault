# Bora B8: an auto top-up never charges a period twice

Date: 2026-11-21 to 2026-11-22
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`).
- The owner approved B8 on 2026-11-21 ("let's fix it", in [the decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md)), and answered "Yes, B8" when asked to move on to it.
- The item as written: a charge_authorization timeout, or any error after Paystack already returned success, reached `recordFailure`, which marked it failed. The next 5-minute run then charged again with a `-rN` reference, up to three times, while the first charge's webhook still posted to BCL. The fix: verify the previous reference with Paystack before charging again, and treat unknown outcomes as unknown, not failed.
- Nothing was committed.

## Change (uncommitted)

- **Unknown is not failed.** In these cases the auto top-up waits on that charge, with `pendingChargeReference` set and the customer-visible reason "Waiting for Paystack to confirm the last charge":
  - a charge request that errors or times out once it was sent;
  - an error after Paystack returned;
  - a charge Paystack answers as pending, `send_otp`, ongoing or similar;
  - a rerun that finds an earlier run already opened this period's charge.
  Nothing is failed, the failure count does not move, and the period stays due.
- **Settled before any new charge.** On every tick, an auto top-up waiting on a charge settles it first:
  - deposit already booked, or Paystack reports success: book it the way the webhook does, then end the wait; the schedule moves on only if the period is still due, otherwise the date the customer chose is kept;
  - Paystack reports failed, abandoned or reversed, or has had no transaction with the reference for 15 minutes: record a real failure, using Paystack's own refusal message if it gave one; the next tick retries with a new reference;
  - still in progress, or Paystack unreachable: keep waiting.
- **Telling "never charged" from "unknown".** Paystack's verify answers HTTP 400 "Transaction reference not found" for a reference it never had; a bad key gives 401. Verify and charge errors now carry Paystack's HTTP status (`paystackHttpStatus`). `isPaystackReferenceUnknown` accepts only that 400 answer.
- **Duplicate period fix (older bug the review found).**
  - `openContribution` caught the duplicate-key error inside the MongoDB transaction. The server aborts a transaction on a write error, so the driver retried the whole transaction for 120 seconds and then threw.
  - The run then recorded a failure, and the next tick charged the period again.
  - The duplicate is now handled outside the transaction.
- **Claim and selection.** The cron selects, and the claim accepts, an ACTIVE auto top-up only if it is due or waiting on a charge. An overlapping tick therefore cannot charge a period another run just settled.
- **Waiting is tied to ACTIVE:**
  - the waiting state is written only while the auto top-up is still ACTIVE;
  - pausing, cancelling, or a goal status change that moves it out of ACTIVE drops the waiting charge and its message;
  - the old charge is still booked by its webhook if Paystack took it.
- **Shared and moved code:**
  - `advanceAutoTopUpSchedule`, `recordAutoTopUpFailure`, `waitForAutoTopUpCharge` and `resolvePendingAutoTopUpCharge` each have their own file;
  - `NO_WAITING_CHARGE` and the waiting message live in `goals/helpers/autoTopUpWaitingCharge.ts`.
- **Side fix:** advancing the schedule now clears the old failure reason with `null`. Before, `undefined` was dropped by Mongoose and cleared nothing.

## Verification

- Full suite (208 suites, 1,906 tests), `tsc`, `yarn build` and Prettier pass.
- A multi-run harness drives the real cron entry against in-memory state, with the selection, claim and guarded writes matched by sift. Its transactions behave like the MongoDB driver: a swallowed write error cannot commit. It covers:
  - the B8 scenario: a timeout, then Paystack took the money, and the customer is charged once;
  - a webhook booking first;
  - Paystack failed, abandoned or reversed, or never received the charge, followed by a retry with the next reference;
  - Paystack unreachable, a refused key or still in progress, which keep waiting;
  - an amount mismatch;
  - a booking error;
  - pending charge answers;
  - an error after success;
  - a stopped run;
  - "not found" within 15 minutes;
  - a kept refusal reason;
  - a cadence change while waiting;
  - a pause during the run;
  - the three-failure stop;
  - an overlapping tick.
- 17 mutations made tests fail, all compiling and running the full 38 tests. Three first runs had not compiled (a false pass) and were re-run with compiling mutations.
- An independent review raised 13 findings. 7 were confirmed (one high: the duplicate period) and fixed; 3 were refuted.

## Incidents during the build

- The first mutation run was wrapped in the machine-wide job limiter while each check also asks it for a slot, so it deadlocked.
  - It left `processDueAutoTopUps.ts` with a test mutation in place for several minutes.
  - The run was stopped and the file restored from the copy saved before the mutation; the restored file was confirmed identical apart from the mutated lines.
  - Every file the run could touch was then checked; nothing is staged.
  - Lesson: never wrap the mutation driver in the limiter, because each check already uses it.

## Open, not B8

- A charge Paystack keeps reporting in progress keeps its auto top-up waiting with no time limit.
- Auto top-up deposits whose webhook never arrives still depend on B11 (the hourly Paystack re-check, approved, not built).
