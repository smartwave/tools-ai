Classification: Internal Use Only

Policy Owner: `<{{AUTOMATION_LEAD_ROLE}} / {{SECURITY_LEAD_ROLE}}>`

Effective Date: `<to be set>`

‌

# **Purpose**

The purpose of this standard is to define the mandatory requirements for building and deploying AI-enabled automation for {{ORG_NAME}}'s internal and operational work — that is, all non-product use (work that is not part of the customer-facing product, which is governed separately). It establishes a risk-tiered, "controls-sized-to-risk" posture so that the safe path is also the fast path: enough control to keep us out of trouble, little enough that no one is tempted to route around it.

This standard is the builder's layer beneath the all-employee [AI Use Framework Guide](https://{{WIKI_HOST}}/wiki/spaces/{{WIKI_SPACE_KEY}}/pages/{{PAGE_ID_AI_USE_FRAMEWORK}}). It assumes the company-wide principles in that guide (you author the intent; own the output; keep a human in the loop; the four non-negotiables) and does not restate them.

The agentic-specific control families in this standard are organized against the four functions of the **NIST AI Risk Management Framework (AI RMF 1.0)** — Govern, Map, Measure, Manage — and draw on the **OWASP Top 10 for Agentic Applications (2026)**. ISO 27001 Annex A remains the certification backbone; the NIST functions provide the agent-specific reasoning beneath it.

This standard satisfies

* ISO 27001:2022 Annex A.8.25 Secure development life cycle
* ISO 27001:2022 Annex A.8.32 Change management

This standard supports

* ISO 27001:2022 Annex A.5.10 Acceptable use of information and other associated assets
* ISO 27001:2022 Annex A.5.15 Access control
* ISO 27001:2022 Annex A.5.23 Information security for use of cloud services
* ISO 27001:2022 Annex A.8.15 Logging and Annex A.8.16 Monitoring activities
* ISO 27001:2022 Annex A.8.29 Security testing in development and acceptance
* ISO 27001:2022 Annex A.8.31 Separation of development, test and production environments

| NIST AI RMF function | Where it lives in this standard |
| --- | --- |
| **Govern** | Roles and Responsibilities; Change control (B1.6); Exceptions and retirement (B1.8); Work-effort tracking (B1.9); Monitoring and Enforcement |
| **Map** | Solution Shape (B1.2); Tier (B1.3); threat modeling in the pre-flight gate (B1.7); behavioral and integration contracts |
| **Measure** | Tests authored in the Solution Design (B1.7a); pre-flight "correct result" and edge-case testing; data-quality bar (ISO/IEC 25012); evaluations; observability of quality and drift |
| **Manage** | Oversight modes (B1.4); guardrails and limits; off switch and rollback; Mandatory Stop-and-Report |

## **This document is informed by**

