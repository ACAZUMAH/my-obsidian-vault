---
type: source
status: active
created: 2026-11-19
updated: 2026-11-19
tags: [preferences, scope, verification, test-data, decision]
sources:
  - ../../raw/sources/2026-11-19-whole-fix-and-no-dev-test-people-direction.md
source_date: 2026-11-19
ingested: 2026-11-19
confidence: high
---

# Whole Fix And No Dev Test People Direction

## Source

- Raw file: [Direction: an approved fix is delivered whole; no test people on the shared dev database](../../raw/sources/2026-11-19-whole-fix-and-no-dev-test-people-direction.md)
- Date: 2026-11-19
- Author: The owner (paraphrased), relayed by the Claude Code session
- Ingested: 2026-11-19

## Core Claims

- An approved fix is delivered whole across every app, screen, message and follow-on effect it touches, including what a review of the fix finds; the agent does not return with "leftovers" to ask about.
- Only genuinely separate features, or decisions that are truly the owner's (such as exact wording), go back as a question.
- Agents never create test users, employees or organizations on the shared LivelyCura dev database for on-screen checks, and do not offer to.

## Useful Details

- Trigger: HRM follow-up 1 (role-only organization lists in the portal and serlp-mobile). The agent twice reported review findings as questions after "Yes, all three", and offered to create a test "Ama" on the dev database.
- Verification instead: integration tests that seed their own in-memory data, and browser checks with fake client-side state on a separate origin (for example `http://[::1]:5173`), never the owner's signed-in tab.

## Connections

- [[../syntheses/personal-operating-manual|Personal Operating Manual]] (Change And Remediation Work).
- Extends the existing "complete its whole reasonable scope" rule from [[altin-module-builds-and-scope-corrections|the Altin scope corrections]].
- [[livelycura-hrm-feature-by-feature-review|LivelyCura HRM Feature-By-Feature Review]] is the review this follow-up came from.

## Contradictions Or Tensions

- "Change only what was asked for" still holds: the whole-fix rule covers what belongs to the approved fix, not unrelated side issues, which stay parked.

## Open Questions

- None.
