# Proposal: Add AIDLC Governance Checks

## Intent

The repo's governance layer defines the AI delivery lifecycle rules as data (`policy/tier-controls.yaml`, `policy/gates.yaml`, `schemas/manifest.schema.json`, `vocabulary/vocabulary.yaml`, `projections/tag-map.yaml`) but nothing enforces them: the three `ci/` checks are stubs that exit 2, Gate 1 and the pre-flight (B1.7) checklist have no machine check, and the AIDLC evaluation-set discipline (declare the acceptable error rate before building, re-measure after) has no home in the repo.

When this change is done, any manifest-carrying asset can be checked mechanically — manifest validity, registry integrity, projection conformance, tier requirements, gate passage, evidenced pre-flight, and correctly ordered evaluation records — with one local command that runs identically in GitHub Actions.

## Scope

In scope:

- A configuration layer (`config/governance.yaml`, git-ignored; committed example) so checks run without substituting the tree's `{{...}}` placeholders.
- Implement the three stub checks: `ci/validate-manifest`, `ci/check-registry`, `ci/check-projections`.
- New checks: `ci/check-tier-controls`, `ci/check-gate1`, `ci/check-preflight`, `ci/check-evaluation`.
- Per-asset evidence layout under `assets/<asset_id>/` (preflight.yaml, exceptions.yaml, evaluation/).
- `ci/run-all` runner, optional `ci/install-hooks` pre-commit hook, one GitHub Actions workflow, PR template, and an AI-solution intake issue template.
- Documentation updates: `ci/README.md`, `GOVERNANCE.md`, root `README.md`, `CHANGELOG.md`, `GOVERNANCE-SPEC.md`.

Out of scope (do not do):

- Implementing the five governance skills in `skills/` (they stay stubs); any change to the two plugins under `plugins/`.
- Substituting placeholder tokens in committed files; editing content values of `policy/`, `vocabulary/`, `schemas/`, `projections/`; touching `confluence/**` or the existing confluence-sync workflow.
- Network calls from checks (no GitHub/AWS API clients).
- Enforcing `[REF insert]` / `[PROPOSED]` rules by default; inventing rules where policy files are silent (report "not machine-checkable" instead).
- Resolving the tier 0–3 vs 1–3 numbering discrepancy (note it; leave it open).

## Approach

Python 3.11+ with only PyYAML + jsonschema, shared code in `ci/lib/` (config resolution, placeholder detection, provenance gating, YAML/JSON loading with line-bearing errors). Existing `ci/<name>` entry points keep their documented names and CLIs. Checks read rule content (gate item lists, tier rows, tag maps) from the policy files at runtime — a policy edit changes enforcement without a code change. Exit codes: 0 pass / 1 violation citing the control id / 3 not configured. Local scripts are the single implementation; the Actions workflow is a thin wrapper that stays green on an unconfigured generic clone.

The prose companion `BUILDOUT-SPEC-aidlc-checks.md` (repo root) carries full rationale and acceptance detail; this change's `specs/` deltas govern where wording differs.

## Open decisions surfaced to the owner (do not decide)

Real `asset_id_prefix` / `tag_namespace` values before any real asset is minted; ratification status driving `enforce_pending_insert`; the tier-numbering reconciliation; whether client evaluation evidence lives in this repo or per-client repos.
