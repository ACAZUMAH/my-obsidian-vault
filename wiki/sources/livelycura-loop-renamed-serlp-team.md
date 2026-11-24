---
type: source
status: active
created: 2026-11-24
updated: 2026-11-24
tags: [livelycura, loop, brand, naming, app-store, decision]
sources:
  - ../../raw/sources/2026-11-24-livelycura-loop-renamed-serlp-team.md
source_date: 2026-11-24
ingested: 2026-11-24
confidence: high
---

# LivelyCura Loop Renamed SERLP Team

## Source

- Raw file: [LivelyCura Loop renamed SERLP Team](../../raw/sources/2026-11-24-livelycura-loop-renamed-serlp-team.md)
- Date: 2026-11-24
- Author: Product owner (verbatim request and answer), with the session's research
- Ingested: 2026-11-24

## Core Claims

- The employee app formerly called Loop (store listing "SERLP Loop") is named **SERLP Team** in both stores and on the phone's home screen. It is written exactly "SERLP Team": SERLP in capitals, Team singular, never "Teams" and never bare "Team".
- In text, "the SERLP Team app" is used where a sentence puts a person into it ("added you to the SERLP Team app"). Elsewhere "SERLP Team" stands alone ("told in SERLP Team").
- The rename covers everything people read. Code names and IDs keep "loop": bundle IDs `com.livelycura.loop*`, slug, schemes, storage keys, wire values such as `LOOP_MOBILE`, identifiers, the repo name, and the old install link path. That way current installs update in place and links already sent keep working.
- In the same change Loop moves from Expo SDK 54 to the latest SDK, and its Xcode 27 workarounds (`patches/`, `plugins/`) are deleted, as serlp-mobile on a newer Expo needs neither.

## Useful Details

- Why this name won over the six combinations the owner weighed:
  - One name everywhere avoids Apple's Guideline 2.3.8 rejection for a phone name that doesn't match the store name.
  - It fits the home screen.
  - It sits alongside SERLP and SERLP AI.
  - It avoids "Teams", which Microsoft's own rules reserve as its product name.
- Square Team is the same business-app / staff-app pattern.
- The owner renames the store listings at release; the designer supplies icons and logos.

## Connections

- Applies to [[../projects/livelycura-loop-app|LivelyCura Loop App]] and to every app that names the staff app: backend messages, the pharmacy portal, SERLP Mobile, the admin portal and the SERLP website.

## Contradictions Or Tensions

- Earlier store artwork used the identity "Loop by SERLP". That identity is superseded; new artwork comes from the designer.

## Open Questions

- None on the name.
