# LivelyCura: serlp-mobile creates from the drawer's Create section, not a list's top button (decided 2026-11-26)

- Date: 2026-11-26
- Author: the product owner, in a LivelyCura Claude Code session
- Recorded from: the owner's own message (verbatim below), about the Job titles screen in serlp-mobile's HRM module
- App: serlp-mobile (SERLP Mobile, the managers' mobile ERP), branch `feature/hrm`
- Status when recorded: built and committed (serlp-mobile `0635209b`); not yet pushed

## The owner's correction (verbatim)

- "remove the add job title button from the job titles screen, it's supposed to be at the create section of the drawer"

## How the session read it

- In serlp-mobile, list screens do not carry their own "Add X" button at the top. Creating goes in the module drawer's Create section, and the module home's matching actions, as "New X", shown only to people with the same permission that adding needs.
- A list's empty-state button may stay.

## How the session applied it (serlp-mobile `0635209b`, 2026-11-26)

- Job titles list: the top "Add job title" button is gone.
- HRM drawer Create section and HRM home actions: "New job title" added right after "New department", for those who can add one (the departments create permission for the whole organization, as the portal's menu manages job titles with the departments permissions).
- "New job title" opens the Job titles list with the Add job title window open, once.
- The empty Job titles list keeps its own button, as Departments does.
