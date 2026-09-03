---
title: "Buildout Spec — AIDLC Checks & Gates"
type: spec
set: tools
status: spec
audience: owner
updated: 2026-08-25
tags:
  - ai-tools
  - spec
  - governance
  - aidlc
---

# Buildout Spec — AIDLC checks and gates for the tools-ai repo

**Audience: a Claude Code session implementing this in the tools-ai repo.** Read this whole file, then `CLAUDE.md` at the repo root, before writing anything.

## 1. Problem and outcome

**Problem.** The repo's governance layer defines the rules of the AI delivery lifecycle as data (`policy/tier-controls.yaml`, `policy/gates.yaml`, `policy/standards.yaml`, `schemas/manifest.schema.json`, `vocabulary/vocabulary.yaml`) — but nothing enforces them. The three checks in `ci/` are stubs that exit 2, there is no machine check for the Gate 1 or pre-flight (B1.7) checkpoints, and the AIDLC's evaluation-set discipline (define "correct" and the acceptable error rate *before* building, re-measure after) has no home in the repo at all.

**Outcome when done.** Any manifest-carrying asset in this repo (and later, in governed repos) can be checked mechanically: does the manifest validate, is the asset registered correctly, do its projections match, does it satisfy its tier's requirements, has it passed Gate 1, is its pre-flight checklist evidenced, and does its evaluation record exist in the right order (threshold declared before results). The checks run locally today with one command and run identically in GitHub Actions when the repo is pushed. A check that cannot run because the adopter has not configured the repo says so clearly instead of failing cryptically.

## 2. Decisions already made (do not revisit)

1. **Local scripts + Actions wrapper.** Every check is a locally runnable script; a single GitHub Actions workflow calls the same scripts. One implementation, two surfaces.
2. **Scope.** Implement the three stub checks, add tier/gate/evaluation checks and PR/intake templates. Do **not** implement the five governance skills in `skills/` (classify-workload, mint-asset-id, author-manifest, project-tags, confluence-projection) — they stay stubs. Do not touch the Confluence sync workflow.
3. **Config file, keep the tree generic.** Do not substitute `{{...}}` placeholder tokens anywhere in the existing tree. Instead, checks read adopter values from a git-ignored local config (see §5). The repo remains the shareable generic edition.

## 3. Sources of truth and their precedence

- `policy/tier-controls.yaml` — what each tier requires: allowed tracks/oversight, required records and gates, modifiers, invariants. **This is the primary rulebook the checks enforce.**
- `policy/gates.yaml` — Gate 1 and pre-flight definitions, including the B1.7 item list and Tier 3 extras.
- `policy/standards.yaml` — control-id index (B1.2–B1.9 etc.); use for check names/messages so failures cite a control id.
- `schemas/manifest.schema.json` + `vocabulary/vocabulary.yaml` — manifest shape and allowed values.
- `projections/tag-map.yaml` — how manifest fields become AWS tags / GitHub topics, and which fields are excluded from public topics.
- The AI-Program docs (05-Process-AIDLC, 04-Standards-AI-Systems, in the SmartWave vault / Claude project) are the *design rationale* for the evaluation-set and stage checks in §8–§9. Where this spec's conventions (file names, evidence formats) are not in any source, they are this spec's own design — implement as written here.

**Enforcement gating (hard rule, from `ci/README.md` and the provenance convention in `policy/tier-controls.yaml`):** enforce only rules tagged `[REF Bx]` or `[REF Technical Controls]`. Rules tagged `[REF insert]` (asset-id minting at Gate 1, tier-2+ manifest MUST, registry format) or `[PROPOSED]` are enforced **only** when the config sets `enforce_pending_insert: true`; otherwise they run in warn-only mode (report, exit 0 for that rule). Build this gating into the shared library, not into each check ad hoc.

**Known discrepancy — do not resolve silently:** the AI-Program tiering doc defines Tiers 0–3; the repo vocabulary defines tiers 1–3 (Low/Moderate/High). The checks enforce the **repo vocabulary (1–3)**. Do not invent a mapping; note the discrepancy in `ci/README.md` as an open reconciliation item.

## 4. Implementation constraints

