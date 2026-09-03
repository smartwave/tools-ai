---
title: "AI Tools Catalog"
type: catalog
set: tools
status: active
audience: owner
updated: 2026-09-02
tags:
  - ai-tools
  - catalog
---

# AI Tools Catalog

One row per tool. A tool that isn't in this table doesn't exist yet as far as the repo is concerned.

**Column values are seeded from the original `AI Tools.md` idea list (now in `_archive/AI Tools - GitHub/`). The Type, Audience, and Tier values are Claude's analysis — first-pass guesses for you to correct, not decisions.** Tier references `AI-Program/02-Governance/01-AI-Risk-Tiering.md`; the working assumption was: human-in-the-loop personal tools = Tier 1, anything that runs unattended, touches money, or that other people depend on = Tier 2. Nothing here looked like Tier 3.

**Status legend:** `idea → spec → building → built → retired`. When a tool reaches `built`, fill in Location.

| Tool | Type | Category | Audience | Status | Tier | Location |
| --- | --- | --- | --- | --- | --- | --- |
| Prepping for a new job | project | Methodology | personal | idea | 1 | — |
| Tiers for AI Solution Governance | — | Methodology | shared | built | — | Done as `AI-Program/02-Governance/01-AI-Risk-Tiering.md` |
| Coaching myself | skill | Coaching | personal | idea | 1 | — |
| 30/60/90 a day gameplan | project | Coaching | personal | idea | 1 | — |
| Communication Coach | skill | Coaching | personal | idea | 1 | — |
| Aligning to my principles | prompt | Coaching | personal | idea | 1 | — |
| Setting up a GitHub Repo | skill | Code | shared | idea | 1 | — |
| Build repo | skill | Code | shared | idea | 1 | — |
| Setup Proper Workflows/Actions | skill | Code | shared | idea | 2 | — |
| Daily Digest / Day Prep | skill | Personal Comms | personal | idea | 1 | — |
| Weekly Prep | skill | Personal Comms | personal | idea | 1 | — |
| Calendar Planning | skill | Personal Comms | personal | idea | 1 | — |
| Convert Meeting Notes to Actions | skill | Personal Comms | personal | idea | 1 | — |
| Daily Look Back | skill | Personal Comms | personal | idea | 1 | — |
| Receipt Handler | agent | Personal Comms | personal | idea | 2 | — |
| Product "Brain" | project | Product | work | idea | 2 | Pattern already specced: `AI-Program/01-Framework-HCAMM/07_agentic-golden-repo-configuration.md` |
| Product Management | agent | Product | work | idea | 2 | — |
| Draft SLAs for Products/Services | skill | Product | work | idea | 1 | — |
| Monitor SLAs for Products and Services | agent | Product | work | idea | 2 | — |
| Pod/Agile Team Management | agent | Team Mgmt | work | idea | 2 | — |
| Weekly Status Updates & Re-Alignment | skill | Team Mgmt | work | idea | 1 | — |
| Monthly Status Updates & Re-Alignment | skill | Team Mgmt | work | idea | 1 | — |
| Updating Assets | agent | Technical Mgmt | work | idea | 2 | — |
| Tracking certificates | agent | Technical Mgmt | work | idea | 2 | — |
| Diagnosing organizational culture | prompt | Strategic | work | idea | 1 | — |
| Purpose instructions / charter | prompt | Strategic | personal | idea | 1 | — |
| Submitting expense receipts | skill | Budget/Financial | work | idea | 2 | — |
| ai-org-management (governance layer) | project | AI Governance | shared | built | 1 | repo root — `GOVERNANCE.md`, `policy/`, `vocabulary/`, `registry/`, `schemas/`, `projections/`, `confluence/`, `ci/`; skills in `skills/` |
| ai-solution-builder | plugin | AI Governance | shared | built | 1 | `plugins/ai-solution-builder/` |
| grc-core | plugin | GRC | shared | built | 2 | `plugins/grc-core/` |
| Org-wide Claude config store | project | AI Governance | shared | spec | 2 | `projects/claude-config-store/` |
| Gate recalibration (Standard amendment) | project | AI Governance | internal-only | spec | — | not in this repo — see the intake note below |
| personal-assistant | plugin | Personal | personal | spec | 0 (proposed) | `plugins/personal-assistant/` |

**Intake 2026-08-25 — org-wide Claude configuration store.** A reconstruction spec for the *golden repo* pattern — a private repo that acts as a Claude Code plugin marketplace and is the sole distribution point for org-approved plugins, skills, instructions, and MCP stubs — was imported to `projects/claude-config-store/`. Spec only: nothing is built. It is the buildable form of `AI-Program/01-Framework-HCAMM/07_agentic-golden-repo-configuration.md`, the same pattern the "Product 'Brain'" row points at. Tier 2 is Claude's analysis pending review — see its `SPEC.md`.

