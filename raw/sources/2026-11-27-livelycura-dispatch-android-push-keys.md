# LivelyCura: SERLP Dispatch Android push keys exist only for the store app id; ringing tested on production (2026-11-27)

- Date: 2026-11-27
- Author: the product owner, in a LivelyCura Claude Code session
- Recorded from: the owner's own messages (quoted verbatim below) and what the session observed while trying to test the ringing on an Android emulator
- Feature: SERLP Dispatch (repo livelycura-courier-mobile, branch `feature/redesign`) delivery offers that keep ringing until the rider answers
- Status when recorded: built, not committed; app checks pass; iPhone simulator push tests pass; Android emulator test not possible

## What the session observed

- `eas credentials -p android` (viewed only, nothing changed) for project `serlp-dispatch`: the production and base profiles (`com.livelycura.dispatch`) have a Google Service Account Key for FCM V1 from Firebase project `livelycura-production-3d769`; the preview profile (`com.livelycura.dispatch.preview`) has none; the development profile (`com.livelycura.dispatch.dev`) has no credentials at all.
- Expo's push API answered "Unable to retrieve the FCM server key for the recipient's app" (InvalidCredentials) for tokens registered under the dev and preview app ids, so dev and preview Android builds of SERLP Dispatch receive no pushes.
- The owner's dev Firebase file (project `livelycura-development`) lists `com.livelycura.dispatch.development`, while `app.config.ts` gives the development variant `com.livelycura.dispatch.dev`; the other apps' dev variants use `.development`.
- A token from the dev Firebase project sent with the production key is refused by Google: "SenderId mismatch" (SENDER_ID_MISMATCH) in the Expo push receipt.
- Expo keeps a token's app id for a short while (about 2 minutes) after the token is registered again under another app id.
- The `GOOGLE_SERVICES_JSON` files in the project's EAS environments (Secret visibility) are the app-side Firebase config, a different thing from the FCM V1 key Expo needs to send; secret values are readable only on EAS build servers, not from the website or CLI.

## The owner's words (verbatim)

- On the EAS environment files: "I already have the firebase files saved in the environments of expo, so I don't get what you mean"
- Decision: "okay then we have to test it in production, and if it didn't work we can fix it"
