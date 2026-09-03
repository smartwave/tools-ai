# Changelog — personal-assistant

All notable changes to this plugin. Versions follow SemVer.

## [2.0.0] — 2026-08-29

Breaking. The skill moves from a ledger scattered across working folders to a single
tracker folder, and from a task ledger to a reminder list.

### Changed
- **One tracker folder.** All files live in `~/Documents/Claude/Claude Task Tracker`,
  named `OPEN-ITEMS <project>.md`, overridable with `CLAUDE_TASK_TRACKER`. Discovery
  is a directory listing; there is no scanning, no registry and no configuration.
  The scattering was the problem being solved — everything else follows from it.
- **Categories inside a file.** `###` headings under `## Open` group distinct efforts,
  so one project file can hold several threads.
- **Item text is a reminder, not an outcome.** The old rule required text that proved
  completion, because nothing observed doneness. Under the actual use the user decides
  when a thread is finished, and the text needs to return them to the right
  conversation instead. An optional `find:` field carries a chat name, chat ID, topic
  or reference.
- **Fields after the item text are labelled** (`find: `, `opened `). This turns the
  format's one corruption case — a stray middle dot splitting the text into a fake
  field — from a heuristic guess into a named error.
- **The folder is checked before any write.** Unreachable means the skill states the
  path, asks for access, and stops. It never falls back to a working folder.
- **`log-item` picks from a list.** `status.py` prints projects and categories with
  counts before asking, so choosing is recognition rather than recall — and naming the
  destination in the request skips the questions entirely.
- **`end-of-session` no longer proposes closures.** It lists what is open and asks;
  it says nothing about what looks finished.

### Added
- **`status.py`** — lists every project with its prefix, `next_id`, categories and
  open counts; `--items` prints every open item. No dependencies, no judgement.
- Validation of the filename pattern, unlabelled fields, ticked checkboxes, empty
  `find:` fields, and any frontmatter key outside the four allowed.

### Removed
- **`## Closed`, the `closed` date, and the seven-day sweep.** Closing an item now
  deletes its line. The old design called version history the archive, and the tracker
  folder is not a repository. The skill prints each line in full before deleting it;
  that report is the only record that survives.
- **`collect.py`, `templates/config.yaml`, `~/.open-items/` and the `--all` status
  mode** — they existed only to answer "where are the files?", which one folder
  answers by being listed. The pyyaml dependency goes with them; the skill is now
  stdlib-only. Delete `~/.open-items/` yourself.
- **The item path field.** It was relative to the folder the ledger sat in, a concept
  that no longer exists. `find:` carries a reference where one is useful.

### Notes
- Delivered through `openspec/changes/update-open-items-single-folder/`.
- The plugin was renamed `personal-assistant` (directory included) and the
  marketplace is `tools-ai`.
- Migration was one file moved by hand. No migration tooling exists and none should
  be written.
- Parked deliberately: surfacing open items unprompted at the start of a session.

## [1.0.0] — 2026-08-26

### Added
- **Plugin created** — `personal-assistant`, a container for personal-productivity
  skills. Named for the category so a second skill needs no rename, no version
  discontinuity and no second marketplace entry.
- **New skill `open-items`** — a per-folder `OPEN-ITEMS.md` ledger of work started
  and not finished. Three commands: `log-item` (mint or update an item,
  deduplicating against open items), `end-of-session` (reconcile every open item in
  one message, close what the user confirms, sweep items closed more than 7 days
  ago), and `open-items-status` (current scope, or `--all` for the cross-scope
  rollup). No item is ever closed without confirmation.
- **`LEDGER-SPEC.md`** — the format contract: file location, frontmatter, item
  grammar, reserved characters, ID minting and the opened → closed → swept
  lifecycle. Read before any write.
- **`ledger.py`, `check_ledger.py`, `collect.py`** — shared parser, format
  validator (runs locally and in CI), and the collector that discovers every ledger
  by filesystem scan, merges the open items and writes `rollup.md` and
  `rollup.json`. Deterministic: no model is involved in walking, parsing, merging
  or sorting.
- **Templates** — an empty ledger and a `~/.open-items/config.yaml` starting point.
- **Self-containment** — `skills/open-items/` is functional when copied out of the
  plugin with nothing else present, so it can be exported or duplicated by hand.
  Its only external dependency is `~/.open-items/config.yaml`, and only for
  `--all`.

### Notes
- Tier 0 is **proposed, pending review** — see `SPEC.md`.
- The tier-numbering discrepancy (Governance `01` uses 0–3, the repo vocabulary
  1–3) is tracked as `TAI-0013` and is not resolved here.
