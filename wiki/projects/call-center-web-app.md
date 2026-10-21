---
type: project
status: active
created: 2026-07-21
updated: 2026-10-09
tags: [project, ceqa, call-center, checkout, orders, react]
sources:
  - ../sources/call-center-customer-detail-navigation-correction.md
  - ../sources/call-center-customer-ui-consistency-correction.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-1.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-2.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-3.md
  - ../sources/ceqa-call-center-hermes-supplement-2.md
  - ../sources/call-center-product-category-filter-contract.md
  - ../sources/call-center-product-grid-container-responsiveness.md
  - ../sources/call-center-wider-search-hook-and-action-correction.md
confidence: high
---

# Call Center Web App

## Summary

Call Center Web App is an operational sales and order-management frontend. Agents select products, build carts, resolve branches and delivery location, create call-center orders, await payment where required, and inspect both call-center and app-originated orders.

## Purpose

Give call-center agents a resilient assisted-ordering surface that integrates catalog, availability, delivery, payment, and order tracking without duplicating customer orders during retries.

## Stack

- Yarn, Vite 7, React 19, and TypeScript 5.8.
- Mantine 7 plus Styled Components.
- React Router 7.
- Redux Toolkit/Redux Persist.
- TanStack Query.
- GraphQL HTTP, request/client hooks, WebSocket subscriptions, and GraphQL Codegen.
- Formik/Yup, Google Maps/location tooling, Recharts, Vitest, and Testing Library.
- ESLint with a tracked flat configuration, Husky, Commitlint, and Commitizen.

## Architecture

- Root providers compose persisted Redux, Query, subscriptions, tenant-aware Mantine theming, system/auth initialization, Styled Components, and routing.
- Protected routes cover Dashboard, Sales, Orders, order details, customer search, and customer details; login uses a separate auth layout.
- The self-scoped `getCurrentCallCenterAgent` query owns live agent identity, active tenant, resolved memberships, switchability, logo, and brand colors. Suspended-brand sessions are held at a required brand switcher before operational routes mount.
- `switchActiveTenant` keeps the existing JWT, then refreshes the self-read, resets cart/order-filter state, purges brand-scoped TanStack Query data, and remounts the authenticated layout under the new tenant scope.
- Product/context hooks own catalog selection, family dimensions, per-variant preferences, and recommendation flows.
- Cart hooks own branch, delivery area/exact location, availability, courier-specific pricing/Altin estimates, gift recipients, checkout, and payment-confirmation state.
- Location search, suggestions, map interaction, reverse geocoding, closest-branch discovery, and delivery pricing cooperate through the cart's fulfillment state rather than maintaining independent address/coordinate copies.
- Orders and order-detail modules separate call-center orders from app-originated orders.
- GraphQL operations use a mixture of generated contracts and focused fetch-based hooks.
- Shared storefront catalog reads pass the active tenant key/id explicitly; token-scoped order and history reads continue deriving brand scope from the server session.

## Folder Ownership

- `src/authentication`, `src/redux/auth`, `src/providers/system`: login/logout, persisted authentication, session-security behavior, and current-user/system initialization.
- `src/hooks/useActiveTenant.ts`: shared application-level active-tenant access used across layouts, theming, catalog, branch, and cart surfaces.
- `src/helpers/tenant.ts`: shared active-tenant derivation, membership reconciliation, suspension, color, and switch-availability helpers.
- `src/switcher/brand`: brand-switcher-owned `components`, `hooks`, `interfaces`, and tests; `useSwitchActiveTenant` belongs here rather than under authentication.
- `src/profile`: the protected user-facing Profile page with separate `components` and `interfaces`; the Profile entry composes those parts from established application state and does not own authentication mechanics.
- `src/products`: product querying, selection, variants/preferences, recommendations, and branch context.
- `src/cart`: cart UI, exact location/delivery areas, availability, estimates, gifts, payment, and checkout orchestration.
- `src/cart/interface`: cart-owned contracts for location, delivery, pricing, checkout, and component boundaries.
- `src/orders`, `src/order`: order lists, filters, details, timelines, fulfillment, payment, and print views.
- `src/customers`, `src/customer`: phone-driven customer search and standalone customer details respectively. Each owns its screen, components, query hooks, interfaces and styles; shared private-request lifecycle primitives live under `src/hooks`.
- `src/dashboard`: sales/order metrics and date filters.
- `src/chat`: call-centre support-chat queue, conversation UI, staff notifications, attachments, order links, GraphQL request hooks, access helpers, and focused tests. The feature root orchestrates hooks while typed presentation components live under `components`.
- `src/notifications/firebaseMessaging.ts` and `public/firebase-messaging-sw.js`: optional browser FCM registration and background push routing; sign-in remains usable when messaging is unconfigured or denied.
- `src/router`, `src/layouts`: route protection and authenticated/order layouts.
- `src/interfaces/graphql`: generated GraphQL contracts; generated files are evidence only, not manually edited knowledge sources.

