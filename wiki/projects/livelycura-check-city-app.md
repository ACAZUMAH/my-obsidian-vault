---
type: project
status: active
created: 2026-07-21
updated: 2026-09-21
tags: [project, livelycura, expo, mobile, ordering]
sources:
  - ../sources/checkcity-typescript-tests.md
  - ../sources/checkcity-delivery-location-confirmation.md
  - ../sources/checkcity-order-support-card-layout.md
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/livelycura-project-knowledge-harvest-batch-2.md
  - ../sources/livelycura-project-knowledge-harvest-batch-3.md
  - ../sources/livelycura-project-knowledge-harvest-batch-4.md
  - ../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1.md
confidence: high
---

# LivelyCura CheckCity App

## Summary

Branded Expo ordering application in the LivelyCura family.

## Purpose

Current features support branch selection, menu/category browsing, search, cart and checkout, orders, delivery information, profiles, addresses, banners, and notifications.

## Stack

- Expo SDK 57, React Native 0.81, React 19, TypeScript.
- React Navigation, Apollo Client/GraphQL, Redux Toolkit, persisted state.
- GraphQL Codegen, Prettier, EAS.
- Yarn.

## Architecture

CheckCity implements the organization-owned customer side of [[../concepts/livelycura-customer-support-architecture|LivelyCura Customer Support Architecture]]. Profile and direct-order entry points open organization-scoped tracked cases whose responders work in Pharmacy Portal CRM; custom-app notification routes open only matching case IDs.

`App.tsx` composes the native providers. `src/navigation` owns stacks/tabs. Features live directly under `src` with local components, hooks, helpers, constants, and interfaces. `src/motion` owns reusable Reanimated interaction primitives; `src/theme` coordinates theme preference and background-transition origin; `src/components/background-decor` owns reusable background presentation across screens and modals.

The accepted bottom navigation keeps Menu, Search, and Orders in one track with Cart as a detached action. Profile/More is not a tab; profile access is deliberately owned by Menu, Cart, and Orders header paths. Shared floating headers default to no profile action and callers opt in.

## Folder Ownership

- `menu`, `menuItem`, `categories`, `search`: discovery.
- `cart`, `order`, `orders`: purchase lifecycle.
- `branch`, `addresses`, `profile`, `login`: customer context.
- `apollo`, `redux`, `navigation`, `theme`, `system`: shared runtime.
- `motion`: reduced-motion-aware screen entry and depth-press primitives.
- `banner`: assigned-app banner query, carousel presentation, CTA handling, and impression/click tracking.

## Commands

- `yarn start`, `yarn ios`, `yarn android`, `yarn web`
- `yarn generate`
- `yarn type-check`
- `yarn format:check`

## Runtime/Deployment

Expo/EAS application with preview and production GitHub workflows.

## Durable Conventions

- Write Cart tests in TypeScript (`.test.ts`, or `.test.tsx` for JSX), with typed mocks/fixtures and valid imports after moves. See [[../sources/checkcity-typescript-tests|the direct TypeScript test correction]].

- Confirm unusually distant or expensive delivery locations after the current estimate completes. Show destination, branch, approximate distance, and fee; require explicit acceptance and invalidate it when location, branch, or fee changes. Require both GH₵60+ and at least 15 km before warning (September 21 correction; 15 km is the interpreted start of the user’s 15–20 km range). A 10.2 km / GH₵41 estimate must not warn. Allow continuation after confirmation, including beyond 20 km; the latest warning-only correction supersedes the earlier hard cap. See [[../sources/checkcity-delivery-location-confirmation|the delivery confirmation requirement]].

- Keep one reusable support conversation per order inside the existing `OrderDetailHelpCard`, separated from the Help heading with a divider. Show opened and closed states; closed chats stay visible and can be reopened. Do not offer new-chat creation when a conversation exists. See [[../sources/checkcity-order-support-card-layout|the layout and lifecycle requirements]].

- Use the shared `Conditional` component for support-screen rendering branches; nullable data access must remain safe because child expressions evaluate before the condition. See [[../sources/checkcity-order-support-card-layout|the support rendering correction]].

