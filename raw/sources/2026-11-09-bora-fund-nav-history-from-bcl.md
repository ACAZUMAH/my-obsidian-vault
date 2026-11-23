# Bora fund NAV history loads from BCL; the stored series is removed

Date: 2026-11-09
Source: Direct user decision on `bora-capital-backend` (paraphrased), the BCL request and response sample the user supplied, plus the change implemented in that session. Uncommitted at recording.

## User decision

At the last client presentation, Bora said BCL already keeps each fund's NAV history and updates it every day. The user decided that customers' fund NAV history loads from BCL and that the stored copy comes off the database.

## BCL contract (user-supplied)

- Request: `POST {base}/api/partner/fetchdata` with `RequestID` `CIPortfolioPrices` and `xmlDetail` `<Request><PortfolioID>…</PortfolioID></Request>`.
- Success: `Status` is `[{ Status: "0", Description: "Success" }]`. `Data` is a list of `{ Date, Price }` rows, for example `{ "Date": "05 Nov 2026", "Price": 0.26558655760761 }`, newest first, business days only.
- The sample ran from 19 Oct to 5 Nov 2026. How far back BCL's history goes is unknown.

## Implementation

- New `src/services/portfolios/CIS/getCISFundPriceHistory.ts` calls the shared `fetchBclData` with `CIPortfolioPrices` and the fund's `portfolioId` (the BCL portfolio ID, such as `BBF1100`), XML-escaped.
- `normalizeCISPrice` (CIS helpers) turns each row into `{ date, nav }`: the date at UTC midnight, `nav` from `Price`. The series keeps one point per date, oldest first.
- Results go into the shared cache `cis:prices:<portfolioId>` (constant `cisPriceHistoryCache`). They are fresh for 30 minutes, and the last known prices are kept for 7 days in case BCL is down. Empty lists are never stored.
- The customer GraphQL contract is unchanged: `CISFundDetails.navHistory(range: FundChartRange = ONE_YEAR): [CustomerFundNavPoint!]!` returning `{ date, nav }`.
  - The field resolver now calls `getCISFundNavHistory({ portfolioId, range })`. It loads only when the field is selected, and ranges count back from the latest BCL price.
  - When BCL fails and nothing is cached, it returns `[]` and logs a warning, so the rest of the fund still loads, as `offerPrice: null` does.
  - `CISFundDetails` carries an internal `portfolioId` that is not a GraphQL field.

## Removed

- `navHistory` from `FundFacts` and `FundFactsInput`, the GraphQL types `FundNavPoint` and `FundNavPointInput`, and the fund model field.
- The `normalizeNavSeries` checks in `validateFundFacts`: the as-of point equal to `factSheetNav`, points within the fund's life, and no point more than a year before the as-of date.
- The `navHistory` arrays and `navPoint` helpers in the gitignored local `scripts/seeds/fundCatalogFixtures.ts` and in the `scripts/funds_production/` constants and helpers.
- Unchanged: `sinceInceptionJourney` (the admin-only Journey of GH¢10,000) and `factSheetNav`.

## Migration

New startup migration `REMOVE_FUND_NAV_HISTORY_V1` (`scripts/migrations/removeFundNavHistory_V1.ts`) unsets `draftFacts.navHistory` and `publishedFacts.navHistory` on the raw funds collection when deployed, in staging and production. This is a permanent deletion the user asked for. The printed points remain in Bora's fact-sheet PDFs.

## Handoff

New `docs/frontend-handoff-2026-11-09.md`. The customer app needs no change. The admin portal (the frontend developer's work) must stop selecting and sending `navHistory` and ship together with this backend release. It can read the customer chart for visible funds through `getCISPortfolioById`.

## Verification

`tsc` clean, `yarn build` passes, and full Jest passes at 193 suites and 1601 tests under Node 26.12.1. No live BCL call was made.