## Commands

- `yarn dev`: Vite development server.
- `yarn build`: TypeScript then Vite build.
- `yarn generate`: GraphQL Codegen against the configured schema.
- `yarn test`: Vitest.
- `yarn lint` / `yarn lint:fix`: ESLint through the tracked flat configuration.
- `yarn preview`: preview the production build.
- `yarn commit`: Commitizen.

## Runtime/Deployment

- The app consumes configured API and GraphQL endpoints and attaches the persisted bearer token.
- GraphQL subscriptions support payment confirmation and other live behavior.
- Google Maps/location behavior requires a public browser API key; values are not stored in the vault.
- GitHub Actions use Node 22, Yarn frozen-lockfile installation, build, and tests for `develop` pushes and `main` pull requests.
- No deployment workflow was found.

## Durable Conventions

- Match existing record navigation and file ownership, not only appearance. Customer search and detail use separate sibling routes and plural/singular feature folders, following `orders`/`order`. Do not mount a selected customer beneath the search UI. Preserve the accepted customer styling and provide back navigation that also works for direct links, loading and errors. See [[../sources/call-center-customer-detail-navigation-correction|Call Center Customer Detail Navigation Correction]].
- Tenant theming currently uses `colorsTuple(primaryColor)`, so `brand.0` is not a reliable light tint. A brand-colored amount needs a contrasting surface, such as the semantic translucent `brand-light`; verify financial totals under both themes.

- Match new feature UI to the existing call-center pages. Before implementation, inspect rendered Orders, Sales and Dashboard views; compare fluid width, panel containment, header/search treatments, typography, spacing, tables and mobile behavior. Verify inside the real application shell and theme rather than relying on an isolated component preview. This workflow follows the user's explicit rejection in [[../sources/call-center-customer-ui-consistency-correction|Call Center Customer UI Consistency Correction]].

