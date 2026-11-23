---
type: source
status: active
created: 2026-11-01
updated: 2026-11-10
tags: [livelycura, hrm, review, scope, communication, correction]
sources:
  - ../../raw/sources/2026-11-01-livelycura-hrm-feature-by-feature-review.md
  - ../../raw/sources/2026-11-10-livelycura-hrm-review-screen-items-belong-to-their-module.md
source_date: 2026-11-01
ingested: 2026-11-01
confidence: high
---

# LivelyCura HRM Feature-By-Feature Review Scope

## Source

- Raw file: [LivelyCura HRM review: one feature at a time, finished features stay closed](../../raw/sources/2026-11-01-livelycura-hrm-feature-by-feature-review.md)
- Raw file: [LivelyCura HRM review: items shown on the current feature's screen still belong to their own module](../../raw/sources/2026-11-10-livelycura-hrm-review-screen-items-belong-to-their-module.md) (2026-11-10)
- Date: 2026-11-01 (with consistent earlier statements from 2026-10-19 and 2026-10-25)
- Author: The user (verbatim messages)
- Ingested: 2026-11-01

## Core Claims

- The HRM review runs one feature at a time. Reports and decisions cover only the current feature's items.
- A finished feature stays closed. New findings in it are not raised, even when the current feature's change caused them.
- Items belonging to a later feature are parked silently and raised only when that feature is reached; parked items are not listed to the user.
- An item that merely appears on the current feature's screen still belongs to its own module: a "Delete Products" or "Create Leave" permission box on the Roles page is Products' or Leaves', not Roles'. Research briefs are filtered the same way before they are presented, and parked items are not listed even as a summary line (2026-11-10).
- A message that already tells the user what happened is not vague and is not flagged for rewording. "Employee already exists in this organization", shown when hiring someone who is already an active employee, is the example.

## Useful Details

- Raised during the Employees feature, after Leaves was finished and before Announcements was reached: the session had listed a Leaves message problem and an announcement-picker gap.
- The same rule was stated earlier for Payroll items (2026-10-19) and for Admin Portal items, which are separate from the current work (2026-10-25).

## Connections

- [[../syntheses/personal-operating-manual|Personal Operating Manual]] (Change And Remediation Work).
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]], [[../projects/serlp-mobile|SERLP Mobile]] and [[../projects/livelycura-loop-app|LivelyCura Loop App]] carry the HRM screens under review.
- [[think-like-a-user-direction|Think Like A User Direction]]: messages and findings are judged from what the user sees.
- [[livelycura-match-existing-ui|LivelyCura Match Existing UI]] and [[livelycura-hrm-employee-record-design|LivelyCura HRM Employee Record Design]] come from the same Employees review.
- [[livelycura-hrm-leave-balances-decisions|LivelyCura HRM Leave Balances Decisions]] already defers payroll links to the Payroll feature, consistent with this rule.

## Contradictions Or Tensions

- Rule 2 means a regression that the current feature causes in a closed feature is not raised during this review. The user stated this explicitly; it is the current rule, not an oversight.

## Open Questions

- None.
