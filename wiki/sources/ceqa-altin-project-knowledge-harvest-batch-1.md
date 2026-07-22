---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [ceqa, altin, keks, call-center, project-knowledge, codex]
source_date: 2026-07-21
ingested: 2026-07-21
confidence: high
sources:
  - ../../raw/sources/2026-07-21-ceqa-altin-project-knowledge-harvest-batch-1.md
---

# C.E.Q.A/Altin Project Knowledge Harvest — Batch 1

## Source

- Raw file: [2026-07-21-ceqa-altin-project-knowledge-harvest-batch-1.md](../../raw/sources/2026-07-21-ceqa-altin-project-knowledge-harvest-batch-1.md)
- Date: 2026-07-21
- Author: Codex, derived from local repositories and eight bounded historical records
- Ingested: 2026-07-21

## Core Claims

- The family contains three independent repositories: Altin Partner Mobile, Keks Admin Portal, and Call Center Web App.
- Twenty-one direct current/legacy working-directory records were discovered; batch 1 processes the eight most recent and leaves thirteen pending.
- Keks uses separate Roles and Designations ownership, server-backed search, permission-aware routes/navigation/actions, and controlled API-key lifecycle UI.
- Call-center checkout treats idempotency as a payload-stable retry contract and keeps address/coordinate state ordered deliberately.
- Altin Partner Mobile currently implements the required Expo/React Navigation/auth scaffold but still contains centralized module-shell code that conflicts with the durable module-local ownership direction.

## Useful Details

- All three repositories were clean and were inspected read-only at recorded branches and commits.
- Keks API-key secrets are one-time UI data and were not copied into this source. Deployment and runtime variable names were observed only as configuration contracts; values were not inspected or stored.
- The user rejected redesigning existing admin interfaces while adding Designations and required Roles and Designations to remain in separate folders.
- The user rejected a staging-only comment for permissions that should behave as ordinary first-class constants.
- Historical verification results are attributed to their sessions. No project test, build, API, service, or deployment was executed during the harvest.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[../projects/keks-admin-portal|Keks Admin Portal]]
- [[../projects/call-center-web-app|Call Center Web App]]
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]]
- [[../syntheses/new-project-bootstrap-operating-manual|New Project Bootstrap Operating Manual]]
- [[../syntheses/project-knowledge-harvest-status|Project Knowledge Harvest Status]]

## Contradictions Or Tensions

- Altin’s live module-directory resolver and generic module shells conflict with the explicit desired module-local ownership model.
- Altin’s README describes Expo Router, while repository instructions and current runtime use `expo/AppEntry.js` plus React Navigation.
- Keks has extensive permission protection, but current unguarded and commented routes prevent a blanket claim that every surface is protected.
- The call-center full historical test run executed nine tests but exited nonzero because of existing unhandled app-test network/router errors; current CI still includes that test surface.
- Call-center GraphQL generation depends on a live staging schema and suppresses generated TypeScript checking.

## Open Questions

- When should Altin remove the centralized module shells and finish concrete module-local feature screens?
- Which remaining Keks routes/actions still need permission coverage against the latest production backend model?
- Should call-center Codegen move to a reproducible checked-in schema or authenticated schema artifact instead of a live staging endpoint?
- Which current coordinate mapping will the backend ultimately standardize, and when can the compatibility exception be removed?
