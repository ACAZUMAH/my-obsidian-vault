# LivelyCura: no header fades in SERLP Team (decided 2026-11-25)

- Date: 2026-11-25
- Author: the product owner, in a LivelyCura Claude Code session
- Recorded from: the owner's own message (verbatim below), right after reviewing the SERLP Mobile-style redesign of SERLP Team on the iOS simulator
- Feature: the employee app SERLP Team (repo livelycura-loop-app), branch `feature/hrm`

## The owner's request (verbatim)

- "remove the header fades away"

## How the session applied it

- The soft fade under every screen header (copied from SERLP Mobile's HeaderFade) is removed from SERLP Team everywhere: the shared screen shell, list screens, the Schedule tab's sticky month header, the Payroll tab switch and the payslip view. Content scrolling up now passes under the header's solid page-coloured band, and content starts 12pt under the header instead of the 24pt the fade needed.
- SERLP Mobile is unchanged; this is a SERLP Team exception to "same as SERLP Mobile".
