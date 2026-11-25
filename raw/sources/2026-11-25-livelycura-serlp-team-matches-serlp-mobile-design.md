# LivelyCura: SERLP Team follows SERLP Mobile's design, colours and dark mode (decided 2026-11-24)

- Date: 2026-11-24 (redesign built overnight into 2026-11-25)
- Author: the product owner, in a LivelyCura Claude Code session
- Recorded from: the owner's own message (quoted verbatim below) and the decisions the session made under it
- Feature: the employee app SERLP Team (repo livelycura-loop-app), branch `feature/hrm`
- Status when recorded: decided; the redesign is built and checked on the iOS simulator in light and dark, not yet committed

## The owner's request (verbatim)

- "now let's move to the loop app now serlp teams same pattern and redesign, impress me, and darkmode to make same as serlp mobile and use the same colors from serlp mobile"

## How the session applied it

- SERLP Team's theme now holds SERLP Mobile's palette in both modes: brand green #256C4A (dark #3B7559), Apple's neutral greys in light, a black page with #1C1C1E cards in dark; the older SERLP Team token names stay as aliases.
- Where SERLP Team's design-system README recorded an earlier owner preference that disagrees with SERLP Mobile (flat cards with no shadow in light, status pills with dots, inset lines in dark, navy washes, per-row colours, spinner replacing the label), the newer SERLP Mobile choice wins, because the owner asked for the same pattern.
- Kept on purpose: SERLP Team's lighter dark-mode red (#F97066) and blue (#5AA2FF) for words, so red and blue text stays readable on dark cards; fills keep SERLP Mobile's colours.
- Dark mode works as in SERLP Mobile: the app's own switch (More → Preferences → Dark mode), native views follow it through `Appearance.setColorScheme`, and the navigation theme uses the dark or light base.
- Chrome as in SERLP Mobile: the native iOS 26 Liquid Glass tab bar on iPhones with iOS 26.1+ (drawn capsule elsewhere), round glass header buttons through `expo-glass-effect` (solid fallback on older builds and Android), pushed titles centred on the back-button row, large left titles on tab roots, the header fade, sheets that fade their scrim while sliding up, the four-box sign-in code, and the version line "SERLP Team v… · by SERLP".
- The native tab bar needed React Navigation upgraded to bottom-tabs 7.22, native 7.5 and native-stack 7.21 (JavaScript only); `expo-glass-effect` is a native package, so the glass shows only after a new app build.
