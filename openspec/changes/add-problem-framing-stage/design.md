# Design: problem framing before the POC

Decisions taken while designing the change, with the reasoning.

## One skill for three phases, but five Gems

On Claude the three phases live in one skill, `ai-problem-framer`, because one
skill can hold the phase state, read the brief's `phase` line, and enforce the
read-only rules across a conversation. Three skills would have needed each to
re-derive where the person was.

On Gemini the same three phases are three Gems. A Gem cannot write a file or
carry state between sessions, so each phase has to be a fresh conversation into
which the person pastes the brief, and the Gem reads the `phase` line to decide
whether it may act. Splitting also keeps each instruction set short enough that
the governing rule is not buried.

The mapping is recorded in `gems/README.md` so a maintainer changing one surface
knows what to change on the other.

## The `phase` line gates, not the conversation

Both surfaces read the brief's `Phase` value before doing anything. A person who
opens with "help me with the root cause" while the brief still says `problem`
is sent back to finish Section 1. This is what makes "the problem statement is
read-only" enforceable by instruction: the tool never has a reason to edit a
section that belongs to a phase it is not in. Re-opening a phase is allowed but
must be named, and the later sections are re-checked afterwards.

## "Never write on the first response" is a rule for the root-cause phase only

The user asked for it there specifically. The reason it belongs there and not
elsewhere: the root-cause phase is where the temptation to "fix" the problem
statement to match a cause is strongest, and where a model most often
short-circuits the Whys chain by stating a plausible cause immediately. Making
the first response a read-back plus a single "why" removes both. The
future-state phase gets the softer form — confirm the exact text before writing —
because it is a conversation that legitimately produces text over several turns.

## The three documents are not governed records

The Standard defines the AI Solution Requirements, Solution Design, and Solution
Spec as records, with tiers and gates. The Ultralight Problem Brief, POC Brief,
and POC Summary are learning artifacts that feed the Requirements document.
Giving them a tier or a gate would put ceremony before the point where a person
knows whether AI is even the answer, which is the failure the Framework's "earn
the right to automate" pattern warns against. So the Standard is untouched and
the templates say "not a governed record".

## Why the change log is kept by the builder, not reconstructed by the summary

The changes made while vibe-coding a POC are the most honest signal of what the
first idea missed, and they are forgotten within hours. So `ai-poc-builder`
writes the log as it goes, from the first change, and `ai-poc-summary-author`
refuses to smooth over a gap in it. On Gemini, the build prompt in the POC Brief
carries the same instruction to whichever tool builds the POC.

## Why the Gems repeat themselves

The user's observation: Gemini treats a hard instruction placed once at the top
of a long instruction set as context, and drifts into drafting the person's
content after a few turns. The response is structural rather than stylistic:
each Gem states the governing rule at the top, restates it inside every step
where the temptation arises, runs a four-item self-check before every reply, and
closes by restating it. `gems/README.md` tells a future maintainer not to tidy
the repetition away.

## Shared methods file rather than inlined methods in each skill

`problem-framing-methods.md` holds 5W1H, slice the loaf, Pareto, the examples,
the Whys rules, the root-cause practices, and the lenses once. The Claude skills
read it at runtime; the Gems inline it because they cannot read files reliably.
That means the Gems can drift from the reference; the README names the reference
as the source and instructs regeneration rather than hand-editing.

## Deliberately not built

- **A Gem that builds the POC.** Gemini is not the build surface.
- **Automation reading the `phase` line.** Gating is instruction-level on both
  surfaces. A validator for the brief could be added later if drift appears.
- **Edits to the deployment standard or `policy/`.** See above.
- **A tier or a gate for the Stage 0 documents.** See above.
