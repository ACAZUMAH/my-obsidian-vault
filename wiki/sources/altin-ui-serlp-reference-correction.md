---
type: source
status: active
created: 2026-11-24
updated: 2026-11-24
tags: [altin, mobile, design-system, react-native, expo, correction]
sources:
  - ../../raw/sources/2026-11-24-altin-ui-serlp-reference-correction.md
confidence: high
---

# Altin UI Follows SERLP Mobile

## Source

- Raw file: [Altin UI SERLP reference correction](../../raw/sources/2026-11-24-altin-ui-serlp-reference-correction.md)
- Date: 2026-11-24
- Author: user, through an Altin Partner Mobile Claude Code session; repository `DESIGN.md` and `AGENTS.md`
- Ingested: 2026-11-24

## Core Claims

- User correction (2026-11-24): the 2026-11-23 glassmorphism pass was wrong for a business app. Red glows mixed with black or white backgrounds are rejected; the UI must look like the user's own updated apps, and SERLP Mobile is the reference. It supersedes [[altin-glass-ui-redesign|the glass redesign record]].
- The accepted model, taken from SERLP Mobile: iOS grouped surfaces (grey page and white cards in light, black page and dark cards in dark), Apple's Liquid Glass only on floating controls, solid content, no decorative gradients, and every header a solid page-coloured band with a short fade below it.
- In Altin this is light page `cloud` `#F6F7F8` with white cards (dark unchanged), `expo-glass-effect` controls in `src/components/glass`, and a shared `HeaderFade` drawn by `Screen`, Home and More. Altin's own palette, icon wells, 0.3 card borders and red Apps button stay.

## Useful Details

- Before redesigning, open the reference app on the simulator and compare screen by screen in both appearances; reading another app's design notes was not enough.
- Native tab bar: blocked on Expo SDK 54, where `bottom-tabs/unstable` needs `Tabs` from a newer `react-native-screens` than the pinned 4.16. Altin keeps a drawn glass capsule with a sliding selection pill, as SERLP's own fallback bar does.
- React Native 0.81: an absolute child with `top: "100%"` in a parent without a fixed height lands at the parent's centre; anchor with a negative `bottom` and an explicit `height`.
- With a grey light page, `surfaceMuted` is only for wells and inputs inside cards or sheets; page-level fills use `surface`.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[../projects/serlp-mobile|SERLP Mobile]]: the reference look.
- [[altin-glass-ui-redesign|Altin Glass UI Redesign]]: the superseded pass.
- [[livelycura-customer-mobile-glass-home-direction|LivelyCura Customer Mobile Glass Home Direction]]: the origin of the controls-only Liquid Glass pattern SERLP follows.

## Contradictions Or Tensions

- The light page moved from white to grey, which changes `background`'s role in the theme guide; the user's SERLP reference governs the look, and the guide still governs palette values, type, spacing and radii.

## Open Questions

- Should Altin move to a newer Expo SDK to use the native iOS 26 tab bar as SERLP does?
- Should SERLP's other details (uppercase section labels on Home, a card around the More identity, inset row separators in light) follow?
