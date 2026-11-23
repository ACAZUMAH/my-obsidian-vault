# LivelyCura customer mobile: dark mode and one tab bar design everywhere

Date: 2026-11-08
Source: direct user request in a `livelycura-customer-mobile` session, plus the code changed and verified in that session (paraphrased). Visual approval is pending; the user was to review after a nap.

The user asked for three things in order: a warmer Contact us screen ("what you did there isn't really encouraging"), dark mode, and then "the same ui design for android and other ios devices" older than the glass release, noting that Telegram keeps its floating tab bar design on devices without glassmorphism.

Implemented (uncommitted, branch `feature/ui-updates`):

- Contact us opens with a green "How can we help today?" card with Chat on WhatsApp and Call us buttons, then a "Prefer to write?" message form, then a "Follow us" Instagram row.
- Dark mode is iOS-style: black page, `#1C1C1E` cards, light text, brighter status colours, deeper hero greens, and pop-up sheets with a hairline outline and deeper backdrop. Profile's Appearance offers Light, Dark and System default; new installs follow the phone (`userInterfaceStyle` automatic). The theme's `white` token is the card colour; a new `onPrimary` token keeps text on green or red white in both modes.
- Android and iOS older than 26.1 get a drawn tab bar matching the iOS 26 native one: floating capsule, sliding selection pill, separate round cart button with the count badge, on solid surfaces. iOS 26.1+ keeps the native Liquid Glass bar.

Verified on the iPhone 17 Pro simulator (iOS 26), including the drawn bar forced on for testing. Android and pre-iOS 26 devices were not run.
