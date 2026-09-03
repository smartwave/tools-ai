---
name: open-items
description: "Reminders of Claude work started and not finished, kept in one folder at ~/Documents/Claude/Claude Task Tracker, one file per project and categories within it. Use when the user says log this, log an item, log where I am, end session, end of session, let's end the session, what's open, open items status, or asks what they have unfinished. Also use when the user is stopping work partway through something, switching between pieces of work, or orienting at the start of a session."
---

# Open Items

A reminder list of Claude work started and not finished. It exists because it is
easy to start something during a workday, move to something else, and forget the
first thing was ever open.

This is not a task tracker. It carries no priorities, deadlines, or owners, and
it does not know whether anything is done.

The format is defined in `LEDGER-SPEC.md` — **read it before writing to any
file.**

## Core rule

**Nothing observes whether work is finished. The user decides.**

An item stays open until the user says to close it, however long that is. Never
propose closing something because work on it happened in front of you — you saw
a session, not a decision. Closing deletes the line permanently, so it only ever
happens on an explicit instruction.

## Where things live

```
~/Documents/Claude/Claude Task Tracker/
    OPEN-ITEMS Claude AI Strategy.md
    OPEN-ITEMS <project>.md
```

One folder. One file per project. Categories are `### headings` inside a file.

**Check the folder first, every session that touches it.** `status.py` exits
with code 2 when the folder is not reachable. When that happens, tell the user
the exact path and ask them to grant access, then stop. Do not create the file
somewhere else, and do not fall back to a working folder — a list they cannot
find is the problem this design removes.

## Running the scripts

Every path below is relative to this skill folder, which is self-contained and
works wherever it has been copied. Quote paths: the folder name contains spaces.

```bash
uv run status.py                    # projects, categories, counts
uv run status.py --items            # ... and every open item
uv run check_ledger.py              # validate every file in the folder
uv run tests/test_open_items.py     # the skill's own tests
```

`uv` is the intended runner. Neither script has dependencies, so `python3` works
too.

## Before writing to a file

1. Read `LEDGER-SPEC.md`. The item grammar is exact.
2. Read the file itself.
3. Run `check_ledger.py` after writing. If it fails, fix it before ending your
   turn.

---

## Command: `log-item`

Triggered by: "log this", "log an item", "log where I am", "log that I stopped
partway", or the user describing something they started and are setting down.

**Fast path.** When the user names the destination — "log to AI Strategy /
Governance: ..." — write it there. Do not ask anything. Speed is the whole point;
a reminder tool that takes a minute to use gets skipped, and a list with gaps is
worse than no list because it gets trusted.

**Interactive path.** When they don't:

1. Run `status.py`. Show the projects with their counts and ask which one, or a
   new name.
2. Show that project's categories with their counts and ask which one, or a new
   name.
3. Once chosen, stay there for the rest of the session unless told otherwise.

Then:

4. Compare against the open items in that file. A probable match updates that
   item's text in place, keeping its ID and `opened` date. Ambiguous → ask:
   "This looks like AISTRAT-0001. Update it, or is this separate?"
5. New item: mint from `next_id`, increment `next_id`.
6. Write the text as a **reminder** — what it was and how to get back to it, in
   one scannable line. Add `find:` when there is a chat name, chat ID, topic, or
   reference to record. Leave it off when there isn't.
7. Set `opened` to today. Update `updated` in the frontmatter.
8. Validate, then confirm briefly: the ID and the line you wrote.

Creating a new project file: name it `OPEN-ITEMS <project>.md`, copy
`templates/open-items-template.md`, and ask for a `scope_prefix` (2–8 uppercase
characters, unique across the folder — `status.py` shows the ones in use).

Do not ask follow-up questions about priority, effort, or dates. The format does
not have those fields.

---

## Command: `end-of-session`

Triggered by: "end session", "end of session", "let's end the session", "I'm
done", or the user clearly stopping work.

1. Run `status.py --items` and list what is open, in one message, not one item at
   a time.
2. Ask which to cross off. Say nothing about which ones look finished.
3. Delete the lines the user names. Report each deleted line in full first — the
   file keeps no record of it afterwards.
4. If the user started something this session that is not on the list, propose an
   item for it. Only what you actually observed; do not guess at work you did not
   see.
5. Update `updated` in the frontmatter of any file you changed.
6. Validate, then report: what was deleted, what remains open.

Keep this short. It is a two-minute operation and it will be skipped if it feels
like a meeting.

---

## Command: `open-items-status`

Triggered by: "what's open", "open items status", "what have I got unfinished".

Run `status.py --items` and report it. Default to everything in the folder; narrow
to one project only when the user asks for one.

This is the command that gets used most. Answer it plainly — the list, oldest
first, nothing added.

---

## Tone

Terse. Confirm what you wrote, nothing more. No summaries of the session, no
encouragement, no restating the user's items back in prose. The file is the
output.
