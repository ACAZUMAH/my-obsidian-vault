# Fleet GraphQL Architecture Correction

- Date: 2026-09-20
- Source: Direct user correction in Codex
- Project: LivelyCura Backend

## Direct Correction

- Build Fleet one feature at a time and use HRM as the repository architecture reference for this independent module.
- Fleet operator resolvers must use named resolver functions, call their owning services directly, and leave endpoint permission checks to GraphQL Shield.
- Do not add a Fleet-specific principal layer that queries organizations, enabled modules, or facilities before calling services. Shield already resolves tenant context and protects the endpoint.
- Compose Fleet type definitions through the repository's single interpolated `#graphql` template pattern.
- Compose the Fleet root resolver map explicitly by `Query`, `Mutation`, and GraphQL object type rather than spreading complete feature resolver objects into the root.
- Fleet operator service functions require concise comments that explain their inputs, behavior, and results.

## Implementation Boundary

This correction removes duplicate GraphQL authorization and tenant-validation plumbing. Fleet services still enforce business rules and query within the organization/facility scope supplied by their inputs. Other Fleet features should receive their own architecture pass rather than being treated as complete because shared plumbing was removed.
