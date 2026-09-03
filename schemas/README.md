# schemas/

Structural **contracts** for governed records.

- [`manifest.schema.json`](manifest.schema.json) — JSON Schema (draft 2020-12)
  for the per-asset governance manifest. Describes the Tier 2+ shape (MUST); for
  Tier 1 only `asset_id`, `name`, `version`, `workload_type`, and `owner` are
  expected.

A worked, validating instance is in [`../examples/manifest.example.yaml`](../examples/manifest.example.yaml).
The manifest is the single source of truth for an asset's governance metadata;
AWS tags and GitHub topics are projections of it (see [`../projections/`](../projections/)).
