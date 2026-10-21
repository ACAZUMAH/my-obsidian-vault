# Bora KYC Supervision And Statement Update — Direct User Evidence

Date: 2026-09-06
Context: User-requested Bora backend update from the supplied seven-page `curl (1).pdf` provider reference. This is a scoped excerpt of direct conversation evidence, not a full private transcript.

## Direct instructions and clarifications

The user requested: "now the kyc is now going to go through verification" and "leave the linked account out for now I still need clarification on that".

When asked about the approval outcome contract, the user clarified: "when we check approval status, the approved, reject or pending will return in the same description".

The user selected "On app refresh (Recommended)" for approval checks and "Allow resubmission (Recommended)" after rejection, then explicitly requested implementation of the resulting plan.

## Accepted implementation contract

- KYC submission returns the provider's `Status[0].SuperviosionID`, stored as internal `kycSupervisionId`, and sets local `SUBMITTED` rather than `APPROVED`.
- `me` checks `RequestID: ApprovalStatus` through `fetchdata`, placing the escaped reference in XML `SupervisionID`. Approval is determined by `Description`, not by successful transport status alone.
- After approval, retrieve the final identity through the existing email-and-phone lookup and persist the identity ID with approval. Provider failure or missing identity retains submitted status for later refresh.
- Use atomic claims and reference/state guards, allow corrected rejected submissions, and require reconciliation rather than automatic replay after ambiguous acceptance.
- Record reads cannot bypass supervision. Account creation requires completed approval and the resulting identity ID for supervised users. Send the existing completion notification only after persisted approval, with notification failures isolated.
- Date-range statements use `fetchministatement_bcl` with `FromDate` and `ToDate` in `DD MMM YYYY`; preserve both public statement operations and ownership checks.
- CI account creation/listing retain their contracts and support distinct accounts in the same portfolio. Linked Portfolio/GrowWealth remains deferred pending the user's clarification.
- Public GraphQL names, inputs, return types, KYC enums, image requirements, and field mappings remain unchanged. Supervision metadata is optional; preserve existing customer flows without a migration.

## Evidence boundary

The supplied PDF establishes the pending supervision envelope and statement/account examples. Terminal outcome descriptions, profile-refresh timing, rejection resubmission, and deferral of linked portfolios were confirmed directly by the user. The plan reuses the existing identity lookup to obtain the final ID. No live-provider verification was requested or performed during this implementation.
