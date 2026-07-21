---
type: entity
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, livelycura, erp, web, desktop]
sources:
  - ../../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../../sources/livelycura-project-knowledge-harvest-batch-2.md
  - ../../sources/livelycura-project-knowledge-harvest-batch-3.md
confidence: high
---

# LivelyCura Pharmacy Portal

## Summary

Primary LivelyCura/SERLP ERP operator application, delivered as web and Electron desktop builds.

## Purpose

Coordinates catalog, inventory, selling, buying, accounting, HRM/payroll, CRM, courier/logistics, marketplace, manufacturing, approvals, MLS, reporting, configuration, and agent-assisted work across organizations and facilities.

## Stack

- Node `>=22.12.0`, TypeScript, React 18, Vite 5.
- Mantine 8, Apollo Client, Redux Toolkit, React Router 6.
- Electron desktop packaging.
- Vitest, Storybook, GraphQL Codegen, ESLint, Prettier, Husky.
- Yarn.

## Architecture

`src/app`, `providers`, `redux`, `router`, and `services` compose shared runtime. Operational domains are direct top-level feature folders. `src/layouts/main` owns app registry, module navigation, header, sidebar, and global utilities. Electron code lives in top-level `electron/`.

MLS separates list, create, edit, and detail flows. `src/mls/builder` owns shared technician-facing form/mapping components, while `src/rendererEngine` owns reusable schema evaluation and definition/result/report/workflow rendering.

## Folder Ownership

- `catalog`, `inventory`, `selling`, `buying`, `accounting`, `manufacturing`: core ERP.
- `hrm`, `payroll`, `crm`, `courier`, `marketplace`, `mls`: operational modules.
- `home`, `apps`, `layouts`, `globalSearch`, `switcher`, `organizationTheme`: shell and navigation.
- `agent`, `rendererEngine`: AI-assisted experience and rendering infrastructure.
- `mls/createTestDefinition`, `mls/editTestDefinition`, `mls/testDefinitionDetails`, `mls/testDefinitions`: flow-specific ownership; each owns its page and operations while importing the shared builder/renderer.
- `layouts/pos` and `selling/posTerminal`: standalone general product POS shell and selling experience, separate from the inventory-backed Sell page.
- `apps/customApps`: management and analytics for banners belonging to organization apps that Admin Portal has already assigned.

## Commands

- `yarn start` / `yarn dev`
- `yarn generate`
- `yarn lint`, `yarn format:check`, `yarn type-check`
- `yarn test`, `yarn test:ci`
- `yarn build`
- `yarn dev:desktop`, `yarn build:desktop`, `yarn dist:mac`, `yarn dist:win`
- `yarn storybook`

## Runtime/Deployment

Vite web app with Docker/Compose, CI/staging/production workflows, and Electron desktop release workflow for macOS and Windows.

## Durable Conventions

- Keep global search, fullscreen/agent actions, and profile/logout accessible from Home without requiring entry into an app.
- Prevent header congestion by giving context, search, and actions explicit ownership.
- Breadcrumbs belong in the module header, not the sidebar; current `MainHeader` implements this latest correction.
- Home owns organization/facility context and app discovery. Current layout uses four app columns normally and five only at `min-width: 120em`, so laptop widths remain four or fewer.
- Theme controls may live outside the dense top row; current Home places them in its appearance footer.
- Keep features split into focused folders/components/hooks; do not put a whole domain in one file.
- MLS result details separate overview, values, AI review, and delivery concerns.
- Separate create, edit, detail, and list ownership. Each GraphQL operation has a focused hook/file, and each lifecycle action has its own confirmation modal; shared builders receive state and callbacks through props.
- Design test-definition controls for laboratory technicians. Do not expose JSON storage, raw relation IDs, developer-only keys, or disabled form controls as the definition viewer; compile lab-language state into the generated GraphQL contract.
- Use the same reusable renderer for definition review, detail view, and future request/result workflows. Samples render names/codes, and nested workflow/result/rule/report information must not disappear between builder and renderer.
- Preserve table column controls and established catalog/table/modal patterns for MLS Samples and HRM Departments.
- Browser-visible UI work requires a real route check in the running app after static checks; report honestly when browser automation is unavailable.
- Custom-app tabs come from actual active organization assignments. Forms remain form-focused, mutation calls live in owned hooks/modals/cards, and this portal must not create or infer assignments.

