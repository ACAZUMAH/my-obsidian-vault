# Bora backend: signup cap, accepted risks, depositCash removal, API domain and Paystack webhook

Date: 2026-11-19
Source: direct statements by the user (repository owner) in a Claude Code session on `bora-capital-backend`, relayed to the vault-writing agent by that session (paraphrased). Repository facts were checked the same day against the local checkout: `src/services/auth/signupLimit.ts`, `git show 8da3912`, `src/common/constants/index.ts`, `src/graphql/auth`, `src/graphql/transactions`, `src/routes/payments.router.ts`, and `git status`/`git diff --stat`. No secret-bearing file was read.

## Signup per-IP cap

The signup cap is 200 per IP per hour, not 20. `src/services/auth/signupLimit.ts` holds `max: 200` with a one-hour window (scope `SIGNUP_IP`). It was raised from 20 in commit `8da3912` (2026-10-30, "fix(rate-limits): stop per-IP limits refusing customers on shared mobile IPs"), because Ghanaian mobile carriers put many customers behind one IP and the 20-per-hour cap refused them at peak times. The same commit gave the public auth operations a per-IP flood guard of 120 calls a minute (`publicIpFloodGuard`), with the real limits durable and per phone number, account, or code. User instruction: do not lower the signup cap.

## Accepted risks (never re-flag in audits)

1. A stolen or unlocked customer phone is outside the system's protection. `resetUserPassword(newPassword)` needs only a valid session (`isAuthenticated`), with no step-up, and that is accepted.
2. Staff who are also customers keep their admin permissions on customer-app and biometric sessions. Accepted because the customer app uses no admin APIs.
3. Customers may open several CIS accounts under the same portfolio.
4. Production CORS deliberately includes Apollo Studio (`https://studio.apollographql.com`) and the `:6443` portal origin (`https://portal.boradvisors.com:6443`, in `src/common/constants/index.ts`) for frontend debugging.

## depositCash removed

`Mutation.depositCash`, a customer-callable direct BCL deposit with a client-controlled amount and no payment, was removed from the GraphQL schema, resolver, and shield in the working tree on 2026-11-19. At recording the removal is uncommitted and not deployed (`git status` shows `src/graphql/transactions/typeDefs.ts`, `resolvers.ts`, `src/graphql/shield/transactions.ts`, generated types, and two specs modified; the specs assert the mutation is gone). The Paystack path, `initializeDepositPayment` then verification or webhook then BCL sync, is the only deposit path.

## Infrastructure

- The production API runs on DigitalOcean App Platform at `api-production-bora-x7evx.ondigitalocean.app`, behind App Platform's Cloudflare-fronted ingress.
- `boracapital.com` is not controlled by Bora: its nameservers are `ns1.afternic.com` and `ns2.afternic.com` (GoDaddy parking), with a private registrant since 2007. Never point clients at it.
- Bora's own domain is `boradvisors.com`, with DNS at Bluehost.
- Recommended API custom domain: `api.boradvisors.com`, added to the app in DigitalOcean and pointed by a CNAME to the App Platform alias. Do not use cPanel's "Create a domain" for it.
- Switching the mobile app's API host needs a new mobile build, because the app pins the `ondigitalocean.app` certificate.
- Never proxy the API through the shared cPanel hosting.

## Open item (state, not a decision)

The Paystack LIVE webhook URL is not configured in the Paystack dashboard. Production has stored zero webhook events, so deposits currently confirm only through app polling (the verify path). Target URL: `https://api-production-bora-x7evx.ondigitalocean.app/payments/paystack/webhook`, or the custom-domain equivalent once `api.boradvisors.com` is live. The route is `POST /payments/paystack/webhook` (`src/routes/payments.router.ts`).
