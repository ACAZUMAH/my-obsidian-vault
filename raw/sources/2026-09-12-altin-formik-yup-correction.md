# Altin Formik and Yup Correction

Date: 2026-09-12
Source: direct user message in the Altin Partner Mobile Codex task.

## Direct user evidence

> issue number 2, I use formik and yup so why are you not using that but you are doing something else?.

Context: the user had already required reference-project and Obsidian consultation and rejected assistant-created alternatives to their query/mutation architecture. This message identifies Formik and Yup as their form convention.

## Scoped repository verification

Codex inspected `/Users/acazumah/Documents/LivelyCura/serlp-mobile/src/crm/createCustomer/hooks/useCreateCustomerForm.ts` and `src/hrm/createEmployee/hooks/useCreateEmployeeForm.ts`. These references use typed `useFormik`, Yup validation schemas, `validateOnMount`, and `onSubmit` invoking named mutation actions; the real Formik form is returned to the UI. This is repository verification, not additional user wording or evidence of user acceptance of a subsequent implementation.
