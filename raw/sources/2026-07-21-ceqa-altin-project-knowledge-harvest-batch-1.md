# C.E.Q.A/Altin Project Knowledge Harvest — Batch 1 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: C.E.Q.A/Altin.
- Repository boundary: `/Users/acazumah/Documents/C.E.Q.A` plus historical working directories under `/Users/acazumah/Documents/Pizzaman` for the same Keks and call-center repositories.
- Repository writes: none.
- Repositories inventoried: exactly 3.
- Historical Codex records processed or classified: exactly 8, the most recent direct working-directory matches.
- Direct current/legacy working-directory records discovered: 21.
- Records remaining after this batch: 13.
- Full transcripts, generated GraphQL files, binaries, dependency trees, environment files, credentials, tokens, private identifiers, and provider values were not copied into the vault.

## Repository Provenance

| Repository | Purpose observed from current source | Branch | Base commit | Inspection state |
| --- | --- | --- | --- | --- |
| `/Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile` | Expo partner operations scaffold with authentication, navigation, module directory, and placeholder operational modules | `main` | `f05077b67018` | clean |
| `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | Keks workforce administration, permissions, reports, and integration settings | `develop` | `3521aaadf7ba` | clean |
| `/Users/acazumah/Documents/C.E.Q.A/call-center-web-app` | Call-center selling, cart/checkout, order management, and operational reporting | `develop` | `6a9cff6b681f` | clean |

All three repositories were inspected read-only. No dependency installation, generation, tests, builds, services, API calls, migrations, deployments, or Git mutations were run.

## Session Provenance

| Session ID | Date | Historical working directory | Indexed or descriptive title | Classification |
| --- | --- | --- | --- | --- |
| `019f591c-6c7e-71d1-97ef-a9106eea3397` | 2026-07-13 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | Add Designations API | substantive; completed |
| `019ee1a9-7cd2-7d90-a4fb-b8c25b09f2ef` | 2026-06-19 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | Fix Chakra Select error | substantive but interrupted; current fix verified statically |
| `019ecd35-0464-7ab0-9e64-f30a23af157c` | 2026-06-15 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | API-key management and permission synchronization | substantive; completed |
| `019ecd33-ffcc-76c1-ac22-bf74103288c3` | 2026-06-15 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | image-only duplicate shell | duplicate/aborted; no independent project claim |
| `019eb952-2c35-7771-9f62-2002147d7523` | 2026-06-12 | `/Users/acazumah/Documents/C.E.Q.A/call-center-web-app` | Fix duplicate checkout orders | substantive; completed |
| `019e6f57-af39-74d0-8386-cd0434ad8830` | 2026-05-28 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | Wire search params to tables | substantive; completed |
| `019e6eca-0fe9-73d1-93b4-9389ddfc2784` | 2026-05-28 | `/Users/acazumah/Documents/C.E.Q.A/call-center-web-app` | Fix checkout address validation | substantive; completed after follow-up correction |
| `019e6b33-73e7-7890-aad5-e482daa302eb` | 2026-05-27 | `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | API search-field rollout precursor | repeatedly interrupted precursor; later session/current code establish the outcome |

## Minimal Sanitized Session Evidence

### Keks Designations

- User-stated correction: this was an additive admin-portal feature, not permission to redesign existing interfaces.
- User-stated correction: Roles and Designations must live in separate folders rather than one combined module.
- Historical outcome: separate `src/hrm/roles` and `src/hrm/designations` ownership with their own components, hooks, interfaces, helpers, bulk imports, and exports; build, lint, 33 tests, and diff validation were reported passing.
- Current verification: the folders remain separate; Designations owns server search, create/update permission wrappers, bulk import, and its own route.

### Keks Permission And Integration Settings

- API-key management is permission-gated, cursor-paginated, and supports create, one-time secret reveal/copy, and revoke.
- The token-exchange toggle is separately permission-gated.
- The user explicitly rejected a staging-only code comment; permissions should remain ordinary first-class constants and begin working against production when the backend exposes them there.
- Permission checks cover route loaders and visible navigation/actions, with a `super_admin` bypass and reusable any/all helpers.
- Historical outcome: 29 tests, build, and an in-app browser settings check were reported passing. These are historical results, not a fresh validation of the current clean tree.
- Current verification: constants, route loaders, navigation metadata, API-key UI, tests, and super-admin/any/all helpers remain present.

### Keks API Search And Chakra Selects

- API-backed filters should pass supported `search` parameters rather than only filtering already-fetched rows.
- Shared selectors must expose loading, empty, and error states and must adapt Chakra Select detail events to the scalar filter value owned by the application.
- Current verification: many filter hooks synchronize search with URL/query parameters; API-backed dropdowns receive remote search and feedback states; report-log status options are a Chakra `createListCollection` and the event adapter extracts the first selected value.
- The May 27 precursor and June 19 error task ended interrupted. Their implementation claims are promoted only where current source confirms them.

### Call-Center Checkout Idempotency

- A duplicate order caused by retry, unstable internet, or rapid clicks must not be solved only by disabling the button.
- The frontend keeps one idempotency key for the same order payload, including gift recipients, reuses it for retries, rotates it when relevant inputs change or checkout completes, and prevents avoidable concurrent submissions.
- Historical focused tests and build passed. The historical full nine-test run executed successfully but exited nonzero because an existing app test emitted unhandled router/network errors; lint was blocked by absent ESLint flat configuration.
- Current verification: fingerprinted key reuse/rotation and the in-flight ref guard remain in `useCheckoutOrder`.

