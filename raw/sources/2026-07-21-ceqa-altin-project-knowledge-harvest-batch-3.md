# C.E.Q.A/Altin Project Knowledge Harvest — Batch 3 Evidence Manifest

Date: 2026-07-21

## Scope

- Family: C.E.Q.A/Altin.
- Repository boundary: `/Users/acazumah/Documents/C.E.Q.A` plus historical working directories under `/Users/acazumah/Documents/Pizzaman` for Keks Admin Portal and Call Center Web App.
- Repository writes: none.
- Repositories rechecked: exactly 3.
- Historical Codex records processed or classified: exactly 5, the checkpointed final family batch.
- Direct current/legacy working-directory records discovered: 21.
- Records processed after this batch: 21.
- Records remaining after this batch: 0.
- Full transcripts, uploaded screenshots/videos, generated GraphQL files, dependency trees, environment files, credentials, tokens, private identifiers, request payload values, and provider values were not copied into the vault.
- Hermes history was searched separately. No direct C.E.Q.A/Altin Hermes implementation session was found; one CompFlow scaffolding session was excluded from this family and checkpointed as a separate bounded supplement.

## Repository Provenance

| Repository | Branch | Base commit | Recheck state |
| --- | --- | --- | --- |
| `/Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile` | `main` | `f05077b67018` | clean; no batch-3 record targeted this repository |
| `/Users/acazumah/Documents/C.E.Q.A/keks-admin-portal` | `develop` | `3521aaadf7ba` | clean |
| `/Users/acazumah/Documents/C.E.Q.A/call-center-web-app` | `develop` | `6a9cff6b681f` | clean |

All three repositories were inspected read-only. No dependency installation, generation, tests, builds, services, browser sessions, API calls, commits, pushes, migrations, deployments, or Git mutations were run.

## Session Provenance

| Session ID | Date | Historical working directory | Indexed title | Classification |
| --- | --- | --- | --- | --- |
| `019e17fc-ab90-7390-8ae8-bc670a4738fb` | 2026-05-11 | `/Users/acazumah/Documents/Pizzaman/keks-admin-portal` | Fix launchpad greeting | substantive launchpad accessibility/test maintenance; completed |
| `019e087e-8415-7fb0-b296-bf7897049dbf` | 2026-05-08 | `/Users/acazumah/Documents/Pizzaman/keks-admin-portal` | Add post-login home tabs | substantive multi-task launchpad/theme/employee-UI record; completed after repeated visual corrections |
| `019de9d4-d4fa-7a70-8e07-0358896f1d03` | 2026-05-02 | `/Users/acazumah/Documents/Pizzaman/call-center-web-app` | Allow branch changes anytime | substantive branch/order-search/delivery-state record; completed |
| `019dda2a-5872-7f83-b151-a4a0163a1e42` | 2026-04-29 | `/Users/acazumah/Documents/Pizzaman/call-center-web-app` | Add location search guide | substantive multi-day location/delivery integration record; completed after multiple corrections |
| `019caebd-b7ec-7e60-a01f-8fd02bec2e52` | 2026-03-02 | `/Users/acazumah/Documents/Pizzaman/call-center-web-app` | Add missing fields to threshold disc | substantive threshold-discount record; completed after pricing correction |

## Minimal Sanitized Session Evidence

### Keks Protected Launchpad

- The authenticated root route is a launchpad outside the full `MainLayout`; selecting a module enters the normal sidebar/header application.
- Show real routable modules rather than placeholder cards. Current source also filters protected cards by the user’s permissions and opens the existing tenant switch when authenticated credentials are missing.
- Screenshots and recordings supplied visual direction. The user repeatedly corrected animation speed, clipping, color intensity, dark-mode consistency, sidebar placement, and responsive treatment rather than authorizing a foreign design system.
- Launchpad entrance and greeting motion must remain smooth, readable, and disabled or made static for `prefers-reduced-motion`.
- Theme preference is one shared System/Dark/Light contract. Controls use clear labels and `aria-pressed`; launchpad, dashboard, and main layout should render the same selected preference rather than maintain independent theme state.
- A component styled as a Chakra hover group must retain its native button role. `role="group"` on the launchpad card was rejected because it removed accessible button semantics; the historical fix restored the button role and added an accessible action label.
- Employee-detail UI keeps its page header unchanged, preserves responsive hero sizing/alignment, and moves the reusable fact component and its props into the feature’s component/interface ownership.
- Historical verification reported focused 12/12 launchpad tests for the accessibility repair and test/build passes at other endpoints. These are session outcomes, not fresh batch-3 runs.

