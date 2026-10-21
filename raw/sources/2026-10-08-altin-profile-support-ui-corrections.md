# Altin Partner Profile and Support UI Corrections — 2026-10-08

Sanitized record of direct user corrections to the Altin Partner Mobile Profile and Support screens in a Claude Code session. No credentials, tokens, or personal identifiers are included.

## Unverified UI reported as done

- The agent reported Profile and Support done after type-check and code reviews; the user's Metro was hung, so no screen had been viewed on the simulator. The user sent screenshots of the ticket details and Edit profile screens: "you do this nonsense and tell me it's done? bad ui".
- Problems found on the device: the reply composer was a labelled form field with separate attach and send buttons floating beside it; linked orders showed a truncated UUID with a large unconfirmed remove button; "Choose photo" and "Attach files" were dark-on-dark buttons on cards; Raise a ticket repeated its title in a card, and its Category label used a different style from the other labels; Profile showed the email twice.
- Fixes, each checked on the simulator: a single SERLP-style composer bar (attach, growing input, round send button); linked-order rows with an icon well, "Order XXXXXXXX" and a note when details aren't available, and unlink confirmation; dashed "add" tiles for attaching files and linking orders; form-style field labels for choices; a flush text action for the profile photo; and Save disabled until something changes.

## Profile fields and the web reference

- The user asked whether the web app had really been referenced, since the web profile shows name, email, phone, city, and about, and mobile let them edit only the photo and alternate phone.
- Verified answer: every web profile editor is a facade. Partner's `ProfileSettings` save is a `TODO` that logs and returns `true`; admin and ERP `useUpdateProfile` hard-code `{ success: true }` with the real call commented out; market has no profile editing. The live staging schema's `user.updateProfile` accepts only `alternatePhoneNumber` and a required `profilePictureId`; nothing updates the signed-in user's name or email, and city and about exist only on the courier KYC profile.
- The user accepted the edit screen as built. They removed the Change number and Verify actions from the Profile view and said the header Edit should do all of that work, so phone change and verification now start from Edit profile.
- Proposed backend change: add first name, last name, city, and about to `UpdateUserProfileInput` and make `profilePictureId` optional.
