---
type: project
status: active
created: 2026-07-21
updated: 2026-10-10
tags: [project, livelycura, erp, web, desktop]
sources:
  - ../sources/livelycura-marketplace-single-delivery.md
  - ../sources/livelycura-independent-fleet-and-platform-dispatch.md
  - ../sources/livelycura-graphql-contract-compatibility.md
  - ../sources/livelycura-lab-order-agent-environment-correction.md
  - ../sources/marketplace-scoped-admin-catalog-order-restructure.md
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/livelycura-project-knowledge-harvest-batch-2.md
  - ../sources/livelycura-project-knowledge-harvest-batch-3.md
  - ../sources/livelycura-project-knowledge-harvest-batch-4.md
  - ../sources/hermes-livelycura-skills-keks-pharmacy-harvest-batch-1.md
  - ../sources/livelycura-stock-sales-hermes-supplement-2.md
  - ../sources/livelycura-stock-sales-hermes-supplement-3.md
  - ../sources/graphql-product-bora-paystack-hermes-chain.md
  - ../sources/portfolio-carousel-skills-livelycura-hermes-supplement.md
  - ../sources/product-lab-badge-mls-hermes-chain.md
  - ../sources/livelycura-pos-missing-price-decision.md
confidence: high
---

# LivelyCura Pharmacy Portal

## Summary

Primary LivelyCura/SERLP ERP operator application, delivered as web and Electron desktop builds.

## Purpose

Coordinates catalog, inventory, selling, buying, accounting, HRM/payroll, CRM, fleet/logistics, marketplace, manufacturing, approvals, MLS, reporting, configuration, and agent-assisted work across organizations and facilities.

## Stack

- Node `>=22.12.0`, TypeScript, React 18, Vite 5.
- Mantine 8, Apollo Client, Redux Toolkit, React Router 6.
- Electron desktop packaging.
- Vitest, Storybook, GraphQL Codegen, ESLint, Prettier, Husky.
- Yarn.

## Architecture

CRM owns the organization-scoped responder surface from [[../concepts/livelycura-customer-support-architecture|LivelyCura Customer Support Architecture]]. Its support routes keep permission and organization boundaries but intentionally bypass the general CRM-module gate; all other CRM routes retain that gate.

`src/app`, `providers`, `redux`, `router`, and `services` compose shared runtime. Operational domains are direct top-level feature folders. `src/layouts/main` owns app registry, module navigation, header, sidebar, and global utilities. Electron code lives in top-level `electron/`.

MLS separates list, create, edit, and detail flows. `src/mls/builder` owns shared technician-facing form/mapping components, while `src/rendererEngine` owns reusable schema evaluation and definition/result/report/workflow rendering.

## Folder Ownership

- `catalog`, `inventory`, `selling`, `buying`, `accounting`, `manufacturing`: core ERP.
- `hrm`, `payroll`, `crm`, `fleet`, `marketplace`, `mls`: operational modules.
- `home`, `apps`, `layouts`, `globalSearch`, `switcher`, `organizationTheme`: shell and navigation.
- `agent`, `rendererEngine`: AI-assisted experience and rendering infrastructure.
- `mls/createTestDefinition`, `mls/editTestDefinition`, `mls/testDefinitionDetails`, `mls/testDefinitions`: flow-specific ownership; each owns its page and operations while importing the shared builder/renderer.
- `mls/testRequestDetails/interfaces`: feature-owned prop contracts for detail sections; components import those contracts and use explicit typed declarations rather than declaring prop interfaces inline.
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

