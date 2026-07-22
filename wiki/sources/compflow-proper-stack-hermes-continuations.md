---
type: source
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [hermes, compflow, graphql, apollo, permissions, migrations, atlas]
sources:
  - ../../raw/sources/2026-07-21-compflow-proper-stack-continuations.txt
confidence: high
---

# CompFlow Proper Stack Hermes Continuations

## Source

- Raw file: `../../raw/sources/2026-07-21-compflow-proper-stack-continuations.txt`
- Date: 2026-07-21
- Author: Hermes audit synthesis
- Ingested: 2026-07-21

## Core Claims

Four substantive continuations after the already-classified root establish the separate business Client Portal, database-managed plans, Apollo-based public consumption, removal of fake overview contracts, record-derived tenant scoping, and a registered migration for the developer platform role. Replay and re-execution prefixes are reference-only.

## Useful Details

### Classified Records

- `20260711_143433_be702f` — substantive mixed-project continuation creating the separate Client Portal and correcting backend auth/context architecture.
- `20260711_152924_5d0016` — replay-heavy substantive continuation covering Atlas diagnosis, database-managed plans, scope correction, and temporary superseded designs.
- `20260712_223001_7e9756` — substantive corrective/refactor continuation covering fake-contract removal, Apollo frontend architecture, pagination, organization scoping, and a superseded standalone role seed.
- `20260713_000653_15136d` — substantive correction/delivery continuation replacing the seed with a registered migration and safely publishing the public frontend.

## Durable Decisions

- Admin is for internal system management; Client Portal is for businesses and remains a separate Vite application.
- Do not invent parallel feature folders when an established destination feature already owns the domain.
- JWT/context/DataLoader responsibilities should follow proven project ownership instead of bespoke context-only helpers.
- Subscription plan amount, currency, interval, limits, features, active state, and provider-plan code are database-managed, not provider-named amount environment values.
- Public plan consumption uses Apollo provider/client, a feature-local query hook, a dedicated formatter, and a small composition hook with static fallback.
- Never restore fake schema/resolver data merely to satisfy stale tests. Remove stale contracts and repair consumers/tests honestly.
- By-ID tenant authorization fetches the entity first and derives organization scope from that entity; platform Admin/SuperAdmin may bypass tenant membership, while tenant users remain scoped.
- Bootstrap data such as a developer platform role belongs in the registered migration system rather than an ad hoc package seed unless a standalone command is explicitly requested.

## Historical Verification

Historical evidence includes backend tests/builds, GraphQL HTTP and subscription transport checks, portal generation/tests/builds, browser rendering checks, public Vitest/ESLint/Vite builds, migration tests, and one verified public-frontend delivery commit. These are historical observations, not current runtime proof.

## Contradictions Or Tensions

### Current Reconciliation

- The four repositories remain separate and clean.
- Current backend keeps database plans, centralized organization scope, shared pagination, role migration, assignment restrictions, and effective-permission aggregation.
- Current public frontend keeps Apollo plan lookup and static fallback.
- Backend no longer exposes `adminOverview`; Admin still queries it and silently falls back.
- No current Admin subscription-plan manager exists; the temporary UI was reverted after scope correction.
- The current migration runner starts after HTTP server readiness, is not awaited, and catches/logs failures. Registered and startup-triggered does not mean fail-closed or pre-readiness.
- Historical Atlas TLS failure occurred before authentication. Allowlisting was plausible but not proven; current live DB health remains unknown.

## Delivery Boundary

Only `20260713_000653_15136d` has exact session-verified delivery attribution: the public frontend `develop` branch was safely rebased and pushed after HTTPS credential failure by using existing SSH authentication without changing origin.

## Connections

- [[compflow-hermes-project-knowledge-harvest-supplement-1|CompFlow Hermes Project Knowledge Harvest — Supplement 1]]
- [[../projects/compflow-backend|CompFlow Backend]]
- [[../projects/compflow-admin|CompFlow Admin Portal]]
- [[../projects/compflow-client-portal|CompFlow Client Portal]]
- [[../projects/compflow|CompFlow Public Frontend]]

## Evidence

- `../../raw/sources/2026-07-21-compflow-proper-stack-continuations.txt`

## Open Questions

- Should startup await migrations and fail closed before GraphQL readiness?
- When will Admin stop querying removed `adminOverview` or adopt a supported replacement?
- Is live Atlas connectivity healthy under the current environment?
- Where should subscription-plan management live if Admin remains out of scope?
