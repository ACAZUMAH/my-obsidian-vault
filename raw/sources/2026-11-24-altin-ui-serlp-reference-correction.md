# Altin Partner Mobile: UI follows SERLP Mobile, not decorative glass

- Date: 2026-11-24
- Author: the user, through an Altin Partner Mobile Claude Code session
- Repository: `altin-partner-mobile`, branch `feature/apps`, uncommitted when recorded
- Repository records: `DESIGN.md` "Glass controls and header fades", the `AGENTS.md` theme bullet "UI reference is SERLP Mobile"

## The user's corrections (verbatim, 2026-11-24)

After the 2026-11-23 glassmorphism pass:

> wrong you know how I updated uis on livelycura and what you did isn't looking anything like it, and that of how background is to I don't how you mix red and black, and red and white for light and dark mode, you have to know is a business app, we don't to play about it

The session then studied `livelycura-customer-mobile` (Liquid Glass on controls only, solid content) and started a second pass. Partway through, the user interrupted:

> OMG, check the serlp mobile, you still doing most of the things wrongly. improve ui and you and you are making it worse

## What the session did

- Reverted the whole 2026-11-23 pass (red ambient glows behind every screen, see-through cards, `expo-blur` bars, frosted sheets and drawer) to the committed look, keeping only the login title typo fix. The rejected work was saved outside the repository as a patch.
- Opened SERLP Mobile (`LivelyCura/serlp-mobile`, signed in on the same simulator) and compared it screen by screen in light and dark, read-only; its dark-mode setting was flipped to inspect light mode and flipped back.
- SERLP's look: iOS grouped surfaces (light `#F2F2F7` page with white cards, dark black page with `#1C1C1E` cards), Apple's Liquid Glass only on floating controls (clear glass, a faint `0 1px 3px rgba(0,0,0,0.08)` shadow in light), every header a solid page-coloured band with a 24pt fade below it, uppercase section labels, and the native iOS 26 tab bar.
- Rebuilt Altin to that model with Altin's own palette: light page `cloud` `#F6F7F8` with white cards (dark unchanged), `expo-glass-effect` `GlassSurface`/`GlassButton` on the tab bar, Apps button, header buttons and list search, a shared `HeaderFade` in `Screen`, Home and More (More's title is now pinned), and the drawn tab bar given a glass capsule, a sliding selection pill and a page-coloured fade behind it. The secondary button took SERLP's card fill with a fine border; the neutral KPI tile moved to the card colour because the old grey now equals the page.
- Verified on the iPhone 17 Pro simulator (iOS 26.5) in light and dark: Home at rest and scrolled, More, an API keys list, the Apps directory, Orders and its drawer.

## Findings

- Altin cannot use SERLP's native tab bar yet: on Expo SDK 54, `@react-navigation/bottom-tabs` 7.18's `unstable` navigator imports `Tabs` from `react-native-screens`, which the SDK-pinned 4.16 does not export (it has the older `BottomTabs`). SERLP has it because it moved to Expo SDK 57.
- On React Native 0.81 an absolutely positioned child with `top: "100%"` inside a parent with no fixed height was placed at the parent's vertical centre instead of below it; anchoring with a negative `bottom` and an explicit `height` works. SERLP's identical `HeaderFade` works on React Native 0.86.
- With a grey light page, anything filled with `surfaceMuted` (the old card grey) that sits directly on the page disappears; it is only for wells and inputs inside cards or sheets.