- Agent is available in local development and staging, hidden in production, and always subject to `agent.access`. Share the environment gate across Home, the main header, and the panel; Vite's optimized-build flag alone cannot distinguish staging from production.
- Keep global search, fullscreen/agent actions, and profile/logout accessible from Home without requiring entry into an app.
- Prevent header congestion by giving context, search, and actions explicit ownership.
- Breadcrumbs belong in the module header, not the sidebar; current `MainHeader` implements this latest correction.
- Home owns organization/facility context and app discovery. Current layout uses four app columns normally and five only at `min-width: 120em`, so laptop widths remain four or fewer.
- Theme controls may live outside the dense top row; current Home places them in its appearance footer.
- Keep features split into focused folders/components/hooks; do not put a whole domain in one file.
- In `testRequestDetails`, keep prop interfaces in the feature interfaces folder and components explicitly typed. Reread every touched component after structural edits; a successful-looking tool response is not file-change verification.
- MLS result details separate overview, values, AI review, and delivery concerns.
- Separate create, edit, detail, and list ownership. Each GraphQL operation has a focused hook/file, and each lifecycle action has its own confirmation modal; shared builders receive state and callbacks through props.
- Fleet people are operators, with `fleet.operators.read/manage` access and `/fleet/operators` navigation. The roster follows the established header/table/filter/modal structure; create, profile update, activate, deactivate, archive, and work-capacity commands each have their own hook. Do not restore `fleetDrivers`, `saveFleetDriver`, custom revisions, expected versions, or client-generated idempotency fields.
- Fleet operator creation uses the protected `/fleet/operators/create` page. `src/fleet/createOperator` owns its page, form components, profile field editors, interfaces, and mutation hook. `src/fleet/operators` owns the roster, profile updates, lifecycle, and capacity; `src/fleet/operatorDetails` owns the routed detail page and its complete by-ID read flow. Do not place create/detail files in the roster folder or use one form component for both create and update.
- Fleet create-page inputs use field-specific placeholders throughout the main form and nested editors. Fleet list-header filters have placeholders instead of visible input labels, with accessible names for screen readers. Fleet `useFilters` hooks mirror established Portal URL parsing, memoized query values, dedicated filter callbacks, pagination reset, and reset action patterns. Parse `page` and `limit` through the ordinary numeric helper and list defaults; keep an unselected status or enum filter nullable, omit it from query variables, and expose clearable selects rather than an invented `ALL` value. Visible Fleet sidebar links and detail tabs include icons.
- Fleet date and date-time form fields use Mantine `DateInput` and `DateTimePicker`; list date ranges use the Portal’s `DatePickerInput` and `normalizeDatePickerRange` helper. Keep picker callbacks bound to the owning Formik or URL-filter state and preserve local date semantics when building query bounds.
- Fleet operator create and update forms follow existing Portal form structure: a feature-owned `use…Form` hook contains typed Formik state and a Yup schema; payload helpers transform validated values; the page or modal coordinates mutation/navigation; components render supplied form state. Do not add `src/fleet/shared` as a generic form, scope, upload, or helper layer.
- Under `src/fleet`, hook/function names and file basenames omit redundant `Fleet` (for example, `useCreateOperatorMutation`). Keep operations aligned with renamed Fleet GraphQL fields/types and regenerated client types. Route contracts remain centrally owned. Date-only filters send the selected local day as inclusive `startDate`/`endDate` bounds. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet naming and filter corrections]].
- Exception (2026-10-10): Fleet jobs live in `src/fleet/fleetJobs`, `createFleetJob` and `fleetJobDetails`, with `FleetJob*` components and hooks and GraphQL operations that follow the backend rename. URLs (`/fleet/jobs...`), `FLEET_JOBS`-style route constants and visible "Jobs" labels stay unchanged. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Fleet jobs naming decision]].
- Fleet operator emergency contacts, identity documents, licenses, and other documents use accordion sections with the add action inside each panel. Keep every operator editor/profile component in its own file under the owning create or update folder instead of a multi-component editor bundle.
- Fleet operator profile-image uploads show the selected image as an inline preview. Update forms also resolve the saved private image through the existing temporary URL query; changing or removing the image updates both the preview and Formik upload ID.
- Fleet operator identity-document sides, license attachments, and other documents show inline image/PDF previews. Each upload field owns its loading state, so uploading one file never marks sibling upload buttons as loading.
- Fleet operator details are a protected `/fleet/operators/:id` page, not a modal. The detail folder owns the by-ID query and focused section components. Show the operator's business profile, compliance files, and work/location state; do not expose database, tenancy, account, or duplicate operator IDs, routine created/updated timestamps, or inactive archive placeholders. Show archive context only for archived operators.
- Fleet operator details follow the CRM Customer and Catalog Product record-page composition: a useful identity summary followed by one tabbed record surface. The private profile photo appears as a circular avatar with an initials fallback and remains visible on narrow layouts. Create and update profile-image controls show the image itself with focused change/remove actions.
- Keep Fleet operator profile, lifecycle, and live work state visible as separate concerns. Registration covers the full person and compliance profile; roster/detail views show online state, availability, current load, capacity, heartbeat, and last coordinates, while capacity changes use the dedicated dispatch permission and mutation.
- Fleet Vehicles follows the same feature ownership: `src/fleet/vehicles` owns the register and update/archive actions, `src/fleet/createVehicle` owns the dedicated Formik/Yup create page, and `src/fleet/vehicleDetails` owns the routed details page. Vehicle details present identity, service state, capacity/odometer, seats, documents, and archive context without raw persistence metadata; private files use inline previews and per-field upload state.
- Route and menu only rebuilt Fleet areas. Keep unfinished earlier Fleet screens unreachable until their own contract and architecture pass succeeds.
- Declare Fleet routes in the shared `routeEndpoints` object and import those constants everywhere navigation is defined or asserted, including the app registry, menu, router, redirects, and tests. Follow the established parent module guard and child permission guard structure.
- Mount no Courier route, catch-all, moved notice, legacy redirect, or retired-Courier history feature in Pharmacy Portal. Keep `src/billing/legacyDeliveries`, delivery-history routes, menu entries, permission bridges, and Courier route constants absent. Current merchant/order references remain with their owning Selling and Billing workflows.
- Design test-definition controls for laboratory technicians. Do not expose JSON storage, raw relation IDs, developer-only keys, or disabled form controls as the definition viewer; compile lab-language state into the generated GraphQL contract.
- Use the same reusable renderer for definition review, detail view, and future request/result workflows. Samples render names/codes, and nested workflow/result/rule/report information must not disappear between builder and renderer.
- Preserve table column controls and established catalog/table/modal patterns for MLS Samples and HRM Departments.
- Browser-visible UI work requires a real route check in the running app after static checks; report honestly when browser automation is unavailable.
- Custom-app tabs come from actual active organization assignments. Forms remain form-focused, mutation calls live in owned hooks/modals/cards, and this portal must not create or infer assignments.
- CRM message reads consume only current `MobileApps` values. Historical `CUSTOMER` targets are filtered at the backend GraphQL boundary; do not restore that retired enum value in the Portal contract.
- Deliveries are single tasks; multi-pickup routes and pickup stops were removed for launch. Marketplace bid orders have no delivery task and no dispatch actions; the winning facility sees only the marketplace delivery's pickup code and rider name, read-only. Source: [[../sources/livelycura-marketplace-single-delivery|Marketplace single delivery decision]].
- Keep current merchant/order delivery references in their Selling and Billing owners. The retired company Courier was preproduction, so do not create a legacy history, settlement, or remittance surface for it under Billing.
- Sale-return forms and details use product-line identity through `saleItemId`; do not retain inventory IDs or present one arbitrary batch/expiry when a returned quantity can restore across multiple movements.
- Keep every top-level sidebar label registered once. Consolidate overlapping Manufacturing, Marketplace, Courier, or other entries in the canonical menu registry and retain duplicate-label regression coverage.
- Ordinary ERP product and category creation/details remain marketplace-agnostic. Do not expose canonical marketplace categories, business-product publication, or marketplace configuration metadata in this portal.

