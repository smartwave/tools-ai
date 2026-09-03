---
title: "Org-Wide Claude Configuration Store"
type: project
set: tools
status: spec
audience: shared
updated: 2026-08-25
tags:
  - ai-tools
  - golden-repo
  - claude-config
---

# Org-Wide Claude Configuration Store

A **golden repo pattern**: a single private GitHub repository that acts as a Claude Code plugin marketplace and becomes the one distribution point for org-approved Claude configuration — plugins, skills, instruction files, and MCP config stubs — for every Claude user in an organization. The committed tree *is* production: clients install straight from it, so merging deploys and nothing rebuilds server-side.

This is the buildable form of the pattern described in `AI-Program/01-Framework-HCAMM/07_agentic-golden-repo-configuration.md`.

## Status

**spec** — Tier 2 — see [SPEC.md](SPEC.md) for the reasoning.

**Nothing is built yet.** This folder currently holds the spec only. There is no marketplace repo, no `marketplace.json`, no linters. The next step is a decision to instantiate, not a code change here.

## What's in this folder

| File | What it is |
| --- | --- |
| `BUILDOUT-SPEC-claude-config-store.md` | The reconstruction spec (v1.0, reverse-engineered from a production instance). Repo layout, agent constitution, marketplace index format, plugin anatomy, CI merge gates, CODEOWNERS, team scaffold, and a reconstruction checklist. |
| `SPEC.md` | This repo's standard tool spec: problem, audience, risk tier, data and access, definition of done, graduation trigger. |
| `README.md` | This file. |

## Placeholders

The buildout spec uses two kinds of placeholder, and they mean different things:

- `{{DOUBLE_BRACE}}` — controlled values, one find-and-replace each. `{{ORG_NAME}}` and `{{GITHUB_ORG}}` are the same tokens the rest of this repo uses (see [PLACEHOLDERS.md](../../PLACEHOLDERS.md)). `{{CONFIG_STORE_REPO}}` and `{{CONFIG_STORE_OWNER_EMAIL}}` are **local to this folder** and are deliberately not in the root index — nothing outside this project consumes them.
- `<angle-brackets>` — illustrative shapes (`<plugin-name>`, `<Team_Name>`, `<TICKET>`). Read them as examples; don't substitute them mechanically.

## Relationship to the governance layer

The spec's Agent Constitution (§3) and CI gates (§6) are a concrete instance of rules this repo already owns at its root: the hard stops in [CLAUDE.md](../../CLAUDE.md) and the tier→controls matrix in `policy/tier-controls.yaml`. When this pattern is instantiated, justify its HITL oversight mode against `policy/tier-controls.yaml` → `oversight_rules` rather than against the spec alone.

## Change log

- 2026-08-25 — created; buildout spec imported and generalized (angle-bracket controlled values converted to repo tokens, named-org instantiation notes replaced with a neutral example).
