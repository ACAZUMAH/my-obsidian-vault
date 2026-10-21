# Bora KYC supervision description uncertainty

Date: 2026-09-18
Source: direct user correction during frontend handoff preparation.

The user stated: "I don't know what description is return when a kyc is approved or rejected, I only know what is returned when it's pending so take note".

The supplied normalizeKycApprovalStatus implementation accepts pending/pending supervision, approved, and reject/rejected. These are implementation mappings, not evidence that BCL actually returns the approved/rejected strings. The user also reaffirmed that Grow Wealth is unfinished and must be identified as such in the frontend handoff.

Do not treat the helper's "known" wording or mocked provider tests as confirmation of BCL's final-outcome vocabulary. Obtain real sanitized approved/rejected responses or an authoritative provider contract before claiming those outcomes are integrated end to end.
