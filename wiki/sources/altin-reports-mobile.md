---
type: source
status: active
created: 2026-10-18
updated: 2026-10-20
tags: [altin, mobile, reports, exports, livelycura]
sources:
  - ../../raw/sources/2026-10-18-altin-reports-mobile.md
  - ../../raw/sources/2026-10-18-altin-reports-rate-scaling.md
  - ../../raw/sources/2026-10-20-altin-reports-fixes.md
  - ../../raw/sources/2026-10-20-altin-reports-print-orientation-refresh.md
  - ../../raw/sources/2026-10-20-altin-reports-landscape-sheet-device-check.md
confidence: high
---

# Altin Reports Mobile

## Source

- Raw file: [Altin Partner Reports tab](../../raw/sources/2026-10-18-altin-reports-mobile.md)
- Raw file: [Altin Partner Reports rate scaling and live check](../../raw/sources/2026-10-18-altin-reports-rate-scaling.md)
- Raw file: [Altin Partner Reports fixes](../../raw/sources/2026-10-20-altin-reports-fixes.md)
- Raw file: [Altin Partner Reports print orientation and undated refresh](../../raw/sources/2026-10-20-altin-reports-print-orientation-refresh.md)
- Raw file: [Altin Partner Reports landscape sheet and device check](../../raw/sources/2026-10-20-altin-reports-landscape-sheet-device-check.md)
- Date: 2026-10-18 to 2026-10-20
- Author: user, through an Altin Partner Mobile Claude Code session; repository `docs/reports.md` and `AGENTS.md`
- Ingested: 2026-10-18; updated 2026-10-20

## Core Claims

- The Reports tab is built and replaces the old placeholder; the unused `ComingSoon` component was deleted (user decision, 2026-10-20). The tab lists the ten web reports the active membership may see: six SHIPPER, then four FLEET, in the web Reports page order (user decision).
- User correction: the report screen is mobile-native. One card per record (a period, a courier, a leaderboard) holds all its figures and status breakdowns. No horizontal-scrolling tables, no separate status tables, and no "Summary" label on the totals card. Each report's loading skeleton has the shape of its own cards.
- User correction: Print, PDF and CSV are the web exports, matching the web's `PrintAdminReportModal` page and `exportToCSV` rows, columns, formatting and file names. They are not a mobile design. Order funnel, Payment attempts and Assignment efficiency use A4 landscape, the rest portrait, as on the web; Print passes the same orientation to the print sheet.
- Documented deliberate differences from the web exports: rate fractions scaled to percentages, a UTF-8 BOM written as bytes, doubled embedded quotes, CSV headings from all rows, plain-text courier lines, and a 297 × 210 mm sheet for landscape reports.
- User decision: exports scale the backend's rate fractions to percentages. The backend sends rates as fractions (0.5275 = 52.75%), and the web prints them unscaled ("0.53%"). Print, PDF and CSV for Assignment efficiency, Payment attempts and Revenue & commission multiply them by 100 with `fractionToPercent`. All other export values are the ones the web prints.
- Dates use the six web presets with the web's day ranges. The range is computed once per "Generate report", stored in `useReportFilters`, and shared by the query, the scope line and every export.
- User decision: Revenue & commission stays, with a caveat that the schema deprecates it.
- Lesson: `pod install` fails silently without a UTF-8 locale, so confirm that a native rebuild actually happened.

## Useful Details

- Each report has a named `permissionRules` entry (permission plus organization type) shared by the catalog, `withPermission`, and the query `skip`.
- One builder per report returns `{ preview, print, csv }` from the same data. Screens use `ReportScreenLayout`, `useReportFilters` and `useReportScreen`; each report's `constants` declares its skeleton shape.
- On screen, missing values show "—", never 0, and rates are computed from counts. Exports print the backend's rate values, scaled to percentages, rather than the screen's count-derived rates.
- `fractionToPercent` (`src/reports/helpers/web.ts`) moves the decimal point two places in the backend's Decimal string, so no float rounding creeps in. Missing or non-numeric rates pass through unchanged. The web's percent format and "%" headings are otherwise kept. On the device, Assignment efficiency printed 54.06% / 11.31% / 30.04% in both the PDF and the CSV.
- Date presets: Last 7 days starts 7 days before today, Last 30 days starts 30 days before, and This month runs to its last day. Filters apply only on "Generate report". Pull and focus refresh move a stored range forward when the day has changed, so a report left open past midnight never mixes days. Receivables aging has no date filter, so refresh always just refetches it.
- `expo-print` takes the paper size from its width and height (842×595 landscape, 595×842 portrait), not from CSS. Print passes the matching orientation to the iOS print sheet, landscape for the three wide reports.
- Print prints the generated PDF; printing the HTML directly clipped the web's 210 mm sheet.
- Landscape reports print on a 297 × 210 mm sheet. The web keeps its 210 mm sheet inside a landscape page and lets the browser shrink the overflowing table; iOS clips it instead, which cut off Payment attempts' last columns. After the change, the device check showed all 14 columns.
- Courier print lines follow the web's `CourierCell` wording: statuses capitalised like the web ("Pending Verification"), the rating clamped to 5, and "No ratings" without an average. They stay plain text because the web cell loses its stylesheet in the print page.
- The BOM is written as bytes because the native string write drops a leading U+FEFF.
- Live check, 2026-10-18 (read-only, production): every report screen, the tab and the filters, plus exports for seven reports, read back from the app cache. COD reconciliation and Receivables aging data and exports were not checked.
- Device check of the 2026-10-20 fixes, 2026-10-20 (read-only, production): the Last 7 days preset matched the web's range; the Assignment efficiency landscape PDF and Print sheet and the Payment attempts PDF fit their pages; the Assignment efficiency, Revenue & commission and Dispatch backlog skeletons matched their cards; Dispatch backlog's PDF, CSV and Print worked. 37 offline checks run outside the repository.
- Not yet checked on a device: dark mode; Android; PDF for Order volume and Revenue & commission, and Order funnel's PDF since the sheet change; Print for Order volume, Order funnel, Payment attempts, Revenue & commission and Fleet leaderboard; COD reconciliation and Receivables aging data and exports.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[altin-permission-gating|Altin Permission Gating]].
- [[altin-theme-navigation-runtime-corrections|Altin Theme, Navigation, and Runtime Corrections]], which put Reports in the tab bar.
- [[altin-profile-support|Altin Profile and Support]], for the related native-module lesson.

## Contradictions Or Tensions

- Supersedes the project page's statement that the Reports tab is a placeholder.
- The first build used horizontally scrolling tables and a separate status table; the user's correction replaced them with one card per record.
- Revenue & commission uses a deprecated query that overcounts cash COD; its replacement is super-admin only.
- Rate scaling is a user-approved departure from "exports identical to the web", because the web's rate values are 100 times too small. On 2026-10-20 the repository docs were corrected to say exports print the web's values except rates, which are scaled; the earlier "keep the web's backend values" wording is gone.
- The first ingest recorded that only Courier earnings had been checked live. The later live check covers every report screen.

## Open Questions

- Do dark mode, Android, and the remaining unchecked exports hold up in the next device pass?
- Should the web partner app fix its unscaled rates, so the two apps' exports match again?
- Should custom date ranges, the courier filter, or per-report Search entries be added?
- When will a non-deprecated revenue report be available to partner members?
