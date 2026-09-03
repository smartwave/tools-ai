---
# Machine-readable header. Generated/maintained on the Solution Spec side; references the approved AI Solution Requirements.
# In the wiki (Confluence in the reference configuration), map these to the Page Properties macro
# (queryable via a Page Properties Report); substitute the equivalent structured-properties feature.
sdr_id:
title:
linked_srb:                  # REQUIRED — the approved AI Solution Requirements this implements
work_effort_epic:            # the B1.9 work-effort Epic key (e.g. TEAM-123); blank until opened at Gate 1
status:                      # draft | in_review | approved | live | retired
tier:                        # 1 | 2 | 3  (confirmed; must match or justify a change from the AI Solution Requirements' proposed tier)
solution_shape:              # workflow | single_request | agent | multi_agent   (B1.2)
deployment_path:             # local | track_b | track_a
oversight_mode:              # HITL | HOTL | autonomous   (B1.4)
accountable_owner:
builder:
change_acceptor:             # must differ from builder
data_labels: []              # any of: public | internal | confidential | regulated
allowed_tools: []
model_and_version:
writes_to_system_of_record: false   # tier driver (B1.3)
ai_makes_key_decision: false        # if true, see B1.2: treat as Tier 3 unless a fixed check verifies
last_reviewed:
next_review_trigger:
---

# Solution Spec — Template

*The second of the two required records for any AI-generated solution that drives a business workflow. The Solution Spec **implements an approved AI Solution Requirements**: it evidences that the solution meets the AI Solution Requirements' requirements and the Standard's controls, and documents how it is tested, observed, and governed. Companion to the **{{ORG_NAME}} AI Use Framework: Standards for Deploying AI in Non-Product Solutions** (the "Standard"). Standards are defined in the Standard, not restated here.*

*Audience: the builder, plus Security and Data/Privacy reviewers. Normative keywords: **MUST**, **SHOULD**, **MAY**, as in the Standard. **[harness]** marks scaffolding around the model; **[red flag]** marks a stop-and-report condition.*

---

## When this document is required

