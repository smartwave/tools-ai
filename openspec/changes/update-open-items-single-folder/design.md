# Design: open-items single tracker folder

Decisions taken during the design discussion, with the reasoning, so a later
reader does not have to re-derive them.

## What is being traded

Per-folder placement gave routing for free: the folder the session was working in
picked the file, so the user never chose. A central folder removes that, and
every log now needs a project and a category chosen.

The analogy that framed the decision: notes currently live in the room you are
working in, so you never think about where to put them. A single filing cabinet
means every note needs a drawer picked.

That cost is accepted because the scattering it removes is the actual complaint.
It is paid down two ways, and both matter more than the folder move itself:

1. **Pick from a list, not from memory.** `status.py` prints the projects and
   categories with counts before any question is asked. Choosing is recognition,
   not recall.
2. **A fast path that skips the questions.** When the user names the destination
   in the request, nothing is asked. A reminder tool used mid-task has seconds,
   not a minute. If it is skipped the list develops silent gaps, and a list with
   gaps is worse than no list because it is still trusted.

## Why files and categories both exist

Two ways to separate work invites the same effort landing as a heading one week
and a file the next, which reproduces the original problem in a smaller space.

The split: a **file** is a standing body of work returned to over months. A
**category** is a distinct effort inside it that will end. The rule is not
enforced — the listing behaviour is what actually prevents drift, because the
user sees what already exists before naming anything new.

One consequence to know: promoting a category into its own file later means a new
prefix and new IDs, because IDs are never renumbered and the prefix must match
the file.

## Why fields are labelled

The old format's one sharp edge: a stray middle dot in item text silently splits
it into a fake field, corrupting the item with no parse error. The old validator
guessed at it — a path field containing spaces was probably misread text — and
the spec admitted it could detect but not prevent it.

Locators frequently contain spaces (chat names), so that heuristic would now fire
constantly or not at all. Labelling every field after the text (`find: `,
`opened `) makes an unlabelled field impossible under the grammar, so it is a
reliable error rather than a guess. The validator names the fragment.

## Why closing deletes

The previous design deleted closed items after seven days and justified it by
saying version history was the archive. The tracker folder is not a repository,
so that justification does not hold there. Rather than add an archive file, the
user's decision is that closed items are simply gone.

The mitigation is procedural, not structural: the skill prints each line in full
before deleting it, so the conversation carries the only record.

## Why the outcome rule was removed rather than softened

The old spec required item text be phrased as an outcome, because nothing
observed completion and the text alone had to answer "is this done?".

Under the actual use, the user decides when a thread is finished. The text does
not need to prove doneness; it needs to return the user to the right
conversation. Those pull in opposite directions, so the rule is removed rather
than qualified — the existing items in the user's file read as good outcome
statements and poor pointers, which is the failure mode being corrected.

## Deliberately not built

- **Unprompted surfacing at session start.** More useful and more annoying;
  parked at the user's request for a later change.
- **Migration tooling.** One ledger existed and it was moved by hand.
- **A `workspace:` frontmatter key** recording the folder each project lives in.
  Proposed and withdrawn: it assumed one file per effort, which categories
  contradict. If a folder path is ever worth recording it belongs under the
  category heading, not in frontmatter.
