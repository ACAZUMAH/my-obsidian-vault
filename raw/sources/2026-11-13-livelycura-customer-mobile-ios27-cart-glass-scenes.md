# LivelyCura customer mobile: iOS 27 cart tab, Reduce Transparency glass, and scene startup

Date: 2026-11-13
Source: the owner's requests and decisions in a Claude Code session on `livelycura-customer-mobile` (paraphrased; quoted phrases are the owner's own words), plus the code built and checked there. Committed on `feature/ui-updates` as e35ad8b, f5882d6, 9a7cd42 and 3ab557b, not pushed.

## Requests and decisions

- The owner reported that iOS 27 removed the separate ("stand alone") tab bar button: only iOS versions with that button should get the animated cart cover, and on iOS 27+ the cart should open "normally like the rest of the screens". The owner chose a normal tab over a pushed page.
- The owner reported that a phone on iOS 26.5.2 showed grey header controls in light mode only. The session reproduced it on the simulator with Reduce Transparency on, which matched the screenshot exactly. The owner approved the fix.
- Testing on the iOS 27.2 simulator showed the app built with Xcode 27 crashes at launch (`UIApplicationEvaluateRuntimeIssueForNoSceneLifecycleAdoption`). The owner asked to look into it ("Yes, look into it") and then to apply the fix ("Yes, apply it"), then to commit ("Yes, commit them").

## What was built

- **Cart (iOS 27+):** a normal tab (`src/cart/CartTab.tsx`) with a native badge, the shared tab header, and the checkout tray above the tab bar; "View cart" pops to the tabs and opens it; the floating orders card hides on that tab. iOS 26.1 to 26.x keeps the search-slot round button and the cover; Android and older iOS keep the drawn bar. The cover and the tab share `src/cart/components/CartBody.tsx`. The earlier "prominent" role for iOS 27 was dropped.
- **Reduce Transparency:** `GlassSurface` shows its solid fallback (the Android look) while iOS Reduce Transparency is on, following the setting live through one shared listener (`src/components/glass/reduceTransparency.ts`). Apple's own tab bar is left as is. The iOS "Tinted" Liquid Glass option looks similar but, as far as known, apps cannot detect it.
- **Scene startup:** `expo-build-properties` ~57.0.23 with `ios.enableSceneSupport: true` in `app.json`. Prebuild then declares a single-scene `UIApplicationSceneManifest` using Expo's built-in `EXExpoAppSceneDelegate` and removes window creation from `AppDelegate`. Expo's scene forwarder dedupes links the AppDelegate already passed to `RCTLinkingManager`. Expo SDK 58 makes this the default; the property can be removed then.
- **Also committed:** the shopper cancel fix (the sheet called the pharmacy's `cancelOrder`; it now calls `cancelMarketplaceOrder(id, data)` with an optional reason).

## Why the scene change matters

Apps built with the iOS 27 SDK must adopt the scene life cycle or they fail to launch on iOS 27. Cloud builds still used an older SDK, so existing iOS 27 users were unaffected, but App Store uploads will require the iOS 27 SDK from April 2027.

## Verification at recording

Type check passed. On the iOS 27.2 simulator: launch, warm and cold links, the Cart tab with badge and tray. On the iOS 26.5 simulator: Reduce Transparency on and off in light and dark, the round button cover, "View cart", the empty cart, and links. Not checked on a real phone.
