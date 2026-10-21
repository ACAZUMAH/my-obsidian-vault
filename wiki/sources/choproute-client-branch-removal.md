---
type: source
status: active
created: 2026-08-07
updated: 2026-08-07
tags: [livelycura, choproute, marketplace, branch, architecture]
sources:
  - ../../raw/sources/2026-08-07-choproute-client-branch-removal.md
confidence: high
---

# ChopRoute Client Branch Removal

## Source

- Raw file: [2026-08-07-choproute-client-branch-removal.md](../../raw/sources/2026-08-07-choproute-client-branch-removal.md)
- Date: 2026-08-07
- Author: User
- Ingested: 2026-08-07

## Core Claims

- ChopRoute no longer has a client-side branch feature because customers choose a delivery location, not a fulfilling ERP facility.
- Branch files, Redux state, hooks, selector routes, and branch-specific UI should be removed rather than retained as dormant legacy code.
- Checkout and reorder behavior must not restore or select a previous facility on the client; those actions remain gated until marketplace-safe server allocation is implemented.

## Useful Details

- The app may explain automatic delivery routing without presenting a branch selection contract.
- Optional custom-app banner reads and event records are no longer scoped by a client-selected facility.
- Backend organizations and facilities remain authoritative and are not deleted by this mobile correction.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura ChopRoute App]]
- [[choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]]
- [[choproute-redux-marketplace-state-correction|ChopRoute Redux Marketplace State Correction]]

## Contradictions Or Tensions

- The earlier project constraint said legacy branch and checkout files would remain dormant for later analysis. The explicit removal instruction supersedes that retention decision.
- Future pickup may require customer-visible location selection, but that must be designed as a new restaurant pickup flow rather than reviving the removed global branch feature.

## Open Questions

- What server inputs beyond delivery coordinates will determine the eligible fulfilling facility for each restaurant order?
