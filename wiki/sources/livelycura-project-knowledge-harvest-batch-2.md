---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [livelycura, project-knowledge, codex, mls, frontend]
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-2.md
---

# LivelyCura Project Knowledge Harvest — Batch 2

## Source

- Raw file: [2026-07-21-livelycura-project-knowledge-harvest-batch-2.md](../../raw/sources/2026-07-21-livelycura-project-knowledge-harvest-batch-2.md)
- Date: 2026-07-21
- Author: Codex, from user-directed repository and transcript evidence
- Ingested: 2026-07-21

## Core Claims

- Ordinary sale creation owns lab-request creation: each lab-linked `SaleItem` produces one `TestRequest` inside the same transaction while retaining normal inventory, accounting, and invoice behavior.
- MLS uses namespace-scoped domain names (`Sample`, `TestDefinition`, `TestRequest`) and preserves the full GraphQL/Shield/DataLoader/service architecture during focused changes.
- Test definitions reference first-class Departments, Samples, and existing product categories. They do not duplicate billing/inventory responsibility or introduce parallel taxonomy/link models.
- Publish, activate, deactivate, archive, and request-status changes are explicit lifecycle actions. Activation is not publish and changes only the selected definition.
- The portal separates list/create/edit/detail ownership while sharing a technician-facing builder, mapper layer, and reusable renderer engine. Lab staff should not write JSON or read raw relation IDs.
- CheckCity uses restrained Reanimated motion with reduced-motion support and a background-only theme reveal; content is never covered by a theme-colored transition sheet.

## Useful Details

- The current request model is one request per sale item, not the older PDF proposal of one parent request containing many tests.
- Product sync is post-creation lifecycle behavior. Category changes use dedicated relation services and propagate to a linked product.
- Employee department is optional; when present it must be active and belong to the same organization, and it can be cleared.
- The POS terminal is a standalone product-based selling route with its own shell that reuses organization/facility, theme, fullscreen, profile, and permission infrastructure.
- Definition view uses the reusable renderer; create/edit compile technician-friendly rule/report state into backend-compatible JSON-shaped inputs.

## Connections

- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../entities/projects/livelycura-backend|LivelyCura Backend]]
- [[../entities/projects/livelycura-pharmacy-portal|LivelyCura Pharmacy Portal]]
- [[../entities/projects/livelycura-check-city-app|LivelyCura CheckCity App]]

## Contradictions Or Tensions

- The older PDF architecture grouped many tests under one request and draft invoice; current code and later explicit corrections use one request per lab-linked sale item.
- Builder layout changed repeatedly. Current code settles implementation reality, while the durable UX principle is guided technician language, no exposed JSON, and a shared operational renderer.
- Historical action-state logic changed during review. Current lifecycle services, permissions, hooks, and confirmation modals outrank earlier intermediate tables.

## Open Questions

- Should multiple test sale items ever gain an explicit higher-level clinical encounter/order aggregate, or is the sale itself the permanent grouping boundary?
- Should the pharmacy portal add repository-level instructions that codify its one-operation-per-hook, separate feature-flow ownership, and live browser-verification conventions?
- Which renderer contracts will be reused first by test-request processing and result entry, beyond definition review?
