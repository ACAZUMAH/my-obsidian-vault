---
type: source
status: active
created: 2026-11-26
updated: 2026-11-26
tags: [livelycura, courier, notifications, push, android, ios, decision]
sources:
  - ../../raw/sources/2026-11-26-livelycura-dispatch-offers-ring-until-answered.md
source_date: 2026-11-26
ingested: 2026-11-26
confidence: high
---

# LivelyCura Dispatch Offers Ring Until Answered

## Source

- Raw file: [SERLP Dispatch delivery offers keep ringing until the rider answers](../../raw/sources/2026-11-26-livelycura-dispatch-offers-ring-until-answered.md)
- Date: 2026-11-26
- Author: Product owner (verbatim request and answer), with the session's built design
- Ingested: 2026-11-26

## Core Claims

- SERLP Dispatch delivery offers and assignments keep ringing until the rider accepts or declines, like inDrive's driver app, so riders don't miss requests (owner: "Yes, build it").
- App open: the offer sheet loops a 24-second ringtone and vibrates, even on silent. Background or closed: Android posts one insistent alert (re-posted every 30 s); iPhone gets a time-sensitive ringtone alert every 30 s while the offer is open.
- An "offer closed" message stops Android ringing; who rings is unchanged (broadcasts only while Working, direct assignments always); older builds keep the single chime.
- The customer-side "rider is here" ringing is not started; who rings (receiver at drop-off or shop at pickup) is still the owner's choice.

## Useful Details

- Contract and plan: livelycura-hq `docs/dispatch-ringing-offers-2026-11/plan.md`; capability `COURIER_DELIVERY_OFFER_RING_V1`, channel `courier-delivery-offer-ring-v1`, sound `dispatch_offer_ring.wav`, native module `DispatchOfferRing` (`modules/dispatch-offer-ring`, Android only).
- Lesson: an Expo push with title, body or channelId is an FCM notification message on Android, so in the background the OS shows it and the app never sees it. Looping alerts need data-only Expo messages and the app's own FirebaseMessagingService; in the foreground Expo drops data-only messages before JS.
- Lesson: bare `android`/`ios` lines in `.easignore` drop local modules' native folders from EAS builds; anchor them as `/android` and `/ios`.
- Lesson: on Android 12+, an insistent notification first posted during a call stays silent on later re-posts; cancel and post it fresh after the call.
- Needs a new store build (expo-audio, the native module, the time-sensitive entitlement); real-phone checks are the owner's.

## Connections

- Applies to [[../projects/livelycura-courier-mobile|LivelyCura Courier Mobile]] and [[../projects/livelycura-backend|LivelyCura Backend]].

## Contradictions Or Tensions

- None.

## Open Questions

- Customer-side "rider is here" ringing: which party rings and in which app.
