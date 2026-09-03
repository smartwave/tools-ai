# Project Context

## Purpose

`tools-ai` is two things in one repository: the catalog of built AI tools (`CATALOG.md` + type folders `plugins/`, `skills/`, `agents/`, `mcps/`, `prompts/`, `projects/`) and the machine-readable **AI governance layer** at the repo root (`GOVERNANCE.md` is its front door): controlled vocabulary, manifest schema, tier→controls policy data, gates, asset registry, tag projections, and CI checks. Read root `CLAUDE.md` first — it tells an agent how to use the governance layer.

## Tech Stack

- Governance rules-as-data: YAML (`policy/`, `vocabulary/`, `registry/`, `projections/`) and JSON Schema (`schemas/manifest.schema.json`)
- Checks: Python 3.11+, dependencies limited to `PyYAML` and `jsonschema` (pinned in `ci/requirements.txt`)
- Check entry points: existing `ci/<name>` script names and CLIs are the contract — keep them
- CI: GitHub Actions (one new workflow; do not modify `.github/workflows/confluence-sync.yml`)

## Project Conventions

- The tree is a **generic edition**: every org-specific value is a `{{DOUBLE_BRACE}}` placeholder. Never substitute placeholders in committed files; adopter values come from git-ignored `config/governance.yaml` (see the active change).
- Provenance tags in `policy/` govern enforceability: enforce only `[REF Bx]` / `[REF Technical Controls]`; `[REF insert]` and `[PROPOSED]` rules are warn-only unless `enforce_pending_insert: true` in config.
- Exit codes for checks: 0 pass, 1 violation (message cites control id + file + line), 3 not configured. Checks run offline — no network calls ever.
- Rule sources, in precedence order: `policy/tier-controls.yaml` (tier requirements, modifiers, invariants), `policy/gates.yaml` (Gate 1, pre-flight/B1.7), `policy/standards.yaml` (control-id index), `schemas/` + `vocabulary/` (manifest shape/values), `projections/tag-map.yaml` (tags/topics + exclusions).
- Known discrepancy, do not resolve: the AI-Program docs define Tiers 0–3; this repo's vocabulary defines 1–3. Checks enforce the repo vocabulary; the discrepancy is noted in `ci/README.md` as an open item.
- Narrative companion: `BUILDOUT-SPEC-aidlc-checks.md` at the repo root is the prose version of the active change — consult it for rationale; the OpenSpec change artifacts govern where they differ.

## Domain Glossary

- **Manifest** — per-asset governance record validating against `schemas/manifest.schema.json` (asset_id, tier, track, shape, oversight, data_class, owner, records, …).
- **Tier** (1–3) — risk level per B1.3; drives required records, gates, and controls.
- **Gate 1** — requirements approved before build; **pre-flight** — the B1.7 go-live checklist.
- **Modifiers** — manifest facts that force a minimum tier (agent shape → ≥2; regulated data → 3; local track → max 1).
- **Evaluation set** — the AIDLC Stage 3 artifact: known-correct cases plus an acceptable error rate declared **before** results exist.
