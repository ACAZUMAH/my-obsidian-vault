---
type: source
status: active
created: 2026-10-23
updated: 2026-10-24
tags: [livelycura, hrm, holidays, attendance, ghana, decision]
sources:
  - ../../raw/sources/2026-10-24-livelycura-hrm-holidays-no-expected-card.md
  - ../../raw/sources/2026-10-23-livelycura-hrm-holidays-decisions.md
  - ../../raw/sources/2026-10-24-livelycura-hrm-holidays-spec-answers.md
source_date: 2026-10-23
ingested: 2026-10-23
confidence: high
---

# LivelyCura HRM Holidays Decisions

## Source

- Raw file: [LivelyCura HRM holidays decisions](../../raw/sources/2026-10-23-livelycura-hrm-holidays-decisions.md)
- Raw file: [LivelyCura HRM holidays build-spec answers](../../raw/sources/2026-10-24-livelycura-hrm-holidays-spec-answers.md) (2026-10-24)
- Raw file: [LivelyCura HRM holidays, no expected card](../../raw/sources/2026-10-24-livelycura-hrm-holidays-no-expected-card.md) (2026-10-24)
- Date: 2026-10-23
- Author: Product owner decisions (verbatim answers) with the session's research context
- Ingested: 2026-10-23

## Core Claims

- Everyone is off on a public holiday by default; managers mark who is working that day, and new hires are covered automatically. Picking up an open shift on a holiday counts as working, and shortfall views show holiday shifts as "Holiday" with the number working.
- Holidays are stored as one entry per year; "repeats every year" makes the system create next year's entry, and this year's and next year's always exist.
- Attendance corrects itself after holiday changes for people who did not clock in, records who caused the change, and never overwrites a clock-in or a manager's manual correction, including when leave changes.
- Each organization's HR adds Eid and other short-notice or government-moved days with New Holiday when they are declared; there is no SERLP-maintained national list and, since 2026-10-24, no "still to be announced" reminder card. A day HR doesn't add was not a holiday for that organization.
- One 88-country picker on every screen; only nationwide public holidays are imported when the feed covers the country, with an "add your holidays" warning when it does not.
- Holidays have a type (Public holiday or Company day off); imported ones are Public; HR must choose "Every year" or "This year only" when creating one, with nothing pre-selected.
- Loop notifies staff when a holiday is added, moved or deleted or when they are marked as working on it, and shows a "Holidays this year" list.
- Build-spec answers (2026-10-24): a picked-up open shift on a holiday counts only for that shift, and the person's usual shifts stay excused unless a manager marks them as working. Someone not marked as working may clock in on a holiday; the clock-in is recorded as Present and flagged "Clocked in but not marked" on the Who's working page with a one-click "Mark as working". Holiday pay will follow the working list.

## Useful Details

- Before these decisions only staff assigned one by one to a holiday were off, so everyone else was recorded "Absent" on public holidays, while leave already skipped every holiday for everyone.
- The Nager.Date feed gives Ghana 11 days a year and lacks Eid-ul-Fitr and Eid-ul-Adha and one-year government moves; Eid dates are announced about a week ahead.
- Holiday pay is parked for the Payroll feature.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]] owns the holiday rules and the shared "off on a holiday" check.
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]], [[../projects/serlp-mobile|SERLP Mobile]], [[../projects/livelycura-admin-portal|LivelyCura Admin Portal]] and [[../projects/livelycura-loop-app|LivelyCura Loop App]] are the holiday surfaces.
- [[livelycura-hrm-leave-balances-decisions|LivelyCura HRM Leave Balances Decisions]]: leave already treats every organization holiday as free for everyone.

## Contradictions Or Tensions

- The existing holiday assignment records meant "who is off"; under these decisions the per-holiday list means "who is working", so existing data and screens must be reinterpreted. HRM is not in production, so no data migration is planned.

## Open Questions

- Holiday pay rules (statutory pay for public holidays, work on a holiday) when Payroll is designed.
