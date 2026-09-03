<!--
CANONICAL SOURCE OF TRUTH.
This file is the authoritative version of the {{ORG_NAME}} AI Use Framework Guide.
The wiki renders FROM this file (GitHub -> wiki, one-way; Confluence is the reference
configuration and another wiki can be substituted). Do not hand-edit the Confluence copy.
Edit here, open a PR, merge -> the org marketplace re-syncs and the wiki page is
regenerated. The ai-requirements-doc-author skill reads this file at runtime so its
guidance always reflects the current policy. Keep section names stable; the skill
refers to them.
Published page: https://{{WIKI_HOST}}/wiki/spaces/{{WIKI_SPACE_KEY}}/pages/{{PAGE_ID_AI_USE_FRAMEWORK}}
-->

# {{ORG_NAME}} AI Use Framework Guide: Using AI Safely to Work Faster

_Audience: every {{ORG_NAME}} employee, especially non-engineers. Reading level: third-year collegiate (junior)._

**Owners:** {{AI_GOVERNANCE_OWNER}}, {{BUSINESS_TECHNOLOGY_LEAD}}
**Version:** 0.4 (proposed draft)
**Governed by:** the Artificial Intelligence (AI) Policy, the Data Management Policy, and the Change Management Policy.

## Why this matters: better work, not merely safer work

Read this as how good AI practice pays off, not as a list of restrictions. Used well, AI raises how much you get through, improves what you produce, and hands you the drudgery while leaving you the judgment — and customers feel that as more reliable output. The key point: safety and quality are the same discipline. The habits that keep you out of trouble — defining the problem, reading the output, knowing where the data goes — are exactly the ones that make the output good. The goal is _sustainable speed_: the fastest _good_ path, which beats the merely fastest one over any real horizon.

## The governing idea: you author the intent, the model executes it

AI is a power tool, not a coworker. You author the intent — what to build, what "correct" means, which trade-offs are acceptable — and the model executes against it. The engineering org puts it bluntly: _don't outsource the thinking._ Hand the model a well-formed problem and it amplifies your judgment; let it originate the plan and the result drifts toward the generic while your own skill quietly atrophies.

## Own the output as if it were entirely your own — verify all AI-generated content

Generative models produce fluent, confident prose that can still be wrong — a failure mode called hallucination — so the human who uses an output, not the tool, owns the result. Hold to one standard: **you are just as accountable for what AI produces as when you relay a Google search result or work you did by hand.** If it goes out under your name or into a decision, you own its correctness, and "the AI said so" is never an answer. Read every output before you rely on, publish, or act on it, and ask: _if this were wrong, who would catch it, and when?_

## Keep a human in the loop — and be deliberate about where

This is the non-negotiable that underwrites the rest: **never put the human fully out of the loop.** AI may draft, triage, summarize, and recommend, but a person reviews and approves before any consequential action takes effect — a message sending, a record changing, money moving, output reaching a customer. Be deliberate about _where_: not every step needs a checkpoint (littering low-stakes work with approvals only teaches rubber-stamping), but consequential and irreversible steps always do. Own accountability for anything you approved that later proves wrong.

## The non-negotiables — {{ORG_NAME}}'s core rules for using AI

If you internalize nothing else, internalize these four:

1. **Keep a human in the loop on anything consequential** — and never fully out of it.
2. **Own and verify every output** before it informs a decision, is published, or reaches a customer.
3. **Protect sensitive data:** use approved, company-managed tools for anything non-public, and never enter customer data, personal data, or anything **Confidential** or **Restricted** into an unapproved public tool.
4. **Report incidents immediately** — any suspected data leak, security issue, or material inaccuracy — to {{SECURITY_CONTACT_EMAIL}}.

_Which tool is cleared for which data is covered in "AI at {{ORG_NAME}}" and the "Getting Started Guide": match the tool to the sensitivity of the data, and use company-managed accounts for any non-public work._

## What good practice looks like — and why it pays

The habits that keep AI use safe are the same ones that make it productive — your operating model, not constraints:

