# LivelyCura HRM: shift management scope, "roles decide" (decided, not yet built)

- Date: 2026-11-21
- Author: the product owner, choosing between two options in a LivelyCura Claude Code session
- Recorded from: the owner's own messages (quoted verbatim below) and the session's investigation findings, relayed to the recording agent by the session's workflow
- Feature: LivelyCura HRM shift management (shift page, Shifts, Schedules, employee page, SERLP AI)
- Status when recorded: decided, build pending

## The owner's concern (verbatim)

- "there are business with many branches and shifts are not managed by branch managers, when I worked on keks assigning shifts, creating shifts and managing is the work of the hr team not branch managers"

## What the investigation found (2026-11-21)

- No earlier owner decision ever gave shift work to branch managers; the branch-level shift checks came from older code.
- The shift screens contradicted the owner's Employees decision 5 (2026-10-25), under which branch managers "can view the info, but actions belong to org level".
- HR suites and ERPs (for example ERPNext, SAP, Sage HR, Keka and Zoho People) default to HR assigning shifts, with optional delegation to a branch person; rota apps default to location managers; every product leaves the choice to set-up.
- Keks, the owner's own HR product, has only company-wide permissions.

## Options put to the owner

- A) Lock shift planning to organization level.
- B) HR-led through roles.

## The owner's answer (verbatim)

- "B: roles decide"

## The rule as decided

1. Every shift action (create or edit a shift and its day slots, assign, unassign, edit an assignment) counts roles at the shift's own branch, on every screen (shift page, Shifts, Schedules, employee page) and in SERLP AI.
2. Organization-wide roles count at every branch, so HR with an organization-wide role runs shifts everywhere; that is the normal set-up.
3. A branch manager gets shift rights only if the business ticks them into a branch role. There is no organization-only lock.
4. Open-shift publishing and pickup approvals keep counting roles at the branch.
5. The rest of Employees decision 5 stays organization-level: hiring, staff details, deactivate and reactivate, roles, and the clock-in phone reset.
