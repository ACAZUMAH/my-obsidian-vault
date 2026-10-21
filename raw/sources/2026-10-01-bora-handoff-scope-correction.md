# Bora Frontend Handoff Scope Correction

Date: 2026-10-01
Source: direct user correction in Claude Code during Bora backend work (2026-10-01)

## User Direction

- The user had said only that investment accounts, goals and top-ups, and withdrawals were already sent to the frontend developer. The user did not say Grow Wealth was part of the previous handoff and objected to its removal from the app handoff.

## Agent Evidence

- When trimming the app handoff, the agent inferred from the old per-feature documents that existing-customer onboarding, KYC, Grow Wealth, and statements had also been sent, and removed them. That inference was wrong; the claim in `2026-10-01-bora-handoff-delta-permissions-inbox.md` that the previous handoff covered those areas is superseded by this correction.
- Grow Wealth had been presented only as two query renames, which is meaningless for a frontend that never received Grow Wealth.

## Implemented Scope

- The app handoff again documents existing-customer onboarding, KYC, Grow Wealth, and statements with current operation names, plus their checklist entries and open items; the rename-only section was removed. Only withdrawals, investment accounts, and goals and top-ups are left out.
- All 25 GraphQL operation examples in the two handoff files validate against the live schema and depth limit; all JSON examples parse.
