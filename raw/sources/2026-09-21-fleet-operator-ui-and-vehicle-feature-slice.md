# Fleet Operator UI And Vehicle Feature Slice

- Date: 2026-09-21
- Source: Direct user correction in Codex
- Projects: LivelyCura Backend and LivelyCura Pharmacy Portal

## Direct Correction

- Improve Fleet operator details using the established CRM Customer and Catalog Product detail-page patterns, and improve the profile-image presentation.
- Rebuild Fleet one feature at a time. For each feature, correct backend services and comments, GraphQL resolvers and type definitions, then build its complete Pharmacy Portal UI before exposing it.
- Service functions receive one object parameter named `data`, not positional `input` and `actorUser` arguments or `{ principal, input }` wrappers.
- A resolver passes only the authenticated actor user ID when the service needs an actor. The service fetches that user and owns the relevant model reads and writes.
- Review later Fleet backend areas against the established project architecture before presenting them for review.

## Verified Resolution

- Operator details now use a routed summary-and-tabs record page with a private profile-photo preview, initials fallback, useful profile/work/compliance information, and conditional archive context.
- Vehicle services, GraphQL, list, dedicated create page, update/archive actions, routed details, seat layout, and private-document previews now follow the accepted feature ownership and data-object boundaries.
- Backend TypeScript and focused backend/frontend lint checks pass. Database-dependent execution remains deferred while the development host cannot resolve the MongoDB SRV record.
