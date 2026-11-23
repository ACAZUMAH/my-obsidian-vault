# Bora: email lowercasing reverted, lookups left exact, and the app told to stop lowercasing

Date: 2026-11-22
Source: direct owner statement in a Claude Code session on `bora-capital-backend`, answering the agent's point that exact-match email lookups would miss a customer who types different capitals. It follows the [owner correction](2026-11-22-bora-email-kept-as-typed-owner-correction.md). Nothing was committed.

## The owner's words (verbatim)

> it wouldn't change anything because all the staging user were created from the app and not linked an account, all all the user's in production are not many because is under test flight and it isn't live and the users there linked their accounts and if their emails came if the emails saved at bcl was caps and the app passed lower they wouldn't have been able to fetch the kyc and the linking would go through. So making the fix and notifying the frontend guy will work and the the app has lowercased emails won't change anything

## What it decides

- **No case-insensitive lookups.** The agent recommended that the email lookups ignore letter case; the owner declined.
- **The owner's reasoning:**
  - staging users were all created from the app, not by linking;
  - production has few users, because the app is on TestFlight only;
  - those users linked their accounts successfully, which BCL's KYC lookup would have refused had BCL's email had capitals and the app sent it lowercased.

  So existing lowercase emails change nothing.
- **The change:** revert the agent's lowercasing and tell the frontend developer to stop lowercasing.

## Change (uncommitted)

- **Reverted.** `src/services/auth/authExistingCustomer.ts` again stores `identity.PrimaryEmail.trim()`, exactly as BCL holds it.
- **Tests:**
  - `tests/unit/services/auth/otpRequestIssuance.spec.ts` is back to its earlier expectation, and the lowercasing test is removed.
  - `tests/unit/services/auth/linkedAccountEmailCase.spec.ts` now tests the owner's rule. An investor whose BCL email is `Ama.Mensah@Example.com` links with it as typed; the account keeps it exactly; password recovery with the same email finds it; and sign-up refuses that email.
  - Putting the lowercasing back fails 3 tests.
- **Checks:** full suite (213 suites, 1,961 tests), `yarn build` and Prettier pass.
- **Handoff.** `docs/frontend-handoff-2026-11-22.md` gains section 5, "Emails are kept exactly as the customer types them". The app must stop lowercasing at these places, trimming spaces only:
  - `canonicalEmail` in `src/utils/phoneNumber.ts:205-206`, used by sign-up (`signup.tsx:204`) and "Link your account" (`existing-customer.tsx:146`);
  - forgot password (`forgot-password.tsx:78`);
  - the next-of-kin email sent to BCL (`src/features/kyc/nextOfKin.ts:92`).

  The admin portal and no-change sections became 6 and 7.

## Not changed

Staff invites (`src/services/staff/inviteStaffUser.ts:43`) and the administrator script (`scripts/admin_production/createAdministrator.ts:65`) still lowercase staff emails in the backend.
