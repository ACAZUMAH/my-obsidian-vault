# Keks Backend Errors And Bulk Time Punches — User Correction

Date: 2026-09-16. Source: direct Codex user request; no credentials or personal data captured.

## User Request

> When creating a user, you just show “an error occurred”. Not the actual error. and also the create user input fields most of them are not required, I updated the yup validation schema to the only things I want to be required. After those updates the next thing we going to work on a way to allow them to able to bulk time punch shifts there is no api for so we have to find a way to loop and request with the id's one by one while give the user feed back on the progress of it, then check the the api redoc very concerning the error notifications most them you just return An error occurred during employee creation, instead of there real error returned from the backend

## Contract Evidence Inspected

The user's edited Yup schema retains first name, last name, gender, phone number, and role as required. Company assignments, joining date, salary, and emergency-contact inputs are optional.

The supplied OpenAPI specification permits omitted branch_id, department_id, date_of_joining, and emergency_contact. A supplied emergency_contact requires name, while relationship and phone_number are optional. The screenshot shows an errors array containing validation messages; the specification also describes error envelopes and detail arrays with loc/msg.

POST /time-punches/override accepts employee_id, not shift_id. The employee's outstanding request determines clock-in or clock-out. Success is HTTP 204. No bulk override endpoint is supplied.
