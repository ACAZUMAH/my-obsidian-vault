# Bora refreshToken session limit

Date: 2026-10-12
Source: direct user approval ("go") of the second rate-limiting follow-up, with repository inspection.

The `refreshToken` shield limit was 10 per minute per caller IP. Customers behind one carrier IP shared it, and a blocked refresh can sign customers out. Refresh tokens are signed JWTs that rotate on every refresh, so a per-IP limit protects nothing beyond flood control, and a per-token key would reset on every rotation.

Implemented: `rateLimitRule` accepts an optional `getKey(args, ctx)` (default: caller IP; undefined skips the limit). `refreshToken` is now `chain(per-IP 120 per minute flood guard, per-session 10 per minute)`. The session key comes from the verified refresh JWT: `session:<sid>` for session-bound tokens and `user:<id>` for legacy tokens. Unverifiable tokens get only the IP limit, and the resolver rejects them. Access tokens last 15 minutes, so normal clients refresh far below the session limit.

Inspection also confirmed that `rotateSessionTokens` revokes the whole session family when a refresh token is reused. Two parallel refreshes with the same token therefore sign the user out, so both frontends must run a single refresh at a time and queue other requests. The app and admin handoffs now say so.
