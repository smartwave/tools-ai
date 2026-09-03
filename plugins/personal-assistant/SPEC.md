---
title: "Personal Assistant — Spec"
type: spec
set: tools
status: spec
audience: owner
updated: 2026-08-29
tags:
  - ai-tools
  - spec
---

# Personal Assistant — Spec

Follows the repo lifecycle: catalog row → SPEC with a risk tier → build →
Definition of Done pass → status `built`.

The plugin is a container. This spec covers the container and its first skill,
`open-items`; a second skill gets its own section here rather than its own SPEC.

## Problem and outcome

**What's broken or missing:** Work started in one session and not finished gets lost
between sessions and between surfaces. Chat threads end, Claude's memory is a
synthesis rather than a record, and open loops accumulate in the tails of dated
session notes with no single place to look.

**Outcome when this works:** one question answerable in seconds — what did I start
and not finish? — from one place, with logging fast enough to actually happen
mid-task. A reminder tool that takes a minute to use gets skipped, and a list with
silent gaps is worse than no list because it is still trusted.

**Baseline (2026-08-25):** open items live in the tails of two dated session notes
(`vault-restructure-2026-08-23.md`, `tools-ai-intake-2026-08-25.md`) and in
recollection. No count was known. Items from 2026-08-22 in the AI-Program README had
been open three days with no visible tracking. **Baseline at first run: 26 open
across 2 ledgers** — recorded because Governance 05 Stage 1 requires a baseline
before the build.

**Revised 2026-08-29.** The per-folder ledgers scattered across the filesystem with
no way to see them together, and three components existed only to compensate: a
collector, a config file of scan roots, and a cached rollup that could go stale
without saying so. All files now live in one folder. The second correction: this is
a reminder list, not a task ledger — the text has to return the user to the right
conversation, not prove that something is done.

## Audience and mode

- **Who uses it:** me only. Shared by hand with individuals; nothing published.
- **Mode:** **personal efficiency** — I am the only consumer and I review every
  output.

## Design

| Component | What it is | Runs |
| --- | --- | --- |
| Tracker files | `OPEN-ITEMS <project>.md`, all in one folder | On disk |
| `LEDGER-SPEC.md` | The format contract | — |
| `SKILL.md` | Agent instructions, three commands | Claude Code, Cowork |
| `ledger.py` | Shared parser | Imported |
| `check_ledger.py` | Validator | Locally |
| `status.py` | Listing — projects, categories, counts, items | Locally |
| `.claude-plugin/plugin.json` | Plugin metadata | Read at install |
| `.claude-plugin/marketplace.json` (repo root) | Marketplace index | Read by `/plugin marketplace add` |

The tracker folder is `~/Documents/Claude/Claude Task Tracker`, overridable with
`CLAUDE_TASK_TRACKER`. It is checked before any read or write; unreachable means the
skill states the path, asks for access, and stops. It never falls back to a working
folder, because a list the user cannot find is the problem this design removes.

**Discovery is a directory listing.** One folder, listed. No registry, no configured
scan roots, no walking — and so no cache, and no staleness.

**Pick from a list, not from memory.** Central placement costs the routing that
per-folder placement gave for free, so `status.py` prints the projects and categories
with counts before any question is asked; choosing becomes recognition rather than
recall. Where the user names the destination in the request, nothing is asked at all.

**Deterministic where possible.** Listing, parsing and counting are scripts with no
judgement in them. The model is used only for the two things it is needed for: does
this new item duplicate an existing one, and is this text a usable reminder.

**Files and categories both exist**, and mean different things: a file is a standing
body of work returned to over months, a category is a distinct effort inside it that
will end. The rule is not enforced — the listing is what prevents drift, because the
user sees what already exists before naming anything new.

**Self-contained skill folders.** `skills/open-items/` works when copied out of the
plugin with nothing else present, because hand-export is a supported distribution
path. This forbids shared code at the plugin root; a module two skills need is
duplicated into each. Full reasoning in the change's `design.md`.

## Non-goals

Recorded so the scope does not creep:

- Not a ticket system. No priority, effort, due dates, assignees, or status fields.
- Not a system of record. Nothing anyone else depends on.
- No write-back from any viewer. The tracker files are the only writable surface.
- No sensing of whether work is done. The user asserts it.
- No public release, and no marketplace linter (deferred to
  `projects/claude-config-store/`, which specs one).
- No unprompted surfacing of open items at the start of a session — more useful and
  more annoying; parked for a later change.
- No migration tooling. One file was moved by hand.

## Risk tier

- **Tier:** **0 (proposed)** per `AI-Program/02-Governance/01-AI-Risk-Tiering.md`.
  This is Claude's analysis via the tiering question flow, **pending owner review** —
  same convention as the other catalog rows.
- **Why:**

  | Question | Answer |
  | --- | --- |
  | Takes action without per-action approval? | No. `log-item` and `end-of-session` write only on explicit instruction, and deletion happens only on an item the user names. `status.py` and `check_ledger.py` are read-only deterministic scripts, not AI systems. |
  | Output leaves the organization or informs a material decision? | No. |
  | Output reaches colleagues as work product? | No. Single user. |
  | → | **Tier 0** |

- **Oversight:** human reviews every output; no item closes without confirmation.

**Case for Tier 1 discipline anyway:** the skill writes to files inside the vault
and the repo. A malformed write is a small blast radius but a real one. Two
compensating controls, both already in the build:

