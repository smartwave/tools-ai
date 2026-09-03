---
name: open-items
description: "Track open items — things started and not finished — in a per-folder OPEN-ITEMS.md ledger. Use when the user says log this, log an item, log where I am, end session, end of session, let's end the session, what's open, open items status, or asks what they have unfinished. Also use when the user is stopping work partway through something, switching between pieces of work, or orienting at the start of a session."
---

# Open Items

A ledger of things started and not finished. One `OPEN-ITEMS.md` per folder the user
works in. Three commands. The format is defined in `LEDGER-SPEC.md` — **read it
before writing to any ledger.**

## Core rule

**Nothing observes whether work is done. The user tells you.**

You may propose closing an item based on what you saw in this session. You never
close one without confirmation. This is the user's sign-off and it is the only
mechanism there is.

## Before writing to a ledger

1. Read `LEDGER-SPEC.md` in this skill folder. The item grammar is exact and a
   malformed line gets silently skipped by the collector.
2. Read the ledger itself.
3. Run `check_ledger.py` against it after writing. If it fails, fix it before
   ending your turn.

## Which ledger

The one at the root of the folder the current session is working in. Never reach
into another scope's ledger — a session in `tools-ai` does not know what happened
in the vault, so anything it wrote there would be a guess.

If no `OPEN-ITEMS.md` exists in the working folder, offer to create one from
`templates/open-items-template.md`, and ask the user for a `scope_prefix` (2–8
uppercase characters, unique across their ledgers).

---

## Command: `log-item`

Triggered by: "log this", "log an item", "log where I am", "log that I stopped
partway", or the user describing something they started and are setting down.

1. Read the ledger.
2. Compare against existing **open** items on the path field and text similarity.
   - Probable match → update that item's text in place. Keep its ID and `opened` date.
   - Ambiguous → ask: "This looks like TAI-0014. Update it, or is this separate?"
   - No match → mint a new item from `next_id`, increment `next_id`.
3. Write the item text **as an outcome, not an activity.** "Three stub CI checks
   implemented and passing" — not "look at the CI checks." If the user's phrasing is
   activity-shaped, rewrite it and show them what you wrote.
4. Set `opened` to today. Add the path field if the item points at a specific file.
5. Update `updated` in the frontmatter.
6. Validate, then confirm briefly: the ID and the line you wrote.

Do not ask follow-up questions about priority, effort, or dates. The format does not
have those fields.

---

## Command: `end-of-session`

Triggered by: "end session", "end of session", "let's end the session", "I'm done",
or the user clearly stopping work.

1. Read the ledger's `## Open` list.
2. **Ask about each open item in one message, not one at a time.** List them and ask
   which are done. Where you saw work on an item during this session, say so —
   "TAI-0014: the checks passed in front of me, close it?" — but still wait for
   confirmation.
3. Close the ones the user confirms: move to `## Closed`, flip to `[x]`, append
   `closed <today>`.
4. If the user started something during this session that is not in the ledger,
   propose an item for it. Only propose what you actually observed in this session;
   do not guess at work you did not see.
5. Sweep: delete closed items whose `closed` date is more than 7 days ago.
6. Update `updated` in the frontmatter.
7. Validate, then report: what closed, what was swept, how many remain open.

Keep this short. It is a two-minute operation and it will be skipped if it feels
like a meeting.

---

## Command: `open-items-status`

Triggered by: "what's open", "open items status", "what have I got unfinished".

**Current scope (default):** read the local ledger, list the open items with their
IDs and opened dates, oldest first.

**All scopes (`--all`, or "everything", "across all my ledgers"):** run
`collect.py`. It scans the roots in `~/.open-items/config.yaml`, parses every
`OPEN-ITEMS.md` it finds, and writes `rollup.md` and `rollup.json`. Report from its
output.

If `collect.py` cannot run (no filesystem access in this surface, roots not
scoped), read `~/.open-items/rollup.md` if it is reachable and **state its
`updated` date**, so the user knows how stale it is. Do not present a stale rollup
as current.

---

## Tone

Terse. Confirm what you wrote, nothing more. No summaries of the session, no
encouragement, no restating the user's items back to them in prose. The ledger is
the output.
