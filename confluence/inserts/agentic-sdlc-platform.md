# Paste-ready insert — Standard & Configuration: The Agentic SDLC (Platform version) (Confluence page {{PAGE_ID_AGENTIC_SDLC}})

> **Placement:** add the subsection below to **Part B — The Configuration (the repository harness)**, after *"The agentic engineering repo (the `.claude/` harness)"* and before *"Pipeline stages and human gates."*
>
> **Header version:** update the document header `Version: {{AGENTIC_SDLC_VERSION}} (draft)` → `Version: {{AGENTIC_SDLC_PENDING_VERSION}} (draft)`.
>
> **Owner sign-off:** this page's Owner is `<{{PLATFORM_SECURITY_LEAD_ROLE}}>`, not the author of this change. The edit is drafted for that owner's review and sign-off; do not treat it as final on this page without it.
>
> **Style note:** written to match this document's register ([REF] = sourced to an external standard or an org convention already in use; [ANALYSIS] = synthesis to validate).
>
> *(Everything below the line is the paste-ready content.)*

---

**Repository naming and asset tagging.** The two-repository model above (Product Brain upstream, agentic engineering repo downstream) sits inside an org-wide naming grammar that is deliberately *not* AI-specific, so that an agentic workload and the conventional infrastructure around it are named by one scheme rather than two. **[REF — org convention]** Repositories take the form `<vendor>-org-management` for org-wide rules per vendor and `<domain>-<vendor>-<type>-<name>` for everything else, where `<domain>` is the owning business unit or functional area, `<vendor>` is the platform the code targets or runs on, and the optional `<type>` is one of four workload types classified by dependency position — `tool`, `platform`, `service`, `app`. The optional `<type>`/`<name>` slots let a complex codebase be split into typed repositories under one domain and vendor (`ops-aws-platform-networking`, `ops-aws-service-reporting`) rather than forcing a monorepo or an ad-hoc split. The behavioral character of a workload (its `shape`: workflow, agent, or multi-agent) is carried as metadata, not as a repository type; there is no `agent` repository type, which keeps "is this agentic?" a queryable tag rather than a naming guess. The canonical, machine-readable vocabulary, manifest schema, projection rules, and asset-ID registry live in `ai-org-management`; this document and the AI Solution Standards reference that source rather than restating its values.

The leverage this adds to the harness is attribution and inventory, both of which the framework already demands but does not yet operationalize. **[REF]** Each in-scope asset carries a governance manifest — the same authoritative record the AI Solution Standards requires — from which two projections are generated: `{{TAG_NAMESPACE}}:`-prefixed AWS resource tags on deployed resources, and `{{TAG_NAMESPACE}}-ai-governed` plus faceted `{{TAG_NAMESPACE}}-*` topics on source repositories. The manifest's enumeration of models, prompt versions, and MCP servers is the natural seed of the **AIBOM** the Build stage emits, and its stable `{{ASSET_ID_PREFIX}}*` identifier plus `owner` field give the per-agent **attribution** that M5 and the *Operate* stage require — the same identifier binds an agent's authoring assets (in an `ai-*` repository) to its deployed infrastructure (in a `<vendor>-*` repository), so "an agent did it" resolves to a specific, revocable, named asset rather than an anonymous process. **[ANALYSIS]** Because GitHub topics are public even on private repositories, environment, owner, and any sensitive value are confined to the manifest and AWS tags; only coarse, non-sensitive facets are projected as topics. Enforcement of tag validity is a control-plane concern, satisfied by AWS Organizations tag policies defined in `aws-org-management` — which is precisely the shared MCP/agent inventory substrate the Evaluation section flags as a missing prerequisite. Standing up the vocabulary, manifest schema, and registry in `ai-org-management`, and the tag policies in `aws-org-management`, is therefore load-bearing for the provenance, attribution, and observability controls in Part A, not a later convenience.

---

## Note for the Evaluation section (optional)

If you want the Evaluation's **gap #2** (no central shared-skills repo, MCP inventory, or agent-ops dashboard) to reflect this, a one-line addition to that item:

> *Update ({{AGENTIC_SDLC_PENDING_VERSION}} draft): the org-wide naming grammar and the `ai-org-management` manifest/registry now specify the inventory substrate this gap describes; the shared-skills repo and MCP inventory become named repositories under the grammar (`<domain>-claude-platform-skills`, `ai-org-management`) rather than undefined future work.*
