---
type: project
status: active
created: 2026-08-04
updated: 2026-09-14
tags: [project, livelycura, doordrop, choproute, expo, mobile, food-marketplace]
sources:
  - ../sources/doordrop-expo-image-native-abi-alignment.md
  - ../sources/doordrop-rebrand-and-asset-structure.md
  - ../sources/marketplace-scoped-admin-catalog-order-restructure.md
  - ../sources/choproute-marketplace-owned-category-taxonomy.md
  - ../sources/choproute-navigation-hook-migration.md
  - ../sources/choproute-navigation-hook-convention.md
  - ../sources/choproute-feature-owned-catalog-queries.md
  - ../sources/choproute-marketplace-feature-folder-removal.md
  - ../sources/choproute-system-marketplace-ownership-custom-app-removal.md
  - ../sources/choproute-client-branch-removal.md
  - ../sources/choproute-redux-marketplace-state-correction.md
  - ../sources/choproute-raised-restaurants-navigation-category-correction.md
  - ../sources/choproute-explore-naming-ownership-correction.md
  - ../sources/choproute-home-restaurants-navigation-direction.md
  - ../sources/choproute-marketplace-stage-one-correction.md
  - ../sources/pice-home-ui-direction.md
  - ../sources/pice-project-bootstrap-directive.md
confidence: high
aliases: [LivelyCura ChopRoute App, LivelyCura Pice App]
---

# LivelyCura doorDrop App

## Summary

doorDrop is LivelyCura's generic consumer food marketplace. The current Expo repository was initially scaffolded as a prospective Pice app, then pivoted to ChopRoute's marketplace architecture, and is now publicly branded doorDrop. The existing ChopRoute backend marketplace identity remains the compatibility boundary until a separate coordinated migration.

## Purpose

Let customers discover ordinary ERP-managed products from every organization with active ChopRoute marketplace access. Delivery-location context will later support server-side fulfillment through the closest eligible organization facility without making branches part of the consumer delivery contract.

## Stack

- Expo SDK 57, React Native 0.86, React 19, and TypeScript 6.
- React Navigation 7 native stack and bottom tabs.
- Apollo Client with generated GraphQL interfaces.
- Redux Toolkit, Redux Persist, AsyncStorage, styled-components/native, Reanimated, Expo notifications/location/updates, and PostHog.
- LivelyCura GraphQL/Mongoose backend with existing Marketplace, MarketplaceOrganizationAccess, Organization, Product, Facility, and ProductPrice ownership.

## Architecture

ChopRoute implements the marketplace-owned customer side of [[../concepts/livelycura-customer-support-architecture|LivelyCura Customer Support Architecture]]. Its direct Orders link into support as `ORDER`, but verified marketplace context keeps responder ownership in Admin rather than exposing the case to fulfilling organizations.

`src/system/SystemProvider.tsx` owns application bootstrap. Beside the existing user `useSystemQuery`, it runs `src/system/useMarketplaceQuery.ts`, which resolves the current marketplace and its access-granted organizations in one GraphQL operation and stores both in the Redux `marketplace` slice. React context and marketplace feature components do not own this state or its render gate. App-wide consumers use the single general `src/hooks/useMarketPlace.ts` Redux hook.

The stage-one product read path is:

`current ChopRoute request identity -> active MarketplaceOrganizationAccess -> Organization -> ordinary organization Product`

The next consumer catalog contract follows this path after the Admin/backend foundation is deployed:

`current ChopRoute request identity -> active MarketplaceOrganizationAccess -> published MarketplaceBusinessProductListing -> ordinary organization Product + canonical MarketplaceCategory`

`MarketplaceCategory` owns customer-facing meaning while the Admin-owned listing controls which ordinary products are published and how they are classified. Ordinary ERP categories are not part of this contract. The marketplace still does not copy product details: `MarketplaceProduct`, ProductLinking, and bidding remain valid for other marketplace capability combinations but are not consulted by ChopRoute Business Product discovery.

The app sends the selected delivery coordinates when requesting display prices. The backend may resolve the nearest ERP facility internally and return the effective product price, but never returns a branch selection contract to the consumer app. Actual delivery allocation remains a future order-stage decision.

## Folder Ownership