- Support chat is brand-wide and separate from branch sales/order chat. Call-centre agents operate only on server-authorized `SUPPORT` conversations; the UI must drive claim, reply, and disabled feedback from `canClaim`, `canReply`, and `accessReason` rather than recreating access rules.
- `/chats` owns the shared unclaimed pool and current-agent assignments; `/chats/:conversationId` is the deep-linkable conversation route. Poll queue state every 15–30 seconds and staff notifications every 30 seconds, but subscribe to `chatNewMessage(channelId)` only while a conversation is open.
- `getChatConversation` is most-recent-first. Normalize it to chronological display, deduplicate live messages, and render `role: "event"` as centered state text rather than a participant bubble.
- Queue assignment is sufficient to reply, but an unassigned pool item must be claimed first. Display `originKind`, branch/order context, and `rotationCount` because they explain escalation origin and urgency.
- Upload chat files to `/chat-attachment` before sending their attachment IDs through `replyToChat`. Preserve uploaded IDs across a failed send; allow attachment-only messages; enforce JPEG/PNG/WebP/PDF, 10 MB per file, and five files per message before upload; reject HEIC/HEIF with conversion guidance.
- Agent login supplies the browser FCM token as `aDeviceToken` when Firebase public configuration and permission are available. Logout sends the stored token before clearing it. Push configuration is optional and must never block the in-app polled queue or notification center.
- Checkout idempotency is tied to a stable fingerprint of branch, cart, form values, and gift recipients.
- Reuse the same key for retries/double-clicks of the same payload; rotate it when relevant input changes or a checkout finishes.
- Keep an in-flight guard to avoid unnecessary concurrent submits, but do not treat button disabling as the idempotency guarantee.
- Keep Formik/Yup `form.isValid` authoritative for checkout field validity. Do not duplicate the schema with ad hoc field-presence checks in the cart component.
- Exact-location checkout requires both human-readable address and coordinates/fulfillment state.
- When location changes can reset branch/form state, commit reset-producing coordinate changes before writing the selected address.
- A map pin is not a valid exact location until reverse geocoding succeeds; commit the location and address together only after a non-empty address is available.
- Preserve the current backend-compatible latitude/longitude transport until the backend contract is deliberately changed and tested.
- Exact-location pricing follows branch courier type: Altin courier branches use the Altin cart estimate; other courier types use the ordinary delivery-price query.
- Keep delivery-area selection visible and disable incompatible controls with tooltip feedback. Exact-location search is an explicit toggle, not a hidden replacement for the delivery-area picker.
- Product queries live in hooks. Keep product-selection helpers, interfaces, list/picker components, and option items in their feature-owned files rather than one large modal component.
- For product catalog category filtering, send exact category document IDs through `GetAllProductsInput.categoryIds`; use slug paths such as `["beef"]` in `categoryPaths` when a root-category control must include products assigned to descendants. Never send document IDs through `categoryPaths`.
- The Sales product grid is owned by a resizable panel, so its responsive columns must use the grid container width rather than the viewport. Preserve the requested `base: 1`, `sm: 3`, `md: 3`, `lg: 4`, and `xl: 5` progression; list mode remains one column.
- Conditional wrappers do not defer evaluation of JSX children. Derive optional values safely before rendering rather than placing unsafe property access inside a false conditional.
- `familyConfig` describes ordered variant dimensions; preferences are annotations on the selected variant. Resolve one concrete variant, enforce required preferences, and preserve preference snapshots on the cart line and checkout input.
- The refreshed copy of the exact opened catalog product owns the picker mode and price. Products with non-empty `preferences` bypass family-dimension options even when their payload also contains `familyConfig`; render those preferences directly against the opened product and preserve its own price. Only products without preferences may enter the family-option flow. Expand variants with the product's dynamic `exactFamily`, never the fuzzy `family` filter, because similarly named normal, `PLUS`, and `ASSORTED` families otherwise contaminate one another. Merge refreshed and already-loaded variants by product ID and keep the merged array referentially stable while its inputs are unchanged.
- Catalog products and merchandising metadata change frequently. Production behavior must never branch on known product IDs, names, family names, prices, dimension labels, preference keys, or option labels. Derive picker mode, dimensions, options, preferences, required state, and price entirely from the current API payload; concrete product values belong only in regression fixtures.
- Branches may be changed or cleared while a cart has items. Every branch change reprices all lines against that branch and invalidates dependent address, coordinates, delivery fee, Altin estimate, and vehicle-category state before the new branch is accepted.
- Delivery area and exact location are mutually exclusive fulfillment modes. Keep the branch selector disabled only when the cart is empty; mode-specific controls own their prerequisites and feedback.
- Suggestion selection resolves coordinates before committing address and location together; pin movement reverse geocodes before commit. Failed or stale requests restore the previous valid pair, and valid location changes may expose up to three closest branches.
- Both call-center and app-order lists support MoMo-number search and a MoMo-number column; display missing values as `-` rather than inventing data.
- Across top-level feature roots, use configured absolute imports. Within the same root feature, use relative imports; keep TypeScript and Vite alias configuration synchronized.
- Threshold-discount eligibility is based on line quantity times the base unit price. Fixed discounts deduct `discountValue`; percentage discounts apply `discountValue` as a percentage. Ignore invalid zero discounted-price fallbacks and never produce a negative applied price.
- Include the current Altin estimate or ordinary calculated delivery fee in the displayed and submitted cart total; exact location without a selected branch has no calculable fee yet.
- Treat autocomplete suggestions and selected-place coordinate resolution as one provider session: create one token when search begins, reuse it through resolution, and clear it after the selected place is consumed. Require three characters before querying.
- Use the cached location-list, coordinate-resolution, and reverse-geocoding operations; normalize supported direct and list-wrapped estimate responses while preserving a usable estimate identifier.
- New request hooks copy the sibling location hooks exactly: fetch-based `useMutation`, log a non-OK response, cast `result.data.<field>` to the generated type, expose a `handle<Operation>` wrapper that logs and returns `undefined` on failure, and return `{ handle<Operation>, ...mutation }`. No inline response interfaces or custom error classes in hook files; contracts live in the feature `interface` folder. See [[../sources/call-center-wider-search-hook-and-action-correction|Call Center Wider Search Hook And Action Correction]].
- Actions inside dropdowns and lists must read as clickable: use a Mantine `Button` (light variant, `radius="lg"`, icon in `leftSection`), not an `UnstyledButton` text row.
- `searchLocationWider` is the agent-triggered fallback when suggestions miss: one call per Enter or "Search wider" press, never per keystroke. Wider places replace the list only when some were found; an empty or refused search keeps the live suggestions and reports above them. Selecting any suggestion closes the menus before coordinate resolution so a second click cannot commit a different place.
- Render brand choices only from `getCurrentCallCenterAgent.data.tenants`; hide the optional switcher for one membership, disable `switchable: false` entries, and treat founding `tenantId: null` as a valid active brand rather than a missing assignment.
- A login with `brandSuspended: true` is a limbo session. Load the self-read and expose only brand switching or logout until an available brand becomes active; do not mount dashboard, catalog, order, or checkout queries first.
- Tenant switching is a data-boundary transition, not a cosmetic theme change. Explicitly tenant-scope products, product-family variant expansion, branches, closest branches, and category roots; isolate their query keys by tenant; clear persisted cart/filter state; and remount local brand-scoped UI state after a successful switch.
- Treat a rejected or empty switch response as ambiguous because the backend may have committed before the response was lost. Purge tenant-scoped state, block operational routes, and reconcile through `getCurrentCallCenterAgent` before deciding which brand is active.
- Treat only `statusCode: 401` as a dead session. A 403 from an operational query refreshes the self-read, while a 403 or any other unsuccessful self-read becomes a blocking account error and must not recursively invalidate itself or let persisted user state mount operational routes.
- Logout calls `callCenterAgentLogout` but clears authentication, cart, filters, and query caches in `finally`, because an already-ended Redis session still requires complete local cleanup.
- Keep only login, logout, invalid-session cleanup, and other genuine session-security behavior under `src/authentication`. Shared active-tenant access belongs in root `src/hooks`; brand-switch mutation/UI/types/tests belong to `src/switcher/brand`; user identity presentation belongs to `src/profile` at `/profile`.
- Preserve each feature's established subfolder boundaries instead of mixing components, hooks, helpers, interfaces, and tests in one folder. Use the shared `Conditional` component for new boolean presentation checks.
- Feature entry components own hook consumption and orchestration, then pass required values and callbacks into extracted presentation components through typed props. Keep those prop contracts in the feature's `interfaces` folder rather than inline in component files.
- Structure the user menu as Application, Active brand, and Danger zone sections so Profile navigation, tenant switching, and logout remain distinct actions.
- Keep product dimension, size, and preference choices in a bounded internal scroll area while the product identity, quantity controls, and Add to Cart action remain visible. Represent grid/list mode as a two-option accessible segmented radio control rather than an ambiguous single toggle.
- Render the active-brand header logo with preserved aspect ratio, explicit bounds, client-side dashboard navigation, and a known fallback for missing or failed tenant assets.

