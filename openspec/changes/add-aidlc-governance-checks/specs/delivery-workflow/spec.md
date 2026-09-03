# Delta for Delivery Workflow

## ADDED Requirements

### Requirement: Single-command runner
`ci/run-all [<manifest> ...]` SHALL run every check in dependency order over all manifests (default `assets/**/manifest.yaml`, plus `examples/manifest.example.yaml` warn-only) and end with one summary table of check × asset × pass/fail/warn/not-checkable.

#### Scenario: Unconfigured generic clone stays green
- GIVEN a fresh clone with placeholders intact and no config
- WHEN run-all executes
- THEN every check reports "not configured" and run-all exits 0

#### Scenario: Configured run with fixtures
- GIVEN test config and the fixture assets
- WHEN run-all executes
- THEN the summary table lists every check result including warn and not-checkable rows

### Requirement: One implementation, two surfaces
`.github/workflows/governance-checks.yml` SHALL run on pull_request and push to main, install the pinned dependencies, materialize `config/governance.yaml` from repo variables when present (else annotate "not configured" and pass), and invoke only the same `ci/` scripts a local run uses. The existing `confluence-sync.yml` MUST NOT be modified. `ci/install-hooks` SHALL offer an optional pre-commit hook (check-registry + validate-manifest on staged files) and MUST NOT auto-install.

#### Scenario: CI mirrors local
- GIVEN a violation reproducible locally with `ci/run-all`
- WHEN the workflow runs on the same commit
- THEN the same check fails with the same control id in its message

### Requirement: Change-control PR template
`.github/PULL_REQUEST_TEMPLATE.md` SHALL capture B1.6 change control: what changed, change class, a named acceptor other than the author, rollback note, whether a `policy/` rule changed (with its Confluence ratification status), and whether an asset's behavior changed (triggering re-evaluation per AIDLC Stage 9).

#### Scenario: Policy rule change surfaced
- GIVEN a PR that edits `policy/tier-controls.yaml`
- WHEN the author fills the template
- THEN the ratification-status question forces the pending-vs-live distinction to be stated

### Requirement: AI-solution intake template
`.github/ISSUE_TEMPLATE/ai-solution-intake.md` SHALL capture AIDLC Stage 1/2: a technology-free problem statement, current process with baseline error rate ("no baseline, no project"), outcome and measure, who the output reaches, data classes, the four tiering questions with recorded reasoning, and a reviewer-capacity statement for tier 2+.

#### Scenario: Technology-first request converted
- GIVEN a requester who writes "we want to use AI for X"
- WHEN they complete the template
- THEN the problem statement field requires the current cost and error rate before any tool is named
