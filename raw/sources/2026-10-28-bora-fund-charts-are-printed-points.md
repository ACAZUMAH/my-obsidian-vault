# Bora fund chart series are the values printed on each chart

Date: 2026-10-28
Source: Direct user correction on `bora-capital-backend` (paraphrased; the user was emphatic), plus the implemented change.

## User correction

What each 30 Sep 2026 fact sheet shows:

- **Balanced:** a 1 Year Price Trend month by month from 30-Sept-25 to 30-Sept-26, NAV 0.2169 to 0.2603, and a journey from 30-Sept-22 to 30-Sept-26 with amounts 10,440 to 26,030.
- **Fixed Income:** a trend NAV 0.1946 to 0.2161, and a journey 10,200 to 21,610.
- **Global Balanced:** a trend from 19-Dec-25, NAV 1.0000 to 1.3230, and a journey 10,000 to 13,230.

The seed's series did not match. The user asked where the data came from.

## Where the earlier data came from

The admin portal repo's `docs/fund-nav-history-2026-09-30/*.csv`. Kusantec's script rebuilt a daily NAV from the vector line of each PDF's Journey chart. The agent had used that series as the journey and its last year as the trend. It is not what the sheets print.

## Implementation

- **`navHistory` (1 Year Price Trend, customers)** holds the NAV prices printed on the trend chart.
- **New `sinceInceptionJourney` (admin only)** holds the GH¢ amounts printed on the Journey of GH¢10,000 chart, as `{ date, amount }`. It replaces the uncommitted `sinceInceptionNavHistory`.
- **Validation:**
  - the journey ends on the as-of date at 10,000 × fact-sheet NAV ÷ initial NAV, within GH¢10;
  - amounts are positive;
  - dates fall within the fund's life.
- **How the dates were found.** The charts' tick labels are not in the PDF text layer, so dates came from:
  - each label's exact position in the PDF, mapped onto that chart's axis (calibrated from where the line starts and ends in the rendered page);
  - then the trading day near that position whose price matches the printed value, preferring the month's last trading day.
- **Exceptions.** Most labels sit on a month-end or quarter-end. These do not:
  - Balanced 0.2143 is on 23 Dec 2025; 31 Dec was 0.2078, the base the sheet's YTD uses.
  - Balanced 11,870 is on 14 Apr 2023.
  - The Fixed Income journey points are mostly not on quarter-ends.
  - Global's labels are within 0.0004 of the daily line.
- **Result:**

  | Fund | Trend points | Journey points |
  | --- | --- | --- |
  | Balanced | 9 | 9 |
  | Fixed Income | 8 | 8 |
  | Global Balanced | 10 | 13 |

  They are written inline in the local-only seed with `navPoint` and `journeyPoint` helpers.
- **Verification:** build, plus full Jest at 174 suites and 1318 tests. The user re-runs `seedFundCatalog --replace`.
