# Bora BCL Error Passthrough And Secret-File Boundary — Direction And Implementation

Date: 2026-10-11
Source: direct user direction in Claude Code during Bora backend work on `bora-capital-backend` (2026-10-11)

## User Direction

- When the agent offered to call the staging BCL API using values from the repository's `.env`, the user replied: "no don't read my .env, there are secrets there I don't want you to compromise them".
- On how BCL `fetchdata` errors should reach the frontend, the user said: "we don't have to know the shape for b what ever that is returned will be send to the frontend, if you check how they build the apis status codes are wrong all you need is the descriptions and the description explains what happened".
- The user approved applying the same error rule to Grow Wealth.

## Agent Evidence

- No `.env` or other secret-bearing file was read. Live BCL calls that need credentials are left for the user to run.

## Implemented Scope

- Every BCL `POST /api/partner/fetchdata` call goes through one shared `fetchBclData` in `src/services/bcl/fetchData.ts`.
- A non-zero BCL `Status[0].Status`, or a BCL `Message`, becomes a 400 (`BAD_REQUEST`) carrying BCL's `Description` or `Message`. The GraphQL error formatter shows that text to the client.
- A 502 (`BAD_GATEWAY`, message hidden) is used only when BCL cannot be reached or returns an unreadable envelope or malformed rows.
- Grow Wealth (`LinkedPortfolio`, `LinkedPortfolioValuation`) was moved onto `fetchBclData`.
- New lookups queries, both `isAuthenticated`:
  - `getCurrencies`: BCL RequestID `Currency`, no `xmlDetail`.
  - `getCurrencyRates`: BCL RequestID `CurrencyRate`, XML `<Request><CurrencyCode/><FromDate/><ToDate/></Request>` with `MM/DD/YYYY` dates; response `Date` uses `DD MMM YYYY`.

## Open With BCL

The user is asking BCL:

- Which direction the currency rate is quoted in.
- Whether rate requests must match the customer's KYC currency.