- App root: `/Users/acazumah/Documents/LivelyCura/livelycura-door-drop`.
- `assets`: one flat static-image directory. `assets/images.js` owns runtime image imports; feature code does not require image files directly or create nested image folders.
- `src/system`: user startup plus current-marketplace/access-organization startup queries and the single application render gate.
- `src/hooks/useMarketPlace.ts`: general app-wide Redux marketplace state and action access.
- There is no top-level `src/marketplace` client feature and no global combined marketplace catalog query. Shared presentation states and category helpers use the established main folders; product/category GraphQL operations live in each consuming feature's `hooks` folder.
- `src/redux/reducers/marketplace`: canonical app-wide current marketplace and access-granted organization state.
- `src/explore`: Explore screen composition with feature-owned `components`, `hooks`, `interfaces`, `helpers`, and `constants` subfolders for live search and category filtering.
- `src/home`: product-led Home composition, delivery-location header, and separate `useMarketplaceProducts`/`useMarketplaceCategories` operations driven by Redux organization IDs; no restaurant discovery.
- `src/categoryProducts`: category-specific product grids and their category-filtered product query, driven by Redux organization IDs.
- `src/restaurants`: access-granted restaurant discovery plus its own product query; restaurant identities come from Redux.
- `src/restaurantsDetails`: organization-scoped browsing with separate product and category operations that accept only organizations present in Redux access state.
- `src/components/menu-item`: canonical shared vertical product card for ordinary backend products.
- `src/components/horizontal-menu-item`: horizontal recent/favourite product variant.
- `src/navigation`: Home, Explore, Cart, and Orders bottom-tab ownership; raised center Restaurants stack action; and restaurant/category detail routes.
- `src/hooks/useAppNavigation.ts` and `src/hooks/useAppNavigationWithRef.ts`: canonical navigation-action abstractions for mounted React code and root-ref/external flows respectively.
- Backend `src/graphql/marketplace/marketplaces` and `src/services/marketplace/marketplaces`: current-context consumer discovery and server-side price resolution.
- ERP organization, product, category, facility, price, and future order modules remain authoritative for their domains.

## Commands

App:

- `yarn type-check`
- `yarn expo config --type public`
- `yarn expo export --platform web`

Backend:

- `yarn generate`
- `yarn build`
- `yarn vitest run --config vitest.integration.config.ts tests/integration/marketplace/dynamicMarketplaceArchitecture.test.ts`

## Runtime/Deployment

- Public identity is doorDrop with scheme/slug `doordrop` and native identifier `com.livelycura.doordrop` plus environment variants.
- Expo SDK 57 native modules are kept on one compatible patch graph. `expo-image` must not be paired with an older `expo-modules-core` lacking its required lifecycle symbols.
- Apollo sends `EXPO_PUBLIC_CLIENT_NAME`, defaulting to `CHOPROUTE_MARKETPLACE`; the active ChopRoute marketplace is configured with the matching `appIdentifier: CHOPROUTE_MARKETPLACE`.
- The existing marketplace/client key is retained for backend compatibility; changing it requires a coordinated marketplace-data and API migration.
- The color system and generated doorDrop mark are provisional until final branding is approved.
- Check City and Pice Restaurant are initial test access organizations, not hard-coded app tenants.

## Durable Conventions

