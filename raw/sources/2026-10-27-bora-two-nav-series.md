# Bora funds keep two NAV series: 1 Year Price Trend and journey since inception

Date: 2026-10-27
Source: Direct user correction on `bora-capital-backend` (paraphrased; the user was emphatic), plus the implemented change.

## User correction

A fact sheet has two different charts, and they must not be mixed:

- **The Journey of GH¢10,000 (since inception):** the fund's whole growth over the years. Shown in the admin portal only.
- **1 Year Price Trend:** the NAV price within the year. Shown to customers in the customer app.

The user also told the agent to separate the two in the data and to write the seed data out in the fixture file, not load it from CSV files.

## Context

There was one field, `navHistory`. The portal loaded the full since-inception series into it (from the PDF's Journey chart line), and the customer app cut the last year out of that series for its 1 Year Price Trend. The agent had put the full series, then the 1-year slice, into that one field.

## Implementation

- `navHistory` is the 1 Year Price Trend. It holds daily NAV for the year to the as-of date and ends with the fact-sheet NAV; a point more than a year before the as-of date is rejected. Customers read it through `CISFundDetails.navHistory`.
- New `sinceInceptionNavHistory` is the journey since inception: daily NAV from the first price to the as-of date, ending with the fact-sheet NAV.
  - It is on the fund facts model and on the admin `FundFacts` type only.
  - It is optional in `FundFactsInput`; left out, the fund keeps its current journey.
  - It is not on any customer type.
- The local-only seed writes both series inline with a `navPoint(date, nav)` helper:
  - Balanced: 248 trend points and 941 journey points.
  - Fixed Income: 248 trend points and 964 journey points.
  - Global Balanced: 191 of each, from 19 Dec 2025.
  - No CSV is read, and the CSV folder was removed.
- Data source: the daily prices are the portal's 30 Sep price history, read from the Journey chart's vector line. The portal notes say Bora confirmed the July part.
  - Reading the 1 Year Price Trend charts' own lines was tried. Balanced and Fixed Income are a redrawn curve, not one point per day. Global matches its printed labels only to 0.0001–0.0004.
  - So both series use the same daily prices, and the trend is the last year of them.
- Verification: build, plus full Jest at 174 suites and 1316 tests. The user re-runs `seedFundCatalog --replace`, which needs `.env`.
