---
title: "Training 2 — AI in This Organization"
type: training-spec
status: draft
version: 0.1
created: 2026-09-03
audience: all employees, single track
format: async self-paced + written reference
prerequisite: "[[training-01-understanding-ai-spec]]"
related: ["[[ai-governance-framework]]"]
---

# Training 2 — AI in This Organization

A reusable template. Built on the Human-Centered Automation & AI framework, genericized with `{{PLACEHOLDER}}` tokens for anything an adopting organization must supply.

## 1. Problem

Two failures, not one.

**Under-use.** People do not know what they are allowed to do, so they do nothing, and the organization pays for capability it does not get. This is the more expensive failure and the one most governance training makes worse.

**Ungoverned use.** People build something useful, it quietly becomes load-bearing for other people, and it never passes a gate because nobody knew there was one.

This training addresses both. If it reads as a rulebook, it has failed.

## 2. Outcome

After this training a learner can:

1. Name what they are expected and encouraged to do with AI at `{{ORG_NAME}}`, and what budget they have to do it.
2. Choose the right approved tool for a task.
3. Point to a worked example of AI applied to work resembling their own.
4. Decide what data may go into which tool.
5. Place a piece of work on the scope ladder.
6. Identify the risk tier of a piece of work and say where the human stands in it.
7. Recognise when a personal helper has become something others depend on, and what to do at that moment.
8. State what they are accountable for and how to report a problem.
9. Complete one real task with an approved tool.

Non-goals: how AI works — that is Training 1, a prerequisite; build standards, gate mechanics, and evaluation — deferred to the builder training; team-level decisions — deferred to the manager training.

## 3. Format

Single track, all employees. Async self-paced, ten modules, ~40 minutes. Card per module, cards concatenate into the reference document. Ends in a real task and an attestation.

**Ratio discipline.** Modules 1, 3, 9 and 10 are enablement; 4, 5, 6, 7, 8 are constraint. If constraint modules come to outnumber enablement modules, the felt message becomes "be careful" regardless of what Module 1 says. Any module added to this training must be counted against that ratio.

## 4. Modules

### Module 1 — What you're expected to do with this

- **Objective:** state what you are encouraged to do and what you have to spend.
- **The opening is the whole design decision.** It leads with the invitation, not the rules. A governance training that opens with prohibitions teaches one lesson — the safe answer is to ask permission — and no later module recovers from it.
- **Key points:** `{{ORG_NAME}}` expects you to use these tools in your daily work; `{{ALLOWANCE_STANDARD}}` per month is yours without a business case, `{{ALLOWANCE_CREATOR}}` if you are building; the rules that follow exist to let you move quickly without stepping on something expensive, and most of what you want to do needs no approval at all.
- **Card:** the invitation and the allowance, in five sentences.

### Module 2 — Approved tools and what each is for

- **Objective:** choose the right tool for a task.
- **Key points:** the tool taxonomy — what each approved tool is for, what it is bad at, and what it costs. `{{TOOL_TABLE}}`
- **Volatile.** This content lives in the appendix, not the module body. See §7.
- **Card:** the one-line selection heuristic.

### Module 3 — What good use looks like here

- **Objective:** find a worked example resembling your own work.
- **The behaviour-change module.** Abstract encouragement changes nothing; six to eight concrete examples of real `{{ORG_NAME}}` work, with the prompt and the result shown, changes behaviour. Cover a spread of functions so most learners find themselves in at least one.
- **Key points:** `{{USE_CASE_GALLERY}}` — each example gives the task, the prompt, the output, and the correction the person had to make.
- **Volatile, and improving.** These get better every quarter. Ship version one with placeholder examples rather than delaying, and run the gallery as a living page the training links to rather than content frozen inside it.
- **Card:** where the gallery lives and how to add to it.

### Module 4 — Data rules

- **Objective:** decide what data may go into which tool.
- **The most-referenced content in the training.** People screenshot this. Write it to be screenshotted: one table, classification down one axis, approved tools across the other, and a plain sentence for the ambiguous cases.
- **Key points:** `{{DATA_CLASSIFICATION_SCHEME}}` mapped to `{{TOOL_TABLE}}`; what to do when you are not sure; why "I removed the names" is usually not enough.
- **Card:** the table.

### Module 5 — The scope ladder

- **Objective:** place a piece of work on the ladder.
- **Key points:** build for me → share with my team → build for my team → deploy for my team → build cross-functional workflows → deploy cross-functional workflows → managed deployments with feedback loops. Obligations rise with each rung. "Where does this sit?" is the single question that routes everything else in this training.
- **Portable.** The ladder transfers to any organization essentially unchanged.
- **Card:** the seven rungs and the routing question.

### Module 6 — Risk tiers and where the human stands

