---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, compflow, frontend, react, payroll]
sources:
  - ../sources/compflow-project-knowledge-harvest-batch-1.md
  - ../sources/compflow-hermes-project-knowledge-harvest-supplement-1.md
  - ../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1.md
  - ../sources/compflow-proper-stack-hermes-continuations.md
  - ../sources/compflow-backend-auth-hermes-continuations.md
confidence: high
---

# CompFlow Public Frontend

## Summary

Public ComplianceFlow marketing and plan-discovery site for payroll compliance services aimed at Ghanaian businesses.

## Purpose

Explains the product, presents payroll/compliance content and pricing, and directs prospective businesses into the platform signup journey owned by [[compflow-backend|CompFlow Backend]].

## Stack

- React 19, Vite 5, TypeScript 5.5, React Router 7.
- Mantine 9, Tabler icons, CSS Modules.
- Apollo Client 4 and GraphQL 16.
- Vitest, Testing Library, ESLint, Prettier.
- Yarn.

## Architecture

`src/app` composes Apollo, Mantine, notifications, and browser routing. `src/router` exposes the landing page under a shared layout. `src/home` is the feature boundary and owns its page, content, payroll examples, components, hooks, interfaces, styles, and tests.

`useHomeContent` composes a feature-local Apollo `usePlatformPlansQuery`, dedicated plan formatter, and local fallback content. Apollo client ownership remains under `src/services`, and fallback resilience must not be mistaken for a successful live query.

## Folder Ownership

- `src/app`: global providers and application composition.
- `src/router`: route table and fallback navigation.
- `src/layouts`: site shell, header, and footer.
- `src/home`: landing-page feature and local tests/styles.
- `src/services`: Apollo client and external-service wiring.
- `src/constants` and `src/styles`: site-level configuration and theme/global CSS.

## Commands

- `yarn dev` — Vite development server on port 5173.
- `yarn build` — TypeScript check then Vite build.
- `yarn test` — Vitest run.
- `yarn lint`, `yarn lint:fix`.
- `yarn format:check`, `yarn format:fix`.
- `yarn preview` — production preview on port 4173.

## Runtime/Deployment

Vite single-page application. GitHub Actions use Node 22 and Yarn for CI on `main` and `develop`; separate workflows target Netlify staging and production. Deployment secret names exist in workflow configuration, but values were not inspected or preserved.

## Durable Conventions

- Keep landing-page behavior inside the `src/home` feature boundary rather than scattering it through global folders.
- Use Mantine for shared design primitives and CSS Modules for feature-local styling.
- Keep public plan display resilient to backend unavailability, while treating the backend response as the live source when available.
- Reuse the family Apollo/site configuration instead of embedding endpoints in components.

## Constraints

- The site is a public marketing surface, not the authenticated payroll workspace.
- There is currently one product page route; new application workflows belong in the client portal or backend unless the public acquisition journey explicitly needs them.
- Static fallback content can hide live-plan failures, so integration verification must distinguish fallback rendering from a successful GraphQL response.

## Decisions And Rationale

- Independent repository/application boundaries keep the public acquisition surface deployable separately from [[compflow-admin|CompFlow Admin]], [[compflow-client-portal|CompFlow Client Portal]], and the backend.
- This boundary is also an explicit user correction: the promotional web belongs in the existing `compflow` folder with its own Yarn lifecycle, not in an inferred root monorepo.
- Live plan lookup lets public pricing follow backend subscription configuration; fallback content preserves a usable marketing page when that lookup fails.
- The public site is the primary customer subscription entry: plan discovery hands off to signup, OTP verification, authenticated checkout, verified payment, and post-payment tenant provisioning. Internal Admin creation is an alternative, not the default customer path.

## Verification Expectations

Run install only when authorized, then lint, format check, Vitest, build, and a live page smoke test. Confirm the home page under both successful `platformPlans` data and an unavailable backend so fallback behavior is not mistaken for end-to-end success. Deployment changes require staging and production workflow review without exposing secret values.

## Evidence

- Current `package.json`, README, provider/router/home source, Apollo configuration, tests, GitHub workflows, and clean Git state at `develop` commit `03421056ea70`.
- Current repository evidence in [[../sources/compflow-project-knowledge-harvest-batch-1|CompFlow Project Knowledge Harvest — Batch 1]]; no historical CompFlow Codex session was discovered.
- Hermes session `20260710_173537_54b264` historically scaffolded and verified the separate promotional application. First commit `21dbe81` preserves its Vite/Yarn, port `5173`, payroll-first paid-pilot, and smoke-test lineage; see [[../sources/compflow-hermes-project-knowledge-harvest-supplement-1|CompFlow Hermes Project Knowledge Harvest — Supplement 1]].
- Hermes session `20260710_190402_e7ba9f` adds the explicit correction that a working project requires the actual dependency/provider/runtime stack and exact saved-skill file ownership, not a minimal renderable stub; see [[../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1|CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1]].
- Continuations #3–#5 in [[../sources/compflow-proper-stack-hermes-continuations|CompFlow Proper Stack Hermes Continuations]] establish database-managed public plans, rejection of raw feature fetching in favor of Apollo provider/query-hook/formatter ownership, historical tests/builds, and exact safe publication of the current `develop` commit.
- `20260711_221940_e79205` in [[../sources/compflow-backend-auth-hermes-continuations|CompFlow Backend Authentication Hermes Continuations]] owns the explicit correction making promotional-site onboarding the normal customer path; later records replace its early static/environment plan pricing with database-managed plans.

## Contradictions

- The historical scaffold was a minimal paid-pilot landing page; current code supersedes that implementation with broader content and live `platformPlans` lookup while preserving its acquisition purpose.
- A rendered pricing section may be live GraphQL data or static fallback unless the network path is verified.

## Confidence

High for current repository structure and configured commands; medium for live backend/deployment behavior because no application, build, or workflow was executed.

## Open Questions

- Should GraphQL failure be visible to monitoring while the visitor continues to receive fallback content?
- Which public actions will own the handoff into signup and checkout as the acquisition journey expands?