- Language: Python 3.11+ for check logic (needs YAML + JSON Schema); keep the existing `ci/<name>` entry points as thin bash wrappers or replace them with Python scripts of the same names and CLIs — the file names and usage lines documented in the current stubs are the contract; keep them.
- Dependencies: `PyYAML` and `jsonschema` only. Pin versions in `ci/requirements.txt`. No other third-party packages.
- Shared code in `ci/lib/` (a small module: config loading, placeholder detection, provenance gating, YAML/JSON loading with line-number-bearing error messages).
- Every check: exit 0 = pass, exit 1 = violation (message names the control id, file, and line where possible), exit 3 = not configured (placeholders unsubstituted and no config present), exit 2 remains "not implemented" and must no longer occur.
- All checks must run offline. No network calls. GitHub-topic and AWS-tag *actuals* are passed in as arguments or files (see check-projections); the checks never query GitHub or AWS themselves.
- Do not modify: `policy/*.yaml`, `vocabulary/vocabulary.yaml`, `schemas/manifest.schema.json`, `projections/tag-map.yaml`, `confluence/**`, the two plugins under `plugins/`. Exception: `ci/README.md` and root docs listed in §11.

## 5. Work item 1 — configuration layer

**Files:** `config/governance.example.yaml` (committed), `config/governance.yaml` (git-ignored; add to `.gitignore`), `ci/lib/config.py`.

`governance.example.yaml` carries every value the checks need, commented, with the same defaults the placeholder docs name:

```yaml
org_name: "Example Org"
asset_id_prefix: "ORG-AI-"     # includes trailing hyphen; immutable once assets are minted
tag_namespace: "org"           # no punctuation
doc_id_prefix: "ORG"
enforce_pending_insert: false  # [REF insert] rules warn-only until the naming/tagging insert is ratified
```

Resolution order: `config/governance.yaml` if present, else fall back to detecting literal substitution in the tree (an adopter who did the documented find-and-replace never needs the config), else exit 3 with a one-line instruction to copy the example. The loader also exposes `resolve(pattern)` that substitutes `{{ASSET_ID_PREFIX}}` / `{{TAG_NAMESPACE}}` tokens in patterns read from the schema/vocabulary/tag-map at runtime, so those files stay generic on disk.

**Accept when:** with the example copied to `governance.yaml`, `ci/validate-manifest examples/manifest.example.yaml` gets past configuration; with no config and placeholders intact, every check exits 3 with the copy-the-example message.

## 6. Work item 2 — implement the three stub checks

### 6.1 `ci/validate-manifest <manifest.yaml> [...]`
- Validate against `schemas/manifest.schema.json` (with `asset_id.pattern` resolved via config).
- Cross-check every enumerated value against `vocabulary/vocabulary.yaml` (the schema and vocabulary must agree; disagreement is a failure that names both files).
- Tier-conditional shape: the schema's `required` list is the Tier 2+ shape. For `tier: 1` manifests, require only `asset_id, name, version, workload_type, owner` (per the schema's own description) and warn on the rest.
- The example manifest contains placeholder tokens; the check must substitute config values into the *manifest under test* only in memory, never on disk.

### 6.2 `ci/check-registry`
- Every `asset_id` in `registry/registry.yaml` matches the resolved pattern `^<prefix>[A-Z0-9]+(-[A-Z0-9]+)+$`; ids unique.
- Append-only: compare against a base ref (`ci/check-registry --base <git-ref>`, default `origin/main` when available, else skip with a notice) — no id removed or rewritten. `lifecycle: retired` is a permitted field change; id string changes are not.

### 6.3 `ci/check-projections <manifest> [--topics-file F] [--tags-file F]`
- Derive expected GitHub topics and AWS tags from the manifest per `projections/tag-map.yaml` (including the `<namespace>-ai-governed` marker topic).
- Diff against actuals supplied in the given files (one item per line for topics; `key=value` per line for tags). With no actuals supplied, print the expected projection and exit 0 (generator mode — useful locally).
- **Leak check always runs:** fail if `environment`, `owner`, `business_unit`, or any value matching the excluded classes in the tag-map appears in the topics actuals.

**Accept when:** the worked example passes all three under test config; a fixture set under `ci/tests/fixtures/` includes at least one failing case per rule (bad enum, duplicate id, rewritten id, leaked topic) and `ci/tests/run` demonstrates each failure with the expected control id in the message.

## 7. Work item 3 — `ci/check-tier-controls <manifest>` (new)

The heart of the SDLC enforcement. Given a manifest, resolve its **effective tier** and assert the tier row from `policy/tier-controls.yaml`:

1. Apply `modifiers` first, exactly as the file's "How to read this file" section says: `shape: agent` forces tier ≥ 2 (B1.2); `data_class: regulated` forces tier 3 and reports the data-privacy involvement requirement (B1.3/Roles); `track: local` caps at tier 1 (B1.5). A manifest whose declared tier is *below* its forced minimum fails; above is permitted (tier-up is always allowed).
2. Assert closed sets: `track` in `allowed_tracks`, `oversight` in `allowed_oversight` for the effective tier.
3. Assert `oversight_rules` conditions where the manifest carries the facts (e.g., tier 2+ with `oversight: autonomous` is a violation per the tier envelope; deeper condition facts like "irreversible" are not in the manifest — report as "not machine-checkable here", do not guess).
4. Assert `required_records` for the tier are present and non-empty in `records` (requirements/spec/epic). Respect provenance gating: the records themselves are `[REF B1.9/B1.7]` (enforce); asset-id-at-gate-1 is `[REF insert]` (gate behind config).
5. Walk `invariants` and enforce each one that is decidable from the manifest + registry (e.g., `tier-2-plus-manifest` is trivially met by having a manifest; `local-tier-1-only`, `agent-raises-tier` are decidable; `no-app-on-app` requires a dependency declaration — check only if the manifest carries one; others report "not machine-checkable").
6. Report `security_triggers` that fire (e.g., `mcp_servers` non-empty → "connector in use: Security review is triggered") — these are routing notices, not failures.

**Accept when:** fixtures demonstrate: agent-shaped tier-1 manifest fails with B1.2 cited; regulated tier-2 fails with B1.3; local track tier-2 fails with B1.5; the worked example passes; every "not machine-checkable" rule is listed in the output so silence never reads as coverage.

## 8. Work item 4 — gate checks and evidence files (new)

Per-asset governance evidence lives in `assets/<asset_id>/` (new top-level folder, one subfolder per minted asset):

- `assets/<asset_id>/preflight.yaml` — one entry per B1.7 item from `policy/gates.yaml` (`requires` list plus `tier_3_additional` when applicable): `{item, status: met|exception|pending, evidence: <link or path>, checked_by, date}`.
- `assets/<asset_id>/exceptions.yaml` (optional) — B1.8 exceptions: `{rule, reason, compensating_control, accepted_by, expires}`.

### 8.1 `ci/check-gate1 <manifest>`
Tier 2+ only (Tier 1 warns): `records.requirements` and `records.epic` present (B1.9); asset id present in `registry/registry.yaml` (`[REF insert]` — gated). Cites `gate-1` from `policy/gates.yaml`.

### 8.2 `ci/check-preflight <manifest>`
- Loads the gate definition from `policy/gates.yaml` — the item list is **read from the policy file, never hardcoded**, so a policy edit changes the check without a code change.
- Every base item `met` or `exception`; every `exception` has a matching, unexpired entry in `exceptions.yaml` with all fields filled (B1.8).
- Tier 3 (effective tier from the §7 logic): the three `tier_3_additional` items required.
- `records.spec` present (spec-before-preflight invariant, B1.7).
- An item with `status: met` and empty `evidence` fails — the checklist is an evidence record, not a box-ticking exercise. (This mirrors the never-check-an-unevidenced-box guardrail already load-bearing in the plugins.)

**Accept when:** a fixture asset passes; removing evidence, expiring an exception, or dropping a Tier 3 extra each fails with the gate id and item named.

## 9. Work item 5 — evaluation-set convention and check (new)

Implements AIDLC Stages 3 and 6 (the evaluation set defined before build; the measured error rate compared to a threshold agreed in advance). File conventions here are this spec's design.

