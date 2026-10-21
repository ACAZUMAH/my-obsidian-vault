---
type: source
status: active
created: 2026-10-11
updated: 2026-10-13
tags: [bora-capital, backend, security, rate-limiting, digitalocean]
sources:
  - ../../raw/sources/2026-10-11-bora-client-ip-app-platform.md
  - ../../raw/sources/2026-10-11-bora-signin-password-lock.md
  - ../../raw/sources/2026-10-12-bora-refresh-token-session-limit.md
  - ../../raw/sources/2026-10-12-bora-signup-flat-ip-cap.md
  - ../../raw/sources/2026-10-13-bora-refresh-token-limit-removed.md
source_date: 2026-10-11
ingested: 2026-10-11
confidence: high
---

# Bora Client IP Behind DigitalOcean App Platform

## Source

- Raw file: [Direct user evidence](../../raw/sources/2026-10-11-bora-client-ip-app-platform.md)
- Follow-up: [Sign-in password lock](../../raw/sources/2026-10-11-bora-signin-password-lock.md), direct user request on 2026-10-11.
- Follow-up: [refreshToken session limit](../../raw/sources/2026-10-12-bora-refresh-token-session-limit.md), direct user approval on 2026-10-12.
- Follow-up: [Signup flat IP cap](../../raw/sources/2026-10-12-bora-signup-flat-ip-cap.md), direct user instruction on 2026-10-12.
- Follow-up: [refreshToken limit removed](../../raw/sources/2026-10-13-bora-refresh-token-limit-removed.md), direct user approval on 2026-10-13; supersedes the 2026-10-12 refreshToken limits.
- Date: 2026-10-11
- Author: Direct user review request and decisions, with repository inspection and DigitalOcean documentation
- Ingested: 2026-10-11

## Core Claims

- On App Platform, the caller's IP is in `do-connecting-ip`; `X-Forwarded-For` holds DigitalOcean's ingress address. Express `trust proxy` cannot recover the caller, and `trust proxy: true` would let callers forge the rate-limit key.
- Bora resolves the caller IP with `getClientIp` (`src/common/helpers/clientIp.ts`) in both the HTTP GraphQL and WebSocket contexts: `do-connecting-ip` when it is a valid IP, otherwise the socket address. `trust proxy` stays unset.
- The API currently points straight at App Platform. When the user's own Cloudflare zone goes in front, `do-connecting-ip` becomes a Cloudflare edge address and all limits become shared again; switch to `CF-Connecting-IP`, trusted only when `do-connecting-ip` is in Cloudflare's published ranges, because the `*.ondigitalocean.app` starter domain stays directly reachable.
- Per-IP limits are only a flood guard; account protection keys on the customer. OTP sends (`reserveAuthRequest`) and OTP guesses (`MAX_CODE_ATTEMPTS`) were already per customer. Sign-in passwords now allow 5 attempts per phone number per 15 minutes (`reserveSigninAttempt`, scope `SIGNIN_PASSWORD`, phone stored as a hash). Each attempt is spent before the password check, unknown numbers are counted alike, and a correct password, code-based reset, or authenticated password change clears the counter.
- `refreshToken` is not rate limited (explicit `allow` policy, 2026-10-13). The signed, single-use token is the credential, and reuse detection is the protection. A limit only caught client loops and had blocked customers sharing an IP. The 2026-10-12 per-IP and per-session limits and the `getKey` option were removed.
- Durable per-key limits use `createRateLimitWindow` (`rateLimitWindows` collection, unique `{ scope, keyHash }`, TTL on `windowEndsAt`), with attempts spent atomically before the guarded action. Signup is capped at a flat 20 per IP per hour (`reserveSignupFromIp`, scope `SIGNUP_IP`). This replaces the escalating `reserveAuthIpRequest` cooldown; `authRequestThrottles` now holds per-user OTP cooldowns only.
- Clients must run one refresh at a time: `rotateSessionTokens` treats a reused refresh token as theft and revokes the whole session family, so two parallel refreshes sign the user out.

## Useful Details

- Before the fix, every shield `rateLimitRule` and the escalating signup cooldown (`reserveAuthIpRequest`, 30 seconds to 1 hour, 24-hour reset) keyed on DigitalOcean's ingress address, so they applied to all customers combined.
- An IP is not a customer: carrier-grade NAT and shared Wi-Fi put many customers behind one IP, and one customer can use many IPs.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]

## Contradictions Or Tensions

- The original review assumed Cloudflare and `X-Forwarded-For`; on App Platform that header is DigitalOcean's ingress address, so the proposed `trust proxy` fix would not work.

## Open Questions

- Is 20 signups per IP per hour right once real traffic is seen? Per-IP caps cannot stop SMS abuse spread across many IPs; signup accepts any international number, so provider fraud controls or country restrictions are the remaining defense.
- Should the leftover production index `ipHash_1_action_1` on `authRequestThrottles` be dropped?
- Does App Platform overwrite a caller-supplied `do-connecting-ip`? DigitalOcean's documentation says it adds the header; confirm in production.
