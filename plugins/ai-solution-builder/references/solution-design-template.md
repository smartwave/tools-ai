---
# Machine-readable header. Generated/maintained on the Solution Design side; references the
# approved AI Solution Requirements and the Solution Spec. In the wiki (Confluence in the reference
# configuration), map these to the Page Properties macro (queryable via a Page Properties Report);
# substitute the equivalent structured-properties feature.
design_id:
title:
linked_requirements:        # REQUIRED — the approved AI Solution Requirements this designs for
linked_spec:                # the Solution Spec this design is evidenced against (once it exists)
status:                     # draft | in_review | approved_for_build | superseded
tier:                       # 2 | 3   (Solution Design is REQUIRED for a new Tier 2/3 solution; optional at Tier 1)
solution_shape:             # workflow | single_request | agent | multi_agent   (B1.2)
accountable_owner:
builder:
design_reviewer:            # must differ from builder (B1.6 separation of duties)
test_plan_status:           # not_started | authored | passing   (tests are a design deliverable — see §6)
last_reviewed:
---

# Solution Design — Template

*The technical design record for a new **Tier 2/3** AI solution that drives a business workflow.
It follows the approved **AI Solution Requirements** (Gate 1) and sits in the staged pipeline as:
**POC (Stage 0) → AI Solution Requirements (Stage 1, Gate 1) → Solution Design (Stage 2) → build →
Solution Spec (Stage 3) → deploy.** The Design says **how** the solution will be built and — the
headline deliverable — **authors the tests** that the build must pass. Companion to the
**{{ORG_NAME}} AI Use Framework: Standards for Deploying AI in Non-Product Solutions** (the
"Standard"); standards are defined there, not restated here.*

*Audience: the builder, plus a design reviewer and Security/Data-Privacy where the tier calls for
it. Normative keywords: **MUST**, **SHOULD**, **MAY**, as in the Standard. **[harness]** marks
scaffolding around the model; **[T3]** marks Tier-3-only items; **[req'd]** marks a required field.*

> **When this is required.** A Solution Design **MUST** be produced for a new Tier 2/3 solution
> before build begins (Standard B1.10). At Tier 1 it is optional — a few sentences of "how" in the
> Solution Spec is enough. It **MUST NOT** be started until the AI Solution Requirements is approved
> at Gate 1, and it is reviewed (design reviewer ≠ builder) before build.

---

## 1. Purpose & scope
- **What this designs** *(one or two sentences; links the approved AI Solution Requirements):* **[req'd]**
- **In / out of scope for this design:**
- **Confirmed tier and solution shape** *(from the Requirements; B1.2/B1.3):* **[req'd]**

## 2. Architecture & solution shape (B1.2)
- **Components and how they connect** *(diagram or bullet list; name each agent/workflow/subagent):* **[req'd]**
- **Data flows** *(what data moves where; label sensitivity per §8 of the Requirements):* **[req'd]**
- **Why this shape** *(a fixed workflow unless an agent is justified; an agent raises the floor to Tier 2 — B1.2):*

## 3. Harness & environment [harness]
*How each harness piece is realised (see the Standard's "harness at a glance"). Match to the chosen
deployment path (Local / Track B / Track A).*
- **Execution / runtime:** **[req'd]**
- **Secrets** *(approved store; never in code/prompts/repo — Technical Controls):* **[req'd]**
- **State / memory:**
- **Tools / data access** *(approved-tool × data-class match; least privilege):* **[req'd]**
- **Guardrails & limits** *(input/output checks, spend/rate caps; enforced outside the agent for T2+):* **[req'd]**
- **Observability, off switch & rollback** *(quality + drift monitoring T2+; tested off switch, all tiers):* **[req'd]**

## 4. Contracts (Tier 2+)
- **Behavioral contract** *(preconditions, postconditions, invariants — B1 Technical Controls):* **[req'd]**
- **Integration contract(s)** *(schema/fields/format for each system read/written; idempotency & partial-failure behavior for anything that writes/sends/moves/deletes):* **[req'd]**

## 5. Control-implementation plan
*For each Required Control that applies at this tier, state how the design meets it and where the
evidence will live (the Solution Spec records the as-built proof). Do not restate the control text.*

| Control (Standard §) | How this design meets it | Evidence location (Spec §) |
|---|---|---|
| Secrets & credentials | | |
| Tools, data & access | | |
| Guardrails & limits (T2+) | | |
| Model/version pinning (T2+) | | |
| Dev/prod separation (T2+) | | |

## 6. Test plan & authored tests **[req'd — this is the point of the Design stage]**
*Tests are authored **here, as a design deliverable** (Standard B1.7a), not first written at
pre-flight. Every functional requirement (Requirements §5) and acceptance criterion
(Requirements §6, Given/When/Then) **MUST** map to at least one concrete test.*

- **Test approach** *(what kinds: unit / functional / integration / data-quality checks / evals for
  model behavior):* **[req'd]**
- **Requirement → test map** *(table: Requirement/AC ID → test name/location → what "pass" means):* **[req'd]**

  | Requirement / AC | Test (name / file) | Pass criterion |
  |---|---|---|
  | | | |

- **Edge & negative cases** *(realistic edge cases; expected-failure behavior):* **[req'd for T2+]**
- **Adversarial / red-team tests** *(prompt injection, tool misuse, excessive agency, memory/context
  poisoning — OWASP Top 10 for Agentic Applications 2026):* **[T3 — req'd]**
- **Where tests live and how they run** *(repo path, CI hook if any; an SDLC test agent SHOULD run
  in the pipeline and open a PR, not self-merge):* **[req'd]**
- **Data for tests** *(synthetic / de-identified; no regulated or production data in test fixtures):* **[req'd]**

## 7. Threat model summary
- **Top risks (OWASP Agentic 2026) and mitigations** *(feeds Requirements §11 and the pre-flight
  threat-model gate B1.7):* **[req'd for T2+]**

## 8. Rollback & retirement design
- **How to turn it off fast** *(tested off switch):* **[req'd]**
- **Rollback plan and retirement path** *(what happens to data on retirement):* **[req'd]**

## 9. Design review & sign-off
- **Design reviewer** *(≠ builder; B1.6 separation of duties):* **[req'd for T2+]**
- **Review outcome / date:**
- **Approved for build?** *(a person decides; this is not a pre-flight sign-off — the Solution Spec's
  pre-flight gate B1.7 still governs go-live):*

---

*This Design does not authorize deployment. Build proceeds against it; the **Solution Spec** records
what was actually built, tested, and verified and carries the pre-flight gate (B1.7) that governs
go-live. If this Design conflicts with the Standard, the Standard wins.*
