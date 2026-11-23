---
type: source
status: active
created: 2026-10-23
updated: 2026-10-23
tags: [livelycura, hrm, leave, labour-act, ghana, decision]
sources:
  - ../../raw/sources/2026-10-23-livelycura-hrm-leave-balances-decisions.md
source_date: 2026-10-23
ingested: 2026-10-23
confidence: high
---

# LivelyCura HRM Leave Balances Decisions

## Source

- Raw file: [LivelyCura HRM leave balances decisions](../../raw/sources/2026-10-23-livelycura-hrm-leave-balances-decisions.md)
- Date: 2026-10-22 to 2026-10-23
- Author: Product owner decisions, relayed as a session summary by the agent
- Ingested: 2026-10-23

## Core Claims

- Annual leave is a hard balance: a request, recording or approval that does not fit is refused for every role. HR's only override is a reasoned manual adjustment in an append-only log.
- Annual leave is charged in each person's own working days from their weekly shifts; off days and organization holidays are free. Staff without weekly shifts use an organization default working week (Monday–Friday, HR-editable).
- One annual allowance per organization, never below 15 working days; individual exceptions are yearly reasoned HR adjustments.
- Mid-year joiners get `ceil(allowance × days employed in the year ÷ days in the year)`, usable at once, from an optional employee employment start date (empty means full year). Mid-year organization starts enter days already taken per employee as one opening adjustment.
- Unused annual days carry over in full with no cap (Labour Act s.31 voids agreements to forgo leave).
- Sick, paternity and compassionate leave have optional, warn-only yearly limits (none by default). Maternity is per pregnancy, default 12 weeks, raisable but never lowerable; longer leave only warns. Unpaid and other leave are counted without a limit.

## Useful Details

- Leave year is the calendar year. Pending requests hold days; rejected, withdrawn, cancelled and expired requests release them; leave ended early returns unused days.
- Labour Act 2003 (Act 651) sections relied on: s.20(1) 15-day minimum, s.22 sickness/pregnancy/public holidays do not reduce the entitlement, s.23 special/compassionate/unpaid leave is not annual leave, s.24 certified sickness during leave is not charged, s.25 recalled workers keep the remainder, s.27(2) record start date, entitlement and dates taken, s.57 maternity at least 12 weeks per pregnancy plus 2 for multiple or abnormal births.
- Review safeguards: holiday changes re-price only current and later years (past years frozen, corrected by adjustment); approval must not drive already-approved future-year leave below zero; balance checks are scoped to the leave's branch; managers cannot adjust their own balance; employment start date edits are audited.
- Unpaid-leave deductions and exit payout are deferred to the Payroll feature.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]] owns the balance rules.
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]], [[../projects/serlp-mobile|SERLP Mobile]] and [[../projects/livelycura-loop-app|LivelyCura Loop App]] are the HRM and employee leave surfaces.

## Contradictions Or Tensions

- Paternity leave and a 14-week maternity minimum appear only in the unpassed Labour Bill; current rules follow Act 651, so paternity has no statutory floor and maternity defaults to 12 weeks.
- The statutory readings are the session's research against the GIPC copy of Act 651; they were not re-verified during ingest.

## Open Questions

- Payroll treatment of unpaid leave and of carried-over days at exit, when the Payroll feature is designed.
- If the Labour Bill passes, the maternity default and a paternity entitlement need revisiting.
