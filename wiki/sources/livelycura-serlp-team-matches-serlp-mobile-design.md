---
type: source
status: active
created: 2026-11-25
updated: 2026-11-25
tags: [livelycura, loop, design, dark-mode, mobile, decision]
sources:
  - ../../raw/sources/2026-11-25-livelycura-serlp-team-matches-serlp-mobile-design.md
  - ../../raw/sources/2026-11-25-livelycura-serlp-team-no-header-fade.md
source_date: 2026-11-24
ingested: 2026-11-25
confidence: high
---

# LivelyCura SERLP Team Matches SERLP Mobile Design

## Source

- Raw file: [SERLP Team matches SERLP Mobile design](../../raw/sources/2026-11-25-livelycura-serlp-team-matches-serlp-mobile-design.md)
- Date: 2026-11-24
- Author: Product owner (verbatim request), with the session's applied decisions
- Ingested: 2026-11-25

## Core Claims

- SERLP Team (the staff app, repo livelycura-loop-app) uses SERLP Mobile's design pattern, its colours, and its dark mode. SERLP Mobile is the reference: when the two apps' recorded preferences disagree, SERLP Mobile's newer choice wins.
- Colours are SERLP Mobile's palette in both modes (brand green #256C4A, dark #3B7559; neutral greys in light; black page with #1C1C1E cards in dark). Light cards get the soft even shadow, dark cards the 1pt #38383A rim; row lines are inset hairlines in light and full-width 1pt lines in dark.
- Dark mode is the app's own switch in More → Preferences, and native views follow it, as in SERLP Mobile.
- Exceptions kept for readability: lighter dark-mode red (#F97066) and blue (#5AA2FF) for words; fills keep SERLP Mobile's colours.
- No header fades in SERLP Team (owner, 2026-11-25: "remove the header fades away"): content scrolls under a solid header band. SERLP Mobile keeps its fade. Raw: [no header fade](../../raw/sources/2026-11-25-livelycura-serlp-team-no-header-fade.md).

## Useful Details

- Chrome copied from SERLP Mobile: the native iOS 26 Liquid Glass tab bar (iPhone, iOS 26.1+; drawn capsule elsewhere), glass round header buttons via `expo-glass-effect`, centred pushed titles on the back-button row, large left tab-root titles (no header fade, by the owner's later request), fade-and-slide sheets, four-box sign-in code, and the installed-version line "SERLP Team v… · by SERLP".
- The native tab bar required React Navigation bottom-tabs 7.22 / native 7.5 / native-stack 7.21. `expo-glass-effect` is native, so a new store build is needed before the glass shows.

## Connections

- Applies to [[../projects/livelycura-loop-app|LivelyCura Loop App]]; the reference look is [[../projects/serlp-mobile|SERLP Mobile]].
- Related: [[livelycura-loop-renamed-serlp-team|LivelyCura Loop Renamed SERLP Team]], [[livelycura-credit-serlp-not-livelycura|Credit SERLP, not LivelyCura]].

## Contradictions Or Tensions

- SERLP Team's earlier design-system README recorded flat light cards (owner found card shadows too heavy), status dots, inset dark lines and per-row colours. Those are superseded by this request; the README is being rewritten to the SERLP Mobile language.

## Open Questions

- None on the direction.
