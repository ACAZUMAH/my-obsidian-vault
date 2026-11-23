# LivelyCura customer mobile: glass Home redesign direction

Date: 2026-11-07
Source: direct user decisions in a `livelycura-customer-mobile` session, plus the code changed and verified in that session (paraphrased).

The user supplied a pharmacy-app Home inspiration (green header with greeting, avatar and icon buttons; search bar with filter button; promo banner; circular category chips; product recommendation row; bottom tab bar) and asked to change the whole Home screen to that style. They asked for "ios glassmorphism ui" on iOS and something nice of its own on Android. They said marketing banners will come later, so the support ("Can we help?") card goes where the banner belongs until a banner replaces it. They said the app will now use light mode and dark mode, with light mode built first and dark mode next.

The agent pointed out that the repo's `PRODUCT.md` listed glassmorphism as an anti-reference. It recommended Liquid Glass on the controls layer only, with content cards staying solid. The user chose all three recommended options: restyle the shared bottom tab bar now as a floating glass bar; put a "Recommended" row (newest live products, since there is no recommendation or rating data) ahead of per-category carousels, keeping the per-category rows; and update `PRODUCT.md` to the new direction.

Implemented (uncommitted, branch `feature/ui-updates`): `expo-glass-effect` and `expo-linear-gradient` added; `src/components/glass/GlassSurface` renders `GlassView` on iOS 26+ (deep-green tint over the brand green so white text stays legible), a translucent fallback on older iOS, and solid white surfaces with elevation on Android. Home has a gradient header (`primary` to `#00A86B`) behind the status bar, greeting, delivery-address chip, glass search and filter, the support card as the banner, category chips, Recommended and category carousels. `SafeAreaInsets` gained per-screen top and bottom strip colors so the header and floating tab bar can run edge to edge. Verified on the iPhone 17 Pro simulator (iOS 26); Android and older iOS were not run.

Earlier the same day the agent moved the app to Expo SDK 57 patch versions (staying on SDK 57 at the user's choice) and built an in-app animated launch splash.
