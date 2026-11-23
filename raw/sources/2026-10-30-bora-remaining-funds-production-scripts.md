# Bora remaining funds go live in production

Date: 2026-10-30
Source: Direct user request on `bora-capital-backend`, plus the resulting change. Settlement account numbers are deliberately left out of this record; they live only in the gitignored script constants.

## User statement

- The rest of the funds are now live. Production BCL (`fetchciportfolios_bcl`) returns four portfolios: `BBF1100` BORA BALANCED UNIT TRUST (offer price 0.2646), `BFI1100` BORA FIXED INCOME UNIT TRUST (0.2175), `BGF1100` BORA GLOBAL BALANCED TRUST (1.3527), and `CBF1100` CDH BALANCED FUND (0.9769).
- Write the remaining production Paystack setup and fund seeds. `BBF1100` is already seeded for both Paystack and its fund.
- `CBF1100` is a new fund; there is no information about it yet.
- The user supplied the 30 Sep 2026 fact-sheet PDFs for the three Bora funds and the settlement accounts for Fixed Income (Fidelity Bank Ghana, Action Chapel) and Global Balanced (Fidelity Bank (Ghana) Ltd., Ridge Towers, branch code 240101).

## Implementation

- Both scripts follow the `scripts/paystack_production` pattern (see `2026-10-29-bora-production-scripts-follow-paystack-production.md`). The user's Balanced scripts were left unchanged.
- **`scripts/paystack_production`:** `setupFixedIncomePortfolio.ts` and `setupGlobalBalancedPortfolio.ts` call a shared `setupPortfolioSubaccount` helper. The helper refuses non-live keys and a `PROD_MONGODB_URI` equal to `MONGODB_URI`, skips a portfolio that already has an active subaccount, and creates the live subaccount. If saving the configuration fails, the error names the created `ACCT_...` code, so an operator saves it by hand instead of rerunning and creating a duplicate.
- **Settlement bank code:** Paystack's live Ghana bank list (`GET /bank?currency=GHS`, 30 Oct 2026) returns `240100` for Fidelity Bank Ghana Limited and `230100` for GT Bank. Paystack settles to a bank, not a branch, so both Fidelity accounts use `240100`; the Ridge Towers code `240101` is a Ghana branch sort code, kept for the record only.
- **`scripts/funds_production`:** `seedFixedIncomeFund.ts` and `seedGlobalBalancedFund.ts` call a shared `seedHiddenFund` helper with the same behaviour as the Balanced seed. Facts are the printed 30 Sep 2026 sheets in their printed wording.
  - Fixed Income prints no Investment Case section, so it has no `investmentCase`. Its exit fee is Nil.
  - Global Balanced page 2 is headed "31ST AUGUST 2026", but its journey ends at 13,230 on 30 Sep, matching page 1.
  - Chart points use the dev-seed dates. Label positions in the PDF text layer agree with those dates within label-placement slack, and the printed returns confirm several of them: FI 17,080 on 31 Dec 2024, GB 1.3491 on 30 Jun 2026.
- **`CBF1100`:** no Paystack configuration and no fund seed until a fact sheet and settlement account exist.
- **Tests:** local-only specs `tests/unit/scripts/fundsProduction.spec.ts` (extended) and `tests/unit/scripts/paystackProduction.spec.ts` (new, added to `.gitignore`) pass, 28 tests. `tsc --noEmit` over `src`, `tests` and `scripts` is clean.