- `check_ledger.py` runs after every write; a failed validation is fixed before the
  turn ends.
- Deletion is the sharper edge now that closing removes the line and the tracker
  folder is not a repository. It is bounded by only ever deleting an item the user
  names, and by printing each line in full before deleting it — that report in the
  conversation is the only record that survives.

**Open discrepancy:** Governance `01` uses tiers 0–3; the repo vocabulary uses 1–3.
Tracked as `TAI-0013`; not resolved here. This SPEC uses the Governance numbering,
and the CATALOG row records the tier as `0 (proposed)`.

## Data and access

- **Data it reads:** `OPEN-ITEMS *.md` in the tracker folder, and nothing else
  anywhere else. Item text is whatever the user logs, so it may name clients or
  internal work; it stays on local disk.
- **Data it writes:** item lines in the one file the user picked. **Deletion is
  irreversible** — closing removes the line, the folder is not a repository, and
  there is no archive. Nothing else is written; there is no cache and no config file.
- **Credentials/permissions needed:** none. Local filesystem only, no network, no
  API keys, no third-party packages. Marketplace installation needs git credentials
  for the private repo, and the tracker folder needs to be readable by the surface
  the skill is running in.

## Definition of done

Checked against `AI-Program/02-Governance/06-Definition-of-Done-AI.md`.
Classification: **New AI System.** Tier 0, so the Tier 2+ criteria marked ○ in the
Governance 06 matrix do not apply. Applicable criteria, unchecked pending the pass:

- [ ] Problem statement with measurable outcome — drafted above
- [ ] Baseline recorded — 26 open across 2 ledgers at first run; 2 open in 1 project file after the 2026-08-29 migration
- [ ] Risk tier assigned with reasoning recorded — proposed above, **pending review**
- [ ] Named accountable owner, confirmed — Owner
- [ ] Documented failure mode: what wrong looks like, who notices — below
- [ ] User documentation published, states limitations — `README.md`, `LEDGER-SPEC.md`
- [ ] Admin docs updated: how to stop it, how to roll back, who to call — below
- [ ] Change record raised per the repo lifecycle — CATALOG row + OpenSpec change
- [ ] System owner signs off — Owner

**Documented failure mode.** The characteristic failure is **capture failure** —
logging is skipped because it felt slow, so the list has gaps while still being
trusted. It is the reason the fast path exists and the reason the interactive path
shows counts rather than asking open questions. Nothing detects it beyond each
file's `updated` date going quiet. Who notices: the user, when something they
remember starting is not on the list.

The second failure is **wrongful deletion** — the user names an item to close and
means a different one. Detection is the printed line, before the delete, in the
conversation. There is no undo, so the print is the control.

The third is a **file that drifts from the format** and stops parsing.
`check_ledger.py` after every write catches it; `status.py` flags any file that
parses with errors and points at the validator.

**How to stop it, how to roll back.** Stop: `/plugin uninstall
personal-assistant@tools-ai`, or delete the skill folder. The tracker files
are plain Markdown and survive; nothing runs on a schedule and nothing runs
unattended. Roll back a bad write by editing the file — it is Markdown, and the
skill holds no state of its own. **A deletion cannot be rolled back**; the folder is
not under version control, which is why the line is printed before it goes. Who to
call: the owner.

## Graduation triggers

Re-tier and reconsider the design when any of these occurs:

1. **A second person writes to any tracker file.** Two writers on one Markdown file
   produce conflicts, and conflicts in a list lose items. Then: add per-item `owner`,
   and move cross-person items to a real tracker.
2. **A client engagement gets a project file.** Where client work lives supersedes
   this design — likely a per-client repo, not a personal folder.
3. **Any item becomes something a third party relies on.** Tier 1 at minimum under
   Governance `01`, and it needs a named accountable human per item.
4. **More than roughly 40 open items in one scope.** Deduplication matching becomes
   unreliable and the scope probably wants splitting.
5. **Deleted items start being missed.** Nothing is retained, by decision. If a
   closed item is ever wanted back, that is the signal to add an archive — or to
   put the tracker folder under version control, which is the cheaper fix.
6. **The plugin is published, or the repo is made public.** The sample config and
   the seeded ledgers carry real vault paths and real work items; both need a review
   pass first.

## Deferred, deliberately

| Deferred | Revisit when |
| --- | --- |
| Surfacing open items unprompted at session start | It proves more useful than annoying — parked deliberately |
| An archive of deleted items | A deleted item is genuinely missed |
| HTML or artifact renderer | The `status.py` listing proves too dense to scan |
| Staleness flags on items | The open list gets unmanageable |
| `blocked` / `resume` fields | Items prove hard to pick back up, or the "waiting on me" view is missed |
| A marketplace linter | The three entries drift from their `plugin.json` files once |

## Change Log

| Change Made By | Change Proposed | Why | Date |
| --- | --- | --- | --- |
| Owner | Initial draft, as a standalone skill SPEC | Establish the skill's spec and tier | 2026-08-25 |
| Owner | Rescoped to the `personal-assistant` plugin; added packaging and distribution | A plugin is what Claude installs, and the container survives a second skill | 2026-08-26 |
| Owner | Single tracker folder; reminder text rather than outcome text; closing deletes; collector, config and rollup removed; renamed `personal-assistant` | Scattered files could not be seen together, and the three compensating components existed only to answer a question one folder answers by being listed | 2026-08-29 |
