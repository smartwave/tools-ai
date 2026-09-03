---
title: "Personal Assistant"
type: plugin
set: tools
status: building
audience: personal
updated: 2026-08-29
tags:
  - ai-tools
---

# Personal Assistant

Personal productivity skills, packaged as a plugin so one install brings the skill,
its scripts and its format contract together. Named for the category rather than the
contents: it holds one skill today and is meant to hold more.

**Skills**

- **open-items** — reminders of Claude work started and not finished. One folder,
  one file per project, categories inside each file, and a status listing so
  choosing where an item goes is picking from a list rather than remembering.

## Status

building — Tier 0 (proposed) — see `SPEC.md` for the reasoning and the pending
tier review.

## Where the files live

```
~/Documents/Claude/Claude Task Tracker/
    OPEN-ITEMS Claude AI Strategy.md
    OPEN-ITEMS <project>.md
```

One folder, listed rather than searched. Override the location with the
`CLAUDE_TASK_TRACKER` environment variable — the tests use it so they never touch
the real folder. If the folder is unreachable the skill says so and stops; it never
writes a tracker file anywhere else.

## How to run it

### Install from GitHub

```
/plugin marketplace add smartwave/tools-ai
/plugin install personal-assistant@tools-ai
```

The repository is **private**, so this needs git credentials for it. If you cannot
clone the repo, use the export path below instead.

### Export the skill by hand

`skills/open-items/` is self-contained. Copy the whole folder anywhere Claude reads
skills — `~/.claude/skills/open-items/`, another plugin, another repo — and it
works with nothing else present. That is a tested property, not a hope: the
verification pass copies it to an empty directory and runs its tests there.

It has no third-party dependencies and no configuration file. The only thing outside
the folder is the tracker folder itself.

### Use it

Say what you want; the skill triggers on the phrasing.

- **log-item** — "log this", "log where I am", "log that I stopped partway".
  Name the destination ("log to AI Strategy / Governance: …") and it writes
  without asking anything.
- **end-of-session** — "end session", "I'm done"
- **open-items-status** — "what's open", "what have I got unfinished"

The scripts, quoted because the folder name contains spaces:

```bash
python3 skills/open-items/status.py --items    # every project, category and item
python3 skills/open-items/check_ledger.py      # validate every file in the folder
python3 skills/open-items/tests/test_open_items.py
```

`uv run` works too and is the intended runner; neither script needs it, because
neither has dependencies.

## Inputs and outputs

- **Reads:** `OPEN-ITEMS *.md` in the tracker folder. Nothing else, nowhere else.
- **Produces:** item lines written to the file the user picked, in that folder only.

## What this is not

- Not a task tracker. No priorities, deadlines, owners, effort or status.
- Not a system of record. Nothing anyone else depends on.
- **Nothing observes whether work is finished. The user decides.** An item stays
  open until they say to close it, however long that takes — the skill never
  proposes closing something because it saw work happen. It saw a session, not a
  decision.
- **Closing deletes the line.** There is no closed section, no sweep and no
  archive. The skill prints each line in full before deleting it, and that report
  in the conversation is the only record that will exist afterwards.
- One writer per file.

## A note on placeholders

Unlike `ai-solution-builder` and `grc-core`, this plugin carries **no `{{...}}`
placeholder tokens**. It governs nothing and enforces no org control, so there is
no organization-specific value to substitute. The one environment-specific value
it does have — the tracker folder — is configuration, not a placeholder: set
`CLAUDE_TASK_TRACKER`. The absence is deliberate, not an oversight.

## Governing documents

- Spec: `./SPEC.md`
- Format contract: `./skills/open-items/LEDGER-SPEC.md`
- Risk tier: `AI-Program/02-Governance/01-AI-Risk-Tiering.md`
- Done checklist: `AI-Program/02-Governance/06-Definition-of-Done-AI.md`

## Change log

See `./CHANGELOG.md`.
