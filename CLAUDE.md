# CLAUDE.md — how an agent reads and uses this repo

This repository is two things in one: the **tool catalog and built outputs**
(`CATALOG.md` plus the type folders — see `README.md`), and the
**machine-readable source of truth** for {{ORG_NAME}}'s non-product AI
governance, which lives at the repo root (formerly the standalone
`ai-org-management` repo; front door: `GOVERNANCE.md`). If you are an agent
driving AI solution work, read this file first, then load only the files you
need.

## The one rule

**This repo owns values and rules; Confluence owns prose and intent.** Never
restate a controlled value or a normative rule in a second place — reference it.
When you need the *reasoning* behind a control, read the Confluence standard
(page `{{PAGE_ID_AI_STANDARDS}}`). When you need the *value or rule* to act on,
read the file here. If they conflict, values/rules win here, prose/intent wins
there — and the conflict is a bug to be reported, not resolved silently.

## Provenance tags

Files in `policy/` tag every rule with its source:

- `[REF Bx]` — a Required Control in the live standard v{{AI_STANDARD_VERSION}}.
  Enforceable now.
- `[REC]` — a Recommended Pattern (SHOULD/MAY). Guidance, not a gate.
- `[REF insert]` — from the **pending** {{AI_STANDARD_PENDING_VERSION}}
  naming/tagging insert. **Do not enforce** until that insert is ratified in
  Confluence.
- `[PROPOSED]` — inferred, unconfirmed. Do not enforce; surface for review.

## What to load for common tasks

| Task | Read | Then |
|------|------|------|
| Find or track a built tool | `CATALOG.md` | the catalog is the front door — a tool not in it doesn't exist |
| Classify a new workload (type/shape/tier) | `vocabulary/vocabulary.yaml`, `policy/tier-controls.yaml` | apply modifiers before reading the tier row |
| Know what a tier requires | `policy/tier-controls.yaml` | check `oversight_rules`, `modifiers`, `invariants` |
| Mint an asset ID | `registry/registry.yaml`, `vocabulary/vocabulary.yaml` (`asset_id`) | never reuse an ID; append, don't rewrite |
| Author a manifest | `schemas/manifest.schema.json`, `examples/manifest.example.yaml` | validate before writing |
| Generate tags/topics | `projections/tag-map.yaml` | keep sensitive fields out of public topics |
| Update Confluence | `confluence/sync-map.yaml`, `confluence/inserts/ai-solution-standards.md`, `confluence/inserts/agentic-sdlc-platform.md`, `confluence/pages/ai-solution-standards.md`, `confluence/pages/agentic-sdlc-platform.md` | **draft only** — see below |

## Hard stops (never violate; see `policy/tier-controls.yaml` → `invariants`)

- An `app` MUST NOT depend on another `app`.
- `track: local` is Tier 1 only.
- A rules-based, pre-mappable step MUST be a fixed workflow, never a
  self-directing agent.
- Choosing an agent raises the solution to at least Tier 2.
- Multi-agent MUST NOT be built for non-product work without Engineering **and**
  Security involvement.
- Secrets MUST live in an approved store/keychain — never in code, prompts,
  Drive, a Claude Project, or a repo.

## Confluence writes are human-gated

Publishing to Confluence is an outward action. Regenerate an insert into
`confluence/inserts/` as a **draft** and stop. Do not update a live page without
explicit human approval. The Agentic SDLC page (`{{PAGE_ID_AGENTIC_SDLC}}`,
source `confluence/pages/agentic-sdlc-platform.md`) is owned by the
{{PLATFORM_SECURITY_LEAD_ROLE}} and needs that owner's sign-off before any edit
lands.

## Configuration

Every double-brace placeholder in this repo must be substituted with a real
value before the rules can be enforced. The full list, with meanings and the
files that must change, is the **Configuration** table in
[GOVERNANCE.md](GOVERNANCE.md), with the toolkit-wide index in
[PLACEHOLDERS.md](PLACEHOLDERS.md).

## Open items

Unfinished work is **not** tracked in this repo. It lives in the tracker folder,
`~/Documents/Claude/Claude Task Tracker`, one file per project — see the
`open-items` skill in `plugins/personal-assistant/`.

- Format contract:
  `plugins/personal-assistant/skills/open-items/LEDGER-SPEC.md`. Read it
  before writing.
- Commands: `log-item`, `end-of-session`, `open-items-status`.
- List what is open (quote the path — it contains spaces):
  `python3 "plugins/personal-assistant/skills/open-items/status.py" --items`
- Validate after any write:
  `python3 "plugins/personal-assistant/skills/open-items/check_ledger.py"`
- Never write a tracker file anywhere but that folder. If it is unreachable, say
  so and stop — do not fall back to the working directory.
- Closing an item deletes its line. Print the line in full first; nothing else
  will record it.
