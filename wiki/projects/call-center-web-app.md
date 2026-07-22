---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, ceqa, call-center, checkout, orders, react]
sources:
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-1.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-2.md
  - ../sources/ceqa-altin-project-knowledge-harvest-batch-3.md
  - ../sources/ceqa-call-center-hermes-supplement-2.md
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

- Root providers compose persisted Redux, Query, subscriptions, system/auth initialization, Mantine, Styled Components, and routing.
- Protected routes cover Dashboard, Sales, Orders, and order details; login uses a separate auth layout.
- Product/context hooks own catalog selection, family dimensions, per-variant preferences, and recommendation flows.
- Cart hooks own branch, delivery area/exact location, availability, courier-specific pricing/Altin estimates, gift recipients, checkout, and payment-confirmation state.
- Location search, suggestions, map interaction, reverse geocoding, closest-branch discovery, and delivery pricing cooperate through the cart's fulfillment state rather than maintaining independent address/coordinate copies.
- Orders and order-detail modules separate call-center orders from app-originated orders.
- GraphQL operations use a mixture of generated contracts and focused fetch-based hooks.

## Folder Ownership

- `src/authentication`, `src/redux/auth`, `src/providers/system`: login, persisted authentication, and current-user/system initialization.
- `src/products`: product querying, selection, variants/preferences, recommendations, and branch context.
- `src/cart`: cart UI, exact location/delivery areas, availability, estimates, gifts, payment, and checkout orchestration.
- `src/cart/interface`: cart-owned contracts for location, delivery, pricing, checkout, and component boundaries.
- `src/orders`, `src/order`: order lists, filters, details, timelines, fulfillment, payment, and print views.
- `src/dashboard`: sales/order metrics and date filters.
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
- Conditional wrappers do not defer evaluation of JSX children. Derive optional values safely before rendering rather than placing unsafe property access inside a false conditional.
- `familyConfig` describes ordered variant dimensions; preferences are annotations on the selected variant. Resolve one concrete variant, enforce required preferences, and preserve preference snapshots on the cart line and checkout input.
- Branches may be changed or cleared while a cart has items. Every branch change reprices all lines against that branch and invalidates dependent address, coordinates, delivery fee, Altin estimate, and vehicle-category state before the new branch is accepted.
- Delivery area and exact location are mutually exclusive fulfillment modes. Keep the branch selector disabled only when the cart is empty; mode-specific controls own their prerequisites and feedback.
- Suggestion selection resolves coordinates before committing address and location together; pin movement reverse geocodes before commit. Failed or stale requests restore the previous valid pair, and valid location changes may expose up to three closest branches.
- Both call-center and app-order lists support MoMo-number search and a MoMo-number column; display missing values as `-` rather than inventing data.
- Across top-level feature roots, use configured absolute imports. Within the same root feature, use relative imports; keep TypeScript and Vite alias configuration synchronized.
- Threshold-discount eligibility is based on line quantity times the base unit price. Fixed discounts deduct `discountValue`; percentage discounts apply `discountValue` as a percentage. Ignore invalid zero discounted-price fallbacks and never produce a negative applied price.
- Include the current Altin estimate or ordinary calculated delivery fee in the displayed and submitted cart total; exact location without a selected branch has no calculable fee yet.
- Treat autocomplete suggestions and selected-place coordinate resolution as one provider session: create one token when search begins, reuse it through resolution, and clear it after the selected place is consumed. Require three characters before querying.
- Use the cached location-list, coordinate-resolution, and reverse-geocoding operations; normalize supported direct and list-wrapped estimate responses while preserving a usable estimate identifier.

## Constraints

- Do not create a new order reference/idempotency key for a retry of an unchanged checkout payload.
- Gift-recipient changes are part of the order fingerprint.
- Altin courier exact-location orders require a current estimate before submission.
- Invalidate an Altin estimate when branch, cart, fulfillment location, order method, or other estimate inputs change. Do not invent an address fallback when the generated request contract permits omission.
- Do not silently swap coordinate fields as incidental frontend cleanup.
- Never store authentication, map, payment, or API values in project knowledge.
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

- Run focused checkout idempotency, gift-recipient, availability, exact-location, and address-reset tests.
- Run `yarn build` and `yarn test --run`; distinguish assertion passes from unhandled-error exit failures.
- Verify duplicate clicks, retry after transient failure, changed payload, successful completion, and mobile-payment confirmation.
- Verify typed address with coordinates, suggestion selection, map pin/reverse geocode, clearing, branch changes, and Altin estimate invalidation.
- Verify Altin and non-Altin exact-location branches independently, including network-call selection, stale-estimate reset, form validity, unavailable-item modal behavior, and post-checkout control reset.
- Verify product families with one and several dimensions, required and optional preferences, no selected variant, closed-modal mounts, cart snapshots, and checkout serialization.
- Verify branch set/change/clear with non-empty carts, line repricing, dependent-state reset, delivery-area versus exact-location exclusivity, and the empty-cart-only branch lock.
- Verify suggestion selection, stale/failed geocoding, pin reverse geocoding, closest-branch results, and cart totals before branch selection and for Altin/non-Altin branches.
- Verify one provider-session token spans suggestion and selected-place resolution, then clears; test the three-character threshold, named coordinate fields, cached-operation behavior, and both supported estimate response shapes.
- Verify threshold boundaries, fixed and percentage deductions, invalid zero discounted prices, and nonnegative totals.
- Verify MoMo search/filter transport and column rendering for both order families, including missing values.
- Do not run Codegen casually against live staging; confirm schema availability and intended generated diff first.

