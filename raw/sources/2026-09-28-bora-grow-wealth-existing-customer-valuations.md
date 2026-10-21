# Bora Grow Wealth existing customer valuations

Date: 2026-09-28
Source: direct user instruction, supplied BCL API document, and supplied portal reference in the Bora backend task.

The user authorized Grow Wealth reads for existing BCL customers. The backend must first call `LinkedPortfolio` with the authenticated customer's server-owned identity and contact fields, then call `LinkedPortfolioValuation` with each returned portfolio ID and a value date.

The app-facing contract must expose two separate authenticated APIs:

- A Grow Wealth dashboard summary that presents the linked portfolio name, total NAV, and NAV grouped by asset class, matching the supplied portal reference.
- A detailed valuation report that preserves the provider's holding-level valuation fields.

The BCL document uses `POST /api/partner/fetchdata`. `LinkedPortfolio` returns `PortfolioID` and `PortfolioName`. `LinkedPortfolioValuation` accepts `IdentityID`, `PortfolioID`, and `ValueDate`, and returns asset, product, purchase, accrued-interest, exchange-rate, and market-value fields. The provider marks success with status code `0`.

New-customer Grow Wealth onboarding and portfolio creation remain on hold. The supplied examples do not establish that flow.