## Constraints

- Do not add disposable screenshots or markdown artifacts to the repository during UI work.
- Reuse current components, tokens, and feature architecture when applying visual inspiration.
- Current package/lockfile is Yarn-authoritative despite npm examples in README.
- Product sync occurs after a TestDefinition exists; it is not part of initial definition form ownership.
- Sale POS supports stock and non-stock products and creates requests for lab-linked sale items. Order placement alone does not create requests. The product-based POS payload omits inventory IDs; the backend decides allocation from the persisted stock/bundle flags. Keep the inventory-backed Sell page's explicit batch behavior separate.
- In the standalone POS, a product without a facility price remains visible at `0.00`, but its cart action is disabled. A configured zero-priced product remains sellable; use the persisted facility-price identity, not a positive-value check, to distinguish the two cases.
- If an organization has no assigned custom apps, hide the navigation entry or redirect the route safely rather than rendering a fake/default app.
- Menu composition must not emit duplicate top-level feature entries through overlapping registries.

## Decisions And Rationale

- Replace the company Courier console with an independent Fleet product covering vehicles, operators, jobs, trips, and company operations. Platform network fulfillment belongs to Admin; company opt-in is separate. Because the retired company Courier was never used in production, remove it without a legacy Portal surface. Source: [[../sources/livelycura-independent-fleet-and-platform-dispatch|Independent Fleet and platform dispatch decision]].

