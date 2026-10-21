# Bora Resolver And Service Documentation Correction

Date: 2026-09-28
Source: direct user correction in Codex

## Correction

The Phase 1 resolvers were incorrectly rewritten as inline functions inside resolver maps, and new or rewritten service functions lost the repository's function documentation.

## Required Direction

- Declare resolver functions as named constants above the resolver map.
- Add the repository's JSDoc to resolver functions, then reference the named functions from `Query`, `Mutation`, and field-resolver maps.
- Every new or rewritten service function must retain or receive an `@description` block with applicable `@param`, `@throws`, and `@returns` entries.
- Rewriting an existing function must preserve its documentation and update it when behavior changes; do not silently remove comments.
