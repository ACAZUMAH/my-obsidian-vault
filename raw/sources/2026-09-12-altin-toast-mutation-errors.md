# Altin mutation error feedback correction

Date: 2026-09-12
Source: direct user correction in the Altin Partner Mobile Codex conversation.

## Direct user instruction

> why are you returning the mutation errors for, that's why the toast is using showing if there errors.
> and what are this assertOutletMutation and readOrderActionResponse and /Users/acazumah/Documents/C.E.Q.A/altin-partner-mobile/src/helpers/ApiError.ts how does throwing the error make the customer see what and what is not correct if the appi returns a validations error fucking remove them and use the toast and lastly I see const saving = useRef(false); in the formiks is that really necessary?

## Scoped reference observation

Read `/Users/acazumah/Documents/LivelyCura/serlp-mobile/src/hrm/createEmployee/hooks/useCreateEmployeeMutation.ts`: a direct typed Apollo mutation, success Toast, catch with error Toast and null return, and named action plus loading alias. It does not rethrow the mutation failure to a form.

## Interpretation applied

Mutation hooks own API business/validation and transport error feedback. Preserve the actual returned validation field messages in readable Toast content. Do not return errors to form banners, rethrow, or replace the rejected assertion/ApiError layer with another wrapper. A failed action returns no successful result, so forms keep drafts and only advance after success. Keep client Yup field validation and read-query errors separate. Formik isSubmitting and Apollo loading suffice for the existing submission controls; remove the parallel saving refs. The action-plus-loading shape is the current mobile implementation, supported by the inspected SERLP hook, not a claim that every reference project has identical aliases.

This correction supersedes earlier assistant instructions to rethrow/map API errors into Formik or insist on forwarding full Apollo mutation results. Query hooks retain their own Apollo result contract. Passing offline tests is not user acceptance or live API verification.
