# Ultralight Problem Brief — Template

*One page. The first artifact of Stage 0, written **by the person** with an AI tool guiding —
not drafting — each section. It comes before any proof of concept and is the document a
POC Brief, a POC Summary, and eventually an AI Solution Requirements (§1 Problem) are built
from. Tier-independent: a brief is worth writing for any problem, whether or not AI turns out
to be the answer.*

*Method guidance lives in `problem-framing-methods.md`; the AI tool reads it and applies it,
and the sections below stay clean.*

**How the phases work.** The brief is written in three phases, in order. Once a phase is
confirmed, its section is **read-only** for the following phases: the root-cause phase does not
edit the problem statement; the future-state phase edits neither. The `phase` line records where
the brief is. A change to an earlier section means going back to that phase deliberately, with
the later sections re-checked.

**DELETE EVERYTHING ABOVE THIS LINE BEFORE SHARING**
---

# Ultralight Problem Brief — [short title]

| | |
|---|---|
| **Author** | |
| **Date** | |
| **Phase** | `problem` → `root-cause` → `future-state` → `complete` |
| **Slice** | *the one who / where / what this brief covers* |
| **Not in this slice** | *other slices of the loaf, one line* |

## 1. Problem statement

*One or two sentences in the author's words that answer who, what, when, where, why it matters,
and how it shows up today. An observable event with a rough number, not a missing tool.*

**5W1H, in brief:**

| Who | What | When | Where | Why it matters | How it shows up today |
|---|---|---|---|---|---|
| | | | | | |

## 2. Root cause

*The condition in the process that, if changed, would stop the problem recurring. Stated as a
condition, not a person's failing and not "lack of a tool". Locked once confirmed.*

**Whys chain (from the problem statement to the cause):**

1. Why? —
2. Why? —
3. Why? —
4. Why? —
5. Why? —

**Root cause (confirmed / suspected):**

**How we know (evidence, or the check that would confirm it):**

**Other contributing causes, ranked:**

## 3. Future state

*How the work flows once the root cause is addressed: steps, hand-offs, inputs and outputs,
checks. Process, not people. No product names.*

**The flow in the future state:**

**What is removed or simplified before anything is automated:**

**Where a person checks or approves:**

**How we would know it worked (signal, rough size, by when):**

**Not changing in this future state:**

---

*Next step: a **POC Brief** (`poc-brief-template.md`) if the future state is worth testing with a
small proof of concept; otherwise, this brief is enough to open a conversation with IT.*
