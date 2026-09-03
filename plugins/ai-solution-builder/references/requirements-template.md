# AI Solution Requirements — Template

*The first of the two required records for any AI-generated solution that drives a business workflow. The **AI Solution Requirements defines the requirements** — the problem and what must be true for the solution to be correct. The builder then produces a **Solution Spec** that implements an approved AI Solution Requirements. Companion to the **{{ORG_NAME}} AI Use Framework: Standards for Deploying AI in Non-Product Solutions** (the "Standard").*

*Audience: the requesting function — technical or not. Normative keywords: **MUST**, **SHOULD**, **MAY**, as in the Standard.*

---
***We strongly advise you write this by hand, not with AI.*** *The requirements need to be in your words. Use AI to refine your thoughts, but don't rely on AI to generate requirements as it tends to lead to ineffective solutions (commonly referred to as "AI slop").*

---

## When this document is required

Complete an AI Solution Requirements (and a downstream Solution Spec) for **any AI-generated solution that drives a business workflow** — i.e., it produces or changes work the business relies on: it writes to a system of record, feeds a decision, faces customers/finance/compliance, or more than one role depends on it (Standard, Scope). A purely personal tool you review every time you run it is exempt — until it crosses any of those lines, at which point both records **MUST** exist *before* the new use begins.

## Risk tiers: determine your proposed tier

Sort the problem or workflow into a tier *before* you design anything, judging by **whichever is worse**: how much harm a mistake could cause, and how much the solution would act on its own (Standard, B1.3). Pick the tier that fits the riskiest answer.

- **Tier 1 — Low:** Internal-only and easy to undo, doesn't write to an authoritative system of record, and touches no regulated data. A mistake is low-cost and reversible, so the solution can act with light supervision.
- **Tier 2 — Moderate:** Writes to an authoritative system of record (CRM, finance, production database), faces outside the company, or moves real money — so a person approves the important steps. *(Choosing a self-directing agent raises the floor to at least Tier 2. If an AI model makes the key decision, treat it as Tier 3 unless a person or a fixed, rule-based check verifies the result — Standard, B1.2.)*
- **Tier 3 — High:** Involves regulated data (personal, health, or financial), affects safety, can't be undone, or makes customer-facing decisions. A person must approve, and Tier 3 carries the fullest requirements plus a documented sign-off.

A solution can be only as independent as the **lower** of two limits allows: what its track record has earned, and what its tier permits.

## How depth scales

One template, three tiers. Each section is tagged with the tier at which it becomes required; the proposed tier above tells you which sections to complete.

