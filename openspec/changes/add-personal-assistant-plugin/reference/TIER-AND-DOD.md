---
title: SPEC — open-items skill
type: spec
set: tools
status: draft
audience: personal
updated: 2026-08-25
tags: [skill, open-items, tier-0]
---

# SPEC — open-items skill

Follows the tools-ai lifecycle: catalog row → SPEC with a risk tier → build →
Definition of Done pass → status `built`.

---

## Problem

Work started in one session and not finished gets lost between sessions and between
surfaces. Chat threads die, Claude's memory is a synthesis rather than a record, and
open loops end up scattered across dated session notes with no single place to look.

## Outcome required

Two questions answerable in under a minute, from any surface:

1. Did I start something and not finish it?
2. Is it done now?

## Baseline (current state, 2026-08-25)

Open items live in the tails of two dated session notes
(`vault-restructure-2026-08-23.md`, `tools-ai-intake-2026-08-25.md`) and in
recollection. No count is known. Items from 08-22 in the AI-Program README have been
open for three days with no visible tracking. **Baseline count at first run: 26 open
across 2 ledgers** — recorded here because Governance 05 Stage 1 requires a baseline
before the build.

## Non-goals

Recorded so the scope does not creep:

- Not a ticket system. No priority, effort, due dates, assignees, or status fields.
- Not a system of record. Nothing anyone else depends on.
- No write-back from any viewer. The ledgers are the only writable surface.
- No sensing of whether work is done. The user asserts it.

---

## Design

| Component | What it is | Runs |
| --- | --- | --- |
| Ledgers | `OPEN-ITEMS.md`, one per scope | On disk |
| `LEDGER-SPEC.md` | The format contract | — |
| `SKILL.md` | Agent instructions, three commands | Claude Code, Cowork |
| `ledger.py` | Shared parser | Imported |
| `check_ledger.py` | Validator | Locally, and in CI per repo |
| `collect.py` | Collector — scan, merge, write rollup | Locally |
| `~/.open-items/config.yaml` | Scan roots | — |

Data flows one direction only: ledgers → collector → rollup. Nothing writes
backwards. If write-back is ever wanted, that is the signal to move to a real
tracker instead of extending this.

**Discovery, not registration.** Ledgers are found by scanning for the filename.
There is no registry file, because a registry is a second thing to keep in sync and
its only data — where the ledgers are — is better answered by the filesystem.

**Deterministic where possible.** Walking, parsing, merging and sorting are scripts.
The model is used only for judgment: is this item done, and does this new item
duplicate an existing one.

---

## Risk tier

**Proposed: Tier 0** (Governance `01`). This is my analysis via the tiering question
flow, pending review.

| Question | Answer |
| --- | --- |
| Takes action without per-action approval? | No. `log-item` and `end-of-session` write only on explicit instruction and per-item confirmation. `collect.py` writes rollup files but is a deterministic script, not an AI system. |
| Output leaves the organization or informs a material decision? | No. |
| Output reaches colleagues as work product? | No. Single user. |
| → | **Tier 0** |

**Case for Tier 1 discipline anyway:** the skill writes to files inside the vault and
the repo. A malformed write is a small blast radius but a real one. Compensating
controls, both already in the build:

- `check_ledger.py` runs after every write; a failed validation is fixed before the
  turn ends.
- Scopes under version control make any bad write recoverable from git history.
  `AIP-0011` tracks bringing the vault under version control for this reason.

**Open discrepancy:** Governance `01` uses tiers 0–3; the tools-ai repo vocabulary
uses 1–3. Tracked as `TAI-0013`. This SPEC uses the Governance numbering.

---

## Definition of Done (Governance `06`)

Classification: **New AI System.** Tier 0, so the Tier 2+ criteria marked ○ in the
Governance 06 matrix do not apply. Applicable criteria, unchecked pending a pass:

- [ ] Problem statement with measurable outcome — drafted above
- [ ] Baseline recorded — 26 open across 2 ledgers at first run
- [ ] Risk tier assigned with reasoning recorded — proposed above, **pending review**
- [ ] Named accountable owner, confirmed — Owner
- [ ] Documented failure mode: what wrong looks like, who notices
- [ ] User documentation published, states limitations — `README.md`, `LEDGER-SPEC.md`
- [ ] Admin docs updated: how to stop it, how to roll back, who to call
- [ ] Change record raised per the repo lifecycle — CATALOG row
- [ ] System owner signs off — Owner

**Documented failure mode.** The characteristic failure is a **silently incomplete
rollup**: a ledger drifts from the format, the collector skips the malformed items,
and the rollup looks complete while missing work. Detection: `check_ledger.py` run
after every write, plus the collector reporting each ledger's `updated` date so a
scope that has not been reconciled is visible. Who notices: the user, on the next
`open-items-status --all`, if the ledger count or the scope list looks wrong.

The second failure is **capture failure** — `log-item` and `end-of-session` are not
run, so the ledger is stale. Nothing detects this beyond the `updated` date. It is
accepted as the cost of a system with no sensors.

---

## Graduation triggers

Re-tier and reconsider the design when any of these occurs:

1. **A second person writes to any ledger.** Two writers on one Markdown file
   produces merge conflicts, and merge conflicts in a task list lose items. At that
   point: add per-item `owner`, and move cross-person items to a real tracker.
2. **A client engagement gets a ledger.** Then the question of where client work
   lives supersedes this design, and the ledger goes wherever that is — likely a
   per-client repo, not a personal vault.
3. **Any item becomes something a third party relies on.** That is Tier 1 at
   minimum under Governance `01` and needs a named accountable human per item.
4. **More than roughly 40 open items in one scope.** Deduplication matching becomes
   unreliable and the scope probably wants splitting.
5. **A ledger not under version control holds items that matter.** Sweeping deletes
   them with no recovery path.

---

## Deferred, deliberately

| Deferred | Revisit when |
| --- | --- |
| Scheduled collector run (`launchd` / cron) | On-demand runs prove insufficient — that is, you go days without running one |
| `install-schedule.sh` | Same |
| n8n or similar runner | This is the third or fourth local automation, not the first |
| HTML or artifact renderer | The Markdown rollup proves too dense to scan |
| Staleness flags on items | The open list gets unmanageable |
| `blocked` / `resume` fields | Items prove hard to pick back up, or the "waiting on me" view is missed |

## Change Log

| Change Made By | Change Proposed | Why | Date |
| --- | --- | --- | --- |
| Owner | Initial draft | Establish the skill's spec and tier | 2026-08-25 |
