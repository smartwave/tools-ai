# Placeholder index

Every organization-specific value across all three artifacts, in one table.
Tokens are `{{UPPER_SNAKE}}` in double braces, so a single pass of find-and-replace
per token is enough to adopt the whole set.

This list covers every *controlled* organization-specific value. It does not
cover illustrative examples — sample repo names, sample domains, example
assignees, the seed registry row, the worked manifest — which were rewritten to
neutral values rather than tokenized, because their job is to illustrate a shape
rather than to be substituted. Change those to match your own environment as you
adopt.

**Substitute before use.** Several tokens sit inside regular expressions, JSON
Schema `pattern` fields, and CI scripts — those files will not validate until the
token is replaced with a literal value. They are marked **CI** below.

## Identity

| Token | What to put there | Used in |
|---|---|---|
| `{{ORG_NAME}}` | Your organization's name, as it should read in prose and author fields. | all three |
| `{{ORG_DOMAIN}}` | Your DNS domain, e.g. `example.com`. Used for the JSON Schema `$id` host and a service-account address. | ai-org-management |
| `{{GITHUB_ORG}}` | Your GitHub organization slug (repository host in the reference configuration). | ai-org-management |

## People and roles

Roles are titles, not names. Map each to the equivalent function in your
organization; if two of these are the same person, use the same value twice.

| Token | What to put there | Used in |
|---|---|---|
| `{{AI_GOVERNANCE_OWNER}}` | Person accountable for the AI governance document set (owner and changelog fields). | ai-org-management, ai-solution-builder |
| `{{AI_GOVERNANCE_OWNER_HANDLE}}` | That person's GitHub handle, for CODEOWNERS. | ai-org-management |
| `{{SECURITY_LEAD_ROLE}}` | Title of the security leader who owns the deployment standard (CISO or equivalent). | ai-solution-builder |
| `{{PLATFORM_SECURITY_LEAD_ROLE}}` | Title of the owner of the Agentic SDLC page, whose sign-off gates edits to it. | ai-org-management |
| `{{PLATFORM_SECURITY_TEAM}}` | GitHub team slug for that security function, for CODEOWNERS. | ai-org-management |
| `{{AUTOMATION_LEAD_ROLE}}` | Title of the leader of your automation function. | ai-solution-builder |
| `{{BUSINESS_TECHNOLOGY_LEAD_ROLE}}` | **Title** of the IT / business-technology leader who can grant an exception to your third-party/vendor management policy. | ai-solution-builder, grc-core |
| `{{BUSINESS_TECHNOLOGY_LEAD}}` | **Name** of the person holding that role, where the AI Use Framework names its co-owner. | ai-solution-builder |
| `{{SOLUTION_OWNER}}` | A person's name for the example manifest's `owner` field (illustrative only). | ai-org-management |

## Contacts

| Token | What to put there | Used in |
|---|---|---|
| `{{SECURITY_CONTACT_EMAIL}}` | Where security issues and stop-and-report escalations go. | ai-solution-builder |
| `{{COMPLIANCE_CONTACT_EMAIL}}` | The mailbox third parties must use to notify you of an incident or breach. | grc-core |
| `{{IT_HELPDESK_EMAIL}}` | Support mailbox for the plugin (manifest author email). | ai-solution-builder |

## Wiki and work tracker

Confluence and Jira are the reference configuration; substitute your own wiki
and tracker and these tokens still describe the values you need.

| Token | What to put there | Used in |
|---|---|---|
| `{{WIKI_HOST}}` | Wiki host, e.g. `example.atlassian.net`. | all three |
| `{{WIKI_SPACE_KEY}}` | Space/section key the governed pages live in. | ai-org-management, ai-solution-builder |
| `{{TRACKER_HOST}}` | Work-tracker host. In the reference configuration this is the **same value** as `{{WIKI_HOST}}` (one Atlassian site serving both Jira and Confluence); it is a separate token so a split stack does not have to fight the substitution. | ai-solution-builder |
| `{{PRODUCT_TRACKER_PROJECT_KEY}}` | Project key for the **product** track, whose Epic field conventions that track follows. | ai-solution-builder |
| `{{TEAM_CONVENTIONS_DOC}}` | The owning team's conventions document the **non-product** track defers to. | ai-solution-builder |
| `{{TICKET_REF}}` | A work-tracker issue key. Two uses: the change ticket a changelog entry was delivered under (`ai-solution-builder/CHANGELOG.md`), and the work-effort Epic key in the example manifest (`ai-org-management/examples/`). Substitute per site rather than globally. | ai-org-management, ai-solution-builder |

