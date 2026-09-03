# Delta for Governance Config

## ADDED Requirements

### Requirement: Adopter configuration without tree substitution
The check suite SHALL read adopter values (org_name, asset_id_prefix, tag_namespace, doc_id_prefix, enforce_pending_insert) from git-ignored `config/governance.yaml`, with a committed `config/governance.example.yaml`, and SHALL NOT modify any `{{...}}` placeholder in committed files.

#### Scenario: Config present
- GIVEN `config/governance.yaml` copied from the example
- WHEN any check runs
- THEN patterns from schema/vocabulary/tag-map are resolved with the config values in memory only
- AND no committed file changes

#### Scenario: No config, placeholders intact
- GIVEN a fresh generic clone with no config file
- WHEN any check runs
- THEN it exits 3 with a one-line instruction to copy the example to `config/governance.yaml`

#### Scenario: Tree already substituted
- GIVEN an adopter performed the documented find-and-replace so no placeholders remain
- WHEN a check runs without a config file
- THEN the literal values detected in the tree are used and the check proceeds

### Requirement: Provenance-gated enforcement
The shared library SHALL enforce only rules tagged `[REF Bx]` or `[REF Technical Controls]`; rules tagged `[REF insert]` or `[PROPOSED]` SHALL run warn-only unless `enforce_pending_insert: true`.

#### Scenario: Pending rule with default config
- GIVEN `enforce_pending_insert: false`
- WHEN a manifest violates the asset-id-at-gate-1 rule (`[REF insert]`)
- THEN the violation is reported as a warning and does not affect the exit code

#### Scenario: Pending rule enabled
- GIVEN `enforce_pending_insert: true`
- WHEN the same violation occurs
- THEN the check exits 1 citing the rule

### Requirement: Exit-code contract
Every check SHALL exit 0 on pass, 1 on violation (message citing control id, file, and line where possible), and 3 when not configured. Exit 2 ("not implemented") MUST NOT occur.

#### Scenario: Violation message content
- GIVEN a manifest with `track: local` and `tier: 2`
- WHEN `ci/check-tier-controls` runs
- THEN it exits 1 and the message names B1.5, the manifest path, and the offending field
