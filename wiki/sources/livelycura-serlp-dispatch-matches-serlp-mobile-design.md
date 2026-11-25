---
type: source
status: active
created: 2026-11-25
updated: 2026-11-25
tags: [livelycura, courier, design, dark-mode, mobile, decision]
sources:
  - ../../raw/sources/2026-11-25-livelycura-serlp-dispatch-matches-serlp-mobile-design.md
source_date: 2026-11-25
ingested: 2026-11-25
confidence: high
---

# LivelyCura SERLP Dispatch Matches SERLP Mobile Design

## Source

- Raw file: [SERLP Dispatch matches SERLP Mobile design](../../raw/sources/2026-11-25-livelycura-serlp-dispatch-matches-serlp-mobile-design.md)
- Date: 2026-11-25
- Author: Product owner (verbatim requests and answer), with the sessions' applied decisions
- Ingested: 2026-11-25

## Core Claims

- SERLP Dispatch (the rider app, repo livelycura-courier-mobile) gets the same redesign and dark mode as SERLP Team, with SERLP Mobile as the reference: SERLP Mobile's palette in both modes, card edges and row lines, native iOS 26 tab bar, glass round header buttons, centred pushed titles, and the version line "SERLP Dispatch v… · by SERLP".
- Restyle only: screens keep every section and its content. No header fades, as in SERLP Team.
- Account's appearance setting is one "Dark mode" switch row with SERLP Mobile's iOS 26 crossfade; it replaces the earlier Light / Dark choice rows.
- No small capital "SERLP DISPATCH" line above screen titles and no "Rider account" line on Account's card (owner, 2026-11-25: "Keep removed"). Sign-in keeps "SERLP Dispatch" beside the logo and its own map artwork, recoloured.

## Useful Details

- The native tab bar shows on iPhones with iOS 26.1+ and falls back to a drawn capsule elsewhere. React Navigation is pinned to bottom-tabs 7.16.2, native 7.2.5 and native-stack 7.16.0.
- `expo-glass-effect` and `react-native-view-shot` are new native packages, so a new store build is needed before the glass buttons and the crossfade show.
- Committed and pushed at the owner's "Commit and push" (2026-11-25): livelycura-courier-mobile `feature/redesign` d0746b0. The Dark mode fixes found on the way went to the sister apps the same day, at the owner's "yes fix them": serlp-mobile `feature/hrm` efdc927c and livelycura-loop-app `feature/hrm` 0419c15.
- Lesson: React Native's iOS `Switch` puts `alignSelf: 'flex-start'` ahead of the style passed in, so in a row taller than the switch it sits high. A switch in a row needs `alignSelf: "center"` (SERLP Mobile: `SWITCH_IN_ROW` in `src/components/styled`).
- Lesson: when a quick second tap can overtake a first tap that is still waiting (here, the crossfade's screen picture), count the taps and let only the latest apply. Comparing the chosen value fails on three taps, where the first and third ask for the same thing.

## Connections

- Applies to [[../projects/livelycura-courier-mobile|LivelyCura Courier Mobile]]; the reference look is [[../projects/serlp-mobile|SERLP Mobile]].
- Same direction as [[livelycura-serlp-team-matches-serlp-mobile-design|LivelyCura SERLP Team Matches SERLP Mobile Design]]; related: [[livelycura-credit-serlp-not-livelycura|Credit SERLP, not LivelyCura]].

## Contradictions Or Tensions

- The project page's earlier rules (keep Courier's flat tab/header layout; explicit Light / Dark theme choice rows) are superseded by this redesign.

## Open Questions

- None on the direction.