- Keep feature code split into owned files and folders; do not implement an entire screen/domain in one file.
- Reorder actions should visually reuse the established cart “Place order” interaction.
- The order view exposes the delivery OTP and push-notification behavior where the backend contract supports them.
- Prefer restrained reusable motion on the existing Reanimated stack; do not add 3D/native-graphics dependencies for ordinary depth, entry, or theme interactions.
- Honor the platform reduce-motion preference in shared motion and decorative animation.
- Theme changes animate the background/decor behind content from the control origin. Never cover the interface with a temporary white/dark theme sheet.
- Menu and Search header controls share the same centered width and outer gutter as their screen bodies.
- Banner loading, error, or empty states stay quiet. Query with the CheckCity app identity plus relevant organization/facility/platform context, then record impressions and clicks through focused hooks.
- Optional native capabilities must not crash startup when unlinked. The in-app-update path uses a dynamic import, and native service config is emitted only when the active variant resolves a file.
- Expo Go is a required acceptance path for customer-app work that does not inherently require a custom native build. Guard optional native modules before module evaluation, exercise JavaScript eligibility logic in Expo Go without invoking host-app-native actions, and do not call the work complete until a cleared-cache Expo Go launch reaches the affected flow without a native-module runtime error.
- App-rating eligibility begins after any successfully created order, regardless of whether fulfillment is pickup or delivery. Trigger only from the checkout-created order path, not from delivery completion or ordinary order-history views; retain the per-user persisted attempt guard and skip the native host-app action in Expo Go.
- Customer feedback is not a separate product surface because it overlaps customer support. Do not restore a dedicated feedback route, profile action, order action, or backend feedback resource unless that product boundary is explicitly reconsidered.
- Keep swipe gesture behavior in a focused hook, show the discoverability hint without trapping the row, support full-swipe removal, and honor reduced motion.
- Preserve active bottom-tab width by compacting inactive items rather than squeezing the active item.
- Keep inactive Cart visually inactive, expand/fill the full active tab surface without an inset gap, and position the detached Cart badge outside the action surface so it remains visible.
- Keep the Menu branch selector floating/transparent at the top; while scrolling, only the selector surface gains themed background and elevation.
- Keep floating-header lists full-screen so content scrolls beneath the header. Disable automatic inset adjustment and use explicit safe-area content insets/offsets plus themed refresh offsets so pull-to-refresh remains visible outside notches and dynamic islands after a full reload.
- Shared presentation components accept caller-owned layout style where context differs. `CategoryFilter` does not impose one bottom margin: Menu adds spacing while Search supplies none.
- Bottom-sheet decorations stay behind a foreground layer. On Android, full-screen dimensions and translucent status/navigation bars prevent the sheet from leaving a system-bar gap; theme-derived text colors preserve light/dark readability.
- Product descriptions use the shared “Freshly prepared and ready to serve.” fallback when API text is missing or blank.
- Device location and fulfilling branch are session-fresh state, not durable customer selections. On cold launch and every return from background/inactive state, resolve the current GPS position, replace the delivery location, and select the nearest branch before checkout can submit. Never fall back to a persisted address, persisted branch, or arbitrary first branch when location refresh fails; clear stale state and block ordering until a fresh location succeeds.

## Constraints

- The curated six-product menu ordering is temporary, frontend-only, and limited to the home Menu grid. Search and recent orders retain API order.
- The temporary rule preserves unmatched products and does not mutate the input array.
- Theme transitions must keep content readable and interactive throughout; the reveal layer is background-only.
- System theme requires native automatic appearance and `expo-system-ui`; after changing this native configuration, build a new native binary rather than relying on JavaScript reload.
- Live Activities are not present on the active branch. Do not treat the deferred branch snapshot as production-ready.
- Current `MenuLoader` is a three-item horizontal loader. Do not restore the historical six-item grid instruction without a new visual decision.

## Decisions And Rationale

The temporary home ordering reflects a small production menu: category priority within descending configured price bands. It is explicitly a bridge until a general backend ordering capability exists.

Shared motion uses small vertical/scale/depth changes rather than theatrical effects. The current background theme reveal lasts 950 ms with softened easing, while reduced-motion users receive the final state without the reveal.

