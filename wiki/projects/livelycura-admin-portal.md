---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, livelycura, admin, web]
sources:
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/livelycura-project-knowledge-harvest-batch-3.md
confidence: high
---

# LivelyCura Admin Portal

## Summary

Independent internal administration web application in the LivelyCura family.

## Purpose

Provides the platform control plane for organizations, facilities, users, roles, products, orders, courier operations, marketing, subscriptions, system administration, and organization custom-app assignment.

## Stack

- TypeScript, React 19, Vite 6.
- Mantine 8, Apollo Client, Redux Toolkit, React Router 7.
- Vitest, Storybook, ESLint, Prettier, Husky, GraphQL Codegen.
- Yarn lockfile.

## Architecture

`src/app` composes the application; `providers`, `redux`, `router`, and `services` own shared runtime wiring. Business areas live as direct top-level domain folders under `src`.

## Folder Ownership

- `organization`, `facility`, `users`, `roles`: administrative identity and access.
- Organization-owned custom-app components and hooks: explicit assignment and unassignment of managed apps.
- `product`, `order`, `courier`, `marketing`, `subscriptions`: operational domains.
- `components`, `layouts`, `hooks`, `helpers`, `constants`, `interfaces`: cross-domain presentation and utilities.

## Commands

- `yarn start` / `yarn dev`
- `yarn generate`
- `yarn lint`
- `yarn test`
- `yarn build`
- `yarn storybook`

## Runtime/Deployment

Static Vite web application with Docker and development/production Compose files. GitHub workflows cover CI, staging, and production.

## Durable Conventions

- Keep this administrative surface separate from the ERP operator portal and customer applications.
- Extend existing top-level domains rather than placing product logic in shared components.
- Regenerate GraphQL types after contract changes.
- Organization custom-app assignment belongs here. Do not make the ERP portal or a read operation create assignments implicitly.

## Constraints

- The current README is untouched GitLab starter boilerplate and is not reliable project documentation.

## Decisions And Rationale

The repository boundary keeps platform administration distinct from day-to-day ERP and customer workflows. Custom-app assignment is a platform-administration decision; assigned-app banner operations stay with the organization’s ERP surface.

## Verification Expectations

Run GraphQL generation when operations change, then lint, Vitest, build, and inspect affected routes. For custom apps, verify explicit assign/unassign behavior and confirm organization reads remain side-effect free. Use Storybook for reusable component work when relevant.

## Evidence

- Current `package.json`, `yarn.lock`, source folders, Docker/Compose files, and GitHub workflows.
- [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Session `019e02a9…` plus current organization custom-app source in [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].

## Contradictions

The README suggests no real product structure; current source and package scripts show a mature admin application. Current code is authoritative. The harvest excluded and preserved pre-existing modifications in generated GraphQL files, so it does not assert generated-output freshness.

## Confidence

High for stack, folder ownership, and custom-app assignment ownership; medium for the remainder of the broad product-purpose wording because no current project-specific README defines it directly.

## Open Questions

- Which operations are intentionally admin-only rather than shared with SuperAdmin behavior in the ERP portal?
- Should this repository receive its own root `AGENTS.md`?