### Call-Center Exact Location

- The selected or typed human-readable address and captured coordinates must stay synchronized; coordinates alone are insufficient for checkout validation.
- The identified bug was ordering: selecting a location wrote the address before a location/branch reset cleared it. The corrected flow commits location/reset effects first and writes the selected address last.
- User-stated constraint: preserve the current backend-compatible latitude/longitude mapping; do not “correct” it as part of the address fix.
- Historical focused tests and build passed. Current source retains the location-first/address-last sequence and focused tests.

## Current Repository Evidence

### Altin Partner Mobile

- Yarn/Expo 54/React Native 0.81/React 19/TypeScript application with `expo/AppEntry.js`, React Navigation, Apollo Client, Redux Toolkit/Persist, AsyncStorage, Styled Components, safe-area handling, and OAuth/OIDC Authorization Code with PKCE.
- Root composition is Redux → theme → Apollo → gesture root → navigation. Authentication chooses Login or the authenticated stack; authenticated bottom tabs are Home, Search, Apps, Notifications, and More.
- Apollo attaches the valid bearer token and a public application identifier to the configured GraphQL endpoint.
- The current app is still mostly an operational scaffold: Home and many feature screens are placeholders. Orders, Outlets, Fleet, Team, Accounting, and Billing have module roots/drawers and registered feature routes.
- Current source still contains centralized `AppModuleScreen`, `AppFeatureScreen`, and module-directory resolver machinery even though the durable correction says each module should own its root, drawer, sections, and concrete screens.
- The generic create-expo-app README incorrectly describes Expo Router and an `app/` directory. The repository instructions and live entry point explicitly require React Navigation under `src/navigation`.
- No test script, production build script, CI workflow, or EAS configuration was found. Runtime config is split between `app.config.ts` and `app.json`; current source/config documentation also use inconsistent API environment names.

### Keks Admin Portal

- Yarn/Vite 7/React 19/TypeScript portal using Chakra UI 3, React Router 7, Redux Persist, TanStack Query/Table, Formik/Yup, Vitest, and PDF/CSV/report tooling.
- Provider composition is Redux → Query → System → Chakra → Router. Axios uses a configured base URL, bearer-token request interception, filtered query serialization, and reset-on-401 behavior.
- Major domains include authentication, launchpad/dashboard, employees, departments, roles, designations, branches, transfers, shifts, check-ins, absences, overtime, reminders, reports, notifications, settings, API keys, and webhooks.
- Roles and Designations are separate domain modules. Search state is commonly URL-backed/debounced and passed into APIs; selector feedback is shared.
- Permission enforcement exists at route, navigation, launchpad, and action levels, with `super_admin` bypass. API-key creation uses Formik and preserves a one-time reveal state until explicit close.
- GitHub Actions use Node 22 and Yarn frozen-lockfile installs, then build and tests. Develop deploys to staging Netlify and main deploys to production Netlify using external environment/secret references; no values were inspected or stored.
- The README is still the generic Vite template. Some current routes remain unguarded or disabled/commented despite the wider permission model, so “permission sync” is not evidence that every possible surface is protected.

### Call-Center Web App

- Yarn/Vite 7/React 19/TypeScript operations app using Mantine 7 plus Styled Components, React Router 7, Redux Persist, TanStack Query, GraphQL HTTP/subscriptions/codegen, Formik/Yup, Vitest, and Google Maps/location tooling.
- Provider composition includes Redux persistence, Query, subscriptions, system/auth loading, Mantine, Styled Components, and router.
- Main routes cover dashboard, sales/cart checkout, call-center orders, app orders, and both order-detail surfaces.
- Current checkout implements availability checks, Altin courier estimates, exact-location or delivery-area fulfillment, gift recipients, payment confirmation subscription, and stable idempotency.
- Current location selection commits coordinates before the address, preserves existing coordinate transport behavior, and invalidates/refreshes dependent estimate state through the existing form flow.
- GitHub Actions use Node 22, Yarn frozen-lockfile install, build, and tests. No deployment workflow was found.
- GraphQL Codegen points at a live staging schema and writes generated contracts with `@ts-nocheck`; the generic Vite README does not document the actual application. The lint script still has no repository ESLint flat config.

## Promotion Decisions

- Create three repository-scoped project pages.
- Add a compact C.E.Q.A/Altin family map and only supported reusable rules to the Software Development Operating Manual.
- Update the New Project Bootstrap Operating Manual only if the repository/session evidence adds a reusable rule not already captured; project-specific UI, permission names, colors, and checkout exceptions remain in project pages.
- Preserve current-versus-desired Altin module ownership, Keks permission coverage, and call-center validation/tooling gaps as contradictions.

## Completion Boundary

- C.E.Q.A/Altin batch 1 processes exactly eight records.
- Thirteen older direct current/legacy working-directory records remain pending for C.E.Q.A/Altin batch 2.
- Batch 2 should process the next eight older records, from `019e64df-8e38-7ef3-ad28-96a779d99465` through `019e266b-c22a-7380-9aec-18cd6bd77841`, leaving the five oldest for a later batch.
