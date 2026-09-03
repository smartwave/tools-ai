# Changelog — tools-ai governance layer (formerly ai-org-management)

Repo-level history. Each machine-readable file also carries its own
`schema_version` (SemVer 2.0.0); this log records repo-wide structural changes.
Pre-1.0.0 (`0.x.y`) denotes draft with no stability guarantee.

## [Unreleased]

### Removed
- **2026-09-03 — internal-only material moved out of the repo.** Two items were
  not safe to publish and are now held internally, with pointers left behind. The
  gate-recalibration amendment plan (`projects/gate-recalibration/`) named the
  organization in prose, carried three live wiki page IDs, and named a real vendor
  and a specific production solution; its own README had flagged the decision as
  outstanding. The seeded open-items ledgers
  (`openspec/changes/add-personal-assistant-plugin/reference/seeded/`) were a dated
  inventory of unclosed governance gaps — what the AI program does not yet have —
  which is not a public document. The travel-risk and TPRM skills were sanitized in
  place rather than removed; see Changed.

### Changed
- **2026-09-03 — Agentic SDLC page restated as not-yet-created.** `sync-map.yaml`,
  `confluence/pages/agentic-sdlc-platform.md`, `confluence/pages/README.md` and
  `.github/CODEOWNERS` described that page as living in a personal wiki space with
  an unfilled owner — a standing governance gap in the record. The page does not in
  fact exist: the adopting organization creates it in `{{WIKI_SPACE_KEY}}`, or the
  equivalent in whatever knowledge tool it uses. All four files now say that, with
  the five prerequisites before `sync: true` listed once in the page source.
  `{{WIKI_PERSONAL_SPACE_KEY}}` is retired from `PLACEHOLDERS.md`;
  `{{PLATFORM_SECURITY_LEAD_ROLE}}` stays a normal adopter-substituted token whose
  CODEOWNERS reviewer is the change-control gate.
- **2026-09-03 — travel-risk and TPRM skills sanitized.** The travel skill's
  pre-approved country list and short-stay threshold became
  `{{TRAVEL_PREAPPROVED_COUNTRIES}}` and `{{TRAVEL_SHORT_STAY_LIMIT}}`, and its
  acceptance tests now describe seven risk profiles instead of named countries with
  standing verdicts — a fixed country list both goes stale and reads as a judgement
  about those countries. The TPRM scoring matrix is labelled a reference
  configuration rather than the policy transcribed verbatim, with the policy stated
  as governing; the band-reconciliation note it carried is held internally.
- **2026-09-03 — de-identified ahead of publication.** Plugin ids, the marketplace
  id, and the install coordinates are now neutral: `personal-assistant`, `tools-ai`,
  and `smartwave/tools-ai`. Install with `/plugin marketplace add smartwave/tools-ai`
  then `/plugin install personal-assistant@tools-ai`. Owner rows and sign-off lines in
  prose now read `Owner`. Hard-coded personal machine paths became configuration:
  `LEDGER-SPEC.md` states the default tracker folder with the `CLAUDE_TASK_TRACKER`
  override, and the openspec reference config no longer names personal scan roots.
  Removed a tracked archive folder and a committed `__pycache__` artifact.

