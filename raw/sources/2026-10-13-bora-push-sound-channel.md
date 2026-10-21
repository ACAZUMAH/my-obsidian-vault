# Bora push notification sound and channel

Date: 2026-10-13
Source: direct user question and decision.

The user asked whether the app could use a custom notification sound with no backend work. The agent explained the split. On Android, the sound comes from the notification channel, so the app alone can control it. On iOS, the push plays the sound file named in the payload, and the backend was sending `sound: 'default'` (five senders; the auto top-up reminder set no sound and arrived silent on iOS). An app-only iOS workaround would need a native Notification Service Extension.

The user chose `sound: "bora_signature_v1.wav"` for iOS and `channelId: "bora_updates_v1"` for Android.

Implemented: constants `pushNotificationSound` and `pushNotificationChannelId` in `src/common/constants`. `sendPushNotification` (`src/services/notifications/push.ts`), which every push goes through, applies both as defaults that a message may override. The per-sender `sound: 'default'` values were removed. The app must bundle the file and create the channel at startup; channel sounds cannot change after creation, so a sound change ships as a new versioned file and channel ID together. The frontend instructions are in `docs/frontend-handoff-2026-10-13.md`.

Addendum (same day): the mobile developer sent an AI-generated proposal adding per-token `capabilities` and `appVersion` to `AddUserExpoPushTokenInput`, sending `channelId` only to devices reporting `BORA_SOUND_V1`, a feature switch, a per-type sound list, and Expo receipt checks. Expo's documentation confirms that an Android push naming a channel missing on the device is not displayed; iOS plays the default sound when the named file is missing. The user noted that the app is not in production and that local Expo builds require a reinstall each time, so capability gating, `appVersion`, and the switch are unnecessary. The backend keeps sending the sound and channel on every push, and the handoff tells testers to reinstall the new build. Two entries in the proposed per-type list (`SUPPORT_CASE_CREATED`, `SUPPORT_CUSTOMER_REPLIED`) are staff notifications, which never push.
