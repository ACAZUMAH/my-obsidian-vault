---
type: source
status: active
created: 2026-10-21
updated: 2026-10-21
tags: [bora-capital, backend, conventions, typescript]
sources:
  - ../../raw/sources/2026-10-21-bora-single-input-object-convention.md
source_date: 2026-10-20
ingested: 2026-10-21
confidence: high
---

# Bora Service Functions Take One Input Object

## Source

- Raw file: [Service functions take one input object](../../raw/sources/2026-10-21-bora-single-input-object-convention.md)
- Date: 2026-10-20
- Author: User correction, implemented by the agent
- Ingested: 2026-10-21

## Core Claims

- Functions take one input object typed by an interface, not separate positional parameters (user correction, 2026-10-20).
- When a function needs values that are not part of the object it forwards, extend the input interface (for example `RegisterInput extends CreateUserInput`) and strip the extra fields before forwarding. Do not add them to a shared interface other callers use.

## Useful Details

- Adding `ip` to the shared `CreateUserInput` broke staff invites and made every signup fail, because `createUser` validates with `additionalProperties: false`.
- Converted: `register`, `verifyOtpAndSignJwt`, `revokeSession`, `revokeAllUserSessions`, `revokeSessionFamily`, `getUserPushTokens`, `getPushTokensByUserIds`.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]]
- [[bora-push-device-binding|Bora Push Notifications Bound To Device And Session]]

## Contradictions Or Tensions

- Many older services still take positional parameters; the user has not asked for a wholesale conversion.

## Open Questions

- None.
