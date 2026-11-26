# LivelyCura: SERLP Dispatch delivery offers keep ringing until the rider answers (decided 2026-11-26)

- Date: 2026-11-26
- Author: the product owner, in a LivelyCura Claude Code session
- Recorded from: the owner's own messages (quoted verbatim below) and the design the session built under them
- Feature: the rider app SERLP Dispatch (repo livelycura-courier-mobile, branch `feature/redesign`) and the backend (repo livelycura-backend, branch `feature/hrm`)
- Status when recorded: approved and built, not yet committed; Android Kotlin compiles; app and backend tests pass; nothing checked on a real phone yet (needs a new store build)

## The owner's words (verbatim)

- The request: "okay now the next thing to work on is the notification of the app we a new request or assignment comes comes in on the dispatch app. I have experience some on the indrive apps, so when a new driver request comes in the phone keeps ringing until the driver declines or accepts, and also when a river gets to pick up location, the customer's phone to keeps ringing showing the driver is here untill you tap I am coming so I want us to add that for the dispatch app so that the riders don't sit there without accepting requests because they simply didn't pay attention"
- Asked "Build the rider ringing as recommended?", the owner answered: "Yes, build it"

## What was built

- App open: the offer sheet loops a 24-second ringtone (made from the existing offer chime) and vibrates, even on silent, until the rider slides Accept or Decline, the offer closes or it runs out. Android plays it on the alarm volume; iPhone on the media volume.
- App in the background or closed, Android: one alert that keeps ringing (insistent) until opened, closed or expired, posted again every 30 seconds so it rings again after the shade is opened, the alert is swiped away or a call cut it off.
- App in the background or closed, iPhone: a time-sensitive alert with the 24-second ringtone, sent again every 30 seconds while the offer is open and unanswered.
- An "offer closed" message stops Android ringing at once; the phone remembers closed offers so a late repeat can't ring again.
- Same rules as before for who rings: broadcast offers only while the rider is Working; direct assignments always. Older app builds keep the single chime. A signed-out Android phone never rings.
- Known limits: iPhone silent switch mutes background alerts; the last iPhone alert can ring up to about 24 seconds after the offer closes; the iPhone in-app ring follows media volume; an iPhone signed out with no signal can keep ringing for an open direct offer until the app is opened or the offer ends.
- The customer-side "rider is here" ringing was not started: who should ring (the receiver at drop-off, or the shop at pickup) is still the owner's choice.

## Technical lessons from the build

- An Expo push with a title, subtitle, body, icon or channelId reaches Android as an FCM notification message: with the app in the background or closed, Android shows it itself and the app's code never runs, so it can't loop. Android ring offers therefore go as data-only Expo messages (alert text inside `data.ring`; no top-level `title` or `message` in data, or Expo shows it itself), handled by the app's own FirebaseMessagingService (a local Expo module registered above Expo's service). With the app on screen, Expo drops data-only messages before JS, so the module hands them to JS through an event.
- A bare `android` or `ios` line in `.easignore` or `.gitignore` matches every folder of that name, so EAS builds silently drop a local module's `android` folder; anchor them as `/android` and `/ios`.
- On Android 12+, re-posting an insistent ringtone notification that was first posted during a call counts as an "insistent update" and stays silent; cancel it and post it fresh once the call is over.
