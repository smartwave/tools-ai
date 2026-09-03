# Tasks

A tested reference implementation sits in `reference/`. Most tasks are "adapt and
verify" rather than "write from scratch". Where the reference and the delta specs
disagree, the specs win.

Two stop points: **before group 7** (writes into the vault and home directory) and
**before group 9.4** (archiving).

## 1. Scaffold the plugin

- [x] 1.1 Create `plugins/personal-assistant/`, `.claude-plugin/`, `skills/open-items/` and `skills/open-items/templates/`
- [x] 1.2 Copy `reference/ledger.py`, `check_ledger.py`, `collect.py` into `skills/open-items/`
- [x] 1.3 Copy `reference/SKILL.md` into `skills/open-items/`
- [x] 1.4 Copy `reference/templates/*` into `skills/open-items/templates/`
- [x] 1.5 Write `skills/open-items/LEDGER-SPEC.md` from the `open-items-ledger` delta spec — it is the human-readable form of the same contract
- [x] 1.6 Write `.claude-plugin/plugin.json`: name `personal-assistant`, displayName `Personal Assistant`, version `1.0.0`, description, personal author, keywords. Follow `plugins/grc-core/.claude-plugin/plugin.json`; no `{{...}}` tokens
- [x] 1.7 Write `README.md` from `_templates/tool-README-template.md`: what this is, what it is not, both install paths, the placeholder-edition exception
- [x] 1.8 Write `SPEC.md` from `_templates/tool-SPEC-template.md`, absorbing `reference/TIER-AND-DOD.md`
- [x] 1.9 Write `CHANGELOG.md`, matching `plugins/ai-solution-builder/CHANGELOG.md`
- [ ] 1.10 Confirm `uv` is installed; verify `uv run check_ledger.py --help` resolves dependencies

## 2. Parser

- [x] 2.1 Verify `ledger.py` is the only module containing parsing logic, and that neither script duplicates it
- [x] 2.2 Verify the item regex matches all four grammar forms in the ledger delta spec
- [x] 2.3 Verify frontmatter parsing handles all four required keys and rejects malformed lines
- [x] 2.4 Verify `find_ledgers` always skips `.git`, `node_modules`, `_archive`, `__pycache__` and de-duplicates by resolved path

## 3. Validator

- [x] 3.1 Verify every check listed in the rollup delta spec's Validator requirement is implemented
- [x] 3.2 Verify all errors are reported, not just the first, and that each names a line number where applicable
- [x] 3.3 Verify the exit code is non-zero on any failure
- [x] 3.4 Verify `--root` scans and validates every ledger beneath a directory
- [x] 3.5 Verify duplicate `scope_prefix` across two ledgers is reported when validating multiple files

## 4. Collector

- [x] 4.1 Verify the collector never modifies a ledger
- [x] 4.2 Verify a malformed ledger is reported as a problem without failing the whole run
- [x] 4.3 Verify each scope's `updated` date appears in the Markdown rollup
- [x] 4.4 Verify items sort oldest first by `opened` date within each scope
- [x] 4.5 Verify `extra_outputs` writes additional copies of the Markdown rollup
- [x] 4.6 Verify absent configuration falls back to defaults and writes a notice to stderr

## 5. Skill

- [x] 5.1 Verify `SKILL.md` describes all three commands and their natural-language triggers
- [x] 5.2 Verify it instructs reading `LEDGER-SPEC.md` before any write
- [x] 5.3 Verify it instructs running the validator after every write
- [x] 5.4 Verify `end-of-session` presents all open items in one message, not one at a time
- [x] 5.5 Verify no command closes an item without user confirmation
- [x] 5.6 Verify `log-item` deduplicates against open items only, never closed ones
- [x] 5.7 Verify ledger creation asks the user for a `scope_prefix` rather than inventing one
- [x] 5.8 Verify `open-items-status --all` states the rollup's generation date when falling back

## 6. Packaging: portability and marketplace

