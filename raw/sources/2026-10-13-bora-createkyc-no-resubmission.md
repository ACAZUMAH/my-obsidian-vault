# Bora createKyc: no resubmission through the add endpoint

Date: 2026-10-13
Source: direct user correction.

The agent told the user that resubmitting a rejected KYC was already supported, because `updateKyc` accepted `REJECTED` users and sent them through `createBclKyc` again. That behavior came from the 2026-09-06 plan, where an agent offered "Allow resubmission" and implemented it by reusing the add endpoint.

The user corrected this firmly. `updateKyc` was only ever meant to create the KYC; it was named "update" because the user record is created at signup before KYC. `addindividualidentity_bcl` (behind `createBclKyc`) only adds a new individual; nothing in BCL's API document says it can update or resubmit a KYC. BCL will provide a separate update endpoint soon. A rejected customer should simply see the rejection reason, with no special error. The user asked to rename the operation to `createKyc`.

Implemented: the service is now `createKycRecords` in `src/services/users/createKyc.ts`; the GraphQL mutation is `createKyc(data: CreateKycInput!): User!` (renamed from `updateKyc`/`UpdateKycInput`). It accepts only `PENDING` users; submitted, approved, and rejected users get the existing 409 "KYC already submitted for this user". The resubmission-specific clearing and restoring of `kycRejectionReason` was removed. `me` still exposes `kycRejectionReason` for rejected users. `docs/frontend-handoff-2026-10-13.md` announces the rename and replaces the earlier "correction form" note: no correction form until BCL's update endpoint arrives.