An Solution Spec is required whenever an AI Solution Requirements is required (see the AI Solution Requirements' "When this document is required") and **MUST NOT** be started until its AI Solution Requirements is approved for design (AI Solution Requirements §13, Gate 1). The Solution Spec records the decisions the Standard requires — solution shape (B1.2), risk tier (B1.3), oversight (B1.4), data/tooling (Technical Controls), and the pre-flight gate (B1.7) — in one place, before building.

## How depth scales

One template, three tiers. Each section is tagged with the tier at which it becomes required. The confirmed tier in the header drives this.

| Tag | Meaning |
|---|---|
| **[req'd]** | Required for every in-scope solution, including light Tier 1 tools. |
| **[T2+]** | Add when the solution is Tier 2 or Tier 3. |
| **[T3]** | Add only for Tier 3. |

The **YAML header** is the machine-readable control record: tooling can read shape, tier, oversight, data labels, allowed tools, and the tier-driver flags (for example, a check that blocks a `tier: 3` deploy with no §22 sign-off).

> **No new forms.** The **Solution Spec is your shared-inventory record** (Standard, Monitoring and Enforcement); the **AI Solution Requirements is the AI-capability request** (Standard, B1.7). Link the two; don't duplicate.

> **At Tier 1**, the AI Solution Requirements and Solution Spec **MAY** live as two sections of a single page. **At Tier 2–3** they are separate documents.

**DELETE EVERYTHING ABOVE THIS LINE BEFORE SUBMITTING**
---

## 0. Source requirements **[req'd]**
*The Solution Spec implements requirements; it does not restate them.*

- **Linked AI Solution Requirements (approved):** *(also in `linked_srb`)*
- **Confirmed tier matches the AI Solution Requirements' proposed tier?** ☐ Yes ☐ No → *if no, justify the change:*
- **Inherits the AI Solution Requirements glossary.** Add technical terms only in §24 below.

---

# Part B — Solution & Process Design

## 1. Solution overview, owner & builder **[req'd]**
*Per the Standard's Roles, name the **Solution Owner** (accountable for results, oversight, monitoring, retirement) and the **Builder** separately; the Builder may not self-accept changes to their own solution.*

**Overview:**

**Solution Owner (accountable):** *(also in `accountable_owner`)*

**Builder:** *(also in `builder`)*

**Continuous-improvement backlog (link):**

## 2. Who is involved **[T2+]**
*Roles in this solution. Loop in Security and Data/Privacy on data labeling, design, and testing (Standard, Roles and Responsibilities).*
-
-

## 3. High-level flow diagram **[T2+]**
*Embed or link.*



## 4. Affected systems and processes **[T2+]**
*Flag any system this **writes to as an authoritative system of record** — a tier driver (B1.3), mirrored as `writes_to_system_of_record`.*

| UPSTREAM system/process | INTERDEPENDENT system/process | DOWNSTREAM system/process |
|---|---|---|
| | | |

**Writes to an authoritative system of record?** ☐ No ☐ Yes → *which:*

## 5. Inputs, outputs & behavioral contract **[T2+]**
*Per Technical Controls (Solution behavior, Tier 2+), the behavioral contract **MUST** be written before build for anything beyond a single request. Define external behavior precisely enough to build and test against.*

**Inputs & outputs:**

| Inputs for this process | Outputs of this process |
|---|---|
| | |

**Behavioral contract:**

| Element | Specification |
|---|---|
| **Preconditions** *(what must be true before it runs)* | |
| **Postconditions** *(what must be true after a successful run)* | |
| **Invariants** *(what must never change / never happen)* | |
| **Integration contracts** *(per system read/written: schema, fields, format — required)* | |
| **Idempotency & failure/retry** *(anything that writes/sends/moves/deletes MUST be idempotent or guarded against double-execution; define partial-failure behavior)* | |

## 6. Key steps / runbook **[T2+]**

| Process step # | Procedure | Reference guide | Expected time |
|---|---|---|---|
| | | | |

## 7. Cost & resources **[T2+]**
*Resources to build and run the solution — both the one-time build cost and the ongoing run cost (compute, model/API spend, licenses, maintenance). Timelines tie to the AI Solution Requirements deliverables.*

| Resource category | Specific resource | When? | Why? |
|---|---|---|---|
| People | | | |
| Money | | | |
| Existing tools | | | |
| Other | | | |

---

# Part C — Shape, Tier & Oversight

## 8. Solution shape **[req'd]** — B1.2
*A rules-based, pre-mappable step **MUST** be built as a fixed workflow or single request, never handed to a self-directing agent. Choosing an agent raises the floor to at least Tier 2; if the agent makes the key decision, treat it as Tier 3 unless a person or a fixed, rule-based check verifies the result. **Multiple coordinated agents MUST NOT** be built for non-product work without Engineering and Security. Mirrored in `solution_shape`.*

- **Shape:** ☐ Fixed workflow ☐ Single request ☐ Agent ☐ Multi-agent
- **If agent or multi-agent — why a fixed workflow won't do:**
- **If the agent makes the key decision — the person or fixed check that verifies the result:**
- **If multi-agent — Engineering & Security involvement (names / date):**

## 9. Risk-tier confirmation & justification **[req'd]** — B1.3
*Confirm the tier against B1.3 criteria. An automation **MUST** be only as independent as the lower of what its track record has earned and what its tier permits.*



## 10. Oversight mode & rationale **[req'd]** — B1.4
*Mirrored in `oversight_mode`. **HITL** (approve each important action first) is required for anything irreversible, leaving the company, or involving money. **HOTL** (run while monitored) only when actions are reversible, internal, recorded, and independently checkable. **Fully autonomous** only for read-only monitoring that makes no judgment calls and that no outside party relies on — never for a tool a non-engineer runs locally.*

- **Mode & why it's permitted at this tier:**

---

# Part D — AI Controls
*Build-time controls that constrain what the solution can do (Standard, Technical Controls). Enum-style fields are mirrored in the YAML header so they can be enforced by tooling rather than by inspection.*

## 11. Data labeling & tool-to-data match **[req'd]** — Tools, data & access
*Take the data the AI Solution Requirements declared (AI Solution Requirements §8) and confirm each tool is approved for that label. A tool cleared only for public data **MUST** be technically blocked from confidential or production data. Regulated or secret data **MUST** be kept out of prompts and protected by hard controls outside the model. Mirrored in `data_labels`.*

| Data the solution touches | Label (Public / Internal / Confidential / Regulated) | Read / Write | Tool approved for this label? | Public-only tools technically blocked from sensitive data? |
|---|---|---|---|---|
| | | | ☐ Yes ☐ No | ☐ Yes ☐ N/A |

## 12. Model & version pinning; prompt version control **[T2+]** — Model & environment
- **AI model & exact version (pinned):** *(also in `model_and_version`)*
- **Where prompts are version-controlled:**

## 13. Development / test / production separation **[T2+]** — Model & environment; ISO 27001 A.8.31
*Development and production **MUST** be separated (credentials and data), and the solution **MUST** be tested in a non-production setting before go-live.*

- **Dev and prod separated (credentials and data)?** ☐ Yes — *how:*
- **Tested in a non-production setting before go-live?** ☐ Yes — *where:*

## 14. Secrets & credentials **[harness] [req'd]** — Secrets & credentials
*Real passwords, API keys, and tokens **MUST NOT** appear in code, prompts, files, Drive, a Claude Project, or a repository. They **MUST** live in an approved secret store or system keychain and be referenced at runtime.*

- **Where secrets live (approved store / Keychain):**
- **Referenced at runtime (not embedded)?** ☐ Yes
- **Separate dev and prod keys?** ☐ Yes
- **Spending limit + alert on any chargeable key?** ☐ Yes ☐ N/A

## 15. Allowed tools & connectors **[req'd list · T2+ full]** — Tools, data & access
*Approved-only tool list (mirrored in `allowed_tools`). MCP servers/connectors **MUST** be IT-reviewed and scope-checked before use. **[red flag: a connector requesting more access than its job needs.]**

| Tool / MCP server | What it can reach | IT-reviewed & scope-checked? |
|---|---|---|
| | | ☐ Yes ☐ N/A |

## 16. Guardrails, limits & untrusted-content handling **[harness] [T2+]** — Guardrails & limits
*The solution **MUST** check input and output and cap spend and rate. It **MUST** treat ingested content (emails, documents, web pages) as untrusted and **MUST NOT** act on instructions hidden inside material it was only asked to read. **[red flag: an agent acting on instructions it found in content.]***

- Input checks:
- Output checks:
- Spend cap / rate limit:
- Untrusted-content / prompt-injection handling:

## 17. Vendor agreement & Security sign-off **[T2+]** — Tools, data & access
*Any AI integration/connector reaching into another system **MUST** have a signed vendor agreement and Security's sign-off first.*
- Vendor agreement in place? ☐ Yes ☐ N/A
- Security sign-off? ☐ Yes — *by / date:*

---

# Part E — Testing, Observability & Governance

## 18. Testing
*State how the solution is tested, then record the evidence. Test against the **exact** Given/When/Then criteria in AI Solution Requirements §6.*

### 18.1 Test approach **[T2+]**
- **Environment(s) tested in** *(non-production — see §13):*
- **Test data** *(how confidential/regulated data is handled or substituted in test):*
- **Who runs the tests:**
- **Coverage** *(happy path + realistic edge cases):*
- **Pass/fail bar:**

### 18.2 Evidence vs AI Solution Requirements acceptance criteria **[req'd light · T2+ full]**

| AI Solution Requirements criterion # | Result (Pass / Fail) | Evidence / notes |
|---|---|---|
| 1 | | |
| 2 | | |

### 18.3 Non-functional & data-quality verification **[T2+]**
*How each NFR target from AI Solution Requirements §7 was met and confirmed. The data-quality row is a **MUST** for any solution that produces or modifies customer or reporting data (Standard, Technical Controls — Data-quality bar; ISO/IEC 25012).*

| Attribute | Target (from AI Solution Requirements §7) | Met? | How verified |
|---|---|---|---|
| Performance efficiency | | ☐ | |
| Reliability / availability | | ☐ | |
| Security | | ☐ | |
| Compatibility / interoperability | | ☐ | |
| Maintainability | | ☐ | |
| Data quality — accuracy, completeness, validity, timeliness | | ☐ | |

### 18.4 Adversarial / stress test **[T3]**
*Deliberately try to break or trick it (including prompt-injection attempts). Record what you tried and what you found (B1.7).*



## 19. Observability, monitoring & stop controls **[harness]**
*State how the solution is watched once live, and how it is stopped or undone (Standard, Technical Controls — Observability).*

- **Decisions logged in reconstructable detail, and where:** **[req'd]**
- **Quality signal monitored** *(and threshold/alert):* **[T2+]**
- **Drift signal monitored** *(behavior change over time):* **[T2+]**
- **Who reviews the signals, how often:** **[T2+]**
- **Tested "off switch"** *(how to stop it fast):* **[req'd]**
- **Documented rollback** *(how to undo a bad run):* **[req'd]**

## 20. Governance & lifecycle
*State how the solution is governed over its life.*

- **Accountable owner & reviewers** *(Solution Owner; Security & Data/Privacy involvement — Roles):* **[req'd]**
- **Separation of duties** *(the change acceptor differs from the builder — mirrored in `change_acceptor`):* **[req'd]**
- **Escalation — Mandatory Stop-and-Report [red flag]:** *Stop the session and contact Security/IT if an agent takes an action you didn't request, a secret is exposed or committed, or a tool demands privilege it shouldn't need (Standard, Mandatory Stop-and-Report; fuller watchlist in Recommended Patterns).* **[req'd]**
- **Review cadence & re-governance triggers** *(re-review on: new dependents, a new system of record, a schedule, or sensitive-data changes — Standard, Scope; mirror `next_review_trigger`):* **[req'd]**
- **Change control (B1.6):** *Deployment and every material change follow the Change Management Policy. For AI, a "change" includes model/version, prompts, tools/connectors, independence, and audience. Each change is classified (Standard / Normal / Emergency), accepted by someone other than the builder, carries a documented rollback if Major Normal or Emergency, and gets a post-implementation review if Emergency or Major Normal. Promoting a personal tool to shared, scheduled, or system-of-record use is a Normal change.* **[req'd]**
- **Exceptions (B1.8):** *Log any waived **MUST** in the Security Exceptions Register with reason, alternative safeguard, who accepted the risk, and expiry. Recurring exceptions signal a rethink. Summary below.* **[as needed]**

| MUST waived | Reason | Alternative safeguard | Risk accepted by | Expiry |
|---|---|---|---|---|
| | | | | |

- **Retirement plan (B1.8):** *How and when it ends, and what happens to its data; an automation left without an owner **MUST** be retired or reassigned.* **[req'd light · T2+ full]**

---

# Part F — Approval

## 21. Pre-flight gate **[T2+]** — B1.7
*Ready for production when all are true:*
- ☐ Implements an approved AI Solution Requirements; confirmed tier matches (or change justified); shape confirmed (§8).
- ☐ Goal defined to root cause; data labeled and least-privilege access set.
- ☐ Model and version fixed; prompts version-controlled (§12).
- ☐ Dev/prod separated; tested in non-production (§13).
- ☐ Secrets in an approved store; chargeable keys capped (§14).
- ☐ Uses only an approved tool list (§15).
- ☐ All AI Solution Requirements acceptance criteria pass (§18.2), including edge cases.
- ☐ NFR and data-quality targets met and verified (§18.3).
- ☐ Guardrails check input/output, cap spend and rate, and reject hidden instructions (§16).
- ☐ Monitoring covers result quality and behavior drift, not just uptime (§19).
- ☐ Decisions logged reconstructably; tested off switch and documented rollback exist (§19).
- ☐ One person named accountable; affected people know their role and how much to trust the output (§20).
- ☐ Documented retirement path (§20).
- ☐ Registered through the standard AI-capability request.
- ☐ **[T3]** Adversarially stress-tested (§18.4) and documented approver sign-off obtained (§22).

## 22. Approver sign-off — GATE 2 **[T3 required · T2 recommended]**
*The approver **MUST** differ from the builder (Standard, Roles).*

| Approver | Role | Date | Signed |
|---|---|---|---|
| | | | |

---

# Appendix

## 23. Local-lane non-negotiables — Tier 1 local tools only **[conditional]** — B1.5
*Complete this only if `deployment_path: local`. A tool a non-engineer builds and runs on their own machine **MUST** meet all of these, and **MUST** move up a lane before any of these conditions change.*

- ☐ Stays Tier 1 work.
- ☐ A person stays involved — never runs unattended or on a schedule.
- ☐ Scoped to a single working folder, not the whole drive.
- ☐ Runs on an IT-enrolled, current device, not an admin login.
- ☐ **[harness]** Secrets in the macOS Keychain or an approved store — never in Drive or a Claude Project.
- ☐ Handles no regulated or personal data without an approved review.
- ☐ **[harness]** Canonical setup backed up to Drive (config only, dated) — Drive is not a runtime, database, or secret store.
- ☐ Listed in the shared inventory (no shadow AI).

## 24. Glossary — technical additions **[optional]**
*Inherits the AI Solution Requirements glossary (AI Solution Requirements §12). Add only technical terms specific to the build.*

| Term | Definition |
|---|---|
| | |

---

## Change Log **[req'd]**
*Each material change is classified and accepted by someone other than the builder (B1.6); follows the Change Management Policy. May also follow [Keep a Changelog](https://keepachangelog.com/). A Claude Project is not version control — keep dated entries.*

| Change made by | Change proposed | Classification (Standard / Normal / Emergency) | Why change was made | Date | Change accepted by (≠ builder) |
|---|---|---|---|---|---|
| | | | | | |
