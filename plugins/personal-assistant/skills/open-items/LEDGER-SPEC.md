# Tracker file format

The contract for the files in the tracker folder. Read this before writing to one
— the grammar is exact, and a malformed line is silently skipped when the file is
read back.

`check_ledger.py` enforces everything here. Run it after every write.

---

## The folder

```
~/Documents/Claude/Claude Task Tracker
```

One folder, and every tracker file lives in it. There is no registry and no
scanning: listing the folder is how files are found. `CLAUDE_TASK_TRACKER`
overrides the location, which is how the tests run without touching the real
folder.

If the folder is not reachable, ask for access and stop. Do not write a tracker
file anywhere else — a list you cannot find is the problem this replaces.

## The file

Named `OPEN-ITEMS <project>.md`. The project name comes from the filename, so it
should read the way you would say it: `OPEN-ITEMS Claude AI Strategy.md`.

One file per project. A project is a standing body of work you return to over
weeks or months, not a single task.

## Frontmatter

Exactly four keys, no more:

```yaml
---
title: Claude AI Strategy
scope_prefix: AISTRAT
next_id: 4
updated: 2026-08-29
---
```

| Key | Rule |
| --- | --- |
| `title` | Free text. Normally the same as the project name in the filename. |
| `scope_prefix` | 2–8 characters, uppercase letters and digits, starting with a letter. Unique across every file in the folder. |
| `next_id` | Integer, strictly greater than the highest item number in the file. |
| `updated` | ISO date. Maintained by tooling, not by hand. |

`next_id` must never be able to reuse an ID. If the highest item is `0015`, a
`next_id` of 15 or lower fails validation.

## Sections

One second-level heading, always present:

```markdown
## Open
```

There is no `## Closed` section. Closing an item deletes its line.

## Categories

Third-level headings under `## Open` group items within a project. A category is
a distinct effort inside the project — a topic, a thread of work, a Claude Code
push.

```markdown
## Open

### AIDLC Governance

- [ ] **AISTRAT-0001** — ...

### Learning Guides

- [ ] **AISTRAT-0003** — ...
```

Items may also sit directly under `## Open` with no category. An empty category
heading is fine and stays until you remove it.

## Item grammar

One line per item. Fields in fixed order: text, `find:`, `opened`.

```
- [ ] **PREFIX-NNNN** — Item text · opened YYYY-MM-DD
- [ ] **PREFIX-NNNN** — Item text · find: locator · opened YYYY-MM-DD
```

- Fields are separated by ` · ` — space, U+00B7 middle dot, space.
- The ID is separated from the text by ` — ` — space, U+2014 em dash, space.
- The ID prefix must match the file's `scope_prefix`.
- The checkbox is always `[ ]`. A `[x]` is an error: closing deletes the line.
- `opened` is required and comes last.
- `find:` is optional and holds whatever gets you back — a chat name, a chat ID,
  a topic, a plain reference.

### Reserved characters

**Item text must not contain `·` or `—`, and must not contain a line break.**

A stray middle dot splits the text into a fake field. Because every field after
the text carries a label (`find:` or `opened`), an unlabelled field is a reliable
signal that this has happened, and the validator reports it by name rather than
by guess.

### Write the reminder, not the outcome

The text answers "what was I doing, and where do I pick it back up?" You decide
when something is finished; the file does not need to prove it.

- Yes: `Practitioner learning guides for OnLogic Learning`
- Yes: `Draft the Q3 access review memo · find: chat "Access review memo"`
- Unnecessary: a full outcome statement listing every source and open question

Keep it to a line you can scan.

## IDs

Minted from `next_id`, zero-padded to four digits, then `next_id` is incremented.

**IDs are never reused and never renumbered**, including after a deletion. If
`AISTRAT-0002` is deleted, the next item still takes the current `next_id`.

Because prefixes are unique per file, `AISTRAT-0007` and `TAI-0007` coexist.

## Lifecycle

```
opened → (text updated) → deleted
```

- **Logging an existing item** rewrites its text in place. The ID and `opened`
  date do not change.
- **Closing** deletes the line. There is no archive, no closed date, and no
  sweep. Report what was deleted in the conversation before deleting it — that
  is the only record there is, and it is deliberate.

## What this format does not have

Priority, effort, due dates, assignees, status, owner, blocked, paused, closed
dates. Anything with a real deadline or a second person belongs in a tracker.
Do not ask for these fields, and do not add them to a line.
