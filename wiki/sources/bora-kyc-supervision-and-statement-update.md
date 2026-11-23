---
type: source
status: active
created: 2026-09-06
updated: 2026-11-12
tags: [bora-capital, backend, kyc, bcl, nia, statements]
sources:
  - ../../raw/sources/2026-09-06-bora-kyc-supervision-and-statement-update.md
  - ../../raw/sources/2026-09-18-bora-kyc-supervision-description-uncertainty.md
  - ../../raw/sources/2026-10-11-bora-kyc-bcl-agreed-outcome-rule.md
  - ../../raw/sources/2026-10-12-bora-kyc-approval-status-contract.md
  - ../../raw/sources/2026-10-13-bora-createkyc-no-resubmission.md
  - ../../raw/sources/2026-10-16-bora-kyc-repost-and-cash-movement.md
  - ../../raw/sources/2026-11-06-bora-kyc-id-image-and-refused-form.md
  - ../../raw/sources/2026-11-06-bora-refused-form-one-transaction.md
  - ../../raw/sources/2026-11-09-bora-nia-unrecognised-answer-400.md
  - ../../raw/sources/2026-11-10-bora-nia-live-selfie-results.md
  - ../../raw/sources/2026-11-12-bora-kyc-jpeg-selfie.md
  - ../../raw/sources/2026-11-12-bora-nia-live-jpeg-match.md
---

# Bora KYC Supervision And Statement Update


## Source

- Raw file: [Direct user evidence](../../raw/sources/2026-09-06-bora-kyc-supervision-and-statement-update.md)
- Date: 2026-09-06
- Author: Direct user instructions and approved implementation plan
- Ingested: 2026-09-06
- Correction: [Provider-description uncertainty](../../raw/sources/2026-09-18-bora-kyc-supervision-description-uncertainty.md), direct user clarification on 2026-09-18.
- Update: [BCL agreed outcome rule](../../raw/sources/2026-10-11-bora-kyc-bcl-agreed-outcome-rule.md), direct user report and implementation instruction on 2026-10-11.
- Contract: [BCL ApprovalStatus samples](../../raw/sources/2026-10-12-bora-kyc-approval-status-contract.md), supplied by the user on 2026-10-12; supersedes the 2026-10-11 interim rule.
- Correction: [createKyc, no resubmission](../../raw/sources/2026-10-13-bora-createkyc-no-resubmission.md), direct user correction on 2026-10-13; supersedes the 2026-09-06 resubmission design.
- Update: [BCL re-post workflow](../../raw/sources/2026-10-16-bora-kyc-repost-and-cash-movement.md), BCL's answer and user decisions on 2026-10-16; supersedes the 2026-10-13 wait for an update endpoint.
- Update: [NIA gate, one ID front image, refused forms](../../raw/sources/2026-11-06-bora-kyc-id-image-and-refused-form.md), direct user decisions and verified code on 2026-11-06, after a production 413; extends `updateKyc` to refused `PENDING` users.
- Correction: [Refused form in one transaction](../../raw/sources/2026-11-06-bora-refused-form-one-transaction.md), direct user decision on 2026-11-06; replaces the same day's best-effort refused-form save.
- Update: [NIA answers it does not recognise are a 400](../../raw/sources/2026-11-09-bora-nia-unrecognised-answer-400.md), staging evidence and direct user decision on 2026-11-09.
- Confirmation: [Live NIA match and non-match](../../raw/sources/2026-11-10-bora-nia-live-selfie-results.md), two user-run checks on 2026-11-10.
- Update: [The NIA selfie can be a JPEG](../../raw/sources/2026-11-12-bora-kyc-jpeg-selfie.md), direct user request on 2026-11-12.
- Confirmation: [Live NIA matches a JPEG](../../raw/sources/2026-11-12-bora-nia-live-jpeg-match.md), a user-run check on 2026-11-12.

## Core Claims

