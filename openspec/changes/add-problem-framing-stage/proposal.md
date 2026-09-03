# Change: Add problem framing, the POC brief, and the POC summary to Stage 0

## Why

An evaluation of the `ai-solution-builder` skills against the AI Use Framework
(`plugins/ai-solution-builder/references/ai-use-framework.md`) found five gaps.
Each is a place where the Framework states a habit and the pipeline has no
artifact or step that produces it.

1. **The pipeline starts at "build a POC".** The Framework's "Before you build a
   solution" section says to map the work on paper before picking any tool, and
   its first recommended habit is "invest in the input". `ai-poc-builder` Step 1
   asks for one testable question, but nothing before it asks what the problem
   is, what causes it, or what the work should look like afterwards. The first
   document that demands a root cause is the Requirements template (§1), which
   arrives *after* the POC has been built. So POCs are framed as solutions, and
   the Requirements author is asked to reverse-engineer a problem from a
   prototype.
2. **The Requirements document is the wrong weight for a first conversation
   with IT.** It is a Gate 1 record with thirteen sections and a tier. A person
   who wants to ask IT "is this worth doing together?" needs one page, not a
   governed record, and the plugin had nothing between "chat" and "Gate 1".
3. **The learning from a POC lives only in chat.** `ai-poc-builder` Step 5
   captures learnings in conversation and maps them to Requirements sections,
   but no document holds them, and the changes made while building — the
   vibe-coded iterations that show what the first idea missed — are not
   recorded anywhere. That record is the most useful thing to show IT.
4. **"Refine, never originate" was stated for requirements but not for the
   problem.** The Framework's governing idea — you author the intent — applies
   earlier than §1 of a Requirements document. Nothing in the plugin enforced
   it for the problem statement, the cause, or the future state.
5. **Only one surface.** The organisation's people are split between Claude and
   Gemini; the plugin only served Claude, so half of them had no guided path.

## What Changes

- **Stage 0 becomes four steps: Frame → POC Brief → Build → POC Summary.** The
  Standard's wording — "POC (Stage 0 — learn, pre-gate)" — still describes the
  stage and is not edited.
- **New skill `ai-problem-framer`** writes the **Ultralight Problem Brief**: one
  page, three gated phases, one document.
  - Problem statement: 5W1H; slice the loaf when it is too big; the Pareto
    principle to find the slice; weak and good examples from other domains.
  - Root cause: the problem statement is read-only; the skill never writes to
    the brief in its first response of the phase; Five Whys plus root-cause
    practices (go and see, category sweep, multiple causes, the disguised
    solution, necessity and sufficiency); validated before writing.
  - Future state: problem and root cause are read-only; lenses offered in
    conversation; process, not people; the exact text is confirmed before
    writing.
  - The person authors every section; the skill guides. The brief's `phase`
    line is what gates the phases, not the opening sentence of a conversation.
- **New skill `ai-poc-brief-author`** turns a complete brief into the **POC
  Brief**: the three sections carried forward read-only, plus the one testable
  question, the smallest build, synthetic data, the safety pre-flight, success
  signal, do-not-build list, timebox, and a paste-ready build prompt for CoWork
  or Claude Code.
- **`ai-poc-builder`** starts from the POC Brief when one exists, keeps a running
  change log of every change made while building, and hands off to the summary
  skill instead of straight to Gate 1.
- **New skill `ai-poc-summary-author`** writes the **POC Summary**: the answer to
  the question, the evidence, the complete change log, surprises, data touched,
  the tripwire check, needs mapped to Requirements sections, and the person's
  ask to IT.
- **Four new references**: `problem-framing-methods.md` (the methods, shared by
  the skills and the Gems), `ultralight-brief-template.md`,
  `poc-brief-template.md`, `poc-summary-template.md`.
- **New `gems/` folder** with five Gemini Gem instruction sets producing the same
  outputs, one Gem per phase or document. The governing rule is restated at the
  top, inside each step, in a pre-reply self-check, and at the end, because
  Gemini drifts past a rule stated once at the top.
- `ai-requirements-doc-author` accepts a completed brief as the requester's own
  §1 input and names the Stage 0 documents in its hand-off.
- Plugin `1.4.0`; manifest, marketplace, READMEs, `TOOLKIT.md`, `CATALOG.md`,
  and both changelogs updated.

## Impact

- Affected specs: `ai-solution-builder-stage-0` (new)
- Affected code: `plugins/ai-solution-builder/` — three new skill folders, one
  modified skill (`ai-poc-builder`), one lightly modified skill
  (`ai-requirements-doc-author`), four new references, the `gems/` folder, the
  plugin manifest and changelog; `.claude-plugin/marketplace.json`; `TOOLKIT.md`;
  `CATALOG.md`; root `CHANGELOG.md`.
- Not changed, deliberately: `references/deployment-standard.md` and the root
  `policy/` files. The three Stage 0 documents are not governed records and
  carry no tier, so the Standard and the rules-as-data need no new control. If
  a later decision makes the Ultralight Problem Brief a required input to Gate 1,
  that is a Standard amendment and a separate change.
- Out of scope, deliberately: a Gem for building the POC (Gemini cannot build
  it; CoWork or Claude Code does), and any automation that reads the brief's
  `phase` line — the gating is instruction-level on both surfaces.