**Intake 2026-08-26 — gate recalibration.** A plan-only amendment to the Non-Product AI Deployment Standard: an exemption class for read-only data-acquisition tooling (Change A) and an advisory-gate posture for Tier 2/3 (Change B, split into B-write and B-docs). Eight open decisions block drafting; nothing in `policy/` or `ci/` anticipates it. **The plan itself is not in this repo.** It names real systems, real wiki pages, a real vendor and a specific production solution, so it was moved to an internal-only location on 2026-09-03 rather than published. Ask the repo owner for it.

**Intake 2026-08-26 — personal-assistant plugin (open-items).** A per-folder `OPEN-ITEMS.md` ledger of work started and not finished, packaged as this repo's third plugin. Three commands (`log-item`, `end-of-session`, `open-items-status`), a format validator that runs after every write and in CI, and a collector that discovers every ledger by filesystem scan and writes a cross-scope rollup. Nothing observes whether work is done — the user asserts it, and no item closes without confirmation; that limitation is what keeps it cheap. Named for the category, not the skill, so a second personal skill needs no rename. Delivered through `openspec/changes/add-personal-assistant-plugin/`. Tier 0 is Claude's analysis via the Governance `01` flow, pending review — see its `SPEC.md`, which also records the case for applying Tier 1 discipline anyway. This intake also made the repo an installable plugin marketplace: `.claude-plugin/marketplace.json` at the root now lists all three plugins.

**Intake 2026-08-29 — open-items moved to a single tracker folder (breaking).** The per-folder `OPEN-ITEMS.md` ledgers scattered across the filesystem with no way to see them together, and three components existed only to compensate: a collector, a config file of scan roots, and a cached rollup that could go stale without saying so. All tracker files now live in `~/Documents/Claude/Claude Task Tracker` as `OPEN-ITEMS <project>.md`, with `###` categories inside each file; discovery is a directory listing and a new `status.py` prints projects, categories and counts so choosing a destination is recognition rather than recall. A second correction came with it: the item text is a reminder that returns you to the right conversation, not an outcome statement that proves doneness. Breaking: closing an item now deletes its line — no Closed section, no sweep, no archive — and `collect.py`, the config file, `~/.open-items/` and the `--all` mode are gone along with the pyyaml dependency, leaving the skill stdlib-only. Plugin at `2.0.0`, renamed `personal-assistant` (directory included). Delivered through `openspec/changes/update-open-items-single-folder/`.

**Intake 2026-09-02 — ai-solution-builder Stage 0: problem framing before the POC.** An evaluation of the plugin's steps against the AI Use Framework found the pipeline started at "build a POC", so nothing captured the Framework's Define step or "invest in the input" before a prototype existed, POCs were framed as solutions, and the vibe-coded changes made while building vanished from the record. Stage 0 is now four steps: `ai-problem-framer` writes the one-page **Ultralight Problem Brief** (problem statement, validated root cause, process-level future state — by the person, in three gated phases with earlier sections read-only), `ai-poc-brief-author` turns it into a **POC Brief** with a paste-ready build prompt, `ai-poc-builder` builds and keeps a change log, and `ai-poc-summary-author` writes the **POC Summary** that opens the conversation with IT. Five Gemini Gem instruction sets in `plugins/ai-solution-builder/gems/` produce the same outputs for people on Gemini. Tier unchanged (1). Delivered through `openspec/changes/add-problem-framing-stage/`.

**Retired from the original list:** "Organizing context projects" (was crossed out in the source note).

**Why the Tier 2 guesses:** Setup Proper Workflows/Actions (CI others depend on), Receipt Handler and Submitting expense receipts (financial data), Monitor SLAs / Updating Assets / Tracking certificates (run unattended, others rely on results), Product Brain / Product Management / Pod Management (work processes other people depend on). Everything else assumed a human reviews each output before it's used — Tier 1. Correct freely.

**Intake 2026-08-25 — AI Governance Toolkit.** The last three rows are the generalized (placeholder-token) governance toolkit, imported already-built: the governance-as-code layer plus two Claude plugins. Their tiers were proposed using the Governance 01 question flow itself (not the shorthand above) and are Claude's analysis pending review; each carries a spec with the reasoning, an unchecked Definition-of-Done pass, and graduation triggers. Later the same day the governance layer was consolidated from `projects/ai-org-management/` into the **repo root** — its front door is `GOVERNANCE.md`, its spec `GOVERNANCE-SPEC.md`, and the toolkit overview and `PLACEHOLDERS.md` sit at the root (`TOOLKIT.md`).
