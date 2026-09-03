# Handoff — how to run this with Claude Code

One change is staged and ready to implement: `changes/add-aidlc-governance-checks/`.

## If you use the OpenSpec CLI / extension

1. In the repo root: `openspec init` (choose Claude Code when asked which assistant). Keep the existing `openspec/` contents if it offers to scaffold — this change folder and `project.md` are already authored.
2. Validate: `openspec validate add-aidlc-governance-checks`
3. In Claude Code: `/opsx:apply add-aidlc-governance-checks` — the agent works through `tasks.md`, checking items off as it goes.
4. When done and verified: `/opsx:archive add-aidlc-governance-checks` — the deltas merge into `openspec/specs/` as the repo's living capability specs.

## Without the CLI

Prompt for a fresh Claude Code session in this repo:

> Read `openspec/project.md`, then `openspec/changes/add-aidlc-governance-checks/proposal.md`, `design.md`, and every file under its `specs/`. Implement the change by working through `tasks.md` top to bottom, marking each task `- [x]` as you complete it. Every Requirement and Scenario in the spec deltas must hold when you finish. Do not touch anything the proposal lists as out of scope. Finish with the verification in task 7.3, then report which tasks are done and any deviations.

## Notes

- `BUILDOUT-SPEC-aidlc-checks.md` at the repo root is the prose companion (rationale, acceptance detail). The spec deltas here govern where wording differs.
- Owner decisions the implementer must surface, not make: real `asset_id_prefix`/`tag_namespace` values; `enforce_pending_insert`; the tier 0–3 vs 1–3 reconciliation; where client evaluation evidence lives.
- `openspec/specs/` is intentionally empty until the change is archived — this repo had no spec'd capabilities before this change.
