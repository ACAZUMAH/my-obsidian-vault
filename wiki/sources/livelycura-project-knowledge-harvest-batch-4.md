---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [livelycura, project-knowledge, codex, courier, mobile]
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-4.md
---

# LivelyCura Project Knowledge Harvest — Batch 4

## Source

- Raw file: [2026-07-21-livelycura-project-knowledge-harvest-batch-4.md](../../raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-4.md)
- Date: 2026-07-21
- Author: Codex, from user-directed repository and transcript evidence
- Ingested: 2026-07-21

## Core Claims

- `SERLP Dispatch` is the courier app’s public identity; the repository’s LivelyCura Courier name is internal. Public sign-up is available to eligible couriers, while operational access can require identity/profile approval.
- Courier notification payloads retain the backend’s existing nested task ID. The app maps that value to one canonical `taskId` route contract instead of adding redundant backend fields or route fallbacks.
- Standalone delivery tasks omit multi-stop metadata. Non-empty children identify a multi-pickup root, while `parentTaskId` identifies a pickup stop; an empty child array alone remains standalone.
- Platform-matched mobile UI requires checking Android elevation separately from iOS shadows, native controlled OTP behavior across Android/iPad, and system-bar coverage for bottom-sheet modals.
- Floating-header lists remain full-screen beneath the header while explicit safe-area insets/offsets keep pull-to-refresh visible; shared presentation components let callers own contextual spacing.
- The older lab JIT/backflush proposal is superseded as current behavior by the implemented ordinary sale/inventory/COGS transaction plus one test request per qualifying sale item.

## Useful Details

- Current SERLP Dispatch config retains courier-specific camera/photo/location purpose strings and iPad support.
- The current courier auth screen uses a native controlled four-digit input; the historical reusable `CustomOtpInput` integration no longer survives in `Auth.tsx`.
- Store update checks dynamically load the optional native dependency only on the production path and fail softly.
- Current CheckCity bottom tabs retain the corrected active/inactive flex ratio, while current `MenuLoader` no longer matches the historical six-item grid.
- Historical App Store phone/tablet screenshots remain external; a Play featured-graphic asset exists in the courier repository but was excluded as binary evidence.

## Connections

- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../projects/livelycura-courier-mobile|LivelyCura Courier Mobile]]
- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]]

## Contradictions Or Tensions

- JIT BOM/backflush was the last proposal in the research session, but later implementation and current code use the ordinary inventory-backed sale path.
- One App Store session explicitly reverted temporary auth copy; current source later contains public-sign-up copy, supported independently by the broader review plan.
- The reusable courier OTP component remains present but unused; current auth uses an inline native controlled input.
- Historical store configuration, screenshot outputs, and CheckCity loader layouts diverge from current source. Current code and config are authoritative.

## Open Questions

- Should the unused courier `CustomOtpInput` be removed or restored as the shared auth input after platform testing?
- Has the reviewer-accessible seeded courier account and its populated task/profile data been verified in the current release process without persisting credentials in documentation?
- Should the CheckCity `MenuLoader` remain horizontal or return to the menu grid shape after current visual review?
- Do the five remaining LivelyCura-working-directory sessions contain unique evidence or only unrelated/duplicate child context?
