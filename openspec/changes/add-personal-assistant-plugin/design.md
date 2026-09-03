# Design: Add the Personal Assistant Plugin (Open Items Ledger)

## Technical Approach

Five components inside one skill, plus the plugin and marketplace packaging around
them. Data flows one direction only.

```
OPEN-ITEMS.md (per scope)
        │
        │  read
        ▼
    ledger.py  ──── imported by ──── check_ledger.py  ── CI, and after every write
        │
        │  imported by
        ▼
    collect.py  ──── writes ────►  rollup.md + rollup.json
        │                                    │
        │                                    └──►  extra copies (e.g. the vault)
        └── reads ~/.open-items/config.yaml
```

Nothing writes backwards. The skill writes ledgers; the collector reads them; the
rollup is a rendering payload regenerated from scratch each run.

| Component | Language | Runs |
| --- | --- | --- |
| `SKILL.md` | Markdown instructions | Claude Code, Cowork |
| `LEDGER-SPEC.md` | Markdown contract | Read on demand |
| `ledger.py` | Python, stdlib only | Imported |
| `check_ledger.py` | Python, stdlib only | Locally and in CI |
| `collect.py` | Python + pyyaml | Locally |
| `config.yaml` | YAML | `~/.open-items/` |
| `plugin.json` | JSON | Read by Claude at install |
| `marketplace.json` | JSON | Read by `/plugin marketplace add` |

## Architecture Decisions

### Decision: Markdown as the only source of truth, no sidecar JSON

A machine-readable sidecar alongside each ledger would make parsing trivial, but two
files representing the same items will drift, and the user will end up trusting
neither. Instead the Markdown grammar is made strict enough to parse reliably, and
the validator is promoted to a first-phase deliverable rather than a nice-to-have.

The cost is real: a stray separator character in item text silently splits the item
into a fake field without producing a parse error. That specific corruption is
detected by a heuristic — a path field containing spaces is almost certainly
misread text — rather than being preventable.

### Decision: Discovery by filesystem scan, not a registry file

An earlier design had a `LEDGERS.yaml` registering every ledger path. It was
discarded because it would need updating from Claude Code sessions, Cowork sessions
and manual work — three writers, no owner, and a silent failure mode where a new
ledger is created, never registered, and quietly absent from every rollup.

The filename is the registration. Every ledger already self-describes through its
frontmatter, so the registry's only unique data was location, which the filesystem
answers better. What remains is a config file holding scan roots, which changes when
a new *category* of location appears — perhaps twice a year — not when a project
starts.

The trade-off accepted: nothing prevents two ledgers claiming the same prefix. This
is handled by detection at scan time rather than prevention, on the grounds that the
fix takes ten seconds and nothing is corrupted in the meantime.

### Decision: The collector is a script, not an agent operation

Walking directories, parsing, merging and sorting are fully specified. Implementing
them as a plain script means the rollup costs nothing to produce, can be scheduled
without an API call, is identical on every run, and cannot paraphrase or omit an
item. The model is reserved for the two genuinely non-deterministic judgments: is
this item done, and does this new item duplicate an existing one.

### Decision: Bullet list with inline fields, not a table

A Markdown table cannot hold a sentence-length item without becoming unreadable, and
it diffs badly — one edit rewrites the whole row. A one-line bullet renders in
Obsidian with a working checkbox, diffs one line at a time, and parses with a single
regular expression.

### Decision: Prefixed, never-reused IDs from the start

`TAI-0007` and `AIP-0007` can coexist and two ledgers can be merged by
concatenation. Adding scoping later would require renumbering every item and
breaking every reference. This costs nothing now and is expensive to retrofit.

### Decision: No archive file; git history is the archive

Closed items are deleted after 7 days. Where the scope is under version control, any
swept item is recoverable from a commit, and the commit carries an author and
timestamp — which is the sign-off evidence a checkbox alone cannot provide. Where a
scope is not under version control, swept items are genuinely gone; that is noted as
a limitation rather than solved.

### Decision: Ledgers live next to the work, one per scope

Co-location makes the path field a relative path, puts ledger edits into the same
version history as the work, and lets an agent close an item without crossing a
folder boundary. One ledger per scope also means one writer at a time, so no
coordination or locking is needed. Scatter across many ledgers is the cost, and the
collector is what pays it.

### Decision: Rollup runs locally, never in CI

A hosted runner receives a clone of one repository. It cannot see the vault, other
repositories, or Cowork folders, so it can never produce a cross-scope view. CI
validates format only. This is a structural limit, not an implementation gap.

### Decision: A plugin is the packaging unit, and it is a container

The alternative was `skills/open-items/` at the repo root, alongside the five
governance skills. Rejected on two grounds. The root `skills/` folder is documented
in `skills/README.md` as the governance skill set covered by `GOVERNANCE-SPEC.md`,
and a personal productivity skill sitting in it is a scope violation of that folder's
own guard. And a plugin is what Claude installs — one `/plugin install` gets the
skill, its scripts, its templates and its spec together, where a loose skill folder
needs a copy step per surface.

