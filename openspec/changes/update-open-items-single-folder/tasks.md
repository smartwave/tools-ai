# Tasks

A reference implementation of every file below already exists and has been
tested. If it has been dropped into the plugin folder, most of these tasks are
verification rather than authoring — but verify each one rather than assuming.

## 1. Format definition

- [x] 1.1 Rewrite `LEDGER-SPEC.md`: single tracker folder, `CLAUDE_TASK_TRACKER`
      override, `OPEN-ITEMS <project>.md` naming, `###` categories under `## Open`
- [x] 1.2 State the item grammar with labelled fields in fixed order: text,
      optional `find:`, required `opened` last
- [x] 1.3 Remove the `## Closed` section, the `closed` field, the sweep, and the
      item path field from the format
- [x] 1.4 Replace the outcome-writing rule with reminder guidance
- [x] 1.5 Keep the four frontmatter keys unchanged; state that `scope_prefix`
      uniqueness is now scoped to the folder

## 2. Parser

- [x] 2.1 Add `tracker_dir()` reading `CLAUDE_TASK_TRACKER` and defaulting to
      `~/Documents/Claude/Claude Task Tracker`
- [x] 2.2 Replace directory-walking discovery with a glob of `OPEN-ITEMS *.md`
      in one folder; return an empty list when the folder is absent
- [x] 2.3 Derive the project name from the filename
- [x] 2.4 Parse `###` headings as categories and attach each item to the heading
      above it; group categories in file order
- [x] 2.5 Parse `find:` and `opened` as labelled fields; collect anything
      unlabelled as an error candidate rather than silently accepting it
- [x] 2.6 Remove closed-item, closed-date and path handling
- [x] 2.7 Record a missing `## Open` section as an error

## 3. Validator

- [x] 3.1 Fail on a filename not matching `OPEN-ITEMS <project>.md`
- [x] 3.2 Fail on any frontmatter key outside the four allowed
- [x] 3.3 Fail on an unlabelled field, naming the fragment and identifying it as
      a probable stray separator
- [x] 3.4 Fail on a ticked `[x]` checkbox, stating that closing deletes the line
- [x] 3.5 Fail on an empty `find:` field
- [x] 3.6 Keep: prefix match, duplicate IDs, reserved characters in text,
      `next_id` greater than the highest ID, prefix uniqueness across files
- [x] 3.7 Default with no arguments to validating every file in the tracker
      folder; support `--folder`

## 4. Status listing

- [x] 4.1 Add `status.py` printing each project with prefix, `next_id`,
      categories and open counts
- [x] 4.2 Add `--items` to print every open item with its opened date and locator
- [x] 4.3 Add `--folder` to point at somewhere other than the default
- [x] 4.4 Exit with code 2 when the folder is unreachable, writing the path to
      standard error
- [x] 4.5 Flag files that parse with errors and point at `check_ledger.py`
- [x] 4.6 No third-party dependencies

## 5. Skill instructions

- [x] 5.1 Rewrite `SKILL.md`: folder layout, access check before any write, and
      an explicit instruction never to write a tracker file elsewhere
- [x] 5.2 Document the fast path and the interactive pick-from-list path for
      `log-item`, including staying on the chosen destination for the session
- [x] 5.3 Document creating a new project file from the template, including
      asking for a unique `scope_prefix`
- [x] 5.4 Rewrite `end-of-session` so it never proposes closures based on
      observed work, and reports each line before deleting it
- [x] 5.5 Make `open-items-status` run `status.py --items`; remove the `--all`
      mode and the stale-rollup fallback
- [x] 5.6 Note that the folder name contains spaces and script paths need quoting
- [x] 5.7 Update the skill `description` frontmatter to describe a reminder tool,
      keeping the existing trigger phrases

## 6. Template

- [x] 6.1 Update `templates/open-items-template.md`: no Closed section, category
      guidance, new grammar comment, reminder guidance
- [x] 6.2 Delete `templates/config.yaml`

## 7. Deletions

- [x] 7.1 Delete `collect.py`
- [x] 7.2 Confirm nothing imports `collect.py` or references `~/.open-items/`
- [x] 7.3 Confirm no remaining dependency on pyyaml anywhere in the skill

## 8. Tests

- [x] 8.1 Replace fixtures with tracker-folder-named files: one valid, one
      malformed, one carrying the removed features, one badly named
- [x] 8.2 Cover: project name from filename, categories grouped in file order,
      locator present and absent, uncategorised items
- [x] 8.3 Cover the failures: stray separator reported as an unlabelled field,
      missing opened date, prefix mismatch, `next_id` too low, bad filename
- [x] 8.4 Cover the removed features explicitly — a `## Closed` section and a
      `[x]` checkbox must fail rather than be quietly accepted
- [x] 8.5 Cover discovery: only `OPEN-ITEMS *.md` is found; a missing folder
      returns empty
- [x] 8.6 Tests run with `python3` and no third-party dependencies

## 9. Verification

- [x] 9.1 `python3 tests/test_open_items.py` passes
- [x] 9.2 `python3 check_ledger.py --folder "<tracker folder>"` reports the user's
      project file as valid
- [x] 9.3 `python3 status.py --folder "<tracker folder>" --items` lists the
      projects, categories and items
- [x] 9.4 `python3 status.py --folder "<absent folder>"` exits 2
- [ ] 9.5 `openspec validate update-open-items-single-folder --strict` passes — **the OpenSpec CLI is not installed on this machine** (`npx openspec` fails to resolve); the change folder follows the shape of the two existing changes and was reviewed by hand

## 10. Repository integration (beyond the handed-over tasks)

- [x] 10.1 Rename `plugins/personal-assistant/` to `plugins/personal-assistant/` so the directory matches the plugin name set in 6e1c656
- [x] 10.2 Bump the plugin to `2.0.0` and rewrite its description and keywords
- [x] 10.3 Resync `.claude-plugin/marketplace.json` — name, version, description and `source` for all three entries
- [x] 10.4 Rewrite the plugin `README.md`, `SPEC.md` and `CHANGELOG.md` for the new design
- [x] 10.5 Rewrite the `## Open items` block in the repo `CLAUDE.md` — tracker folder, never fall back to the working directory, print before deleting
- [x] 10.6 Replace `.github/workflows/check-ledger.yml` with `open-items-tests.yml` — a runner has no tracker folder to validate, but can run the skill's tests
- [x] 10.7 Update `CATALOG.md` (row + intake), `TOOLKIT.md`, `README.md`, `plugins/README.md` and the root `CHANGELOG.md`
- [x] 10.8 Correct the stale names in the unarchived `add-personal-assistant-plugin` delta spec and its install commands
- [ ] 10.9 Owner: delete `~/.open-items/` — nothing references it any more
