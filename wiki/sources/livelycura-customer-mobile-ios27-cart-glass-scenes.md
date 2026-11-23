---
type: source
status: active
created: 2026-11-13
updated: 2026-11-13
tags: [livelycura, customer-mobile, ios, ios-27, liquid-glass, accessibility, expo, scene-lifecycle]
sources:
  - ../../raw/sources/2026-11-13-livelycura-customer-mobile-ios27-cart-glass-scenes.md
source_date: 2026-11-13
ingested: 2026-11-13
confidence: high
---

# LivelyCura Customer Mobile iOS 27 Cart, Glass And Scene Startup

## Source

- Raw file: [LivelyCura customer mobile: iOS 27 cart tab, Reduce Transparency glass, and scene startup](../../raw/sources/2026-11-13-livelycura-customer-mobile-ios27-cart-glass-scenes.md)
- Date: 2026-11-13
- Author: The owner (requests and decisions, paraphrased) and the implementing session
- Ingested: 2026-11-13

## Core Claims

- iOS 27 has no separate round tab bar button, so on iOS 27+ the cart is a normal tab (native badge, checkout tray above the bar, "View cart" switches to it). iOS 26.1 to 26.x keeps the round button and the grow-out cover; Android and older iOS keep the drawn bar.
- With iOS Reduce Transparency on, glass controls show their solid fallback instead of Apple's grey glass, which looked muddy over the brand green; the native tab bar is left to iOS.
- The app adopts the UIScene life cycle through `expo-build-properties` `ios.enableSceneSupport: true` (Expo SDK 57), because Xcode 27 builds otherwise fail to launch on iOS 27.

## Useful Details

- Files: `src/cart/CartTab.tsx`, `src/cart/components/CartBody.tsx` (shared by cover and tab), `src/navigation/helpers` (`usesNativeTabBar`, `cartIsTab`, `cartTabRole`), `src/components/glass/reduceTransparency.ts` and `useReduceTransparency.ts`.
- Scene startup uses Expo's built-in `EXExpoAppSceneDelegate`; no app SceneDelegate file. Remove the property after upgrading to Expo SDK 58, which has it built in.
- The generated `ios/` folder is not in git; prebuild regenerates it. In an agent shell, `pod install` needs `LANG`/`LC_ALL` set to UTF-8, and prebuild rewrites `.xcode.env.local` with the shell's Node path.
- The iOS 27 simulator runtime (8.3 GB) was installed for testing; Xcode 27.2 is on the Mac.
- Commits on `feature/ui-updates`: e35ad8b (cancel), f5882d6 (glass), 9a7cd42 (cart tab), 3ab557b (scenes); not pushed.

## Connections

- [[livelycura-customer-mobile-glass-home-direction|LivelyCura Customer Mobile Glass Home Direction]] holds the original cart-cover and glass decisions this refines.
- [[../projects/livelycura-customer-mobile|LivelyCura Customer Mobile]] carries the conventions.

## Contradictions Or Tensions

- Supersedes the earlier plan to use the "prominent" tab role on iOS 27: iOS 27 shows it inside the bar, so the cart became a normal tab there.
- The iOS "Tinted" Liquid Glass option looks like Reduce Transparency but, as far as known, apps cannot detect it, so it is not covered.

## Open Questions

- Not yet checked on a real iPhone (iOS 26.x with Reduce Transparency, iOS 27).
- A development-only "JUMP_TO was not handled" warning at startup comes from `src/navigation/stack.tsx` switching to Home before the tabs exist; left as is.
