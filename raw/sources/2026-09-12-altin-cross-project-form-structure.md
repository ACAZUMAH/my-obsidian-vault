# Altin Cross-project Form Structure Correction

Date: 2026-09-12
Source: direct user correction in the Altin Partner Mobile Codex task.

## Direct user evidence

> not fucking how I write my formik and yup code wtf fuck is wrong with you why can't you be consistent damn. I don't fucking want to go to this project and things I do there is different and I go to this other project and things there are different that's why I want consistency across all of them and you fucking still do things different wtf\\

Context: this explicitly rejects the assistant's preceding Formik/Yup migration and its claim of completion. The user requires consistent code structure across projects, not merely the presence of the same libraries.

## Scoped source inspection

Codex compared SERLP Mobile `src/crm/createCustomer/hooks/useCreateCustomerForm.ts`, `src/crm/createCustomer/CreateCustomer.tsx`, `src/hrm/createEmployee/hooks/useCreateEmployeeForm.ts`, `src/catalog/createProduct/hooks/useCreateProductForm.ts`, and `src/selling/createOrder/hooks/useCreateOrderForm.ts`.

Observed pattern: private module-level `const validationSchema = yup.object().shape(...)`; named `use…Form` hook; typed useFormik with initialValues, direct async onSubmit using the named mutation, validateOnMount and validationSchema; return form plus mutation state. Components consume form.values, form.touched/errors, handleChange, handleBlur, setFieldValue and handleSubmit. Complex flows can retain domain helpers and workflow state. These observations are repository evidence, not extra user wording or acceptance of any replacement implementation.