## Constraints

- Do not create a new order reference/idempotency key for a retry of an unchanged checkout payload.
- Gift-recipient changes are part of the order fingerprint.
- Altin courier exact-location orders require a current estimate before submission.
- Invalidate an Altin estimate when branch, cart, fulfillment location, order method, or other estimate inputs change. Do not invent an address fallback when the generated request contract permits omission.
- Do not silently swap coordinate fields as incidental frontend cleanup.
- Never store authentication, map, payment, or API values in project knowledge.
- Never derive active tenant from the JWT claim after a switch; use the self-scoped account response because the JWT tenant claim is intentionally stale.
- Never omit `tenant` from shared storefront catalog queries while a tenant brand is active; an agent token is treated as public by those reads and omission silently falls back to the founding catalog.
- Do not preserve a branch-dependent address, estimate, vehicle category, or delivery fee after the branch changes.
- Do not treat a threshold amount as the discount amount; eligibility and deduction are distinct concepts.

## Decisions And Rationale

- Stable idempotency protects against rapid clicks and network retries at the request-contract level; an in-flight ref only reduces avoidable parallel calls.
- Location-first/address-last sequencing preserves the visible address across branch/location resets.
- Reverse-geocode-first map commits prevent the form from entering the invalid intermediate state `location + empty address`.
- Courier-type dispatch keeps third-party/ordinary delivery pricing separate from Altin’s cart-estimate contract.
- Showing disabled fulfillment controls maintains spatial continuity while tooltips explain the prerequisite or incompatible order method.
- Precomputing safe display values prevents JavaScript property access from throwing before a presentation-only conditional can hide the child.
- Server payment confirmation remains authoritative for mobile-payment completion before the cart is cleared.
- Repricing every line during branch transition keeps displayed availability and discounts consistent with the selected fulfillment source, while resetting derived delivery state prevents stale fees and estimates.
- Treating address and coordinates as one committed value prevents map, search, and checkout from disagreeing after asynchronous failures.

