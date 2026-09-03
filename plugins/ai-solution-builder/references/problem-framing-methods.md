# Problem-framing methods — Stage 0 reasoning guidance

*Plugin-internal guidance read by `ai-problem-framer` (all three phases), `ai-poc-brief-author`,
and `ai-poc-summary-author`, and inlined into the five Gemini Gems in `../gems/`. Not a
wiki-synced document. It implements the AI Use Framework's "Before you build a solution: map the
work first" section and the Standard's "Earn the right to automate" pattern (Define → Remove →
Optimize → Design-for-scale → Automate) for the pre-gate stage.*

## The rule that governs every method here: guide, never author

The person authors the problem, the root cause, and the future state **in their own words**. The
AI tool asks questions, offers methods, holds up examples, and points out gaps. It does not write
the substance for them. This is the Framework's governing idea ("you author the intent, the model
executes it") applied one step earlier than the Requirements document — and it matters more here,
because a problem an AI invented is the fastest route to a solution nobody needed.

Operationally:

- If the person gives a topic and no content, respond with **questions**, not a draft.
- Offer *structures* (a 5W1H table, a Whys chain, a set of lenses) and *examples from other
  domains*; never fill the structure with a guess about their situation.
- Sharpen what they wrote: tighten, make specific, surface what is missing. Hand it back for them
  to accept, edit, or reject. Their acceptance is what makes the words theirs.
- Nothing is written into the brief until the person confirms the wording.

---

## Part A — Problem statement

### A1. 5W1H: the six questions a problem statement must answer

| Question | What it pins down | Ask it like this |
|---|---|---|
| **Who** | Who experiences the problem; who else is affected | "Who feels this first? Who feels it next?" |
| **What** | What actually happens (the observable event), not the missing tool | "What do you see happen? Describe the last time." |
| **When** | When it occurs; frequency; trigger | "When did it last happen? How often? What sets it off?" |
| **Where** | The process step, system, team, or location | "Where in the process does it show up?" |
| **Why it matters** | The impact — cost, delay, risk, quality, morale | "What does it cost when it happens? To whom?" |
| **How** | How it currently shows up / how it is currently handled | "How is it dealt with today? How do you know it happened?" |

A statement that answers all six in one or two sentences is nearly always specific enough to
work on. One that cannot answer *when* or *where* is usually not a problem yet — it is a feeling
about a problem, and needs observation first.

### A2. Slice the loaf: when the problem feels too big

If the 5W1H answers sprawl — several *whos*, several *wheres*, a *what* that is really three
things — the problem is a loaf, not a slice. A POC and an IT proposal both need a slice.

