# LivelyCura Fleet GraphQL And Filter Naming Correction

- Date: 2026-09-25
- Source: direct user correction in the current Codex task.

The user corrected the earlier Fleet naming pass because it changed only service functions while leaving GraphQL and interfaces unchanged. The correction requires the rename to cover the whole contract. The user also identified incorrectly passed filters in list-record queries, especially date filters, and directed the implementation to follow existing project patterns.

Direct excerpt: “I said change them and you only did at the services functions and left the graphql and interfaces out ... most of the queries you are passing most of the filters wrong especially the dates ... follow what I do on the other parts of the project.”
