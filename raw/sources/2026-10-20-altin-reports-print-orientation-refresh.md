# Altin Partner Reports Print Orientation and Undated Refresh — 2026-10-20 (addendum)

Sanitized addendum to [the 2026-10-20 Reports fixes](2026-10-20-altin-reports-fixes.md), from the same Claude Code session and the same user-approved fix pass. Evidence: the "Date range", "PDF" and "Verification" sections of the repository's `docs/reports.md`, as of 2026-10-20. No credentials, tokens, organization names, or personal identifiers are included.

## Details

- **Print orientation:** Print passes the matching orientation to the iOS print sheet: landscape for Order funnel, Payment attempts and Assignment efficiency, portrait for the rest. It matches the PDF, whose A4 size comes from `expo-print`'s width and height (842×595 or 595×842).
- **Undated refresh:** Receivables aging has no date filter. Pull and focus refresh always just refetch it; there is no stored range to move forward.
- The docs list print orientation among the 2026-10-20 fixes that still need a device pass.
