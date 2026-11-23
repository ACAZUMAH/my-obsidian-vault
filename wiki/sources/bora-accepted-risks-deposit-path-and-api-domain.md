---
type: source
status: active
created: 2026-11-19
updated: 2026-11-19
tags: [bora-capital, backend, security, rate-limiting, payments, paystack, digitalocean, dns]
sources:
  - ../../raw/sources/2026-11-19-bora-accepted-risks-deposit-path-and-api-domain.md
source_date: 2026-11-19
ingested: 2026-11-19
confidence: high
---

# Bora Accepted Risks, Deposit Path, And API Domain

## Source

- Raw file: [Direct user evidence](../../raw/sources/2026-11-19-bora-accepted-risks-deposit-path-and-api-domain.md)
- Date: 2026-11-19
- Author: Direct user (repository owner) statements in a Claude Code session, relayed by that session; repository facts checked against the local `bora-capital-backend` checkout
- Ingested: 2026-11-19

## Core Claims

- The signup cap is 200 per IP per hour (`src/services/auth/signupLimit.ts`, `max: 200`, scope `SIGNUP_IP`), raised from 20 in `8da3912` (2026-10-30) because Ghanaian mobile carriers put many customers behind one IP. Do not lower it.
- Accepted risks, never to be re-flagged in audits: a stolen, unlocked customer phone is outside the system's protection (`resetUserPassword` needs no step-up on a valid session); staff who are also customers keep admin permissions on customer-app and biometric sessions, because the customer app uses no admin APIs; customers may open several CIS accounts under the same portfolio; production CORS deliberately allows Apollo Studio and the `:6443` portal for frontend debugging.
- `Mutation.depositCash` (customer-callable direct BCL deposit, client-controlled amount, no payment) was removed from the schema, resolver, and shield on 2026-11-19, uncommitted and not yet deployed. The Paystack path (`initializeDepositPayment` → verification or webhook → BCL sync) is the only deposit path.
- Production API: DigitalOcean App Platform at `api-production-bora-x7evx.ondigitalocean.app`, behind App Platform's Cloudflare-fronted ingress.
- `boracapital.com` is not Bora's (Afternic/GoDaddy parking, private registrant since 2007); never point clients at it. Bora's domain is `boradvisors.com` (DNS at Bluehost). The recommended API custom domain is `api.boradvisors.com`: add it in DigitalOcean and CNAME it to the App Platform alias, not through cPanel's "Create a domain". Never proxy the API through the shared cPanel hosting.
- Moving the app to a new API host needs a new mobile build, because the app pins the `ondigitalocean.app` certificate.

## Useful Details

- The CORS origins live in `src/common/constants/index.ts` (`https://studio.apollographql.com`, `https://portal.boradvisors.com:6443`); Helmet's `connectSrc` also lists the `:6443` portal.
- Commit `8da3912` also set a 120-calls-a-minute per-IP flood guard on the public auth operations; the real limits stay durable and per phone number, account, or code.
- Open item, not a decision: the Paystack LIVE webhook URL is not set in the Paystack dashboard, production has stored zero webhook events, and deposits confirm only through app polling of the verify path. Target: `https://api-production-bora-x7evx.ondigitalocean.app/payments/paystack/webhook`, or the `api.boradvisors.com` equivalent once live.

## Connections

- [[../projects/bora-capital-backend|Bora Capital Backend]] — signup cap, accepted risks, deposit path, production host, and webhook open item.
- [[../projects/bora-capital-mobile-app|Bora Capital Advisors Mobile App]] — certificate pinning ties an API host change to a new build; the app already uses only the Paystack deposit path.
- [[bora-client-ip-app-platform|Bora Client IP Behind DigitalOcean App Platform]] — earlier record of the 20-per-hour signup cap.

## Contradictions Or Tensions

- Supersedes the flat 20-per-IP-per-hour signup cap recorded on 2026-10-12 in [[bora-client-ip-app-platform|Bora Client IP Behind DigitalOcean App Platform]]; the code has held 200 since 2026-10-30.
- Supersedes the project page's "legacy direct-deposit mutation remains for compatibility" and its open `depositCash` concern, once deployed.

## Open Questions

- When will the Paystack LIVE webhook URL be configured, and will it follow the move to `api.boradvisors.com`?
- When will the `depositCash` removal be committed and deployed, and does the admin portal or any script still call it?
