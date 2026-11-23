# Bora KYC: refused form and claim release in one transaction

Date: 2026-11-06
Source: direct user decision in a `bora-capital-backend` session, plus the code changed and verified in that session (paraphrased).

Earlier the same day, the agent implemented keeping a refused KYC form (NIA failure or BCL 400) as a best-effort save followed by a separate claim release. The agent had not checked the user's 2026-10-16 convention of `withTransaction` instead of best-effort try/catch. When a vault update surfaced the conflict, the agent recommended one transaction. Its reasoning: a save that fails while the release succeeds needs a form that fails validation, and that form would also fail on the success path after BCL had accepted it. An unavailable database fails the release either way. The user chose: "Yes, one transaction".

Implemented: `src/services/users/kyc/releaseKycSubmission.ts` now opens a session and, in one `withTransaction`, restores the prior status, supervision reference and rejection reason. The restore is conditioned on the claim (`kycStatus: SUBMITTED`, `kycSupervisionId: null`), and the form is then upserted to `kycSubmissions`. If the claim changed, or either write fails, the transaction rolls back. The request answers 502 "KYC submission requires reconciliation. Please contact support before retrying.", is logged and reported to Sentry, and the claim stays SUBMITTED. `restoreKycSubmissionEligibility.ts` was folded into it and deleted.

Tests: the test session mock now rolls the user and saved form back when a transaction callback throws. New tests cover a failed save rolling back the release and a changed claim saving no form. Moving the save outside the transaction made 6 tests fail. Full Jest: 192 suites and 1591 tests; `yarn build` passes under Node 26.12.1. Uncommitted.
