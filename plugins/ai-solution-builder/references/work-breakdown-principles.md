# Work-Breakdown Principles

Reasoning guidance for the **ai-work-planner** skill when shaping a work-effort Epic and its child
issues in the work tracker (Jira in the reference configuration; substitute the equivalent tracker).
These are principles the planner must *explain per decision*, not a checklist to cite
silently. They apply within the three-artifact end state: the **AI Solution Requirements** sets the
requirements, the **Solution Spec** evidences the build, and the **work-effort Epic** tracks the
work (Standard B1.9). The Epic tracks; it never substitutes for either document.

## Principles

### 1. Vertical slices
Each child issue should deliver something checkable end-to-end — a thin path through the whole
solution — rather than a horizontal layer ("build all the parsing", "build all the UI"). A vertical
slice can be demonstrated, tested against an acceptance criterion, and cancelled without stranding
half-built layers.

### 2. Spikes for unknowns first
Every open technical question inherited from the Requirements or Spec becomes an early, time-boxed
spike child: unvalidated connectors, unconfirmed API behavior, custom fields that may not resolve by
name, data whose shape is assumed rather than observed. A spike's acceptance criterion is an
*answer*, documented on the ticket — not code.

### 3. Risk-first sequencing
Order children so the riskiest assumptions are tested earliest. If the effort is going to fail, it
should fail in week one on the assumption that kills it, not in week six after safe work is done.
Requirements §11 (risks) is the primary input here.

### 4. ~1 person-week grain, rolling-wave detail
Near-term children (roughly the next few weeks) are split to about one person-week each — small
enough to show honest progress, large enough not to drown the board. Later work stays as coarser
placeholder children, split only when the Solution Spec firms up enough to justify the detail.
Detailing far-future work before the design settles produces tickets that only get rewritten.

### 5. Non-code work gets tickets
Documentation, the Solution Spec itself, security review, vendor sign-off, Gate 2, and user
communication are children like any other. If it consumes effort and can block go-live, it is
visible on the board.

### 6. Expect append and cancel
Plans change as the Spec firms up. Appending new children and cancelling obsolete ones (with a
one-line reason) is the healthy pattern; keeping stale tickets "for the record" is not. The Epic's
final state should read as what actually happened. Cancellation, never deletion — and always with
human confirmation.

## Hard gates (the only prescriptions)

1. **Definition of Done content bar.** Every child created in the work tracker MUST carry an opening
   statement (what and why, in one or two sentences) and acceptance criteria (how we'll know it's
   done).
2. **{{PRODUCT_TRACKER_PROJECT_KEY}} field gate (product track).** The four manual
   {{PRODUCT_TRACKER_PROJECT_KEY}} fields — Effort Person-Weeks, Planned Start Date
   ({{PRODUCT_TRACKER_PROJECT_KEY}}), Engineers Assigned, Confidence Level — hold the requester's own
   numbers or stay blank. {{PRODUCT_TRACKER_PROJECT_KEY}} Include is set last, only when all four are
   present, mirroring the tracker's guardrail automation.

## Lifecycle touchpoints

- **Gate 1:** Epic + discovery/spike children.
- **Spec firming up:** append implementation children under the same Epic (one work effort = one
  Epic).
- **Close:** verify the Solution Spec pre-flight gate (§21) is complete — and Gate 2 where required
  — before the Epic closes; confirm the Epic reflects the work actually performed.

## Anti-patterns

- Bare-summary tickets with no opening statement or acceptance criteria.
- A second Epic for the same work effort.
- A `tasks.md` (or similar file) maintained as a parallel status source — the work tracker is the
  status record. Ephemeral scaffolding may be cited once as Solution Spec evidence, then retired.
- Invented estimates, dates, or confidence levels.
- Deleting issues instead of cancelling them with a reason.
