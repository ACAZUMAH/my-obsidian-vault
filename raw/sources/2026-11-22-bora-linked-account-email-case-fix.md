# Bora: linked accounts store the email lowercased, so password recovery finds them

Date: 2026-11-22
Source: one Claude Code session on `bora-capital-backend` (branch `feature/updates`).
- The checks behind the 2026-11-22 frontend handoff found the bug ([evidence](2026-11-22-bora-frontend-handoff-2026-11-22.md)).
- The owner answered "Yes, fix it" when asked whether to fix the password-recovery email bug first.
- Nothing was committed.

## The bug

- The uncommitted 2026-11-19/20 "Link your account" change opened new accounts with BCL's `PrimaryEmail` exactly as BCL holds it, for example `Ama.Mensah@Example.com`.
- Password recovery (`forgetPassword` → `getUserByEmail`) and sign-up's duplicate check (`checkUserExist`) match the email exactly. The app always sends emails lowercased (`canonicalEmail`; sign-up has lowercased since at least 2025-10).
- So a linked investor whose BCL email has capitals got "User not found" at password recovery. Sign-up could also open a second account for the same mailbox.
- Shipped code never had this. The committed linking code stored the email the app typed, which is already lowercased.

## Change (uncommitted)

- `src/services/auth/authExistingCustomer.ts`: the account email is now `identity.PrimaryEmail.trim().toLowerCase()`.
- The case-insensitive lookup (collation strength 2) is kept, so an older account holding capitals is reused unchanged rather than doubled.
- Comments were updated to explain why.

## Verification

- **New test** `tests/unit/services/auth/linkedAccountEmailCase.spec.ts` uses an in-memory users store with exact and case-insensitive matching, and the real `getUserByEmail`, `forgetPassword` and `checkUserExist`. It covers three cases:
  - an investor whose BCL email has capitals links, is told to finish linking, then recovers their password;
  - sign-up refuses the same mailbox;
  - an older account with capitals is reused.
- **Updated test:** one expectation in `otpRequestIssuance.spec.ts`, plus a new test that the account opens lowercased.
- **Mutation checks.** All three made tests fail with no type errors:
  - removing the lowercasing (4 failed);
  - a case-sensitive lookup (2 failed);
  - dropping the trim (5 failed).
- Full suite (213 suites, 1,962 tests), `tsc`, `yarn build` and Prettier pass.
- **Independent review.** Three lenses ran: completeness, regression, and stored data. One finding was raised: older accounts with capitals keep them, so a migration would be needed. A verifier refuted it, because shipped code has always stored lowercased customer emails, and staff invites and the administrator script lowercase too. Only this uncommitted pre-fix code could have written capitals, and only into the staging database the local environment points at.
