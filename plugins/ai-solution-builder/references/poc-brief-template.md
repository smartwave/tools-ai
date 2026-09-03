# POC Brief — Template

*The second artifact of Stage 0. Turns a **complete** Ultralight Problem Brief into the one
document a person needs to generate a throwaway proof of concept in CoWork or Claude Code. It
carries the three brief sections forward unchanged and adds the few data points a build needs.
The brief never authorises deployment; a POC built from it is personal, on synthetic data, and
throwaway (Standard B1.5, B1.6; `ai-poc-builder`).*

*Method guidance: `problem-framing-methods.md` (Part C, simplest-shape and reversibility lenses)
and the pre-flight safety check in `../skills/ai-poc-builder/SKILL.md`.*

**DELETE EVERYTHING ABOVE THIS LINE BEFORE SHARING**
---

# POC Brief — [short title]

| | |
|---|---|
| **Author** | |
| **Date** | |
| **Source brief** | *link or filename of the Ultralight Problem Brief (phase: complete)* |
| **Timebox** | *e.g., half a day; one day at most* |
| **Environment** | CoWork · Claude Code |
| **Lane** | script · packaged skill · single-file HTML prototype |

## A. Carried forward (read-only from the Ultralight Problem Brief)

**Problem statement:**

**Root cause:**

**Future state (one paragraph):**

## B. The one testable question

*The single thing this POC exists to find out, phrased as a question with a yes/no/partly answer.
"Can a model reliably pull the invoice date from these PDFs?" — not "build an invoice tool".*

**Question:**

**Hypothesis (what we expect):**

**What would disprove it:**

## C. The smallest thing that answers it

*What the POC will actually do and show. One thing. If three things must be true, this is the
riskiest one.*

## D. Data

*Synthetic or de-identified only. Never live customer, personal, reporting, Confidential, or
Restricted data; never a production system of record.*

| Sample data the POC uses | Stands in for (real data type) | Where the sample comes from |
|---|---|---|
| | | |

## E. Safety pre-flight (all three must be true before building)

- ☐ Data is synthetic or de-identified, and no production system is touched.
- ☐ No secrets in code, prompt, file, or repo; any key is a throwaway with a spend cap, read from the environment.
- ☐ Blast radius is personal: outputs are for the author only; nothing sends, posts, writes to a shared system, or runs on a schedule.

## F. Success signal

*How the author will know the question is answered — what to count or observe, and the rough
threshold that would count as "yes".*

## G. Do not build

*Explicit exclusions. An AI builder cannot infer scope from omission.*

-
-

## H. Build prompt (paste into CoWork or Claude Code)

*Assembled from A–G above, in the author's words. The AI build tool reads this block first.*

```
You are helping me build a throwaway proof of concept. It exists to answer one question, on
synthetic data, for me alone. Do not connect it to any real system, credential, schedule, or
other person.

Question: [B]
What to build: [C]
Environment and lane: [header]
Sample data: [D]
Success signal: [F]
Do not build: [G]
Timebox: [header]

Keep a running change log of every change we make while building — what changed, why, and
who asked — so I can summarise it afterwards.
```

---

*Next step: build it (`ai-poc-builder` in Claude Code, or paste block H into CoWork), then write
the **POC Summary** (`poc-summary-template.md`).*