| Tag | Meaning |
|---|---|
| **[req'd]** | Required for every in-scope solution, including light Tier 1 tools. |
| **[T2+]** | Add when the solution is Tier 2 or Tier 3. |
| **[T3]** | Add only for Tier 3. |

> **At Tier 1**, the AI Solution Requirements and Solution Spec **MAY** live as two sections of a single page (they remain two logical records). **At Tier 2–3** they are separate documents with the requesting-function sign-off (§13) as the gate between them.

> **No new forms.** The **AI Solution Requirements is your AI-capability request** (Standard, B1.7) — the ask. The **Solution Spec is your shared-inventory record** (the shared AI solution inventory; Standard, Monitoring and Enforcement) — the built thing. Don't duplicate these elsewhere; link to them. *(This mapping is a default — adjust if your intake process differs.)*

**DELETE EVERYTHING ABOVE THIS LINE BEFORE SUBMITTING**
---

## Executive summary (BLUF) **[req'd]**
*A few lines. Fill last, place first.*

- **Requested by / sponsor:**
- **Requesting function:**
- **Proposed risk tier:**
- **Work-effort Epic:** [created after Gate 1]

---

## 1. Problem **[req'd]**
*State the real problem to its root, across its human, organizational, and technical dimensions — not the tool you imagine applying (Standard, "Earn the right to automate", step 1 — Define). Do not frame the problem as a missing feature.*



## 2. Desired outcome / proposed direction **[req'd]**
*What good looks like, and (optionally) the approach you have in mind. The builder may propose a different design in the Solution Spec.*



## 3. Goal **[req'd]**
*Make it SMART where you can: specific, measurable, achievable, realistic, time-bound.*



## 4. Scope **[req'd]**
*Tier 1: one line is enough. State out-of-scope items positively and explicitly — an AI builder cannot infer scope from omission.*

**In scope:** **[T2+]**

**Not in scope (explicit "do NOT build"):** **[T2+]**
-
-

## 5. Functional requirements / deliverables **[T2+]**

*NOTE: Effective functional requirements should be* ***objectively testable***, *not subjective to the reader or any particular stakeholder.*
- Example 1 - Effective and testable: ***A non-admin user can enter in a new customer record - our standard onboarding workflow.***
- Example 2 - Vague and subjective: *Manage customer records.*

| # | Requirement / deliverable | Value (MUST HAVE / NICE TO HAVE) | Owner | Notes |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

## 6. Acceptance criteria **[req'd]**
*The contract of "done." Write each as **Given / When / Then** — readable for reviewers and directly usable as test scaffolding by the builder (and any AI builder). The Solution Spec records test evidence against these exact criteria. Tier 1: one or two; Tier 2+: cover realistic edge cases.*

**Expected outcome (one line):** **[req'd]**
*Tier 1: one line is enough, without the table below.*

| # | Given (context) | When (action) | Then (expected result) | Edge case? |
|---|---|---|---|---|
| 1 | | | | ☐ |
| 2 | | | | ☐ |

## 7. Non-functional requirement targets **[T2+]**
*One line per applicable attribute (ISO/IEC 25010). These are targets the solution must meet; the Solution Spec records how they were met and verified. **Any solution that produces or modifies customer or reporting data MUST meet a data-quality bar proportionate to its tier** (Standard, Technical Controls — Data-quality bar); state those targets in the data-quality row.*

| Attribute | Target |
|---|---|
| Performance efficiency | |
| Reliability / availability | |
| Security | |
| Compatibility / interoperability | |
| Maintainability | |
| Data quality (ISO/IEC 25012) | *(accuracy, completeness, validity, timeliness)* |

## 8. Data involved & sensitivity (declared) **[req'd]**
*Declare every kind of data the solution will read or write. This declaration helps us meet our security and compliance commitments to customers and the business; it also informs the proposed tier and constrains which tools may be used. The Solution Spec confirms the tool-to-data match (Standard, Technical Controls — Tools, data & access).*

| Data the solution will touch | System(s) to interact with | Read / Write |
|---|---|---|
| | | |

## 9. Success metrics — business value **[T2+]**

**{{ORG_NAME}}-related metrics:**

**Initiative impact** — *how this benefits the business and how success is measured after implementation:*

| # | Goal | By when? | Explain |
|---|---|---|---|
| 1 | *e.g., reduce spend by $10k* | | |
| 2 | *Other: increase revenue · increase efficiency · mitigate churn / customer happiness · increase data quality* | | |

## 10. Process-readiness gate **[req'd]**
*AI Solution Requirements intake gate, operationalizing the Standard's strongly-recommended "Earn the right to automate" pattern (Standard, Recommended Patterns). Automation comes last. If either answer is no, the process goes back to be improved before an Solution Spec is started.*

- Is the process already well-run and **Monitored (OM3)** — you track whether it works and act on the numbers? ☐ Yes ☐ No
- Has it been run through **define → remove → optimize → design-for-scale**, automation reserved for last? ☐ Yes ☐ No
- *If no to either:* what has to be true before it's ready?

## 11. Business risks, unknowns & downstream implications **[req'd]**
1. Risks to implementing this?
2. Risks to **not** implementing it?
3. Downstream implications of implementing it?

## 12. Glossary **[req'd if non-obvious terms are used]**
*Define domain terms, acronyms, and internal names (e.g., an internal acronym, a reporting framework, a vendor or data-source name, a data-modeling term, a recurring internal process). The Solution Spec inherits this glossary.*

| Term | Definition |
|---|---|
| | |

## 13. Requesting-function review & sign-off — GATE 1 **[T2+ required · T1 optional]**
*A person other than the eventual builder validates that the problem is worth solving and the requirements are sound, **before** design begins (Standard, Roles and Responsibilities). On approval, mark the AI Solution Requirements approved for design and start the Solution Spec.*

| Reviewer | Function | Date | Decision (Approve for design / Revise / Hold) |
|---|---|---|---|
| | | | |

---

## Change Log **[req'd]**

| Change made by | Change proposed | Why change was made | Date | Change approved by |
|---|---|---|---|---|
| | | | | |