### Added
- **2026-09-02 — Stage 0 of `ai-solution-builder` restructured into Frame → POC Brief →
  Build → POC Summary.** The pipeline used to start at "build a POC", so the AI Use
  Framework's first habits — map the work first, invest in the input, you author the
  intent — had no artifact before the prototype. Three new skills add them:
  `ai-problem-framer` (the one-page Ultralight Problem Brief: problem statement by 5W1H,
  root cause by Five Whys with validation, process-level future state through lenses;
  three gated phases, earlier sections read-only, written in the person's own words),
  `ai-poc-brief-author` (the POC Brief with a paste-ready build prompt), and
  `ai-poc-summary-author` (what the POC did, every vibe-coded change, the ask to IT).
  `ai-poc-builder` now builds from the brief and keeps a change log. Four new
  references carry the methods and templates, and a `gems/` folder ships five Gemini
  Gem instruction sets producing the same outputs. Plugin `1.4.0`. Delivered through
  `openspec/changes/add-problem-framing-stage/`.

### Changed
- **2026-08-29 — open-items moved to a single tracker folder (breaking).** The
  `open-items` skill no longer keeps an `OPEN-ITEMS.md` at the root of each working
  folder. All tracker files live in `~/Documents/Claude/Claude Task Tracker` as
  `OPEN-ITEMS <project>.md` (overridable with `CLAUDE_TASK_TRACKER`), with `###`
  categories inside each file; discovery is a directory listing. Adds `status.py`
  (projects, categories, counts, items) so choosing a destination is picking from a
  list. Item text becomes a reminder with an optional `find:` locator rather than an
  outcome statement, and fields after the text are labelled, which turns the format's
  stray-separator corruption from a heuristic guess into a named error. Breaking:
  closing an item deletes its line — the `## Closed` section, the `closed` date and
  the seven-day sweep are removed, and there is no archive; `collect.py`,
  `templates/config.yaml`, `~/.open-items/`, the `--all` status mode and the pyyaml
  dependency are deleted, leaving the skill stdlib-only. The plugin is `2.0.0` and
  was renamed `personal-assistant`, directory included, to match the rename in
  6e1c656; `.github/workflows/check-ledger.yml` becomes `open-items-tests.yml`,
  because a hosted runner has no tracker folder to validate but can still run the
  skill's tests. Delivered through
  `openspec/changes/update-open-items-single-folder/`.

### Changed
- **2026-08-25 — consolidated into `tools-ai`.** The standalone
  `ai-org-management` repo was merged into the tools-ai repo root:
  `vocabulary/`, `schemas/`, `policy/`, `registry/`, `projections/`,
  `examples/`, `confluence/`, `ci/`, and `.github/` moved to the root; the five
  governance skills moved into the shared `skills/` folder; the repo README
  became `GOVERNANCE.md`; `CLAUDE.md` was extended to cover the combined repo.
  Relative paths inside the governance files are unchanged.

### Added
- **2026-08-26 — `personal-assistant` plugin, and the repo became a plugin
  marketplace.** Added `plugins/personal-assistant/` — a container for personal
  productivity skills, first skill `open-items`: a per-folder `OPEN-ITEMS.md`
  ledger of unfinished work with three commands, a format validator
  (`check_ledger.py`, also run in CI by the new `.github/workflows/check-ledger.yml`),
  a cross-scope collector (`collect.py`), the `LEDGER-SPEC.md` format contract, and
  24 tests. The skill folder is self-contained so it can be exported or duplicated by
  hand. Delivered through `openspec/changes/add-personal-assistant-plugin/` (four
  delta specs). Added `.claude-plugin/marketplace.json` at the repo root, listing all
  three plugins, so they install with `/plugin marketplace add smartwave/tools-ai`.
  `CATALOG.md`, `README.md`, `TOOLKIT.md`, `plugins/README.md` and `CLAUDE.md`
  updated. This plugin is deliberately outside the placeholder edition — it is
  personal tooling and carries no `{{TOKEN}}` values.

### Added
- **2026-08-25 — org-wide Claude configuration store spec.** Added
  `projects/claude-config-store/` holding the reconstruction spec for the golden
  repo pattern (a private Claude Code plugin marketplace distributing org-approved
  plugins, skills, instructions, and MCP stubs), plus its `README.md` and `SPEC.md`
  (Tier 2, proposed). Spec only — nothing built, no existing structure changed.
  Angle-bracket placeholders in the imported spec were converted to `{{TOKEN}}` form
  for controlled values; the two new tokens are folder-local and deliberately not in
  `PLACEHOLDERS.md`.
- **2026-08-26 — gate-recalibration amendment plan imported** as a plan-only
  artifact (held at `projects/gate-recalibration/` at the time; moved out of the
  repo on 2026-09-03, see Unreleased → Removed): an acquisition
  exemption class held by a seven-condition test, and an advisory-gate posture
  for Tier 2/3 split into a write-path and a documentation reading. No
  normative language is drafted and eight open decisions remain, so `policy/`,
  `vocabulary/`, `schemas/`, and the `ci/` checks are deliberately unchanged —
  the Confluence standard is the ratification surface, and the rules-as-data
  edit follows the prose, not the other way round.
- **2026-08-25 — AIDLC checks and gates implemented.** The three CI stubs are
  now real checks and five more join them: `validate-manifest`,
  `check-registry`, `check-projections`, `check-tier-controls`, `check-gate1`,
  `check-preflight`, `check-evaluation`, plus `run-all`, `install-hooks`, and a
  fixture suite (`ci/tests/run`) that asserts one failing case per rule with
  the control id in the message. Shared library in `ci/lib/` owns config
  resolution and provenance gating, so `[REF insert]` and `[PROPOSED]` rules
  stay warn-only until `enforce_pending_insert` is set. New `config/` layer
  (`governance.example.yaml`; the real file is git-ignored) lets adopters
  configure the checks without substituting placeholders in the tree. New
  `assets/<asset_id>/` evidence layout: `preflight.yaml`, `exceptions.yaml`,
  and `evaluation/` (eval set with a declared threshold, dated results). New
  `.github/workflows/governance-checks.yml`, PR template (B1.6 change control)
  and AI-solution intake issue template (AIDLC Stage 1/2).
- Full repository scaffold: `vocabulary/`, `schemas/`, `policy/`, `registry/`,
  `projections/`, `examples/`, `confluence/`, `skills/`, `ci/`, each with a
  README; root `README.md` (now `GOVERNANCE.md`), `CLAUDE.md`, and this
  changelog.
- `policy/tier-controls.yaml` (0.2.0) — tier→required-controls matrix
  (rules-as-data), reconciled against the live AI Solution Standards
  **v{{AI_STANDARD_VERSION}}**.
- `policy/standards.yaml` and `policy/gates.yaml` — stubs for the B1.x control
  catalog and the lifecycle-gate definitions.
- `confluence/sync-map.yaml` — repo-section ↔ Confluence-page binding.
- Skill and CI stubs (not yet implemented).

### Seeded from the naming/tagging module
- `vocabulary/vocabulary.yaml`, `schemas/manifest.schema.json`,
  `registry/registry.yaml`, `projections/tag-map.yaml`,
  `examples/manifest.example.yaml`, and the two `confluence/inserts/*`.

### Notes
- **Not ratified.** Confluence is the ratification surface. Rows tagged
  `[REF insert]` depend on the pending {{AI_STANDARD_PENDING_VERSION}}
  naming/tagging control and must not be enforced until it lands.
