---
type: source
status: active
created: 2026-11-24
updated: 2026-11-25
tags: [altin, mobile, design-system, react-native, expo, correction]
sources:
  - ../../raw/sources/2026-11-24-altin-ui-serlp-reference-correction.md
  - ../../raw/sources/2026-11-24-altin-serlp-reference-not-copy.md
  - ../../raw/sources/2026-11-25-altin-no-header-fade.md
confidence: high
---

# Altin UI Uses the SERLP Redesign as a Reference

## Source

- Raw files: [Altin UI SERLP reference correction](../../raw/sources/2026-11-24-altin-ui-serlp-reference-correction.md); [SERLP is a reference, not a template](../../raw/sources/2026-11-24-altin-serlp-reference-not-copy.md); [No header fade](../../raw/sources/2026-11-25-altin-no-header-fade.md)
- Date: 2026-11-24
- Author: user, through an Altin Partner Mobile Claude Code session; repository `DESIGN.md` and `AGENTS.md`
- Ingested: 2026-11-24

## Core Claims

- User corrections (2026-11-24):
  - The 2026-11-23 glassmorphism pass was wrong for a business app (red glows on black or white). It supersedes [[altin-glass-ui-redesign|the glass redesign record]].
  - Later the same day: SERLP Mobile is "a reference, not copy everything and paste"; the two apps do different things. The user wants the quality of the SERLP Mobile redesign they approved, applied in Altin's own identity.
- The session first misread "check the serlp mobile" as "make Altin look like SERLP" and rebuilt Altin's shell to SERLP's look (grey page, glass controls, header fades). That copy is under review, not the target.
- The transferable part is the SERLP redesign method (serlp-mobile `dbd1a835`; board `livelycura-hq/tasks/mobile-ui-redesign.md`; handoff `docs/mobile-ui-redesign-2026-11/handoff.md`):
  - Tab by tab, with the owner checking each.
  - Glass only on floating controls; solid content; header fades; list ends clear of the tab bar. In Altin the owner dropped the header fade on 2026-11-25: headers are a solid band with no fade.
  - Light mode on neutral greys: no harsh outlines, a soft shadow, inset hairlines, near-black text, darker status words. Dark mode untouched.
  - A black modal dim that fades in.
  - Every module audited for crowded or repetitive screens, each reworked keeping every fact.
  - An independent review per area, and checks on several devices.
- Altin keeps its own palette, red brand, icon-well rule, 0.3 card border rule (unless the owner changes it), Apps button, screens and AGENTS.md rules.

## Useful Details

- Before UI work, read the SERLP board and handoff for the method and the owner's standing UI preferences, and look at SERLP on the simulator for the quality bar; then design for Altin's own screens and data.
- Native tab bar: blocked on Expo SDK 54, where `bottom-tabs/unstable` needs `Tabs` from a newer `react-native-screens` than the pinned 4.16. Altin keeps a drawn glass capsule with a sliding selection pill, as SERLP's own fallback bar does.
- React Native 0.81: an absolute child with `top: "100%"` in a parent without a fixed height lands at the parent's centre; anchor with a negative `bottom` and an explicit `height`.
- With a grey light page, `surfaceMuted` is only for wells and inputs inside cards or sheets; page-level fills use `surface`.

## Connections

- [[../projects/altin-partner-mobile|Altin Partner Mobile]]
- [[../projects/serlp-mobile|SERLP Mobile]]: the redesign whose method and quality are the reference.
- [[altin-glass-ui-redesign|Altin Glass UI Redesign]]: the superseded pass.
- [[livelycura-customer-mobile-glass-home-direction|LivelyCura Customer Mobile Glass Home Direction]]: the origin of the controls-only Liquid Glass pattern SERLP follows.

## Contradictions Or Tensions

- The light page moved from white to grey during the copy pass; whether that stays for Altin is part of the review. The theme guide still governs palette values, type, spacing and radii.

## Open Questions

- Should Altin move to a newer Expo SDK to use the native iOS 26 tab bar as SERLP does?
- Does the owner keep the 0.3 card border rule, or take the SERLP method's no-outline light cards?
