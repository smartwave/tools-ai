# Gemini Gems — the Stage 0 flow for people on Gemini

Five Gem instruction sets that produce the same Stage 0 outputs as the Claude skills in
`../skills/`, for {{ORG_NAME}} employees whose tool is Google Gemini rather than Claude. Each file
holds the Gem's name, a description for the Gem's description field, the optional knowledge files
to attach, and the instructions to paste into the Gem's Instructions field.

| Gem | Produces | Claude equivalent |
|---|---|---|
| `gem-1-problem-statement.md` | Ultralight Problem Brief §1 (5W1H, slice, Pareto) | `ai-problem-framer` Phase 1 |
| `gem-2-root-cause.md` | Ultralight Problem Brief §2 (Five Whys, validated); §1 read-only | `ai-problem-framer` Phase 2 |
| `gem-3-future-state.md` | Ultralight Problem Brief §3 (lenses; process, not people); §1–§2 read-only | `ai-problem-framer` Phase 3 |
| `gem-4-poc-brief.md` | POC Brief, with the paste-ready build prompt | `ai-poc-brief-author` |
| `gem-5-poc-summary.md` | POC Summary, with the vibe-coded change log and the ask to IT | `ai-poc-summary-author` |

The Gems do not build the POC. Building happens in CoWork or Claude Code (`ai-poc-builder`, or the
POC Brief's block H pasted into CoWork); the person keeps the change log there and brings it to
Gem 5.

## Why the instructions repeat themselves

Gemini tends to treat a hard rule stated once at the top of a long instruction as context rather
than as a constraint, and drifts into drafting the person's content for them after a few turns.
So each Gem states the governing rule — **guide, never author** — at the top, again inside every
step where the temptation arises, in a self-check the Gem runs before every reply, and again at
the end. The repetition is deliberate. Do not "tidy" it away.

## How the document travels between Gems

Gems cannot write files. "Write to the brief" means: output the **entire** brief in one Markdown
code block, with the locked sections reproduced **character for character** from what the person
pasted, and only the current section changed. The person copies the block into their own file and
pastes it into the next Gem. Each Gem reads the `Phase` line first and refuses to act on a brief
in the wrong phase.

## Source of truth

The methods and templates the Gems inline are `../references/problem-framing-methods.md`,
`../references/ultralight-brief-template.md`, `../references/poc-brief-template.md`, and
`../references/poc-summary-template.md`. When those change, regenerate the Gem instructions from
them; do not let the two drift. Attaching the reference files as Gem knowledge files is optional
and helps with the examples, but the instructions must work without them.

## Placeholders

Substitute `{{ORG_NAME}}` and `{{SECURITY_CONTACT_EMAIL}}` before pasting. Everything else is
literal.
