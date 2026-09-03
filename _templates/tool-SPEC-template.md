---
title: "[TOOL NAME] — Spec"
type: spec
set: tools
status: spec
audience: owner
updated: [DATE]
tags:
  - ai-tools
  - spec
---

# [TOOL NAME] — Spec

> Copy this file into the tool's folder as `SPEC.md` before building. It is deliberately short: if a section is hard to fill in, that's the signal to stop and think, not to skip it.

## Problem and outcome

**What's broken or missing:** [One or two sentences. A real problem, not a tool looking for one.]

**Outcome when this works:** [The measurable result. What changes, for whom, by how much? "No baseline, no project."]

## Audience and mode

- **Who uses it:** [me only / shared with work / client]
- **Mode** (per the AI-Program deployment standards): [**personal efficiency** — I am the only consumer and I review every output, or **process automation** — other people or systems depend on the output]

## Risk tier

- **Tier:** [1 / 2 / 3] per `AI-Program/02-Governance/01-AI-Risk-Tiering.md`
- **Why:** [One sentence of reasoning — what data it touches, who depends on it, what happens if it's wrong]
- **Oversight:** [human reviews every output / human samples outputs / human approves actions before they run]

## Data and access

- **Data it reads:** [sources; note anything sensitive]
- **Data it writes or actions it takes:** [outputs; anything irreversible?]
- **Credentials/permissions needed:** [least privilege — list them]

## Definition of done

Before setting status `built`, check this tool against `AI-Program/02-Governance/06-Definition-of-Done-AI.md` for its tier, and record here which items applied and how they were satisfied:

- [ ] [item] — [how satisfied]

## Graduation trigger

[What change would force this tool into a higher tier or the formal deployment lane — e.g., "if anyone else starts relying on the output" or "if it starts running on a schedule without me watching."]
