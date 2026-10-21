# LivelyCura Courier Requestor Identity Correction

Date: 2026-09-26

## User Decision

- A delivery request may be initiated by a Customer, Facility, or Organization.
- Removing organization and facility ownership from Courier applies to courier-company, rider, and fulfillment management. It does not remove the identity of the merchant that requested a delivery.
- `organizationId`, `facilityId`, and `customerId` on a delivery task are requestor, order, billing, and cash-remittance context. They must not be treated as ownership of a rider or courier provider.
- A stored or requested Facility requestor must remain Facility. Do not silently coerce it to Organization.

## Context

This corrects an over-broad cleanup that removed Facility from the Courier requestor enum and task contract after company Fleet management was separated from platform Courier.
