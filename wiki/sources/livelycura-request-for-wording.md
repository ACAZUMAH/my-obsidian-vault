---
type: source
status: active
created: 2026-11-25
updated: 2026-11-25
tags: [livelycura, loop, hrm, copy, wording, correction]
sources:
  - ../../raw/sources/2026-11-25-livelycura-request-for-wording.md
source_date: 2026-11-25
ingested: 2026-11-25
confidence: high
---

# LivelyCura Request For Wording

## Source

- Raw file: [Staff copy says "request for" a shift](../../raw/sources/2026-11-25-livelycura-request-for-wording.md)
- Date: 2026-11-25
- Author: Product owner (verbatim correction and option pick), with the session's applied wording
- Ingested: 2026-11-25

## Core Claims

- When staff ask for a shift, the verb is "request for", never a bare "request" with the shift as its object. The owner, seeing "Request this shift?": "it should either request for this shift or just request not request this shift", then picked option 1, "request for" everywhere staff read it.
- The wording in use: button "Request for this shift", confirmation "Request for this shift?", "You can't request for this shift.", "... you can request for it again.", and the push "Tap to request for it."
- "Request" as a noun stays as it is: "Send request", "Withdraw your request?", "Request sent".

## Useful Details

- Built on `feature/hrm` in livelycura-loop-app `a6d0662` (open-shift button, confirmation, can't-take note, withdraw confirmation and toast, and their tests) and livelycura-backend `2f72bdf57` (the open-shift published/reopened push and its integration test). "Take this shift" for first-come open shifts is unchanged.
- New staff-facing copy about asking for something follows the same form, and old "request this / request it" copy is changed when touched.

## Connections

- Applies to [[../projects/livelycura-loop-app|LivelyCura Loop App]] (SERLP Team) and the staff pushes sent by [[../projects/livelycura-backend|LivelyCura Backend]].
- Related copy conventions: [[livelycura-match-existing-ui|LivelyCura Match Existing UI]], [[livelycura-loop-renamed-serlp-team|LivelyCura Loop Renamed SERLP Team]].
- The open-shift pickup flow it words: [[livelycura-hrm-shift-management-scope-decision|LivelyCura HRM Shift Management Scope Decision]].

## Contradictions Or Tensions

- None. The owner's message allowed a bare "Request" as the other form; option 1 chose "request for".

## Open Questions

- None.