- KYC now passes through BCL supervision; submission is not approval.
- Refresh approval through `me` and keep supervision references internal. `createKyc` (formerly `updateKyc`) creates only a user's first KYC. BCL has no update endpoint: a rejected KYC never becomes an IMS identity, so BCL's workflow is to re-post the corrected KYC through `addindividualidentity_bcl`, and the same email, phone, and ID are accepted. `updateKyc` does that for `REJECTED` users: sent fields are merged with the saved form, and saved images are reused unless replaced.
- The submitted form, images included exactly as sent, is kept in the `kycSubmissions` document, one per user. It is saved in the same Mongo transaction as the supervision reference and deleted in the same transaction as the approval. `User.kycSubmission` is returned to its owner only, with `imagesOnFile` flags instead of image data. The code follows the repository pattern: one function per service file, pure helpers in `services/users/helpers`, and `withTransaction` instead of best-effort try/catch. `submitKycToBcl` shares the claim, restore, and reconciliation path between create and update; a BCL 400 restores the rejection reason.
- NIA gates the BCL post (user decision, 2026-11-06; already implemented in `submitKycToBcl`). The NIA selfie check runs first; any NIA error (no match, invalid data, watch-listed card, NIA error or unreachable) or a spent daily selfie-check limit stops the KYC from reaching BCL and returns the error to the customer to correct, such as retaking the selfie.
- An NIA answer the backend does not recognise is a 400, never a 502 (user decision, 2026-11-09). NIA's live replies put `success`, `code` and `msg` beside `data`, and staging got an undocumented code `11` with HTTP 400; the backend reads the code from either place, counts a match only for code 00 with `verified` true, and answers any other coded reply that is not a documented result with 400 "NIA could not verify this Ghana Card and selfie…", logging NIA's code and PIN-redacted `msg`. Only a reply with no code, a timeout, a network failure, or code 04 stays 502 "unavailable". The KYC never reaches BCL either way. The yes/no endpoint does return the NIA `person` record, which is never kept or logged. See [raw evidence](../../raw/sources/2026-11-09-bora-nia-unrecognised-answer-400.md).
- Live NIA confirms the binary outcome the user wants (2026-11-10): a non-match is HTTP 200, code `01`, "Not Matched Found", `verified` "FALSE", and the customer gets 400 "Your selfie did not match…"; a match is HTTP 200, code `00`, "Verified Successfully", `verified` "TRUE", and the KYC goes on to BCL. `success` is true for both, so it means NIA processed the request; only `code` and `verified` decide. See [raw evidence](../../raw/sources/2026-11-10-bora-nia-live-selfie-results.md).
- The NIA selfie can be a PNG or a JPEG (user request, 2026-11-12). The backend reads the format from the image's bytes, not the data URL label, and sends NIA `dataType` `PNG` or `JPG`; anything else is 400 "The selfie must be a PNG or JPEG image." NIA's document shows only PNG and no JPEG `dataType` value; live NIA confirmed JPEG on 2026-11-12: the user's own selfie as a JPEG with `dataType` `JPG` returned HTTP 200, code `00`, "Verified Successfully". The JPEG was 129 KB against 915 KB for the same selfie as a PNG. App changes: `docs/frontend-handoff-2026-11-12.md`. See [raw evidence](../../raw/sources/2026-11-12-bora-kyc-jpeg-selfie.md) and [the live JPEG match](../../raw/sources/2026-11-12-bora-nia-live-jpeg-match.md).
- Before 2026-11-12, `scripts/nia_staging/testNiaSelfie.ts` converted every photo to PNG, so a run with a `.jpg` file sent NIA a PNG; only a run with `--format jpg` sends a JPEG. Read the printed `dataType`, not the input filename.
- Refused forms are kept (2026-11-06, at the user's request). When NIA fails or BCL returns a 400, `releaseKycSubmission` restores the prior status and saves the form to `kycSubmissions` in one `withTransaction` (user decision, 2026-11-06). The restore applies only while the claim is still held. If the claim changed or either write fails, both roll back, the claim stays `SUBMITTED`, and the request answers 502 for reconciliation. `updateKyc` accepts `PENDING` as well as `REJECTED` (`SUBMITTED`/`APPROVED` get 409 "KYC already submitted for this user"), so the customer corrects only what was refused instead of recapturing every document after an app restart. An uncertain BCL outcome (502, reconciliation) keeps the claim and saves nothing.
- The ID front image is sent once (user decision, 2026-11-06). The app sends `imgIDFrontString` (now required on `CreateKycInput`) and `imgIDBackString`; `imgIDString` is gone from `CreateKycInput` and `UpdateKycInput`, and `formatPayload` sends the front image to BCL as both `imgIDString` and `imgIDFString`.
- The Express JSON body limit stays at 5 MB for security (user decision, 2026-11-06). Fix a 413 by shrinking the payload, never by raising the limit.
- Date-range statements use the mini-statement endpoint; CI accounts remain distinct by account number even when portfolio IDs match.
- Linked Portfolio/GrowWealth remains deferred pending user clarification.

## Useful Details

- Preserve the provider response typo `SuperviosionID` but use XML `SupervisionID` in approval queries.
- Confirmed ApprovalStatus contract (2026-10-12): `Status` holds the outcome code, not `0` for success. `P` pending; `A` approved (`Remarks` empty, no IdentityID); `R` rejected with a customer-facing `Remarks` reason; `0` with `Invalid` means BCL does not recognize the reference. The earlier code required `Status: "0"` and would have kept every real submission pending forever.
- Implemented mapping: `P` (or the `0` plus pending-description shape from the original PDF) keeps SUBMITTED. `A` resolves the IdentityID through `fetchidentity_bcl` by email and phone, then approves; a missing identity or failed lookup keeps SUBMITTED for a later retry. `R` rejects and stores `Remarks` as the user's `kycRejectionReason` (GraphQL `User.kycRejectionReason`). `Invalid` and unknown codes keep SUBMITTED and are logged for reconciliation. ApprovalStatus stays outside `fetchBclData`.
- `fetchidentity_bcl` reports only an HTTP 400 with a `Message` (or an empty list or non-zero status) as not found; transport failures are 502.
- Superseded: the 2026-10-11 interim rule that inferred approval or rejection from the identity lookup.
- Guard concurrent submissions and stale approval writes. Ambiguous submission outcomes require reconciliation; record reads and notification failures cannot change the approval decision.
- Existing GraphQL contracts, image-field translations, and existing-customer onboarding remain compatible. No background polling or data migration is introduced.
- The NIA check applies when the ID number is a Ghana Card PIN; a Ghanaian national without one is refused with a 400. Tests: `tests/unit/services/user/kycLifecycle.spec.ts`, "NIA selfie check".
- The 2026-11-06 production `413 PayloadTooLargeError` came from body-parser (`express.json({ limit: '5mb' })` in `src/servers/createExpressApp.ts`) before GraphQL ran, so it never reached BCL. Likely cause: the app sent the ID front as both `imgIDString` and `imgIDFrontString` while its size budget counted it once.
- `KycImagesOnFile.id` is deprecated and returns the same as `idFront`. `kycSubmissions` no longer stores `imgIDString`, and `mergeKycForm` drops it from older saved forms. The BCL KYC read type `KycRecords` still returns `imgIDString`.
- `imgIDString` was removed without a deprecation phase because, as of 2026-11-06, the customer app ships only through TestFlight (user statement). The app changes are in `docs/frontend-handoff-2026-11-06.md` in the backend repo; refused-form handling for the app goes there or into a later dated handoff, per [[bora-frontend-handoff-frozen|the frozen-handoff rule]].
- Verification on 2026-11-06: `tsc` clean, `yarn build` passed, full Jest 192 suites/1590 tests under Node 26.12.1. Not committed; no live NIA or BCL call.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[../projects/bora-capital-mobile-app|Bora Capital Advisors Mobile App]]
- [[bora-fund-fact-sheet-pdfs|Bora Fund Fact-Sheet PDFs]] (its 3 MiB PDF cap exists to stay inside the same 5 MB body limit)

