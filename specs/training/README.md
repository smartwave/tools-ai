---
title: "AI Training Program — Specs"
type: index
status: draft
created: 2026-09-03
---

# AI Training Program — Specs

Specs for a set of AI trainings. Two are drafted; two are on the roadmap.

| # | Training | Audience | Status | Spec |
|---|---|---|---|---|
| 1 | Understanding AI | All employees, no technical floor | Draft v0.1 | [[training-01-understanding-ai-spec]] |
| 2 | AI in This Organization | All employees, single track | Draft v0.1 | [[training-02-ai-in-this-organization-spec]] |
| 3 | Building AI Solutions | Builders | Planned | — |
| 4 | AI for Managers | People leaders | Planned | — |

Training 1 is a prerequisite for Training 2. Trainings 1 and 2 are single tracks with no audience splits — builder and manager content was deliberately pulled out rather than layered in, because content that presumes you are building does not survive contact with an audience that is not.

## Shared design principles

**Backward design.** Behaviour change first, then assessment, then content. "Understands AI" is not an outcome; "can tell whether a task is safe to hand to an agent" is.

**One misconception per module.** Adults learn by having a wrong model corrected, not a blank filled. Every module names the belief it is killing.

**Scenario judgment, not recall.** Assessment asks what you would do, never which of these is a large language model.

**Cards, not two documents.** Each module ends in a one-paragraph standalone card. The cards concatenated are the written reference. Nobody re-reads a course; they re-read a card. Generating the reference from the training is what stops the two from drifting apart.

**Transcripts replace the demo.** With no facilitator, annotated real exchanges are the only way to show behaviour rather than describe it. This is the highest-effort production item in both specs and the one that decides whether they land.

**Volatile content lives outside.** Tool lists, figures, approver names and examples update without reissuing the training.

**Training is the 10%.** Neither training works without job aids and reinforcement. Both end in a real task rather than a quiz, because completion of one real task is what converts to use.

## Format

Both trainings are async self-paced plus written reference. No live or instructor-led component.

## Framework basis

Training 2 is built on the Human-Centered Automation & AI framework — the scope ladder, the five-tier risk model, and the gates — then genericized with `{{PLACEHOLDER}}` tokens. Its §8 records what transfers to another organization unchanged, what transfers as structure needing local values, and what must be supplied locally.

## Next

- Fill the placeholder register in Training 2 §6 for the first adopting organization.
- Commission the eight annotated transcripts for Training 1 §7.
- Decide the hosting platform; both specs have an open question on whether it supports per-answer self-check feedback.
