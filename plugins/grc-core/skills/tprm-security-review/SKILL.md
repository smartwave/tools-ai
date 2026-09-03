---
name: tprm-security-review
description: >-
  Perform a third-party / vendor security risk review for {{ORG_NAME}} — for a NEW vendor before engagement or an EXISTING vendor at re-evaluation. Gathers evidence from the compliance platform (Drata in the reference configuration — an equivalent tool on another compliance platform can be substituted): vendor record, attached documents, prior security reviews. Points to the vendor's trust center with a retrieval checklist, checks against the Third Party and Vendor Management Policy and Risk Management Policy, scores Likelihood × Impact on the sanctioned risk matrix, and returns a review memo plus a proposed inventory row — both drafts for human review. Use whenever someone asks to assess, review, triage, or re-evaluate a vendor or third party's security, run a TPRM review, vendor risk assessment, or security review of a tool/service, or pastes a vendor name + the data it would touch. Triggers include "security review for [vendor]", "TPRM review of [vendor]", "assess this vendor", "is [tool] safe to use", "re-evaluate [vendor]", "vendor risk assessment". READ-ONLY — never writes to the compliance platform, the inventory, or the wiki, and never approves a vendor; it recommends. To write an approved outcome back to systems of record, hand off to tprm-vendor-review-update.
---

# TPRM Security Review (read-only)

This skill implements your organization's **Third Party and Vendor Management Policy** (wiki page `{{PAGE_ID_TPRM_POLICY}}`) and the scoring model in your **Risk Management Policy** (wiki page `{{PAGE_ID_RISK_MANAGEMENT_POLICY}}`) — Confluence is the wiki in the reference configuration. It applies that logic; it does not redefine it. Where this skill and a policy disagree, the policy governs — flag the discrepancy for the policy owner (GRC / Security).

Pinned: skill **v1.0** ↔ TPVM Policy **v{{TPRM_POLICY_VERSION}} ({{TPRM_POLICY_DATE}})** + Risk Management Policy **v{{RISK_POLICY_VERSION}} ({{RISK_POLICY_DATE}})**. Re-fetch both pages at the start of every run and compare versions; if either moved, say so and treat the rubric as potentially stale rather than assuming this pin still holds.

## Prime directive

This skill produces a **recommendation for a human reviewer**. It never states a vendor "is approved," never assigns a final accepted rating on its own authority (management may override any computed rating — Risk Management Policy), never writes to the compliance platform / the inventory / the wiki, never downloads files, and never accepts a trust-center NDA or click-through. Legal and compliance determinations (contract/NDA sufficiency, GDPR/DORA/CPRA applicability, data-transfer adequacy) belong to Legal — flag them, don't conclude them.

## When to use / not use

**Use:** a new vendor before engagement, or an existing vendor at re-evaluation, wherever a security judgment on a third party is needed.

