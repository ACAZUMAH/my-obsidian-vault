# Bora KYC ApprovalStatus contract from BCL

Date: 2026-10-12
Source: BCL's sample responses for every ApprovalStatus scenario, supplied by the user, and the user's instruction to return to the originally intended flow. Credentials and session cookies are omitted.

Request: `POST /api/partner/fetchdata` with `RequestID: "ApprovalStatus"` and `xmlDetail: "<Request><SupervisionID>…</SupervisionID></Request>"`.

Sample responses:

- Pending (reference 1017446): `{ "Status": [{ "Status": "P", "Description": "Pending Supervision" }] }`
- Invalid (reference 1017406): `{ "Status": [{ "Status": "0", "Description": "Invalid" }] }`
- Rejected (reference 1017443): `{ "Status": [{ "Status": "R", "Description": "Rejected", "Remarks": "Invalid Postal Address" }] }`
- Approved (reference 1017446, later): `{ "Status": [{ "Status": "A", "Description": "Approved", "Remarks": "" }] }`

The user said that with these samples, the interim rule (ApprovalStatus only detects pending, then the identity lookup decides) no longer applies, and the flow should return to the original design: explicit approved and rejected outcomes.

Findings and implementation:

- The original code required `Status: "0"`, so against these real responses every submission would have stayed pending forever, under both the original and the interim flow.
- Mapping by code: `P` keeps SUBMITTED (the `0` plus pending-description shape from BCL's original PDF is also accepted). `A` approves after resolving the IdentityID through `fetchidentity_bcl` by email and phone, because the approval response has no IdentityID. `R` rejects and stores `Remarks` as the user's `kycRejectionReason`. `0` with `Invalid` means BCL does not recognize the reference, so the submission stays SUBMITTED and the error is logged for reconciliation. Anything else stays unchanged and is logged.
- `kycRejectionReason` is exposed on the GraphQL `User` type. It is cleared when the customer resubmits, and restored if BCL rejects the resubmission outright.
- ApprovalStatus stays outside `fetchBclData`, which treats any status other than `0` as an error.
