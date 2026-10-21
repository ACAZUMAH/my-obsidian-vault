# Altin Partner Reports Tab — 2026-10-18

Sanitized record of the user's decisions and the resulting build of the Altin Partner Mobile Reports tab in a Claude Code session on `feature/apps`. Evidence: the repository's `docs/reports.md` and the "Reports (2026-10-18)" section of its `AGENTS.md`, both written that day, plus the session's research notes. The work was uncommitted on top of `9ea69b1` when recorded. No credentials, tokens, organization names, or personal identifiers are included.

## What was built

- The Reports tab replaces the ComingSoon placeholder. It lists only the reports the active membership may see.
- Ten reports, from the web partner app (`../altin-web-apps/apps/partner`, `modules/ProtectedModules/Reports/**`, `lib/graphqlQuerySchemas/reportSchema.ts`):
  - SHIPPER: Order volume & status mix, Order funnel & delivery SLA, Payment attempts, Revenue & commission, Receivables aging, Dispatch backlog.
  - FLEET: Courier earnings & payouts, Assignment efficiency, COD reconciliation, Fleet leaderboard.
- Each report has a named `permissionRules` entry (its report permission, granted by `ADMIN`, plus its organization type). The catalog, `withPermission` on the registered route, and the query `skip` all use it.
- Ownership: `src/reports` owns the tab, the catalog, and the shared report pieces. Each report is a sibling feature folder holding its operation hook, screen hook, builder, constants, interfaces and screen. Report screens render `ReportScreenLayout` with `useReportFilters` and `useReportScreen`.
- One builder per report returns `{ preview, print, csv }` from the same API data.
- Filters match the web defaults (Today, Daily, All sources, Top 10) and change the report only on "Generate report". Dates use the six web presets only: no custom range picker. The schema's `courierId` filters are not exposed, as on the web.
- On screen, values the API didn't return show "—", never 0. A total is known only if every part is known. Rates are computed from counts because the API's rate unit is undocumented; exports print the backend rates, as the web does.

## User decisions and corrections

- The first build showed the report as tables with horizontal scrolling and a separate status table. The user corrected it: the mobile screen is designed for mobile, with one card per record (a period, a courier, a leaderboard) holding all its figures and status breakdowns together. No horizontal scrolling and no separate status tables.
- The totals card has no "Summary" label.
- Print, PDF and CSV are not a mobile design: they must be what the web report exports, matching the web's `PrintAdminReportModal` page and `exportToCSV` rows, columns, formatting and file names.
- Reports are built in the web Reports page order.
- Revenue & commission is kept, with a caveat, even though the schema deprecates `orderRevenueCommissionSummary` (it overcounts cash COD; its replacement `revenueSummary` is super-admin only).

## Exports

- PDF: `expo-print` renders the web's print page to an A4 PDF, named like the web's (for example `Courier_Earnings_Payout_Ops_<date>.pdf`), and shares it with `expo-sharing`.
- Print sends that same PDF to the iOS print sheet. Printing the HTML directly clipped the web's fixed 210 mm sheet onto two pages. Cancelling the sheet is not an error.
- CSV: the web's `exportToCSV` output, every value quoted, with the web file name.
- Exports are written to `Caches/reports`, cleared before each export.
- Deliberate, documented differences from the web:
  - the CSV starts with a UTF-8 byte-order mark, written as bytes because the native string write drops a leading U+FEFF, so Excel reads "GH₵";
  - embedded quotes are doubled;
  - CSV headings are collected from every row, because the web drops status columns missing from its first row;
  - couriers print as plain lines (name, phone, status, group, rating), because the web's `CourierCell` loses its stylesheet in the print page;
  - the QR placeholder prints as an empty box, because iOS does not draw CSS gradients in PDFs.
- Kept exactly as on the web: the "Admin Reports" business name, per-page date styles, "0%" vs "--" for missing rates, and Fleet leaderboard's untitled first table.

## Environment lesson

- `expo-print` and `expo-sharing` are native modules. A binary built before they were added red-boxes with `Cannot find native module 'ExpoPrint'`.
- The user's `yarn ios` rebuild failed silently in `pod install` because the shell had no UTF-8 locale. The rebuild that worked set `LANG=en_US.UTF-8` (`LANG=en_US.UTF-8 CI=1 npx expo run:ios --no-bundler`, reusing the user's Metro). Confirm that a native rebuild actually happened before diagnosing missing native modules.

## Verification

- `yarn type-check` and prettier passed on the changed files.
- 29 offline checks ran from a scratch folder, not committed, because the user had removed the repository's test suite. They covered every builder against its web mapping, HTML escaping and the CSV format, missing values, catalog permission and organization-type rules, the Apollo query hook outcomes, the export service with stubbed native modules, and the one-export-at-a-time guard.
- Checked read-only on production in the iOS simulator: Courier earnings only, including the cards, filters, Print, PDF and CSV, with the generated files read back from the app cache.
- Not yet checked live: the other nine reports and dark mode. The SHIPPER reports need a SHIPPER organization selected.

## Not built

- Custom date ranges, the courier filter, `courierPayoutThroughputOps`, and Search entries for individual reports.
