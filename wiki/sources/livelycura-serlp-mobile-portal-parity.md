---
type: source
status: active
created: 2026-11-05
updated: 2026-11-05
tags: [livelycura, serlp-mobile, pharmacy-portal, parity, conventions, correction]
sources:
  - ../../raw/sources/2026-11-05-livelycura-serlp-mobile-portal-parity.md
source_date: 2026-11-05
ingested: 2026-11-05
confidence: high
---

# LivelyCura SERLP Mobile Portal Parity

## Source

- Raw file: [LivelyCura: serlp-mobile does everything the SERLP portal does](../../raw/sources/2026-11-05-livelycura-serlp-mobile-portal-parity.md)
- Date: 2026-11-05
- Author: The user (verbatim message)
- Ingested: 2026-11-05

## Core Claims

- `serlp-mobile` is the mobile version of the ERP. Anything the SERLP portal (`livelycura-pharmacy-portal`) does, `serlp-mobile` must also be able to do, adapted to mobile.
- Never offer "portal-only" as an option, and never ask how much of a feature belongs on `serlp-mobile`.
- Anything the portal does that `serlp-mobile` cannot yet do is parity work to build, not a scope choice.

## Useful Details

- Raised while planning HRM Employees for `serlp-mobile`; the session had offered options for how much of the feature the app should do, with roles staying portal-only. The user rejected the framing outright.
- "Adapted to mobile" matches the existing serlp-mobile convention: the portal is the ERP GraphQL/domain reference, adapted to mobile interaction rather than copied as desktop UI.

## Connections

- [[../projects/serlp-mobile|SERLP Mobile]] and [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]] carry the rule.
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]] (LivelyCura Family).
- [[livelycura-hrm-feature-by-feature-review|LivelyCura HRM Feature-By-Feature Review Scope]] and [[livelycura-refetch-queries-after-mutation|LivelyCura Refetch Queries After Mutation]] come from the same HRM work.

## Contradictions Or Tensions

- The rule covers the SERLP portal (`livelycura-pharmacy-portal`). Platform concerns the [[../projects/serlp-mobile|SERLP Mobile]] page already assigns to the Admin Portal (marketplace category assignment, Business Product publication) belong to a different app and are not portal features (inference).

## Open Questions

- None.
