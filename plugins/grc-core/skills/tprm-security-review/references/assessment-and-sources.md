# Assessment Checklist & Source Registry — TPRM Security Review

Two parts: (1) the assessment domains to work through, and (2) where evidence comes from. Both derive from your organization's Third Party and Vendor Management Policy (`{{PAGE_ID_TPRM_POLICY}}`). Registry entries are pointers, not cached answers — fetch live each run and stamp an as-of date.

## Part 1 — Assessment domains (from TPVM Policy)

Work each domain relevant to the vendor's data/access. For each, record: what was found, the evidence source, an as-of date, and whether it is verified or **UNVERIFIED**. Scale the depth to the Stage-A triage — a Public/no-access tool does not need the full set; a Restricted-data privileged-access sub-processor needs all of it.

1. **Competence & reputation** — industry standing, breach/financial-instability history, references, certifications (ISO 27001, SOC 2 Type II), track record.
2. **Information security policy & practices** — comprehensive policies (confidentiality/integrity/availability), executive support, regular review.
3. **Identity & access control** — RBAC, MFA, least privilege, periodic user-access reviews, strong authentication for sensitive data.
4. **Human resource risk** — background checks, security-awareness training, signed confidentiality agreements.
5. **Risk management** — their own risk-assessment program, risk treatment plans, their own third-party/sub-processor risk management, independent audit of compliance.
6. **Business continuity & DR** — tested BCP/DRP, redundancy/failover for critical services.
7. **Data protection** — encryption at rest and in transit (e.g., AES-256), data access controls, data classification.
8. **Backups** — frequency, encryption/secure storage, restore testing.
9. **Data retention** — retention policy and periods aligned to regulatory needs.
10. **Data destruction** — secure destruction methods, certificates of destruction for regulated data.
11. **Software development** — secure SDLC, code review, change management.
12. **Operational security** — technical protections (firewall/IDS/IPS/AV), vulnerability management/patching, logging & monitoring.
13. **Incident response** — IR plan, prompt breach-notification process, post-incident review. (TPVM requires third parties to notify {{ORG_NAME}} of incidents/breaches via {{COMPLIANCE_CONTACT_EMAIL}}.)
14. **Physical security** — facility access controls, visitor management, secure storage of assets/media.

**Special case — third parties acting on {{ORG_NAME}}'s behalf or embedded in the product:** additionally assess whether the vendor lets {{ORG_NAME}} meet its customer commitments (SLAs, data protection, data privacy, sub-processor obligations).

## Part 2 — Source registry

### Compliance platform (read-only)
Tool names below are Drata's in the reference configuration; the equivalent tool on another compliance platform can be substituted without changing the logic.
- `Drata_listVendors` / `Drata_getVendor` — existing vendor record: current rating, owner, last assessment date, category.
- `Drata_listVendorDocuments` — attached evidence (SOC 2, ISO cert, DPA, pen test).
- `Drata_listVendorSecurityReviews` — prior reviews and their outcomes.
- `Drata_listRiskRegisters` / `Drata_searchRisks` — any risks already logged against the vendor.
- Do **not** call `Drata_createVendor` / `Drata_updateVendor` here — writes belong to `tprm-vendor-review-update` under its confirm gate.

### Trust center (human-performed retrieval — point, don't automate)
Name the vendor's trust center and list what to obtain; the human downloads and accepts any NDA. Standard request set:
- SOC 2 Type II report (current period).
- ISO 27001 certificate + Statement of Applicability.
- Most recent penetration test summary / attestation.
- DPA and current sub-processor list.
- BCP/DR summary.
Never auto-login, auto-download, or accept a click-through NDA (Legal/Compliance gate).

### Policies (the wiki — Confluence in the reference configuration; fetch live, confirm pinned versions)
- Third Party and Vendor Management Policy — `getConfluencePage(cloudId="{{WIKI_HOST}}", pageId="{{PAGE_ID_TPRM_POLICY}}", contentFormat="markdown")` — pinned v{{TPRM_POLICY_VERSION}} ({{TPRM_POLICY_DATE}}).
- Risk Management Policy — `pageId="{{PAGE_ID_RISK_MANAGEMENT_POLICY}}"` — pinned v{{RISK_POLICY_VERSION}} ({{RISK_POLICY_DATE}}).
- Information Security Policy — `pageId="{{PAGE_ID_INFORMATION_SECURITY_POLICY}}"` — top-level control expectations, when needed.
- If a fetched version differs from the pin, flag drift and treat the rubric as potentially stale.

### Inventory (read to check current state)
- Business tools inventory spreadsheet (Google Sheets in the reference configuration), tab `gid={{INVENTORY_SHEET_TAB_GID}}` (vendor list + manually managed vendor/tools list).
- Read to check whether the vendor already exists and its current row values.
- **Column reconciliation open item:** the exact header row was not captured at authoring time (connector timeout). Confirm the live headers before mapping. Policy-required fields the row MUST carry (TPVM Policy): service provided, data owner, assigned risk rating, date of last security assessment. The skill adds vendor name, data classification, and re-evaluation due date.

## Compliance context (for framing, not for the skill to determine)
Adherence supports SOC 2, ISO 27001, ISAE 3000 (data assurance), and efforts under CPRA, GDPR, DORA. Whether a specific regulation applies to a given vendor is a Legal determination — flag, don't conclude.