- Execute the existing marketplace plan one independently verifiable stage at a time.
- Keep the current marketplace and its access-granted organizations in Redux. Do not restore a React marketplace context or request the organization list again inside product/category catalog queries.
- Load the current marketplace and accessible organizations from `src/system`, beside user startup. Do not move application bootstrap back into `src/marketplace`.
- Keep `src/hooks/useMarketPlace.ts` as the only general marketplace hook. Do not add a global combined product/category catalog hook.
- Put each product/category GraphQL operation in the consuming feature's `hooks` folder and derive its allowed organization IDs from Redux.
- Home always owns separate product and category query files; do not recombine them.
- Do not restore a top-level `src/marketplace` feature directory. Marketplace is system/Redux context in this client; place genuinely shared utilities in the established main folders and feature behavior in its owning feature.
- Do not restore a ChopRoute `src/customApp` client feature. Custom-app types in generated GraphQL reflect the shared backend schema and must not be hand-edited or treated as active client ownership.
- Marketplace access grants determine which organizations appear; never hard-code the initial organizations.
- Display ordinary organization products directly. Do not duplicate or link them into `MarketplaceProduct` for ChopRoute.
- Keep organization facilities out of the consumer delivery contract. Location selection is customer-facing; facility resolution is server-side.
- Do not maintain a client-side branch feature, branch Redux state, branch hooks, selector routes, or branch UI. Future fulfillment must not revive them.
- Explore is the full-catalog browse identity. Keep its screen and owned behavior under `src/explore`; do not restore parallel top-level `menu`, `search`, or standalone `categories` browse features.
- Follow the established mobile feature structure: components, hooks, interfaces, helpers, and constants live in their owned subfolders rather than being flattened into the feature root or accumulated in the screen.
- Keep static images directly under root `assets` and export runtime images through `assets/images.js`; do not add nested image folders or direct feature-level image requires.
- After changing Expo native-package patch versions, run Expo compatibility alignment, regenerate the native project, reinstall Pods, and verify an actual simulator launch; JavaScript type-check/export alone cannot detect native ABI mismatch.
- Route all navigation actions through `useAppNavigation` or `useAppNavigationWithRef`. Direct `useNavigation` is not an accepted feature-level alternative; improve the shared hook typing if necessary. Direct `useRoute` remains valid for reading route parameters.
- Home is product-led: Categories, Popular, then up to four five-item category rails. Do not render restaurants on Home.
- Category chips are not the end of Home. Render the matching grouped product rails below Popular and the marketing card.
- Popular `View all` opens Explore; category actions open category-specific product grids.
- Bottom tabs are Home, Explore, Cart, and Orders. Keep their labels visible in the full-width shelf; Cart quantity controls only its badge.
- The shelf uses one continuous top border that curves down around the raised Restaurants action and reconnects to both tab groups. Never approximate it with a floating circle over a straight divider.
- Restaurants is the raised center action, not a fifth bottom-tab route. It opens a standalone root-stack screen with its own Back action. Restaurant detail remains organization-scoped and filters its shared product grid by that organization's categories.
- Use active `MarketplaceCategory` records as the canonical ChopRoute taxonomy. Customer-facing category IDs are canonical IDs, never same-name organization-category groups.
- Consume only published Admin-owned Business Product configurations and their canonical category IDs. Do not read ordinary ERP categories, category-name grouping, or product-name fallback for ChopRoute classification.
- Keep marketplace classification and publication out of ERP and SERLP Mobile; those clients continue ordinary product/category management.
- Show only active canonical categories used by currently visible products. Restaurant category filters use the same taxonomy scoped to that restaurant's products.
- Keep local ERP categories available for internal classification only; ChopRoute classification comes exclusively from Admin-owned Business Product configurations.
- Preserve the approved shared vertical `MenuItem`; use the separate horizontal variant for recent/favourite sections.
- Do not render decorative background patterns or floating background motifs.

## Constraints

- Stage one does not create marketplace orders, cart allocation, payouts, branch selection, pickup, bidding, product links, or modifier-domain replacements.
- Cart and Orders remain visible for navigation continuity but are gated so the old single-branch ordering path cannot run.
- The legacy client branch implementation is removed. Checkout and reorder entry points remain gated until marketplace-safe server allocation is designed.
- Do not branch a separate Pice project unless the Pice engagement is agreed and the user explicitly starts it.

## Decisions And Rationale

The existing MarketplaceOrganizationAccess relationship already expresses which organizations participate in ChopRoute. Reusing Organization and Product preserves ERP ownership and prevents catalog drift, synchronization failures, and unnecessary translation models.

`MarketplaceCategory` owns cross-organization customer-facing meaning. Admin-owned `MarketplaceBusinessProductConfiguration` is the adapter to ordinary ERP products: it stores canonical category IDs and publication state without changing `Product.categoryIds`, projecting organization categories, inferring names, or duplicating product details.

The current marketplace and accessible organization list are application-wide identity/discovery state used across Home, Explore, Restaurants, and later ordering stages. Redux therefore owns them after bootstrap. Because loading them is system startup work like user loading, `SystemProvider` owns the render gate and invokes a system-owned query; the marketplace feature must not introduce a second provider or state source.

The app should know that a customer selected a product from a restaurant and supplied a delivery location. It should not choose a delivery branch. Server-side orchestration has the authoritative organization facilities, pricing, availability, and future eligibility rules needed to make that decision safely.

The repository was pivoted in place instead of branched because Pice is not yet an agreed custom-app engagement. The previous UI corrections remain useful design evidence. Public app identity now belongs to doorDrop while the proven ChopRoute marketplace architecture and backend key remain in place for compatibility.

The first doorDrop build paired a newer precompiled Expo Image framework with an older Expo Modules Core that lacked `BaseModule.willDestroy`, causing an immediate `dyld` termination. The fix is dependency-graph alignment and a clean native rebuild, not application-code fallback or reversal of Expo Image caching.

