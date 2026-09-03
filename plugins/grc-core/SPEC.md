---
title: "grc-core — Spec"
type: spec
set: tools
status: built
audience: owner
updated: 2026-08-25
tags:
  - ai-tools
  - spec
  - grc
---

# grc-core — Spec

> Written at intake (2026-08-25), after the tool was built. The tier and mode
> below are Claude's analysis per the Governance 01 question flow, not a
> decision — review before relying on them.

## Problem and outcome

**What's broken or missing:** Vendor security reviews and international-travel
work-request reviews are recurring, evidence-heavy, and inconsistent when done
ad hoc — facts go stale (sanctions, advisories, adequacy decisions), scoring
drifts from the policy's risk matrix, and outcomes aren't recorded uniformly.

**Outcome when this works:** Each review produces a cited, as-of-dated memo
with a recommended verdict on the sanctioned risk matrix, pinned to specific
policy versions, ready for a human decision — plus a gated, human-confirmed
write-back of the approved outcome. Baseline: manual reviews with variable
depth and citation.

## Audience and mode

- **Who uses it:** shared — generic (placeholder) edition for Security/GRC,
  adoptable for day job or clients once `{{...}}` tokens are substituted.
- **Mode:** process automation — reviewers and decision-makers depend on the
  output. Recommendations only; a human makes every determination.

## Risk tier

- **Tier:** 2 (proposed — Claude's analysis) per
  `AI-Program/02-Governance/01-AI-Risk-Tiering.md`.
- **Why:** Q1 no — the write-back skill proposes every change and executes
  only on explicit per-change confirmation, so no unapproved action. Q2 yes — 
  the travel skill informs decisions that materially affect a person's
  employment and access (whether they may work from a country), and vendor
  reviews inform engagement decisions → Tier 2.
- **Oversight:** human approves every action before it runs; verdicts are
  recommendations to a named human reviewer; unverifiable blocker-domain facts
  fail safe to "manual review required."

## Data and access

- **Data it reads:** compliance platform vendor records (read-only; Drata in
  the reference configuration), vendor trust centers, org policy pages, public
  sources (OFAC, State Department, EU adequacy, Freedom House, Citizen Lab,
  Amnesty Security Lab, Forbidden Stories). Data-minimization guardrail: no
  confidential customer names, contract values, or excess personal data.
- **Data it writes or actions it takes:** review memos and proposed inventory
  rows as drafts; compliance-platform updates only via the gated write-back
  skill, per-change confirmed. Its executing write path must stay disabled
  org-wide until the write capability is itself approved.
- **Credentials/permissions needed:** compliance platform read; write scope
  only for the write-back skill and only once approved. No email/send
  capability by design.

## Definition of done

Not yet checked against `AI-Program/02-Governance/06-Definition-of-Done-AI.md`
for its tier. Tier 2 items to evidence when adopted: inventory registration,
security risk review, documented human review, logging, documented failure
mode:

- [ ] DoD review for Tier 2 — pending

## Graduation trigger

Enabling the write path without per-change confirmation, auto-sending outcomes
to third parties, or scheduling unattended runs → Tier 3 controls (own
identity, blast-radius limits, kill switch, audit trail).

## Alignment watch-item

Skill logic is pinned to specific policy versions
(`{{TPRM_POLICY_VERSION}}`, `{{RISK_POLICY_VERSION}}`,
`{{TRAVEL_STANDARD_VERSION}}`). Re-version the skills when the policies
change — see `TOOLKIT.md` at the repo root.
