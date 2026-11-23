# LivelyCura HRM: holidays decisions (decided, not yet built)

- Date: 2026-10-23
- Author: the product owner, choosing between plain-language options one at a time in a LivelyCura Claude Code session
- Recorded from: the owner's own answer messages (quoted verbatim below) and the session's research brief
- Feature: LivelyCura HRM "Holidays" (public holidays and company days off)
- Status when recorded: decided, not yet built; a build spec is being written

## What the research found (context for the decisions)

- A holiday was one organization-wide row (name, date, optional "repeats every year"); a repeating holiday was stored once with its first-saved year.
- Only staff HR assigned one by one to a holiday were off: a missed shift on a holiday was recorded "Holiday" for assignees and "Absent" for everyone else, while leave already skipped every holiday for everyone.
- Public holidays came from the Nager.Date feed (11 days a year for Ghana), which has no Eid-ul-Fitr or Eid-ul-Adha and never knows one-year government moves or substitute days.
- Holiday changes never corrected attendance already recorded, and nobody was notified about holidays.

## The owner's decisions (verbatim)

1. "Everyone is off on a public holiday by default; managers mark who is working that day, and new hires are covered automatically." Accepted with it: picking up an open shift on a holiday counts as working that day, and the shortfall view shows holiday shifts as "Holiday" rather than short-staffed (this settled decision 8).
2. "Each organization's HR adds them, prompted by a 'still to be announced' card on the Holidays page." (Eid and other short-notice or government-moved days; a SERLP-maintained yearly Ghana list was not chosen.)
3. "One holiday entry per year; 'repeats every year' means the system creates next year's entry itself, and this year's and next year's always exist."
4. "Attendance corrects itself after holiday changes for people who didn't clock in, logs who caused it, and never overwrites a clock-in or a manager's manual correction (including when leave changes)."
5. "One 88-country picker on every screen; load only nationwide public holidays when the online list covers the country, with a clear 'add your holidays' warning when it doesn't."
6. "Nothing pre-selected on either app; HR must pick 'Every year' or 'This year only' before saving."
7. "Add a type: Public holiday or Company day off; imported ones are Public, HR picks for their own, and labels follow the type."
8. Settled by decision 1: holiday shifts show as "Holiday" with how many are working, not short-staffed.
9. "Loop notices when a holiday is added, moved or deleted, or when a manager marks someone as working on it, plus a 'Holidays this year' list in Loop."

## Parked

- Holiday pay (the session's research pointed at Labour Act 2003, Act 651, s.72, s.75(2), s.77 and s.43; not re-verified here) belongs to the later Payroll feature.
