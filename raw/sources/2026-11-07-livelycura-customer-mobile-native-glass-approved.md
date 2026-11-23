# LivelyCura customer mobile: native glass tab bar and approved Home top

Date: 2026-11-07
Source: direct user decisions and approval in a `livelycura-customer-mobile` session, plus the code changed and verified in that session (paraphrased).

After the hero fade work, the user asked that the grey strips at the top and bottom of the app be removed. They also asked that the location picker, favourite and profile buttons float while scrolling. They called the first floating version, a solid green bar, rubbish, and chose "floating glass controls": no bar, each control its own glass element over the content. They said the hero background was "too deep" and, asked to clarify, chose both a softer colour and a fade that runs from the search bar to the banner. They later set the hero's top colour back to the brand `primary` themselves.

On glass, the user compared the app with WhatsApp and Telegram in light mode. Those apps' tab bars show a nicer active-tab background that animates to the next tab, and the user asked the app's glass and buttons to follow them. The agent switched to React Navigation's native tab navigator (`createNativeBottomTabNavigator` from `@react-navigation/bottom-tabs/unstable`, on react-native-screens native tabs). That is Apple's UIKit tab bar, with Liquid Glass and the sliding selection on iOS 26, and Material navigation on Android. Icons are SF Symbols on iOS and PNGs rendered from the app's icon fonts on Android. Header controls moved to Apple's clear glass style with dark content. The user replied "Yes, looks right".

Implemented (uncommitted, branch `feature/ui-updates`): tab screens run edge to edge through a per-screen safe-area layout (`screenLayout`); pushed screens keep normal padding. The Home top row is pinned over the page with a soft page-coloured fade under the status bar once the green has scrolled away. The old JS tab bar was deleted. Verified on the iPhone 17 Pro simulator (iOS 26); Android and pre-iOS 26 were not run.
