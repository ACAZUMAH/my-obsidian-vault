# Altin Partner Reports Rate Scaling and Live Check — 2026-10-18 (addendum)

Sanitized addendum to [the Reports tab record](2026-10-18-altin-reports-mobile.md), from the same Claude Code session. Evidence: the "Deliberate differences from the web" and "Verification" sections of the repository's `docs/reports.md`, the Reports section of its `AGENTS.md`, and `src/reports/helpers/web.ts`, as of 2026-10-18. The work was still uncommitted on `feature/apps`. No credentials, tokens, organization names, or personal identifiers are included.

## User decision: exports scale rate fractions to percentages

- The live check found that the backend sends rates as fractions: an `acceptanceRate` of 0.5275 means 52.75%. The web prints these values unscaled, so its export shows "0.53%" for a 52.75% acceptance rate, 100 times too small.
- The user decided that the mobile exports scale them. Print, PDF and CSV for Assignment efficiency (acceptance, rejection and expiry rates), Payment attempts (success, failure and retry rates) and Revenue & commission (commission rate) now multiply the rate by 100.
- `fractionToPercent` (`src/reports/helpers/web.ts`) moves the decimal point two places in the backend's Decimal string instead of multiplying a float, so no rounding creeps in. Missing or non-numeric rates pass through unchanged.
- The web's percent format and "%" column headings are otherwise unchanged. The repository records this as the first of its deliberate differences from the web exports.
- Checked on the device: Assignment efficiency printed 54.06% / 11.31% / 30.04% in both the PDF and the CSV.

## Live check, read-only, on production in the iOS simulator

- Checked: every report screen, the Reports tab with one card per report, and the filters. One FLEET and one SHIPPER organization were used.
- Exports read back from the app cache:
  - PDF, CSV and Print for Courier earnings;
  - PDF and CSV for Assignment efficiency, Fleet leaderboard (4 pages) and Order funnel;
  - CSV for Order volume, Payment attempts and Revenue & commission.
- COD reconciliation and Receivables aging returned the server's "Reports temporarily disabled". Their error state was checked; their data was not.
- Order funnel returns 0 for every stage and SLA sample, even on a day with deliveries. This is backend data.
- Not checked: dark mode, and Dispatch backlog's exports.
