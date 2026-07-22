---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, altin, react-native, modules, lists]
sources:
  - ../../raw/sources/2026-07-21-altin-mistitled-casual-greeting-continuations.txt
confidence: high
---

# Altin Mistitled Casual-Greeting Continuations

## Source

- Raw file: `../../raw/sources/2026-07-21-altin-mistitled-casual-greeting-continuations.txt`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Two generic-titled coder records belong to Altin Partner Mobile, not SERLP or Bora. They establish the Apps directory and grouped target-branded UI, reject a centralized generic module architecture, and replace it with module-owned roots/features composed from shared presentation/mechanics primitives.

## Useful Details

- `20260719_015234_50d0c5` — substantive. Built the Apps directory, target-branded grouped light/dark surfaces, and typed module navigation. Its centralized `AppModuleScreen`/`AppFeatureScreen` architecture was completed historically but explicitly rejected by its successor.
- `20260719_035336_d709a6` — substantive. Corrected ownership so each module owns its root, drawer, sections, constants/styles, future data, and feature screens. Added `ListHeader`, generic `EntityList`, and `FiltersModal` mechanics and composed them in fourteen module-owned feature screens.

### Durable Boundaries

- Apps owns discovery metadata and root navigation only.
- Each module owns its root screen, drawer, sections, styles/constants, concrete feature screens, and future data/query behavior.
- Shared list primitives own mechanics and presentation; concrete feature screens own queries/data, filter state and controls, entity types, row rendering, and navigation.
- Empty data remains explicit until real business integration exists; do not invent fake API models to make shells appear complete.

## Current Static Boundaries

- Current source supports module-local ownership and uses the three shared primitives across fourteen feature screens.
- Feature screens remain honest empty-data shells rather than completed workflows.
- Rejected generic files (`AppModuleScreen`, `AppFeatureScreen`, `useAppModule`, and a stale interface) remain physically present but appear inactive.
- Historical project checks were not rerun during harvesting.

## Connections

- [[ceqa-altin-hermes-conversation-harvest-supplement-1|C.E.Q.A/Altin Hermes Conversation Harvest — Supplement 1]]
- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Centralized module shells were historically completed but explicitly rejected.
- Inactive generic shell residue contradicts accepted module-local ownership even though live routes use the correct architecture.

## Open Questions

- When should inactive rejected generic shell files be removed?
- Which module receives the first real data/query implementation?
