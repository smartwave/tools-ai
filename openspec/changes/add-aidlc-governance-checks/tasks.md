# Tasks

## 1. Configuration layer and shared library
- [ ] 1.1 Add `config/governance.example.yaml` (org_name, asset_id_prefix, tag_namespace, doc_id_prefix, enforce_pending_insert: false — commented) and add `config/governance.yaml` to `.gitignore`
- [ ] 1.2 Build `ci/lib/config.py`: resolution order (config file → detected literal substitution → exit 3 with copy-the-example message) and `resolve(pattern)` for in-memory token substitution
- [ ] 1.3 Build `ci/lib` helpers: YAML/JSON loading with file+line in errors, provenance-gating function, exit-code conventions
- [ ] 1.4 Pin `PyYAML` + `jsonschema` in `ci/requirements.txt`

## 2. Implement the three stub checks
- [ ] 2.1 `ci/validate-manifest`: JSON-Schema validation (pattern resolved via config), vocabulary cross-check with schema/vocabulary disagreement reported as failure naming both files, tier-1 relaxed required set (asset_id, name, version, workload_type, owner) with warns for the rest
- [ ] 2.2 `ci/check-registry`: resolved asset_id pattern, uniqueness, append-only vs `--base` git ref (default origin/main when available, else skip with notice); lifecycle field changes permitted, id string changes not
- [ ] 2.3 `ci/check-projections`: derive expected topics/tags from `projections/tag-map.yaml` incl. the governed marker topic; diff vs `--topics-file`/`--tags-file`; generator mode when no actuals; always-on leak check for excluded fields in topics
- [ ] 2.4 Fixtures under `ci/tests/fixtures/` (bad enum, duplicate id, rewritten id, leaked topic, passing example) and `ci/tests/run` demonstrating each failure cites the expected control id

## 3. Tier-controls enforcement
- [ ] 3.1 `ci/check-tier-controls`: effective-tier resolution (modifiers first: agent ≥2, regulated →3, local ≤1), declared-below-minimum fails, tier-up allowed
- [ ] 3.2 Closed-set assertions (`allowed_tracks`, `allowed_oversight`) and required_records presence for the effective tier, with provenance gating for `[REF insert]` rows
- [ ] 3.3 Invariant walk: enforce each invariant decidable from manifest+registry; print "not machine-checkable" for the rest; report firing `security_triggers` as routing notices, not failures
- [ ] 3.4 Fixtures: agent-shaped tier-1 fails citing B1.2; regulated tier-2 fails citing B1.3; local-track tier-2 fails citing B1.5; worked example passes

## 4. Gates and evidence
- [ ] 4.1 Create `assets/` layout + README; fixture asset with `preflight.yaml` and `exceptions.yaml`
- [ ] 4.2 `ci/check-gate1`: tier 2+ requires records.requirements + records.epic (B1.9) and registry presence (`[REF insert]`, gated); tier 1 warns
- [ ] 4.3 `ci/check-preflight`: gate items read from `policy/gates.yaml` at runtime; every base item met|exception; exceptions matched, complete, unexpired (B1.8); tier-3 extras when effective tier 3; records.spec present; met-with-empty-evidence fails
- [ ] 4.4 Fixtures: missing evidence, expired exception, missing tier-3 extra — each fails naming gate id and item

## 5. Evaluation lifecycle
- [ ] 5.1 Define and document `assets/<asset_id>/evaluation/eval-set.yaml` and `evaluation/results/*.yaml` formats (fields per design); warn <20 cases or missing case kinds; warn runs <3
- [ ] 5.2 `ci/check-evaluation`: tier 2+ (tier 1 warns): set exists and valid; threshold + reasoning declared_date earlier than earliest results (dates inside files); latest results max error rate ≤ threshold; zero failures in unacceptable kinds; reviewed_by non-empty and reported
- [ ] 5.3 Wire into pre-flight: the correct-result-defined-and-tested item auto-satisfies only when check-evaluation passes, else needs manual evidence
- [ ] 5.4 Fixtures: threshold-after-results ordering failure, over-threshold failure, unacceptable-kind failure, passing case threading through to pre-flight

## 6. Runner, hook, Actions, templates
- [ ] 6.1 `ci/run-all [<manifest> ...]`: dependency-ordered run over `assets/**/manifest.yaml` (+ example in warn-only), summary table check × asset × pass/fail/warn/not-checkable
- [ ] 6.2 `ci/install-hooks`: optional pre-commit running check-registry + validate-manifest on staged files; never auto-installed
- [ ] 6.3 `.github/workflows/governance-checks.yml`: PR + push to main; pinned deps; config materialized from repo variables when present, else annotate "not configured" and pass; calls `ci/run-all` only; leave confluence-sync.yml untouched
- [ ] 6.4 `.github/PULL_REQUEST_TEMPLATE.md` (B1.6: change class, named non-author acceptor, rollback, policy-rule ratification question, re-evaluation trigger question)
- [ ] 6.5 `.github/ISSUE_TEMPLATE/ai-solution-intake.md` (Stage 1/2: technology-free problem statement, baseline "no baseline no project", outcome + measure, audience, data classes, four tiering questions with reasoning, reviewer-capacity statement for tier 2+)

## 7. Documentation and verification
- [ ] 7.1 Rewrite `ci/README.md`: check table all implemented, exit codes, config resolution, provenance gating, tier 0–3 vs 1–3 open item, `assets/` layout
- [ ] 7.2 Update `GOVERNANCE.md` (Enforcement section; config path vs find-and-replace as alternatives), root `README.md` (`assets/`, `config/` rows), `CHANGELOG.md` (one Unreleased entry), `GOVERNANCE-SPEC.md` (stale "CI stubs" caveats revised)
- [ ] 7.3 Final verification: `ci/run-all` exits 0 reporting "not configured" on the fresh unconfigured tree; with test config + fixtures it produces the full summary table; `ci/tests/run` green
