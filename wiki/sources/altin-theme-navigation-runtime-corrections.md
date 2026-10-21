---
type: source
status: active
created: 2026-10-07
updated: 2026-10-07
tags: [altin, mobile, theme, navigation, runtime]
sources:
  - ../../raw/sources/2026-10-07-altin-theme-navigation-runtime-corrections.md
confidence: high
---

# Altin Theme, Navigation, and Runtime Corrections

## Source

- Raw file: [Altin theme, navigation, and runtime corrections](../../raw/sources/2026-10-07-altin-theme-navigation-runtime-corrections.md)
- Date: late September 2026 (corrections); confirmed 2026-10-07
- Author: user, through Altin Partner Mobile Codex tasks and a Claude Code session
- Ingested: 2026-10-07

## Core Claims

- Altin Partner Mobile's colors, typography, spacing, and radii come from the repository's `docs/app-theme-guide.md`, implemented in `src/theme/constants.ts`. User-tuned values in that file win over the guide. The earlier brand-book theme pass and its custom fonts were rejected; typography uses system fonts.
- Primary-colored icons inside icon wells look the same in both appearances: primary-red glyph on a subtle red well, deep red in dark mode. White glyphs or neutral `surfaceMuted` wells in dark mode are wrong. Neutral controls such as notification and back buttons keep neutral tokens.
- Card and card-skeleton borders are 0.3 wide project-wide; input, selection, and navigation outlines keep their own widths.
- The bottom tabs are Home, Search, Reports, and More, plus the center Apps action. Reports replaced Notifications intentionally; Notifications opens from the Home bell.
- OAuth testing requires the development build. Agents must not leave a background Metro server on port 8081.

## Useful Details

- The brand book still governs the logo, lockups, and app-icon assets; the rejection covers the brand-book palette and fonts as applied to the app theme.
- The current tokens are `brandIconBackground*` for primary icon wells and `neutralIcon*` for neutral controls.
- A request about one visual detail authorizes changing only that detail; adjacent icons, glyphs, and controls stay untouched.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[altin-mobile-brand-system|Altin Mobile Brand System]].
- [[altin-search-browse-grouping|Altin Search Browse Grouping]].
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].

## Contradictions Or Tensions

- Supersedes the [[altin-mobile-brand-system|brand-system]] palette and font claims as the implemented mobile theme authority.
- Supersedes the Notifications tab recorded in [[altin-orders-mobile-web-reference|Altin Orders Mobile and Web Reference]] and [[ceqa-altin-hermes-conversation-harvest-supplement-1|Hermes Supplement 1]].

## Open Questions

- Whether other Altin mobile apps also take `app-theme-guide.md` over the brand-book palette and fonts.
