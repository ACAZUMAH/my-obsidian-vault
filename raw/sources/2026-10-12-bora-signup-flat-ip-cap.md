# Bora signup flat IP cap

Date: 2026-10-12
Source: direct user instruction ("move to 3") for the third rate-limiting follow-up, with repository inspection.

Signup used `reserveAuthIpRequest`: an escalating cooldown per hashed IP in `authRequestThrottles` (30 seconds, doubling to 1 hour, reset only after 24 idle hours). One busy carrier or office IP could therefore lock out signups for a day. Signup sends the code by both email and SMS, so a per-IP cap is still needed against SMS cost abuse, and keying signup on email would not help because attackers use new emails.

Implemented: a generic durable fixed-window limiter, `createRateLimitWindow` (`src/services/auth/rateLimitWindows.ts`), in a `rateLimitWindows` collection keyed by `{ scope, keyHash }` with a TTL on `windowEndsAt`. The sign-in password lock from 2026-10-11 now uses scope `SIGNIN_PASSWORD` (5 per 15 minutes); the earlier `signinAttempts` model was never deployed and was folded in. Signup uses scope `SIGNUP_IP` through `reserveSignupFromIp`: a flat 20 signups per IP per hour, after the existing-user check and before user creation. `reserveAuthIpRequest` and the `ipHash` field and index on `authRequestThrottles` were removed; that collection now holds per-user OTP cooldowns only. Existing production `ipHash` records expire through their TTL, and the old index `ipHash_1_action_1` can be dropped manually.

The 20-per-hour value is a judgment call between SMS-abuse cost and customers sharing an IP, and can be tuned. Signup accepts any valid international phone number, so an attacker spreading across many IPs can still trigger SMS to arbitrary numbers. That needs provider-side fraud controls or country restrictions, not per-IP limits.
