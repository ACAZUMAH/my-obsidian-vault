---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, portfolio, admin, cms, react]
sources:
  - ../sources/portfolio-project-knowledge-harvest-batch-1.md
confidence: high
---

# Portfolio Admin Portal

## Summary

React/Vite administrative CMS and dashboard for managing portfolio content, projects, media, leads, resumes, availability, and analytics.

## Purpose

Provides authenticated administrative workflows over the shared Portfolio GraphQL backend.

## Stack

- React 19, Vite 6, strict TypeScript.
- Apollo Client, Redux Toolkit/Redux Persist, React Router 7.
- Mantine 8 with modals and notifications.
- Formik and Yup.
- GraphQL Codegen and Vitest configured to permit no tests.

## Architecture

Global providers compose persisted Redux, Apollo, Mantine/theme, modals/notifications, and routing. Protected route ownership lives under `src/router`. Feature folders own pages, components, hooks/operations, interfaces, and details views.

## Folder Ownership

- `src/app`: provider composition.
- `src/router`: route definitions and protection.
- `src/redux`: persisted client/application state.
- `src/services`: Apollo client composition.
- `src/theme`: Mantine theme.
- Top-level feature folders: pages, components, hooks, operations, and feature contracts.

## Commands

- `yarn dev` — Vite on port 5174.
- `yarn build` — TypeScript and Vite build.
- `yarn generate` — GraphQL generation from backend endpoint.
- `yarn lint` — ESLint.
- `yarn test` — Vitest, currently allowed to pass with no tests.
- `yarn preview` — static preview.

## Runtime/Deployment

Static Vite application backed by the Portfolio GraphQL API. No tracked CI, container, hosting manifest, project README, or production deployment contract was found.

## Durable Conventions

- Co-locate GraphQL operations with focused feature hooks; avoid one monolithic operations file.
- Feature entities own their components, hooks, and details views.
- Forms use Formik/Yup; shared conditional rendering uses the established component.
- Provider ordering is deliberate: persistence, Apollo, design system, then router.
- Query hooks normalize loading, empty, and error states.

## Constraints

- Codegen depends on a reachable backend endpoint rather than a checked-in schema snapshot.
- Current test configuration may pass with no tests.
- Feature-directory capitalization is inconsistent and should not be expanded casually.

## Decisions And Rationale

The admin was intended to mirror proven Redux/router/Apollo patterns and preserve entity-local ownership. The user rejected a historical project CRUD structure as incomplete; future work must inspect current feature folders rather than accepting the historical “complete” claim.

## Verification Expectations

Run Codegen against the intended backend, lint, focused route/hook/form tests, full tests, and build. Start the backend and admin, then exercise login, protected routing, dashboard, project/media CRUD, leads, resumes, availability, analytics, loading/error states, and generated-contract compatibility.

## Evidence

- Clean `main@b0a86f9009d7`, current package/config/provider/router/Apollo/Redux/feature structure.
- Historical architecture and reported Codegen/build/browser checks in [[../sources/portfolio-project-knowledge-harvest-batch-1|Portfolio Project Knowledge Harvest — Batch 1]].

## Contradictions

- The initial record reported project CRUD complete, but the user later rejected its folder structure and the restructuring ended unfinished.
- No tracked substantive tests, README, CI, or deployment contract were found.
- Historical browser checks are not current integration proof.

## Confidence

High for current static stack and ownership; medium for complete CRUD/runtime behavior because no current generation, tests, build, backend, or browser flow was run.

## Open Questions

- Which admin feature folders still require the rejected project-structure correction?
- What is the production deployment target and API endpoint contract?
- Which authenticated route and CRUD flows need first focused tests?