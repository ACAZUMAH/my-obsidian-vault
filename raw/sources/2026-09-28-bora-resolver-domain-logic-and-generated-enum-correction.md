# Bora Resolver Domain Logic And Generated Enum Correction

Date: 2026-09-28
Source: direct user correction in Codex

## Correction

The CIS field resolvers incorrectly contained customer-field transformation, performance filtering, and NAV date-range calculations. The NAV range argument also repeated the GraphQL enum as a handwritten string union.

## Required Direction

- GraphQL resolvers are transport-only delegates; calculations, filtering, normalization, and response construction belong to documented domain services.
- A nested field resolver may remain only when GraphQL supplies an argument at that field. It must pass the parent data and generated argument directly to the owning service.
- Import and use generated GraphQL operation argument types and enums. Do not reproduce schema enums as handwritten TypeScript string unions.
- Add a resolver-boundary test proving delegation and service tests covering each enum value.
