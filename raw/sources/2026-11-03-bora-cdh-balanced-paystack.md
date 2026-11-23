# Bora CDH Balanced Fund gets production Paystack setup

Date: 2026-11-03
Source: Direct user request on `bora-capital-backend`, plus the resulting change. The settlement account number is deliberately left out of this record; it lives only in the gitignored script constants.

## User statement

- A new fund was introduced: production BCL returns `CBF1100`, `CDH BALANCED FUND`, offer price 0.9769.
- Add its production Paystack setup. The user supplied its settlement account: Republic Bank, current account, account name `HFCN CDH BALANCED FUND LTD-TNX`.

## Implementation

- `scripts/paystack_production/setupCdhBalancedPortfolio.ts` calls the shared `setupPortfolioSubaccount` helper, the same as Fixed Income and Global Balanced.
- Paystack's live Ghana bank list (`GET /bank?currency=GHS`, 3 Nov 2026) returns `110100` for Republic Bank (GH) Limited; that is the settlement bank code.
- The subaccount's business name is the portfolio name, which differs from the bank account name. The operator checks `resolvedAccountName` against `HFCN CDH BALANCED FUND LTD-TNX`.
- No fund seed was added for `CBF1100`: there is still no fact sheet.
- Before this change, the user had removed the `PROD_MONGODB_URI` versus `MONGODB_URI` guard from `setupPortfolioSubaccount`. No reason was stated. The funds seed helper still has the guard.
- The local-only spec `tests/unit/scripts/paystackProduction.spec.ts` covers `CBF1100` and passes, 20 tests. `tsc --noEmit` is clean.
