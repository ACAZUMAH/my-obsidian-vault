---
type: source
status: active
created: 2026-11-26
updated: 2026-11-26
tags: [livelycura, serlp-mobile, hrm, navigation, ui, correction]
sources:
  - ../../raw/sources/2026-11-26-livelycura-serlp-mobile-create-in-drawer.md
source_date: 2026-11-26
ingested: 2026-11-26
confidence: high
---

# LivelyCura SERLP Mobile Create In The Drawer

## Source

- Raw file: [serlp-mobile creates from the drawer's Create section](../../raw/sources/2026-11-26-livelycura-serlp-mobile-create-in-drawer.md)
- Date: 2026-11-26
- Author: Product owner (verbatim correction), with the session's reading and applied change
- Ingested: 2026-11-26

## Core Claims

- In serlp-mobile, list screens don't carry their own "Add X" button at the top. Creating belongs in the module drawer's Create section, and the module home's matching actions, as "New X", shown only to people with the permission that adding needs. The owner, on the Job titles screen: "remove the add job title button from the job titles screen, it's supposed to be at the create section of the drawer".
- A list's empty-state button may stay.

## Useful Details

- Built on `feature/hrm` in serlp-mobile `0635209b`: the Job titles list lost its top "Add job title" button; "New job title" sits after "New department" in the HRM drawer's Create section and the HRM home actions, gated by the departments create permission for the whole organization (as the portal's menu manages job titles), and opens Job titles with the Add job title window open, once. The empty list keeps its own button, as Departments does.

## Connections

- Applies to [[../projects/serlp-mobile|SERLP Mobile]].
- Related UI conventions: [[livelycura-match-existing-ui|LivelyCura Match Existing UI]] (an "Add job title" link inside a form was rejected earlier), [[livelycura-serlp-mobile-portal-parity|LivelyCura SERLP Mobile Portal Parity]].
- Collected with the other LivelyCura conventions in [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].

## Contradictions Or Tensions

- The owner's words name the Job titles screen; the wider rule is the session's reading of "it's supposed to be". Repository inspection at capture (`feature/hrm` at `0635209b`) found other lists that still have a top create button: HRM Assignments ("New assignment") and SMS Segments ("New segment"), Templates ("New template"), Opt-outs ("Add numbers") and Lists ("New list").

## Open Questions

- Do those remaining top create buttons move to their module drawers' Create sections too? Not discussed with the owner.
