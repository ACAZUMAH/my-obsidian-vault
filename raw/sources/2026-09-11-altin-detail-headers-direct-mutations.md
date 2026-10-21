# Altin detail headers and direct mutations

Date: 2026-09-11
Source: direct user correction in the Altin Partner Mobile task.

## Direct evidence

The user said that no detail screen should show a drawer button, and Report an issue belongs on the right side of the order-detail header. The user explicitly requested useMutation and removal of useMutationResource, asked that create/update flows follow SERLP Mobile, and emphasized simple code they can understand and maintain.

## Scoped source verification

SERLP Mobile's crm/createCustomer/hooks/useCreateCustomerMutation.ts uses Apollo useMutation and a named createCustomer action. Its form hook owns validation and submission; customerDetails/hooks/useEditCustomerFlow.ts similarly calls useMutation directly and owns edit state locally. This supports direct feature mutation hooks with shared form presentation and locally owned validation/errors, without another generic mutation lifecycle wrapper.

## Boundaries

Preserve intervening user edits, use the already-running app, and keep production mutations out of development testing. This correction explicitly supersedes the previous interpretation that asking about useMutationResource did not authorize its deletion. It also extends the earlier no-drawer rule for list headers to every detail screen.
