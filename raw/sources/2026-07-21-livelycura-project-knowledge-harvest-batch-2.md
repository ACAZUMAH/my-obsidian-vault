# LivelyCura Project Knowledge Harvest — Batch 2 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: LivelyCura.
- Live repository root: `/Users/acazumah/Documents/LivelyCura`.
- Affected repositories: `livelycura-backend`, `livelycura-pharmacy-portal`, and `livelycura-check-city-app`.
- Repository writes: none.
- Codex sessions processed: exactly 8, as fixed by the previous checkpoint.
- Transcript handling: only session metadata, short sanitized user statements, durable claims, corrections, and reported verification outcomes are preserved. Full transcripts and routine tool chatter are excluded.
- Secret-bearing files and values were not inspected or copied. Generated output, dependencies, build output, caches, binaries, and unrelated attachments were excluded.

## Processed Codex Sessions

| Date | Session ID | Working directory | Indexed title |
| --- | --- | --- | --- |
| 2026-06-14 | `019ec6f5-89f0-79f2-9dc7-25a94e6afe70` | `/Users/acazumah/Documents/LivelyCura` | Add lab requests to sales |
| 2026-06-12 | `019eb927-e9a8-70e1-b559-9b35bffb628b` | `/Users/acazumah/Documents/LivelyCura` | Review backend against PDF |
| 2026-06-07 | `019ea1d1-ae47-7340-8842-0ee5e5d83363` | `.../livelycura-pharmacy-portal` | Fix test builder renderer |
| 2026-06-05 | `019e9562-55d4-7830-868d-b7a8484cd26c` | `.../livelycura-pharmacy-portal` | Polish rendering engine UI |
| 2026-05-30 | `019e78b1-163a-70f0-b619-b4f90e4110f3` | `/Users/acazumah/Documents/LivelyCura` | Plan lab test definition rollout |
| 2026-05-29 | `019e7553-e228-76a2-b842-d69fa817be5c` | `/Users/acazumah/Documents/LivelyCura` | Add samples section |
| 2026-05-21 | `019e4af8-1012-79d3-b679-346a61c1dff6` | `.../livelycura-backend` | Add lab test builder |
| 2026-05-14 | `019e28e5-be8d-7912-be33-816f759c9db7` | `.../livelycura-check-city-app` | Add animations and theme toggle |

## Minimal Sanitized Conversation Evidence

- `019ec6f5…`: ordinary sale creation remains the transaction owner. A lab-linked sale line should create a test request inside that sale transaction without turning the general sale API into a lab-specific API or bypassing normal stock behavior. MLS domain names should be concise inside the MLS namespace (`Sample`, `TestDefinition`, `TestRequest`). The user explicitly rejected removing GraphQL, Shield, DataLoader, filters, or read/list services merely to narrow a change. Test-request status changes use a dedicated mutation. The general product-based POS is a standalone selling surface with its own shell, while the existing inventory-backed Sell page remains unchanged.
- `019eb927…`: an older architecture document proposed one clinical request containing many tests and one draft invoice, using the existing Customer as patient. At that time the backend had test catalogs but no request layer. This proposal was later superseded by the implemented one-request-per-lab-linked-sale-item model.
- `019ea1d1…`: the builder and renderer must cover the generated definition contract rather than silently dropping nested sample, material, workflow, result, rule, and report fields. The UI is for laboratory technicians, so JSON-shaped storage must be mediated by lab-language controls. Samples render names/codes rather than raw IDs. A later requested rebuild organized the form as a guided wizard while retaining generated GraphQL types as the backend boundary and compiling technician-friendly state into rule/report JSON.
- `019e9562…`: the rendering engine is reusable operational infrastructure, not a set of disabled form fields. Definition view has its own page/query and uses the same renderer. Create and edit own separate pages, hooks, forms, and mutations while sharing a prop-driven builder. Each table action owns its confirmation modal and each mutation owns its hook/file. Activation is a separate lifecycle mutation, not an alias for publish. Browser-visible verification was repeatedly required for UI work.
- `019e78b1…`: the test-definition rollout introduced a generic schema/runtime layer and an MLS-specific builder, with create, edit, detail, version, publish, duplicate, deactivate, archive, category, sample, workflow, result-schema, rule, report, and product-sync concerns. Product sync occurs after definition creation. Historical layout proposals changed several times; current code is authoritative for the surviving wizard/renderer arrangement.
- `019e7553…`: Samples follows established catalog table/modal/hook patterns and supports list, create, view, edit, activate/deactivate, archive, filters, column controls, permissions, and generated GraphQL types. The same session added full department management and made employee department optional: omit it on create, validate an active same-organization department when present, and allow clearing it on update.
- `019e4af8…`: test definitions are structured lab configuration, not a duplicate billing/inventory subsystem. Departments and Samples are first-class records referenced by ID. Existing product categories are reused and managed through dedicated add/remove services; synced product categories follow those changes. Product linkage belongs on TestDefinition/Product rather than a separate linking model. Publish and activate are distinct lifecycle actions; activation affects only the target definition. Employee department remains optional because not every organization uses departments.
- `019e28e5…`: CheckCity motion uses the existing Reanimated stack rather than adding 3D dependencies. Reusable primitives include restrained screen entry, depth press, and reduced-motion support. Theme changes animate only the background/decor from the theme-control origin, never a white/dark full-screen cover over content. Menu and Search headers align to the same constrained body width.

## Current-Code Verification

### LivelyCura Backend

