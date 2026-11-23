# LivelyCura HRM: employee record redesign (decided, not yet built)

- Date: 2026-10-25
- Author: the user, during the LivelyCura HRM Employees review in a Claude Code session
- Recorded from: the user's own messages (quoted verbatim) and their answers to four plan questions
- Status when recorded: plan approved, phase 1 starting

## The user's words (verbatim)

- "let's take a moment and revise the hold employee feature, we we have not even complete and their thing we need to add, we need to look into other systems and plan on how we are going to take more employees data. because we have now is not complete some orgs might want to take more info and some orgs want less. the phone number and the email is required and compulsory and we can also think about the fields we can add the almost every orgs will always need and then the plan on how we come handle the rest depending on the org and the kinda data they want from their employees like dynamic forms or something like that"
- "before we get back to answering the questions you have to know the erp is not for pharmacies only, it's general"

## Answers to the plan questions

- Built-in field groups: Job details and Personal details (not Contact & emergency, not ID & licences).
- Start date required when adding an employee: Optional.
- Who sees private details (date of birth, gender, questions marked private): only people with a new "View private employee details" permission, plus the person.
- Organization questions shown to the employee in Loop by default: Yes, unless HR ticks "HR only".

## Approved design (summary)

- Always required: first name, last name, phone, email.
- Built in: job title (organization's own list, starts empty), employment type, contract/service end (required for fixed-term, national service, intern), probation end, staff number; other names, date of birth, gender, nationality. Each organization sets optional built-in fields to Don't ask / Optional / Required.
- Organization questions (custom fields): 8 types, Required / Private / HR only, archive instead of delete, type fixed after creation, special-data labels made private automatically.
- Phases: 1 job details and foundations; 2 private details; 3 organization choices and questions; 4 reminders.
