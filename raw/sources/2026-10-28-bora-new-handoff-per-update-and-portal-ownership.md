# Bora: a new handoff for each update, and the admin portal is not ours

Date: 2026-10-28
Source: Direct user correction on `bora-capital-backend` (paraphrased; the user was emphatic), plus the resulting change.

## User correction

- **New update, new file.** The user has said repeatedly that a new backend update gets a new handoff file. They had already sent `docs/frontend-handoff-2026-10-24.md`. The agent had extended it with the `sinceInceptionJourney` change, relying on an earlier answer that it was unsent.
- **The admin portal is not ours.** The user and this agent did not build it, and parts of it are wrong. One example is the NAV CSVs the agent had used as seed data instead of the PDFs the user supplied.
- **Warn the frontend developer.** The handoff should tell the frontend developer to be careful, because he keeps updating the database with wrong data.

## Outcome

- **2026-10-24 handoff restored.** It is back to its committed `47d0850` content.
- **New file: `docs/frontend-handoff-2026-10-28.md`.** It covers:
  - the two chart series;
  - rules for writing fund data;
  - portal and app fixes;
  - the 24 Oct items `develop` still lacks.
- **Basis for the fixes.** They come from an audit of portal `develop` `4e95a26` and app `develop` `e498168`. The audit had five auditors, an independent verifier per area, and a completeness critic. It checked the code against Bora's 31 Jul and 30 Sep PDFs and the backend.
- **Correction to the earlier record.** `2026-10-28-bora-fund-charts-are-printed-points.md` says "Kusantec's script" built the CSVs. The script lives in the admin portal repository (`Kusantec/bora-admin-portal`), which the frontend developer builds. It is not the user's work.

## Audit findings that wrote, or could write, wrong fund data

- **`scripts/load-fund-nav-history.ts` publishes to staging with no review.**
  - Commands: `load`, `refresh`, `import-factsheet --apply` and `attach-pdf --apply`.
  - `refresh` merges 41 chart-traced daily prices into the printed trend.
- **The `docs/fund-nav-history-*` CSVs are not Bora prices.** They are the points of the Journey chart's line, converted to NAV. The portal docs call them "confirmed by Bora".
- **`setSixMonths` and `fixSixMonths` write a calculated 6M return** with no benchmark.
- **Integration tests write to real data.**
  - Suite 08 deletes every fund's fact-sheet upload records on `INTEGRATION_MONGODB_URI` before sign-in.
  - Suite 03 publishes made-up facts on the real `BFI1100`.
- **The import mishandles the charts and the sheet date.**
  - It merges one as-of point into the old trend instead of replacing it with the printed labels.
  - It never sends the journey.
  - It applies allocations without the sheet's date.
  - It attaches a PDF without checking its printed fund or date.

## Backend issues raised with the user, not with the frontend

- **An explicit `null` or `[]` for `sinceInceptionJourney` erases the stored journey.**
- **Re-seeding before deploying the journey change loses the journey.** A save and publish on the older backend strips the journey (Mongoose strict mode).
- **Global's 1-year problem.** Global's chart is titled "Price Trend since Inception". After 19 Dec 2026, the backend's 1-year rule would reject printed labels older than a year.
- **Possibly stale returns.** The 1M and 3M figures on the 30 Sep sheets equal the 31 Jul sheets' figures. Bora should confirm them.