## Contradictions Or Tensions

- The 2026-09-18 correction supersedes any implication that approved/rejected descriptions are known provider values. The helper comment and mocked tests establish code behavior only.
- The 2026-10-11 interim rule was replaced on 2026-10-12, when BCL supplied explicit approved and rejected outcomes with a rejection reason. The user's original objections to inferring outcomes from the identity lookup held.
- BCL's original PDF showed pending as `Status: "0"`; the 2026-10-12 samples use `P`. Both shapes are accepted for pending only.

- This supersedes immediate approval of newly submitted KYC. Legacy identity-based onboarding remains supported.
- The new PDF contains a linked-portfolio response sample, but the user explicitly deferred that feature; sample availability alone does not authorize exposing GrowWealth.
- The first 2026-11-06 refused-form save was best effort, which broke the 2026-10-16 rule of `withTransaction` over best-effort try/catch. The user resolved it the same day by choosing one transaction, so the rule holds without exception. The 2026-10-16 "remain compatible" note covers that change only; the 2026-11-06 removal of `imgIDString` is an intentional breaking input change.
- The 2026-10-16 `updateKyc` was `REJECTED`-only; since 2026-11-06 it also accepts `PENDING`.

## Open Questions

- What does NIA code `11` mean? NIA's document lists only 00 to 04, and the user's 2026-11-10 match and non-match runs did not reproduce it (both HTTP 200). The next staging occurrence logs NIA's PIN-redacted `msg`; otherwise ask NIA.

- Will BCL add the IdentityID to the approved response, so approval no longer depends on an email/phone lookup? Which identity returns for a customer with an earlier identity or a repeat submission? Can a rejected customer resubmit with the same email and phone?

- How should linked portfolios be exposed after the user clarifies the account requirements?
- Was the duplicated ID front image the actual cause of the 2026-11-06 production 413? It is the likely cause, not a confirmed one; at recording the change was uncommitted and had not been exercised in production.
- Once the customer app is publicly released, breaking GraphQL input changes need a deprecate-then-remove phase again; re-check the TestFlight-only status before the next one.
