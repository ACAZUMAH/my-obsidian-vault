---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [portfolio, project-knowledge, codex, react, graphql]
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-portfolio-project-knowledge-harvest-batch-1.md
  - hermes-conversation-harvest-scope-correction.md
  - portfolio-featured-projects-hermes-chain.md
  - portfolio-batch1-integration-standalone-reconnaissance.md
---

# Portfolio Project Knowledge Harvest — Batch 1

## Source

- Raw file: [2026-07-21-portfolio-project-knowledge-harvest-batch-1.md](../../raw/sources/2026-07-21-portfolio-project-knowledge-harvest-batch-1.md)
- Date: 2026-07-21
- Author: Codex history plus read-only current repository reconciliation
- Ingested: 2026-07-21

## Core Claims

- Portfolio is a three-application production family—backend, admin CMS, and public client—plus a dirty parent launcher.
- The explicit dependency correction is app-local Yarn ownership: no root workspace or root dependency installation. A root command launcher does not make the applications one monorepo.
- Backend, frontend feature, GraphQL operation, and permission ownership remain explicit; thin resolvers and feature-local hooks/operations are preferred.
- Public portfolio claims and counts should be CMS/API-backed with explicit fallbacks. Design references are inspiration, while established visual language, responsive breathing room, real asset formats, and reduced motion remain constraints.
- Four direct working-directory rollouts were substantive. One earlier index entry has no surviving rollout and supports no project claim.

## Useful Details

- Default process-control record `20260721_113041_3f113d`, audited in [[portfolio-batch1-integration-standalone-reconnaissance|Portfolio Batch 1 Integration And Standalone Reconnaissance]], owns this batch's focused vault writes and historical validation. It does not own the underlying Codex evidence, schema/templates, application repositories, or Git delivery.
- Current revisions recorded by the batch: root `main@8621a0286205` dirty/diverged; backend `main@c211320705f5` clean; admin `main@b0a86f9009d7` clean; client `main@d54e1e4466d9` clean.
- The parent remote shares the client lineage while local parent `main` is unrelated, so the dirty parent is not a reproducible aggregate snapshot.
- Current backend exposes content/CMS, auth, media, leads, resume, availability, project visibility, and analytics domains through Express/Apollo/Mongoose with Shield and request DataLoaders.
- Current client retains Hero → About composition, backend-driven profile/count/detail data, light availability treatment, social/CTA strip, responsive layout, and reduced-motion handling.
- Historical UI experiments—including the About collage/Build Console, glowing hero control, constrained global rail, and Threads background—are superseded by current source.
- Historical verification is attributed. No current project command or runtime surface was exercised during the harvest.

## Connections

- [[../projects/portfolio-workspace|Portfolio Workspace]]
- [[../projects/portfolio-backend|Portfolio Backend]]
- [[../projects/portfolio-admin-portal|Portfolio Admin Portal]]
- [[../projects/portfolio-client-portal|Portfolio Client Portal]]
- [[hermes-conversation-harvest-scope-correction|Hermes Conversation Harvest Scope Correction]]
- [[portfolio-featured-projects-hermes-chain|Portfolio Featured Projects Hermes Chain]]
- [[portfolio-batch1-integration-standalone-reconnaissance|Portfolio Batch 1 Integration And Standalone Reconnaissance]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- The parent working tree describes a multi-app launcher absent from parent `HEAD`; nested repositories are clean but parent status is heavily dirty and its remote points to the client lineage.
- Root documentation says initial content is automatically seeded, while current backend startup leaves seeding disabled.
- Historical tests were inconsistently reported, and current test commands permit empty suites; build success must not be treated as authorization or behavioral coverage.
- The initial record claimed the admin project flow was complete, but the user later rejected its structure and the record ended before that restructuring was completed.
- A dedicated full About page was intended, but current source has no such route and the home About has evolved into a richer section.
- Current hero availability/location copy is not fully CMS-driven even though related data is available upstream.
- The raw manifest's repository-only prototype classification is superseded and does not support an active project page.
- This batch's limited-search statement that no direct Portfolio Hermes implementation session was found is superseded for the Client Portal's Featured Projects only by three exact June 22 records; preserve the immutable raw statement as historical search evidence.

## Open Questions

- Should the parent become a real monorepo, track nested repositories as submodules, or remain an external launcher with corrected remote/history?
- Should backend startup seeding be restored or root documentation corrected?
- Should the intended dedicated About page be implemented, or is the current richer home About now the product decision?
- Which CI, deployment, test, and runtime contracts should be added to the three production applications?