## Verification Expectations

- Verify customer search → standalone detail → back, fresh direct links, loading/error exits, and routed-customer changes. Previous profile/history data must disappear and in-flight reads must abort on context changes. Inspect desktop/mobile presentation in both themes.

- Validate maintained chat/login/logout GraphQL operation documents against the current staging schema before relying on generated-type presence alone. Verify pool/mine separation, claim-gated reply, assigned reply, chronological event rendering, notification deep links/read state, attach/detach order, close confirmation, attachment-only send, failed-send retention, queue polling, and live-message subscription.
- Verify chat controls with backend-denied access messages and cross-brand/non-support conversations; never assume disabled UI replaces authorization. Exercise `/chats` and `/chats/:conversationId` with a mock or safe agent session and inspect the browser console for JavaScript failures.
- Run focused checkout idempotency, gift-recipient, availability, exact-location, and address-reset tests.
- Run `yarn build` and `yarn test --run`; distinguish assertion passes from unhandled-error exit failures.
- Verify duplicate clicks, retry after transient failure, changed payload, successful completion, and mobile-payment confirmation.
- Verify typed address with coordinates, suggestion selection, map pin/reverse geocode, clearing, branch changes, and Altin estimate invalidation.
- Verify Altin and non-Altin exact-location branches independently, including network-call selection, stale-estimate reset, form validity, unavailable-item modal behavior, and post-checkout control reset.
- Verify product families with one and several dimensions, required and optional preferences, no selected variant, closed-modal mounts, cart snapshots, checkout serialization, and mixed families where a no-config product has configured siblings.
- Verify exact-category selectors send `categoryIds`; verify root-category browsing selectors send the root slug through `categoryPaths`, clear `categoryIds`, include descendant products, and preserve tenant-scoped category loading.
- Verify the Sales product grid emits container-query rules for three, four, and five columns and reflows from the Products panel's inline size.
- Verify branch set/change/clear with non-empty carts, line repricing, dependent-state reset, delivery-area versus exact-location exclusivity, and the empty-cart-only branch lock.
- Verify suggestion selection, stale/failed geocoding, pin reverse geocoding, closest-branch results, and cart totals before branch selection and for Altin/non-Altin branches.
- Verify one provider-session token spans suggestion and selected-place resolution, then clears; test the three-character threshold, named coordinate fields, cached-operation behavior, and both supported estimate response shapes.
- Verify threshold boundaries, fixed and percentage deductions, invalid zero discounted prices, and nonnegative totals.
- Verify MoMo search/filter transport and column rendering for both order families, including missing values.
- Verify login limbo routing, fail-soft membership preservation, unavailable-brand disabling, same-token and ambiguous-response switching, active-account refresh, tenant-key isolation for list and family-variant queries, cart/filter/query-cache reset, layout remounting, transport/envelope 401 cleanup, 403 account refresh, and logout cleanup on both success and failure.
- Verify the Profile menu hierarchy, authenticated `/profile` navigation and unauthenticated redirect, tenant-logo failure fallback, grid/list selected state, and constrained product-picker scrolling with enough variants to overflow naturally.
- Do not run Codegen casually against live staging; confirm schema availability and intended generated diff first.

