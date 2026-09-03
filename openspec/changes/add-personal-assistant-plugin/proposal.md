# Proposal: Add the Personal Assistant Plugin (Open Items Ledger)

## Intent

Work started in one session and not finished gets lost between sessions and between
surfaces. Chat threads end, Claude's memory is a synthesis rather than a record, and
open loops accumulate in the tails of dated session notes with no single place to
look.

Two questions need to be answerable in under a minute, from any surface:

1. Did I start something and not finish it?
2. Is it done now?

Baseline at time of writing: 26 unfinished items are scattered across two dated
session notes (`vault-restructure-2026-08-23.md`, `tools-ai-intake-2026-08-25.md`)
and the AI-Program README's open decisions. Some have been open since 2026-08-22
with no tracking beyond prose.

This change delivers that tracking as **`personal-assistant`**, the repo's third
plugin — a container for personal-productivity skills, whose first skill is
`open-items`. The container framing is deliberate: personal tooling accumulates,
and a plugin named for the one skill it happens to hold today would have to be
renamed the moment a second arrives.

## Scope

**In scope:**

- A plugin at `plugins/personal-assistant/`, following the shape already set by
  `plugins/ai-solution-builder/` and `plugins/grc-core/`.
- A `open-items` skill inside it: a per-folder `OPEN-ITEMS.md` ledger with a
  strict, machine-parseable format, and three commands — `log-item`,
  `end-of-session`, `open-items-status`.
- A validator that enforces the format contract.
- A collector that discovers every ledger by filesystem scan, merges the open items,
  and writes a rollup as Markdown and JSON.
- `.claude-plugin/marketplace.json` at the repo root, so plugins in this repo are
  installable from GitHub. The first marketplace index in this repo; it lists all
  three plugins.
- CI validation of ledger format, per repository.

**Out of scope — recorded so the scope does not creep:**

- Priority, effort estimates, due dates, assignees, or status fields. Anything with
  a real date or a second person belongs in a tracker, not here.
- Any write-back from a viewer to a ledger. Data flows one direction only.
- Any sensing of whether work is actually finished. The user asserts it.
- Multi-user support. Single writer per ledger.
- A second skill in the plugin. The container starts with one.
- A separate marketplace repository, and any marketplace linter. The index here is
  hand-maintained; automated linting belongs to `projects/claude-config-store/`,
  which specs it.
- A public release. The repo is private; distribution is the owner, the owner's
  machines, and people granted access.
- A scheduled collector run, an HTML renderer, and a Claude artifact viewer. All
  deferred; see Deferred Work below.

## Approach

**Ledgers live next to the work they track.** One `OPEN-ITEMS.md` per scope — a
repo, a vault subtree, a Cowork project folder. The `where` field becomes a relative
path, version history becomes the sign-off record, and the agent doing the work can
close an item without crossing a folder boundary.

**Discovery, not registration.** The collector finds ledgers by scanning for the
filename. There is no registry file, because a registry is a second thing to keep in
sync and its only data — where the ledgers are — is better answered by the
filesystem. The filename is the registration.

**Deterministic where possible.** Walking directories, parsing, merging and sorting
are fully specified operations, so they are plain Python with no model involved. The
model is used only for judgment: is this item done, and does this new item duplicate
an existing one. This makes the collector schedulable, free to run, and incapable of
inventing an item that does not exist.

**One direction.** Ledgers → collector → rollup. Nothing writes backwards. If
write-back is ever wanted, that is the signal to move to a real tracker rather than
extend this.

**Two distribution paths, one of which constrains the design.** The plugin installs
from GitHub through the marketplace index, and it is also copied by hand — cloned,
duplicated, or the skill folder lifted out on its own into someone else's
`~/.claude/skills`. The second path is the binding constraint: the skill folder must
be functional with nothing else present.

## Known limitation, accepted deliberately

**Nothing observes whether work is done.** There is no sensor, no integration, and
no captured session state. The agent may propose closing an item based on what it
observed in the session it is in; the user confirms. Work done outside a session is
invisible until the user says so.

This is accepted because it is what keeps the system cheap. Anything that *knows*
whether work is finished has to be wired into commits, pull requests and tickets —
which is the ticket system this exists to avoid.

## Deferred work

Recorded here so it is a decision rather than an omission.

| Deferred | Revisit when |
| --- | --- |
| Scheduled collector run (`launchd` / cron) | On-demand runs prove insufficient |
| HTML or Claude artifact renderer | The Markdown rollup proves too dense to scan |
| Staleness flags on items | The open list becomes unmanageable |
| `blocked` and `resume` fields | Items prove hard to pick back up, or the "waiting on me" view is missed |
| Per-item `owner`, multi-writer support | A second person writes to any ledger |
| A marketplace linter | The three entries drift from their `plugin.json` files once |

## Open decisions surfaced to the owner (do not decide)

The Tier 0 proposal in `reference/TIER-AND-DOD.md`, pending confirmation. The
tier-numbering discrepancy — Governance `01` uses 0–3, the repo vocabulary 1–3 —
already tracked as `TAI-0013`; this change does not resolve it. Whether the 26
seeded items are all still open; the first `end-of-session` run is the review pass.
