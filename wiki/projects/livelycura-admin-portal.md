---
type: project
status: active
created: 2026-07-21
updated: 2026-09-26
tags: [project, livelycura, admin, web]
sources:
  - ../sources/livelycura-independent-fleet-and-platform-dispatch.md
  - ../sources/livelycura-graphql-contract-compatibility.md
  - ../sources/marketplace-scoped-admin-catalog-order-restructure.md
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

Each marketplace workspace includes the permission-protected marketplace support queue and case thread from [[../concepts/livelycura-customer-support-architecture|LivelyCura Customer Support Architecture]], including assignment, private notes, lifecycle actions, foreground polling, and browser-alert deep links.

`src/app` composes the application; `providers`, `redux`, `router`, and `services` own shared runtime wiring. Business areas live as direct top-level domain folders under `src`. Marketplace administration begins with launchpad-style marketplace cards. Selecting one replaces the Marketplace app's sidebar links with marketplace-ID-scoped Organizations, catalog, category, order, and Settings routes; each route renders its established full list/table page.

## Folder Ownership

- `organization`, `facility`, `users`, `roles`: administrative identity and access.
- Organization-owned custom-app components and hooks: explicit assignment and unassignment of managed apps.
- `product`, `order`, `courier`, `marketing`, `subscriptions`: operational domains.
- `marketplaces/details`: marketplace-scoped route composition and capability gating; it passes the selected marketplace ID into existing organization/product/category/order/settings pages without building an in-content tab workspace.
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
- Admin Courier consumes the platform-rider `DeliveryAgent` contract. Do not query or present removed company-provider fields such as `agentType`, organization/facility ownership, or external-request opt-in; remove stale filters and generated typings with the operation.
- Admin delivery-task operations preserve the actual requestor type and relationship: Customer, Facility, or Organization. Query and present the matching requestor reference without treating facility or organization identity as rider/provider ownership.
- Keep notification consumption and Courier notification configuration separate. Put the signed-in administrator's notification inbox behind the main-header bell. Keep Courier Configuration in Courier navigation for platform rider delivery notification settings. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Admin notification and Courier configuration correction]].
- Keep notification feature ownership directly under `src/notifications`: root-level drawer/content plus `components`, `hooks`, `helpers`, and `interfaces`. Do not add a redundant `inbox` folder, and move operation hooks and imports together during structural changes.
- Organization custom-app assignment belongs here. Do not make the ERP portal or a read operation create assignments implicitly.
- Marketplace Business Product category/publication configuration belongs here. Keep its GraphQL operations in product hooks and its types in owning interface/generated folders; ERP clients must not recreate this control plane.
- Keep legacy marketplace list routes redirected to marketplace selection while retaining detail routes needed by scoped list views.
- Keep marketplace selection visually aligned with the main app launchpad. Once selected, put marketplace sections in the main sidebar and never rebuild them as tabs inside one details page.
- Filter selected-marketplace sidebar routes from the marketplace's enabled catalog sources and order modes; never advertise a disabled capability.
- Keep marketplace organization access as a searchable table with an explicit Add Organization modal. Keep one refresh control per list header and provide shape-matched skeletons for every loading marketplace list/table.
- Preserve the standard Admin table contract on marketplace pages: leading `#`, trailing labeled/centered `Actions`, and row action controls in that final column.
- Render marketplace table-body loading and data branches through the shared `Conditional` component, following the existing Roles, Orders, Products, Facilities, and Categories table structure.
- Implement marketplace list filters through owning URL-filter hooks and GraphQL filter inputs. Filter organization-owned products/orders by active marketplace organization access; keep category, publication, and status filters aligned with each backend query contract.

## Constraints

- The current README is untouched GitLab starter boilerplate and is not reliable project documentation.

## Decisions And Rationale

- Own LivelyCura network dispatch for standalone riders and requests from marketplaces, custom apps, and manual intake, fulfilled through SERLP Dispatch. Company fleet operations belong to the independent ERP Fleet product. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Independent Fleet and platform dispatch decision]].

The repository boundary keeps platform administration distinct from day-to-day ERP and customer workflows. Custom-app assignment is a platform-administration decision; assigned-app banner operations stay with the organization’s ERP surface. Marketplace selection establishes the administrative scope so catalog classification, organization access, category trees, bidding demand, direct fulfillment, and capability settings cannot drift across separate global pages.

## Verification Expectations

Run GraphQL generation when operations change, then lint, Vitest, build, and inspect affected routes. Marketplace work must verify selection, all nested tabs, capability-disabled subtabs, removed redundant selectors, business-product listing/publishing, and both order views. For custom apps, verify explicit assign/unassign behavior and confirm organization reads remain side-effect free. Use Storybook for reusable component work when relevant.

## Evidence

- Current `package.json`, `yarn.lock`, source folders, Docker/Compose files, and GitHub workflows.
- [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Session `019e02a9…` plus current organization custom-app source in [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].
- [[../sources/marketplace-scoped-admin-catalog-order-restructure|Marketplace-Scoped Admin Catalog And Order Restructure]] records marketplace-scoped navigation and Admin ownership. The 2026-08-08 implementation passed the production build, 32-file/117-test suite, focused marketplace-details tests, formatting, and `git diff --check`.
- The same source records the later UI corrections. Live verification on 2026-08-08 showed launchpad-style marketplace cards; capability-filtered ChopRoute and LivelyCura sidebars; searchable organization tables; the Add Organization modal; one refresh action; standardized `#`/`Actions` columns; and working organization/category/publication/status filters. A Check City filter updated the URL and returned only Check City products. The corrected production build and 34-file/121-test suite passed.

## Contradictions

The README suggests no real product structure; current source and package scripts show a mature admin application. Current code is authoritative. The harvest excluded and preserved pre-existing modifications in generated GraphQL files, so it does not assert generated-output freshness.

## Confidence

High for stack, folder ownership, and custom-app assignment ownership; medium for the remainder of the broad product-purpose wording because no current project-specific README defines it directly.

## Open Questions

- Which operations are intentionally admin-only rather than shared with SuperAdmin behavior in the ERP portal?
- Should this repository receive its own root `AGENTS.md`?
