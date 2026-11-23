# Bora: emails matched ignoring letter case, still stored as typed

Date: 2026-11-22
Source: owner messages and repository change in a Claude Code session on `bora-capital-backend`, branch `feature/updates`. The change is uncommitted, on top of `ca3cfa1`.

## The owner's words (verbatim)

Reopening the earlier decision:

> I am thinking about the emails issue and what you recommended. so now we telling the frontend guy send the email as it is right, so the emails that are already saved in lowercase and the emails from bcl how do handle that?
>
> I am thinking right and it's better we fix it properly rather than me assuming production won't be affected

Approving the design, after the agent's analysis: "Yes, build it".

Asked whether `docs/frontend-handoff-2026-11-22.md` had been sent, the owner chose "Sent: new handoff".

## What the agent's analysis found

A five-agent workflow read the backend, the BCL calls and both clients read-only. A skeptic challenged the design.

- **Production stored every customer email lowercase, linked investors included.**
  - On `origin/main`, "Link your account" saved the app's lowercased email through `upsertUser({ email: data.email })`, not BCL's `PrimaryEmail`.
  - BCL's casing is not stored anywhere in our database.
- **With exact lookups, once the app stops lowercasing:**
  - forgot password returns 404 for anyone who types a capital;
  - sign-up lets a second account in for the same mailbox, differing only by case;
  - staff invites refuse, or create duplicates.
- **iOS never capitalises:** the app's email fields set `autoCapitalize="none"`.
- **Lowercase addresses deliver in practice.** RFC 5321 lets a server treat the local part as case-sensitive but discourages relying on it, and every production customer received codes at lowercased addresses.
- **BCL's own case handling is unknown.** Checks against BCL's test environment are listed separately; they are owner items, not in the handoff.

## Change

**Rule (unchanged):** a stored or sent email is never lowercased.

**Index**
- A new unique index `email_ci_1` on `{ email: 1 }`, collation `{ locale: 'en', strength: 2 }`. `email_1` stays.
- `EMAIL_MATCH_COLLATION` is defined in `src/common/helpers/contacts.ts`. `isSameEmail` moved there too, re-exported from `getBclKyc`.

**Guard (`src/models/user/emailMatch.ts`)**
- Query middleware on the user schema throws when a filter compares `email` without exactly that collation.
- It looks inside `$or`, `$and` and `$nor`.
- Regex and `$exists` filters are allowed.

**Lookups**
- They use the collation and trim the input: `getUserByEmail`, `checkUserExist`, `authExistingCustomer`, `inviteStaffUser`.
- `checkUserExist` and the staff invite are split into separate email and phone queries, so the phone index is still used.

**Duplicate-key handling**
- **Link flow:** a duplicate-key error on the email index re-reads and reuses the account; one on the phone index answers 409.
- **Staff invite:** a create race now answers 409 instead of 500.

**`upsertUser`:** deleted, since nothing called it.

**Migration `CREATE_USER_EMAIL_CASE_INSENSITIVE_INDEX_V1` (registered last)**
- It refuses on non-text emails, or on accounts whose emails differ only by case or surrounding spaces. The error lists user IDs, never emails.
- It then builds the index.
- If the index refuses a pair the JavaScript check missed (invisible or full-width characters), it names the accounts using the index's own collation.

**Production audit**
- A read-only script in gitignored `scripts/email_audit_production/`, following the `paystack_production` layout with `PROD_MONGODB_URI`.
- It prints counts and IDs only, including `readyForMigration`.
- Its spec, `tests/unit/scripts/emailAuditProduction.spec.ts`, is gitignored too.

**Handoff:** `docs/frontend-handoff-2026-11-22-emails.md` (new, because the 2026-11-22 file was sent).
- It corrects section 5: matching ignores case.
- The app's no-lowercase build ships only after this backend.
- The portal stops lowercasing at `ForgotPasswordPage.tsx:78`.

## Verification

- **Full suite:** 216 suites, 2,023 tests. `yarn build`, `tsc` and Prettier pass.
- **Real Mongoose checks:** the guard rejects an exact email query before reaching the database, and a query with the collation reaches the driver with it.
- **Mutation checks:** 26, all caught, with no type errors. They covered:
  - each lookup's collation;
  - trimming;
  - the phone check;
  - the link race handling;
  - the staff comparison and race;
  - the guard;
  - the index declaration;
  - each migration refusal;
  - the collision naming;
  - the registration.
- **Independent review:** three lenses, each finding re-checked by a skeptic. It confirmed 1 of 3 findings, low, which was fixed: collisions the JavaScript check misses are now named by account. The other two were rejected with evidence:
  - an empty database already fails at earlier migrations;
  - no stored email can have surrounding spaces.

## Release order

1. Run the audit on production (`readyForMigration` must be true).
2. Deploy the backend.
3. Release the app build that stops lowercasing.

## Still open

The BCL checks: does BCL match email case on identity lookup, statements, withdrawals and accounts?
