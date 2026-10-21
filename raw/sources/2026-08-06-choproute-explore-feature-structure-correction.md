# ChopRoute Explore Feature Structure Correction

## Source Context

- Date: 2026-08-06
- Author: User
- Evidence type: direct Codex conversation correction
- Implementation root: `/Users/acazumah/Documents/LivelyCura/livelycura-pice-app`

## Direct Evidence

- New ChopRoute features must follow the existing mobile code structure rather than introducing an agent-preferred layout.
- A feature such as `src/explore` separates its owned components, interfaces, hooks, helpers, and constants into the established subfolders.
- The earlier instruction to remove unnecessary folders referred to obsolete competing top-level browse features, not to flattening Explore's internal feature structure.
- Screen files should compose feature-owned pieces instead of absorbing presentation, state, transformation, constants, and type ownership into one file.

## Evidence Boundary

This record corrects the internal folder-ownership interpretation. It does not change Explore's customer-facing name, visual header, catalog source, or route behavior.