* **Automate the drudgery and standard decisions; keep the high-risk judgment.** Give the model the repetitive scaffolding and first drafts, and keep the design decisions and final call for yourself. Faster _and_ more engaging work.
* **Invest in the input.** A well-framed problem with the right context beats a one-line request — the few minutes spent framing are the highest-return minutes in the task.
* **Build reusable patterns, not heroic one-offs.** When a prompt or workflow works, save and share it so good practice compounds across the team.
* **Calibrate trust to the risk.** Move fast where mistakes are cheap and you'd catch them at once; slow down to verify where you wouldn't.

## Protect credentials, and treat inputs as untrusted (OWASP AI Top 10)

Never paste passwords, API keys, or tokens into a prompt, and never store them in a shared Drive folder or Claude Project — a shared secret is a disclosed secret. If an automation must authenticate, request a scoped, least-privilege credential from IT rather than reusing your personal login. Treat any content the model ingests — emails, documents, web pages — as untrusted: it can carry hidden instructions (prompt injection), and the model must never act on directions buried in material it was only asked to read.

## Before you build a solution: map the work first, then keep it simple

Most of the time you'll use AI inside a tool someone else built. But sometimes you'll _build_ something yourself — a reusable prompt, a small automation, a process that runs on its own. When you do, map the work as a series of steps _on paper, before you pick any tool._ It's the cheapest way to avoid rework and stay out of trouble — the same governing idea as elsewhere, _you author the intent,_ applied one step earlier.

For each step, ask: does the outcome follow fixed, predictable rules (a **standard process**), or does it need judgment you can't spell out in advance (**a decision**)? Predictable steps should run as a fixed, step-by-step workflow — most accuracy, most control, lowest cost. Only steps that truly need open-ended judgment justify letting the AI decide its own path. Add complexity only when the work forces it; most business needs are standard processes, so the simplest build is usually right.

* **Map first, build second.** Sketch the whole process before choosing a tool — the map makes every other question answerable.
* **Note the data each step touches, and match the tool to its sensitivity** (non-negotiable #3). A clever build on the wrong tool is still a data incident.
* **Prefer the simplest pattern that does the job,** moving up only when the one below can't: a single AI request -> a fixed workflow -> an agent (AI deciding its own steps) -> multiple coordinated agents. Each step up adds cost, unpredictability, and review burden — earn it.
* **Test by reversibility, not cleverness:** _if this ran wrong, who'd catch it, and when?_ Costly or hard to undo -> keep a person in the loop and keep it a fixed workflow.
* **More freedom means more exposure.** The more tool access and autonomy an AI has, the more prompt injection can mislead it — another reason to keep self-directed agents rare and reviewed.
* **You're not deciding alone.** Anything that runs without a person checking each result, is used by others, or feeds a system of record goes through IT and Security _before_ it goes live. When in doubt, ask first: {{SECURITY_CONTACT_EMAIL}} or an IT helpdesk ticket.

**Plain-language definitions:**
- **Workflow** — fixed steps you design; the AI fills in each but doesn't choose the order (most builds should be this).
- **Agent** — the AI directs itself, using tools in a loop until done; best for open-ended work you can't map ahead, and the pattern that most needs review.
- **Multiple coordinated agents (orchestrator and subagents)** — a "lead" AI splits a job among helper AIs and combines the results; powerful but costly and unpredictable, and an advanced pattern to design _with_ IT.
- **Harness** — the controls, limits, logging, and checks around the model that keep a solution reliable and safe to run.

## Personal use, shared use, and the silent-promotion trap

A personal tool you alone review is low-risk because _you_ are the validation layer. That changes the instant others depend on the output, it feeds a system of record, or it runs without a human checking each result — yet the controls often don't follow. This is the _silent-promotion trap_: a personal helper quietly becomes load-bearing infrastructure without being re-governed. Re-classify and escalate to the deployment standard **before** the new use begins, not after an incident makes the case for you.

## What we recommend

Three habits. First, treat every AI output as your own work product — read it, own it, and stay in the loop wherever stakes are real. Second, invest in the input, since a sharper problem statement and better context are the cheapest route to better output and the reason the work goes faster. Third, when something works, capture it as a reusable pattern — and when a personal tool starts serving others, pause and route it through IT and Security. When in doubt, ask before you act: Security would far rather answer a question than remediate a leak — {{SECURITY_CONTACT_EMAIL}} or an IT helpdesk ticket.
