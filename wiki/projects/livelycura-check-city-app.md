---
type: project
status: active
created: 2026-07-21
updated: 2026-07-21
tags: [project, livelycura, expo, mobile, ordering]
sources:
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

- Expo SDK 54, React Native 0.81, React 19, TypeScript.
- React Navigation, Apollo Client/GraphQL, Redux Toolkit, persisted state.
- GraphQL Codegen, Prettier, EAS.
- Yarn.

## Architecture

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

- Keep feature code split into owned files and folders; do not implement an entire screen/domain in one file.
- Reorder actions should visually reuse the established cart “Place order” interaction.
- The order view exposes the delivery OTP and push-notification behavior where the backend contract supports them.
- Prefer restrained reusable motion on the existing Reanimated stack; do not add 3D/native-graphics dependencies for ordinary depth, entry, or theme interactions.
- Honor the platform reduce-motion preference in shared motion and decorative animation.
- Theme changes animate the background/decor behind content from the control origin. Never cover the interface with a temporary white/dark theme sheet.
- Menu and Search header controls share the same centered width and outer gutter as their screen bodies.
- Banner loading, error, or empty states stay quiet. Query with the CheckCity app identity plus relevant organization/facility/platform context, then record impressions and clicks through focused hooks.
- Optional native capabilities must not crash startup when unlinked. The in-app-update path uses a dynamic import, and native service config is emitted only when the active variant resolves a file.
- Keep swipe gesture behavior in a focused hook, show the discoverability hint without trapping the row, support full-swipe removal, and honor reduced motion.
- Preserve active bottom-tab width by compacting inactive items rather than squeezing the active item.
- Keep inactive Cart visually inactive, expand/fill the full active tab surface without an inset gap, and position the detached Cart badge outside the action surface so it remains visible.
- Keep the Menu branch selector floating/transparent at the top; while scrolling, only the selector surface gains themed background and elevation.
- Keep floating-header lists full-screen so content scrolls beneath the header. Disable automatic inset adjustment and use explicit safe-area content insets/offsets plus themed refresh offsets so pull-to-refresh remains visible outside notches and dynamic islands after a full reload.
- Shared presentation components accept caller-owned layout style where context differs. `CategoryFilter` does not impose one bottom margin: Menu adds spacing while Search supplies none.
- Bottom-sheet decorations stay behind a foreground layer. On Android, full-screen dimensions and translucent status/navigation bars prevent the sheet from leaving a system-bar gap; theme-derived text colors preserve light/dark readability.
- Product descriptions use the shared “Freshly prepared and ready to serve.” fallback when API text is missing or blank.

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

## Verification Expectations

Run GraphQL generation after schema changes, then TypeScript and formatting checks. Exercise the relevant native platform, logout/login restoration, order/reorder flow, cart swipe/removal, delivery OTP, banners/analytics, categories, notification registration, optional update-module absence, and system/manual themes. Native configuration changes require a development/release rebuild. For visual changes, compare both themes, reduced-motion behavior, decorated screens/modals, Android system-bar coverage, checkout total clearance, Menu/Search/Orders refresh controls after cold reload, floating-header under-scroll, caller-specific category spacing, and tab labels/active width on narrow and far-end selections.

## Evidence

- Current package, app entry, feature folders, EAS configuration, and workflows.
- Session `019f56a3…` in [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- Session `019e28e5…` in [[../sources/livelycura-project-knowledge-harvest-batch-2|LivelyCura Project Knowledge Harvest — Batch 2]].
- Sessions `019e191c…`, `019e02a9…`, `019e0007…`, `019dffe9…`, and `019dfea2…` in [[../sources/livelycura-project-knowledge-harvest-batch-3|LivelyCura Project Knowledge Harvest — Batch 3]].
- Sessions `019de5bd…` and `019dda04…` plus current decoration/modal/list/category/tab source in [[../sources/livelycura-project-knowledge-harvest-batch-4|LivelyCura Project Knowledge Harvest — Batch 4]].
- Direct Hermes session `20260707_234259_178721` in [[../sources/compflow-checkcity-hermes-conversation-harvest-supplement-1|CompFlow And CheckCity Hermes Conversation Harvest — Supplement 1]] establishes the final track/detached-cart layout, profile placement, branch-selector scroll treatment, feature-file separation, and historically reported iOS bundle/format verification.

## Contradictions

The README contains only the repository name. Purpose is inferred from current code and the processed order/menu sessions. Historical theme attempts briefly used a full-screen reveal cover; the latest correction and current code use background-only decor animation. The deferred Live Activities branch still contains the superseded custom-module approach, while the latest explicit package direction is external and the active branch contains no Live Activity implementation. Historical store artwork was moved outside the repository and is not asserted to exist now. The BackgroundDecoration session ended with a six-item grid loader correction, but current `MenuLoader` is horizontal with three placeholders; current code outranks that intermediate layout.

The Hermes tab session briefly introduced More/Profile and notification-bell variants before explicitly removing them. Current four-route registration and header profile ownership are authoritative. Notification registration now exists elsewhere, so the session-era unavailable-backend explanation is historical only.

## Confidence

High for stack, current feature ownership, banners, tab/cart/theme behavior, and the deferred Live Activities state; medium for the broader product description.

## Open Questions

- When will curated menu ordering move to a backend-configurable policy?
- Which push-notification registration paths are verified on current iOS and Android builds?
- Which deferred Live Activity files remain useful after replacing the custom module with the maintained package?
