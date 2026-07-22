---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [compflow, project-knowledge, hermes, scaffold]
source_date: 2026-07-10
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-compflow-hermes-project-knowledge-harvest-supplement-1.md
---

# CompFlow Hermes Project Knowledge Harvest — Supplement 1

## Source

- Raw file: [2026-07-21-compflow-hermes-project-knowledge-harvest-supplement-1.md](../../raw/sources/2026-07-21-compflow-hermes-project-knowledge-harvest-supplement-1.md)
- Date: 2026-07-10
- Author: User and Hermes session `20260710_173537_54b264`, reconciled by Codex against current repositories
- Ingested: 2026-07-21

## Core Claims

- The user explicitly rejected an accidental root monorepo and required the promotional web, admin dashboard, and backend to be scaffolded in their existing independent folders with Yarn.
- The session created and historically verified those three baseline applications, then removed its accidental root artifacts.
- The current three repositories preserve that separation and parts of the initial architecture, but current code supersedes several minimal baseline behaviors.
- The client portal is a later fourth repository and is not session-derived evidence.

## Useful Details

- The initial web/admin shape used Vite, React, TypeScript, Mantine, Apollo, Redux, routing, GraphQL Codegen structure, Vitest, and ports `5173`/`5174`; the backend used Express/Apollo/WebSockets, Jest/Supertest, and port `4000`.
- Historical session verification reported passing tests/builds, three started services, and successful page/endpoint smoke checks. These results were not rerun during the harvest.
- Current public code expands the paid-pilot scaffold with live platform-plan lookup and fallback. Current backend retains health but no longer exposes the initial `adminOverview`; current admin still queries it and can silently fall back.
- The proposal’s statutory rates and bands are historical product inputs, not current legal truth. Production payroll rules require current authoritative validation and versioned configuration.

## Connections

- [[../projects/compflow|CompFlow Public Frontend]]
- [[../projects/compflow-admin|CompFlow Admin]]
- [[../projects/compflow-client-portal|CompFlow Client Portal]]
- [[../projects/compflow-backend|CompFlow Backend]]
- [[compflow-project-knowledge-harvest-batch-1|CompFlow Project Knowledge Harvest — Batch 1]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../concepts/codex-project-knowledge-harvest|Codex Project Knowledge Harvest]]

## Contradictions Or Tensions

- The session’s final report named a REST admin-overview path and two backend tests; the first Git commit instead records a GraphQL `adminOverview` and three repository tests. Both are preserved as successive historical states.
- The current admin retains the initial `adminOverview` query, while the current backend schema no longer exposes it; admin fallback can mask this integration drift.
- The session’s build and smoke results establish only its 2026-07-10 baseline, not current runtime, integration, or deployment health.

## Open Questions

- Should the admin replace or remove `adminOverview`, or should the backend restore a permissioned current equivalent?
- Which authoritative process will validate and version Ghanaian payroll rules before production calculations?
