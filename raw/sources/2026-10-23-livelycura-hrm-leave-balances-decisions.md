# LivelyCura HRM: leave balances decisions (decided, not yet built)

- Date: 2026-10-22 to 2026-10-23
- Author: the product owner, answering plain-language options one at a time in a LivelyCura Claude Code session
- Recorded from: the session agent's summary of those answers, relayed for promotion on 2026-10-23 (a faithful summary, not a verbatim transcript)
- Feature: LivelyCura HRM "Leave balances"
- Status when recorded: decided, not yet built; no repository design document or code exists yet

## The owner's decisions

1. Over balance: an annual leave request, recording or approval that does not fit the balance is refused for everyone (employees and managers). HR's only override is a manual adjustment with a written reason, kept in a log that cannot be edited.
2. Opening balances: when an organization starts mid-year, HR enters per employee the days already taken this year; it becomes one adjustment.
3. Joiners mid-year: a share of the yearly allowance (allowance × days employed in the year ÷ days in the year, rounded up), usable straight away; an optional employment start date on the employee (empty = full year).
4. Counting days: annual leave is charged in each person's own working days from their weekly shifts (the Labour Act's literal "working days"); off days and organization holidays are not charged; staff without weekly shifts use an organization default working week, Monday–Friday, which HR can change.
5. One annual figure per organization (never below 15 working days); exceptions for individual staff are given as yearly HR adjustments with a reason.
6. Sick, paternity and compassionate leave: optional yearly limits that only warn (never block), empty (no limit) by default. Maternity: per pregnancy, default 12 weeks (HR can raise, never lower); a longer one only warns. Unpaid and other leave are counted with no limit.

## Fixed rules from the research

Ghana Labour Act 2003 (Act 651), as verified in the session against the GIPC copy: <https://www.gipc.gov.gh/wp-content/uploads/2023/05/LABOUR-ACT-2003-ACT-651.pdf>

- s.20(1): at least 15 working days paid annual leave per calendar year.
- s.22: sickness, pregnancy and public holidays do not reduce the annual entitlement.
- s.23: special, compassionate and unpaid leave is not counted as annual leave.
- s.24: certified sickness during annual leave is not counted as leave.
- s.25: recalled workers keep the remainder.
- s.27(2): the employer must record start date, entitlement and dates taken.
- s.31: agreements to forgo leave are void, so unused annual days carry over in full, with no cap.
- s.57: maternity is at least 12 weeks per pregnancy, in addition to annual leave, plus at least 2 weeks for multiple or abnormal births.
- Paternity and the 14-week maternity rule exist only in the unpassed Labour Bill.

Product rules fixed alongside:

- Leave year: calendar year (January–December).
- Pending requests hold their days; rejected, withdrawn, cancelled and expired requests release them; leave ended early returns unused days.
- Payroll links (unpaid-leave deductions, payout at exit) are deferred to the Payroll feature.

## Design notes adopted from review

- Holiday changes re-price leave only in the current and later years; past years are frozen, and corrections are made by adjustment.
- Approving leave must not push already-approved future-year leave below zero.
- Balance checks are scoped to the leave's branch.
- Managers cannot adjust their own balance.
- Edits to the employment start date are audited.