### Call-Center Branch And Order Behavior

- Agents may change or clear the selected branch while the cart contains items; an accidental suggested-branch choice must not force cart clearing.
- Branch changes recompute every cart line from the selected branch’s prices. Changing or clearing an existing branch also invalidates address, exact location, delivery fee, Altin estimate, vehicle selection, and cart-level delivery fee so dependent values are recalculated.
- Call-center and app-order lists support MoMo-number search and display a MoMo-number column; an absent value renders as a dash.
- Before a branch is selected, exact-location delivery displays a neutral zero rather than a post-checkout/unavailable estimate message. Estimate feedback belongs after both location and branch establish a calculable request.

### Call-Center Location And Delivery

- Branch selection is disabled only while the cart is empty.
- Delivery has two mutually exclusive input paths: exact searched/pinned location or the existing delivery-area fee picker. The UI presents one delivery concept and disables the other path when one is active.
- Address and coordinates are one location contract. Suggestion selection resolves coordinates and updates search text, marker, and map center; pin selection reverse-geocodes and updates both search inputs. Failed or stale requests preserve the previous valid location.
- Location actions belong in a hook, while interfaces live in the feature’s interface folder and repeated suggestion rendering lives in its own component.
- Exact-location changes unlock and clear the old branch, request the closest branches from current coordinates, and allow reselection without clearing cart items.
- Altin estimate results are parsed from the API payload, converted to lower currency units, displayed in Delivery, and included in Total. Manual delivery-area fees remain a fallback path and also contribute to Total.
- User-stated import rule: configure TypeScript and Vite alias resolution together; use absolute imports across top-level feature/root folders and relative imports within the same feature/root folder.
- The supplied guide said the Altin estimate mutation allowed only a customer role while call-center order creation used staff roles. Current source still requires and requests a client-side Altin estimate for exact-location checkout, so backend authorization compatibility remains unverified.
- Historical verification reported builds and browser checks at several corrected endpoints. These were not rerun during this harvest.

### Call-Center Threshold Discounts

- Adding GraphQL fields alone was not feature completion; pricing behavior, cart state, display, and checkout flow also had to consume the threshold contract.
- `thresholdAmount` is only the eligibility check against the line total. The deduction uses `discountValue`: a fixed amount for fixed mode or a percentage calculation for percentage mode.
- A backend/default `discountedPrice` of zero must not replace a valid base price. Current code accepts a branch discounted price only when positive and no greater than the base price, otherwise tries a positive percentage discount and finally falls back to the base price.
- Applied unit price is clamped non-negative, threshold discount snapshots are stored on cart lines, and branch/quantity changes recalculate pricing.
- Historical final verification reported a passing TypeScript no-emit check; this is provenance, not a current run.

## Current Repository Reconciliation

### Altin Partner Mobile

- `AppModuleScreen`, `AppFeatureScreen`, and `useAppModule` remain tracked, but current source-wide reference checks found no active route or barrel consumer. They are legacy/inactive machinery rather than the current runtime owner of module behavior.
- The generic README conflicts with the repository not only on Expo Router and the `app/` directory, but also on npm usage and a nonexistent reset script. Current `AGENTS.md`, Yarn lockfile, scripts, and React Navigation tree remain authoritative.
- Dynamic and static Expo configuration still disagree on some assets; the effective dynamic configuration should be treated as current until the files are consolidated.

### Keks Admin Portal

