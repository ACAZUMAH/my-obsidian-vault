# Bora KYC: NIA before BCL, the 5 MB body limit, one ID front image, and keeping refused forms

Date: 2026-11-06
Source: Direct user statements and decisions in a `bora-capital-backend` session, plus the code changed and verified in that session (paraphrased).

## NIA selfie check gates the BCL post

- User decision: the NIA selfie check runs before the KYC is posted to BCL. If NIA returns any error (no match, invalid data, a watch-listed card, an NIA error or NIA unreachable) or the daily selfie-check limit is hit, the KYC is not sent to BCL. The error goes back to the customer so they can correct it, for example by retaking the selfie.
- This was already the implemented behaviour: `src/services/users/kyc/submitKycToBcl.ts`, tested in `tests/unit/services/user/kycLifecycle.spec.ts` under "NIA selfie check". In the code, the check applies when the ID number is a Ghana Card PIN; a Ghanaian national who does not give a Ghana Card PIN is refused with a 400.

## Express JSON body limit

- User decision: the Express JSON body limit stays at 5 MB (`express.json({ limit: '5mb' })` in `src/servers/createExpressApp.ts`) for security reasons. Do not raise it to fix 413 responses; shrink the payload instead.

## Production 413 on a KYC submission

- On 2026-11-06 production returned `413 PayloadTooLargeError` on a KYC submission. body-parser rejected it before GraphQL ran, so it never reached BCL.
- Likely cause: the app sent the ID front image twice, as `imgIDString` and `imgIDFrontString`, while its client-side size budget counted it once.
- User decision: the app sends only `imgIDFrontString` (now required on `CreateKycInput`) and `imgIDBackString`. `imgIDString` was removed from `CreateKycInput` and `UpdateKycInput`. The backend's `formatPayload` sends the front image to BCL as both `imgIDString` and `imgIDFString`.
- `KycImagesOnFile.id` is deprecated and returns the same value as `idFront`. The `kycSubmissions` model no longer stores `imgIDString`, and `mergeKycForm` drops it from older saved forms.

## Keeping a refused form

- Implemented at the user's request: when NIA or BCL definitively refuses a KYC (an NIA failure, or a BCL 400), the backend saves the form to `kycSubmissions` while it still holds the submission claim, then restores the prior status. The save is best effort: a failed save is logged and never keeps the claim. New file: `src/services/users/kyc/releaseKycSubmission.ts`.
- `updateKyc` now accepts `PENDING` as well as `REJECTED`; `SUBMITTED` and `APPROVED` return 409 "KYC already submitted for this user". A customer whose first KYC was refused corrects only what was refused, instead of recapturing every document after an app restart.
- An uncertain BCL outcome (502, reconciliation) still keeps the claim and saves nothing.

## App distribution context

- The user said that, as of 2026-11-06, the Bora customer app is distributed only through TestFlight, with no public store builds. Breaking GraphQL input changes can therefore ship with a new TestFlight build, without a deprecate-then-remove phase. Re-check this once the app is publicly released.

## Frontend handoff

- The handoff for these changes is `docs/frontend-handoff-2026-11-06.md` in the backend repository. It covers the ID image change. The app changes for keeping refused forms go into it or into a later dated handoff, depending on whether the user has already sent it.

## Verification at the time of recording

- Backend `tsc` clean, `yarn build` passed, and full Jest passed at 192 suites and 1590 tests under Node 26.12.1.
- Nothing was committed. No live NIA or BCL call was made.
