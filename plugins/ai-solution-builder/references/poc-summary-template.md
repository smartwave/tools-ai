# POC Summary — Template

*The third artifact of Stage 0 and the first document shown to IT. Records what the proof of
concept actually did, every change made while building it, what was learned, and the author's
recommendation: partner with IT, ask IT to build it, keep it personal, or stop. It records only
what happened — no invented results, no rounded-up accuracy. It does not authorise deployment;
if the recommendation is to build, the next step is Gate 1 (`ai-requirements-doc-author`).*

*Where each part lands later: the mapping to AI Solution Requirements sections is in §H.*

**DELETE EVERYTHING ABOVE THIS LINE BEFORE SHARING**
---

# POC Summary — [short title]

| | |
|---|---|
| **Author** | |
| **Date** | |
| **Source POC Brief** | |
| **Source Ultralight Problem Brief** | |
| **Time spent** | *against the timebox* |

## A. Bottom line

**The question:** *(from the POC Brief, verbatim)*

**The answer:** Yes · Partly · No — *one sentence of why*

**Recommendation:** Partner with IT to build it · Ask IT to build it · Keep as a personal tool · Stop here — *one sentence of why*

## B. What was built

*Environment, lane, and what the thing does, in plain language. Where the files are (personal
location only).*

## C. Evidence

*What was run, on what sample data, and what was observed. Rough numbers labelled as rough.
Failure modes seen.*

| What we tried | Sample size | What happened | Counts as |
|---|---|---|---|
| | | | pass / fail / unclear |

## D. Change log — every change made while building

*Every vibe-coded change, in order. This is the part IT most wants to see: it shows what the
first idea missed.*

| # | What changed | Why | Who asked | Effect on the answer |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

## E. What surprised us

*Including anything that suggests the problem statement or root cause needs revisiting.*

## F. Data touched

| Sample data used | Stands in for (real data type) | Read / write |
|---|---|---|
| | | |

## G. Tripwire check (all must still be true)

- ☐ Only the author has used it.
- ☐ Only synthetic or de-identified data was used; no production system touched.
- ☐ No secret was placed in code, prompt, file, or repo.
- ☐ It has not run on a schedule, sent anything, or written to a shared system.

*If any box cannot be ticked, the POC has become a deployment: stop using it and start Gate 1
(Standard B1.6).*

## H. What the real version would need

*The author's view, mapped to where it will land in the AI Solution Requirements.*

| Need | Lands in Requirements |
|---|---|
| | §1 Problem (from the Ultralight Problem Brief) |
| | §2 Outcome / §9 Success metrics |
| | §5 Functional requirements / §6 Acceptance criteria |
| | §8 Data & sensitivity |
| | §10 Process-readiness gate |
| | §11 Risks |

## I. The ask to IT

*One paragraph, in the author's words: what was proven, what is being asked for (partnership or
build), and what the author will bring to Gate 1.*

---

*Next step: share this with IT. If the answer is to build, start Gate 1 with
`ai-requirements-doc-author`; the Ultralight Problem Brief and this summary drop straight into it.*