**Short-circuit (state the outcome, don't run the full review):**
- No access to {{ORG_NAME}} systems and no {{ORG_NAME}} data of any classification touched (e.g., a public marketing site, a read-only reference tool) → lightweight note, no full assessment; recommend Public/Internal-only classification and stop.
- Pure procurement/pricing question with no security dimension → out of scope; say so.

Per TPVM Policy, Confidential or Restricted data must **not** be shared with a third party until a risk assessment is completed and a written agreement with security terms is executed. If the request implies data is already flowing to an unassessed vendor, flag that as a policy exception that only the {{BUSINESS_TECHNOLOGY_LEAD_ROLE}}, President, or Board can grant.

## Inputs

- **Required:** vendor name.
- **Strongly recommended:** the service provided; the data classification(s) the vendor will access/process/store (Restricted / Confidential / Internal / Public); access level (privileged vs. limited); whether the vendor acts on {{ORG_NAME}}'s behalf or is embedded in a {{ORG_NAME}} product sold to customers.
- **Optional:** existing vendor ID in the compliance platform; trust-center URL; data owner.

Do not collect or embed contract value, spend, ARR, or customer names — none of that belongs in a review artifact (data minimization; see Guardrails). If data classification is unknown, ask once; otherwise proceed and record the assumption.

## Process

### Step 1 — Intake, scope, new-vs-existing
Normalize the vendor. Determine data classification in scope and access level. Check the compliance platform for an existing record (`Drata_listVendors` / `Drata_getVendor` in the reference configuration; substitute the equivalent tool on your platform) — if found, note the current rating, last assessment date, and attached evidence; this is a re-evaluation.

### Step 2 — Triage / inherent risk (Stage A)
From data sensitivity + access + on-behalf-of/embedded status, set the assessment depth and the re-evaluation cadence. Per TPVM Policy, high-risk and/or Major/Critical-impact vendors handling sensitive data, or with privileged access, are re-evaluated **at least annually**. See `references/rubric.md`.

### Step 3 — Gather evidence (Stage B)
- **Compliance platform (read-only):** `Drata_getVendor`, `Drata_listVendorDocuments`, `Drata_listVendorSecurityReviews`, and the risk register (`Drata_listRiskRegisters` / `Drata_searchRisks`) for anything already logged. These are the Drata tool names in the reference configuration — the equivalent tools on another compliance platform can be substituted.
- **Trust center:** produce a retrieval checklist naming exactly what a human should obtain (SOC 2 Type II report, ISO 27001 certificate + Statement of Applicability, most recent penetration test summary, DPA / sub-processor list, BCP/DR summary). The skill points; the human downloads and accepts any NDA.
- **Policies (drift check):** re-fetch `{{PAGE_ID_TPRM_POLICY}}` and `{{PAGE_ID_RISK_MANAGEMENT_POLICY}}` and confirm the pinned versions still match.

Record each item with its **source and an as-of date**. See `references/assessment-and-sources.md`.

### Step 4 — Assess against the checklist
Work the fourteen TPVM assessment domains in `references/assessment-and-sources.md`, noting strengths, gaps, and missing evidence per domain, each with a source and as-of date. No conclusion without evidence: if an item cannot be verified, mark it **UNVERIFIED** and lower confidence — never assume a control is present.

### Step 5 — Score (Stage C)
Assign an **Impact** (1–5) and a **Likelihood** (1–5) with a one-line justification each, tied to Step 4 evidence. Look up the rating on the matrix in `references/rubric.md` and map it to the policy risk response (Low → accept; Medium → GRC review; High/Critical → mandatory Risk Treatment Plan). Show the L, I, product, and cell so the result is reproducible.

### Step 6 — Assemble outputs
Produce the review memo and the proposed inventory row (below). Both are drafts. If the outcome is High or Critical, state plainly that engagement/continuation is outside risk tolerance until a documented Risk Treatment Plan exists.

## Fact-verification requirements

- **Freshness:** evidence gathered this run; stamp each item with an as-of date. Prior reviews on file are inputs, not substitutes — re-verify.
- **No fabrication:** never invent a certification, control, or audit result. Missing evidence is UNVERIFIED, not "compliant."
- **Fail safe:** a vendor that would touch Restricted/Confidential data with unverifiable core controls (encryption, access control, SOC 2 / ISO 27001) defaults to **MANUAL REVIEW**, never "Low / clear."
- **Provenance:** every rating input cites where the evidence came from (Drata document, trust-center report + date, policy clause).

## Output format

Portable Markdown (pastes into a compliance-platform review note, a wiki page, or a ticket — Drata and Confluence in the reference configuration). Lead with the recommendation; never omit the disclaimer or the source/as-of stamps.

```
# TPRM Security Review — {Vendor}

Recommendation: {LOW | MEDIUM | HIGH | CRITICAL | MANUAL REVIEW}
Vendor: {name}   Service: {what it does}
Data in scope: {Restricted/Confidential/Internal/Public}   Access: {privileged/limited}
On behalf of {{ORG_NAME}} / in-product: {yes/no}
Reviewed: {YYYY-MM-DD}   Re-evaluate by: {YYYY-MM-DD}

Risk score: Likelihood {1-5} × Impact {1-5} = {product} → {rating}   (matrix cell cited)
Policy response: {accept / GRC review / mandatory Risk Treatment Plan}

Assessment summary (evidence + as-of):
| Domain | Finding | Evidence (as-of) |
| ... the material domains, strengths and gaps ... |

Blockers: {none | list}
Required before engagement/continuation: {contract security terms | NDA | DPA | treatment plan | ...}
Determinations to route to Legal: {contract/NDA sufficiency, GDPR/DORA/CPRA, data transfer}
Assumptions / UNVERIFIED items: {list}

Proposed inventory row (draft — reconcile columns against the live sheet):
{vendor} | {service} | {data owner} | {data classification} | {rating} | {last assessment date} | {re-eval due date}

_Recommendation only — not an approval and not a legal/compliance determination. Management may override this rating. Evidence as of the dates above; re-verify before a final decision. No contract value, spend, or customer names in this artifact._
```

## Guardrails

- **Recommendation, not decision.** Never say a vendor "is approved." A human sets the accepted rating.
- **No writes, no downloads, no NDA.** Read-only across the compliance platform and the wiki (Drata/Confluence in the reference configuration); point to the trust center, don't automate it. To persist an approved outcome, hand off to `tprm-vendor-review-update`.
- **Defer determinations.** Contract/NDA sufficiency and regulatory applicability are Legal's — flag, don't conclude.
- **Data minimization.** No contract value, spend, ARR, or customer names in the memo or the inventory row.
- **Fail safe.** Unverifiable core controls on a Restricted/Confidential vendor → MANUAL REVIEW.

## Edge cases

- **Existing vendor, stale review (> re-eval cadence):** run a full re-evaluation; note the staleness.
- **No trust center / vendor refuses documentation:** MANUAL REVIEW with what was found; cannot rate "clear" on absence of evidence.
- **Embedded in a {{ORG_NAME}} product / acts on our behalf:** raise the bar — assess ability to meet {{ORG_NAME}}'s customer SLAs, data-protection, and sub-processor commitments (TPVM "Third Parties Acting on Behalf of {{ORG_NAME}}").
- **Conflicting evidence:** present both, take the more conservative rating, note the conflict.
- **Policy version drift detected in Step 3:** flag it and treat the rubric as potentially stale; recommend re-versioning the skill.

## Acceptance test cases

Profiles, not real vendors. A build passes when each returns the expected band with sourced, as-of-dated evidence.

| Input profile | Expected | Why |
|---|---|---|
| Reference/marketing tool, no {{ORG_NAME}} data, no access | Lightweight / Low | Short-circuit: no data, no access |
| SaaS sub-processor, Confidential data, SOC 2 Type II + ISO 27001, MFA + AES-256, recent pen test | Medium | Sensitive data but strong evidenced controls → GRC review |
| Vendor with privileged production access, no SOC 2, no pen test evidence | High/Critical | Privileged access + unverified core controls → treatment plan |
| Vendor handling Restricted data that refuses all documentation | Manual review | Fail-safe: cannot clear on absent evidence |

## Maintenance

- Owner: **GRC / Security**. Changes to scoring or tiers require the policy owner's approval.
- Keep the description tight for accurate triggering; test against the acceptance profiles before publishing.
- Pinned to TPVM v{{TPRM_POLICY_VERSION}} + Risk Management v{{RISK_POLICY_VERSION}}. Re-version when either policy changes (scale, matrix, cadence, checklist). Review at least annually.
