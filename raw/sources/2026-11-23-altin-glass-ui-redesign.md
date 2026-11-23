# Altin Partner Mobile: glass UI redesign

- Date: 2026-11-23
- Author: the user, through an Altin Partner Mobile Claude Code session
- Repository: `altin-partner-mobile`, branch `feature/apps`, uncommitted when recorded
- Repository records: `DESIGN.md` "Glass layer", the `AGENTS.md` theme bullet "Glass system", `.impeccable/surfaces/src-home-homescreen-tsx.md`

## The user's request (verbatim, 2026-11-23)

> we are going to work on improving the ui of the partner app, when I was building it I was focus on the functionalities so now we moving to improving the ui to premium look with classmorphism and nice looks, you know the drill already impress me

"classmorphism" is glassmorphism. Later the user handed the simulator over: "Sim is yours".

## What was built

- Theme (`src/theme/constants.ts`): light `background` moves to the existing paper tone `#F8F6F3`; `surface` becomes translucent (white 66% light, white 5.5% dark), `surfaceMuted` ink 5% / white 7%, `border` ink 8% / white 10%; new `surfaceSolid` for opaque fills. A `glass` group per appearance holds blur tints (system chrome, thick and ultra-thin materials), fallback fills, glow specs, shadows and the inline finishes `cardFinish`, `heroFinish` and `tileFinish`; `accentGlass` holds the red glass gradient.
- `AmbientBackdrop`: the first child of every screen root; one red key light top right, faint secondary glows, drawn as CSS radial gradients.
- `GlassCardView` / `GlassCardPressable`: about 37 card styles across every module swapped their base element so the finish (top sheen, depth shadow) applies everywhere without per-screen edits.
- `GlassSurface` with `expo-blur` (`~15.0.8`, native rebuild): the floating tab bar (`chrome`) and Home's header (`bar`: blur only, faded in on scroll so content frosts beneath it). The Apps button is a red glass orb.
- `GlassFill` for sheets and the module drawer.
- Kept: palette, system fonts, brand icon wells, 0.3 card borders, icons, layout, the user's tuned KPI colors (gloss added). Copy fix: the login title "Welcome to Back" became "Welcome back".

## Findings (verified on the iPhone 17 Pro simulator, iOS 26.5)

- React Native 0.81 parses `radial-gradient(circle 400px at 98% -4%, …)` wrongly: after a single size it consumes the next token, so `at` is lost, the positions are read as sizes and every glow is centered. Writing `ellipse 400px 400px at 98% -4%` works.
- styled-components (native) turns `boxShadow` into legacy `shadow*` props (murky on translucent views), renames `experimental_backgroundImage` to an unknown key and ignores a `style` returned from `.attrs`. Glass finishes must arrive through the instance `style` prop.
- On iOS, a translucent border on a view with non-uniform corner radii (only the left corners rounded) renders through a stretched image and smeared a visible ~52-point band down the module drawer. One uniform radius, overhanging the panel's flush edge and clipped by the panel, keeps a plain layer border.
- `expo-blur` does not blur inside a React Native `Modal` on iOS (Fabric): text behind the sheet stayed sharp, and remounting the blur after layout did not help. Sheets and the drawer use a 98.5% frosted fill with sheen and rim instead; real blur stays on non-modal chrome.
- Fast Refresh does not reliably update an open `Modal`'s content; verify sheet changes after a full reload.
- The simulator's dev build loaded serlp-mobile's bundle from port 8081; the app reads its packager location from the `RCT_jsLocation` user default, which was pointed at Altin's Metro on 8082.
