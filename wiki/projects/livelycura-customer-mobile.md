---
type: project
status: active
created: 2026-07-21
updated: 2026-11-13
tags: [project, livelycura, expo, customer, mobile]
sources:
  - ../sources/livelycura-project-knowledge-harvest-batch-1.md
  - ../sources/livelycura-customer-mobile-glass-home-direction.md
  - ../sources/livelycura-customer-mobile-ios27-cart-glass-scenes.md
confidence: medium
---

# LivelyCura Customer Mobile

## Summary

Customer-facing Expo application for LivelyCura shopping and care journeys.

## Purpose

Current feature ownership includes home/product discovery, categories, favorites, cart/checkout, orders, prescriptions, care access, loyalty, profile, addresses, walkthrough, and notifications.

## Stack

- Expo SDK 57, React Native 0.86, React 19, TypeScript (moved from SDK 54 on `develop`; the user chose to stay on SDK 57 rather than SDK 58 on 2026-11-07).
- React Navigation, Apollo Client/GraphQL, Redux Toolkit.
- GraphQL Codegen, persistent client state, EAS.
- Yarn.

## Architecture

The tracked support center implements the marketplace-mobile side of [[../concepts/livelycura-customer-support-architecture|LivelyCura Customer Support Architecture]], with Profile/Get Care/order entry points, private image attachments, foreground polling, unread state, and strict support-notification navigation.

`App.tsx` composes native providers. `src/navigation` owns route structure. Customer domains live directly under `src`; shared infrastructure remains in `apollo`, `redux`, `theme`, `system`, `components`, `hooks`, and `helpers`.

## Folder Ownership

- `home`, `products`, `productDetails`, `categories`, `favorites`: discovery.
- `cart`, `checkout`, `orders`, `orderDetails`: commerce.
- `prescriptions`, `prescriptionDetails`, `get-care`: health/care.
- `login`, `profile`, `addresses`, `loyalty`, `notifications`: customer identity and engagement.

## Commands

- `yarn start`, `yarn ios`, `yarn android`, `yarn web`
- `yarn generate`
- `yarn type-check`
- `yarn format:check`

## Runtime/Deployment

Expo/EAS application with CI, preview, and production GitHub workflows.

## Durable Conventions

- Follow the family React Navigation and feature-owned mobile architecture.
- Keep Apollo server state, Redux application/session state, and local screen state deliberately separate.
- Preserve native safe-area, status-bar, and theme behavior.
- Visual direction (user decisions, approved 2026-11-07): the tab bar is the platform's native one (`@react-navigation/bottom-tabs/unstable`; Liquid Glass with the sliding selection on iOS 26, Material on Android), not a JS rebuild. Other iOS controls use clear Liquid Glass through `src/components/glass/GlassSurface` with dark content; content cards stay solid; Android gets no blur. Tab screens run edge to edge. The repo `PRODUCT.md` records this. See [[../sources/livelycura-customer-mobile-glass-home-direction|Glass Home Direction]].
- Android and older iOS (below 26.1) get a drawn tab bar matching the iOS 26 layout on solid surfaces, like Telegram (user request, 2026-11-08). Dark mode follows the phone by default, with an in-app Light/Dark/System choice on Profile.
- The cart is the tab bar's separate round button (full count badge); tapping it grows a full-screen cart cover out of the button, covering the tab bar, and closing shrinks it back, like Telegram's search (approved 2026-11-08). No floating cart bubble.
- iOS versions (2026-11-13): the cart is the round tab bar button with a grow-out cover only on iOS 26.1 to 26.x; on iOS 27+ it is a normal tab. With iOS Reduce Transparency on, glass controls show their solid fallback. The app adopts the UIScene life cycle via `expo-build-properties` `ios.enableSceneSupport` (Xcode 27 builds fail to launch on iOS 27 without it; remove after Expo SDK 58). See [[../sources/livelycura-customer-mobile-ios27-cart-glass-scenes|iOS 27 Cart, Glass And Scene Startup]].
- Pushed screens never put a title under the back button: a title, if any, sits centred on the same row as the glass back button (`src/components/floating-back-bar`); Profile, Account and New address use it. Inspo images are style references, not templates (user corrections, 2026-11-08).
- The Home banner slot holds the support card until marketing banners exist; banners replace it in place.

## Constraints

- No processed batch-1 session establishes a customer-mobile-specific product correction; current code is the primary evidence.

## Decisions And Rationale

The independent repository keeps consumer shopping/care interaction separate from ERP operations and workforce/courier apps.

## Verification Expectations

Run codegen, type check, formatting, and the intended native platform. Exercise authentication persistence, navigation, cart/checkout, order state, prescriptions, and notification behavior when touched.

## Evidence

- Current package, source layout, EAS configuration, and GitHub workflows.
- [[../sources/livelycura-project-knowledge-harvest-batch-1|LivelyCura Project Knowledge Harvest — Batch 1]].
- [[../sources/livelycura-customer-mobile-glass-home-direction|LivelyCura Customer Mobile Glass Home Direction]].
- [[../sources/livelycura-customer-mobile-ios27-cart-glass-scenes|LivelyCura Customer Mobile iOS 27 Cart, Glass And Scene Startup]].

## Contradictions

There is no root README, so purpose is inferred from live folders and routes.

## Confidence

High for stack and current folder ownership; medium for broader domain wording and historical rationale.

## Open Questions

- Which older Codex sessions contain the latest customer-mobile-specific interaction rules?
- Is secure laboratory-result history intentionally web-only or planned for this app later?
- Is dark mode chosen by an in-app setting, the system appearance, or both? (`settings.darkMode` has no toggle yet and `userInterfaceStyle` is `light`.)