The plugin is named for the category, not the skill. `personal-assistant` holding
`open-items` today can hold a second personal skill tomorrow without a rename, a
version discontinuity, or a second marketplace entry. The cost is one directory of
indirection while there is only one skill in it.

This plugin also sits **outside the placeholder edition**. `ai-solution-builder` and
`grc-core` use `{{ORG_NAME}}` because they are org tooling meant to be adopted;
this one is personal, its author is a person, and substituting a placeholder into it
would imply an org ownership that does not exist. The exception is stated in the
plugin README rather than left to be inferred.

### Decision: The skill folder is self-contained, and that outranks convenience

Sharing here is partly by hand: the skill folder gets copied into someone else's
`~/.claude/skills`, or duplicated as the base for a variant. So `skills/open-items/`
must be functional with nothing else present — every path it needs resolves relative
to `SKILL.md`, or comes from user config that has a documented default.

Concretely this forbids three otherwise-reasonable things: shared Python in a plugin
`lib/`, a `references/` folder at the plugin root serving multiple skills (which
`ai-solution-builder` does use), and any path in `SKILL.md` written relative to the
repo. `ledger.py` is duplicated into the skill folder rather than shared, and if a
second skill ever needs it, it gets its own copy. Duplication is the price of the
export path, and it is small.

The rule is testable, so it is a spec requirement and a verification step, not an
aspiration: copy the folder to an empty directory and the validator must still run.

### Decision: One marketplace index in this repo, listing all three plugins

The install path is `/plugin marketplace add smartwave/tools-ai`, which reads
`.claude-plugin/marketplace.json` at the repo root. That file is repo-scoped, not
plugin-scoped, so introducing it for `personal-assistant` decides distribution for
the two existing plugins too. Listing all three is the choice: they are built, they
are in `plugins/`, and omitting them means a second index later in a second repo.

The consequence to hold: three entries now duplicate `name` and `version` from three
`plugin.json` files, and nothing checks that they agree. The delta spec makes the
match a requirement and the DoD makes it a manual check. A linter belongs to
`projects/claude-config-store/`, which already specs one; it is deferred here rather
than built twice.

The repo is private, so installation needs git credentials for it. That is a README
note, not a design problem — but it does mean the marketplace path works for the
owner and for granted collaborators, and the hand-copy path is what serves everyone
else. Both paths are supported deliberately.

## Data Flow

**Writing.** User instruction → skill reads `LEDGER-SPEC.md` → skill reads the
ledger → deduplication check against open items → write → validate → confirm.

**Reading.** `collect.py` → load config → scan roots for `OPEN-ITEMS.md` →
`ledger.parse_ledger` per file → merge → sort → render Markdown and JSON → write to
output directory and any extra paths.

**Installing.** `/plugin marketplace add smartwave/tools-ai` → Claude reads
`.claude-plugin/marketplace.json` → `/plugin install personal-assistant@tools-ai`
→ Claude reads `plugins/personal-assistant/.claude-plugin/plugin.json` and loads
every skill under the plugin's `skills/`.

## File Changes

New, under `plugins/personal-assistant/`:

- `.claude-plugin/plugin.json`
- `README.md`, `SPEC.md`, `CHANGELOG.md`
- `skills/open-items/SKILL.md`
- `skills/open-items/LEDGER-SPEC.md`
- `skills/open-items/ledger.py`, `check_ledger.py`, `collect.py`
- `skills/open-items/templates/open-items-template.md`
- `skills/open-items/templates/config.yaml`

New at the repo root:

- `.claude-plugin/marketplace.json`

Elsewhere:

- `CATALOG.md` — one row plus a dated intake paragraph, per the repo lifecycle
- `OPEN-ITEMS.md` at the root of each scope
- `~/.open-items/config.yaml`
- `.github/workflows/check-ledger.yml` per repository holding a ledger
- `CLAUDE.md` — an open-items block per repository

`SPEC.md` absorbs `reference/TIER-AND-DOD.md`; there is no separate tier file in the
built plugin, because `_templates/tool-SPEC-template.md` already has the sections.

## Reference Implementation

`reference/` in this change folder holds a tested implementation of every component,
plus two ledgers seeded from real unfinished work. It has been run: the seeded
ledgers validate clean, the collector merges them, and a deliberately malformed
ledger produces fifteen specific errors.

**The specs are the contract; the reference is one implementation of them.** Use it
as a starting point rather than rebuilding from scratch, but where the two disagree,
the specs win and the reference is wrong.

Three things in `reference/` are known to predate the plugin decision and must be
adapted rather than copied verbatim: `INTEGRATION-SNIPPETS.md` writes paths as
`skills/open-items/`, `TIER-AND-DOD.md` is a standalone file rather than the
`SPEC.md` sections this repo uses, and `check_ledger.py` exits 1 when a `--root`
scan finds no ledger — which turns a repo holding the skill and no ledger yet into a
red CI run. An empty scan is not a failure under the rollup delta spec's
non-zero-on-failure wording, so the built copy exits 0 with a notice.