- Pick **one** who, **one** where, **one** what. Name the slice explicitly ("vendor invoices from
  the top five suppliers, in the AP step, for the finance analysts").
- The other slices are not lost: list them in one line as "not in this slice", so the reader
  knows the loaf exists.
- A good slice is one that, if solved, the person would notice within a month.

### A3. The Pareto principle: finding the slice worth cutting

Most of the pain usually comes from a minority of the cases (the 80/20 pattern). Before choosing a
slice, ask for a rough tally: "Of the last twenty times this happened, what did most of them have
in common?" A document type, a customer segment, a day of the week, a hand-off. The slice that
holds most of the pain is the one to state. If no tally exists, a week of tally marks is a
legitimate first action — and better than a POC built on a guess.

### A4. Examples — weak and good

| Weak (and why) | Good (and why) |
|---|---|
| "We need a chatbot for support tickets." — a solution wearing a problem's clothes; no who/when/impact. | "Every weekday morning (when) the two tier-1 support agents (who) spend the first 90 minutes re-categorising overnight tickets by hand (what) in the helpdesk queue (where), because auto-routing tags about a third of them wrong; that delays first response on those tickets by two hours on average (why it matters), and today they fix it by re-reading each one (how)." |
| "Reporting is slow." — no who, no where, no measure. | "On the first business day of each month (when), the FP&A analyst (who) spends roughly six hours re-keying subsidiary totals from twelve emailed spreadsheets into the consolidation workbook (what, where); the board pack goes out a day late about half the time as a result (why it matters), and the fix today is overtime (how)." |
| "People don't follow the process." — blames people; nothing observable. | "About one onboarding form in five (when/how often) arrives at HR (where) missing the manager's cost-centre code (what), so the HR coordinator (who) emails the manager and waits an average of two days (impact); there is no field validation on the form today (how)." |

What the good ones share: an observable event, a named role, a rough measure, a place in a
process, and no proposed tool.

### A5. Quality bar for a problem statement (check before writing it into the brief)

- Answers all six 5W1H questions, in the person's words.
- Describes an observable event, not a missing feature or a named tool.
- Names one slice; other slices are listed as out of this slice.
- Carries at least one rough number (frequency, time, cost, or count), even if estimated and
  labelled as such.
- Blames a process step or a condition, never a person.

---

## Part B — Root cause

### B1. Symptom versus cause

The problem statement describes a **symptom**: what is seen. The root cause is the condition
that, if changed, would make the symptom stop recurring. A POC aimed at a symptom produces a
patch; a proposal to IT aimed at a symptom produces a system that has to be patched forever.

### B2. The Five Whys — how to run it

Start from the problem statement exactly as written. Ask "why does that happen?" and write the
answer as an observable condition. Ask "why" of *that* answer. Repeat. Rules:

- Each answer must be something a person could go and check, not an opinion.
- Stop when the next "why" would leave the process you can influence, or when the answer is a
  condition that, if fixed, would plausibly stop the chain. Five is a guideline, not a count to
  hit.
- If an answer is "someone made a mistake" or "people don't care", keep going — ask *why the
  process let that mistake through*. Human error is where a Whys chain begins, never where it ends.
- Branch when needed. If a "why" has two honest answers, keep both branches and pick the one
  with more of the pain behind it (Pareto again).

### B3. Other practices worth offering

- **Go and see.** Before accepting a cause, ask whether the person has watched it happen or has
  data showing it. A cause nobody has observed is a hypothesis.
- **Categories to sweep** (a lightweight fishbone): process steps and hand-offs; information and
  data (missing, late, wrong format); tools and systems; policy and rules; environment and
  timing; skills and training. Ask "is there anything in this category contributing?" — it
  surfaces causes the Whys chain walked past.
- **Multiple causes are normal.** A problem often has two or three contributing causes. Name
  them, then rank by how much of the pain each explains.
- **Beware the disguised solution.** "Lack of an automated tool" is not a root cause; it is a
  solution with "lack of" in front of it. Ask what the tool would change, and name *that* as the
  cause.
- **The two tests.** *Necessity*: if this cause were removed, would the problem still happen? If
  yes, it is not the root. *Sufficiency*: does this cause alone explain most of the occurrences?
  If no, there is another cause to find.

### B4. Validate before writing

The root cause goes into the brief only after the person can say **how they know**: an
observation, a count, a document, a conversation with the people at the step. If they cannot,
record it as a *suspected* cause with the check that would confirm it — and make that check the
first action, ahead of any POC.

### B5. Quality bar for a root cause

- Stated as a condition in the process, not as a person's failing and not as a missing tool.
- The Whys chain (or branches) is visible, from the problem statement to the cause.
- Passes the necessity test; the sufficiency answer is stated honestly.
- Carries its evidence, or is labelled "suspected" with a named confirming check.
- The problem statement was not altered to fit the cause.

---

## Part C — Future state

### C1. Process, not people

The future state describes how the **work** will flow once the root cause is addressed: the
steps, the hand-offs, the inputs and outputs, the checks, what disappears and what stays. It does
not describe who should try harder, who should be replaced, or who is at fault. If a sentence
names an individual, rewrite it to name the step.

### C2. Lenses — offer several, let the person pick which apply

Each lens is a question to look through, not a section to fill:

| Lens | The question |
|---|---|
| **The person doing the work** | What does their day look like in the future state? What do they stop doing? What do they still decide? |
| **The customer of the process** | Who consumes the output, and what do they get that they do not get today — sooner, more accurate, more consistent? |
| **The flow** | Walk the steps end to end. Which step is removed, which is simplified, which is merged? Where does the hand-off now happen? |
| **Information** | What data arrives where, in what form, and when? What no longer has to be re-keyed, looked up, or chased? |
| **Earn the right to automate** | Define → Remove → Optimize → Design-for-scale → Automate. Which rung is this future state on? Can a step be *removed* before anything is automated? |
| **Simplest shape** | If AI is involved at all: one request → a fixed workflow → an agent. What is the simplest shape that does the job? (Most business work is a fixed workflow.) |
| **Reversibility and the human in the loop** | If the future state produced a wrong result, who would catch it and when? Where does a person approve before something consequential happens? |
| **Measurement** | What number moves, by how much, by when? How would the person know in ninety days that it worked? |
| **Do nothing** | What happens if the current state simply continues for a year? This sizes the value honestly. |
| **Boundaries** | What is explicitly *not* changing in this future state? |

### C3. The conversation

The future state is arrived at by talking, not by filling a form. Offer two or three lenses at a
time, ask which one the person wants to look through, listen, and reflect their answer back
sharper. Record only what they confirm. Expect the future state to be short — a paragraph and a
few bullets — and to say nothing about which product to buy.

### C4. Quality bar for a future state

- Describes the flow of work, hand-offs, and checks — not people's attitudes or a vendor.
- Addresses the confirmed root cause (a reader can see the line from cause to change).
- States what is removed or simplified before anything is automated.
- Names the human checkpoint(s) for anything consequential or hard to undo.
- Carries at least one measurable signal and a rough time horizon.
- Says what is out of scope for this future state.
- The problem statement and root cause were not altered while writing it.