## Evidence

- [[../sources/call-center-customer-detail-navigation-correction|Call Center Customer Detail Navigation Correction]]: direct acceptance of styling and rejection of inline profile navigation, with current route/folder ownership and theme-contrast verification.

- Current repository: `/Users/acazumah/Documents/C.E.Q.A/call-center-web-app`, branch `develop`, base commit `6a9cff6b681f`; the multi-brand integration remained uncommitted at verification.
- Historical location: `/Users/acazumah/Documents/Pizzaman/call-center-web-app`; all directly discovered sessions under that path have been classified.
- Current package manifest, provider/router composition, cart/location/checkout hooks and tests, GraphQL Codegen config, and CI workflow.
- Processed records: `019eb952-2c35-7771-9f62-2002147d7523`, `019e6eca-0fe9-73d1-93b4-9389ddfc2784`, `019e63bc-dc06-73b1-a669-1b7ae43c69ee`, `019e5c27-e267-72c0-8d61-17ba7f7e256e`, `019e2825-6af9-7bd2-bb76-69bac885ebfc`, `019e266d-9d8c-7303-a71b-a7ea7f386abd`, `019e266b-c22a-7380-9aec-18cd6bd77841`, `019de9d4-d4fa-7a70-8e07-0358896f1d03`, `019dda2a-5872-7f83-b151-a4a0163a1e42`, and `019caebd-b7ec-7e60-a01f-8fd02bec2e52`.
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-1|C.E.Q.A/Altin Project Knowledge Harvest — Batch 1]].
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-2|C.E.Q.A/Altin Project Knowledge Harvest — Batch 2]].
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-3|C.E.Q.A/Altin Project Knowledge Harvest — Batch 3]].
- Direct Hermes session `20260709_202251_e5340a` plus current static location/tooling source in [[../sources/ceqa-call-center-hermes-supplement-2|C.E.Q.A Call Center Hermes Supplement — 2]].
- Repository integration guide `docs/CALL_CENTER_ACCOUNT_API.md` plus the tenant-aware profile/switcher/catalog implementation inspected and verified through 2026-07-30.
- Repository integration guide `docs/CHAT_CALL_CENTER_GUIDE.md`, the `src/chat` implementation, optional Firebase messaging lifecycle, focused chat regressions, and staging schema validation completed on 2026-08-04. A disposable GraphQL mock exercised pool/mine rendering, claim-gated input, assigned replies, notification deep links, and order-link UI with zero browser JavaScript errors.
- Backend category-filter guidance relayed by the user on 2026-08-01, preserved in [[../sources/call-center-product-category-filter-contract|Call Center Product Category Filter Contract]], plus the focused frontend regression and current generated `GetAllProductsInput` contract.
- User-specified panel-responsive product-grid behavior from 2026-08-01, preserved in [[../sources/call-center-product-grid-container-responsiveness|Call Center Product Grid Container Responsiveness]], plus the focused container-query regression.
- Authenticated local browser verification on 2026-07-30 used a disposable GraphQL mock to complete Pizzaman Chickenman → Second Brand → Pizzaman Chickenman in one persisted session. At each settled state only the active brand was disabled and the previous brand recovered as selectable. The same mock-backed UI verified protected Profile presentation and brand-logo image/initial fallback behavior.
- The earlier 2026-07-29 browser smoke test exercised Sales grid/list control and a twelve-size product picker; the picker viewport was 304 px high against 555 px of content and accepted a 220 px scroll offset.
- The supplied 2026-07-30 production response exposed the actual options/preferences defect. The fuzzy `family` request for `CHICKENMAN_JOLLOF_MINI_BUCKET` returned normal, `PLUS`, and `ASSORTED` products together, while Wings products contained both `familyConfig` and required sauce preferences. The required UI contract is preference-first: `Jollof Mini Bucket (Wings)` shows only Hot Sauce/No Sauce at GH¢140, and `Assorted Jollof Mini Bucket (Wings)` shows only Hot Sauce/No Sauce at GH¢160. Current source uses `exactFamily` and suppresses family pickers whenever the exact opened product has preferences. Focused regressions, lint, TypeScript, and build pass. A Chromium harness verified both prices and preference-only states, verified `exactFamily: ASSORTED_JOLLOF_MINI_BUCKET`, completed sauce selection, and reported zero JavaScript errors. The earlier family-option-first diagnosis was wrong and is superseded by this evidence.

