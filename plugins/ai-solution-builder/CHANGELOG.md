# Changelog — ai-solution-builder

All notable changes to this plugin. Versions follow SemVer.

## [1.4.0] — 2026-09-02

### Added
- **Stage 0 restructured into four steps, three of them new.** The pipeline previously started at
  "build a POC"; the AI Use Framework's first habits ("map the work first", "invest in the input",
  "you author the intent") had no artifact before the prototype, so POCs were framed as solutions
  and the Requirements document's root-cause demand arrived after the build.
  - **New skill `ai-problem-framer`** — the **Ultralight Problem Brief**: problem statement (5W1H,
    slice the loaf, Pareto, weak/good examples), root cause (Five Whys, validation; problem
    statement read-only; never writes on its first response), future state (lenses; process, not
    people; exact text confirmed before writing). One document, three gated phases, in the
    person's own words.
  - **New skill `ai-poc-brief-author`** — the **POC Brief**: carries the three brief sections
    forward read-only and adds the one testable question, smallest build, synthetic data, safety
    pre-flight, success signal, do-not-build list, and a paste-ready build prompt.
  - **New skill `ai-poc-summary-author`** — the **POC Summary**: what the POC did, every
    vibe-coded change, what was learned, the tripwire check, and the person's ask to IT.
  - **New references** `problem-framing-methods.md`, `ultralight-brief-template.md`,
    `poc-brief-template.md`, `poc-summary-template.md`.
  - **New `gems/` folder** — five Gemini Gem instruction sets producing the same Stage 0 outputs,
    with the governing rule restated throughout because Gemini drifts past a single top-of-document
    instruction.

### Changed
- `ai-poc-builder` — Step 1 starts from the POC Brief when one exists (Section A read-only);
  Step 4 keeps a running change log of every change made while building; Step 5 hands off to
  `ai-poc-summary-author` rather than straight to Gate 1. Stage list updated.
- `ai-requirements-doc-author` — Step 3 §1 guidance accepts a completed Ultralight Problem Brief
  as the requester's own §1 input; handoff text names the Stage 0 documents.
- `references/README.md`, plugin `README.md`, manifest description — updated for eight skills.
- The deployment standard is deliberately unchanged: the three Stage 0 documents are not governed
  records and the Standard's "POC (Stage 0 — learn, pre-gate)" wording still describes the stage.

## [1.1.0] — {{TICKET_REF}}

### Added
- **New skill `ai-work-planner`** — turns an approved AI Solution Requirements document (and the
  Solution Spec, once started) into a Jira work-effort Epic with child issues, and creates them via
  the Atlassian connector only on the requester's explicit approval. Covers both the product
  (`{{PRODUCT_TRACKER_PROJECT_KEY}}`) and non-product tracks. Proposes, never auto-creates; never
  invents estimates, dates, or confidence; never assigns people; never deletes issues.
- **New reference `references/work-breakdown-principles.md`** — reasoning guidance for shaping the
  Epic and its children (vertical slices, spikes-first, risk-first sequencing, ~1 person-week
  grain, rolling-wave detail).
- **Standard `B1.9` (Work-effort tracking)** added to `references/deployment-standard.md` — Tier 2+
  solutions MUST have a Jira Epic opened at Gate 1, before build; Jira is the authoritative work
  record.

### Changed
- `references/solution-spec-template.md` — added `work_effort_epic` field to the YAML control header.
- `references/requirements-template.md` — added optional BLUF row `Work-effort Epic: [created after
  Gate 1]`.
- `ai-requirements-doc-author` — tier lines now state the B1.9 Epic requirement (recommended at
  Tier 1; required at Tier 2+); Step 5 handoff directs to `ai-work-planner` after Gate 1.
- `ai-solution-spec-author` — Step 1 adds a work-effort Epic gate check; Step 3 records the
  `work_effort_epic` header field; ephemeral-scaffolding evidence note; Step 8 handoff confirms the
  Epic reflects work performed.

## [1.0.0]
- Initial release: `ai-requirements-doc-author` and `ai-solution-spec-author` skills with bundled
  Standard, framework, and templates as source of truth.
