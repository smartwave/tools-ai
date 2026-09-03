# Design: Add AIDLC Governance Checks

## Technical approach

All check logic in Python 3.11+ under `ci/`, shared module `ci/lib/` (importable as plain files; no packaging). Entry points keep the existing stub names and usage lines — `ci/validate-manifest <manifest> [...]`, `ci/check-registry [--base <git-ref>]`, `ci/check-projections <manifest> [--topics-file F] [--tags-file F]` — implemented either as Python scripts with those names or bash shims calling `ci/lib`. New checks follow the same pattern.

## Architecture decisions

### Decision: config file instead of placeholder substitution
The tree stays the shareable generic edition. `ci/lib/config.py` resolves values in this order: `config/governance.yaml` if present → literal substitution detected in the tree (an adopter who did the documented find-and-replace needs no config) → exit 3 with "copy config/governance.example.yaml to config/governance.yaml". A `resolve(pattern)` helper substitutes `{{ASSET_ID_PREFIX}}` / `{{TAG_NAMESPACE}}` into patterns read from schema/vocabulary/tag-map at runtime, in memory only.

### Decision: provenance gating in the shared library
One function decides enforceability from the rule's provenance tag: `[REF Bx]` / `[REF Technical Controls]` → enforce; `[REF insert]` / `[PROPOSED]` → warn-only unless config `enforce_pending_insert: true`. Individual checks never hardcode this.

### Decision: rules read at runtime, never restated in code
`check-preflight` reads the B1.7 item list from `policy/gates.yaml`; `check-tier-controls` reads tier rows, modifiers, and invariants from `policy/tier-controls.yaml`. Failure messages cite control ids from `policy/standards.yaml`. Editing policy changes enforcement with no code change — matching the repo's "this repo owns values and rules" principle.

### Decision: offline checks; actuals passed in
No network calls. GitHub-topic / AWS-tag actuals arrive as files; with none supplied, `check-projections` prints the expected projection (generator mode) and exits 0. The leak check (excluded fields in public topics) always runs when a topics file is supplied.

### Decision: evidence as per-asset files
`assets/<asset_id>/preflight.yaml` (one entry per gate item: status met|exception|pending, evidence link, checked_by, date), `assets/<asset_id>/exceptions.yaml` (B1.8 fields incl. expiry), `assets/<asset_id>/evaluation/eval-set.yaml` + `evaluation/results/*.yaml`. A `met` item with empty evidence fails — the checklist is an evidence record. Ordering (threshold declared before results) is judged from declared dates inside the files, not filesystem timestamps.

### Decision: exit-code contract
0 pass; 1 violation (control id + file + line where possible); 3 not configured. Exit 2 ("not implemented") must no longer occur. `ci/run-all` aggregates into one check × asset summary table; warn and "not machine-checkable" rows are printed so silence never reads as coverage.

## Known discrepancy (carry, don't fix)

AI-Program tiering defines Tiers 0–3; repo vocabulary defines 1–3. Enforce the repo vocabulary; document the discrepancy in `ci/README.md` as an open reconciliation item.

## File changes

- New: `config/governance.example.yaml`, `ci/lib/*`, `ci/requirements.txt`, `ci/check-tier-controls`, `ci/check-gate1`, `ci/check-preflight`, `ci/check-evaluation`, `ci/run-all`, `ci/install-hooks`, `ci/tests/` (fixtures + runner), `assets/` (README + fixture asset), `.github/workflows/governance-checks.yml`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/ISSUE_TEMPLATE/ai-solution-intake.md`.
- Rewritten in place: `ci/validate-manifest`, `ci/check-registry`, `ci/check-projections`.
- Modified: `.gitignore` (+`config/governance.yaml`), `ci/README.md`, `GOVERNANCE.md`, root `README.md`, `CHANGELOG.md`, `GOVERNANCE-SPEC.md`.
- Untouched: `policy/`, `vocabulary/`, `schemas/`, `projections/`, `registry/` content values; `confluence/**`; `plugins/**`; `skills/**`.
