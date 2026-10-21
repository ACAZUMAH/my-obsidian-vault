# Bora Campaign SMS Hold — Decision And Implementation

Date: 2026-10-01
Source: direct user direction in Claude Code during Bora backend work (2026-10-01)

## User Direction

- The user needs to investigate the Hubtel SMS API first, so bulk SMS sending must be put on hold before the branch is pushed, so that it cannot affect anything. The user will check Hubtel later, and SMS campaigns will be added back then.

## Agent Evidence

- Bora has no Hubtel batch integration. Campaign SMS is sent one message at a time by the delivery worker through the single-send endpoint, and campaign test sends call it directly. OTP and transaction SMS use separate direct sends.
- `.env.default` is ignored by git (`.env*` in `.gitignore`) and has never been tracked. No tracked file lists `API_PUBLIC_URL`, `UNSUBSCRIBE_TOKEN_SECRET`, or `UPLOADS_BASE_URL`, so the deployment must be configured from other notes.

## Implemented Scope

- Campaign SMS is enabled only when `CAMPAIGN_SMS_ENABLED` is exactly `true`; unset or any other value keeps the hold.
- While on hold, scheduling, sending, or testing a campaign that includes SMS returns 400 "SMS campaigns are on hold; remove the SMS channel", and campaign dispatch queues no SMS, even for campaigns scheduled earlier. Drafts may still store SMS text. SMS already queued before a hold is switched on is not cancelled by the flag; cancelling the campaign skips it.
- The admin handoff tells the portal to hide the SMS option and the preview's SMS count.
- Verification: build passed; 142 test suites and 888 tests passed; 6 mutations were killed.