- `/` remains protected and renders `Launchpad` outside `MainLayout`; system pages remain under the authenticated layout.
- Launchpad cards are permission-filtered, are real buttons with accessible labels, and use responsive grid, hover/focus, tenant-switch, theme, and entrance/greeting behavior.
- Launchpad CSS retains a slow red/muted text sweep, entrance motion, unclipped text treatment, and reduced-motion overrides.
- `ThemeModeControl` is shared across launchpad/auth/main-layout surfaces and exposes System, Dark, and Light buttons with `aria-pressed`.
- `EmployeeHero`, `HeroFact`, and their interfaces remain separate; the responsive hero treatment requested in the final correction is current.
- Current launchpad constants still include Announcements, while the Announcements route is commented out. This conflicts with the “only implemented routable modules” rule.
- Current tracked repository evidence contains CI build/test workflows but no Netlify, Vercel, Docker, Procfile, or other deployment configuration. Earlier deployment-destination claims are therefore unverified external knowledge, not current repository facts.

### Call Center Web App

- Cart branch selection is available whenever the cart is nonempty. `setCartBranch` recomputes every line’s branch and threshold pricing; changing or clearing an existing branch resets dependent fulfillment/estimate state.
- Current order filters and table queries/items include MoMo-number search/display and render missing values as `-`.
- Delivery-area and exact-location flows remain mutually exclusive. Location changes clear/unlock branch selection and expose up to three closest-branch choices.
- `LocationSearchInput`, `LocationSuggestionsList`, `LocationMap`, and `useLocationSearchActions` preserve the search↔map synchronization and stale-request rollback behavior.
- `CartTotals` adds the current Altin or ordinary exact-location estimate to Total, uses manual delivery-area fees when no exact location is active, and displays zero for exact location before branch selection.
- `calculateCartItemPricing` implements the verified threshold eligibility/deduction distinction and rejects invalid zero discounted prices.
- Vite and TypeScript alias resolution are configured, but current same-feature imports mix relative paths with `src/cart/...` absolute paths. This conflicts with the explicit boundary-based import rule.
- Current exact-location Altin checkout requires an estimate ID and calls the estimate mutation. The historical CU-only role note is not resolved by current frontend source.
- A current tracked `eslint.config.js` supplies the flat ESLint configuration. The earlier “lint blocked because config is absent” claim is superseded, although lint itself was not run during this read-only harvest.

## Hermes Reconciliation Supplement

- Direct Hermes-history searches for Altin Partner Mobile, Keks Admin Portal, Call Center Web App, and their batch-specific domain terms found no additional C.E.Q.A implementation session to promote.
- Hermes session `20260710_173537_54b264` is a substantive CompFlow scaffolding record. It created and verified separate promotional-web, admin, and backend applications after the user corrected an accidental root-monorepo direction.
- That session is not C.E.Q.A evidence and is not processed in this batch. It is recorded in the checkpoint as the next one-session CompFlow supplement so Portfolio is not started before this known gap is reconciled.

## Promoted Knowledge Boundary

- Keks and Call Center project pages receive current implementation, explicit conventions, historical outcomes, and current-versus-historical contradictions.
- The Software Development Operating Manual receives only reusable rules about accessible interactive semantics, shared theme/motion contracts, alias boundaries, dependent-state invalidation, and pricing eligibility versus deduction.
- The New Project Bootstrap Operating Manual receives only reusable alias-resolution, import-boundary, accessible theme-control, and reduced-motion foundations.
- Altin Partner Mobile receives only repository-derived current-state corrections; none of the five Codex records targeted it and no session-derived Altin claim is added.

## Completion Boundary

- C.E.Q.A/Altin batch 3 processes exactly five records.
- All 21 discovered direct current/legacy working-directory records are now classified.
- C.E.Q.A/Altin historical coverage is complete for the discovered set as of 2026-07-21.
- Portfolio remains the next unprocessed family in the original procedure order.
- The immediate checkpoint is instead one bounded CompFlow Hermes supplement for session `20260710_173537_54b264`; after that reconciliation, resume Portfolio batch 1.
