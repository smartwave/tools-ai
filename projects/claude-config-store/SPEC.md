---
title: "Org-Wide Claude Configuration Store — Spec"
type: spec
set: tools
status: spec
audience: owner
updated: 2026-08-25
tags:
  - ai-tools
  - spec
---

# Org-Wide Claude Configuration Store — Spec

The detailed buildout instructions live in [BUILDOUT-SPEC-claude-config-store.md](BUILDOUT-SPEC-claude-config-store.md). This file is the repo-standard spec: why it exists, what tier it is, and what "done" means.

## Problem and outcome

**What's broken or missing:** When an organization adopts Claude at scale, plugins, skills, and instruction files spread across individual laptops, Drive folders, and Claude Projects. There is no single approved source, no review before a skill reaches everyone, and no way to answer "what is my org actually running?" The pattern for fixing this is described in `AI-Program/01-Framework-HCAMM/07_agentic-golden-repo-configuration.md`, but there was no buildable spec in this repo — nothing anyone could hand to a Claude session and say "build this."

**Outcome when this works:** One private repo is the sole distribution point for org-approved Claude configuration. A user registers the marketplace once, installs plugins by name, and updates with one command. Every change to anything distributed is a PR with a named human approver and a green CI gate. The answer to "what is the org running, and who approved it?" is `git log`.

## Audience and mode

- **Who uses it:** shared — the spec is for anyone standing up this pattern; the resulting repo serves every Claude user in an adopting organization.
- **Mode:** **process automation.** Other people and systems depend on the output; the committed tree is production, installed directly by end users.

## Risk tier

- **Tier:** 2 per `AI-Program/02-Governance/01-AI-Risk-Tiering.md`
- **Why:** the blast radius is every Claude user in the org, and what is distributed is *executable configuration* — skills, hooks, and MCP stubs that run on other people's machines against other people's credentials. A bad merge propagates on the next plugin update. Nothing here touches money or makes irreversible external decisions, so it does not reach Tier 3.
- **Oversight:** human approves every write. Reads and searches are autonomous; every change to a distributed file requires a PR, a CODEOWNER review, and a merge performed by someone other than the author. No autonomous merge, ever.

## Data and access

- **Data it reads:** its own repository contents. Classification is Internal — no customer, personal, Confidential, or Restricted data in any file (a `.gitignore` blocking tabular formats and output folders enforces this structurally).
- **Data it writes or actions it takes:** the committed tree, which is installed by end users. Reversible by revert, but only after it has already propagated — hence the pre-merge gate.
- **Credentials/permissions needed:** repo write for maintainers; branch protection with required CODEOWNER review. MCP config stubs reference scoped least-privilege **service accounts** by named placeholder only — never personal or admin credentials, and never a real secret value in the tree.

## Definition of done

This spec is at status `spec`, not `built`. Before anything here moves to `built`, check it against `AI-Program/02-Governance/06-Definition-of-Done-AI.md` for Tier 2 and record which items applied:

- [ ] Tier assigned and reviewed — proposed Tier 2 above; not yet confirmed by a second reader.
- [ ] Oversight mode justified against `policy/tier-controls.yaml` → `oversight_rules`, not asserted from the buildout spec alone.
- [ ] Named owner and named approver for the resulting repo.
- [ ] Branch protection applied (required checks, CODEOWNER review, ≥1 approval).
- [ ] Reconstruction checklist in the buildout spec (§14) fully green.
- [ ] Rollback path documented and tested once (revert + confirm clients pick it up).

## Graduation trigger

Two directions to watch:

- **Upward:** if any distributed plugin gains write access to a production system, handles money, or acts without a human in the loop, that plugin — and the store's review posture around it — goes to Tier 3 and into the formal deployment lane. The buildout spec's rule that access-restricted tooling stays in its *own* gated plugin exists to keep that escalation contained to one artifact.
- **Into the catalog:** the moment this repo is actually instantiated, its outputs (the marketplace repo, individual plugins) become tools in their own right and need their own `CATALOG.md` rows.
