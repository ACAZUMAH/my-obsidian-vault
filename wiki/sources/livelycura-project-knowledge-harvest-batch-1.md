---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [livelycura, project-knowledge, codex, repositories]
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-1.md
---

# LivelyCura Project Knowledge Harvest — Batch 1

## Source

- Raw file: [2026-07-21-livelycura-project-knowledge-harvest-batch-1.md](../../raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-1.md)
- Date: 2026-07-21
- Author: Codex, from user-directed repository and transcript evidence
- Ingested: 2026-07-21

## Core Claims

- LivelyCura is ten independently versioned TypeScript repositories sharing a backend and product family, not a root monorepo.
- Repositories own distinct surfaces: shared API, ERP web/desktop, administration, customer web/mobile, workforce mobile, courier mobile, branded ordering mobile, SERLP public web, and SERLP operator mobile.
- Durable implementation practice is domain ownership: use focused folders and existing project infrastructure instead of importing a convenient helper from an unrelated domain.
- Laboratory-result handling has a deliberate human-in-the-loop contract: persisted values, scoped AI validation, exact values-hash review, scientist finalization or reasoned override, explicit delivery, OTP-gated public access, and non-blocking explanation.
- Global actions remain reachable from the ERP home without entering an app, but header density must remain controlled.
- The intended courier architecture is business-agnostic and separates merchant charges, delivery fees, rider payout, collection, and remittance. Current code does not yet fully implement this model.

## Useful Details

- Backend and mobile/web apps use Yarn; Customer Portal also contains an npm lockfile and needs an explicit lockfile decision.
- Backend and Pharmacy Portal target Node 22. Backend testing uses Vitest, despite stale Mocha wording in its README.
- Expo apps use React Navigation and feature-owned folders; SERLP Mobile explicitly excludes Expo Router.
- SERLP public web keeps crawler SSR in top-level `ssr/` and excludes Apollo/Redux/data prefetching from that package.
- The public laboratory-result page is intentionally outside the authenticated customer layout but retains the portal theme and its own explanatory page header.

## Connections

- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../projects/livelycura-backend|LivelyCura Backend]]
- [[../projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../projects/livelycura-customer-portal|LivelyCura Customer Portal]]
- [[../projects/livelycura-courier-mobile|LivelyCura Courier Mobile]]

## Contradictions Or Tensions

- The latest courier design is desired architecture while current task persistence remains a simpler single-pickup/single-drop-off model.
- Several READMEs lag behind current packages and source layout. Current code and package scripts are authoritative; README differences remain recorded rather than erased.
- Historical sessions include successive UI corrections. The latest correction and current implementation outrank earlier proposals.

## Open Questions

- How should courier provider agreements, quotes, rider payouts, collections, and remittances map into the current task model?
- Should Customer Portal standardize on Yarn by removing the competing npm lockfile?
- Which current app repositories need project-specific `AGENTS.md` files rather than relying on family patterns and historical sessions?
