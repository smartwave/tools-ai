---
title: "Governance layer — Spec"
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

# Governance layer (formerly ai-org-management) — Spec

> Written at intake (2026-08-25), after the tool was built; updated the same
> day when the layer was consolidated from `projects/ai-org-management/` into
> the repo root. The tier and mode below are Claude's analysis per the
> Governance 01 question flow, not a decision — review before relying on them.

## Problem and outcome

**What's broken or missing:** Governance rules that live only as wiki prose
can't be enforced or acted on by agents. Values drift between documents, cloud
tags, repo topics, and inventories, and there is no single answer to "what are
the allowed values, what rules apply at this tier, and does this asset exist?"

**Outcome when this works:** One machine-readable home for the controlled
vocabulary, manifest schema, tier→controls matrix, gates, asset registry, and
tag projections — with CI able to verify conformance and a one-way sync
keeping the wiki prose consistent. Agents act on the rules instead of
paraphrasing them. Baseline: rules exist as prose only; conformance is manual.

## Audience and mode

- **Who uses it:** shared — generic (placeholder) edition, adoptable for day
  job or clients once `{{...}}` tokens are substituted. Its five skills
  (classify-workload, mint-asset-id, author-manifest, project-tags,
  confluence-projection) live in the shared `skills/` folder and are covered
  by this spec; they operate on this layer's data and are meaningless without
  it.
- **Mode:** process automation once adopted — builders, agents, and CI depend
  on its values and rules.

## Risk tier

- **Tier:** 1 (proposed — Claude's analysis) per
  `AI-Program/02-Governance/01-AI-Risk-Tiering.md`.
- **Why:** Q1 no — the skills propose (mint, author, project) and the CI
  checks report; nothing changes data without a person committing it. Q2 no —
  its outputs are internal governance data, not external or person-affecting
  decisions. Q3 yes — colleagues and agents rely on the registry, vocabulary,
  and policy data as work product → Tier 1.
- **Why it might deserve Tier 2 treatment anyway (analysis):** once CI
  conformance checks *gate* other teams' deployments, an error here blocks or
  wrongly passes work at scale. If adopted org-wide, consider running it under
  Tier 2 discipline (registration, documented review of rule changes) even
  though the question flow lands at Tier 1.
- **Oversight:** rule and registry changes land via reviewed commits
  (CODEOWNERS in the reference configuration); the wiki remains the
  ratification surface for prose.

## Data and access

- **Data it reads:** its own YAML/JSON rule files; wiki pages (one-way sync
  reference). No personal or regulated data by design.
- **Data it writes or actions it takes:** registry rows, manifests, tag/topic
  projections — all as proposed changes a human commits. Asset IDs are
  immutable once minted, so minting deserves care.
- **Credentials/permissions needed:** repo write via normal PR flow; wiki read
  (sync pull); CI runner. The conformance checks are implemented (see
  [`ci/README.md`](ci/README.md)), run offline, and need no credentials of
  their own: GitHub topics and AWS tags are supplied as files rather than
  queried.
- **Enforcement posture:** only `[REF Bx]` rules fail a build. `[REF insert]`
  rules are warn-only until the adopter sets `enforce_pending_insert`, and an
  unconfigured clone reports "not configured" instead of failing.

## Definition of done

Not yet checked against `AI-Program/02-Governance/06-Definition-of-Done-AI.md`
for its tier:

- [ ] DoD review for Tier 1 — pending
- [x] Rules-as-data enforced mechanically: `ci/run-all` covers manifest,
      registry, projections, tier controls, Gate 1, pre-flight, and evaluation,
      with a fixture suite (`ci/tests/run`) that asserts a failing case per rule

## Graduation trigger

CI checks becoming a hard gate other teams' deployments depend on, or any
skill gaining an auto-write path to the registry, wiki, or cloud tags without
per-change human commit → re-tier per Governance 01 (likely Tier 2; auto-write
→ Tier 3 controls).

## Consolidation note (2026-08-25)

This layer's "tool folder" is the repo root: `GOVERNANCE.md` is its README,
this file is its SPEC, and its directories sit beside the catalog and type
folders. One consequence to be aware of: `.github/` (CODEOWNERS and the
confluence-sync workflow) and `CHANGELOG.md` now apply to the **whole**
tools-ai repo, not just the governance files — their path rules
(`/policy/`, `/vocabulary/`, `/confluence/pages/*`) still target only
governance paths, but anything added at those paths inherits them.

## Alignment watch-item

The root `policy/*` rules-as-data parallel the AI-Program 02-Governance set but
are not generated from it; the provenance tags (`[REF Bx]`, `[REC]`,
`[PROPOSED]`) mark what was enforceable vs. proposed in the source
configuration. Reconcile deliberately when either side changes — see
`TOOLKIT.md` at the repo root.