- Current MLS models, services, GraphQL schema/resolvers, Shield rules, and DataLoaders use `Sample`, `TestDefinition`, `TestDefinitionVersion`, `TestRequest`, and `TestResult` naming inside the MLS namespace.
- `createSaleInSession` creates sale items, then calls `createTestRequestForSale` with the same MongoDB session before inventory movements, COGS, and invoice finalization. Lab-linked products therefore retain the normal sale/stock path.
- `createTestRequestForSale` creates at most one request per qualifying `SaleItem`, requires a customer/patient, rejects quantities above one per test line, pins the active definition/version, uses the first workflow step, and is idempotent through the unique sparse `saleItemId` relation.
- Test-request status is handled by `updateTestRequestStatus`; GraphQL Shield protects the dedicated mutation with `testRequests.update`.
- Test definitions reuse product categories through `addTestDefinitionCategory` and `removeTestDefinitionCategory`, and propagate changes to an already linked product. The model owns `categoryIds` and `linkedProductId`; no separate definition-product linking model is present.
- `publishTestDefinition`, `activateTestDefinition`, and `deactivateTestDefinition` are separate services/mutations. Activation currently changes only the selected definition to active; it does not publish, snapshot, or alter sibling definitions.
- TestDefinition and Sample persistence use the archive metadata convention `archived`, `archivedAt`, `archivedBy`, and `archivedReason` alongside status and soft deletion.
- Employee department is optional. Create/update resolve only active departments in the same organization when a value is supplied, and update can clear the relation.

### LivelyCura Pharmacy Portal

- MLS currently has separate list, create, edit, and detail feature folders. Create and edit own their queries/forms/mutations; `src/mls/builder` owns shared builder components and mapping; `src/rendererEngine` owns reusable schema evaluation and definition/result/report/workflow rendering.
- The current shared builder is a guided `TestDefinitionWizard`. It compiles technician-facing result checks, interpretation rules, and report layout into backend-compatible inputs and passes the same structures to live review rendering.
- Definition detail has its own query/page and renders through `DefinitionRenderer`. Sample requirements pass sample names/codes rather than only IDs.
- Test-definition lifecycle actions have separate mutation hooks and separate confirmation modals. Activation/deactivation share one conditional menu position but invoke distinct actions.
- Samples is an MLS-owned table feature with create, view, edit, status/archive actions, permissions, pagination/filters, and column visibility controls.
- The POS terminal is mounted outside `MainLayout` under `PosLayout`; its header provides back navigation, organization/facility context, the established theme selector, fullscreen, and profile actions. The route remains a general product-based selling surface.

### LivelyCura CheckCity App

- `src/motion` exports `DepthPressable`, `AnimatedScreenEnter`, and `useReducedMotion`; shared motion honors the platform reduce-motion preference.
- Theme preference updates immediately while `BackgroundDecoration` performs a 950 ms circular reveal of the new decor behind content from the supplied origin. No full-screen foreground theme sheet is present.
- Menu/branch and Search header containers are centered, capped at 1024 px, and use the same theme spacing as their body boundaries.

## Reported Historical Verification

- Backend sessions reported successful TypeScript/build checks for the request, department, test-definition, and lifecycle work; focused lifecycle/department tests were also reported where added.
- Pharmacy Portal sessions reported successful GraphQL generation, type checks, focused renderer/schema tests, broader Vitest runs, lint/format checks, and live browser checks for POS, MLS definitions/requests, Samples, and Departments.
- CheckCity reported successful `yarn type-check` and `yarn format:check` after the motion, theme-transition, and header-width corrections.
- These are transcript-reported outcomes from May–June 2026. The harvest itself performed read-only source inspection and did not rerun repository test suites.

## Contradictions And Uncertainty

- The PDF-era parent-request/many-tests/one-draft-invoice proposal conflicts with the later explicit sale integration and current code. Current implementation is one `TestRequest` per lab-linked `SaleItem`, all within the ordinary sale transaction.
- Builder layout direction changed from tabs, to steppers, to one-page sections/accordions, and later to a guided wizard rebuild. Current `TestDefinitionWizard` plus current detail renderer define implementation reality; the durable principle is technician-facing guidance and shared rendering, not any historical intermediate layout.
- Some transcript symbols used `Lab*` prefixes and older names such as `resultSchema`; current backend and portal use the newer MLS-scoped names and current generated contracts.
- Historical verification includes periods when codegen depended on a running localhost GraphQL server and could not run. Current generated output was excluded from this harvest, so only source ownership—not generated-file freshness—is asserted.
- Test-definition action enablement changed during review. Current code is authoritative; the stable rule is that lifecycle actions are explicit, permissioned, and confirmed rather than silently overloading another mutation.

## Follow-Up Boundary

The next bounded batch remains LivelyCura and should process exactly these eight indexed sessions:

1. `019edbb8-c050-7422-acd5-5d6423e29599` — Update iOS mockups with screenshots.
2. `019edb14-5a4c-7203-b874-732d0046b020` — Update iOS screens.
3. `019e88a0-484c-7ea1-998a-92fd115116db` — Delete seed data except orgs.
4. `019e191c-5c93-7970-98a5-97ad9fe7bf05` — Update iOS screens and logos.
5. `019e02a9-1c7a-76b2-b722-61d9fe53fda3` — Add dynamic app banners.
6. `019e0007-1015-7c22-875e-dae188fa0ccb` — Add live activity support.
7. `019dffe9-809c-7051-8e17-accb646dcdf6` — Fix ExpoInAppUpdates crash.
8. `019dfea2-359d-7182-91d6-be1d54e0dd3c` — Stretch active bottom tab.

After that batch, continue the remaining indexed LivelyCura sessions, then triage unindexed sessions for unique evidence before moving to CompFlow.
