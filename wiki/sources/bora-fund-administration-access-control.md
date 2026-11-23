---
type: source
status: active
created: 2026-09-28
updated: 2026-11-09
tags: [bora-capital, backend, funds, rbac, admin-portal]
sources:
  - ../../raw/sources/2026-09-28-bora-fund-administration-access-control-plan.md
  - ../../raw/sources/2026-09-28-bora-rbac-livelycura-naming-correction.md
  - ../../raw/sources/2026-09-28-bora-resolver-and-service-documentation-correction.md
  - ../../raw/sources/2026-09-28-bora-resolver-domain-logic-and-generated-enum-correction.md
  - ../../raw/sources/2026-10-26-bora-customer-holding-period-exit-fees.md
  - ../../raw/sources/2026-10-26-bora-empty-exit-fees-mean-nil.md
  - ../../raw/sources/2026-10-26-bora-fund-fact-formats-and-sep-seed.md
  - ../../raw/sources/2026-10-27-bora-seed-keeps-full-nav-history.md
  - ../../raw/sources/2026-10-27-bora-seed-restored-with-price-trend.md
  - ../../raw/sources/2026-10-27-bora-two-nav-series.md
  - ../../raw/sources/2026-10-28-bora-fund-charts-are-printed-points.md
  - ../../raw/sources/2026-10-28-bora-journey-cannot-be-cleared.md
  - ../../raw/sources/2026-10-28-bora-production-admin-and-fund-seed.md
  - ../../raw/sources/2026-10-29-bora-production-scripts-follow-paystack-production.md
  - ../../raw/sources/2026-10-30-bora-remaining-funds-production-scripts.md
  - ../../raw/sources/2026-11-03-bora-cdh-balanced-paystack.md
  - ../../raw/sources/2026-11-03-bora-no-same-database-guard.md
  - ../../raw/sources/2026-11-09-bora-fund-nav-history-from-bcl.md
confidence: high
---

# Bora Fund Administration And Access Control

## Source

- Raw files:
  - [2026-09-28-bora-fund-administration-access-control-plan.md](../../raw/sources/2026-09-28-bora-fund-administration-access-control-plan.md)
  - [2026-09-28-bora-rbac-livelycura-naming-correction.md](../../raw/sources/2026-09-28-bora-rbac-livelycura-naming-correction.md)
  - [2026-09-28-bora-resolver-and-service-documentation-correction.md](../../raw/sources/2026-09-28-bora-resolver-and-service-documentation-correction.md)
  - [2026-09-28-bora-resolver-domain-logic-and-generated-enum-correction.md](../../raw/sources/2026-09-28-bora-resolver-domain-logic-and-generated-enum-correction.md)
  - [2026-10-26-bora-customer-holding-period-exit-fees.md](../../raw/sources/2026-10-26-bora-customer-holding-period-exit-fees.md)
  - [2026-10-26-bora-empty-exit-fees-mean-nil.md](../../raw/sources/2026-10-26-bora-empty-exit-fees-mean-nil.md)
  - [2026-10-26-bora-fund-fact-formats-and-sep-seed.md](../../raw/sources/2026-10-26-bora-fund-fact-formats-and-sep-seed.md)
  - [2026-10-27-bora-seed-keeps-full-nav-history.md](../../raw/sources/2026-10-27-bora-seed-keeps-full-nav-history.md)
  - [2026-10-27-bora-seed-restored-with-price-trend.md](../../raw/sources/2026-10-27-bora-seed-restored-with-price-trend.md)
  - [2026-10-27-bora-two-nav-series.md](../../raw/sources/2026-10-27-bora-two-nav-series.md)
  - [2026-10-28-bora-fund-charts-are-printed-points.md](../../raw/sources/2026-10-28-bora-fund-charts-are-printed-points.md)
  - [2026-10-28-bora-journey-cannot-be-cleared.md](../../raw/sources/2026-10-28-bora-journey-cannot-be-cleared.md)
  - [2026-10-28-bora-production-admin-and-fund-seed.md](../../raw/sources/2026-10-28-bora-production-admin-and-fund-seed.md)
  - [2026-10-29-bora-production-scripts-follow-paystack-production.md](../../raw/sources/2026-10-29-bora-production-scripts-follow-paystack-production.md)
  - [2026-10-30-bora-remaining-funds-production-scripts.md](../../raw/sources/2026-10-30-bora-remaining-funds-production-scripts.md)
  - [2026-11-03-bora-cdh-balanced-paystack.md](../../raw/sources/2026-11-03-bora-cdh-balanced-paystack.md)
  - [2026-11-03-bora-no-same-database-guard.md](../../raw/sources/2026-11-03-bora-no-same-database-guard.md)
  - [2026-11-09-bora-fund-nav-history-from-bcl.md](../../raw/sources/2026-11-09-bora-fund-nav-history-from-bcl.md)
- Date: 2026-09-28
- Author: user-approved Codex plan
- Ingested: 2026-09-28

