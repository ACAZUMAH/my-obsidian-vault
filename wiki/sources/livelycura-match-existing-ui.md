---
type: source
status: active
created: 2026-10-26
updated: 2026-10-26
tags: [livelycura, ui, forms, conventions, correction]
sources:
  - ../../raw/sources/2026-10-26-livelycura-match-existing-ui.md
source_date: 2026-10-26
ingested: 2026-10-26
confidence: high
---

# LivelyCura Match Existing UI

## Source

- Raw file: [LivelyCura: new screens must match the existing UI](../../raw/sources/2026-10-26-livelycura-match-existing-ui.md)
- Date: 2026-10-26
- Author: The user (verbatim messages)
- Ingested: 2026-10-26

## Core Claims

- New or changed screens must copy the existing screens' patterns exactly instead of inventing new ones.
- Portal inputs use placeholders in the house wording ("Enter …" for text, "Select …" for selects and dates), not description or hint text under the input; hints push inputs out of line in 2-column grids.
- Forms carry no extra links or shortcuts (an "Add job title" link under a select label was rejected).
- No "Private" tags, lock icons or badges: data a viewer may not see is simply not shown, and a person viewing their own data needs no marker.

## Useful Details

- Reference form for HRM layout: `src/hrm/createLeave/components/CreateLeaveForm.tsx` in the portal; HRM date inputs use `valueFormat="DD MMM YYYY"`.
- The correction applied to the Employees redesign in the portal, serlp-mobile and Loop.

## Connections

- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]], [[../projects/serlp-mobile|SERLP Mobile]] and [[../projects/livelycura-loop-app|LivelyCura Loop App]] carry the convention.
- [[think-like-a-user-direction|Think Like A User Direction]]: both corrections push toward what users actually see and need.
- [[livelycura-hrm-employee-record-design|LivelyCura HRM Employee Record Design]]: the screens this corrected.

## Contradictions Or Tensions

- The approved employee-record plan gave organization questions optional help text and marked private fields; this correction drops help text in favour of placeholders and removes private markers.

## Open Questions

- None.
