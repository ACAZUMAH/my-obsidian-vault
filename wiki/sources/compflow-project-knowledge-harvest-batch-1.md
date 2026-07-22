---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [compflow, project-knowledge, codex, repository-inventory]
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-compflow-project-knowledge-harvest-batch-1.md
---

# CompFlow Project Knowledge Harvest — Batch 1

## Source

- Raw file: [2026-07-21-compflow-project-knowledge-harvest-batch-1.md](../../raw/sources/2026-07-21-compflow-project-knowledge-harvest-batch-1.md)
- Date: 2026-07-21
- Author: Codex, from user-directed read-only repository inventory and bounded session discovery
- Ingested: 2026-07-21

## Core Claims

- CompFlow is four independently versioned applications: public web, internal admin, business client portal, and backend API.
- Zero historical Codex sessions matched the CompFlow family, so the batch promotes observed current implementation without inventing user rationale.
- The public site consumes live platform plans with static fallback; the admin currently centers on one overview dashboard; the client portal mixes live employee GraphQL with several demo/static feature services; the backend owns OTP auth, onboarding/payment, tenant scope, subscription plans, and payroll.
- Current GraphQL generation wiring is incomplete across the family, and client onboarding/settings diverge from the backend contract.

## Useful Details

- The three web applications use Vite, React, TypeScript, Mantine, Apollo, and React Router; admin and client add persisted Redux state and GraphQL Codegen.
- Public and client repositories have Node 22/Yarn CI plus Netlify staging/production workflows. Admin and backend have no comparable deployment configuration in the current checkout.
- Backend tenant reads/writes resolve organization scope in services; Admin/SuperAdmin bypass membership while ordinary users remain organization-bound.
- Backend payroll uses permissioned creation, approval, paid, and cancellation operations with persisted calculations, reports, and payslips.
- Reusable bootstrap lesson: package scripts, lockfiles, generated-contract configuration, and actual artifacts must be verified together before declaring a scaffold ready.

## Connections

- [[../projects/compflow|CompFlow Public Frontend]]
- [[../projects/compflow-admin|CompFlow Admin]]
- [[../projects/compflow-client-portal|CompFlow Client Portal]]
- [[../projects/compflow-backend|CompFlow Backend]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../concepts/codex-project-knowledge-harvest|Codex Project Knowledge Harvest]]

## Contradictions Or Tensions

- Client registration and simulated security settings do not match the backend's OTP-verification and authenticated-checkout sequence.
- Admin/client Codegen configurations expect an absent backend schema artifact; the backend itself exposes a `generate` script without its referenced config.
- Client portal contains both Yarn and npm lockfiles even though scripts/workflows favor Yarn.
- Backend README documents a database bypass flag that current startup ignores.

## Open Questions

- Which client/admin demo paths are intentional prototypes, and which should be connected to current backend operations?
- What artifact or command should be the canonical source for GraphQL client generation?
- What deployment path is intended for the admin and backend repositories?
- Will future CompFlow Codex sessions explain the rationale behind the current transitional paths?
