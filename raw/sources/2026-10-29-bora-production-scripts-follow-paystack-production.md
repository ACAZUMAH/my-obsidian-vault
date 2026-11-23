# Bora production scripts follow the paystack_production pattern

Date: 2026-10-29
Source: Direct user correction on `bora-capital-backend` (paraphrased; the user was emphatic), plus the corrected change. The administrator's personal details are deliberately left out of this record.

## User correction

The agent's first production fund seed and admin bootstrap (recorded in `2026-10-28-bora-production-admin-and-fund-seed.md`) used the application's local runtime: `initializeEnvironment`, `connectDB`, the local `.env`, and `fetchCISPortfoliosFromBcl`. The local environment is configured for **staging**, so those scripts would have read staging BCL and written to the staging database.

The user had pasted the production BCL data (`BBF1100`, `BORA BALANCED UNIT TRUST`, offer price 0.2647) precisely so the script would not fetch it. The user pointed to how they built `scripts/paystack_production` as the pattern to follow.

## The pattern (scripts/paystack_production)

- **Layout:** a dedicated `scripts/<thing>_production/` folder containing:
  - a README covering manual setup, the environment, the currently exposed portfolio, how to run it, and items waiting for production IDs;
  - `constants/` holding the pasted production data;
  - `helpers/` with `requiredEnvironmentValue`;
  - `interfaces/`;
  - one script.
- **Configuration:**
  - production values come from `PROD_`-prefixed variables;
  - the script calls `mongoose.connect(PROD_MONGODB_URI)` directly;
  - no `initializeEnvironment` or `connectDB`;
  - no external fetch of data that the constants already hold.
- **Behaviour:** it refuses non-production configuration, and it skips work that is already done.
- **Git:** the folder is gitignored.

## Corrected implementation

- **Reverted.** The development files the agent had changed for production were restored exactly: `scripts/seeds/seedFundCatalog.ts`, `fundCatalogFixtures.ts`, `scripts/bootstrap/bootstrapAdmin.ts` and their tests. The first production seed files were deleted.
- **`scripts/funds_production/seedBalancedFund.ts`:**
  - `constants` holds the pasted BCL portfolio and the Balanced 30 Sep 2026 facts as printed.
  - It validates the facts before connecting, then connects to `PROD_MONGODB_URI`.
  - It refuses a URI equal to `MONGODB_URI`.
  - It skips an existing fund, and creates the fund hidden from customers.
  - It makes no BCL call.
- **`scripts/admin_production/createAdministrator.ts`:**
  - It runs against `PROD_MONGODB_URI` with the same local-database guard.
  - A missing account is created with `PROD_ADMIN_PASSWORD`, which is required only then, checked against the password rules, and never printed. The account gets admin access only, plus the system Administrator role.
  - An existing account is promoted, keeping its customer access and password.
  - It refuses conflicting or disabled accounts.
  - It sends no email.
  - Changes are audited as `STAFF_ACCESS_UPDATED`.
- **Git and verification:**
  - Both folders and their two test files are added to `.gitignore`.
  - 19 new tests pass, and all 13 script suites (75 tests) pass.
  - `tsc` over `src`, `tests` and `scripts` passes, and so does the build.
  - Nothing was run against production.