- **Objective:** identify the tier of a piece of work and the human's position in it.
- **Key points, from the framework's five-tier model:**
  - T1 — built for and used by one person.
  - T2 — AI reads, then recommends or drafts, for multiple people. Human in the loop.
  - T3 — the same read-and-recommend, triggered by something other than a person. Human on or out of the loop.
  - T4 — AI writes to a system on a person's behalf, no self-directing agent. Human in the loop by construction.
  - T5 — agentic writes, triggered without a person. Human on or out of the loop.
  - A draft or a proposed change is a proposal, not a write.
  - Data sensitivity and consequence sit on top of the grid and can raise any tier.
  - Anything that needs a person's authorization to proceed is human-in-the-loop. If the AI needs a human decision, that is human-in-the-loop.
- **Plain-language rule:** define human in / on / out of the loop in ordinary words the first time each appears. Most of this audience has never met the terms.
- **Distinctive.** This tier model is `{{ORG_NAME}}`'s own. Adopting organizations should keep the structure and replace only the thresholds and approver roles.
- **Card:** the five tiers in one table, plus the overrides.

### Module 7 — When your helper becomes everyone's

- **Objective:** recognise the moment a personal tool becomes shared, and know what to do.
- **The most likely real failure in year one,** and it is not a builder's failure — it is an ordinary person's script or prompt that six colleagues came to depend on without anyone deciding it should happen.
- **Key points:** the silent promotion, taught as a named scenario; the signals that it has happened — someone else runs it, someone else's decision rests on it, it writes somewhere that matters, it runs without you; what to do at that moment, which is `{{PROMOTION_ENTRY_POINT}}`, not stop.
- **Also carries the builder framing in short form:** the tools arriving at your desk are non-player characters somebody designed. Designed well they save the day; designed badly they do not help, or they harm. If you want to build one, there is a path with gates on it — `{{BUILDER_TRAINING_LINK}}`.
- **Card:** the four signals and the one thing to do.

### Module 8 — Your obligations

- **Objective:** state what you are accountable for.
- **Key points:** you own the output you pass on, including the parts you did not read; `{{DISCLOSURE_POLICY}}` — when to say AI was involved; `{{INCIDENT_REPORTING}}` — how to report it when it goes wrong, and the assurance that reporting early is not punished.
- **Tone note:** written as professional accountability, not liability transfer. If this module reads as the organization protecting itself from the learner, Module 1's invitation is retroactively cancelled.
- **Card:** the three obligations.

### Module 9 — Getting help and getting unstuck

- **Objective:** know where to go.
- **Key points:** `{{SUPPORT_CHANNEL}}`; `{{APPROVAL_PROCESS}}` and expected turnaround; what to do when the tool disappoints you the first time, which is the moment most people quit permanently — this is enablement content, not support content, and it belongs in this training rather than a help page.
- **Card:** where to go, for what.

### Module 10 — Your first task

- **Objective:** complete one real task with an approved tool.
- Pick something from this week, choose a tool using Module 2, check it against Module 4, run it, save the result.
- **Strongest lever in the training.** People who complete one real task convert to use; people who pass a quiz do not.
- Followed by the scenario assessment and attestation.

## 5. Assessment and attestation

Five to six scenarios, scored, attestation on pass. Scenario judgment rather than recall — nobody needs to recite a tier definition, they need to place a real request.

Coverage: one data-classification call; one scope-ladder placement; one tier identification; one silent-promotion recognition; one "this is fine, go ahead, no approval needed" case.

That last one is not filler. An assessment where every correct answer is caution teaches caution as the correct answer.

## 6. Placeholder register

| Token | Supplied by | Volatile |
|---|---|---|
| `{{ORG_NAME}}` | adopting org | no |
| `{{TOOL_TABLE}}` | IT / security | yes |
| `{{DATA_CLASSIFICATION_SCHEME}}` | security | no |
| `{{ALLOWANCE_STANDARD}}` / `{{ALLOWANCE_CREATOR}}` | finance / program owner | yes |
| `{{USE_CASE_GALLERY}}` | program owner | yes, continuously |
| `{{DISCLOSURE_POLICY}}` | legal / comms | no |
| `{{INCIDENT_REPORTING}}` | security | no |
| `{{SUPPORT_CHANNEL}}` | program owner | yes |
| `{{APPROVAL_PROCESS}}` | program owner | yes |
| `{{PROMOTION_ENTRY_POINT}}` | program owner | no |
| `{{BUILDER_TRAINING_LINK}}` | program owner | no |

## 7. Volatile appendix

Everything marked volatile above lives in a separate appendix that updates without reissuing the training or re-running attestation. Tool names, allowance figures, approver names, turnaround times, and the use-case gallery.

Rationale: a governance reference containing a stale tool list is wrong within a quarter, and people who catch it being wrong once stop trusting all of it.

## 8. What is portable and what is not

**Transfers unchanged:** the scope ladder; the module sequence and the enablement-first opening; the silent-promotion scenario; the ratio discipline.

**Transfers as structure, needs local values:** the five-tier risk model; the gates; the allowance model.

**Must be supplied locally:** tool table, data classification, approval routing, use-case gallery.

## 9. Open questions

- Does attestation renew annually, and does a volatile-appendix change ever trigger re-attestation?
- Who owns the use-case gallery once the training ships? Without a named owner it stops being living content within two quarters.
- Does Module 1's allowance statement need finance sign-off before the training can quote a figure?
