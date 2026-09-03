# grc-core

Governance, Risk & Compliance skills for {{ORG_NAME}}. **Recommendations only — never approves, sends, or acts.**

- **security-review-travel-risk** — evaluates a request to work internationally
  from a country outside the pre-approved list. Re-verifies current sanctions,
  travel-advisory, data-adequacy, and state-surveillance facts across four risk
  domains, applies the standard's tiered decision logic (Tier 1 auto-approve →
  Tier 4 decline), and outputs a Jira-ready risk review with cited, as-of-dated
  evidence. Implements your organization's *Standard: Evaluating International
  Travel Work Requests* (v{{TRAVEL_STANDARD_VERSION}}); it does not redefine
  that logic.

- **tprm-security-review** — read-only third-party / vendor security risk review
  for a new vendor before engagement or an existing vendor at re-evaluation.
  Gathers evidence from the compliance platform (Drata in the reference
  configuration, read-only), points to the vendor's trust center
  with a retrieval checklist, checks against your organization's *Third Party
  and Vendor Management Policy* (v{{TPRM_POLICY_VERSION}}) and *Risk Management
  Policy* (v{{RISK_POLICY_VERSION}}), scores
  Likelihood × Impact on the sanctioned risk matrix, and returns a review memo
  plus a proposed inventory row — both drafts. Never writes, downloads, accepts
  an NDA, or approves a vendor; it recommends.
- **tprm-vendor-review-update** — records a completed, human-approved TPRM review
  outcome to the compliance platform and prepares the business-tools inventory
  row. **Gated write
  capability:** proposes every change and executes only on explicit per-change
  confirmation, and its executing write path must not be enabled org-wide until
  {{ORG_NAME}}'s own approval of the write capability — an approved amendment to
  the solution's requirements and spec documents — is in place. Companion to
  `tprm-security-review`.

Invoke as `/grc-core:security-review-travel-risk`,
`/grc-core:tprm-security-review`, or `/grc-core:tprm-vendor-review-update`.

## Guardrails

- **Recommendation, not decision.** Output is a recommended verdict for a human
  reviewer — never an approval, and never a legal or compliance determination.
- **Defer determinations.** Sanctions and data-protection calls are Legal's.
- **Data minimization.** No confidential customer names, contract values, usage
  data, or excess personal data — output lands in a ticket.
- **Fail safe.** Unverifiable blocker-domain facts → "manual review required,"
  never "clear."

## Configuration

Fill every placeholder below before adopting this plugin. Tokens use
double-brace UPPER_SNAKE syntax and appear across `plugin.json`, the three
`SKILL.md` files, and the `references/` files.

| Placeholder | What to put there |
|---|---|
| `{{ORG_NAME}}` | Your organization's name, as it should read in prose and in the plugin author field. |
| `{{COMPLIANCE_CONTACT_EMAIL}}` | The mailbox third parties must use to notify you of an incident or breach. |
| `{{BUSINESS_TECHNOLOGY_LEAD_ROLE}}` | The role title that can grant an exception to your third-party/vendor management policy (alongside your President and Board). |
| `{{TPRM_POLICY_VERSION}}` | Version of your Third Party and Vendor Management Policy that this skill is pinned to (e.g. `2.2`). |
| `{{TPRM_POLICY_DATE}}` | Effective date of that pinned TPVM Policy version (`YYYY-MM-DD`). |
| `{{RISK_POLICY_VERSION}}` | Version of your Risk Management Policy that supplies the likelihood/impact scales and matrix (e.g. `2.3`). |
| `{{RISK_POLICY_DATE}}` | Effective date of that pinned Risk Management Policy version (`YYYY-MM-DD`). |
| `{{TRAVEL_STANDARD_VERSION}}` | Version of your Standard: Evaluating International Travel Work Requests that the travel skill implements. |
| `{{WIKI_HOST}}` | Host / cloud ID of your wiki (Confluence in the reference configuration), e.g. `example.atlassian.net`. |
| `{{PAGE_ID_TPRM_POLICY}}` | Wiki page ID of your Third Party and Vendor Management Policy. |
| `{{PAGE_ID_RISK_MANAGEMENT_POLICY}}` | Wiki page ID of your Risk Management Policy. |
| `{{PAGE_ID_INFORMATION_SECURITY_POLICY}}` | Wiki page ID of your Information Security Policy (top-level control expectations). |
| `{{INVENTORY_SHEET_TAB_GID}}` | Tab/sheet identifier of the business-tools inventory (vendor + tools list) you record approved outcomes into. |

The named integrations are the **reference configuration, not a requirement**:
the compliance platform (Drata) and the work tracker (Jira / Atlassian,
including Confluence for policy pages) can each be swapped for an equivalent
product. MCP tool names such as `Drata_getVendor` are the real tool names in the
reference configuration — substitute the equivalent tool from your own platform
and the surrounding logic is unchanged. Public sources referenced by the travel
skill (OFAC, US State Department, EU adequacy decisions, Freedom House, Citizen
Lab, Amnesty Security Lab, Forbidden Stories) are generic and need no
configuration.

Owner: Security / GRC. Skill version tracks the standard version
(v1.0 ↔ v{{TRAVEL_STANDARD_VERSION}}); re-version both when the rubric, tiers,
or sources change.
