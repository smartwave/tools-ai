---
title: "Training 1 — Understanding AI"
type: training-spec
status: draft
version: 0.1
created: 2026-09-03
audience: all employees, no technical floor
format: async self-paced + written reference
related: ["[[training-02-ai-in-this-organization-spec]]", "[[ai-governance-framework]]"]
---

# Training 1 — Understanding AI

## 1. Problem

People form a mental model of AI from using it, and the model they form is usually wrong in a specific way: they treat it as a system that knows things and will tell them when it doesn't. Every downstream mistake — over-trust, under-use, bad delegation, skipped verification — traces back to that model.

This training replaces the model. It is not a tool tutorial and not a governance course.

## 2. Outcome

After this training a learner can:

1. Explain, in their own words, why AI can be fluent and wrong at the same time.
2. Identify what the AI can and cannot see in any given task.
3. Tell whether they are using chat, a tool, or an agent, and say what changes at each step.
4. Recognise the six common failure modes in output they receive.
5. Scope a task for AI the way they would brief a capable new colleague.
6. State which part of the work is still theirs.

Non-goals: how models are trained, what a token is, prompt-engineering technique, tool-specific instructions, organisational policy.

## 3. Audience and prerequisites

All employees. No technical floor. Assumes the learner has seen a chat AI at least once and has formed opinions about it — the content is corrective, not introductory.

No prerequisites. This training is the prerequisite for Training 2.

## 4. Format

- Async self-paced, eight modules of five to seven minutes. ~50 minutes total.
- Each module ends with a **card** — a one-paragraph standalone version.
- The eight cards concatenated are the written reference document. The reference is generated from the training, not written separately, so the two cannot drift apart.
- Self-checks are ungraded and explain why each wrong answer is tempting.
- No live component, no facilitator. Everything a facilitator would demonstrate is carried by annotated transcripts.

## 5. The spine

One metaphor runs through all eight modules: **AI is an incredibly capable, incredibly eager intern.** Brilliant, fast, willing, and on their first day. Humans get their risk boundaries from the physical world — you can see the shredder, you know whose desk that is, you know what "expensive to break" looks like. AI has no physical world. Every boundary it has, someone supplied digitally.

Module 4 breaks the metaphor on purpose. A metaphor that is never falsified becomes a belief.

## 6. Modules

### Module 1 — It predicts, it doesn't know

- **Objective:** explain why AI can be confidently wrong.
- **Misconception killed:** "It looked it up."
- **Key points:** it produces the most plausible continuation, and plausible is not the same as true; fluency is not a confidence signal; there is no internal fact-check step; it is not consulting a database unless someone connected one.
- **Worked example needed:** a request for a source or citation that returns a plausible, well-formatted, non-existent one.
- **Card:** what it does and why that explains almost every surprise.
- **Self-check:** given four outputs, which is most likely fabricated and what tipped you off.

### Module 2 — The eager intern

- **Objective:** describe what the AI brings to a task and what it does not.
- **Misconception killed:** "It should have known."
- **Key points:** capable, fast, and willing; day one; no badge, no org chart, no history, no sense of what is expensive to break; it will not stop to ask unless asked to; the boundaries are yours to supply.
- **Worked example needed:** "clean up the customer list" — an instruction a capable person would query and an eager one would execute.
- **Card:** the intern framing, stated once, cleanly.
- **Self-check:** an instruction with three unstated assumptions; name them.

### Module 3 — Context is the whole job

- **Objective:** identify what the AI can and cannot see in a given task.
- **Misconception killed:** "I told it that yesterday."
- **Key points:** it knows only what is in the room; the context window and what falls out of it; memory features are a room someone furnished on purpose, not recall; pasted documents versus connected systems; more context is not better if it is the wrong context.
- **Worked example needed:** the same prompt run with and without the relevant document, side by side.
- **Card:** what is in the room.
- **Self-check:** for a described task, list what the AI would need supplied.

### Module 4 — Where the metaphor breaks

- **Objective:** state the two ways AI is unlike an intern, and what that means for review.
- **Misconception killed:** "It will get better as it learns me."
- **Key points:** a real intern accumulates context over months and knows when they are lost; this does neither reliably; its certainty is uncorrelated with its accuracy; therefore verification is not politeness, it is the part of the job that did not get automated.
- **Worked example needed:** two answers, one hedged and correct, one certain and wrong.
- **Card:** the two breaks, and the reviewing habit they require.
- **Self-check:** which of these outputs would you sign your name to as-is.

### Module 5 — Chat, tools, agents

- **Objective:** tell which of the three you are using and say what changes.
- **Misconception killed:** "It's just a chatbot."
- **Key points:** chat — it talks, you act; tools — it acts, one step, because you asked; agents — it chooses the sequence and keeps going; consequence scales at each step, and so does the need to set boundaries before rather than during.
- **Worked example needed:** one task shown at all three levels.
- **Card:** the three levels and the question to ask at each.
- **Self-check:** classify four described setups.

### Module 6 — How it fails

- **Objective:** recognise the six failure modes in output you receive.
- **Misconception killed:** "It will say if it's unsure."
- **Key points, as intern behaviours:** makes things up rather than come back empty-handed; agrees with your premise (tell it the number looks low and it will find reasons the number is low); drifts over a long conversation; finishes eight of ten rows and reports success; believes whatever it reads, and cannot reliably tell your instruction from text inside a document you handed it; does more than you asked.
- **Worked example needed:** one annotated output with several failures marked in place.
- **Card:** the six, named, in plain language.
- **Self-check:** label the failure mode in each of six short excerpts.

### Module 7 — Your job changed

- **Objective:** scope a task the way you would brief a person.
- **Misconception killed:** "AI replaces the thinking."
- **Key points:** the work moves from doing to directing — problem, outcome, inputs, acceptance criteria, feedback point; the person who defines the problem well beats the person with the clever prompt; deciding what "good" looks like is not delegable.
- **Worked example needed:** a vague brief and a scoped brief, with both results shown.
- **Card:** the five things to state before you start.
- **Self-check:** rewrite a vague brief.

### Module 8 — Try it

- **Objective:** complete one real task.
- **Not a quiz.** Pick something from this week, scope it using Module 7, run it, note the one place you had to correct it.
- Completion is self-reported. The point is conversion to use, not measurement.

## 7. Production requirements

| Item | Count | Notes |
|---|---|---|
| Annotated transcripts | 8 | Highest-effort item. Real prompts and real outputs, lightly edited. Decides whether the training lands. |
| Cards | 8 | Become the reference document. |
| Self-checks | 7 | Each wrong answer needs an explanation of why it is tempting. |
| Module scripts | 8 | 700–900 words each at five to seven minutes reading. |

Accessibility: plain language, no jargon without definition in the same sentence, every visual carries its meaning in text as well.

## 8. Maintenance

Modules 1 through 7 are durable — they describe behaviour that has held across model generations and should need review annually, not quarterly.

Module 8 and any tool names mentioned anywhere are volatile. Keep tool names out of Modules 1 to 7 entirely so the concepts do not expire when the tool list changes.

## 9. Open questions

- Which platform hosts the async modules, and does it support ungraded self-checks with per-answer feedback?
- Are the transcripts drawn from real internal use, which is more persuasive but needs clearance, or constructed?
- Is completion tracked, and does anything depend on it?
