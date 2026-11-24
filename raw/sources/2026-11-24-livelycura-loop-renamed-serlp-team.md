# LivelyCura: the staff app Loop is renamed "SERLP Team" (decided 2026-11-24)

- Date: 2026-11-24
- Author: the product owner, in a LivelyCura Claude Code session
- Recorded from: the owner's own messages (quoted verbatim below), and the research the session presented before the owner decided
- Feature: the employee app (repo livelycura-loop-app). Its App Store / Play listing was "SERLP Loop" and its home-screen name "Loop".
- Status when recorded: decided; the rename and an Expo upgrade are being built on `feature/hrm`

## The owner's request (verbatim)

- "the loop app needs rebranding, we changing the name to serlp teams or team by serlp, I am still contemplating."
- "so about the about the renaming these are combinations so I want to do our research and pick the best fit
  1. Teams by Serlp on app store and play store and when they download the app the name shows just teams
  2. Team by Serlp on app store and play store and when they download the app the name shows just team
  3. Serlp Team on app store and play store and when they download the app the name shows just Serlp Team
  4. Serlp Team on app store and play store and when they download the app the name shows just Team
  5. Serlp Teams on app store and play store and when they download the app the name shows just Serlp Teams
  6. Serlp Teams on app store and play store and when they download the app the name shows just Teams"
- "the logos and the icons will be created by our designer so we can skip that"

## The session's recommendation

Option 3, written "SERLP Team" (capitals, as the main SERLP app writes its name). Reasons given:
- The phone name is the same as the store name. Apple rejects apps whose name on the phone doesn't "sufficiently match" the store name (Guideline 2.3.8; for example "Where Is My Money" in the store and "My Money" on the phone was rejected).
- 10 characters fit on the home screen.
- "Team", not "Teams": Microsoft's own store rules list "Teams" as a Microsoft product name third-party apps must not use, and recommend "Brand + noun" instead. A "Teams" icon clashes with Microsoft Teams, and Google Play's impersonation policy flags confusable titles.
- Searching "SERLP" shows SERLP and SERLP Team side by side, and the family reads SERLP, SERLP AI, SERLP Team.
- Square Team (Square's staff app for clock-in, schedules and open shifts) is the same pattern.

## The owner's answer (verbatim)

- "serlp mobile doesn't have those apps and it's working so why must we keep them delete them and update it to the latest expo version, and start the renaming process"

"Those" refers to Loop's `patches/` and `plugins/` folders. They are Xcode 27 workarounds needed only because Loop was on Expo SDK 54. The owner's instruction to "start the renaming process" accepted the option-3 recommendation.

## What the session set as the rename rules

- Everything people read says "SERLP Team". Where a sentence puts a person into the app, it says "the SERLP Team app".
- Code names and IDs keep "loop", so that current installs update in place and links already sent keep working: bundle IDs, slug, schemes, storage keys, wire values, identifiers, the repo name, and the old install link path.
- The owner renames the store listings at release. The designer supplies icons and logos.
