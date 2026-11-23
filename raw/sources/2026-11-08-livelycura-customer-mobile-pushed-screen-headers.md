# LivelyCura customer mobile: pushed-screen headers and inspo as reference

Date: 2026-11-08
Source: direct user corrections in a `livelycura-customer-mobile` session, plus the code changed and verified in that session (paraphrased).

While restyling Profile, Account and the add-address screen, the agent kept placing a large screen title (and on one screen a subtitle) under the glass back button. The user had removed those titles from Profile and Account themselves, then saw "New address" placed under the back button again and objected strongly. The rule they gave: never put the title under the back button; if a screen has a title, it goes on the same row as the back button, centred. Profile has no title.

On the Profile settings list, the user supplied a settings-style inspiration image. The agent copied it too literally: Delete Account mixed into the Settings rows, and the inspo's own tile colours (amber, yellow, blue, dark). The user said the image was only a reference, not something to copy exactly. They asked for Delete Account and Sign out to sit in their own group, and chose brand-green tiles (theme `primary` tint and icon), with red kept for Sign out and Delete Account.

The user also asked that the back button not scroll away with the page.

Implemented (uncommitted, branch `feature/ui-updates`): a shared `BackTitleRow` (glass back button, optional title centred on the same row) and `FloatingBackBar` (that row pinned over a scrolling page with a soft page-coloured fade under the status bar) in `src/components/floating-back-bar`. Account and "New address" use a centred title on that row; Profile has none. Verified on the iPhone 17 Pro simulator (iOS 26).
