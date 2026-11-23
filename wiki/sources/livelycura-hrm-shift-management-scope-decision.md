---
type: source
status: active
created: 2026-11-21
updated: 2026-11-21
tags: [livelycura, hrm, shifts, roles, permissions, decision]
sources:
  - ../../raw/sources/2026-11-21-livelycura-hrm-shift-management-scope-decision.md
source_date: 2026-11-21
ingested: 2026-11-21
confidence: high
---

# LivelyCura HRM Shift Management Scope Decision

## Source

- Raw file: [LivelyCura HRM shift management scope decision](../../raw/sources/2026-11-21-livelycura-hrm-shift-management-scope-decision.md)
- Date: 2026-11-21
- Author: Product owner (verbatim concern and answer) with the session's investigation findings
- Ingested: 2026-11-21

## Core Claims

- "Roles decide": the owner chose option B, HR-led through roles, on 2026-11-21. Decided, build pending.
- Every shift action (create or edit a shift and its day slots, assign, unassign, edit an assignment) counts roles at the shift's own branch, on the shift page, Shifts, Schedules and the employee page, and in SERLP AI.
- Organization-wide roles count at every branch, so HR with an organization-wide role runs shifts everywhere; that is the normal set-up. A branch manager gets shift rights only when the business ticks them into a branch role. There is no organization-only lock.
- Open-shift publishing and pickup approvals keep counting roles at the branch.
- The rest of Employees decision 5 (2026-10-25) stays organization-level: hiring, staff details, deactivate and reactivate, roles, and the clock-in phone reset.

## Useful Details

- The owner's concern: in businesses with many branches, HR creates, assigns and manages shifts, not branch managers, as in his work on Keks.
- Investigation: no earlier owner decision gave shift work to branch managers; the branch-level shift checks came from older code, and the shift screens contradicted Employees decision 5, under which branch managers "can view the info, but actions belong to org level".
- HR suites and ERPs (ERPNext, SAP, Sage HR, Keka, Zoho People) default to HR assigning shifts with optional delegation to a branch person; rota apps default to location managers; every product leaves it to set-up. Keks has only company-wide permissions.
- The rejected option A would have locked shift planning to organization level.
- A branch role is a role given to someone at one branch; roles remain one kind per organization.

## Connections

- [[../projects/livelycura-backend|LivelyCura Backend]], [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]] and [[../projects/serlp-mobile|SERLP Mobile]] carry the rule; SERLP AI shift actions follow it too.
- [[livelycura-hrm-employee-record-design|LivelyCura HRM Employee Record Design]] records other 2026-10-25 Employees decisions.

## Contradictions Or Tensions

- For shift actions this amends Employees decision 5's "actions belong to org level": a business may give shift work to a branch role. Every other decision 5 action stays organization-level.
- Nothing is built yet; check the shift screens and SERLP AI against this rule once the build lands.

## Open Questions

- Employees decision 5 is known here only from the session's quotation; the Employees decisions have no Source Record yet.
