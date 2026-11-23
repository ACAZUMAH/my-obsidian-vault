# Bora fund seed keeps the full daily NAV history

Date: 2026-10-27
Source: Direct user correction after running `seedFundCatalog --replace` on the dev database (paraphrased; the user was emphatic).

## What happened

The 30 Sep seed carried only the printed as-of NAV point. This followed the earlier "printed values only, never chart estimates" seed rule and the 2026-10-26 choice that "seed keeps a single printed point". After the user re-seeded with `--replace`, each fund's `navHistory` held only the 30 Sep point. The daily series the dev funds had before were gone: 941 points for Balanced, 964 for Fixed Income, and 191 for Global Balanced. The customer NAV chart then had nothing to draw.

## User correction

Updating the seed to 30 Sep was meant to keep the NAV history, not drop it.

## Resolution

- The local-only seed now loads each fund's full daily series from `scripts/seeds/navHistory/<fund>.csv`. The files are copies of the admin portal's `docs/fund-nav-history-2026-09-30/{balanced,fixed-income,global-balanced}.csv`. They are identical to what dev held before the re-seed, and each ends on the sheet's printed 30 Sep NAV (0.2603, 0.2161, 1.3230).
- The series pass the fact validator: points lie within inception to as-of date, and the as-of point equals the fact-sheet NAV. The user re-runs `seedFundCatalog --replace` to restore them on dev.
- Rule going forward: a seed or data replacement must not drop existing NAV history. If a change would shrink `navHistory`, say so explicitly and get confirmation first.
