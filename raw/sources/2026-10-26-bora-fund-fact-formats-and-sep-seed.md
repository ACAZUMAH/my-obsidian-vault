# Bora fund facts: one stored format, stricter validation, 30 Sep seed

Date: 2026-10-26
Source: Direct user request and decisions on `bora-capital-backend` (`feature/updates`), plus a field-by-field audit of the dev `funds` export against the 30 Sep 2026 fact sheets, and the implemented change.

## Request

The frontend developer's admin-portal testing overwrote the dev funds with wrong data in mismatched formats. The user asked to review the seeds, write validators to prevent this, update the seeds to the 30 Sep sheets, and re-seed.

## Audit findings

- The portal's staging scripts (`import-factsheet --apply`, `refresh`) published the 30 Sep sheets on 2026-10-23. Nearly every number matched the sheets. The problems were these:
  - A computed `6M` return that no sheet prints, with no benchmark: Balanced 19.79, Fixed Income 4.70. It came from `setSixMonths`, and the portal README says Bora asked for it.
  - A daily NAV series reconstructed from the PDF chart line (941, 964, and 191 points). It agrees with the printed returns, but Bora did not supply it as a price list.
  - Sheet wording copied verbatim: '3 Year', '≤ 1st year', 'FDs', 'Tbills', 'Cash (GH¢)', upper-case sectors, '1H', 'FY - 2025'.
  - Explicit nulls for facts not on the sheet.
- The sheets' "1H" is calendar H1 2026, not trailing 6 months. It is identical on the Jul and Sep sheets and equals 31 Dec → 30 Jun exactly. The July seed had mapped it to `6M`, which showed H1 to customers as a 6-month return.
- Bora sheet issues to confirm with Bora:
  - "3M" and "1M" are unchanged from July and match Q1 2026.
  - The Balanced price is labelled "31ST AUG 2026", but the evidence says 30 Sep.
  - Global Balanced page 2 is headed "31ST AUGUST 2026".
  - The benchmark figures are inconsistent between the Jul and Sep sheets.
  - Global Balanced inception is 25 Nov 2025, but pricing starts 19 Dec 2025.

## User decisions

1. Normalize known sheet wording to one stored format and reject unknown wording. Sector labels get only case and currency clean-up, because sectors change from sheet to sheet.
2. Every performance row needs both a fund and a benchmark figure.
3. NAV series are allowed with range checks. The seed keeps the single printed as-of point.
4. Seed objective, strategy, and disclaimer use the printed text verbatim. The implementation also uses the printed benchmark name.

## Implementation

- **`normalizeAndValidateFundFacts`**, through `src/services/funds/helpers/factFormats.ts`:
  - Holding period becomes "N years", 50 at most.
  - Exit-fee tiers become "Up to N years", "More than N years and up to M years", "After N years", or a single "All periods". They must be ordered with no gaps. A printed % in a label must match the tier's percentage. All-0% or Nil is stored as `[]`.
  - Period codes are 1M, 3M, 6M, 1Y, YTD, FY<yyyy>, H1_/H2_<yyyy>, and SINCE_INCEPTION. The label is derived from the code. A half-year without a year must have ended by the as-of date. Full-year and half-year periods must lie within the fund's life.
  - Asset classes use a closed alias map. Sectors are tidied. Holding names get bracketed classes expanded and cash rows standardized.
  - Other rules:
    - every performance row needs fund and benchmark figures;
    - since inception ≈ NAV growth within 0.1 points;
    - dates are at 00:00 UTC, with inception ≤ as-of ≤ today;
    - NAV points lie within [inception, as-of];
    - unit prices are > 0;
    - the benchmark name is required;
    - labels are not blank;
    - optional nulls are dropped.
- **`publishFund`** re-validates and normalizes the draft (lean read), so a draft saved before the rules existed cannot go live in the old wording.
- **The local-only seed** now holds the 30 Sep sheets. Holding names follow the portal's rule: the issuer as printed, with the class appended only when an issuer repeats, so re-imports match. `--replace` overwrites existing funds' published facts and clears drafts and draft PDFs. It refuses, before writing anything, if a published PDF is dated differently from the new facts.
- **Handoff:** `docs/frontend-handoff-2026-10-24.md` section 5 tells the portal to:
  - stop calculated rows;
  - replace the performance list as a whole;
  - map "1H" to H1_<year>;
  - compare in the stored format;
  - send null for optional facts a sheet does not print;
  - check before loading chart-reconstructed NAV series again.
- **Verification:** build, plus full Jest at 172 suites and 1251 tests. The re-seed against the dev database is for the user to run, because it needs `.env`.