* [AI Policy](https://{{WIKI_HOST}}/wiki/spaces/{{WIKI_SPACE_KEY}}/pages/{{PAGE_ID_AI_POLICY}})
* [Risk Management Policy](https://{{WIKI_HOST}}/wiki/spaces/{{WIKI_SPACE_KEY}}/pages/{{PAGE_ID_RISK_MANAGEMENT_POLICY}})
* [Information Security Policy](https://{{WIKI_HOST}}/wiki/spaces/{{WIKI_SPACE_KEY}}/pages/{{PAGE_ID_INFORMATION_SECURITY_POLICY}})
* [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
* [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
* [OWASP State of Agentic AI Security and Governance / Enterprise Adoption Maturity Model (2026)](https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/)

## **This document informs**

* [AI Use Framework Guide: Using AI Safely to Work Faster](https://{{WIKI_HOST}}/wiki/spaces/{{WIKI_SPACE_KEY}}/pages/{{PAGE_ID_AI_USE_FRAMEWORK}})
* AI Solution Requirements template
* Solution Spec template

### Scope

* **Who:** all employees, contractors, and third parties who build or deploy AI-enabled automation for {{ORG_NAME}}'s internal or operational work, technical or not.
* **What — this standard applies the moment an automation:**

    * more than one role relies on;
    * writes to an authoritative system of record;
    * acts without a person approving each result; or
    * touches customers, finances, safety, or compliance.
    
* **Out of scope (until a trigger above is met):** a personal tool you build and review yourself each time. It is out of scope **until** it grows into one of the conditions above — at which point it must be brought under this standard *before* the new use begins.
* **Governed separately:** the customer-facing product (covered by the product SDLC and its own controls).

‌

# **Non-Product AI Deployment Standard**

The following govern how we build and deploy AI for internal and operational work. **Required Controls** are mandatory (**MUST / SHALL**). **Recommended Patterns** are strongly advised but not gates (**SHOULD / MAY**). **\[harness\]** marks the scaffolding around the model — runtime, secrets, state, guardrails, logging, the off switch. **\[red flag\]** marks a stop-and-report condition. Tier applicability (Tier 1 / 2 / 3) is noted where a control scales.

How the records relate: the **AI Solution Requirements** sets a solution's requirements; this **Standard** sets the bar; the **Solution Design** (Tier 2/3) sets out how the solution will be built and authors the tests; the **Solution Spec** evidences that a given solution meets all three. Standards are defined here, not in the records.

The staged, gated pipeline for a non-product AI solution is: **POC (Stage 0 — learn, pre-gate) → AI Solution Requirements (Stage 1, Gate 1 — earns the right to be promoted to production) → Solution Design (Stage 2, required for a new Tier 2/3 solution — B1.10) → build → Solution Spec (Stage 3 — as-built evidence, governed by the pre-flight gate, B1.7) → deploy.** Independence and ceremony scale with tier: Tier 1 stays light; Tier 2/3 add the Design record, authored tests, and sign-offs.

## **Guiding Principles**

*Non-normative — the reasoning behind the controls.*

* **The safe path should be the easy path.** Controls are sized to the risk on purpose. The goal is sustainable speed: the fastest *good* path.
* **You author the intent; the model executes it.** Independence is therefore granted deliberately, never by default — an automation gets only as much autonomy as its track record and risk tier allow.
* **The simplest shape that does the job is the right one.** Each step up in complexity adds cost, unpredictability, and review burden, so complexity must be earned.
* **Automation is the top of the climb, not the start.** A process should be understood and simplified before it is mechanized; automating a broken or un-optimized process locks in the waste.
* **Govern at the speed you ship, not behind it.** The failure mode this standard exists to prevent is well documented: organizations adopting agents faster than they can govern them, with oversight still calibrated for assistant-style copilots while teams quietly ship custom and multi-agent systems.

## **Roles and Responsibilities**

*The roles below are named as **functions**, not job titles: each maps to {{ORG_NAME}}'s equivalent function, whatever it is called locally (for example, "Security" is whoever performs security review and exception approval; "IT / Platform" is whoever owns device enrollment and the approved tool list). Where a specific title is needed — the policy owner, the escalation authority — this standard uses a placeholder ({{AUTOMATION_LEAD_ROLE}}, {{SECURITY_LEAD_ROLE}}) for {{ORG_NAME}} to fill. A single person may hold more than one function, except where this standard requires two different people.*

* **Solution Owner (Accountable):** one person named accountable for every in-scope solution — for its results, its oversight mode, its monitoring, and its retirement. Logs any exception with reason, safeguard, risk acceptor, and expiry. An automation left without an owner must be retired or reassigned.
* **Builder:** designs, tests, and documents the solution to this standard. May not self-accept changes to their own solution.
* **Change Acceptor / Approver:** accepts each change (someone other than the builder); provides documented sign-off for Tier 3 solutions.
* **Security:** approves exceptions; reviews MCP servers/connectors and their scope; is looped in on data labeling, design, and testing; receives stop-and-report escalations.
* **Data / Privacy:** is looped in on data labeling and on any use of regulated or personal data.
* **IT / Platform:** maintains device enrollment, approved secret stores, the approved tool list, and connector review.
* **Engineering:** owns Track A (production / regulated / Tier 2–3) builds; is involved before any multi-agent solution is built.
* **Managers:** ensure their teams comply and surface exceptions and shadow AI.

## **Standards (Required Controls)**

### **Solution Shape and Tier**

* **Shape (B1.2):** A step that is a standard process (rules-based, pre-mappable) **MUST** be built as a fixed workflow or single request, never handed to a self-directing agent. Choosing an **agent MUST** raise the solution to at least **Tier 2**; if the agent makes the key decision, treat it as **Tier 3** unless a person or a fixed, rule-based check verifies the result. **Multiple coordinated agents MUST NOT** be built for non-product work without Engineering and Security involvement.
* **Tier (B1.3):** Every in-scope solution **MUST** be tiered before design, by whichever is worse — potential harm or degree of independence:

    * **Tier 1 (Low):** easy to undo, internal-only, no writes to an authoritative system, no regulated data.
    * **Tier 2 (Moderate):** writes to an authoritative system, faces outside the company, or moves money.
    * **Tier 3 (High):** regulated data, safety impact, irreversible, or customer-facing decisions.
    
    An automation **MUST** be only as independent as the *lower* of what its track record has earned and what its tier permits.
* **Oversight (B1.4):**

    * **Human-in-the-loop** (approve each important action first) is **required** for anything irreversible, leaving the company, or involving money.
    * **Human-on-the-loop** (run while monitored/spot-checked) is permitted **only** when actions are reversible, internal, recorded, and independently checkable.
    * **Fully autonomous** is permitted **only** for read-only monitoring that makes no judgment calls and that no outside party relies on. It is **NOT** permitted for a tool a non-engineer runs locally.

### **Process Controls**

* **Local-lane non-negotiables — Tier 1 only (B1.5):** A tool a non-engineer builds and runs on their own machine **MUST**:

    * stay Tier 1 work;
    * keep a person involved — never run unattended or on a schedule;
    * be scoped to a single working folder, not the whole drive;
    * run on an IT-enrolled, current device, not an admin login;
    * **\[harness\]** keep secrets in the macOS Keychain or an approved store — never in Drive or a Claude Project;
    * not handle regulated or personal data without an approved review;
    * **\[harness\]** back up the canonical setup to Drive (config only, dated) — Drive is not a runtime, database, or secret store;
    * be listed in the shared inventory (no shadow AI).
    
    It **MUST** move up a lane before any of those conditions change.
* **Change control (B1.6):** Deploying an in-scope solution, and every material change after, **MUST** follow the [Change Management Policy](https://{{WIKI_HOST}}/wiki/spaces/{{WIKI_SPACE_KEY}}/pages/{{PAGE_ID_CHANGE_MANAGEMENT_POLICY}}). For AI, a "change" includes the model or version, the prompts, the tools/connectors it can reach, its independence, and its audience. Each change **MUST**:

    * be classified (Standard / Normal / Emergency);
    * be accepted by someone other than the builder;
    * carry a documented rollback plan if it is a Major Normal or Emergency change;
    * get a post-implementation review if it is Emergency or Major Normal.
    
    **Promoting a personal tool to shared, scheduled, or system-of-record use is a Normal change.**
* **Pre-flight gate (B1.7):** Before going live, all of the following **MUST** be true:

    * the goal is defined down to its root cause;
    * data is labeled and least-privilege access is set;
    * the model and version are fixed, and prompts are tracked;
    * the solution uses approved tools only;
    * a "correct result" is defined and tested against realistic and edge-case inputs;
    * guardrails check input and output, with spend and rate caps;
    * monitoring covers result *quality* and behavior *drift*, not just uptime;
    * decisions are logged in reconstructable detail;
    * one person is named accountable;
    * the solution has been threat-modeled against the **OWASP Top 10 for Agentic Applications (2026)** — at minimum covering tool misuse, excessive agency, memory/context poisoning, and prompt injection — with identified risks either mitigated or logged as accepted exceptions;
    * there is a documented rollback and retirement path.
    
    **\[Tier 3\]** also requires adversarial stress-testing and documented approver sign-off. The solution **MUST** be registered through the standard AI-capability request.
* **Author tests in design (B1.7a) — Tier 2+ \[DRAFT — pending Security/SME sign-off\]:** For a Tier 2/3 solution, the tests that verify the pre-flight "correct result" (B1.7) **MUST** be authored as a **design deliverable — before build, in the Solution Design (B1.10)** — not first written at pre-flight. Every functional requirement and acceptance criterion in the approved AI Solution Requirements **MUST** map to at least one concrete test; **\[Tier 3\]** additionally **MUST** include adversarial tests (prompt injection, tool misuse, excessive agency, memory/context poisoning). Test fixtures **MUST** use synthetic or de-identified data — never regulated or production data. At Tier 1 authoring tests up front is **SHOULD**.
* **Exceptions and retirement (B1.8):** Any exception to a **MUST** is logged with reason, alternative safeguard, who accepted the risk, and an expiry date; recurring exceptions signal a rethink. An automation left without an owner **MUST** be retired or reassigned. *(Exceptions to change control follow the Change Management Policy's own authority.)*
* **Work-effort tracking (B1.9):** Every in-scope Tier 2+ solution **MUST** have an Epic in the work tracker (Jira in the reference configuration; substitute the equivalent tracker) in the owning team's project, opened when the AI Solution Requirements is approved (Gate 1) and before build begins, so the build effort itself is recorded — not only the outcome. The Epic **MUST** link the approved Requirements and (once it exists) the Solution Spec; child issues record the work performed, including discovery/spike work. The Epic **MUST NOT** be closed until the Solution Spec's pre-flight gate (B1.7) is complete or the effort is formally abandoned (record why). The work tracker is the authoritative record of work status and effort; no parallel task list may serve as a second source of truth. For Tier 1, an Epic (or a single tracked issue) is recommended. Solutions owned by teams participating in {{PRODUCT_TRACKER_PROJECT_KEY}} follow {{PRODUCT_TRACKER_PROJECT_KEY}}'s Epic field conventions; the {{PRODUCT_TRACKER_PROJECT_KEY}} Include flag is set only when its required fields are populated.
* **Solution Design (B1.10) — Tier 2/3 \[DRAFT — pending Security/SME sign-off\]:** A **new Tier 2/3** solution **MUST** have an approved **Solution Design** before build begins. It records: architecture and solution shape (B1.2); how each applicable Required Control is implemented; the harness (runtime, secrets, state, tools, guardrails, observability, off switch); the threat model (B1.7); rollback and retirement design; and the authored test plan (B1.7a). It follows the approved AI Solution Requirements (Gate 1) and **MUST** be reviewed by someone other than the builder (B1.6) before build. At **Tier 1** a Solution Design is **recommended, not required** — a brief "how" captured in the Solution Spec suffices. The Solution Design **does not** authorize go-live; the pre-flight gate (B1.7), recorded in the Solution Spec, governs deployment.

### **Technical Controls**

* **Secrets & credentials \[harness\]:**

    * Real passwords, API keys, and tokens **MUST NOT** appear in code, prompts, files, Drive, a Claude Project, or a repository.
    * They **MUST** live in an approved secret store or system keychain and be referenced at runtime.
    * Development and production **MUST** use separate keys.
    * Any key that can incur charges **MUST** have a spending limit and alert.
    
* **Tools, data & access:**

    * A solution **MUST** use only an approved tool list.
    * Each tool **MUST** be approved for the sensitivity label of the data it touches; a tool cleared only for public data **MUST** be technically blocked from confidential or production data.
    * Regulated or secret data **MUST** be kept out of prompts and protected by hard controls outside the model.
    * MCP servers/connectors **MUST** be IT-reviewed and scope-checked before use **\[red flag: a connector requesting more access than its job needs\]**.
    * Any connector reaching into another system **MUST** have a signed vendor agreement and Security sign-off first.
    
* **Solution behavior — Tier 2+:**

    * The **behavioral contract** — preconditions, postconditions, invariants — **MUST** be written before build (for anything beyond a single request).
    * Anything that writes, sends, moves, or deletes **MUST** be idempotent or guarded against double-execution, and **MUST** define its partial-failure and retry behavior.
    * Each system it reads from or writes to **MUST** have an explicit integration contract (schema, fields, format).
    
* **Model & environment — Tier 2+:**

    * The exact model and version **MUST** be pinned, and prompts version-controlled.
    * Development and production **MUST** be separated (credentials and data).
    * The solution **MUST** be tested in a non-production setting before go-live.
    
* **Data-quality bar:** Any solution that produces or modifies customer or reporting data **MUST** meet a data-quality bar — accuracy, completeness, validity, timeliness — proportionate to its tier. We use ISO/IEC 25012 to define this bar; we are not audited to it, but we build our framework against it.
* **Guardrails & limits \[harness\] — Tier 2+:**

    * A solution **MUST** check what goes in and what comes out, and **MUST** cap how much it can spend and how fast it can run.
    * It **MUST** treat ingested content (emails, documents, web pages, tool outputs) as untrusted, and **MUST NOT** act on instructions hidden inside material it was only asked to read (prompt injection) **\[red flag: an agent acting on instructions it found in content\]**. As of 2026 there is **no fully reliable defense against prompt injection**; input/output checks are mitigations, not guarantees, and design **MUST NOT** assume they will catch every attempt.
    * **\[Tier 2+\]** Guardrail and policy checks **MUST** be enforced **outside the agent's own code** — at the platform or gateway layer the agent cannot reason around — not by instructions in the prompt. On the reference stack this is AWS Bedrock AgentCore Guardrails and Policy enforced at the Gateway; a GCP-hosted agent (where justified by data gravity) would use the equivalent Model Armor layer. On another stack, substitute the equivalent out-of-agent enforcement layer — the requirement is the enforcement point, not the product.
    
* **Observability, off switch & rollback \[harness\]:**

    * A solution **MUST** log decisions in enough detail to reconstruct them.
    * It **MUST** monitor result quality and behavior drift, not just uptime (Tier 2+).
    * It **MUST** have a tested off switch and a documented rollback (all tiers).
    

### **Mandatory Stop-and-Report \[red flag\]**

Regardless of lane, you **MUST** stop the session and contact Security/IT if:

* an agent takes an action you didn't request;
* a secret is exposed or committed; or
* a tool demands privilege it shouldn't need.

The fuller watchlist is in Recommended Patterns below.

## **Recommended Patterns (Non-Normative)**

*Not gates — the accelerators that make the Required Controls easy to meet. **SHOULD / MAY.***

* **Earn the right to automate (strongly recommended).** Automate last. A process should already be well-run, measured, and simplified before it is mechanized. Recommended sequence:

    1. **Define** the problem down to its root.
    2. **Remove** the steps that don't earn their place.
    3. **Optimize** what remains.
    4. **Design for scale.**
    5. **Automate — with AI — last.**
    
    Automating an un-optimized process is one of the most common ways automation work fails: you mechanize the waste and lock it in. If a process isn't there yet, send it back to be improved first.
* **Use the paved roads \[harness\] (strongly recommended).** Prefer a managed, approved service over hand-built plumbing — you inherit most of the pre-flight controls by default. On the reference stack (substitute {{ORG_NAME}}'s own approved equivalents):

    * **AWS / Amazon Bedrock AgentCore** — a hosted agent runtime;
    * **Workato** — cross-system workflows;
    * **Claude Skills / Plugins** — when the capability can live inside Claude (Anthropic provides the runtime);
    * **Snowflake** — a governed data source reached under least privilege (not a host; we don't rely on Cortex);
    * **Track A** (Engineering-built, infrastructure-as-code) for production / regulated / Tier 2–3; **Track B** for internal, low-risk Tier 1.
    
    Don't stand up a second cloud just to host an agent — Google Cloud / Vertex is not a current paved road. Named services are current examples; confirm each is on the approved list with IT/Security before building.
* **Author → promote → operate (technical recommendation — SHOULD / MAY, expected to change as tooling matures).** A solution moves through three stages; use the lightest tool that fits each.

    * **Author** — design and build it. Today: Claude (Code / Cowork, org skills/plugins).
    * **Promote** — ship it from repository to runtime through an automated, reviewed pipeline. Today: GitHub Actions. The review-and-approve step — a pull request — *is* how change control (B1.6) is met, so a deployment is checked like any other code rather than hand-assembled in a console.
    * **Operate** — run it in production. Today: AgentCore (see *Use the paved roads* and *the harness at a glance* for what each runtime provides).
    
    Two pointers, not gates: keep a capability in the Claude lane while it lives inside Claude under approved connectors and a person publishes; move it to AgentCore once it must act on a system of record, run unattended, or reach Tier 2+. An SDLC agent that only proposes — e.g. code review, test-fixing — **SHOULD** run inside the pipeline and open a pull request rather than merge on its own (this is *Agent proposes, human publishes* applied to CI); a durable or acting agent SHOULD run on AgentCore.
* **Agent proposes, human publishes \[harness\] (strongly recommended for Track B agents).** Keep a person at the decision point — let the agent *propose* the change and a person *publish* it. A self-healing data-importer service is the model example: its agent can propose code changes but cannot publish them itself.
* **Keep it light where the tier is light (recommended).** Outside the required items, prefer a sentence over a sub-form, and "N/A — why" over a blank. The record should be something a reviewer can act on, not paperwork for its own sake.
* **Red-flags watchlist \[red flag\] (recommended practice).** None of these is cause for panic, but each is worth a quick message to Security or IT — a false alarm costs little, a missed one costs a lot:

    * A tool or script asks for admin/`sudo` access you weren't expecting.
    * A password or key ended up committed to a repository.
    * An agent accessed files, sent something, or took an action you didn't request.
    * An unfamiliar program shows up in startup items or background processes.
    * AI-generated code connects to a domain or address you can't explain.
    * A local tool or agent burns unusual CPU or memory for no clear reason.
    * A personal tool you built is suddenly used by colleagues or feeding a shared system — a governance trigger (re-govern it), not just a security one.

### The harness at a glance \[harness\]

| Harness piece | Local (macOS + Drive) | Claude (Skills / Plugins) | Track B (cloud, Tier 1) | Track A (cloud, Tier 2–3) |
| --- | --- | --- | --- | --- |
| **Execution** | Approved AI client's loop | Claude's own loop (Anthropic-managed) | Workato, or AgentCore runtime | AgentCore on IaC |
| **Secrets** | macOS Keychain | None in skill files; connector auth | AWS Secrets Manager | Centrally managed secrets |
| **State / memory** | Drive (config backup only) | Claude context + connector data | Managed memory or small store | AgentCore Memory |
| **Tools / data** | Single working folder | Approved MCP connectors only | Approved connectors; Snowflake read/write | Least-privilege to system of record |
| **Guardrails** | You review before confirming | Connector scoping + human review | Input/output checks + caps | Managed guardrails + Policy |
| **Observability** | Your own notes / logs | Claude surface + connector logs | CloudWatch | Full tracing + quality monitoring |
| **Cost control** | Capped dev key | Plan / usage limits | Budget alerts + per-key limits | Budget controls + rate caps |
| **Off switch** | You (manual) | Disable skill/plugin; revoke connector | Disable runtime / job | Tested kill switch + rollback |

## **Reporting Violations**

It is the responsibility of all in-scope individuals to follow the requirements of this standard and to report any observed or suspected non-compliance — including the stop-and-report conditions above — to your manager or to [{{SECURITY_CONTACT_EMAIL}}](mailto:{{SECURITY_CONTACT_EMAIL}}).

## **Monitoring and Enforcement**

* The shared AI solution inventory, change records, and solution decision logs are the primary monitoring surface for this standard.
* Security and the function led by the {{AUTOMATION_LEAD_ROLE}} may review in-scope solutions for conformance.
* A solution found materially non-compliant may be required to pause or be disabled until it meets the Required Controls.

## **Review and/or Audit Schedule**

* This standard will be reviewed at least once per calendar year.
* This standard may be reviewed after major incidents or major model / platform / tooling changes.
* This standard tracks the evolving agentic-standards landscape as a standing review trigger. NIST's Center for AI Standards and Innovation (CAISI) formally launched its AI Agent Standards Initiative on February 17, 2026, and OWASP's agentic guidance is updated frequently; a material update to either is grounds for an off-cycle review.
* Control checks will be conducted annually.

## **Acknowledgement and Agreement**

Acknowledgement and agreement of the terms in this standard occurs when either:

* An employee or contractor signs the {{ORG_NAME}} Risk Management Policy Acknowledgment and Acceptance Agreement;
* A contractor signs their contract to work with {{ORG_NAME}}; or
* An employee or contractor affirms they accept updated policies via an annual review.

Any attempts to intentionally circumvent or bypass the requirements of this standard will be investigated, and may result in disciplinary action.

# **Further Detail**

For further detail or to ask any questions you may have, please contact [{{SECURITY_CONTACT_EMAIL}}](mailto:{{SECURITY_CONTACT_EMAIL}}) or the function led by the {{AUTOMATION_LEAD_ROLE}}.

Updates to this document will be provided via standard company communication channels.

# **Exceptions**

Log exceptions in the Security Exceptions Register with compensating controls (e.g., a tighter scope, additional monitoring, or a shorter review interval), the person who accepted the risk, and an expiry date. Recurring exceptions to the same control signal that the design — or the control — should be revisited. Exceptions to change control follow the [Change Management Policy](https://{{WIKI_HOST}}/wiki/spaces/{{WIKI_SPACE_KEY}}/pages/{{PAGE_ID_CHANGE_MANAGEMENT_POLICY}})'s own exception authority.

# **Terms and Terminology**

* **Workflow:** an automation that follows a fixed, pre-mapped set of steps. Predictable; the right shape for a standard process.
* **Agent:** an automation that decides its own next step toward a goal. More flexible, less predictable; raises the tier.
* **Multi-agent / orchestrator:** several agents coordinated by a controlling agent. Powerful but costly and hard to predict; out of bounds for non-product work without Engineering and Security.
* **Subagent:** a helper agent invoked by another to handle a narrow task.
* **Harness:** the scaffolding around the model — runtime, secrets handling, state/memory, tools, guardrails, logging, cost controls, and the off switch. Most safety lives in the harness, not the model.
* **Tier (1 / 2 / 3):** the risk level of a solution, set by the worse of potential harm and degree of independence.
* **Human-in-the-loop:** a person approves each important action before it happens.
* **Human-on-the-loop:** the automation runs while a person monitors and can intervene.
* **System of record:** the authoritative source for a piece of data (e.g., the system other teams trust as "the truth").
* **Gateway:** the enforcement point between an agent and the tools or data it reaches, where access policies and guardrails are applied outside the agent's own code. Routing every tool and context call through one gateway lets a single control layer govern all of an agent's capabilities.
* **Least privilege:** granting only the minimum access needed to do the job.
* **Idempotent:** safe to run more than once without causing duplicate or compounding effects.
* **Behavioral contract:** the written preconditions, postconditions, and invariants a solution must hold to.
* **Integration contract:** the agreed schema, fields, and format for a system a solution reads from or writes to.
* **Model / version pinning:** fixing the exact model and version a solution uses, so behavior doesn't change underneath it.
* **MCP (Model Context Protocol) server / connector:** a component that lets an AI solution reach an external system or data source.
* **Prompt injection:** hidden instructions placed inside content the model reads, intended to make it act against the user's intent.
* **Paved road:** a managed, approved platform that carries most controls by default, so builders inherit them rather than rebuild them.

# **Changelog**

‌

| Version | Date | Description | Author | SME Reviewed and Approved | Approved |
| --- | --- | --- | --- | --- | --- |
| 0.7 (DRAFT) | `<date>` | **Pending Security/SME sign-off.** Added the staged/gated pipeline description (POC Stage 0 → Requirements Gate 1 → Solution Spec → Solution Design → build → deploy) and two new Required Controls: **B1.7a** (author tests as a design deliverable, Tier 2+) and **B1.10** (Solution Design required for a new Tier 2/3 solution). NIST Measure row updated to reference authored tests. No existing control weakened. | `@{{AI_GOVERNANCE_OWNER}}` |  |  |
| 0.6 | `<date>` | Aligned to house standards template (Endpoint Security Standard pattern): added Classification / Owner / Effective Date header, Purpose with ISO 27001 Annex A mappings, informed-by / informs, Scope, Roles and Responsibilities, and standard footer sections (Reporting Violations, Monitoring and Enforcement, Review/Audit, Acknowledgement, Further Detail, Exceptions, Terms and Terminology, Changelog). Restructured body into Guiding Principles / Standards (Required Controls) / Recommended Patterns. Drafting provenance tags removed; \[harness\] and \[red flag\] retained. | `<{{AUTOMATION_LEAD_ROLE}} / {{SECURITY_LEAD_ROLE}}>` |  |  |
| 0.5 | `<date>` | Restructured into Part A Principles / Part B Hard standards / Part C Recommended patterns; deduplicated against the AI Use Framework Guide; requirement lists bulleted. | `@{{AI_GOVERNANCE_OWNER}}` |  |  |

‌