## Page identifiers

One per governed document. If you are not using a page-id-based wiki, replace
these with whatever addresses a page (a slug, a path, a URL).

| Token | Document | Used in |
|---|---|---|
| `{{PAGE_ID_AI_STANDARDS}}` | AI Solution Standards: Deploying AI Solutions | ai-org-management |
| `{{PAGE_ID_AGENTIC_SDLC}}` | Standard & Configuration: The Agentic SDLC | ai-org-management |
| `{{PAGE_ID_AI_USE_FRAMEWORK}}` | AI Use Framework Guide (all-employee) | ai-solution-builder |
| `{{PAGE_ID_AI_POLICY}}` | AI Policy | ai-solution-builder |
| `{{PAGE_ID_RISK_MANAGEMENT_POLICY}}` | Risk Management Policy | ai-solution-builder, grc-core |
| `{{PAGE_ID_INFORMATION_SECURITY_POLICY}}` | Information Security Policy | ai-solution-builder, grc-core |
| `{{PAGE_ID_CHANGE_MANAGEMENT_POLICY}}` | Change Management Policy | ai-solution-builder |
| `{{PAGE_ID_TPRM_POLICY}}` | Third Party and Vendor Management Policy | grc-core |

## Policy versions and dates

These pin a skill to a specific revision of your policy, so the skill can state
what it is implementing. Re-pin when the policy is re-versioned.

| Token | What to put there | Used in |
|---|---|---|
| `{{AI_STANDARD_VERSION}}` | Live version of your AI Solution Standard (reference value: `0.2.0`). | ai-org-management |
| `{{AI_STANDARD_PENDING_VERSION}}` | Version of the *pending, unratified* standard insert (reference value: `0.3.0`). Rules tagged `[REF insert]` must not be enforced until it lands. | ai-org-management |
| `{{AGENTIC_SDLC_VERSION}}` | Live version of the Agentic SDLC page (reference value: `0.2`). | ai-org-management |
| `{{AGENTIC_SDLC_PENDING_VERSION}}` | Pending version of that page (reference value: `0.3`). | ai-org-management |
| `{{TPRM_POLICY_VERSION}}` / `{{TPRM_POLICY_DATE}}` | Version and effective date of your Third Party and Vendor Management Policy. | grc-core |
| `{{RISK_POLICY_VERSION}}` / `{{RISK_POLICY_DATE}}` | Version and effective date of your Risk Management Policy — the source of the likelihood/impact scales and the matrix. | grc-core |
| `{{TRAVEL_STANDARD_VERSION}}` | Version of your Standard: Evaluating International Travel Work Requests. | grc-core |

## Travel review

| Token | What to put there | Used in |
|---|---|---|
| `{{TRAVEL_PREAPPROVED_COUNTRIES}}` | The countries your organization already accepts as work locations, so a trip there short-circuits the review. | grc-core |
| `{{TRAVEL_SHORT_STAY_LIMIT}}` | Stay length at or under which a pre-approved destination needs no security review (reference value: `2 weeks`). Above it, the HR/tax notification flag applies. | grc-core |

## Naming and tagging — **CI**

These appear inside regexes, JSON Schema patterns, and conformance scripts.
**The repository's CI will fail until they are literal values.**

| Token | What to put there | Reference value | Used in |
|---|---|---|---|
| `{{ASSET_ID_PREFIX}}` | Prefix for minted asset IDs, uppercase, immutable once minted. | `ORG-AI-` | ai-org-management |
| `{{TAG_NAMESPACE}}` | Namespace for cloud resource tags and repository topics. | `org` | ai-org-management |
| `{{DOC_ID_PREFIX}}` | Prefix of your **document**-ID family (distinct from asset IDs). | `ORG` | ai-org-management |
| `{{INVENTORY_SHEET_TAB_GID}}` | Tab identifier of the business-tools inventory that approved vendor outcomes are recorded into. | — | grc-core |

Files that must be substituted before CI passes:
`vocabulary/vocabulary.yaml`, `schemas/manifest.schema.json`,
`registry/registry.yaml`, `examples/manifest.example.yaml`,
`projections/tag-map.yaml`, `ci/check-registry`, `ci/check-projections`, and
`.github/workflows/confluence-sync.yml` (which additionally needs repository
secrets and variables — listed in a comment at the top of that file).

## Finding what is left

```bash
grep -rno '{{[A-Z0-9_]*}}' . --exclude-dir=.git | sort -u
```

Run it after substitution; a clean result means the artifacts are fully adopted.
