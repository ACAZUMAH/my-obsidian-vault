# Bora B12: BCL's reply stored, and deposits BCL never received sent again hourly

Date: 2026-11-21
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`). The owner approved B12 on 2026-11-21 in [the decision list](2026-11-21-bora-deposit-withdrawal-flow-decisions-and-fix-backlog.md). The item as written: BCL's actual reply was not saved on the deposit, only a fixed text, which is why BCL's reason for the 16 Nov deposit could not be seen; and a short BCL outage made every deposit in that window a manual case, even ones BCL never received. The owner then answered "let's move to the next" when B12 was next in the saved order. Nothing was committed.

## Change (uncommitted)

- `src/services/bcl/replies.ts` (the B14 helper file) gains two helpers.
  - `isBclNotReached(error)` is true only when the post certainly never reached BCL:
    - any non-axios error, which the client throws before sending, such as having no access token;
    - BCL refusing our sign-in or access token (`isBclAuthFailure`);
    - no response with `ECONNREFUSED`, `ENOTFOUND` or `EAI_AGAIN`.
  - Timeouts and dropped connections do not count, because BCL may have recorded the deposit.
  - `describeBclReply` keeps the HTTP status, the body (at most 2,000 characters) or the error code and message, and the time.
- `transfer.ts` (`transferCash`): the thrown 400 now carries `bclReply` and `bclNotReached`. When BCL answered, only its access-token refusal counts as not reached. The message is BCL's own text, then the error message.
- New `BclSyncStatus.RETRY_PENDING` and a `bclSync.lastReply` field (`httpStatus`, `body`, `error`, `at`) on the transaction model.
- `bclSync/markPostFailure.ts` (`markBclPostFailed`): a post BCL never received, with attempts left, goes to `RETRY_PENDING`.
  - The deposit stays `PROCESSING` and stays claimed, so no Paystack answer can post it (the B7 rule holds).
  - Its reason is "BCL did not receive the deposit; it is sent again every hour", and BCL's reply is stored.
  - Anything else goes to manual reconciliation (`RECONCILIATION_REQUIRED`).
  - The write is guarded on `PROCESSING` with `bclSync IN_PROGRESS`.
- `bclSync/constants.ts`:
  - `BCL_POST_MAX_ATTEMPTS = 25`, the first post plus 24 hourly retries, about a day; after that the deposit becomes a manual case;
  - `BCL_POST_ALERT_AFTER_ATTEMPTS = 3`.
- `bclSync/markReconciliation.ts` now stores BCL's reply in `bclSync.lastReply`. When BCL accepted the deposit but the local finalize failed, it also stores BCL's `bclErpReffID`, so the case can be decided without guessing.
- New `reconciliation/retryUnsentBclDeposits.ts`, run by the existing hourly reconciliation job (`15 * * * *`) after the Paystack webhook retries and before the alerts. Each run takes up to 25 `RETRY_PENDING` deposits, oldest attempt first.
  - Each deposit is checked with Paystack again; the fresh Paystack data also carries the payment details the finalize step saves.
  - If Paystack no longer confirms it, or the amount, currency or reference differ, it goes to reconciliation and is not posted.
  - Otherwise it is taken back with one atomic update guarded on `RETRY_PENDING`: `IN_PROGRESS`, `lastAttemptAt`, attempt count plus one, and the waiting reason removed. Then it is posted. It is posted at most once per take.
  - If Paystack cannot be reached, the deposit keeps waiting for the next run. One failure does not stop the batch.
- `reconciliation/alertBclReconciliation.ts` keeps one alert per manual case. It also sends one summary per run when any deposit has waited for 3 or more posts:
  - the text is "BCL has still not received deposits; they are sent again every hour. Do not post them by hand.";
  - it carries the count, the 10 most recent references and BCL's last reply.
- The owner's local `scripts/deposits_production/README.md` notes the attempt count and says a `RETRY_PENDING` deposit is not a manual case and must never be posted by hand.

## Verification

- Focused suites cover the new paths:
  - `replies.spec.ts` covers when a post counts as never received;
  - `depositPayment.spec.ts` and `depositDoublePost.spec.ts` replay the flow end to end on an in-memory store, from first failure to a later successful retry, and assert no failure reason is left;
  - `retryUnsentBclDeposits.spec.ts` covers the claim, a lost race, the three Paystack refusals, Paystack down and carrying on after one failure;
  - `paymentReconciliation.spec.ts` covers the retry running before the alerts, the summary and no summary below 3 posts.
- Full suite (201 suites, 1,807 tests), `tsc`, `yarn build` and Prettier pass.
- Mutations made tests fail with no type errors. The mutations of the first build:
  - a pre-send error not counted as never received;
  - a timeout retried;
  - BCL's answer ignored;
  - no attempt cap;
  - an unknown error retried;
  - a Paystack mismatch ignored;
  - BCL's ERP reference lost.
- The mutations of the review fixes:
  - no summary;
  - the waiting reason not removed;
  - the alerts run before the retry;
  - the retry stage removed.
- An independent review (three reviewers, one skeptic per finding) raised 8 findings; 3 were confirmed and fixed, 5 refuted.
  - No alert came until all 25 posts failed, about a day; before B12 the first alert came within an hour. Fixed with the summary after 3 posts.
  - The retry stage was untested, so deleting it or running it after the alerts passed every spec. Fixed with tests.
  - A deposit that succeeded on a retry kept the waiting reason, because Mongoose drops `failureReason: undefined`. Fixed by removing the reason when the retry takes the deposit back.
- The README line was added as a precaution, although the reviewer finding behind it was refuted.

## Notes

- A deposit left `IN_PROGRESS` by a crash during a retry is not reported by the hourly alert. The existing B10 design note already covers it: list every deposit whose `bclSync.status` has been `IN_PROGRESS` past the BCL timeout.
- The app needs no change. Customers see the deposit as `PROCESSING` while it waits.
