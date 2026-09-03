---
title: "Governance Layer — Values and Rules"
type: index
set: tools
status: built
audience: owner
updated: 2026-08-25
tags:
  - ai-tools
  - governance
---

# Governance layer (formerly the `ai-org-management` repo)

> **Merge note (2026-08-25).** This was a standalone governance-as-code repo; it
> was consolidated into `tools-ai` at the repo root. Its directories
> (`vocabulary/`, `schemas/`, `policy/`, `registry/`, `projections/`,
> `examples/`, `confluence/`, `ci/`) now live beside the tool catalog, and its
> five skills live in the shared `skills/` folder. Relative paths below are
> unchanged. Spec: [`GOVERNANCE-SPEC.md`](GOVERNANCE-SPEC.md); agent
> instructions: [`CLAUDE.md`](CLAUDE.md).

The **canonical, machine-readable home** for {{ORG_NAME}}'s organization-wide AI
artifacts — the controlled values, schemas, rules, and inventory that builders
and agents must follow when deploying non-product AI solutions.

The **human-readable standard** lives in Confluence
(*{{ORG_NAME}} AI Solution Standards: Deploying AI Solutions*, page
`{{PAGE_ID_AI_STANDARDS}}`, and *The Agentic SDLC*, page
`{{PAGE_ID_AGENTIC_SDLC}}`). This repo and Confluence point at each other:

- **Confluence owns the prose** — the reasoning, the normative MUST/SHOULD
  requirements, the review and approval trail. It is the ratification surface.
- **This repo owns the values and rules** — the controlled vocabulary, the
  manifest schema, the tier→controls matrix, the projection rules, and the
  asset-ID registry, all machine-readable so an agent can act on them.

**When they disagree:** this repo governs *values and rules*; Confluence governs
*prose and intent*. One authoritative home per question.

## Layout

| Path | What it owns | Answers |
|------|--------------|---------|
| [`vocabulary/`](vocabulary/) | Controlled values (types, shape, tier, track, oversight, data class, prefixes) | "What are the allowed values?" |
| [`schemas/`](schemas/) | The governance-manifest JSON Schema | "What shape must a manifest take?" |
| [`policy/`](policy/) | Rules-as-data: tier→controls matrix, control catalog, gates | "What rules/gates/approvals apply?" |
| [`registry/`](registry/) | The `{{ASSET_ID_PREFIX}}*` asset inventory | "Does this asset exist, and where?" |
| [`projections/`](projections/) | Manifest → AWS tags / GitHub topics mapping | "How do fields become tags/topics?" |
| [`examples/`](examples/) | A worked, validating manifest | — |
| [`confluence/`](confluence/) | The prose-projection layer: page↔section sync map and paste-ready inserts | "Where does the prose live, and how is it generated?" |
| [`skills/`](skills/) | Shared skills folder; the five governance skills (classify, mint, author, project, confluence-projection) operate *on* this layer | "How does an agent act on the above?" |
| [`ci/`](ci/) | Enforcement: manifest, registry, projection, tier, gate, and evaluation checks | "Is a repo/asset actually compliant?" |
| [`assets/`](assets/) | Per-asset governance evidence (pre-flight, exceptions, evaluation) | "What has this asset actually satisfied?" |
| [`config/`](config/governance.example.yaml) | Adopter configuration for the checks | "What are this adopter's literal values?" |

## Scope

The **repository grammar** and the **four workload types** are domain-general:
they name all deployed workloads, AI or not. The **manifest overlay fields**
(`asset_id`, `tier`, `track`, `shape`, `oversight`, `data_class`) are
AI-governance-specific and apply to assets in scope of the Non-Product AI
Deployment Standard.

## The scheme in one screen

**Repositories**

```
<vendor>-org-management            # org-wide rules per vendor: aws-, snowflake-, aiven-  (and ai- for cross-vendor AI governance)
<domain>-<vendor>-<type>-<name>    # everything else; <type> and <name> optional
```

- `<domain>` — the owning business unit or functional area (`platform`, `data`,
  `finance`, `ops`, `legacy`, `dataops`, `ai`).
- `<vendor>` — the platform it targets or runs on (`aws`, `snowflake`, `aiven`,
  `claude`, `github`, `workato`).
