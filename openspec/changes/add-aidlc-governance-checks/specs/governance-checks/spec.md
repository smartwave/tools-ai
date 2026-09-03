# Delta for Governance Checks (manifest, registry, projections)

## ADDED Requirements

### Requirement: Manifest validation
`ci/validate-manifest <manifest> [...]` SHALL validate manifests against `schemas/manifest.schema.json` (asset_id pattern resolved via config) and cross-check every enumerated value against `vocabulary/vocabulary.yaml`. Schema/vocabulary disagreement SHALL be reported as a failure naming both files. For `tier: 1` manifests only `asset_id, name, version, workload_type, owner` are required; missing Tier-2+ fields warn.

#### Scenario: Valid worked example
- GIVEN test config values and `examples/manifest.example.yaml` with tokens substituted in memory
- WHEN validate-manifest runs
- THEN it exits 0

#### Scenario: Bad enumerated value
- GIVEN a manifest with `oversight: continuous`
- WHEN validate-manifest runs
- THEN it exits 1 naming the field, the offending value, and the allowed vocabulary values

### Requirement: Registry integrity
`ci/check-registry` SHALL assert every asset_id in `registry/registry.yaml` matches the resolved pattern, ids are unique, and the registry is append-only versus a base git ref (`--base`, default origin/main when available, else skip with a notice). Lifecycle field changes are permitted; changing or removing an id string is a violation.

#### Scenario: Rewritten id
- GIVEN an id present at the base ref changed in the working tree
- WHEN check-registry runs with that base
- THEN it exits 1 identifying the old and new id

#### Scenario: Retirement is not a violation
- GIVEN an entry whose `lifecycle` changed to `retired` with the id unchanged
- WHEN check-registry runs
- THEN it passes

### Requirement: Projection conformance and leak prevention
`ci/check-projections <manifest>` SHALL derive expected GitHub topics and AWS tags from `projections/tag-map.yaml` (including the governed marker topic), diff them against actuals supplied via `--topics-file`/`--tags-file`, and MUST fail if `environment`, `owner`, `business_unit`, or any excluded class appears in the topics actuals. With no actuals supplied it SHALL print the expected projection and exit 0.

#### Scenario: Sensitive value leaked to topics
- GIVEN a topics file containing an owner value
- WHEN check-projections runs
- THEN it exits 1 identifying the leaked field regardless of other matches

#### Scenario: Generator mode
- GIVEN no actuals files
- WHEN check-projections runs on a valid manifest
- THEN the expected topics and tags are printed and it exits 0

### Requirement: Offline operation
Checks MUST NOT make network calls; all external state (topics, tags, git refs) arrives as arguments, files, or the local git repository.

#### Scenario: No network available
- GIVEN a machine with no network access
- WHEN the full check suite runs
- THEN behavior is identical to a networked machine
