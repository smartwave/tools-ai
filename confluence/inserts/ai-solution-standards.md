# Paste-ready insert — AI Solution Standards (Confluence page {{PAGE_ID_AI_STANDARDS}})

> **Placement:** add the control below to **Standards (Required Controls) → Technical Controls**, immediately after **Version numbering** (both are asset-identity controls). It is written unnumbered to match its sibling Technical Controls; if you prefer a control number, it slots as **B1.10**.
>
> **Reference model:** this control *references* the canonical vocabulary in `ai-org-management`; it does not restate the values. Prose lives here; values live there.
>
> **SemVer:** this is a backward-compatible addition of scope → **MINOR** bump, **{{AI_STANDARD_VERSION}} → {{AI_STANDARD_PENDING_VERSION}}**. Changelog row provided at the end.
>
> *(Everything below the line is the paste-ready content.)*

---

* **Naming, tagging & inventory:** Every in-scope solution and its governed records **MUST** be identifiable and discoverable through a consistent name, a governance manifest, and projected tags. The controlled values for every field below are defined once, in the machine-readable vocabulary maintained in `ai-org-management`; this control sets the requirement, that vocabulary sets the values, and the two **MUST NOT** diverge.

    * **Repository naming.** Repositories follow `<vendor>-org-management` for org-wide rules per vendor (e.g. `aws-org-management`; `ai-org-management` for cross-vendor AI governance) and `<domain>-<vendor>-<type>-<name>` for everything else, where `<type>` and `<name>` are optional. `<domain>` is the owning business unit or functional area; `<vendor>` is the platform the code targets or runs on. When present, `<type>` **MUST** be one of the four workload types — `tool`, `platform`, `service`, `app` — classified by dependency position, not internal implementation: `tool` is a standalone collection of libraries or utilities; `platform` is infrastructure or tooling that others build on; `service` supplies data to apps; `app` is the top-of-stack workload and **MUST NOT** depend on another `app`. `<name>` is used only together with a `<type>`, and lets a complex codebase be split into typed repositories. Agentic behavior is not a type — it is recorded as `shape` (B1.2). Names use lowercase letters, numbers, and hyphens, with no invented abbreviations.

    * **Asset identifier.** Every in-scope asset **MUST** carry a stable, immutable identifier of the form `{{ASSET_ID_PREFIX}}<DOMAIN>-<SLUG>`, minted in the `ai-org-management` registry when the solution comes in scope (Gate 1). The identifier survives repository renames and is the handle the AI Solution Requirements, the Solution Spec, and the work-tracker Epic (Jira in the reference configuration) reference. Where a solution has both authoring assets (skills, prompts) and deployed infrastructure (IaC), both **MUST** carry the same identifier.

    * **Governance manifest.** Every **Tier 2+** solution **MUST** carry a governance manifest — in SKILL.md frontmatter, a plugin manifest, or a `SOLUTION.md` — validating against the schema in `ai-org-management`. It records at minimum the asset identifier, SemVer, workload type, shape, tier, track, oversight mode (B1.4), maximum data sensitivity touched, the accountable owner, lifecycle state (B1.8), the linked governed records (Requirements, Spec, Epic), and any MCP servers reached (which feed the AIBOM). The manifest is the single authoritative source for this metadata; other surfaces are projections of it and **MUST NOT** be maintained as a second source of truth. For **Tier 1**, a manifest is **recommended (SHOULD)**.

    * **Tag projections.** The manifest projects onto two discovery surfaces. Deployed resources **MUST** carry `{{TAG_NAMESPACE}}:`-prefixed AWS resource tags (workload type, shape, tier, environment, owner, and the asset identifier at minimum); source repositories **MUST** carry the `{{TAG_NAMESPACE}}-ai-governed` marker topic plus the `{{TAG_NAMESPACE}}-` / `{{TAG_NAMESPACE}}-ai-` topics that project the manifest, per the projection map in `ai-org-management`. Because GitHub topics are public even on private repositories, environment, owner, business unit, and any customer-identifying, secret, or financial value **MUST NOT** appear in a topic; these live in the manifest and in AWS tags only. Data sensitivity in a topic is limited to the coarse class.

    * **Enforcement and inventory.** The `{{TAG_NAMESPACE}}-ai-governed` marker and the `{{ASSET_ID_PREFIX}}*` registry together constitute the shared AI solution inventory this standard monitors — a repository or resource that runs an in-scope asset without them is shadow AI. Tag validity **MUST** be enforceable through AWS Organizations tag policies, defined in `aws-org-management`.

---

## Terms and Terminology — entries to add

*(Insert alphabetically into the existing Terms and Terminology list.)*

* **Asset identifier (`{{ASSET_ID_PREFIX}}*`):** the stable, immutable name for an in-scope AI asset, of the form `{{ASSET_ID_PREFIX}}<DOMAIN>-<SLUG>`, minted in the `ai-org-management` registry and referenced by the Requirements, Spec, and Epic. Survives repository renames.
* **Governance manifest:** the authoritative per-asset metadata block (identifier, version, workload type, shape, tier, track, oversight, data class, owner, lifecycle, records, MCP servers) from which AWS tags and GitHub topics are projected. The single source of truth for an asset's governance metadata.
* **Workload type:** the classification of an asset by dependency position — `tool`, `platform`, `service`, or `app` — independent of how it decides (its shape). Names *where a thing sits*, not *how it behaves*.
* **Inventory marker (`{{TAG_NAMESPACE}}-ai-governed`):** the GitHub topic applied to any repository carrying an in-scope AI asset, making the standard's inventory a single query. Its absence on such a repository is a shadow-AI signal.

---

## Changelog — row to add

*(Add to the top of the existing Changelog table.)*

| Version | Date | Description | Author | SME Reviewed and Approved | Approved |
| --- | --- | --- | --- | --- | --- |
| {{AI_STANDARD_PENDING_VERSION}} | 7/14/2026 | Added Technical Control **Naming, tagging & inventory**: repository grammar (`<vendor>-org-management` / `<domain>-<vendor>-<type>-<name>`, with optional type/name), four workload types, `{{ASSET_ID_PREFIX}}*` asset identifier, governance manifest, AWS-tag and GitHub-topic projections, and inventory enforcement. Controlled values referenced from the canonical machine-readable vocabulary in `ai-org-management`. Added four Terms entries. | {{AI_GOVERNANCE_OWNER}} |  |  |
