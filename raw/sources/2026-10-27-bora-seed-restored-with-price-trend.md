# Bora fund seed restored, then updated to 30 Sep with the 1 Year Price Trend

Date: 2026-10-27
Source: Direct user corrections after the 30 Sep seed rewrite (paraphrased; the user was emphatic).

## User corrections

- `navHistory` is the fact sheet's **1 Year Price Trend**, not a single point and not the since-inception series.
- The 30 Sep seed should have been the user's original `scripts/seeds/fundCatalogFixtures.ts` with only what needed changing, not a rewrite. The agent was told to write the original back and add what else needed adding.

## Resolution

- The original July file was restored byte-for-byte from the session's first read (367 lines). Only these changed:
  - the as-of date (30 Sep 2026), NAV and fund size;
  - the YTD and since-inception figures;
  - the sheets' "1H" column, which had been stored as `6M` and became `H1_2026` / "H1 2026". Global Balanced gained it as a new row;
  - the asset allocations, holdings and sectors, set to the 30 Sep values in the original naming style (Petrosol added, ACCESS FD dropped, Fixed Income's KASAPREKO sector became Beverage and Oil & Gas);
  - Fixed Income's Nil exit fee, as `[]`;
  - `navHistory`, now each fund's 1 Year Price Trend: daily prices from 30 Sep 2025 to 30 Sep 2026, read from `scripts/seeds/navHistory/*.csv` (copies of the portal's `docs/fund-nav-history-2026-09-30`). That is 248, 248 and 191 points (Global from 19 Dec 2025), each ending on the printed 30 Sep NAV.
- The original's wording for objective, strategy, disclaimer and benchmark was kept, which reverses the 2026-10-26 "printed text verbatim" choice.
- The original file stored only one NAV point per fund (31 Jul). The 941-point series in the dev export came from the portal import, not from the seed.
- Rules going forward:
  - Update a user's seed in place and keep its conventions. Do not rewrite it.
  - Before changing stored data, look at what the data actually is and what the user calls it.
