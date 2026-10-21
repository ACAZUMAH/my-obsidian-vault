# LivelyCura GraphQL Contract Compatibility Fixes

- Date: 2026-09-21
- Author: User
- Context: Pharmacy Portal CRM messages and Admin Portal Courier

## Reported Failures

- CRM Messages failed because a persisted marketing-message application value, `CUSTOMER`, was no longer represented by the current `MobileApps` GraphQL enum.
- Admin Courier failed because its Delivery Agents query still selected `agentType`, which had been removed from the platform-rider `DeliveryAgent` contract.

## Durable Interpretation

When cleanup of a retired enum value is deferred, enum-list field resolvers may omit values that the current GraphQL enum cannot serialize; the removed enum member must not be restored merely to expose stale storage. When the backend removes a field as part of a domain boundary change, every client query, filter, view, generated type, and test must move to the current contract. Platform delivery agents are standalone network riders and no longer carry company-provider `agentType`, organization, or facility ownership.
