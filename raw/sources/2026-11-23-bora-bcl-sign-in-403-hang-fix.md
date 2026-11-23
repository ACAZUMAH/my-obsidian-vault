# Bora: BCL sign-in 403 hang fixed

Date: 2026-11-23
Source: owner approval and repository change in a Claude Code session on `bora-capital-backend`, branch `feature/updates`, on top of `1ab2559`. The change is uncommitted.

## The owner's words (verbatim)

After the agent explained the hang and showed a reproduction (see `2026-11-23-bora-a4-wording-approved-bcl-email-case-deferred.md`), the owner answered the agent's question, "Apply the BCL sign-in 403 fix?", with:

> Yes, fix it

## Change

**`src/services/bcl/client.ts`, response interceptor**
- It retries a 403 once after renewing the token, unless the failed request is the sign-in itself (`isTokenRequest`: the request URL contains `/auth/generate`, the same check the request interceptor uses to skip the token header).
- The comment says why: the sign-in's retry would wait on the very token request that failed, which never settles, so every later BCL call would wait on it until a restart.
- With the fix:
  - A 403 on the sign-in fails the call at once.
  - `tokenRefreshPromise` is cleared.
  - The next call signs in afresh.
  - The existing `isBclAuthFailure` / `isBclNotReached` in `src/services/bcl/replies.ts` treat that failure as a server error that never reached BCL.

**New spec, `tests/unit/services/bcl/clientSignInRefusal.spec.ts`**
- It runs the real client, interceptors included, against a fake BCL adapter.
- It resets the singleton's token state between tests, and reports a hang as "still waiting" after 1 s instead of timing the test out.
- Three tests:
  1. A 403 on the sign-in rejects at once with that 403, after one request.
  2. The next call signs in again and succeeds once BCL accepts.
  3. An expired token on another call is still renewed and that call retried once (`sign-in, call, sign-in, call`).

## Verification

- **Full suite:** 217 suites, 2,026 tests. `tsc --noEmit`, `yarn build` and the Prettier check pass.
- **Mutation checks:** 3, all caught.
  - Guard made ineffective (`isTokenRequest || !isTokenRequest`): 2 tests fail.
  - Every request treated as the sign-in: the retry test fails.
  - Wrong URL (`/auth/signin`): 3 tests fail.
  - An earlier variant that deleted the guard only produced a type error (unused variable) and was replaced.

## Notes

- **Not changed:** the 1-minute token cache, a decided item.
- **No frontend handoff:** the change is backend only.
