---
name: tprm-vendor-review-update
description: >-
  Record the outcome of a COMPLETED, human-approved TPRM security review to {{ORG_NAME}}'s systems of record — update the vendor's record in the compliance platform (Drata in the reference configuration; an equivalent tool on another compliance platform can be substituted) with the assigned risk rating, last-assessment date and review notes, and produce the inventory row for the business-tools sheet. Use only after tprm-security-review has produced a result AND a human has approved the rating (and, for High/Critical, a Risk Treatment Plan exists). Trigger phrases include "record this vendor review", "update [vendor]'s risk rating in Drata", "log the approved review", "write the review outcome to the inventory", "mark the TPRM review complete". This skill WRITES to a system of record — a governed capability that proposes every change and executes only on explicit per-change confirmation. It never invents a review outcome, never approves a vendor itself, and never auto-writes. It is NOT vendor onboarding/procurement — only the review-outcome write-back.
---

# TPRM Vendor Review Update (gated write)

Companion to `tprm-security-review`. That skill recommends; this one records an already-approved outcome to the compliance platform (Drata in the reference configuration) and the inventory. It implements the same policies (TPVM `{{PAGE_ID_TPRM_POLICY}}` v{{TPRM_POLICY_VERSION}}, Risk Management `{{PAGE_ID_RISK_MANAGEMENT_POLICY}}` v{{RISK_POLICY_VERSION}}) and versions with them (skill **v1.0**).

## Governance banner — read before use

This skill introduces a **write capability** to a system of record (the compliance platform) and prepares a write to the business-tools inventory. Per your organization's AI deployment standard, that is a new capability beyond the read-only review lane and **requires {{ORG_NAME}}'s own approval of the write capability — an approved amendment to the solution's requirements and spec documents (formerly "SRB" and "SDR") — before this skill is rolled out**. Until that amendment is in place, use the skill only to *propose* changes; do not enable the executing write path.

## Prime directive

- **Never invent an outcome.** The rating, evidence, and reviewer must come from a completed `tprm-security-review`. If no approved review is provided, stop and ask for it — do not re-derive or guess a rating here.
- **Propose, then execute on confirmation.** Show the exact before→after diff for every field and wait for an explicit "yes" per change. No silent writes, no batch auto-apply.
- **Human owns the decision.** The skill does not approve vendors, accept risk, or sign off. It records a decision a human already made.

## Preconditions (refuse if unmet)

1. A completed `tprm-security-review` result is supplied, including the rating, the Likelihood×Impact basis, and the evidence/as-of dates.
2. A human has approved the rating. Management may override the computed rating (Risk Management Policy) — record the human-approved value, not the raw computed one, and note if they differ.
3. If the approved rating is **High or Critical**, a documented **Risk Treatment Plan** reference is supplied. Without it, the vendor is outside risk tolerance and must not be recorded as accepted — stop and flag.
4. **Reviewer separation:** the person approving/applying this write should not be the sole author of the review. Note who reviewed and who approved; if they are the same person, flag it for a second approver before executing.

## Process

### Step 1 — Load the approved outcome
Take the review result and the approved rating as input. Do not open a fresh assessment; if the review is missing or stale, hand back to `tprm-security-review`.

### Step 2 — Resolve the target
`Drata_getVendor` (or `Drata_listVendors`) to fetch the current record from the compliance platform — substitute the equivalent tool if you run another platform. Read the current inventory row for the vendor from the business-tools sheet (`gid={{INVENTORY_SHEET_TAB_GID}}`).

### Step 3 — Build the diff
Compute, per field, current value → proposed value:
- **Vendor record in the compliance platform:** assigned risk rating, date of last security assessment, review notes / next re-evaluation due date (map to the actual fields returned by `Drata_getVendor`, or by its equivalent on your platform; do not assume field names — read them first).
- **Inventory row:** service provided, data owner, assigned risk rating, last security assessment date, re-evaluation due date. Reconcile against the live sheet headers before mapping (authoring-time column capture was blocked by a connector timeout).

### Step 4 — Confirm, then execute
Present the full diff. For each change, get an explicit confirmation.
- **Compliance platform:** on confirmation, apply with `Drata_updateVendor` — or its equivalent on your platform — once {{ORG_NAME}}'s approval of the write capability (the requirements/spec amendment) is in force. One vendor at a time.
- **Inventory:** there is **no first-party spreadsheet write tool available**, so this skill cannot execute the inventory update even when authorized. Output the exact paste-ready row and the target tab/row for a human to apply. Do not attempt browser UI automation to write the sheet.

### Step 5 — Report
Summarize what was written to the compliance platform (with the resulting values) and what still needs manual application (the inventory row), plus the re-evaluation due date.

## Guardrails

- **Confirm-before-execute on every write.** No exceptions for "obvious" or "small" changes.
- **No fabricated outcomes.** Rating and evidence trace to a `tprm-security-review`; no review, no write.
- **High/Critical gate.** No "accepted" record without a Risk Treatment Plan reference.
- **Reviewer separation.** Flag when author and approver are the same.
- **Data minimization.** Never write contract value, spend, ARR, or customer names into compliance-platform notes (Drata in the reference configuration) or the inventory.
- **No deletes.** This skill updates; it never deletes a vendor or an inventory row.
- **Scope.** Review-outcome write-back only — not procurement, contracting, or access provisioning.

## Maintenance

- Owner: **GRC / Security**. Pinned to TPVM v{{TPRM_POLICY_VERSION}} + Risk Management v{{RISK_POLICY_VERSION}}; re-version with them and with `tprm-security-review`.
- Rollout is gated on {{ORG_NAME}}'s approval of the write capability — the amendment to the solution's requirements and spec documents. Review at least annually.