## Evidence

- Current repository: `/Users/acazumah/Documents/C.E.Q.A/call-center-web-app`, branch `develop`, base commit `6a9cff6b681f`, clean at inspection.
- Historical location: `/Users/acazumah/Documents/Pizzaman/call-center-web-app`; all directly discovered sessions under that path have been classified.
- Current package manifest, provider/router composition, cart/location/checkout hooks and tests, GraphQL Codegen config, and CI workflow.
- Processed records: `019eb952-2c35-7771-9f62-2002147d7523`, `019e6eca-0fe9-73d1-93b4-9389ddfc2784`, `019e63bc-dc06-73b1-a669-1b7ae43c69ee`, `019e5c27-e267-72c0-8d61-17ba7f7e256e`, `019e2825-6af9-7bd2-bb76-69bac885ebfc`, `019e266d-9d8c-7303-a71b-a7ea7f386abd`, `019e266b-c22a-7380-9aec-18cd6bd77841`, `019de9d4-d4fa-7a70-8e07-0358896f1d03`, `019dda2a-5872-7f83-b151-a4a0163a1e42`, and `019caebd-b7ec-7e60-a01f-8fd02bec2e52`.
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-1|C.E.Q.A/Altin Project Knowledge Harvest — Batch 1]].
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-2|C.E.Q.A/Altin Project Knowledge Harvest — Batch 2]].
- [[../sources/ceqa-altin-project-knowledge-harvest-batch-3|C.E.Q.A/Altin Project Knowledge Harvest — Batch 3]].
- Direct Hermes session `20260709_202251_e5340a` plus current static location/tooling source in [[../sources/ceqa-call-center-hermes-supplement-2|C.E.Q.A Call Center Hermes Supplement — 2]].

## Contradictions

- The README remains the generic Vite template and omits the real product, environment, Codegen, and checkout architecture.
- GraphQL Codegen depends on a live staging endpoint and injects `@ts-nocheck` into generated output, reducing reproducibility and type assurance.
- The historical full nine-test run passed assertions but exited nonzero because an existing app test emitted unhandled router/network errors against staging.
- The earlier missing-flat-config claim is superseded: current source includes `eslint.config.js`. No current lint-pass claim is made because the command was not run during this read-only harvest.
- CI runs the full test command, so the unhandled app-test behavior may remain a pipeline risk until verified or repaired.
- The product-preferences session reported that list-level picker components owned iteration, but current `SelectProductModal.tsx` again owns dimension, size, and preference `.map` loops. This conflicts with the latest explicit structure correction even though helpers, interfaces, hooks, and item components remain separated.
- The family-config API guide was supplied as reference-only evidence. That session completed no repository change, and no maintained guide file was found in the current checkout.
- The user-established import rule is absolute imports across top-level feature roots and relative imports within one root feature, but current `src/cart` code mixes both styles internally.
- Historical location guidance says `getAltinCartEstimate` was authorized only for the CU role, while current call-center checkout requires an Altin estimate for eligible branches and invokes that operation for call-center users. Backend role compatibility remains unverified.
- Older delivery copy said a fee was calculated after checkout. Current source instead shows zero before a branch makes calculation possible and uses availability feedback after an attempted estimate; current behavior supersedes the older wording.
- The direct Hermes response claimed several delivery-fee, timing, and courier fields were added to one direct-payment order mutation, but current source and the containing commit show only `location` added to that selection set. Generated type fields do not establish operation selection.
- Historical lint eventually exited zero under `--quiet` after rules were demoted to warnings; treat this as tooling-operability evidence, not a clean-lint result.

## Confidence

High for current static checkout/location architecture and explicit session corrections; medium for end-to-end payment, maps, backend coordinate behavior, and CI because no external integration or current test run was executed.

## Open Questions

- Does the backend enforce the same idempotency contract, including key scope and retention?
- Should GraphQL schema acquisition move from live staging to a reproducible artifact?
- When will the historical unhandled app-test network/router errors be rechecked or fixed against the current tree?
- When can the coordinate compatibility exception be removed after backend normalization?
- Should product dimension/size/preference iteration return to imported list-level components?
- Should the family configuration and preference contracts be added as maintained repository documentation?
- Should same-feature `src/cart/...` imports be normalized to relative paths to match the explicit import-boundary rule?
- Does the backend authorize the call-center roles that the current Altin estimate flow requires, or must the operation/role contract change?
