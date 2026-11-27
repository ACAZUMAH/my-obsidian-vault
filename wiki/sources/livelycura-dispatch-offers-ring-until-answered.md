---
type: source
status: active
created: 2026-11-26
updated: 2026-11-27
tags: [livelycura, courier, notifications, push, android, ios, decision]
sources:
  - ../../raw/sources/2026-11-26-livelycura-dispatch-offers-ring-until-answered.md
  - ../../raw/sources/2026-11-27-livelycura-dispatch-ringing-packages-and-ringtone.md
source_date: 2026-11-26
ingested: 2026-11-26
confidence: high
---

# LivelyCura Dispatch Offers Ring Until Answered

## Source

- Raw file: [SERLP Dispatch delivery offers keep ringing until the rider answers](../../raw/sources/2026-11-26-livelycura-dispatch-offers-ring-until-answered.md)
- Raw file: [Ringing uses packages, ringtone 1C, Android speed first](../../raw/sources/2026-11-27-livelycura-dispatch-ringing-packages-and-ringtone.md) (2026-11-27)
- Date: 2026-11-26
- Author: Product owner (verbatim request and answer), with the session's built design
- Ingested: 2026-11-26

## Core Claims

- SERLP Dispatch delivery offers and assignments keep ringing until the rider accepts or declines, like inDrive's driver app, so riders don't miss requests (owner: "Yes, build it").
- App open: the offer sheet loops a 24-second ringtone and vibrates, even on silent. Background or closed: Android posts one insistent alert (re-posted every 30 s); iPhone gets a time-sensitive ringtone alert every 30 s while the offer is open.
- An "offer closed" message stops Android ringing; who rings is unchanged (broadcasts only while Working, direct assignments always); older builds keep the single chime.
- The customer-side "rider is here" ringing is not started; who rings (receiver at drop-off or shop at pickup) is still the owner's choice.
- 2026-11-27: packages only, no custom native module ("notify-kit route"; "I don't want us to build any module"): Expo's background notification task receives Android offer pushes and react-native-notify-kit posts the looping alert; ringtone 1C (louder rising chime); the short start-up gap on a fully closed app is accepted; speed on low-end Android and weak data comes first.

## Useful Details

- Contract and plan: livelycura-hq `docs/dispatch-ringing-offers-2026-11/plan.md`; capability `COURIER_DELIVERY_OFFER_RING_V1`, channel `courier-delivery-offer-ring-v1`, sound `dispatch_offer_ring.wav` (ringtone 1C). Android: react-native-notify-kit 10.10.1 (Android only via `react-native.config.js`) + expo-task-manager ~57.0.24 background task; the earlier custom module `modules/dispatch-offer-ring` was removed (never committed).
- Lesson: expo-task-manager before 57.0.21 (SDK 57) drops its task manager when the app is opened within about 2 s of a headless background run, silently stopping later background tasks (offer rings and background location); update to the SDK's latest patch. Before 57.0.23, JS timers can hang in background tasks on React Native 0.86.
- Lesson: Expo's background notification task runs for data-only pushes in every app state, but nothing holds a wake lock between the push and the task finishing; a locked idle phone can delay a cold start.
- Lesson: an Expo push with title, body or channelId is an FCM notification message on Android, so in the background the OS shows it and the app never sees it. Looping alerts need data-only Expo messages. While the app is in front, Expo's own received-listener does get data-only pushes (ExpoHandlingDelegate), so don't handle them twice.
- Lesson: bare `android`/`ios` lines in `.easignore` drop local modules' native folders from EAS builds; anchor them as `/android` and `/ios`.
- Lesson: on Android 12+, an insistent notification first posted during a call stays silent on later re-posts; cancel and post it fresh after the call.
- Needs a new store build (expo-audio, the native module, the time-sensitive entitlement); real-phone checks are the owner's.

## Connections

- Applies to [[../projects/livelycura-courier-mobile|LivelyCura Courier Mobile]] and [[../projects/livelycura-backend|LivelyCura Backend]].

## Contradictions Or Tensions

- None.

## Open Questions

- Customer-side "rider is here" ringing: which party rings and in which app.
