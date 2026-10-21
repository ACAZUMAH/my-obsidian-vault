---
type: source
status: active
created: 2026-09-06
updated: 2026-10-16
tags: [bora-capital, backend, kyc, bcl, statements]
sources:
  - ../../raw/sources/2026-09-06-bora-kyc-supervision-and-statement-update.md
  - ../../raw/sources/2026-09-18-bora-kyc-supervision-description-uncertainty.md
  - ../../raw/sources/2026-10-11-bora-kyc-bcl-agreed-outcome-rule.md
  - ../../raw/sources/2026-10-12-bora-kyc-approval-status-contract.md
  - ../../raw/sources/2026-10-13-bora-createkyc-no-resubmission.md
  - ../../raw/sources/2026-10-16-bora-kyc-repost-and-cash-movement.md
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

## Core Claims

- KYC now passes through BCL supervision; submission is not approval.
- Refresh approval through `me` and keep supervision references internal. `createKyc` (formerly `updateKyc`) creates only a user's first KYC. BCL has no update endpoint: a rejected KYC never becomes an IMS identity, so BCL's workflow is to re-post the corrected KYC through `addindividualidentity_bcl`, and the same email, phone, and ID are accepted. `updateKyc` does that for `REJECTED` users: sent fields are merged with the saved form, and saved images are reused unless replaced.
- The submitted form, images included exactly as sent, is kept in the `kycSubmissions` document, one per user. It is saved in the same Mongo transaction as the supervision reference and deleted in the same transaction as the approval. `User.kycSubmission` is returned to its owner only, with `imagesOnFile` flags instead of image data. The code follows the repository pattern: one function per service file, pure helpers in `services/users/helpers`, and `withTransaction` instead of best-effort try/catch. `submitKycToBcl` shares the claim, restore, and reconciliation path between create and update; a BCL 400 restores the rejection reason.
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

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]

## Contradictions Or Tensions

- The 2026-09-18 correction supersedes any implication that approved/rejected descriptions are known provider values. The helper comment and mocked tests establish code behavior only.
- The 2026-10-11 interim rule was replaced on 2026-10-12, when BCL supplied explicit approved and rejected outcomes with a rejection reason. The user's original objections to inferring outcomes from the identity lookup held.
- BCL's original PDF showed pending as `Status: "0"`; the 2026-10-12 samples use `P`. Both shapes are accepted for pending only.

- This supersedes immediate approval of newly submitted KYC. Legacy identity-based onboarding remains supported.
- The new PDF contains a linked-portfolio response sample, but the user explicitly deferred that feature; sample availability alone does not authorize exposing GrowWealth.

## Open Questions

- Will BCL add the IdentityID to the approved response, so approval no longer depends on an email/phone lookup? Which identity returns for a customer with an earlier identity or a repeat submission? Can a rejected customer resubmit with the same email and phone?

- How should linked portfolios be exposed after the user clarifies the account requirements?
