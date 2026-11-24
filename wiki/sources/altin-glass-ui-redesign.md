---
type: source
status: superseded
created: 2026-11-23
updated: 2026-11-24
tags: [altin, mobile, design-system, glassmorphism, react-native, expo]
sources:
  - ../../raw/sources/2026-11-23-altin-glass-ui-redesign.md
confidence: high
---

# Altin Glass UI Redesign

> [!warning] Superseded 2026-11-24
> The user rejected this pass as unbusinesslike (red glows on black and white, see-through cards, blurred bars and sheets) and pointed to SERLP Mobile as the reference. It was reverted. See [[altin-ui-serlp-reference-correction|Altin UI Follows SERLP Mobile]]. The React Native gotchas below remain technically true.

## Source

- Raw file: [Altin Partner glass UI redesign](../../raw/sources/2026-11-23-altin-glass-ui-redesign.md)
- Date: 2026-11-23
- Author: user, through an Altin Partner Mobile Claude Code session; repository `DESIGN.md` and `AGENTS.md`
- Ingested: 2026-11-23

## Core Claims

- User direction (2026-11-23): with the features built, Altin Partner Mobile moves to a premium glassmorphism look across the whole app. It supersedes the earlier flat, opaque surfaces and Home's "flat tonal depth"; the palette, system fonts, icon-well rules and 0.3 card borders stay.
- The glass lives in the theme and shared components, not per screen: translucent `surface`/`border` tokens plus a `glass` token group, an `AmbientBackdrop` first in every screen root, card styles built on `GlassCardView`/`GlassCardPressable`, and `GlassSurface`/`GlassFill` for chrome and sheets.
- Real blur (`expo-blur`, iOS system materials) is reserved for chrome that content scrolls under: the floating tab bar and Home's header, which stays invisible at rest and fades in on scroll. Cards are translucent with a lit top edge instead of blurred, which keeps long lists smooth.
- Sheets and the module drawer use a near-opaque frosted fill, because a native blur inside a React Native `Modal` does not blur on iOS.

## Useful Details

- Gotchas: write CSS radial gradients as `ellipse Rpx Rpx at x y` (React Native 0.81 drops the position after a single `circle Rpx` size); pass `boxShadow` and `experimental_backgroundImage` through the instance `style` (styled-components rewrites or drops them, and ignores `attrs({ style })`); give a translucent border one uniform radius (non-uniform radii render it as a stretched band on iOS); verify Modal changes after a full reload.
- Each screen draws its own backdrop rather than sharing one behind transparent native-stack screens, which would show the previous screen during a push.
- `expo-blur` is native: the app needs a rebuild after installing it, and the import is gated with `requireOptionalNativeModule`. Android has no blur and uses opaque fallback fills.
- Verified in light and dark on the iPhone 17 Pro simulator; screenshots are in the repository's `design-audit/glass/`.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[altin-theme-navigation-runtime-corrections|Altin Theme, Navigation, and Runtime Corrections]]: the theme-guide authority this pass extends.
- [[altin-mobile-brand-system|Altin Mobile Brand System]]: the rejected brand-book look that must still not return.

## Contradictions Or Tensions

- The project's design tooling advises system materials and no hand-rolled glass on iOS; the user's explicit direction wins, so blur uses system materials and cards carry a translucent finish.
- The theme guide lists opaque surface colors; the live glass tokens now differ, and the repository records that the guide still governs palette, type, spacing and radii.

## Open Questions

- Does the glass hold up on Android, where chrome falls back to opaque fills?
- Should sheets gain real blur if a Modal-compatible blur becomes available?
