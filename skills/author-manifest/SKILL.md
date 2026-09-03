---
name: author-manifest
description: >
  Emit a governance manifest that validates against the schema. STUB — not yet
  implemented.
version: 0.0.0
status: stub
---

# author-manifest (stub)

## Intent
Produce a per-asset governance manifest (SKILL.md frontmatter, plugin manifest,
or `SOLUTION.md`) that validates against `schemas/manifest.schema.json`, using
`examples/manifest.example.yaml` as the reference shape.

## Must honor
- Tier 2+ → manifest is MUST; Tier 1 → SHOULD (minimal field set).
- Values must come from `vocabulary/vocabulary.yaml`.
- Link the governed records (Requirements, Spec, Epic); the manifest is the
  single source of truth, not a copy of another surface.

## TODO
- [ ] Gather fields (from classify-workload output where available).
- [ ] Validate against the schema before writing.
- [ ] Fail loudly on any value outside the controlled vocabulary.
