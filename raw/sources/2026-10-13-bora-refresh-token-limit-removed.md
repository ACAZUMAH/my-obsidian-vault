# Bora refreshToken rate limit removed

Date: 2026-10-13
Source: direct user question ("is it really necessary to rate limit it?") and approval ("go").

Assessment given to the user: refresh tokens are signed JWTs, so they cannot be guessed. A stolen token needs only one refresh, and the real protection is rotation with reuse detection, which revokes the session family. Fake tokens fail a cheap signature check before any database work. A valid-token flood costs no more than any authenticated query, none of which are rate limited, and the REST `/auth/refresh` endpoint never had a limit. The per-session limit added on 2026-10-12 only caught client refresh loops, which are app bugs, and a 429 could leave the user stuck. The original per-IP limit had actively blocked customers sharing an IP.

Implemented: `refreshToken` has an explicit `allow` shield policy with a comment explaining why. The per-IP (120/min) and per-session (10/min) limits and the `rateLimitRule` `getKey` option were removed, so `rateLimitRule` is back to its committed per-IP form. The test now asserts that 50 refreshes from one IP all pass. The frontend "refresh one at a time per device" requirement stays, because it prevents reuse-detection sign-outs regardless of rate limits.
