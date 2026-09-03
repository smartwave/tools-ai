# Tasks

## 1. References
- [x] 1.1 `references/problem-framing-methods.md` — Part A (5W1H, slice, Pareto, examples, bar), Part B (Whys, practices, validate, bar), Part C (process not people, lenses, conversation, bar)
- [x] 1.2 `references/ultralight-brief-template.md` with the `Phase` line
- [x] 1.3 `references/poc-brief-template.md` with the build prompt block
- [x] 1.4 `references/poc-summary-template.md` with the change log and Requirements mapping
- [x] 1.5 `references/README.md` table updated

## 2. Skills
- [x] 2.1 `ai-problem-framer` — three phases, `phase` gating, first-response rule in Phase 2, confirm-before-write in Phase 3, refusals
- [x] 2.2 `ai-poc-brief-author` — complete-brief gate, Section A verbatim, pre-flight on explicit yes, build prompt
- [x] 2.3 `ai-poc-summary-author` — record-only rule, change log, tripwires, Requirements mapping, ask to IT
- [x] 2.4 `ai-poc-builder` — Step 1 from the brief, Step 4 change log, Step 5 hand-off to the summary
- [x] 2.5 `ai-requirements-doc-author` — accepts the brief as §1 input; hand-off names Stage 0 documents

## 3. Gems
- [x] 3.1 `gems/README.md` — mapping, why the repetition, how the document travels
- [x] 3.2 Gems 1–5, each with name, description, knowledge files, instructions; rule restated at top, per step, self-check, end

## 4. Repository integration
- [x] 4.1 Plugin manifest `1.4.0`, description, keywords
- [x] 4.2 `.claude-plugin/marketplace.json` synced
- [x] 4.3 Plugin `README.md`, `CHANGELOG.md`; `TOOLKIT.md`; `CATALOG.md` intake; root `CHANGELOG.md`

## 5. Verification
- [x] 5.1 Every new SKILL.md has valid frontmatter (`name`, `description`) and every `../../references/*.md` path it names exists
- [x] 5.2 Manifest and marketplace versions match
- [ ] 5.3 `openspec validate add-problem-framing-stage --strict` — CLI not installed on this machine; folder follows the shape of the existing changes
- [ ] 5.4 Owner: run `ai-problem-framer` end to end on a real problem and confirm the Phase 2 first-response rule holds
- [ ] 5.5 Owner: paste Gem 2 into a Gemini Gem and confirm it does not draft a cause when handed a brief and a topic
