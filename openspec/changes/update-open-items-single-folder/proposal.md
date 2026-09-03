# Change: Move open-items to a single tracker folder

## Why

The open-items skill stores one `OPEN-ITEMS.md` at the root of every folder work
happens in. That placement is convenient at write time — the working folder picks
the file, so nothing has to be chosen — but it scatters the files across the
filesystem and leaves no way to see them together. Three pieces exist only to
compensate: a collector script that walks directories, a config file listing scan
roots, and a cached rollup that can be stale without saying so.

The scattering is the problem being solved. Nothing else about the skill is
changing for its own sake.

A second correction comes with it. The skill was written as a task ledger: item
text must be phrased as an outcome so the line itself answers "is this done?".
The actual use is narrower — a reminder of Claude work started and set down
during a workday, closed when the user decides the thread is finished. The text
needs to get the user back to the right conversation, not prove completion.

## What Changes

- All tracker files move to one folder, `~/Documents/Claude/Claude Task Tracker`,
  named `OPEN-ITEMS <project>.md`. Discovery becomes a directory listing.
- Categories arrive as `###` headings inside a file, so one project file can hold
  several distinct efforts.
- A new `status.py` lists projects, categories and counts, so choosing where an
  item goes is picking from a list rather than remembering.
- The folder is checked before any write. If it is unreachable the skill asks for
  access and stops; it never writes a tracker file elsewhere.
- Item text becomes a reminder rather than an outcome statement, with an optional
  `find:` field for a chat name, chat ID, topic or reference.
- Fields after the item text are labelled, which turns the format's known
  corruption case from a heuristic guess into a named error.
- **BREAKING**: closing an item deletes its line. The `## Closed` section, the
  `closed` date, and the seven-day sweep are removed. There is no archive.
- **BREAKING**: the item path field is removed.
- `collect.py`, `templates/config.yaml`, `~/.open-items/` and the `--all` status
  mode are deleted along with the pyyaml dependency.

## Impact

- Affected specs: `open-items`
- Affected code: the `open-items` skill folder in the personal-assistant plugin —
  `SKILL.md`, `LEDGER-SPEC.md`, `ledger.py`, `check_ledger.py`, `templates/`,
  `tests/`; adds `status.py`; deletes `collect.py` and `templates/config.yaml`
- Affected data: the user's own tracker file has already been migrated by hand
  and the previous per-folder ledger deleted. No migration tooling is needed and
  none should be written.
- Out of scope, deliberately parked: surfacing open items unprompted at the start
  of a session.

## Supersedes

This repository's `add-personal-assistant-plugin` change is still in
`openspec/changes/` and has not been archived, so its delta specs are the only
description of the capability. This change supersedes parts of it. Archive that
change first, then this one, so the folds land in the right order.

| Prior delta spec | Effect |
| --- | --- |
| `open-items-ledger` | Modified — the item grammar, the file location and the lifecycle are all restated here |
| `open-items-commands` | Modified — `open-items-status --all` is gone; `log-item` gains the destination-picking flow; `end-of-session` no longer proposes closures |
| `open-items-rollup` | Superseded — the collector, its configuration and the cached rollup are removed outright |
| `personal-assistant-plugin` | Unaffected — the packaging, self-containment and marketplace requirements still hold |

What was removed, and why:

- **Per-folder ledger placement.** Placing `OPEN-ITEMS.md` at the root of each working folder is what scattered the files and made them impossible to see together. It is the problem this change exists to solve. The user's single ledger has already been moved by hand; no migration tooling is required.
- **Cross-scope collection and rollup.** `collect.py`, `~/.open-items/config.yaml` and the cached `rollup.md` / `rollup.json` existed only to answer "where are the files?". One folder answers that by being listed, and the cache's staleness problem no longer has a reason to exist. The user deletes `~/.open-items/` themselves.
- **Closed section and seven-day sweep.** The design relied on version-control history as the archive, and the tracker folder is not a repository. Closed items are deleted outright; nothing is carried forward.
- **Item path field.** The path was relative to the folder the ledger sat in, a concept that no longer exists. Where a reference is useful, `find:` carries it.

## Note for the implementer — resolved

`openspec/specs/open-items/spec.md` does not exist in this repository, so there was
no baseline to modify. The `## MODIFIED Requirements` section has been folded into
`## ADDED Requirements` and `## REMOVED Requirements` dropped, as instructed; the
removal reasoning is kept under **Supersedes** above so it is not lost.