The Home launchpad is both navigation and a global-control surface. Users should not enter an app merely to search globally, log out, or toggle fullscreen. Large-monitor density can increase, but normal laptops keep a less crowded four-column grid.

Laboratory UI reflects the backend human-review contract: AI review is visible to staff, invalid results can be corrected/revalidated, final values lock, and delivery follows finalization.

The TestDefinition builder uses technician-facing state plus mapper/compiler boundaries for JSON-shaped result checks, interpretations, and report layout. The current implementation is a guided wizard with live operational review; historical tab, stepper, and single-page accordion variants are not independent conventions.

The POS terminal is intentionally mounted outside the main ERP shell so it can optimize a focused selling task while reusing organization/facility context, theme, fullscreen, profile, permissions, and the product-wide visual language.

Missing facility pricing is handled through action safety rather than hiding or replacing the displayed amount. The POS shows the normalized zero value and disables cart entry until a facility price exists, while preserving legitimate configured zero-price sales.

Custom-app configuration is operational ownership, not platform assignment ownership. This portal manages banners, targeting, lifecycle, and analytics only after Admin Portal has assigned the app to the organization.

Marketplace catalog classification follows the same ownership boundary: ERP organizations maintain ordinary products and internal categories, while Admin Portal assigns canonical marketplace categories and publication state for Business Products.

## Verification Expectations

Run codegen, lint/format, type check, Vitest, and production build. For desktop changes, run the Electron build path. Visually inspect Home/header/sidebar at laptop, very large monitor, tablet, and mobile widths; verify search, context switching, logout, fullscreen, breadcrumbs, app launch, unique top-level menu labels, MLS states, and courier handoffs. For MLS builder/renderer changes, exercise create, edit/draft autosave, publish/version lifecycle, definition detail, rule/report evaluation, samples, requests, and the general POS through the live browser rather than relying only on disabled/static previews. For custom apps, verify zero/one/multiple assignment states, app-specific banner mutations and analytics, permission gating, both themes, and the safe no-assignment route behavior. For sale returns, verify multi-product quantities and `saleItemId` payloads without inventory-era fields or misleading single-batch presentation. For marketplace bid orders, verify that no dispatch or delivery-status action appears and that only the winning facility sees the pickup code and rider.

## Evidence

