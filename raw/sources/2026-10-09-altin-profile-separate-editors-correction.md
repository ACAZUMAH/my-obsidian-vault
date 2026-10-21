# Altin Partner Profile Separate Editors Correction — 2026-10-09

Sanitized record of a direct user correction in an Altin Partner Mobile Claude Code session. No credentials, tokens, or personal identifiers are included.

## The correction

- The Profile edit mode put the photo, the primary phone number and the alternate phone in one form with one Save. Saving chained `updateProfile`, a code request and code confirmation.
- The user said the primary number, the alternate number and the profile picture do not have to be changed in one place: the APIs are clearly different, and the agent put them together anyway.
- The user also said phone numbers should be converted with `awesome-phonenumber`; members should not have to type the whole +233.

## What was built

- Profile now has no global edit mode. Each part changes on its own, in place, like the admin portal's section editors (`organizationBasicInfoSection`):
  - **Photo:** tap the avatar; it saves at once.
  - **Phone number:** Change or Verify, with an inline SMS code step.
  - **Alternate phone:** Edit, with Save and Cancel.
- Each editor is a component with its own state-only Formik hook and its own handlers.
- `awesome-phonenumber` (^7.5.0, as in Check City and the admin portal) was added. A shared `src/helpers/phoneNumbers.ts` validates local Ghana numbers and converts them to E.164; stored numbers prefill in local form.
