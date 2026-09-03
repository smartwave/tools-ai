# Delta for Lifecycle Gates

## ADDED Requirements

### Requirement: Per-asset evidence layout
Governance evidence SHALL live in `assets/<asset_id>/`: `preflight.yaml` (one entry per gate item: item, status met|exception|pending, evidence link/path, checked_by, date) and optional `exceptions.yaml` (rule, reason, compensating_control, accepted_by, expires — the B1.8 fields).

#### Scenario: Fixture asset
- GIVEN the fixture asset under `assets/`
- WHEN its files are loaded
- THEN they parse against the documented formats

### Requirement: Gate 1 check
`ci/check-gate1 <manifest>` SHALL require, for effective tier 2+, `records.requirements` and `records.epic` (B1.9) and presence of the asset id in `registry/registry.yaml` (`[REF insert]`, provenance-gated). Tier 1 SHALL warn instead of fail.

#### Scenario: Tier 2 without an epic
- GIVEN an effective Tier-2 manifest whose `records.epic` is missing
- WHEN check-gate1 runs
- THEN it exits 1 citing gate-1 and B1.9

### Requirement: Pre-flight check reads the gate from policy
`ci/check-preflight <manifest>` SHALL load the B1.7 item list (and `tier_3_additional`) from `policy/gates.yaml` at runtime — never hardcoded — and SHALL require every base item met or exception, tier-3 extras at effective tier 3, and `records.spec` present (spec-before-preflight).

#### Scenario: Policy edit changes enforcement
- GIVEN a new item added to the gate's requires list in `policy/gates.yaml`
- WHEN check-preflight runs with no code change
- THEN the new item is required

#### Scenario: Missing Tier 3 extra
- GIVEN an effective Tier-3 asset whose preflight.yaml lacks `adversarial-stress-testing`
- WHEN check-preflight runs
- THEN it exits 1 naming the gate and the item

### Requirement: Evidence is mandatory for met items
A preflight item with `status: met` and empty evidence SHALL fail; a `status: exception` item SHALL require a matching, complete, unexpired entry in `exceptions.yaml`.

#### Scenario: Unevidenced checkbox
- GIVEN an item marked met with no evidence value
- WHEN check-preflight runs
- THEN it exits 1 stating the checklist is an evidence record

#### Scenario: Expired exception
- GIVEN an exception whose `expires` date has passed
- WHEN check-preflight runs
- THEN it exits 1 citing B1.8 and the expired rule
