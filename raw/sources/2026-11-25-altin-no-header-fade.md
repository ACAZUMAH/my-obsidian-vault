# Altin Partner Mobile: no fade under headers

- Date: 2026-11-25
- Author: the user, through an Altin Partner Mobile Claude Code session
- Repository: `altin-partner-mobile`, uncommitted when recorded

## What happened

During the Altin UI improvement (method from the SERLP Mobile redesign), the session added a 24pt page-coloured fade under every header (`HeaderFade` in the shared `Screen`, Home and More). The user then removed it themselves: they deleted it from `src/components/screen/Screen.tsx` and commented it out in `src/home/components/HomeHeader.tsx`. Asked whether to remove it everywhere to match, the user answered "Yes, remove everywhere".

## Decision

- Altin headers are a solid page-coloured band with no fade under them; content scrolls up to the band's edge.
- The session removed `HeaderFade`, the screen context that padded content 24pt below the fade, and More's own fade, and restored the original content spacing.
- The floating tab bar's page-coloured fade and the Reports export bar's short fade were kept: they sit above footers, not under headers.
