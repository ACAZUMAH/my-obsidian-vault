# Fleet Operator Work-State Correction

- Date: 2026-09-19
- Source: Direct user correction in Codex
- Project: LivelyCura Backend

## Direct Correction

- A Fleet company must be able to see whether an operator is online and available for work, the operator's work capacity, and the operator's current geographic location.
- These requirements apply to delivery fleets as well as passenger-ride businesses.
- One generic operator update function must not update every concern. Operator profile changes and operational work-state changes require clear, purpose-specific services and APIs.

## Implementation Boundary

This correction applies to the independent company Fleet backend. It does not merge Fleet operators with LivelyCura's platform Courier riders, and it does not authorize migrations or client rollout work.
