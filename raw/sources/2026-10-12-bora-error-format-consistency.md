# Bora error format consistency

Date: 2026-10-12
Source: review items the user asked to verify and fix ("any go"), with the agent's reproduction against the real Apollo and Express stack.

Findings, reproduced:

- Apollo Server 5.5.1 sets `originalError` on its own parse, validation, and user-input errors (`originalError: graphqlError.originalError ?? graphqlError`). `formatGraphqlErrors` therefore unwrapped them as unknown crashes. An unknown field, a missing variable, a wrongly typed variable, or a syntax error returned HTTP 400 with "Internal server error" and `INTERNAL_SERVER_ERROR`, and each was reported to Sentry. The existing unit test missed it because it built a plain `GraphQLError` without `originalError`.
- Errors raised before GraphQL (invalid access token, unknown `client` header, broken JSON, unknown route) and REST `/auth/refresh` errors were returned by `constructHTTPResponse` as `{ data: null, errors: { message, details } }`: an object with no `extensions.code`, unlike the handoff's documented array.
- An expired OTP throws 410, which was missing from the status-to-code map, so it returned its message with `INTERNAL_SERVER_ERROR`. Body-parser's 415 had the same gap.

Implemented:

- `formatGraphqlErrors` maps Apollo's client error codes (`GRAPHQL_PARSE_FAILED`, `GRAPHQL_VALIDATION_FAILED`, `BAD_USER_INPUT`, `OPERATION_RESOLUTION_FAILURE`, `BAD_REQUEST`) to `BAD_REQUEST` with the real message, logs a warning, and does not report to Sentry. Persisted-query codes are left alone, because Apollo Client relies on them.
- The Apollo server sets `hideSchemaDetailsFromClientErrors: !isDevelopment`, so "Did you mean" field suggestions do not leak the schema now that validation messages reach clients.
- A shared `getErrorCode(status)` (`src/common/helpers/errorCodes.ts`) maps any unlisted 4xx to `BAD_REQUEST` and any other unlisted status to `INTERNAL_SERVER_ERROR`. It is used by both the GraphQL formatter and `constructHTTPResponse`.
- `constructHTTPResponse` returns errors as `[{ message, extensions: { code } }]`, which covers the Express error handler and the REST auth controller. The `details` field was unused and was dropped.
- The frontend changes are in the new `docs/frontend-handoff-2026-10-12-errors-and-accounts.md`.
