# Bora: A4 wording approved, BCL email case deferred, BCL sign-in 403 hang reproduced

Date: 2026-11-23
Source: owner messages and an agent reproduction in a Claude Code session on `bora-capital-backend`, branch `feature/updates` at `1ab2559` (pushed to origin).

## The owner's words (verbatim)

The agent listed the owner's open items, then explained items 3–5. The owner replied:

> 1. is done
> 2. is done
> 3. what bcl latter case check
> 4. what sign-in retry on 403
> 5. what deposit wording are still talking about
> 6. that will be checked you don't have to tell me

Items 1–6:
1. The production email audit.
2. Sending `docs/frontend-handoff-2026-11-22-emails.md`.
3. The BCL email letter-case check.
4. The BCL sign-in 403 retry.
5. The A4 deposit wording.
6. The live A1 settlement check after deploy.

After the explanations:

> 5 is okay, ignore 3, if there is an issue is raised in production we fix it, I only made ignore the type checking because of the staging data, but production does really have a lot of them yet so we can handle it later, now about 4 I don't really get how you want us to fix it

## Decisions

- **Production email audit:** done by the owner. The agent was not shown the result.
- **The emails handoff:** sent.
- **Post-deploy live checks (A1 settlement):** the owner checks them. Agents do not list them.
- **A4 deposit result wording:** approved as written in `docs/frontend-handoff-2026-11-22.md`, section 2:
  - `SUCCESSFUL`: title "Deposit Successful". Subtitle: "Your deposit has gone through. You'll get a confirmation message telling you when it will reflect on your portfolio."
  - Server-returned `PROCESSING`: title "Payment received". Subtitle: "Your payment has been received and your deposit is awaiting confirmation. Do not pay again."
  - `FAILED` on Home's card: title "Top-up not completed". Subtitle: "This top-up was not invested. If you were charged for it, your payment has been refunded. Contact support if you have any questions."
- **BCL email letter case, deferred:**
  - The open question was whether BCL matches `PrimaryEmail` ignoring case.
  - Statements (`fetchministatement_bcl`) and withdrawals (`addcicashwithdrawal_bcl`) send the account number, the stored email and the phone, with no identity ID.
  - Investors linked before `1ab2559` hold the app's lowercased email.
  - The owner's call: few production customers so far, so fix it only if production raises it.

## BCL sign-in 403 hang (reproduced, still undecided)

**The code:** `src/services/bcl/client.ts:44-60`.
- The response interceptor retries any 403 once after fetching a new token.
- That includes a 403 on the token request itself, `/api/auth/generateaccesstoken`.
- The retry calls `getAccessToken()`, which returns the pending `tokenRefreshPromise`: the very request that failed. The promise waits on itself and never settles.
- Its `finally` never clears it, so every later BCL call waits on the same promise until the server restarts.

**Reproduction (agent, 2026-11-23, outside the repository):** the real client was loaded with an axios adapter that answers 403 to the sign-in.
- **Current code:**
  - the first BCL call was still waiting after 3 s;
  - the second was too;
  - one request reached BCL, the sign-in.
- **Proposed fix** (skip the retry when the request URL contains `/auth/generate`):
  - both calls rejected with 403 at once;
  - each tried a fresh sign-in.
  - The existing `isBclAuthFailure` / `isBclNotReached` helpers in `src/services/bcl/replies.ts` already treat a sign-in failure as a server error that never reached BCL.

**Status:** the owner asked how the fix would work. It is not approved yet.
