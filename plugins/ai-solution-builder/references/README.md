# Canonical source of truth

These files are the **authoritative** versions of {{ORG_NAME}}'s non-product AI deployment
documents. The skills in this plugin (`ai-problem-framer`, `ai-poc-brief-author`, `ai-poc-builder`,
`ai-poc-summary-author`, `ai-requirements-doc-author`, `ai-solution-spec-author`,
`ai-solution-design-author`, `ai-work-planner`) and the Gemini Gems in `../gems/` read them at runtime, so plugin
guidance can never drift from policy. Edit here, open a PR, merge — the org marketplace re-syncs and
(downstream) the wiki is regenerated. **One edit point. Do not hand-edit the Confluence copies.**

| File | Role | Authority |
| --- | --- | --- |
| `deployment-standard.md` | Non-Product AI Deployment Standard — the controls/bar | **The bar.** Standards are defined here; the AI Solution Requirements and Solution Spec cite it by section (B1.2–B1.8, Technical Controls, Roles, Recommended Patterns). |
| `ai-use-framework.md` | All-employee AI Use Framework Guide | Company-wide principles the Standard sits beneath. |
| `requirements-template.md` | AI Solution Requirements template | Requirements record (the ask). |
| `solution-spec-template.md` | Solution Spec template | Evidence record (the built thing). Leading YAML header maps to the Confluence Page Properties macro — **keep it the first line; do not prepend anything.** |
| `solution-design-template.md` | Solution Design template (Tier 2/3) | Technical design + authored test plan for a new Tier 2/3 solution (B1.10). Leading YAML header maps to the Confluence Page Properties macro — **keep it the first line; do not prepend anything.** |
| `problem-framing-methods.md` | Problem-framing reasoning guidance for Stage 0 (5W1H, slice the loaf, Pareto, Five Whys and validation, future-state lenses) | Plugin-internal reasoning guidance read by `ai-problem-framer`, `ai-poc-brief-author`, `ai-poc-summary-author`, and inlined into the Gems. Not a wiki-synced document. |
| `ultralight-brief-template.md` | Ultralight Problem Brief template (Stage 0, step 1) | The one-page problem / root cause / future state record, written by the person. Its §1 becomes Requirements §1. Not a governed record; not wiki-synced. |
| `poc-brief-template.md` | POC Brief template (Stage 0, step 2) | The document a person builds a throwaway POC from, with the paste-ready build prompt. Not a governed record. |
| `poc-summary-template.md` | POC Summary template (Stage 0, step 4) | What the POC did, every change made while building, what was learned, the ask to IT. The first document IT sees; not a governed record. |
| `work-breakdown-principles.md` | Work-breakdown reasoning guidance for `ai-work-planner` | Plugin-internal reasoning guidance (vertical slices, spikes-first, risk-first sequencing, grain). Not a wiki-synced document; supports B1.9 work-effort Epic planning. |

Sync direction is GitHub -> wiki, one-way. If the Standard, AI Solution Requirements, or Solution Spec changes, only these
files change; the skills pick it up automatically because they read the file, not a hard-coded copy.

## Configuration

Confluence is the **reference configuration** for the wiki side of this sync; another wiki
(Notion, SharePoint, MediaWiki, a docs repo) can be substituted — the one-way,
GitHub-is-the-source model and the "do not hand-edit the published copies" rule are what
matter, not the product. Likewise Jira is the reference work tracker and GitHub the
reference repository host; substitute the equivalent tool your organization uses.

Fill these placeholders before publishing these documents inside your organization:

| Placeholder | What it is |
| --- | --- |
| `{{ORG_NAME}}` | Your organization's name. |
| `{{SECURITY_CONTACT_EMAIL}}` | Where security issues and stop-and-report escalations go. |
| `{{AI_GOVERNANCE_OWNER}}` | The person accountable for these documents (changelog / owner fields). |
| `{{AUTOMATION_LEAD_ROLE}}` | Title of the leader of the automation function. |
| `{{SECURITY_LEAD_ROLE}}` | Title of the security leader who owns the Standard. |
| `{{BUSINESS_TECHNOLOGY_LEAD_ROLE}}` | Title of the IT / business-technology leader (third-party-policy exception authority). |
| `{{BUSINESS_TECHNOLOGY_LEAD}}` | Name of the person holding that role, named as an AI Use Framework co-owner. |
| `{{WIKI_HOST}}` / `{{WIKI_SPACE_KEY}}` | Wiki host and space the published copies live in. |
| `{{PAGE_ID_AI_USE_FRAMEWORK}}` | Published page id of the AI Use Framework Guide. |
| `{{PAGE_ID_AI_POLICY}}` | Published page id of the AI Policy. |
| `{{PAGE_ID_RISK_MANAGEMENT_POLICY}}` | Published page id of the Risk Management Policy. |
| `{{PAGE_ID_INFORMATION_SECURITY_POLICY}}` | Published page id of the Information Security Policy. |
| `{{PAGE_ID_CHANGE_MANAGEMENT_POLICY}}` | Published page id of the Change Management Policy. |
| `{{PRODUCT_TRACKER_PROJECT_KEY}}` | Work-tracker project key whose Epic field conventions the product track follows. |