## Core Claims

- Bora administration uses hybrid database-backed authorization: active role permissions and direct user grants are unioned on every request, with exact, namespace-wildcard, and global matching.
- The legacy GraphQL `User.role` remains deprecated compatibility output only. Authorization uses access channels, `platformRoles`, direct `permissions`, staff invitation state, and the `ADMIN_PORTAL` client boundary.
- The live LivelyCura backend is the structural and naming authority for Bora RBAC: use `Role`, `RoleModel`, role operations, `services/roles/permissions`, and a separate staff domain.
- Bora resolver maps reference named, documented, transport-only resolver functions declared above the map. Mapping, filtering, calculation, normalization, and response construction belong to documented domain services. New or rewritten service functions retain repository-style `@description` JSDoc with applicable parameters, errors, and returns.
- Fund administration deliberately stores one record per BCL portfolio, one isolated draft, and one customer-visible publication. Publishing replaces the customer payload and retains no prior version.
- BCL owns the live offer price and, since 2026-11-09, the daily NAV history customers see. Local published facts own analysis. Customer reads continue with a null price and an empty NAV history during provider outages. (Superseded: until 2026-11-09 local published facts also owned NAV history; see Contradictions Or Tensions.)
- The three July 2026 fund records are production fixtures sourced from the supplied PDFs, use only exact printed values and dated NAV points, and skip existing records without mutation. (The dated NAV points were removed from the seeds on 2026-11-09.)
- Customers must see each fund's recommended holding period and redemption (exit) fee tiers before investing (user requirement, 2026-10-26). `CISFundDetails` exposes `recommendedHoldingPeriod` and `redemptionFees { label percentage }` from the published facts; the other fees stay admin-only. `totalAum` is the sheet's "Fund Size". An empty `redemptionFees` list means the sheet says Nil (the portal import saves Nil as an empty list), so the app shows "No exit fee"; the import copies sheet labels verbatim, such as "3 Year" and "≤ 1st year".
- Fund facts are stored in one format (user decision, 2026-10-26). `normalizeAndValidateFundFacts` rewrites known sheet wording and rejects unknown wording. It normalizes the holding period to 'N years'; exit-fee tiers to 'Up to N years' / 'More than N years and up to M years' / 'After N years' / 'All periods', with Nil and all-0% stored as []; period codes to 1M/3M/6M/1Y/YTD/FY<yyyy>/H1_<yyyy>/H2_<yyyy>/SINCE_INCEPTION with derived labels; and asset classes through a closed alias map. Every performance row needs fund and benchmark figures. Since inception must match NAV growth within 0.1 points. Dates are at 00:00 UTC. `publishFund` re-validates the draft. The sheets' '1H' is calendar H1, not trailing 6 months.
- The local-only fund seed is the user's original fixture file updated in place to the 30 Sep 2026 sheets: printed figures in its original wording. Its `sinceInceptionJourney` holds the GH¢ amounts printed on the Journey of GH¢10,000, admin only, written inline (user corrections, 2026-10-27 and 2026-10-28). Until 2026-11-09 its `navHistory` also held the NAV prices printed on each fund's 1 Year Price Trend, shown to customers; that series is now removed (superseded, see below). `updateFund` refuses an explicit `null` or `[]` journey once the fund has one, so the printed amounts cannot be cleared by accident (user decision, 2026-10-28).
- On 2026-10-30, production BCL returned four portfolios: `BBF1100`, `BFI1100`, `BGF1100` and the new `CBF1100` (CDH Balanced Fund). Fixed Income and Global Balanced received production Paystack setup and hidden fund seeds, following the `paystack_production` pattern. Both Fidelity settlement accounts use Paystack's bank code `240100`, because Paystack settles to a bank, not a branch. `CBF1100` gets nothing until its fact sheet and settlement account arrive.
- On 2026-11-03, `CBF1100` (CDH Balanced Fund) received production Paystack setup: a Republic Bank current account, which uses Paystack bank code `110100`. Its bank account name differs from the portfolio name. It still has no fund seed, because there is no fact sheet.
- Production scripts carry no guard against `PROD_MONGODB_URI` equalling `MONGODB_URI`. The user sets both values and removed the guard; agents must not add one, test for one, or flag its absence (user corrections, 2026-10-31 and 2026-11-03).
- Customer fund NAV history loads from BCL, and the stored copy is deleted (user decision, 2026-11-09, after Bora told the client presentation that BCL keeps each fund's NAV history and updates it daily). `CISFundDetails.navHistory(range)` keeps its customer contract and now reads BCL's `CIPortfolioPrices` through `getCISFundNavHistory`, only when selected. `navHistory` left `FundFacts`, `FundFactsInput`, the fund model, the seeds and the production fund scripts, along with the `FundNavPoint`/`FundNavPointInput` types and the NAV-series checks in `validateFundFacts`. Startup migration `REMOVE_FUND_NAV_HISTORY_V1` unsets the stored series in staging and production; the printed points survive only in Bora's PDFs. `sinceInceptionJourney` and `factSheetNav` are unchanged ([raw evidence](../../raw/sources/2026-11-09-bora-fund-nav-history-from-bcl.md)).

## Useful Details

- Registered permissions are `funds.read/update/publish`, `roles.read/create/update`, and `staff.read/create/update`, plus namespace and global wildcards.
- The rejected intermediate names `AccessRole`, `accessRoleIds`, `directPermissions`, and `access.*` are not part of the contract. GraphQL uses `getRole`, `getRoles`, `createRole`, and `updateRole`; staff mutations accept `roleIds` and `permissions`.
- Resolver functions stay outside `Query`, `Mutation`, and field maps so their intent and JSDoc remain reviewable. They delegate without transforming domain data. Nested field resolvers that receive GraphQL field arguments pass parent data and generated arguments directly to the owning service. Reuse generated GraphQL argument types and enums instead of handwritten shapes or string unions. Rewriting a documented service function requires preserving or updating its documentation rather than deleting it.
- Staff invitation completion chooses a password, consumes a one-time code, activates admin access, and revokes existing sessions. Removing admin access preserves customer access and becomes effective through request-time permission resolution.
- New BCL portfolios remain customer-hidden until both published facts and visibility are present.
- Customer comparison and favorites do not add backend state in this phase. Support, marketing, and campaign administration remain later work.
- Verification on 2026-09-28 completed GraphQL generation, formatting, TypeScript build, 107 Jest suites/551 tests, and the production audit. The audit retains only two repository-approved temporary lodash exceptions expiring 2026-10-15.
- BCL NAV history (2026-11-09): `CIPortfolioPrices` takes the BCL portfolio ID (such as `BBF1100`) in `<Request><PortfolioID>…</PortfolioID></Request>` and returns `{ Date: "05 Nov 2026", Price }` rows, newest first, business days only. `getCISFundPriceHistory` goes through `fetchBclData`, normalizes rows with `normalizeCISPrice` to `{ date: UTC midnight, nav }` (one per date, oldest first), and caches them as `cis:prices:<portfolioId>`: fresh for 30 minutes, last known prices kept 7 days for outages, empty lists never stored. Ranges count back from the latest BCL price. With BCL down and nothing cached, `navHistory` is `[]` with a logged warning. `CISFundDetails` carries an internal, non-GraphQL `portfolioId`. The admin portal must stop sending `navHistory` and ship with the backend release (`docs/frontend-handoff-2026-11-09.md`); the customer app needs no change. Verification: `tsc`, `yarn build`, and full Jest at 193 suites/1601 tests under Node 26.12.1; no live BCL call.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-grow-wealth-existing-customer-valuations|Bora Grow Wealth Existing Customer Valuations]]
- [[bora-production-ci-audit-scope|Bora Production CI Audit Scope]]

