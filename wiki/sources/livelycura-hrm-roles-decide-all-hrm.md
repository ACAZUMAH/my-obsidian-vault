---
type: source
status: active
created: 2026-11-23
updated: 2026-11-23
tags: [livelycura, hrm, roles, permissions, approvals, decision]
sources:
  - ../../raw/sources/2026-11-23-livelycura-hrm-roles-decide-all-hrm.md
source_date: 2026-11-23
ingested: 2026-11-23
confidence: high
---

# LivelyCura HRM Roles Decide For All HRM

## Source

- Raw file: [LivelyCura HRM roles decide widened to all of HRM](../../raw/sources/2026-11-23-livelycura-hrm-roles-decide-all-hrm.md)
- Date: 2026-11-23
- Author: Product owner (verbatim answer) with the session's context
- Ingested: 2026-11-23

## Core Claims

- "Roles decide" now covers all of HRM, not only shift actions: approving open-shift pickups, overtime and leave, and "anything in hrm", count the roles the person holds at the record's branch, with organization-wide roles counting at every branch.
- A company with an HR team gives HR organization-wide roles and HR handles everything. A company without one gives branch managers those permissions at their branch, and they act instead.
- Who is told about a request (inbox and push) follows the same rule: everyone holding the permission at that branch, organization-wide holders included. This is the session's reading of the decision, not the owner's words.

## Useful Details

- Came up while planning the follow-up "First-come pickups have no manager safeguards"; the owner said the plan made sense and added this rule.
- The record's branch is the shift's branch for shift and pickup work, and the employee's branch for leave and overtime.
- Never design HRM features around branch managers as the default actor; wording says "the person who manages your leave" or names the role holder, not "your branch manager".

## Connections

- Widens [[livelycura-hrm-shift-management-scope-decision|LivelyCura HRM Shift Management Scope Decision]] (2026-11-21) from shift actions to all of HRM.
- Applies to [[../projects/livelycura-backend|LivelyCura Backend]], [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]] and [[../projects/serlp-mobile|SERLP Mobile]], and to SERLP AI actions.

## Contradictions Or Tensions

- Employees decision 5 (2026-10-25) still keeps hiring, staff details, deactivate and reactivate, roles and the clock-in phone reset at organization level; the owner's "anything in hrm" was said about approvals and day-to-day HRM actions, not about those.

## Open Questions

- Which existing HRM approvals and approver notifications already follow the rule is not yet checked.