Separating Restaurants from Home keeps Home optimized for meal discovery while still giving organizations a first-class browse path. Organization filtering is a server-side catalog filter over ordinary ERP products, not a new restaurant listing or linked product model. Requested organization IDs are intersected with active marketplace access so client parameters cannot reveal an unapproved catalog.

## Verification Expectations

For stage one, verify Redux marketplace bootstrap, active-access organization isolation, published Business Product and canonical marketplace-category discovery, ordinary ERP-category exclusion, procurement-product exclusion for ChopRoute, server-only nearest-facility price resolution, delivery-location selection without a branch modal, shared product cards on Home, Explore, category grids, and restaurant detail, Explore search/filter behavior, Home category routing, raised-center Restaurants stack navigation and Back behavior, organization-filtered catalog denial for inaccessible IDs, visible tab labels, inactive Cart badge behavior, TypeScript, Expo config/export, backend build, and focused integration coverage.

Ordering, cross-organization carts, allocation, pickup, availability, fees, and payment/payout behavior require separate design and verification in later stages.

## Evidence

- Canonical taxonomy decision and implementation contract in [[../sources/choproute-marketplace-owned-category-taxonomy|ChopRoute Marketplace-Owned Category Taxonomy]].
- Current Admin-owned catalog and order boundary in [[../sources/marketplace-scoped-admin-catalog-order-restructure|Marketplace-Scoped Admin Catalog And Order Restructure]].
- Direct architecture correction in [[../sources/choproute-marketplace-stage-one-correction|ChopRoute Marketplace Stage-One Correction]].
- Redux ownership correction in [[../sources/choproute-redux-marketplace-state-correction|ChopRoute Redux Marketplace State Correction]].
- Client branch removal in [[../sources/choproute-client-branch-removal|ChopRoute Client Branch Removal]].
- System-owned marketplace bootstrap and custom-app removal in [[../sources/choproute-system-marketplace-ownership-custom-app-removal|ChopRoute System Marketplace Ownership And Custom-App Removal]].
- Marketplace feature-folder removal in [[../sources/choproute-marketplace-feature-folder-removal|ChopRoute Marketplace Feature Folder Removal]].
- Feature-owned product/category query correction in [[../sources/choproute-feature-owned-catalog-queries|ChopRoute Feature-Owned Catalog Queries]].
- Navigation abstraction correction in [[../sources/choproute-navigation-hook-convention|ChopRoute Navigation Hook Convention]].
- Completed navigation migration in [[../sources/choproute-navigation-hook-migration|ChopRoute Navigation Hook Migration]].
- Home/restaurant navigation correction in [[../sources/choproute-home-restaurants-navigation-direction|ChopRoute Home And Restaurant Navigation Direction]].
- Explore naming and folder-ownership correction in [[../sources/choproute-explore-naming-ownership-correction|ChopRoute Explore Naming And Ownership Correction]].
- Raised-center navigation and direct category discovery correction in [[../sources/choproute-raised-restaurants-navigation-category-correction|ChopRoute Raised Restaurants Navigation And Category Correction]].
- Historical UI constraints in [[../sources/pice-home-ui-direction|Pice Home UI Direction]].
- Rebrand and flat-asset directive in [[../sources/doordrop-rebrand-and-asset-structure|doorDrop Rebrand And Asset Structure]].
- Native ABI crash evidence and verified remediation in [[../sources/doordrop-expo-image-native-abi-alignment|doorDrop Expo Image Native ABI Alignment]].
- Live app repository: `/Users/acazumah/Documents/LivelyCura/livelycura-door-drop`.
- Live backend repository: `/Users/acazumah/Documents/LivelyCura/livelycura-backend`.
- On 2026-08-06 the app passed TypeScript, Expo public configuration, `git diff --check`, and a production-style web export.
- On 2026-08-06 the backend passed TypeScript build, `git diff --check`, and the focused dynamic marketplace integration file with 17 of 17 tests.
- On 2026-08-06 a 393 × 852 browser comparison verified the image-led Restaurants tab and hero/category/product-grid restaurant detail against the supplied references; the final browser console reported no errors.
- On 2026-08-06 a 393 × 852 browser pass verified the adjacent Explore search/filter header, filter toggle, and live product search with no console errors; TypeScript, web export, formatting, and `git diff --check` passed after obsolete browse features were removed.
- On 2026-08-06 Explore, categoryProducts, and restaurants were corrected to the repository's established feature subfolders; focused formatting, TypeScript, `git diff --check`, and a fresh production-style web export passed without redesigning the visible experiences.
- On 2026-08-06 the live ChopRoute context returned five active ERP category records from Check City and Pice, merged into the customer-facing Fried Rice, Jollof, and Pizza filters. A 393 × 852 in-app Browser pass verified the labeled four-tab shelf, raised center Restaurants action, standalone screen, Back action, and a clean console.
- On 2026-08-06 a focused source/implementation comparison verified the shelf border's continuous center curve. The same 393 × 852 pass showed Fried Rice, Jollof, and Pizza product rails below the marketing card; Fried Rice `View all` opened its populated category screen, Restaurants remained a standalone stack action, TypeScript and `git diff --check` passed, and the browser reported zero console errors.
- The initial mobile bootstrap returned HTTP 401 because the active ChopRoute record had no `appIdentifier`. After confirming no marketplace or custom-app routing collision, the record was assigned `CHOPROUTE_MARKETPLACE`; `resolveMarketplaceRequestContext("CHOPROUTE_MARKETPLACE")` then resolved ChopRoute successfully.
- On 2026-08-07 the React marketplace context/provider was removed. A Redux marketplace slice now receives the current marketplace and both live access organizations during bootstrap; the iOS Restaurants route rendered Check City and Pice Restaurant from Redux after reload. Focused formatting, relaxed-unused TypeScript validation, and `git diff --check` passed; strict TypeScript remained blocked by an unrelated live user edit with an unused `theme` parameter in `RestaurantMenuItem`.
- On 2026-08-07 all client branch files and remaining imports were removed, including branch navigation/types, branch UI, branch-dependent checkout guards, organization bootstrap, banner facility scoping, and client-facility reorder restoration. Checkout and reorder now remain explicitly gated. A repository search found no remaining branch feature symbols, the app reloaded successfully in the iOS Simulator, and focused formatting, relaxed-unused TypeScript validation, and `git diff --check` passed.
- On 2026-08-07 marketplace and access-organization loading moved from marketplace-owned bootstrap code into `src/system/useMarketplaceQuery.ts`, invoked beside user loading by `SystemProvider`. `src/hooks/useMarketPlace.ts` became the single general Redux hook; marketplace bootstrap/context code, `src/customApp`, and unused custom-app banner infrastructure were removed. The iOS Simulator reached the populated ChopRoute Home screen, focused formatting, relaxed-unused TypeScript, and `git diff --check` passed. Strict TypeScript remained blocked only by the pre-existing unused `theme` parameter in `RestaurantMenuItem.tsx`.
- On 2026-08-07 the remaining `src/marketplace` directory was removed. Its shared catalog components, query hook, filter interface, category helper, and stage screens moved into the established top-level main folders without changing UI or query behavior. No `src/marketplace` imports or filesystem directory remained; formatting, relaxed-unused TypeScript, and `git diff --check` passed.
- On 2026-08-07 the transitional global `useMarketplaceCatalogQuery` and filter interface were removed. Home now owns separate product/category operations in its two pre-existing empty hook files; Explore and Restaurant Details also own separate operations, while Restaurants and Category Products own the product operations they need. All build organization filters from Redux. The iOS Simulator rendered the populated Home screen; relaxed-unused TypeScript and `git diff --check` passed.
- On 2026-08-07 current-code inspection found direct `useNavigation` calls in Home, Explore, Category Products, Restaurants, and Restaurant Details despite the existing app navigation abstractions. The user confirmed all navigation actions must use those hooks; no navigation code was changed during that explanatory turn.
- On 2026-08-07 the user authorized complete remediation. Direct navigation actions were replaced across new and legacy screens plus the custom tab bar; direct `useNavigation` remained only inside `useAppNavigation`, while `useRoute`/`useNavigationState` remained read-only. Relaxed-unused TypeScript, `git diff --check`, source audit, and an iOS Simulator reload passed.
- On 2026-08-07 the canonical category plan was implemented across the backend, ChopRoute app, SERLP Mobile, and Pharmacy Portal. The backend added protected organization projections, canonical assignment/removal contracts, canonical consumer discovery/filtering, explicit Check City/Pice migration support, and synchronization rules. A live dry run reported all five known mappings already present with no writes; live GraphQL returned Fried Rice, Jollof, and Pizza with exact products only. Backend TypeScript, 22 focused integration tests, 3 focused product-creation tests, all three client TypeScript checks, the 2-test ERP creation suite, and `git diff --check` passed.
- On 2026-08-08 that projection implementation was removed and replaced with marketplace-scoped Admin configuration. Backend and Admin foundations passed builds, full/focused tests, migration dry run, formatting, and diff checks; Pharmacy Portal built and SERLP Mobile type-checked after marketplace assignment UI removal. The ChopRoute consumer-app switch remains deliberately unimplemented in this stage.
- On 2026-09-14 the doorDrop iOS app was rebuilt after aligning Expo SDK 57 native packages and regenerating CocoaPods. The build succeeded with zero errors, `com.livelycura.doordrop` launched in the iPhone Simulator, no subsequent `dyld`/missing-symbol termination appeared, and Expo dependency validation, TypeScript, all-platform export, and `git diff --check` passed.

