# Altin Partner Reports Fixes — 2026-10-20 (addendum)

Sanitized addendum to [the Reports tab record](2026-10-18-altin-reports-mobile.md) and [the rate-scaling addendum](2026-10-18-altin-reports-rate-scaling.md), from the same Claude Code session. The user approved these fixes. Evidence: the repository's `docs/reports.md` and the Reports section of its `AGENTS.md`, as of 2026-10-20. The work was still uncommitted on `feature/apps`. No credentials, tokens, organization names, or personal identifiers are included. The user said backend data issues are out of scope, so none are recorded here.

## Fixes

- **Export wording:** the repository docs now say exports print the backend values the web prints, except rates, which are scaled to percentages. This replaces the earlier wording that exports "keep the web's backend values".
- **Date presets:** the six web presets now use the web's day ranges. Last 7 days starts 7 days before today, Last 30 days starts 30 days before, and This month runs to the month's last day. There is still no custom range picker.
- **Stored date range:** the range is computed once when a report is generated and stored with the filters in `useReportFilters`. The query, the scope line and every export use that stored range. Pull and focus refresh fetch it again, first moving it forward if the day has changed, so a report left open past midnight never mixes days.
- **Landscape pages:** Order funnel, Payment attempts and Assignment efficiency print and export as A4 landscape, portrait for the rest, as on the web. `expo-print` takes the paper size from its width and height (842×595 or 595×842), not from CSS.
- **Skeletons:** each report has its own loading-skeleton shape, declared in its `constants`, matching its cards.
- **Courier print lines:** they match the web's `CourierCell`. Statuses are capitalised like the web ("Pending Verification"), the rating is clamped to 5, and a courier without an average rating prints "No ratings". The lines stay plain text because the web's `CourierCell` loses its stylesheet in the print page.
- **ComingSoon:** the unused `ComingSoon` component was deleted (user decision).

## Verification

- `yarn type-check` and prettier pass on the changed files.
- 34 offline checks now run from the session's shared notes folder, outside the repository, because the user removed the repo's test suite. New checks cover landscape pages, the web date presets, the stored range rolling forward after midnight, catalog order, courier print lines and the export paper size.
- Not yet checked on a device: dark mode; Android (native build and every export); PDF and Print for Order volume, Payment attempts, Revenue & commission and Dispatch backlog; CSV for Dispatch backlog; and the 2026-10-20 fixes (landscape PDFs, web date presets, stored range, per-report skeletons).