- [x] 6.1 Verify every path in `SKILL.md` resolves relative to the skill folder — no plugin-root and no repo path
- [x] 6.2 Verify `check_ledger.py` and `collect.py` import `ledger.py` from their own directory, not from the working directory
- [x] 6.3 Verify `collect.py` defaults to `~/.open-items/config.yaml`, honours `--config`, and does not assume a repo checkout
- [x] 6.4 Copy `skills/open-items/` alone to a scratch directory outside the repo; run the validator against a ledger there. This is the self-containment test
- [x] 6.5 Write `README.md`'s "Export this skill" section: copy the folder anywhere Claude reads skills; the only external dependency is `~/.open-items/config.yaml`, and only for `--all`
- [x] 6.6 Write `.claude-plugin/marketplace.json` at the **repo root**: marketplace name `tools-ai`, owner block, and entries for all three plugins with `source` as a relative path
- [x] 6.7 Verify each marketplace entry's `name` and `version` equal that plugin's `plugin.json` — by hand, all three
- [x] 6.8 Add one line to `README.md` (repo root) and `TOOLKIT.md` noting the repo is a plugin marketplace and how to add it

## 7. Tests

- [x] 7.1 Write a fixture ledger that is valid, and assert the validator exits zero
- [x] 7.2 Write a fixture ledger containing every error class in the Validator requirement, and assert each is reported
- [x] 7.3 Assert the stray-separator case produces the "split item text" error specifically
- [x] 7.4 Assert the collector merges two valid ledgers into one rollup with the correct open count
- [x] 7.5 Assert two ledgers sharing a prefix produce a reported problem
- [x] 7.6 Assert running the collector twice on unchanged ledgers produces identical output apart from the generation date

## 8. Deploy — **stopped here; 8.1–8.4, 8.7, 8.8 await review**

Writes outside the repo, into the vault and home directory.

- [ ] 8.1 Install `~/.open-items/config.yaml` from the template; set real scan roots
- [ ] 8.2 Point `extra_outputs` at the Obsidian vault so the rollup lands somewhere already visible
- [ ] 8.3 Seed a tracker file for this repo (the seeded ledgers are held internally, not in this repo)
- [ ] 8.4 Seed a tracker file for the vault AI-Program folder (same — held internally)
- [x] 8.5 Add the open-items block to each repo's `CLAUDE.md` — from `reference/INTEGRATION-SNIPPETS.md`, with paths rewritten to `plugins/personal-assistant/skills/open-items/`
- [x] 8.6 Add `.github/workflows/check-ledger.yml`, path-filtered to `**/OPEN-ITEMS.md` and `plugins/personal-assistant/**` — also runs the skill tests
- [ ] 8.7 Run `uv run collect.py --print` and confirm the rollup matches the two ledgers
- [ ] 8.8 Push the branch; from a directory outside this repo run `/plugin marketplace add smartwave/tools-ai` then `/plugin install personal-assistant@tools-ai`, and confirm the skill loads

## 9. Repository lifecycle

Per the repo lifecycle: catalog row → SPEC with a tier → build → Definition of Done
pass → status `built`.

- [x] 9.1 Add the `CATALOG.md` row, status `spec`, plus a dated intake paragraph below the table
- [ ] 9.2 Review the Tier 0 proposal now in `SPEC.md`; confirm or change it
- [ ] 9.3 Resolve or explicitly defer the tier-numbering discrepancy — Governance `01` uses 0–3, the repo vocabulary uses 1–3 (tracked as `TAI-0013`)
- [ ] 9.4 Run the Definition of Done pass in `SPEC.md`
- [ ] 9.5 Move the CATALOG row to status `built`
- [ ] 9.6 Update the root `CHANGELOG.md`
- [ ] 9.7 Commit

## 10. Review before archiving this change

- [ ] 10.1 Review the seeded items — they are drawn from session notes and may include work already finished
- [ ] 10.2 Run `end-of-session` in both scopes as the first real reconciliation
- [ ] 10.3 Tune `exclude` patterns after the first full scan; the first run will surface ledgers in forgotten places
- [ ] 10.4 Archive this change so the four delta specs merge into `openspec/specs/`
