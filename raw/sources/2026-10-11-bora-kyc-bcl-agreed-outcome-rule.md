# Bora KYC BCL agreed outcome rule

Date: 2026-10-11
Source: direct user report of a meeting with the BCL API team, the follow-up discussion, and the user's instruction to implement the interim flow.

The user reported that BCL's team said the app should use the ApprovalStatus check only to detect pending, then call the Get KYC API (`fetchidentity_bcl`): KYC returned means approved, an error means rejected. BCL emails the customer when KYC is approved. The user had told BCL in the meeting that this flow would not work; BCL kept it. BCL has still not documented the approved or rejected ApprovalStatus descriptions, and gives no rejection reason. KYC creation returns only the SupervisionID, not the IdentityID.

The user posted a follow-up in the shared BCL WhatsApp group asking for ApprovalStatus to return an explicit approved outcome with the IdentityID, an explicit rejected outcome with a customer-facing reason, the full list of status values, confirmation that rejected customers can resubmit with the same email and phone, and optionally a status-change webhook. A BCL contact objected that this went against the meeting agreement. That is unresolved; the user is waiting for BCL's answer on the rejection part.

The user then confirmed the interim flow and said to implement it while waiting:

- A pending ApprovalStatus keeps the submission pending.
- Any other description triggers the Get KYC lookup by email and phone.
- Identity returned: approved, with its IdentityID.
- Confirmed not-found from Get KYC: rejected, with a generic customer message.
- Timeouts, server errors, auth failures, or unrecognized responses: stay pending and retry; never a rejection.

The user's goal is that a customer who receives BCL's approval email and opens the app sees approved, not pending. That works through the existing profile-refresh check, provided the app fetches the profile from the network.