## Contradictions

The original Pice project record described a branch-scoped custom app and `PICE_STOREFRONT`. That identity is superseded for the current repository by doorDrop's public identity and ChopRoute's retained marketplace context and location-first discovery. The raw Pice sources remain valid historical evidence for approved UI behavior, not current tenant architecture.

Earlier records use ChopRoute as both the public app name and backend marketplace identity. doorDrop supersedes the public name, Expo identity, native identifiers, analytics label, and repository path. `CHOPROUTE_MARKETPLACE` remains the backend compatibility key until an explicit migration is approved.

Existing bidding, MarketplaceProduct, product-linking, marketplace-order, and allocation code may still be valid elsewhere in LivelyCura. Its existence does not authorize reuse in ChopRoute's consumer catalog or stage-one ordering.

Earlier ChopRoute notes and implementation used Menu as the full-catalog tab name. Explore supersedes that route identity; “Menu” remains valid only where it describes a restaurant's product section or the shared ERP product domain.

The first Explore ownership note incorrectly described a flat internal feature. That interpretation is superseded: obsolete top-level features stay removed, while Explore itself follows the established component/hook/interface/helper/constant structure.

The earlier five-tab Restaurants contract and selected-route-only label rule are superseded by the newest navigation reference: Restaurants is a raised center stack action, while all four ordinary tab labels remain visible.

