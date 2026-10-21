---
type: source
status: active
created: 2026-09-23
updated: 2026-10-07
tags: [altin, mobile, brand, typography]
sources:
  - ../../raw/sources/2026-09-23-altin-mobile-brand-decision.md
confidence: high
---

# Altin Mobile Brand System

## Source

- Raw decision: [Altin mobile brand decision](../../raw/sources/2026-09-23-altin-mobile-brand-decision.md).
- Brand book: [Altin Brand Book v1.0](../../raw/assets/altin-brand-book-v1.0.pdf), September 2026.
- Ingested: 2026-09-23.

## Core Claims

- The supplied brand package is the Altin apps' mobile visual authority; earlier web-app colors and typography are superseded for mobile.
- One master Altin mark and wordmark serve all services. Use the supplied logo and app-icon files, never a retyped or recolored logo.
- Product UI uses Altin Red `#F40F1B`, Charcoal `#232221`, Paper `#F8F6F3`, White, and the provided neutral and functional colors. Small white text on a red fill requires Red 700 `#C20B15` for contrast.
- Plus Jakarta Sans serves headings and buttons, IBM Plex Sans serves body text and labels, and IBM Plex Mono serves tracking IDs, amounts, times, and other scannable data.

## Useful Details

- The icon master is a 1024-pixel red square with a white mark. Android uses the supplied transparent white foreground over Altin Red.
- The mobile light theme uses Paper as ground and White for cards; the dark theme uses warm near-black ground and Charcoal cards. The brand book reserves full-red backgrounds for covers and similar short surfaces.
- The Partner repository converts the supplied variable fonts to fixed weight variants for reliable React Native rendering. The repository's `PRODUCT.md` and `DESIGN.md` hold the implemented mobile tokens.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]].
- [[../syntheses/software-development-operating-manual|Software Development Operating Manual]].

## Contradictions Or Tensions

- Older Altin project guidance named `#F9F1EF` as the mobile background. The supplied September 2026 brand book supersedes it with Paper `#F8F6F3`.
- For Altin Partner Mobile, the user later rejected this palette and the custom fonts as the app theme. The repository's `docs/app-theme-guide.md` and system typography now govern; the logo, lockup, and app-icon rules here still apply. See [[altin-theme-navigation-runtime-corrections|the theme correction]].

## Open Questions

- Whether other Altin app repositories have adopted this package remains to be checked in each repository.
