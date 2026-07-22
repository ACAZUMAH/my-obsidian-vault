---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, compflow, admin, react, graphql]
sources:
  - ../sources/compflow-project-knowledge-harvest-batch-1.md
  - ../sources/compflow-hermes-project-knowledge-harvest-supplement-1.md
  - ../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1.md
  - ../sources/compflow-proper-stack-hermes-continuations.md
  - ../sources/compflow-backend-auth-hermes-continuations.md
confidence: high
---

# CompFlow Admin

## Summary

Internal ComplianceFlow team dashboard, separated from the business-facing client portal.

## Purpose

Provides the internal control surface for platform overview and future back-office operations; businesses use [[compflow-client-portal|CompFlow Client Portal]] instead.

## Stack

- React 19, Vite 5, TypeScript 5.5, React Router 7.
- Mantine 9 with modals and notifications.
- Apollo Client 4, GraphQL 16, GraphQL Codegen.
- Redux Toolkit, React Redux, Redux Persist.
- Vitest and Testing Library.
- Yarn.

## Architecture

The application provider shell composes persisted Redux state, Apollo, Mantine, modals, notifications, and routing. The current router exposes one dashboard. Its hook queries `adminOverview` and supplies a static fallback when the live response is missing or errors.

Only the settings slice is persisted. Generated client interfaces are intended to live under `src/interfaces/graphql`.

## Folder Ownership

- `src/app`: provider composition.
- `src/router`: route configuration.
- `src/dashboard`: overview components, constants, GraphQL, hook, and interfaces.
- `src/redux/settings`: persisted internal UI settings.
- `src/services`: Apollo and external-service wiring.
- `src/interfaces/graphql`: generated GraphQL client artifacts.

## Commands

- `yarn dev` — Vite development server on port 5174.
- `yarn generate` — configured GraphQL Codegen entry point; currently blocked by the absent sibling schema artifact.
- `yarn test` — Vitest run.
- `yarn build` — project TypeScript build then Vite build.
- `yarn preview` — production preview on port 4174.

## Runtime/Deployment

Vite single-page application. No GitHub deployment workflow, Dockerfile, or other deployment configuration was found in the current repository checkout.

## Durable Conventions

- Preserve the admin/client-portal separation: this surface is for the internal team.
- Keep feature GraphQL, hooks, constants, interfaces, and components co-located under the feature boundary.
- Persist only deliberate cross-session state; current configuration limits persistence to settings.
- Treat generated GraphQL output as derived, not hand-maintained source.

## Constraints

- The current UI is an overview dashboard, not evidence that all backend administration capabilities have a UI.
- Historical backend contracts support organization review/rejection/resubmission and role management, but this page does not infer matching current Admin UI from backend capability alone.
- A temporary subscription-plan manager was explicitly reverted after scope correction. Database-managed plans exist, but current Admin plan management is incomplete.
- Static fallback overview data can mask a failed or unavailable backend query.
- GraphQL generation must not be reported as working until the canonical schema artifact/path is restored.

## Decisions And Rationale

- The internal portal remains independently deployable and does not share the authenticated business route tree.
- Direct Hermes correction confirms that internal admin and business client portal are different product surfaces; successful provider wiring does not authorize collapsing them into one application.
- Its separate `compflow-admin` repository and Yarn lifecycle are an explicit user correction, not an inferred split from current code alone.
- The provider composition establishes shared state, data, theme, modal, and notification infrastructure before feature expansion.

## Verification Expectations

Restore or identify the canonical GraphQL schema source before running generation. Then run generation, tests, build, and live dashboard checks for both real `adminOverview` data and error/fallback behavior. Any deployment claim requires separate configuration or an explicit external deployment record.

## Evidence

- Current `package.json`, README, provider/router/dashboard source, Redux persistence, Codegen config, and clean Git state at `main` commit `832109de1042`.
- Current repository evidence in [[../sources/compflow-project-knowledge-harvest-batch-1|CompFlow Project Knowledge Harvest — Batch 1]]; no historical CompFlow Codex session was discovered.
- Hermes session `20260710_173537_54b264` historically scaffolded and verified the separate admin application. First commit `5fd5786` preserves its Vite/Yarn, port `5174`, provider/router/Redux, `adminOverview`, fallback, and smoke-test lineage; see [[../sources/compflow-hermes-project-knowledge-harvest-supplement-1|CompFlow Hermes Project Knowledge Harvest — Supplement 1]].
- Hermes session `20260710_190402_e7ba9f` supplies later stack/file-ownership and admin-versus-client product-boundary provenance; see [[../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1|CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1]].
- [[../sources/compflow-proper-stack-hermes-continuations|CompFlow Proper Stack Hermes Continuations]] records the explicit admin-versus-business boundary, reverted plan manager, deliberate backend `adminOverview` removal, and current stale-consumer contradiction.
- [[../sources/compflow-backend-auth-hermes-continuations|CompFlow Backend Authentication Hermes Continuations]] records the downstream admin-review role in customer onboarding and backend organization/RBAC capabilities while preserving that current Admin coverage is narrower and its temporary plan manager was reverted.

## Contradictions

- `codegen.ts` points to `../compflow-backend/schema.graphql`, but that file is absent from the current backend checkout.
- The dashboard still queries the scaffold-era `adminOverview`, but the current backend no longer exposes that field. Its silent static fallback means visual completion does not establish backend integration.

## Confidence

High for current source structure and the generation-path contradiction; medium for runtime behavior because commands and live services were not executed.

## Open Questions

- Which back-office domains should the admin own, and should subscription-plan management be explicitly added in a separate approved scope?
- What is the canonical deployment path?
- Should backend query failure be surfaced distinctly from an intentionally seeded demo state?
