---
type: source
status: active
created: 2026-11-07
updated: 2026-11-08
tags: [livelycura, customer-mobile, design, liquid-glass, home, conventions]
sources:
  - ../../raw/sources/2026-11-07-livelycura-customer-mobile-glass-home-direction.md
  - ../../raw/sources/2026-11-07-livelycura-customer-mobile-home-header-correction.md
  - ../../raw/sources/2026-11-07-livelycura-customer-mobile-hero-fade-clarification.md
  - ../../raw/sources/2026-11-07-livelycura-customer-mobile-native-glass-approved.md
  - ../../raw/sources/2026-11-08-livelycura-customer-mobile-pushed-screen-headers.md
  - ../../raw/sources/2026-11-08-livelycura-customer-mobile-profile-title.md
  - ../../raw/sources/2026-11-08-livelycura-customer-mobile-cart-button-cover.md
  - ../../raw/sources/2026-11-08-livelycura-customer-mobile-dark-mode-and-drawn-tab-bar.md
source_date: 2026-11-07
ingested: 2026-11-07
confidence: high
---

# LivelyCura Customer Mobile Glass Home Direction

## Source

- Raw file: [LivelyCura customer mobile: glass Home redesign direction](../../raw/sources/2026-11-07-livelycura-customer-mobile-glass-home-direction.md)
- Raw file: [LivelyCura customer mobile: Home header follows the inspo layout](../../raw/sources/2026-11-07-livelycura-customer-mobile-home-header-correction.md)
- Raw file: [LivelyCura customer mobile: Home hero fades into the banner](../../raw/sources/2026-11-07-livelycura-customer-mobile-hero-fade-clarification.md)
- Raw file: [LivelyCura customer mobile: native glass tab bar and approved Home top](../../raw/sources/2026-11-07-livelycura-customer-mobile-native-glass-approved.md)
- Raw file: [LivelyCura customer mobile: pushed-screen headers and inspo as reference](../../raw/sources/2026-11-08-livelycura-customer-mobile-pushed-screen-headers.md)
- Raw file: [LivelyCura customer mobile: Profile gets a centred title](../../raw/sources/2026-11-08-livelycura-customer-mobile-profile-title.md)
- Raw file: [LivelyCura customer mobile: cart button in the tab bar opens a cover](../../raw/sources/2026-11-08-livelycura-customer-mobile-cart-button-cover.md)
- Raw file: [LivelyCura customer mobile: dark mode and one tab bar design everywhere](../../raw/sources/2026-11-08-livelycura-customer-mobile-dark-mode-and-drawn-tab-bar.md)
- Date: 2026-11-07 to 2026-11-08
- Author: The user (decisions and approval, paraphrased) and the implementing session
- Ingested: 2026-11-07

## Core Claims

- The tab bar is the platform's own, via React Navigation's native tab navigator (`@react-navigation/bottom-tabs/unstable`). iOS 26 gets Liquid Glass with the sliding selection, matching WhatsApp and Telegram; Android gets Material bottom navigation. It must not be rebuilt in JS. The user approved this ("Yes, looks right").
- Other iOS controls (location pill, header buttons, search and filter) use Apple's clear Liquid Glass with dark text and icons. Content cards, including the Home banner, stay solid. Older iOS gets a translucent fallback; Android does not blur.
- Home top follows the inspo: delivery-address pill left, Favourites, Notifications and Profile right, search below, no greeting. The green (brand `primary` to a softer `#86E3BD`) runs behind the status bar, starts fading at the search bar and is gone by the top of the banner.
- That top row floats while scrolling with no bar behind it; a soft page-coloured fade sits under the status bar once the green has scrolled away. The user rejected a solid green pinned bar.
- Tab screens run edge to edge, under the status bar and the tab bar; pushed screens keep normal safe-area padding.
- The customer app will support light and dark mode; light mode is built first, dark mode next.
- The Home banner slot holds the support card until marketing banners exist; banners replace it in place.
- Home keeps a "Recommended" row (newest live products, no recommendation data exists) ahead of the per-category product carousels.
- Android and iOS older than 26.1 keep the same tab bar design as iOS 26 (floating capsule, sliding selection, separate round cart button), drawn on solid surfaces instead of glass, as Telegram does; the user asked for this. iOS 26.1+ keeps the native bar.
- Dark mode is iOS-style (black page, `#1C1C1E` cards). Profile's Appearance offers Light, Dark and System default, and new installs follow the phone. Visual approval of dark mode was still pending in the source session.
- The cart is the native tab bar's separate round button with a full count badge; it never becomes the selected tab. Tapping it grows the cart out of the button into a full-screen cover over everything, tab bar included, and its close button shrinks it back, like Telegram's iOS 26 search; the open takes about 0.7 s. "View cart" opens the same cover, and there is no floating cart bubble. The user corrected a first version that opened the cart as a normal tab, then approved this one.
- Pushed screens never put a title or subtitle under the back button. A title, if any, sits centred on the same row as the glass back button, and that row stays pinned while the page scrolls. Profile, Account and New address all have a centred title there; the user asked for Profile's after first leaving it untitled. The user set this rule after removing stacked titles themselves.
- An inspo image is a style reference, not a template. On Profile the user rejected copying its grouping and colours: Sign out and Delete Account get their own group, and settings tiles are brand green with red only for those two.
- The repo's `PRODUCT.md` records this direction and no longer lists glassmorphism as an anti-reference.

## Useful Details

- Shared glass component: `src/components/glass/GlassSurface` (props `tone`, `glassStyle` regular or clear, `tintColor`, `interactive`).
- Tab icons: SF Symbols on iOS; PNGs in `assets/tabs` rendered from the app's Ionicons and MaterialCommunityIcons fonts for Android.
- Pushed-screen header: `BackTitleRow` and `FloatingBackBar` (with `title`) in `src/components/floating-back-bar`.
- Cart cover: the search slot on iOS 26.1 to 26.x with `tabBarSelectionEnabled: false` (superseded for iOS 27+ on 2026-11-13: the cart is a normal tab there, see [[livelycura-customer-mobile-ios27-cart-glass-scenes|iOS 27 Cart, Glass And Scene Startup]]); the press pushes a transparent-modal `cart` route animated by `src/cart/hooks/useCartCover.ts`. iOS clips native badges on that button, so `src/navigation/components/CartButtonBadge.tsx` draws the count.
- Edge-to-edge is done with navigator `screenLayout`: the stack wraps every screen except the tab navigator in `SafeAreaInsets`; the tab navigator wraps non-Home tabs in a top-only `TopSafeArea`.

## Connections

- [[../projects/livelycura-customer-mobile|LivelyCura Customer Mobile]] carries the conventions.
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]] (LivelyCura Family).

## Contradictions Or Tensions

- Supersedes the earlier repo `PRODUCT.md` anti-reference to glassmorphism.
- The native tab navigator is in React Navigation's "unstable" entry point, so its API may change in later versions.

## Open Questions

- Android and pre-iOS 26 were not run on devices in the source sessions.
