# Bora production: first administrator and fund seed

Date: 2026-10-28
Source: Direct user request on `bora-capital-backend`, plus the implemented change. The administrator's personal details are deliberately left out of this record.

## Request

The user asked for two things:

- **An administrator account in production** for themselves, so they can start checking things.
- **A production seed for the funds.** Production BCL lists only `BBF1100` (Bora Balanced Unit Trust), and the user said the other funds come later. They attached Bora's original 30 Sep 2026 Balanced fact sheet as the source.

## Implementation

Both scripts are local-only and gitignored, like the development seed.

- **`scripts/bootstrap/bootstrapAdmin.ts`, extended in place.** It finds one account by phone number (local or international) or by email:
  - **No account:** it creates one with a random, never-revealed password. It gives the account the system Administrator role (`*`), sets the invitation to pending, and sends the normal staff invitation email (`/staff/setup`, 6-digit code, 10 minutes). The person sets their own password there. This mirrors `inviteStaffUser`, without an inviting administrator, and is audited as `STAFF_INVITED`.
  - **An unaccepted invitation:** re-running sends a new code.
  - **An existing account:** promoted as before. Customer access and the current password are kept.
  - **Refusals:** the phone number and email belong to different accounts; the account is disabled; `ADMIN_PORTAL_URL` is unset when an invitation is needed. In each case nothing is written.
- **`scripts/seeds/seedProductionFunds.ts` and `productionFundFixtures.ts`.**
  - **Source:** `BBF1100` is written from the printed sheet, with verbatim text and the printed labels. Seed validation stores them in the backend's one format.
  - **Holding names:** the printed issuer, plus the asset class for a repeated issuer, as the portal import names them.
  - **Figures:** identical to the development seed.
  - **Safety:** the seed refuses unless production BCL lists every fixture's portfolio.
  - **Visibility:** it creates funds hidden; an administrator shows them in the portal after review.
  - **Shared logic:** it reuses `seedFundCatalog`, which now takes optional `fixtures` and `visible`. The defaults are unchanged.
- **Verification:**
  - 26 bootstrap and seed tests pass.
  - `tsc` over `src`, `tests` and `scripts` passes.
  - The build passes.
  - Nothing was run against production: the user runs both scripts with the production environment.