Order Live Activities and Android progress notifications were intentionally isolated on a local `feature/live-activities` branch so unrelated cart/profile/navigation changes could remain on the active branch. When resumed, the app should use Software Mansion’s maintained Expo Live Activity package instead of preserving the branch’s earlier custom local module.

A short-lived structured-feedback implementation was removed after product review because feedback and customer support served the same user need. Customer-support work should own the eventual contact/intake experience instead of maintaining a parallel feedback domain.

App ratings belong to the successful order-creation milestone rather than the delivery lifecycle. Pickup customers must be eligible too, so delivery-status checks and completed-delivery counts must not gate the native review attempt. Ordinary historical order-detail navigation must not masquerade as a newly created order.

## Verification Expectations

Run GraphQL generation after schema changes, then TypeScript, tests, and formatting checks. For Expo-compatible changes, clear Metro's cache and launch the real app in Expo Go; verify the affected navigation and data flows, optional-native-module absence, and that native-only behavior is skipped without falsely recording success. Exercise the relevant native platform, logout/login restoration, order/reorder flow, cart swipe/removal, delivery OTP, banners/analytics, categories, notification registration, and system/manual themes. Native configuration changes require a development/release rebuild. For visual changes, compare both themes, reduced-motion behavior, decorated screens/modals, Android system-bar coverage, checkout total clearance, Menu/Search/Orders refresh controls after cold reload, floating-header under-scroll, caller-specific category spacing, and tab labels/active width on narrow and far-end selections.

## Evidence

- Current package, app entry, feature folders, EAS configuration, and workflows.
- Session `019f56a3…` in [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Session `019e28e5…` in [[../sources/livelycura-project-knowledge-harvest-batch-2|LivelyCura Project Knowledge Harvest — Batch 2]].
- Sessions `019e191c…`, `019e02a9…`, `019e0007…`, `019dffe9…`, and `019dfea2…` in [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].
- Sessions `019de5bd…` and `019dda04…` plus current decoration/modal/list/category/tab source in [[../sources/livelycura-project-knowledge-harvest-batch-4|LivelyCura Project Knowledge Harvest — Batch 4]].
- Direct Hermes session `20260707_234259_178721` in [[../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1|CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1]] establishes the final track/detached-cart layout, profile placement, branch-selector scroll treatment, feature-file separation, and historically reported iOS bundle/format verification.
- Direct user correction on 2026-08-29 establishes Expo Go as a mandatory completion path; the same run verified a cleared-cache iOS Expo Go bundle, active/completed delivery-order states, and suppression of the native store-review action in the Expo Go host.
- Direct user correction on 2026-08-30 establishes successful creation of any order, including pickup, as the app-rating trigger and supersedes delivery-completion/count eligibility.
- Direct user correction on 2026-09-01 establishes that CheckCity must refresh the device location and nearest branch after every cold launch and foreground return, and that stale persisted location/branch state must never remain orderable after a failed refresh.

## Contradictions

The README contains only the repository name. Purpose is inferred from current code and the processed order/menu sessions. Historical theme attempts briefly used a full-screen reveal cover; the latest correction and current code use background-only decor animation. The deferred Live Activities branch still contains the superseded custom-module approach, while the latest explicit package direction is external and the active branch contains no Live Activity implementation. Historical store artwork was moved outside the repository and is not asserted to exist now. The BackgroundDecoration session ended with a six-item grid loader correction, but current `MenuLoader` is horizontal with three placeholders; current code outranks that intermediate layout.

The Hermes tab session briefly introduced More/Profile and notification-bell variants before explicitly removing them. Current four-route registration and header profile ownership are authoritative. Notification registration now exists elsewhere, so the session-era unavailable-backend explanation is historical only.

The dedicated customer-feedback app/backend implementation was verified and then removed on 2026-08-29 after the product decision that it duplicated customer support. Current source and the removal decision are authoritative.

## Confidence

High for stack, current feature ownership, banners, tab/cart/theme behavior, and the deferred Live Activities state; medium for the broader product description.

## Open Questions

- When will curated menu ordering move to a backend-configurable policy?
- Which push-notification registration paths are verified on current iOS and Android builds?
- Which deferred Live Activity files remain useful after replacing the custom module with the maintained package?
