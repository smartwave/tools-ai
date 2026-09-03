# Delta for Tier-Controls Enforcement

## ADDED Requirements

### Requirement: Effective-tier resolution with modifiers
`ci/check-tier-controls <manifest>` SHALL resolve the effective tier by applying `modifiers` from `policy/tier-controls.yaml` before the tier row: `shape: agent` forces tier ≥ 2 (B1.2), `data_class: regulated` forces tier 3 (B1.3), `track: local` caps at tier 1 (B1.5). A declared tier below the forced minimum SHALL fail; a declared tier above it SHALL pass.

#### Scenario: Agent shape declared Tier 1
- GIVEN a manifest with `shape: agent` and `tier: 1`
- WHEN check-tier-controls runs
- THEN it exits 1 citing B1.2 and the forced minimum of 2

#### Scenario: Voluntary tier-up
- GIVEN a workflow-shaped, confidential-data manifest declaring `tier: 3`
- WHEN check-tier-controls runs
- THEN no tier violation is reported

### Requirement: Closed-set and record assertions
For the effective tier the check SHALL assert `track` ∈ `allowed_tracks`, `oversight` ∈ `allowed_oversight`, and presence of the tier's `required_records` in `records`, with `[REF insert]` rows subject to provenance gating.

#### Scenario: Autonomous oversight at Tier 2
- GIVEN an effective Tier-2 manifest with `oversight: autonomous`
- WHEN check-tier-controls runs
- THEN it exits 1 citing B1.4 and the allowed envelope [hitl, hotl]

### Requirement: Invariant walk with honest coverage
The check SHALL evaluate every entry in `invariants`, enforcing each one decidable from the manifest and registry, and SHALL list every rule it cannot machine-check as "not machine-checkable" in the output so silence never reads as coverage. Rules read from the policy file at runtime; none hardcoded.

#### Scenario: Undecidable invariant reported
- GIVEN a manifest carrying no dependency declaration
- WHEN check-tier-controls evaluates `no-app-on-app`
- THEN the output lists that invariant as not machine-checkable rather than passing it silently

### Requirement: Security-trigger routing notices
The check SHALL report each firing `security_triggers` condition (e.g., non-empty `mcp_servers`) as a routing notice, not a failure.

#### Scenario: Connector in use
- GIVEN a manifest listing an MCP server
- WHEN check-tier-controls runs and no other rule is violated
- THEN it exits 0 and the output states that Security review is triggered by connector use
