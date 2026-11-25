# LivelyCura: SERLP Dispatch follows SERLP Mobile's design, colours and dark mode (decided 2026-11-25)

- Date: 2026-11-25
- Author: the product owner, in LivelyCura Claude Code sessions
- Recorded from: the owner's own messages (quoted verbatim below) and the decisions the sessions made under them
- Feature: the rider app SERLP Dispatch (repo livelycura-courier-mobile), branch `feature/redesign` off `develop`
- Status when recorded: decided; the redesign is built and checked on the iOS simulator in light and dark, not yet committed; Android not checked

## The owner's words (verbatim)

- Moving on from the SERLP Team redesign: "now move to the next app, the courier mobile"
- Resuming in a new session: "let's continue with the ui updates here, we were on the courier mobile so fetch the context from the vault and continue"
- Asked "Keep the "SERLP DISPATCH" and "Rider account" labels removed, or bring them back?", the owner answered: "Keep removed"

## How the sessions applied it

- SERLP Dispatch gets the same redesign and dark mode as SERLP Team, with SERLP Mobile as the reference: SERLP Mobile's palette in light and dark, card edges and row lines, the native iOS 26 Liquid Glass tab bar on iPhones with iOS 26.1+ (drawn capsule elsewhere), round glass header buttons, pushed titles centred on the back-button row, and the version line "SERLP Dispatch v… · by SERLP".
- Restyle only: every screen keeps its sections and content. No header fades, as in SERLP Team.
- Account's appearance setting is SERLP Mobile's single "Dark mode" switch row (it replaces the earlier Light / Dark choice rows), with SERLP Mobile's iOS 26 crossfade: a picture of the screen covers the change, with the switch cut out so it keeps moving, then fades away.
- Sign-in keeps Dispatch's own map artwork and words, recoloured to SERLP Mobile's palette; "SERLP Dispatch" stays beside the logo there.
- Removed, and kept removed by the owner's answer above: the small capital "SERLP DISPATCH" line above the big title on the tab screens (Home, Deliveries, Money, Account) and on rider setup and account review, and the small "Rider account" line above the rider's name on Account's top card. SERLP Mobile and SERLP Team have no such lines.
- New native packages `expo-glass-effect` (glass buttons) and `react-native-view-shot` (the crossfade picture), so a new store build is needed before those show; React Navigation is pinned to bottom-tabs 7.16.2, native 7.2.5 and native-stack 7.16.0 for the native tab bar.
