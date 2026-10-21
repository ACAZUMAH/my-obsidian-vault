# Altin Partner Reports Landscape Sheet and Device Check — 2026-10-20 (addendum)

Sanitized addendum to [the 2026-10-20 Reports fixes](2026-10-20-altin-reports-fixes.md), from the same Claude Code session and fix pass. Evidence: the "Deliberate differences from the web" and "Verification" sections of the repository's `docs/reports.md`, and its `AGENTS.md` Reports section, as of 2026-10-20. No credentials, tokens, organization names, or personal identifiers are included.

## Deliberate difference: landscape sheet

- Landscape reports (Order funnel, Payment attempts, Assignment efficiency) now print on a landscape-sized 297 × 210 mm sheet.
- The web keeps its 210 mm sheet inside a landscape page and lets the browser shrink the overflowing table. iOS clips it instead, which cut off Payment attempts' last columns.
- The repository lists this among its deliberate differences from the web exports.

## Device check of the 2026-10-20 fixes

Read-only, on production in the iOS simulator, with the same organizations as the 2026-10-18 check:

- Presets: Last 7 days showed the web's range (Oct 13 – Oct 20, 2026), and the PDF printed the matching start date.
- Landscape: the Assignment efficiency PDF (842×595, 2 pages) and its Print sheet. The Payment attempts PDF fit all 14 columns after the sheet change.
- Skeletons: Assignment efficiency, Revenue & commission and Dispatch backlog matched their cards.
- Dispatch backlog: PDF (portrait, 2 pages), CSV (BOM, web rows) and Print.
- 37 offline checks now run outside the repository.

## Still not checked on a device

- dark mode;
- Android (native build and every export);
- PDF for Order volume and Revenue & commission, and the Order funnel PDF since the landscape sheet change;
- Print for Order volume, Order funnel, Payment attempts, Revenue & commission and Fleet leaderboard;
- COD reconciliation and Receivables aging data and exports.
