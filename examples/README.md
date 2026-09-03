# examples/

Worked, **validating** examples.

- [`manifest.example.yaml`](manifest.example.yaml) — an internal DataOps tool
  (illustrative values only) that validates against
  [`../schemas/manifest.schema.json`](../schemas/manifest.schema.json). Includes
  a commented deployed-agent variant showing the source-vs-runtime, one-`asset_id`
  pattern.

**Substitution:** the example validates once `{{ASSET_ID_PREFIX}}` and
`{{TAG_NAMESPACE}}` are replaced with literal values — in this file, in
`../schemas/manifest.schema.json`, and in `../vocabulary/vocabulary.yaml`. Until
then the `asset_id` pattern cannot match. See the Configuration table in the
root README.

Examples use illustrative values only — never real customer names, secrets, or
financial data.
