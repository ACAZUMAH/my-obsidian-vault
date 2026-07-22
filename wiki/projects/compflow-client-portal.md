---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, compflow, client-portal, react, payroll]
sources:
  - ../sources/compflow-project-knowledge-harvest-batch-1.md
  - ../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1.md
  - ../sources/compflow-proper-stack-hermes-continuations.md
  - ../sources/compflow-backend-auth-hermes-continuations.md
confidence: high
---

# CompFlow Client Portal

## Summary

Authenticated business workspace for employee, payroll, organization, settings, and subscription activity.

## Purpose

Gives business owners the operational surface for using ComplianceFlow after signup, verification, and subscription onboarding.

## Stack

- React 19, Vite 5, TypeScript 5.5, React Router 7.
- Mantine 9 with forms, modals, and notifications.
- Apollo Client 4, GraphQL 16, GraphQL Codegen.
- Redux Toolkit, React Redux, Redux Persist.
- Vitest and Testing Library.
- Yarn in scripts/workflows; an npm lockfile also exists.

## Architecture

The provider shell composes persisted Redux, Apollo, Mantine, modals, notifications, and routing. Public routes cover login, registration, and verification. Protected routes cover dashboard, employees, payroll, settings, and subscription; persisted authentication and organization verification control access.

The Apollo client injects the persisted bearer token and a client-name header. Employee hooks use live backend CRUD operations. Other feature services currently mix static data, in-memory state, delays, and placeholder responses.

## Folder Ownership

- `src/features/auth`: login, registration, verification, auth GraphQL/services, and route guards.
- `src/features/employees`: live GraphQL employee list and mutations plus an older parallel mock service.
- `src/features/dashboard`, `payroll`, `subscription`, `settings`: pages, hooks, services, and current demo/live boundaries.
- `src/redux/auth`, `dashboard`, `settings`: persisted application state.
- `src/layouts` and `src/router`: authenticated shell and route ownership.
- `src/services`: Apollo and shared service configuration.
- `src/interfaces/graphql`: generated GraphQL client artifacts.

## Commands

- `yarn dev` — Vite development server on port 5177.
- `yarn generate` — configured GraphQL Codegen entry point; currently blocked by the absent sibling schema artifact.
- `yarn test` — Vitest run.
- `yarn build` — project TypeScript build then Vite build.
- `yarn preview` — production preview on port 4175.

## Runtime/Deployment

Vite single-page application. GitHub Actions use Node 22 and Yarn for CI on `main` and `develop`; separate workflows target Netlify staging and production. Deployment secret values were not inspected or preserved.

## Durable Conventions

- Authentication state and organization verification guard protected business routes.
- Keep feature UI, hooks, GraphQL, service behavior, and interfaces inside the owning feature.
- Use the Apollo auth link for bearer/client headers rather than adding per-operation transport logic.
- Treat backend GraphQL as authoritative for employee CRUD; do not extend the parallel in-memory employee service as though it were production persistence.
- Preserve the business/client boundary: internal team operations belong in [[compflow-admin|CompFlow Admin]].

## Constraints

- Current backend authentication is OTP-only; simulated password/passcode/two-factor settings are not a supported backend contract.
- Organization creation should follow the backend's verified signup and authenticated subscription checkout sequence, not the portal's current direct-create placeholder flow.
- Dashboard, payroll, subscription, and parts of settings are not fully backend-backed.
- Conflicting lockfiles require an explicit package-manager decision before dependency changes.

## Decisions And Rationale

- Protected routing separates identity verification from operational access.
- Persisted auth allows Apollo and route guards to share one principal state.
- Feature ownership keeps payroll, employee, subscription, and security flows independently replaceable as their live backend contracts mature.
- Direct continuation evidence confirms creation and provider/runtime verification of the separate business-facing Client Portal after the root record merely requested it. Current source is substantially newer, but preserves the boundary and application ownership.

## Verification Expectations

First resolve lockfile ownership and the GraphQL schema-generation source. Then run generation, tests, build, and live flows for login/OTP, organization verification, employee CRUD, dashboard, payroll, subscription, and settings. Explicitly distinguish demo responses from backend-backed success and verify authorization redirects after reload because auth is persisted.

## Evidence

- Current `package.json`, provider/router/auth/employee and other feature source, Redux/Apollo configuration, Codegen config, workflows, and clean Git state at `develop` commit `55e4e4d16087`.
- Repository-only evidence in [[../sources/compflow-project-knowledge-harvest-batch-1|CompFlow Project Knowledge Harvest — Batch 1]]; no historical CompFlow Codex session was discovered.
- Product-boundary-only Hermes provenance from `20260710_190402_e7ba9f` in [[../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1|CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1]]; current client implementation remains repository evidence rather than a session-completed outcome.
- `20260711_143433_be702f` in [[../sources/compflow-proper-stack-hermes-continuations|CompFlow Proper Stack Hermes Continuations]] owns the separate Client Portal creation, provider wiring, GraphQL generation/tests/build, browser role verification, and dashboard-folder correction; later feature expansion remains current-repository evidence.
- [[../sources/compflow-backend-auth-hermes-continuations|CompFlow Backend Authentication Hermes Continuations]] provides backend ownership for employee, tax, payroll-run, report, payslip, role, and organization-lifecycle APIs. It does not prove the portal’s current demo payroll/subscription screens are fully integrated.

## Contradictions

- Both `yarn.lock` and `package-lock.json` exist, while package scripts and CI favor Yarn.
- Registration directly creates an organization and returns placeholder identity/token values; the backend requires OTP verification, JWT authentication, checkout, and successful payment before organization creation.
- Password, passcode, and two-factor settings are simulated despite the backend's OTP-only authentication contract.
- Live employee hooks coexist with an older in-memory employee service, while dashboard, payroll, and subscription remain substantially static/demo-driven.
- `codegen.ts` points to an absent backend `schema.graphql` artifact.

## Confidence

High for current route/data-source boundaries and contradictions; medium for end-to-end behavior because no application, backend, or deployment was executed.

## Open Questions

- Which demo services are intentional product prototypes versus unfinished integrations?
- Should direct organization registration be removed in favor of the backend platform-signup/checkout contract?
- Which authentication settings will be supported beyond OTP, if any?
- Which lockfile is canonical, and what should generate the shared GraphQL schema artifact?
