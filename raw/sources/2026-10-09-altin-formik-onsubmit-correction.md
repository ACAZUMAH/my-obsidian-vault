# Altin Partner Formik onSubmit Correction — 2026-10-09

Sanitized record of a direct user correction in an Altin Partner Mobile Claude Code session. No credentials, tokens, or personal identifiers are included.

## The correction

- After the profile form rewrite, the user told the agent to go through all Formik code and remove the code from `onSubmit`: Formik's `onSubmit` will no longer be used for making requests to the backend.
- The user named the references: the LivelyCura pharmacy portal or admin portal, or the Check City app.
- The user said Profile and Support will be revisited because the work on them was bad. They told the agent to look at Check City's Support UI and judge its own Support work against it.

## What the references do

- Check City (`src/login/hooks/usePhoneNumberForm.ts`, `useOtpForm.ts`): form hooks contain a Yup schema and `useFormik` with `validateOnMount: true` and `onSubmit: () => {}`. The consuming component (`src/login/components/Auth.tsx`) has `handleSendOTP` and `handleVerifyOTP`. Each reads `form.values`, calls a mutation hook's named action, and moves to the next step on success. Buttons use the mutation's `loading` and `!form.isValid`. Multi-step screens keep handlers in a screen hook (`src/cart/hooks/useCheckoutScreen.ts`).
- Pharmacy portal: 166 of about 175 form `onSubmit` values are `() => {}`. Create pages own `handleSubmit` (`src/accounting/createCurrency/index.tsx`). Edit form hooks take the record, memoize `initialValues`, and set `enableReinitialize: true` (`src/accounting/currencyDetails/hooks/useUpdateCurrencyForm.ts`).
- Admin portal: same shape (`src/organization/components/organizationBasicInfoSection`). That section also edits in place, switching between view and edit components with an `isEditing` flag.

## Supersedes

- The 2026-09-12 Altin rules that form hooks call named mutations inside Formik `onSubmit`, use `isSubmitting`, and seed edit forms once through a ref and effect.
- The same-day instruction to copy the repository's committed form hooks, which used that `onSubmit` shape.