## Constraints

- Do not add disposable screenshots or markdown artifacts to the repository during UI work.
- Reuse current components, tokens, and feature architecture when applying visual inspiration.
- Current package/lockfile is Yarn-authoritative despite npm examples in README.
- Product sync occurs after a TestDefinition exists; it is not part of initial definition form ownership.
- The standalone POS remains product-based and sale-generic. Lab-linked products use the ordinary create-sale flow, and the existing inventory-backed Sell page remains unchanged.
- If an organization has no assigned custom apps, hide the navigation entry or redirect the route safely rather than rendering a fake/default app.

## Decisions And Rationale

The Home launchpad is both navigation and a global-control surface. Users should not enter an app merely to search globally, log out, or toggle fullscreen. Large-monitor density can increase, but normal laptops keep a less crowded four-column grid.

Laboratory UI reflects the backend human-review contract: AI review is visible to staff, invalid results can be corrected/revalidated, final values lock, and delivery follows finalization.

The TestDefinition builder uses technician-facing state plus mapper/compiler boundaries for JSON-shaped result checks, interpretations, and report layout. The current implementation is a guided wizard with live operational review; historical tab, stepper, and single-page accordion variants are not independent conventions.

The POS terminal is intentionally mounted outside the main ERP shell so it can optimize a focused selling task while reusing organization/facility context, theme, fullscreen, profile, permissions, and the product-wide visual language.

Custom-app configuration is operational ownership, not platform assignment ownership. This portal manages banners, targeting, lifecycle, and analytics only after Admin Portal has assigned the app to the organization.

## Verification Expectations

Run codegen, lint/format, type check, Vitest, and production build. For desktop changes, run the Electron build path. Visually inspect Home/header/sidebar at laptop, very large monitor, tablet, and mobile widths; verify search, context switching, logout, fullscreen, breadcrumbs, app launch, MLS states, and courier handoffs. For MLS builder/renderer changes, exercise create, edit/draft autosave, publish/version lifecycle, definition detail, rule/report evaluation, samples, requests, and the general POS through the live browser rather than relying only on disabled/static previews. For custom apps, verify zero/one/multiple assignment states, app-specific banner mutations and analytics, permission gating, both themes, and the safe no-assignment route behavior.

## Evidence

- Current package, README, Home/header/layout/MLS/courier source, Electron, Docker/Compose, and workflows.
- Sessions `019f7d44…`, `019f7af0…`, `019f7714…`, `019f62a3…`, and `019f5cbd…` in [[../../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Sessions `019ec6f5…`, `019ea1d1…`, `019e9562…`, `019e78b1…`, and `019e7553…` in [[../../sources/livelycura-project-knowledge-harvest-batch-2|LivelyCura Project Knowledge Harvest — Batch 2]].
- Session `019e02a9…` plus current `src/apps/customApps` and navigation source in [[../../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].

## Contradictions

- README installation and quality examples use npm while current package scripts, lockfile, and family practice use Yarn.
- The README folder tree is incomplete relative to current domains.
- Historical UI proposals moved breadcrumbs and global actions between surfaces; latest explicit correction plus current code keep breadcrumbs in the header and global actions accessible on Home.
- TestDefinition builder layout moved through tabs, steppers, split panes, and accordions before the current guided wizard. Preserve technician guidance, flow ownership, and shared rendering; verify the current component before applying an older layout instruction.
- Historical action enablement and permission names changed during review. Current generated types, backend lifecycle mutations, portal hooks, and permission constants are authoritative.
- Historical custom-app work used `src/settings/customApps` and briefly placed assignment behavior in this portal. Current `src/apps/customApps`, current Admin Portal ownership, and the latest user correction supersede that path and responsibility.

## Confidence

High for current implementation and latest launchpad/result corrections.

## Open Questions

- Should the repository add a root `AGENTS.md` consolidating the now-proven shell, feature-ownership, and verification rules?
- Which test-request and result-entry screens should become the first non-definition consumers of `rendererEngine`?
- How will courier-company console flows fit into this same ERP portal without overloading merchant navigation?
