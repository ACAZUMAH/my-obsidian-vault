## Exact-ID determination

- **ID:** `20260721_030948_da545b`
- **Classification:** `process-control` — interrupted continuation with independent read-only reconnaissance.
- **Whole-record duplicate:** **No.** The opening is replay, but 121 later rows are unique execution.
- **Promotion:** `incomplete` / `reference-only`; **zero new durable project claims**.
- **C.E.Q.A/Altin integration:** **No.** It investigated the final five Codex records but did not write or integrate Batch 3.
- **Six-template/direct-project transition:** **Not owned.** Those paths already existed when unique execution began, and the record made no schema writes.
- **Unrelated work:** **None found.**
- **Confidence:** High.

## Exact metadata

| Field | Verified value |
|---|---|
| Store | Default-profile `/Users/acazumah/.hermes/state.db` |
| Logical locator | `sessions.id='20260721_030948_da545b'`; `messages.session_id` same |
| Started | `2026-07-21 03:09:48.806114 UTC` |
| Ended | `2026-07-21 03:15:58.725649 UTC` |
| Last message | `2026-07-21 03:14:55.696144 UTC` |
| Metadata cleanup gap | `63.029505` seconds |
| Source | `desktop` |
| Parent | `20260721_020029_f66b3b` |
| Parent→child gap | `0.000448` seconds |
| End reason | `compression` |
| Archived | `0` |
| Profile / cwd / title | `NULL` / `NULL` / `NULL` |
| Frozen-cutoff rows | 2 user / 41 assistant / 140 tool |
| Post-cutoff rows | `0` |
| Coder-store collision | None |

## Replay and unique boundary

- Rows `4383–4444`: **62-row replay/compaction preamble**.
- **39 exact parent matches:** 15 assistant, 23 tool, 1 user. This is a lower-bound replay control.
- The two user-role rows are the inherited harvest request and a generated preserved task list; neither is a fresh request.
- Rows `4445–4565`: **121 unique execution rows**—22 assistant tool-call-only rows and 99 tool results, with:
  - no fresh human request or correction;
  - no non-empty final assistant outcome;
  - no write, patch, delegation, build, test, or validator call.

## Component status

| Component | Status |
|---|---|
| Parent request/context | `reference-only` duplicate |
| Fresh user request/correction | None |
| C.E.Q.A/Altin Batch 2 | Existing artifacts inspected; not authored or integrated here |
| Final-five-record Batch 3 reconnaissance | Independent but `incomplete` |
| Batch 3 vault integration | None |
| Six-template/project-template/direct-`wiki/projects/` transition | Not owned; already present |
| Schema or validator changes | None |
| Current-source/Git-history inspection | Read-only reconnaissance |
| Validation | None; no canonical validator, build, test, or runtime command |
| Git operations | Read-only `status`, `log`, and `show`; no stage, commit, push, branch, or remote mutation |
| Unrelated work | None |
| Evidence promotion | Zero new claims |

## Current versus historical boundary

- During the record, Git status already showed `_template/`, `schema/`, `scripts/`, and `wiki/projects/` as existing untracked infrastructure. Batch 1/2 C.E.Q.A artifacts also already existed.
- The target then inspected the same five historical records later captured in C.E.Q.A/Altin Batch 3, but compression occurred before synthesis or writes.
- Current vault state now contains:
  - schema version 2;
  - six templates, including the project template;
  - direct `wiki/projects/` ownership;
  - integrated C.E.Q.A/Altin Batch 3;
  - project-page provenance for all five inspected records;
  - C.E.Q.A/Altin family coverage at 21/21.
- That is **later state**, not retroactive completion by this record. Current Batch 3 provenance attributes the integration to Codex/Hermes reconciliation, not this exact continuation.
- Current vault Git is dirty and uncommitted:
  - `main` at `10f7baf9a3476032100845dbf56584fd3ee9f785`;
  - local `origin/main` tracking ref matches, `0/0` ahead/behind; no fresh fetch;
  - 0 staged;
  - 93 porcelain entries: 14 modified, 15 deleted, 64 untracked;
  - schema, project template, Batch 3 source, and project pages are absent from committed `HEAD`.
- Current project repositories remain clean:
  - Altin Partner Mobile: `main` at `f05077b6701885aaf928fca79281b95dee0babcf`
  - Keks Admin Portal: `develop` at `3521aaadf7ba45474880115d8f8b53e805648d95`
  - Call Center Web App: `develop` at `6a9cff6b681fd558761683d591865d76298891fc`

## Successor and checkpoint

- Direct successor: `20260721_031558_72a825`
  - started `2026-07-21 03:15:58.726257 UTC`, `0.000608` seconds later;
  - source `desktop`, parent exact target, ended by compression;
  - body intentionally not inspected.
- Once durably checkpointed, classification coverage should advance from **41/130 to 42/130**, leaving **88**.
- Evidence-bearing promotion count from this ID: **0**.

## Recommended targets

1. Audit `20260721_031558_72a825` next for actual Batch 3 integration and schema-transition ownership.
2. Resolve the open questions in `hermes-vault-validation-harvest-continuation-batch-3.md`; preserve this ID as reconnaissance-only provenance.
3. Advance the classification checkpoint to 42/130 without adding C.E.Q.A project claims or duplicate rules.
4. Do not update C.E.Q.A project pages from this record; the later Batch 3 source already owns that evidence.
5. Resolve the stale five-template `vault-maintenance` documentation in a separately authorized maintenance pass.

**Files created or modified by this audit:** none.  
**Limitations:** successor body and concurrent Codex provenance were outside exact-ID scope; no fresh validator, build, test, service, or runtime command was run. No secrets, private payloads, full transcript, prompts, or tool chatter were reproduced.