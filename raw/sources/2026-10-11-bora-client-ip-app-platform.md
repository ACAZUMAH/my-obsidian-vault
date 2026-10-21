# Bora client IP behind DigitalOcean App Platform

Date: 2026-10-11
Source: direct user review request and decisions, with repository inspection and DigitalOcean documentation.

A review reported that customers share one rate limit because the API sits behind Cloudflare and Express does not trust the proxy, and proposed `app.set('trust proxy', …)`. The user asked whether this was true and how to solve it.

Repository inspection found the GraphQL context set `ip` to `String(req.ips[0] || req.ip)` with `trust proxy` unset, so the value was the TCP peer: DigitalOcean's ingress. Every `rateLimitRule` keys on that value (signin, forgetPassword, resendOtp and authenticateExistingCustomer at 3 per minute; signup, OTP verification, onboarding completion, password recovery, biometric login and enable, staff invitation at 5; refreshToken at 10), so each limit was shared by all customers. The signup cooldown in `reserveAuthIpRequest` also keys on a hash of that IP and escalates from 30 seconds to 1 hour with a 24-hour reset, so it was effectively platform-wide.

DigitalOcean documents that App Platform adds a `do-connecting-ip` header with the client IP and uses `x-forwarded-for` for the address of its own ingress server. `trust proxy` therefore cannot recover the client, and `trust proxy: true` would make the caller-written leftmost `X-Forwarded-For` value the rate-limit key.

The user decided the API currently points straight at App Platform, and said that will change in future (their own Cloudflare zone in front). The user initially assumed one IP equals one customer; it was explained that carrier-grade NAT and shared Wi-Fi put many customers behind one IP, and one customer can use many IPs. The user approved the fix: resolve the client IP from `do-connecting-ip`, falling back to the socket address, for both HTTP and WebSocket contexts. Per-customer limit keys were agreed as a later follow-up.