## Contradictions Or Tensions

- The approved plan used `AccessRole` naming, but the later direct correction supersedes it with the live LivelyCura `Role`/`platformRoles` structure. The deprecated legacy role output remains queryable and is never an authorization source.
- The initial implementation also inlined resolver functions and omitted service JSDoc; the later direct correction supersedes that structure with named resolver functions and documented services. A follow-up correction moved CIS transformation and NAV-range logic out of field resolvers and replaced a handwritten chart-range union with the generated `FundChartRange` enum.
- Paper fact sheets include chart lines without exact point labels; those visual estimates are intentionally excluded from production seed data.
- NAV history ownership changed on 2026-11-09. Earlier records made the stored `navHistory` the customer chart: the full daily series ([2026-10-27 full history](../../raw/sources/2026-10-27-bora-seed-keeps-full-nav-history.md)), then the 1 Year Price Trend ([2026-10-27 price trend](../../raw/sources/2026-10-27-bora-seed-restored-with-price-trend.md), [2026-10-27 two series](../../raw/sources/2026-10-27-bora-two-nav-series.md)), then the points printed on that chart ([2026-10-28 printed points](../../raw/sources/2026-10-28-bora-fund-charts-are-printed-points.md)), with a rule never to shrink it silently. The user's 2026-11-09 decision ([raw evidence](../../raw/sources/2026-11-09-bora-fund-nav-history-from-bcl.md)) supersedes all of these: BCL's daily prices are the only customer NAV-history source, and the stored series is deliberately deleted. Current best interpretation: high confidence for the contract and code; medium for the data, because BCL's history depth is unknown and no live call has been made, so a range may show fewer points than the sheets printed.

## Open Questions

- What backend contracts will later phases use for customer-support tickets, marketing/news administration, and scheduled push, email, and SMS campaigns?
- When will new-customer Grow Wealth creation resume, and which BCL operations will authorize it?
- How far back does BCL's `CIPortfolioPrices` history go for each fund? The 2026-11-09 sample covered only 19 Oct to 5 Nov 2026.
