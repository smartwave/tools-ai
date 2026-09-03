---
title: "AI Governance Toolkit — Overview"
type: index
set: tools
status: built
audience: owner
updated: 2026-08-25
tags:
  - ai-tools
  - governance
  - toolkit
---

# AI Governance Toolkit

A vendor-neutral, organization-neutral edition of three connected artifacts for
governing non-product AI work: a governance-as-code layer, a builder-facing
plugin that walks a solution through the gates, and a GRC plugin for the two
review workflows that most often sit alongside it.

Every organization-specific value — company name, role titles, contacts, page
identifiers, project keys, tag namespaces, policy versions — is a double-brace
placeholder token. [`PLACEHOLDERS.md`](PLACEHOLDERS.md) is the complete index.

> **Location note (2026-08-25).** The toolkit was intaken into this repo and
> then consolidated: the governance-as-code layer (formerly the standalone
> `ai-org-management` repo) now lives at the **repo root** — front door
> [`GOVERNANCE.md`](GOVERNANCE.md), its five skills in
> [`skills/`](skills/README.md) — and the two plugins live under `plugins/`.

## What's here

| Artifact | Location | What it is |
|---|---|---|
| Governance layer | repo root — [`GOVERNANCE.md`](GOVERNANCE.md) | Governance-as-code: controlled vocabulary, manifest schema, tier→controls matrix, gates, asset registry, tag projections, CI conformance checks, and a one-way sync to the wiki where the human-readable standard lives. Machine-readable, so an agent can act on the rules rather than paraphrase them. |
| `ai-solution-builder` | [`plugins/ai-solution-builder/`](plugins/ai-solution-builder/) | Plugin: eight skills that carry an AI solution from a one-page problem brief (problem, root cause, future state — written by the person, guided by the AI), through a POC brief, a throwaway proof of concept with its change log, and a POC summary for IT, then the requirements document and Gate 1, the solution design and its authored tests, the build-evidence spec, and the work-tracker Epic. Bundles the deployment standard, methods, and templates as its source of truth, plus five Gemini Gem instruction sets producing the same Stage 0 outputs. |
| `grc-core` | [`plugins/grc-core/`](plugins/grc-core/) | Plugin: three skills — third-party/vendor security review, the gated write-back of an approved review outcome, and an international travel work-request risk review. Recommendations only; never approves, sends, or acts. |
| `personal-assistant` | [`plugins/personal-assistant/`](plugins/personal-assistant/) | Plugin: personal productivity skills, currently one — `open-items`, reminders of Claude work started and not finished, kept as one file per project in a single tracker folder with a validator and a status listing. Personal tooling: outside the placeholder edition, and not part of the governance toolkit. |

All three plugins install from this repo's marketplace index (`.claude-plugin/marketplace.json`): `/plugin marketplace add smartwave/tools-ai`, then `/plugin install <name>@tools-ai`.

The three governance artifacts are usable independently. Together, the governance layer holds the
rules, `ai-solution-builder` applies them to a solution being built, and
`grc-core` handles the adjacent vendor and travel reviews.

## Adopting

1. **Read [`PLACEHOLDERS.md`](PLACEHOLDERS.md)** and decide your values. Most
   are obvious; the CI-affecting ones (`{{ASSET_ID_PREFIX}}`,
   `{{TAG_NAMESPACE}}`, `{{DOC_ID_PREFIX}}`) are worth deciding deliberately
   because asset IDs are immutable once minted.
2. **Substitute.** One find-and-replace per token across the whole tree.
3. **Verify nothing is left**:
   ```bash
   grep -rno '{{[A-Z0-9_]*}}' . --exclude-dir=.git | sort -u
   ```
4. **Have your own owners ratify the policy content** before treating it as
   policy — see the caveat below.
5. **Wire up the integrations** you actually use. Note that
   `ci/check-registry` and `ci/check-projections` ship as stubs — they define
   the conformance contract but exit non-zero as unimplemented, so implementing
   them is part of adoption.

## The named integrations are a reference configuration

Confluence (wiki), Jira / Atlassian (work tracker), GitHub (repository host and
CI), Drata (compliance platform), and AWS (cloud) appear by name because the
skills need something concrete to talk to. None of them is required. Substitute
the equivalent product and the surrounding logic is unchanged — the connector
and MCP tool names in the skills are the real names in the reference
configuration, not a dependency of the governance model.

Public sources are left exactly as they are and need no configuration: NIST AI
RMF, OWASP, OFAC / US Treasury, US State Department travel advisories, EU
adequacy decisions, Freedom House, Citizen Lab, Amnesty Security Lab,
Forbidden Stories.

## Relationship to AI-Program (alignment watch-item)

The requirements side of this vault system lives in `AI-Program` (SmartWave
vault): the 00–06 governance set and the HCAMM framework.
`plugins/ai-solution-builder/references/deployment-standard.md` and
`references/ai-use-framework.md` are **their own bundled policy documents** —
they parallel the AI-Program set but are not generated from it. If the
AI-Program docs evolve (tier definitions, gates, definition of done), the
bundled references and the root `policy/` files do **not** update
automatically. Treat AI-Program as the thinking surface and this toolkit as
the shipped edition; reconcile deliberately when either side changes.

## Important caveat on the policy content

`plugins/ai-solution-builder/references/deployment-standard.md`,
`plugins/ai-solution-builder/references/ai-use-framework.md`, and the
rules-as-data in the root `policy/` folder carry a complete and internally
coherent control set. They are **a starting draft, not compliance**. They are
not ratified policy for your organization until your own security, legal, risk,
and privacy owners have reviewed and adopted them, and nothing here is legal
advice. The provenance tags in `policy/` (`[REF Bx]`, `[REC]`, `[REF insert]`,
`[PROPOSED]`) exist precisely so you can see which rules were enforceable in
the source configuration and which were still proposals — carry that discipline
forward rather than adopting the whole set as binding.

Similarly, the guardrail language throughout both plugins — recommendation not
decision, propose never auto-create, never fabricate evidence, reviewer ≠
builder, human-gated outward actions — is load-bearing. If you relax it, do so
knowingly.