- [[../sources/livelycura-lab-order-agent-environment-correction|LivelyCura Lab Sale And Agent Environment Corrections]] restores Sale POS as the lab trigger after the withdrawn order direction, while retaining local/staging Agent visibility with production disabled.
- Current package, README, Home/header/layout/MLS/courier source, Electron, Docker/Compose, and workflows.
- Sessions `019f7d44…`, `019f7af0…`, `019f7714…`, `019f62a3…`, and `019f5cbd…` in [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Sessions `019ec6f5…`, `019ea1d1…`, `019e9562…`, `019e78b1…`, and `019e7553…` in [[../sources/livelycura-project-knowledge-harvest-batch-2|LivelyCura Project Knowledge Harvest — Batch 2]].
- Session `019e02a9…` plus current `src/apps/customApps` and navigation source in [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].
- Session `019de35a…` plus current courier payload/type helpers and focused tests in [[../sources/livelycura-project-knowledge-harvest-batch-4|LivelyCura Project Knowledge Harvest — Batch 4]].
- Direct Hermes sessions `20260621_010814_92d057` and `20260621_024824_d0e17a` plus current static `testRequestDetails` source in [[../sources/hermes-livelycura-skills-keks-pharmacy-harvest-batch-1|Hermes LivelyCura Skills, Keks, And Pharmacy Harvest — Batch 1]]. Current source confirms ten matching components import prop contracts from `../interfaces` and use `React.FC<...>`; no current project command was rerun.
- Direct continuation `20260629_193407_346702` plus current sale-return form/detail source in [[../sources/livelycura-stock-sales-hermes-supplement-2|LivelyCura Stock And Sales Hermes Supplement — 2]].
- Direct continuation `20260712_183956_816de0` in [[../sources/livelycura-stock-sales-hermes-supplement-3|LivelyCura Stock And Sales Hermes Supplement — 3]] closes the historical Portal full-suite report while preserving that it ran before the final backend-only patch.
- [[../sources/graphql-product-bora-paystack-hermes-chain|GraphQL Product And Bora Paystack Hermes Chain]] records duplicate menu-registration cleanup and retained top-level-label regression coverage.
- The unique LivelyCura tail in [[../sources/portfolio-carousel-skills-livelycura-hermes-supplement|Portfolio Carousel, Skills, And LivelyCura Hermes Supplement]] records frontend MLS query-field consistency alongside the backend fallback correction; frontend type-check remained blocked and the final product-table badge request was unanswered.
- Topical successor `20260624_123800_8292b3` in [[../sources/product-lab-badge-mls-hermes-chain|Product Lab Badge And MLS Hermes Chain]] completes that unanswered request and later records own MLS refresh and stock/bundle UI work. Current POS keeps the Lab test badge, while the Products table replaced its historical Type column with Stock Behavior.
- [[../sources/livelycura-pos-missing-price-decision|LivelyCura POS Missing-Price Decision]] records the current missing-price presentation and cart-safety rule, verified by the focused product-card suite.
- [[../sources/marketplace-scoped-admin-catalog-order-restructure|Marketplace-Scoped Admin Catalog And Order Restructure]] restores the ordinary non-marketplace ERP product/category flow. On 2026-08-08 the generated contract and production build passed after the marketplace-category UI/hooks were removed.

## Contradictions

- The earlier 2026-09-09 Order POS direction was explicitly withdrawn later in the same conversation; Sale POS remains the lab-request trigger. Agent environment guidance was not withdrawn. A production-optimized staging build is not a production deployment.
- The Products query still fetches `testDefinitionId`, but the table no longer shows the requested Lab test/normal Type column; POS alone retains the explicit badge.
- README installation and quality examples use npm while current package scripts, lockfile, and family practice use Yarn.
- The README folder tree is incomplete relative to current domains.
- Historical UI proposals moved breadcrumbs and global actions between surfaces; latest explicit correction plus current code keep breadcrumbs in the header and global actions accessible on Home.
- TestDefinition builder layout moved through tabs, steppers, split panes, and accordions before the current guided wizard. Preserve technician guidance, flow ownership, and shared rendering; verify the current component before applying an older layout instruction.
- Historical action enablement and permission names changed during review. Current generated types, backend lifecycle mutations, portal hooks, and permission constants are authoritative.
- Historical custom-app work used `src/settings/customApps` and briefly placed assignment behavior in this portal. Current `src/apps/customApps`, current Admin Portal ownership, and the latest user correction supersede that path and responsibility.
- The historical interface move first produced a false completion claim and later a regex corruption before manual restoration. Current source confirms the final structure, but the session’s verification cited only a representative file reread and no full project checks.

## Confidence

High for current implementation and latest launchpad/result corrections.

## Open Questions

- Should the repository add a root `AGENTS.md` consolidating the now-proven shell, feature-ownership, and verification rules?
- Which test-request and result-entry screens should become the first non-definition consumers of `rendererEngine`?
- How will courier-company console flows fit into this same ERP portal without overloading merchant navigation?