- `<type>` — optional; one of `tool`, `platform`, `service`, `app`.
- `<name>` — optional; used **only with** a `<type>`.
- No invented abbreviations. Lowercase letters, numbers, hyphens.

**Workload type** (structural — *where a thing sits*): `tool` / `platform` →
`service` → `app`. **Shape** (behavioral — *how a thing decides*), orthogonal:
`workflow` / `agent` / `multi-agent`. Agentic behavior is metadata (`shape`),
never a repository type.

## How an asset uses this

1. **Mint an asset ID** in [`registry/registry.yaml`](registry/registry.yaml)
   when the asset comes in scope (Gate 1). Format
   `{{ASSET_ID_PREFIX}}<DOMAIN>-<SLUG>`, uppercase, immutable.
2. **Carry a manifest** ([`schemas/manifest.schema.json`](schemas/manifest.schema.json))
   in the asset — SKILL.md frontmatter, plugin manifest, or a `SOLUTION.md`.
   Tier 2+ MUST; Tier 1 SHOULD.
3. **Project the tags** per [`projections/tag-map.yaml`](projections/tag-map.yaml):
   `{{TAG_NAMESPACE}}:*` AWS tags on resources, `{{TAG_NAMESPACE}}-*` /
   `{{TAG_NAMESPACE}}-ai-*` topics on the repo, plus the
   `{{TAG_NAMESPACE}}-ai-governed` marker topic.
4. **One asset, two artifacts.** A deployed agent's authoring assets live under a
   `<domain>-claude-*` repo; its IaC lives under a `<domain>-aws-*` repo. Both
   carry the **same** `asset_id`.

## Configuration

This layer ships **placeholder-only**: every double-brace placeholder must be
replaced with a literal value before the rules validate and CI can pass. The
full token index for the whole toolkit is [`PLACEHOLDERS.md`](PLACEHOLDERS.md).
File paths named there and below predate the 2026-08-25 merge: the governance
repo's `README.md` is now this file (`GOVERNANCE.md`), and its `skills/README.md`
is now the merged [`skills/README.md`](skills/README.md).

The named integrations (Confluence, GitHub, AWS, Jira, Claude) are the
reference configuration — each is swappable for an equivalent platform, in
which case adjust the surrounding wording too.

**CI will fail until substituted.** The regex-bearing files
(`vocabulary/vocabulary.yaml` → `asset_id.pattern`,
`schemas/manifest.schema.json` → `asset_id.pattern`, `ci/check-registry`,
`ci/check-projections`, `projections/tag-map.yaml`, `registry/registry.yaml`,
`examples/manifest.example.yaml`) carry `{{ASSET_ID_PREFIX}}` /
`{{TAG_NAMESPACE}}` inside patterns and values, so no asset ID, tag, or topic
can match until literals replace them. The workflow
`.github/workflows/confluence-sync.yml` additionally needs its repo secrets and
variables set (listed in the comment at the top of that file).

## Enforcement

The rules in `policy/` are enforced by the checks in
[`ci/`](ci/README.md) — manifest schema and vocabulary, registry invariants,
tag/topic projections, the tier row, Gate 1, the B1.7 pre-flight gate, and the
evaluation set. They run locally (`ci/run-all`) and in
`.github/workflows/governance-checks.yml`, which calls the same scripts.

Configuration is an **either/or**: copy `config/governance.example.yaml` to
`config/governance.yaml` and keep the tree generic, *or* do the placeholder
find-and-replace described above. With neither, the checks report "not
configured" (exit 3) and `ci/run-all` still exits 0, so a generic clone stays
green. Only rules tagged `[REF Bx]` fail a build; `[REF insert]` rules stay
warn-only until `enforce_pending_insert` is set.

## Status

**Draft for review.** Values and rules here are proposed and not yet ratified;
the Confluence standard is the ratification surface. The `policy/` rules-as-data
files are reconciled against the live standard **v{{AI_STANDARD_VERSION}}**; rows
tagged `[REF insert]` depend on the pending naming/tagging control
({{AI_STANDARD_PENDING_VERSION}} draft) and must not be enforced until that
insert is ratified. See [CHANGELOG.md](CHANGELOG.md).
