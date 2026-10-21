# Courier Backend Boundary Correction

- Source: direct user instructions in Codex, 2026-09-17.
- Scope: durable architecture correction; no completion or deployment claim.

## User correction

“the existing currier is not supposed to have anything to do with org and facilities again”

“remove all the migrations focus on properly building the feature before we move there”

“any here ... /src/services/courier should have nothing to do with fleet don't mix them up”

“let's focus on the backend ... follow code structure and architecture check the other parts of the project”

The user rejected the prior Fleet services, models, GraphQL resolvers and type definitions and asked to address the backend before other applications.

## Explicit clarification

Question: “For Courier, I’m removing company ownership and management. Should delivery requests still retain a reference to the requesting merchant/order for billing and cash remittance?”

User answer: “Keep merchant/order references only”.