## Contradictions

- The README remains the generic Vite template and omits the real product, environment, Codegen, and checkout architecture.
- GraphQL Codegen depends on a live staging endpoint and injects `@ts-nocheck` into generated output, reducing reproducibility and type assurance.
- The 2026-07-29 full Vitest run historically exited zero, but the current `feature/family` branch no longer isolates the browser-router boundary in `App.test.tsx`. On 2026-07-30, both the isolated app test and the full run passed their assertions but exited one because JSDOM's `AbortSignal` is rejected by Node/Undici as a different realm; Redux Persist/local-storage warnings also remain.
- The earlier missing-flat-config claim is superseded: current source includes `eslint.config.js`, and the 2026-07-29 `yarn lint` run exited zero.
- CI still requires remote confirmation. The focused product regression, lint, and production build pass locally, while the unrelated app-router test infrastructure currently prevents a zero-exit full test run.
- The product-preferences session reported that list-level picker components owned iteration, but current `SelectProductModal.tsx` again owns dimension, size, and preference `.map` loops. This conflicts with the latest explicit structure correction even though helpers, interfaces, hooks, and item components remain separated.
- The family-config API guide was supplied as reference-only evidence. That session completed no repository change, and no maintained guide file was found in the current checkout.
- The user-established import rule is absolute imports across top-level feature roots and relative imports within one root feature, but current `src/cart` code mixes both styles internally.
- Historical location guidance says `getAltinCartEstimate` was authorized only for the CU role, while current call-center checkout requires an Altin estimate for eligible branches and invokes that operation for call-center users. Backend role compatibility remains unverified.
- Older delivery copy said a fee was calculated after checkout. Current source instead shows zero before a branch makes calculation possible and uses availability feedback after an attempted estimate; current behavior supersedes the older wording.
- The direct Hermes response claimed several delivery-fee, timing, and courier fields were added to one direct-payment order mutation, but current source and the containing commit show only `location` added to that selection set. Generated type fields do not establish operation selection.
- Historical lint eventually exited zero under `--quiet` after rules were demoted to warnings; treat this as tooling-operability evidence, not a clean-lint result.

## Confidence

High for current static checkout/location and multi-brand profile/switcher/catalog architecture plus local lint, test, build, mock-backed A → B → A switching, menu/Profile/catalog UI verification, and unauthenticated route protection; medium for staging-backed switching, end-to-end payment, maps, backend coordinate behavior, and remote CI because no valid staging multi-brand agent session or live external integration was exercised.

## Open Questions

- Does the backend enforce the same idempotency contract, including key scope and retention?
- Should GraphQL schema acquisition move from live staging to a reproducible artifact?
- When will a safe multi-brand staging account be available to exercise successful switching, suspended-brand limbo, and catalog isolation end to end?
- When can the coordinate compatibility exception be removed after backend normalization?
- Should product dimension/size/preference iteration return to imported list-level components?
- Should the family configuration and preference contracts be added as maintained repository documentation?
- Should same-feature `src/cart/...` imports be normalized to relative paths to match the explicit import-boundary rule?
- Does the backend authorize the call-center roles that the current Altin estimate flow requires, or must the operation/role contract change?