The first raised-center implementation still left a straight top divider behind the circle. That approximation is superseded by the continuous shelf border that curves around the center action.

The initial stage-one mobile implementation described and used a current-marketplace React context. Redux ownership supersedes that client-state mechanism; the backend request-context boundary remains unchanged.

The subsequent temporary Redux implementation still placed bootstrap and the general selector hook inside `src/marketplace`. System-owned startup and the top-level `src/hooks/useMarketPlace.ts` convention supersede that folder ownership. Historical custom-app client files are also removed from ChopRoute; generated CustomApp schema types remain shared-backend artifacts only.

The next temporary correction still allowed catalog-domain files to keep a top-level `src/marketplace` feature directory. That allowance is superseded: the client has no marketplace feature folder, although the Redux slice and backend marketplace GraphQL names remain valid domain contracts.

Moving the former combined query from `src/marketplace` into global `src/hooks` was also incorrect. Feature-owned product/category operations supersede that transitional implementation; only the Redux marketplace accessor remains general.

The temporary direct typed `useNavigation` implementation did not supersede the app abstraction and has been removed. Remaining direct React Navigation access is limited to the abstraction implementation and read-only route/navigation-state hooks.

The earlier decision to retain dormant branch and checkout implementation files is superseded. Client branch ownership is removed; only server-side facility resolution remains part of the future architecture.

The earlier direct-ERP-category discovery, same-name merge, and uncategorized product-name fallback are superseded by the marketplace-owned canonical taxonomy. Ordinary organization categories remain internal classification only, not customer-facing category authority.

The protected organization-category projection and ERP assignment implementation are also superseded. Admin-owned Business Product configuration now references ordinary products and canonical marketplace categories directly; ERP categories are internal only. The ChopRoute consumer-app switch is intentionally deferred until that backend/Admin foundation is deployed.

## Confidence

High for the stage-one boundary, reuse of existing marketplace access grants plus ordinary ERP products, marketplace-owned canonical taxonomy, Admin-owned Business Product configuration, confirmed marketplace client identifier, and completed backend/Admin/ERP/SERLP verification. The consumer app still reflects the pre-switch query stage and must be migrated separately.

## Open Questions

- What eligibility inputs beyond distance will future delivery routing use?
- How should multi-organization carts, fees, payments, and order splitting work in their later stage?
- What pickup branch-selection experience will be introduced if pickup is approved?
- When should the backend ChopRoute marketplace name and `CHOPROUTE_MARKETPLACE` client key be migrated to doorDrop identifiers?
- What ranking/configuration should choose Popular order and the four Home category sections?
