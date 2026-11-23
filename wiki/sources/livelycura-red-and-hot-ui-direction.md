---
type: source
status: active
created: 2026-11-10
updated: 2026-11-11
tags: [livelycura, red-and-hot, check-city, design, ui-direction, mobile]
sources:
  - ../../raw/sources/2026-11-10-livelycura-red-and-hot-ui-direction.md
  - ../../raw/sources/2026-11-10-livelycura-red-and-hot-chop-bar-picks.md
  - ../../raw/sources/2026-11-11-livelycura-red-and-hot-brand-colours.md
source_date: 2026-11-10
ingested: 2026-11-10
confidence: high
---

# LivelyCura Red And Hot UI Direction

## Source

- Raw file: [LivelyCura Red and Hot app: UI direction chosen](../../raw/sources/2026-11-10-livelycura-red-and-hot-ui-direction.md)
- Raw file: [LivelyCura Red and Hot app: Chop Bar part picks and build](../../raw/sources/2026-11-10-livelycura-red-and-hot-chop-bar-picks.md)
- Raw file: [LivelyCura Red and Hot app: brand colours and icon](../../raw/sources/2026-11-11-livelycura-red-and-hot-brand-colours.md)
- Date: 2026-11-10
- Author: The owner (decision, paraphrased with one quoted phrase), relayed by the implementing Claude Code session
- Ingested: 2026-11-10

## Core Claims

- The Red and Hot UI must look "totally different from the check city app".
- The owner chose direction B "Chop Bar" over A "Ember" (the session's and reviewers' pick) and C "Clean Heat", because it is the most different from Check City.
- Chop Bar: paper-cream background, chilli red lead colour, palm-oil orange price stickers, leaf green accent, Lilita One headings, Nunito body text, roasted-brown dark mode.
- Kept from B as drawn: the price sticker and the add button on product cards.
- To be redesigned because they still look like Check City: the bottom tab bar (floating rounded track, growing filled pill, separate round Cart button), the product card image (round photo overlapping the card top), and the item detail screen.
- Tab destinations (Menu, Search, Orders, Cart) and screen content stay; only the look changes.
- Final picks: tab bar "Signboard plank", product card "Edge to edge", item screen "Torn paper" with the photo filling its frame. Built into the app the same day; checks pass, device view pending the backend custom app record.
- The owner chooses designs by seeing and clicking options, not by reading explanations.
- 2026-11-11: with the real logo, brand colours became red and white (light) and red and black (dark), replacing Chop Bar's cream, brown, palm-oil orange and paper grain while keeping its shapes. Logo red #F20304; #DC0304 where white text sits on red; #FF4040 in dark mode. App icon: white R&H cut from the logo on red. Menu tab uses an icon; tab bar top corners are rounded.

## Useful Details

- The mockups are HTML files in `/Users/acazumah/Documents/LivelyCura/design-probes/red-and-hot-app` (outside the app repository), served by the `red-and-hot-design-probes` entry in `/Users/acazumah/Documents/LivelyCura/.claude/launch.json`. `content-checklist.md` there lists every element each screen must keep.
- Build prerequisite found during review: the `black` theme token is used both as ink on the primary colour and as plain text and shadow colour in several components; those uses must be repointed before the palette changes, or text turns white on white in light mode.

## Connections

- [[../projects/livelycura-red-and-hot-app|LivelyCura Red And Hot App]] carries the decision.
- [[livelycura-red-and-hot-app-kickoff|LivelyCura Red And Hot App Kickoff]] records the logic-identical port this restyle sits on.
- [[../projects/livelycura-check-city-app|LivelyCura CheckCity App]] is the look Red and Hot must move away from.

## Contradictions Or Tensions

- The session recommended A; the owner chose B. Best interpretation (high confidence): distinctness from Check City outranks the reviewers' build-cost and fidelity scores for this owner.
- Check City's accepted bottom navigation (one track plus a detached Cart) is replaced in Red and Hot by owner decision; it remains Check City's convention.

## Open Questions

- How do the built screens look on the device once the custom app record exists?
