# TypeScript Service Conditional-Flow Decision

Date: 2026-08-01

## User Correction

> this file /Users/acazumah/Documents/LivelyCura/livelycura-backend/src/services/courier/deliveryTasks/createDeliveryTask.ts to has same messy code. chaining function calls with "?" is wrong

## Clarified Convention

- Do not use chained or nested conditional expressions to orchestrate backend service work.
- Split loading, validation, calculation, document construction, and persistence orchestration into domain-owned helpers.
- Pass related values to functions through one typed data object defined in the owning interface layer.

## Verified Application

- Refactored delivery-task creation into owned context, agreement, pricing, settlement, proof, document, and item helpers.
- Changed the transactional creation entry point to accept one typed object.
- Focused courier delivery-task tests, TypeScript build, and lint passed.