- `assets/<asset_id>/evaluation/eval-set.yaml` — `{owner (business owner, not builder), scoring_method, rubric (text or path), acceptable_error_rate, error_rate_reasoning, unacceptable_error_kinds: [...], declared_date, cases: [{id, input|input_ref, expected, kind: routine|edge|ambiguous|insufficient-information|known-hard}]}`. Minimum 20 cases (warn below; the 20–100 range is the AIDLC's) and at least one case of each of the five kinds (warn if missing).
- `assets/<asset_id>/evaluation/results/<YYYY-MM-DD>-<label>.yaml` — `{run_date, runs (≥1; AIDLC asks for 3 — warn below), model, model_version, prompt_version, scores: [...], error_rate_range: {min, max}, failures_by_kind: {...}, reviewed_by}`.

### `ci/check-evaluation <manifest>`
- Tier 2+ (per Standards 4.4/4.5; Tier 1 warns): the eval set exists, is schema-valid, and `acceptable_error_rate` + reasoning carry a `declared_date` **earlier than the earliest results file** — the threshold was set before results existed. Ordering by the declared dates inside the files, not filesystem timestamps.
- Latest results: `error_rate_range.max` ≤ `acceptable_error_rate`, and `failures_by_kind` shows zero in every `unacceptable_error_kinds` category.
- `reviewed_by` non-empty and different from the manifest `owner` only if the owner is the builder — cannot be machine-decided; instead require `reviewed_by` non-empty and report who.
- `check-preflight` gains a dependency: the `correct-result-defined-and-tested-including-edge-cases` B1.7 item is auto-satisfiable only when `check-evaluation` passes; otherwise it must carry manual evidence.

**Accept when:** fixtures show a threshold-declared-after-results ordering failure, an over-threshold failure, and an unacceptable-kind failure, each with a clear message; the passing fixture threads through to pre-flight.

## 10. Work item 6 — runner, hook, Actions, and templates

- `ci/run-all [<manifest> ...]` — runs every check in dependency order against all manifests found (default: `assets/**/manifest.yaml` plus `examples/manifest.example.yaml` in warn-only mode); one summary table at the end: check × asset × pass/fail/warn/not-checkable.
- `ci/install-hooks` — optional `pre-commit` hook that runs `check-registry` and `validate-manifest` on staged files only (fast path; full `run-all` stays manual/CI). Do not auto-install.
- `.github/workflows/governance-checks.yml` — on `pull_request` and `push` to main: checkout, install pinned deps, materialize `config/governance.yaml` from repo variables when present (else the workflow annotates "not configured" and passes — a generic clone must stay green), run `ci/run-all`. Do not modify the existing `confluence-sync.yml`.
- `.github/PULL_REQUEST_TEMPLATE.md` — B1.6 change control: what changed; change class; **acceptor other than the author** (named); rollback note; "does this change a `policy/` rule?" (if yes: cite the Confluence ratification status); "does this change an asset's behavior?" (if yes: re-run evaluation per Stage 9 triggers).
- `.github/ISSUE_TEMPLATE/ai-solution-intake.md` — AIDLC Stage 1/2: problem in one sentence with no technology named; current process, cost, baseline error rate ("no baseline, no project"); outcome and measure; who the output reaches; data classes; the four tiering questions with the reasoning recorded; reviewer-capacity statement for Tier 2+.

**Accept when:** `ci/run-all` on the fresh tree (no config) exits 0 with everything reported "not configured"; with test config + fixtures it produces the summary table; the workflow file lints (`actionlint` if available, else careful review) and references only the same scripts.

## 11. Documentation updates (same change set)

- `ci/README.md` — rewrite the check table (all statuses `implemented`), document exit codes, config resolution, enforcement gating, the tier 0–3 vs 1–3 discrepancy note, and the `assets/` evidence layout.
- `GOVERNANCE.md` — add a short "Enforcement" section pointing at `ci/README.md` and the config layer; note that the placeholder find-and-replace path and the config path are alternatives.
- Root `README.md` structure table — add `assets/` and `config/` rows.
- `CHANGELOG.md` — one entry under `[Unreleased]` for the whole buildout.
- New rows are **not** added to `CATALOG.md` (the checks are part of the governance layer, covered by `GOVERNANCE-SPEC.md`); instead update `GOVERNANCE-SPEC.md`'s Definition-of-Done section: the "CI stubs" caveats are now stale — revise its Data-and-access lines and note the checks are implemented.

## 12. Non-goals (do not do)

- No implementation of the five governance skills; no changes to the two plugins.
- No substitution of placeholder tokens in the committed tree; no editing of `policy/`, `vocabulary/`, `schemas/`, `projections/` content values.
- No network calls from checks; no GitHub/AWS API clients.
- No enforcement of `[REF insert]` / `[PROPOSED]` rules by default.
- No new process invention: where the policy files and this spec are silent, prefer reporting "not machine-checkable" over inventing a rule.

## 13. Suggested implementation order

1. Config layer + shared lib (§5) — everything depends on it.
2. validate-manifest, check-registry, check-projections (§6) with fixtures.
3. check-tier-controls (§7).
4. Evidence layout + check-gate1 + check-preflight (§8).
5. Evaluation convention + check-evaluation (§9).
6. run-all, hook, Actions workflow, templates (§10).
7. Docs (§11). Run `ci/run-all` both unconfigured and configured as the final verification.

Commit in these increments with the repo's PR-template discipline in mind (even if committing directly): each increment's message states what rule coverage it adds.

## 14. Open items for the owner (implementer: surface these, do not decide them)

- Choose real values for `asset_id_prefix` and `tag_namespace` before minting any real asset — ids are immutable.
- Ratification status of the naming/tagging insert governs `enforce_pending_insert`.
- The tier 0–3 (AI-Program) vs 1–3 (repo vocabulary) reconciliation.
- Whether evaluation evidence for client work belongs in this repo or per-client repos — `assets/` assumes this repo for now.
