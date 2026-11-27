# LivelyCura: SERLP Dispatch offer ringing uses packages, ringtone 1C, Android speed first (decided 2026-11-27)

- Date: 2026-11-27
- Author: the product owner, in a LivelyCura Claude Code session
- Recorded from: the owner's own messages (quoted verbatim below) and what the session built under them
- Feature: SERLP Dispatch (repo livelycura-courier-mobile, branch `feature/redesign`) delivery offers that keep ringing until the rider answers; builds on the 2026-11-26 decision
- Status when recorded: built, not committed; app checks pass; iPhone 17 Pro Max simulator push tests pass; Android emulator and real-phone checks not done

## The owner's words (verbatim)

- After the custom Android module was built: "first of all you did show sounds we would use for me to select the best one, and if there is a package for the android I suggest we use that rather than building a module and we need to test it to so I don't know if the simulators support that"
- Asked which Android route: "notify-kit route"
- After the review found gaps in the package route: "I don't want us to build any module we either use the package and make sure it works, about the ringtones 1 is okay but it has to be something disturbing." and "one thing you have to keep in head we need the app to efficient, accepting order deliveries and performing actions needs to be quit and know that in ghana here most of the riders uses androids phone so efficiency is an important thing here"
- Ringtone and the locked-phone gap: "ringtone I pick 1c, and about the phone locked thing let's go with the package route, since it only happens when their phone falls back asleep I don't think riders will allow their phones sleep that long"
- On the simulator used for testing: "I have the app open in the 17promax simulator in this context why do you keep opening it in the 17pro simulator in a different context??"

## How the session applied it

- No custom native module. Android offer pushes stay data-only; Expo's own background notification task (expo-notifications + expo-task-manager) receives them in every app state and posts the looping alert with react-native-notify-kit 10.10.1 (maintained Notifee fork; linked on Android only through react-native.config.js). The in-app ring uses expo-audio (media volume) on both phones.
- expo-task-manager updated from 57.0.14 to 57.0.24 (same SDK): 57.0.21 fixed a bug where opening the app within about 2 s of a background push run left Expo's task manager unregistered, stopping later rings and background location; 57.0.23 fixed timers in background tasks on React Native 0.86.
- Ringtone 1C: the existing offer chime climbing in three steps, back to back, about 11 dB louder than the first ringtone.
- Accepted gap: when the app was fully closed, the app's code needs 1–3 s to start and nothing keeps the phone awake meanwhile, so a locked idle phone can ring late (worst case the next 30 s repeat). While a rider is Working the app keeps running in the background and the gap does not apply.
- Weak-data work: the open app rings the moment the push arrives; offer requests are waited on for 10 s and stopped at 25 s, a late answer still shows the offer; the server's "offer gone" answer (FORBIDDEN) removes the offer; tapping the Android alert opens that offer directly; 30 s repeats no longer refetch lists; the background run stays warm while an offer rings.
