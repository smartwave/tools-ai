---
title: "ai-solution-builder — Spec"
type: spec
set: tools
status: built
audience: owner
updated: 2026-08-25
tags:
  - ai-tools
  - spec
  - governance
---

# ai-solution-builder — Spec

> Written at intake (2026-08-25), after the tool was built. The tier and mode
> below are Claude's analysis per the Governance 01 question flow, not a
> decision — review before relying on them.

## Problem and outcome

**What's broken or missing:** Getting an AI solution from idea to approved
deployment requires a consistent set of documents and gates (requirements, risk
tier, design with tests, build evidence, tracked work). Without guidance,
builders — especially non-engineers — skip them or write them inconsistently,
and the governance standard exists only as prose nobody follows in practice.

**Outcome when this works:** Every AI solution reaches Gate 1 with a
review-ready requirements document and proposed tier, and reaches deployment
with a design, authored tests, an evidence spec, and a work-tracker Epic — 
without the builder needing to know the standard by heart. Baseline: today this
happens ad hoc or not at all.

## Audience and mode

- **Who uses it:** shared — generic (placeholder) edition, adoptable for day
  job or clients once `{{...}}` tokens are substituted.
- **Mode:** process automation once adopted — its documents feed an org review
  process other people depend on. Every output is a draft the requester
  reviews and places; nothing is published or created without explicit
  approval.

## Risk tier

- **Tier:** 1 (proposed — Claude's analysis) per
  `AI-Program/02-Governance/01-AI-Risk-Tiering.md`.
- **Why:** Q1 no — it never acts without per-item approval (work-tracker
  issues are created only on explicit per-issue confirmation). Q2 no — outputs
  are internal governance documents, not external or person-affecting
  decisions. Q3 yes — colleagues rely on the documents as work product, and a
  named requester is accountable for each → Tier 1.
- **Oversight:** human reviews every output; human approves every
  work-tracker action before it runs.

## Data and access

- **Data it reads:** the requester's own input; the bundled `references/`
  standard and templates; org policy pages on the wiki (reference
  configuration: Confluence). The POC skill explicitly keeps work off
  sensitive data.
- **Data it writes or actions it takes:** draft documents handed back to the
  requester; work-tracker issues only on per-issue approval. Nothing
  irreversible without a human choosing it.
- **Credentials/permissions needed:** wiki read; work-tracker create-issue
  (only if the ai-work-planner skill is used). Least privilege: no write
  access to the wiki, no admin scopes.

## Definition of done

Not yet checked against `AI-Program/02-Governance/06-Definition-of-Done-AI.md`
for its tier. The artifact was built and generalized before intake into this
repo; run the DoD pass and record results here:

- [ ] DoD review for Tier 1 — pending

## Graduation trigger

If its documents start going to customers, auditors, or regulators unedited,
or it processes regulated/customer-confidential data → Tier 2. If work-tracker
creation ever runs without per-issue approval → Tier 3 controls apply.

## Alignment watch-item

`references/deployment-standard.md` and `references/ai-use-framework.md` are
bundled policy documents, separate from the AI-Program 00–06 set. When either
side changes, reconcile deliberately — see `TOOLKIT.md` at the repo root.
