---
title: "AI Tools — Catalog, Built Outputs & Governance Layer"
type: index
set: tools
status: active
audience: owner
updated: 2026-08-25
tags:
  - ai-tools
  - index
---

# tools-ai

The **output side** of a two-part system. The requirements side — policies, standards, playbooks, and the human-centered automation framework — lives in the `AI-Program` folder (SmartWave vault). This repository holds three things: the **catalog** of AI tools worth building, the **built tools themselves** organized by what kind of output they are, and — since the 2026-08-25 consolidation — the **machine-readable governance layer** (formerly the standalone `ai-org-management` repo) at the repo root.

> **A starting draft, not compliance.** The governance layer, the bundled
> standards and frameworks, and the rules-as-data in `policy/` are internally
> coherent but **not ratified policy for your organization**, and nothing here is
> legal advice. Several bundled documents are explicitly drafts pending sign-off,
> and the Type/Audience/Tier values in `CATALOG.md` are first-pass analysis for a
> human to correct. The provenance tags in `policy/` (`[REF Bx]`, `[REC]`,
> `[REF insert]`, `[PROPOSED]`) show which rules were enforceable in the source
> configuration and which were still proposals — carry that distinction forward
> rather than adopting the set as binding. See `TOOLKIT.md` for the full note.

Tools here serve two audiences: things built for personal use, and things built to share with the day job. That split is tracked per-tool in the catalog (`Audience` column), not by folder.

## Structure

| Location | What goes there |
| --- | --- |
| `CATALOG.md` | The tracker: every tool idea and its type, audience, status, and risk tier. **The catalog is the front door — a tool that isn't in it doesn't exist.** |
| `plugins/` | Built plugins (e.g., Claude/Cowork plugins), one subfolder per plugin |
| `.claude-plugin/marketplace.json` | The marketplace index: this repo is an installable Claude plugin marketplace, listing every plugin in `plugins/` |
| `skills/` | Built skills, one subfolder per skill — includes the five governance skills that operate on this repo's rule files (see `skills/README.md`) |
| `agents/` | Built agents (autonomous or semi-autonomous workers), one subfolder per agent |
| `mcps/` | Built MCP servers and connectors (MCP = Model Context Protocol, the standard for giving AI tools access to systems), one subfolder each |
| `prompts/` | Reusable prompts and instruction sets that aren't full skills |
| `projects/` | Named collections that bundle several outputs toward one goal |
| `_templates/` | The README and SPEC every built tool starts from |
| `_archive/` | Retired items, plus the pre-restructure `AI Tools - GitHub` folder (its idea list became `CATALOG.md`) |

### Installing the plugins

This repo is a Claude plugin marketplace. From Claude Code:

```
/plugin marketplace add smartwave/tools-ai
/plugin install <plugin-name>@tools-ai
```

The index is `.claude-plugin/marketplace.json` and lists every plugin under
`plugins/`. Add a plugin there in the same change that adds the plugin — each
entry's `name` and `version` must match that plugin's `plugin.json`, and nothing
checks it for you. The repo is private, so installing needs git credentials for
it.

### Governance layer (at the repo root)

Merged in from the `ai-org-management` repo on 2026-08-25. `GOVERNANCE.md` is its front door; `CLAUDE.md` tells an agent how to use it; `GOVERNANCE-SPEC.md` is its spec.

| Location | What it owns |
| --- | --- |
| `vocabulary/` | Controlled values (types, shape, tier, track, oversight, data class, prefixes) |
| `schemas/` | The governance-manifest JSON Schema |
| `policy/` | Rules-as-data: tier→controls matrix, control catalog, gates |
| `registry/` | The asset-ID inventory |
| `projections/` | Manifest → AWS tags / GitHub topics mapping |
| `examples/` | A worked, validating manifest |
| `confluence/` | Prose-projection layer: page↔section sync map and paste-ready inserts |
| `ci/` | Enforcement: manifest, registry, projection, tier, gate, and evaluation checks |
| `assets/` | Per-asset governance evidence: pre-flight checklist, exceptions, evaluation set and results |
| `config/` | Adopter configuration for the checks (`governance.example.yaml`; the real one is git-ignored) |
| `TOOLKIT.md` + `PLACEHOLDERS.md` | Overview of the governance toolkit (this layer + the two plugins) and the placeholder-token index for adopting it |

## The lifecycle of a tool

1. **Idea** — add a row to `CATALOG.md` with status `idea`.
2. **Spec** — copy `_templates/tool-SPEC-template.md` into the tool's future folder; assign a risk tier per the AI-Program risk tiering standard. Status `spec`.
3. **Build** — work in the tool's subfolder under its type. Status `building`.
4. **Done** — check the AI-Program Definition of Done for its tier, fill in the tool's README, set status `built` and the catalog `Location`.
5. **Retired** — move the folder to `_archive/`, set status `retired`.

## Governing documents (in AI-Program)

- Risk tier before build: `02-Governance/01-AI-Risk-Tiering.md`
- Ship gate: `02-Governance/06-Definition-of-Done-AI.md`
- Personal/local tools lane: `01-Framework-HCAMM/05_local-automation-standard-non-engineer.md`
- Anything others depend on: `01-Framework-HCAMM/02_standard-deploying-automation-solutions.md`

Note the governance layer's `policy/` files are a parallel, machine-readable edition of governance rules — they are **not** generated from the AI-Program docs. When either side changes, reconcile deliberately (see `TOOLKIT.md`).

## Conventions

Tool subfolders use lowercase-with-hyphens names (`daily-digest`, not `Daily Digest`). Every built tool carries a `README.md` (what it is, how to run it) and a `SPEC.md` (why it exists, its tier, its done-checklist) from `_templates/`. The governance layer is the one exception: its "folder" is the repo root, so its pair is `GOVERNANCE.md` + `GOVERNANCE-SPEC.md`.
