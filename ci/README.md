# ci/

**Enforcement** — checks that assert a repo/asset actually conforms to the
values, schema, projections, and gates defined here. They run locally with one
command and run identically in GitHub Actions
(`.github/workflows/governance-checks.yml` calls the same scripts).

```bash
pip install -r ci/requirements.txt
cp config/governance.example.yaml config/governance.yaml   # then set real values
ci/run-all
```

| Check | Asserts | Status |
|-------|---------|--------|
| [`validate-manifest`](validate-manifest) | Manifests validate against `schemas/manifest.schema.json` and use only `vocabulary/` values; Tier 1 manifests are held to the five-field shape, Tier 2+ to the full one. | implemented |
| [`check-registry`](check-registry) | `asset_id`s are unique, pattern-valid, and never rewritten or removed (append-only vs a base ref). | implemented |
| [`check-projections`](check-projections) | A repo's topics / a resource's tags match its manifest per `projections/tag-map.yaml`, and no excluded field leaks into a public topic. | implemented |
| [`check-tier-controls`](check-tier-controls) | The effective tier (modifiers first) satisfies its row in `policy/tier-controls.yaml`: allowed tracks/oversight, required records, decidable invariants. | implemented |
| [`check-gate1`](check-gate1) | Gate 1 per `policy/gates.yaml`: Requirements + Epic linked (Tier 2+), asset id minted. | implemented |
| [`check-preflight`](check-preflight) | Every B1.7 pre-flight item is evidenced (or waived by an unexpired B1.8 exception); Tier 3 extras included; spec exists. | implemented |
| [`check-evaluation`](check-evaluation) | The evaluation set exists, its threshold was declared before any results existed, and the latest run is within threshold with zero unacceptable-kind failures. | implemented |
| [`run-all`](run-all) | Every check above, in dependency order, with a summary table. | implemented |
| [`install-hooks`](install-hooks) | Optional `pre-commit` hook: staged manifests + the registry only. Never auto-installed. | implemented |
| [`tests/run`](tests/run) | Fixture suite — one passing and at least one failing case per rule, each asserting the control id in the message. | implemented |
| [`pull-page`](pull-page) | Confluence sync helper (unchanged by this buildout). | — |

## Exit codes

| Code | Meaning |
|------|---------|
| `0` | pass — warnings and "not machine-checkable" notices are allowed |
| `1` | violation — the message names the control id, the file, and the line where one can be located |
| `3` | not configured — no `config/governance.yaml` and the tree still carries `{{...}}` placeholders |
| `4` | environment problem — pinned dependencies not installed |

`2` used to mean "not implemented" and must never occur again.

## Configuration

Two adoption paths, and the checks detect which one you took:

1. **Config file (keeps the tree generic).** Copy
   `config/governance.example.yaml` to `config/governance.yaml` (git-ignored)
   and set real values. The checks resolve `{{ASSET_ID_PREFIX}}`,
   `{{TAG_NAMESPACE}}`, `{{ORG_NAME}}`, and `{{DOC_ID_PREFIX}}` out of the
   schema, vocabulary, tag-map, registry, and manifest under test **in memory
   only** — nothing on disk is rewritten.
2. **Find-and-replace.** Substitute the placeholders across the tree as
   `PLACEHOLDERS.md` documents. No config file is then needed; the loader
   derives the values back out of the substituted tree.

With neither, every check exits 3 with the copy-the-example instruction, and
`ci/run-all` still exits 0 — a generic clone of this toolkit stays green.

Two environment variables exist for the fixture suite and are not part of the
adopter contract: `GOVERNANCE_CONFIG` (config file location) and
`GOVERNANCE_ASSETS_DIR` (evidence root).

## Enforcement gating

Provenance decides what can fail the build, exactly as `policy/` tags it:

- `[REF Bx]` / `[REF Technical Controls]` — enforced. A violation exits 1.
- `[REF insert]` — the pending naming/tagging insert (asset-id minting at Gate
  1, the Tier 2+ manifest MUST, the registry format). **Warn-only** until the
  adopter sets `enforce_pending_insert: true`, which is appropriate only once
  the insert is ratified in Confluence.
- `[REC]` / `[PROPOSED]` — never enforced; reported as warnings.

This lives in `ci/lib/report.py`, not in individual checks, so a check cannot
enforce a pending rule by accident.

## What the checks will not do

Rules that exist but cannot be decided from a manifest — the B1.4 oversight
conditions ("irreversible", "leaves the company"), secrets placement, the
off-switch, reviewer independence — are printed as `N/C … (not machine-checkable
here)` on every run. Silence never reads as coverage, and a check never guesses.

All checks run offline. GitHub topics and AWS tags are supplied as files
(`--topics-file`, `--tags-file`); nothing here queries GitHub or AWS.

## Evidence layout

Per-asset evidence lives in `assets/<asset_id>/` — `preflight.yaml`,
`exceptions.yaml`, and `evaluation/`. See [`assets/README.md`](../assets/README.md)
for the shape of each file; worked fixtures are in `ci/tests/fixtures/assets/`.

## Open reconciliation item — tiers 0–3 vs 1–3

The AI-Program tiering doc defines **Tiers 0–3**; `vocabulary/vocabulary.yaml`
and `policy/tier-controls.yaml` define **tiers 1–3** (Low/Moderate/High). These
checks enforce the repo vocabulary (1–3). No mapping between the two schemes has
been invented here; reconciling them is an open decision for the governance
owner.
