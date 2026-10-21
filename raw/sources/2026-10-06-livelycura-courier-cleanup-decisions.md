# LivelyCura Courier Cleanup Decisions

Date: 2026-10-06
Source: Direct user answers during the courier cleanup follow-ups

## Decisions

1. A customer may cancel their own (non-marketplace) order only while it is PLACED or ACCEPTED, before preparation starts. Staff cancellation is unchanged.
2. Marketplace buyers keep the earlier rule: they may cancel until the rider picks up, with an automatic full refund.
3. "We don't want a situation where the order will be ready and then it will be waiting for a rider ... that's why we find a rider while the order is being prepared." When a delivery is cancelled while the order is being prepared, the replacement task is created immediately; if the cancelled task already had a rider requested or assigned, the replacement automatically searches for a rider again.
4. Customer delivery tracking: the link is sent only by SMS, automatically when the rider picks up the order (no staff share button). The public tracking page shows status, a timeline and the ETA only (no rider map, no rider name, no pay-online, no drop-off code). The page is built in the customer portal on a new branch from develop.
5. Admin Connect Users is a feature on hold; leave it as it is.
6. Remove unused helpers from the Dispatch app; fix the remittance `.save()` convention break.
