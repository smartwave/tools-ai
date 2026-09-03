# Delta for Open Items Ledger

## Purpose

The file format for tracking unfinished work. Defines the ledger file, its
frontmatter, its item grammar, and the lifecycle of an item from opened to swept.
This is the contract that the skill, the validator and the collector all read.

## ADDED Requirements

### Requirement: Ledger File Location and Naming

A ledger file MUST be named exactly `OPEN-ITEMS.md` and MUST sit at the root of the
scope it tracks. A scope is any folder work is done in. There MUST be at most one
ledger per scope, and there MUST NOT be a registry file listing ledger locations —
the filename is the registration.

#### Scenario: Ledger created in a new scope

- GIVEN a folder with no ledger
- WHEN a ledger is created for that folder
- THEN the file is named `OPEN-ITEMS.md`
- AND it sits at the folder root
- AND it is discoverable by a filesystem scan without any registration step

#### Scenario: Cross-scope write refused

- GIVEN a session working in scope A
- WHEN an item belonging to scope B is logged
- THEN the item is written to scope A's ledger or refused
- AND scope B's ledger is not modified

### Requirement: Frontmatter

Every ledger MUST carry YAML frontmatter with exactly four keys: `title`,
`scope_prefix`, `next_id`, `updated`. `scope_prefix` MUST be 2–8 characters of
uppercase letters and digits, starting with a letter, and MUST be unique across all
of the user's ledgers. `next_id` MUST be an integer strictly greater than the
highest item number in the file. `updated` MUST be an ISO date and MUST be
maintained by tooling rather than by hand.

#### Scenario: next_id would reuse an ID

- GIVEN a ledger whose highest item number is 0015
- WHEN `next_id` is set to 15 or lower
- THEN validation fails with an error naming the collision risk

#### Scenario: Invalid scope prefix

- GIVEN a ledger with `scope_prefix: tai`
- WHEN the ledger is validated
- THEN validation fails, because the prefix is not uppercase

### Requirement: Sections

A ledger MUST contain exactly two second-level headings, `## Open` and `## Closed`,
in that order, both present even when empty. No other second-level heading is
permitted. Items MUST NOT appear outside these two sections.

#### Scenario: Unexpected heading

- GIVEN a ledger containing a `## Notes` heading
- WHEN the ledger is validated
- THEN validation fails and names the offending heading

### Requirement: Item Grammar

An item MUST occupy a single line and MUST match this grammar, with fields in this
fixed order: text, `opened`, `closed`, path.

```
- [ ] **PREFIX-NNNN** — Item text · opened YYYY-MM-DD
- [ ] **PREFIX-NNNN** — Item text · opened YYYY-MM-DD · relative/path.md
- [x] **PREFIX-NNNN** — Item text · opened YYYY-MM-DD · closed YYYY-MM-DD
- [x] **PREFIX-NNNN** — Item text · opened YYYY-MM-DD · closed YYYY-MM-DD · relative/path.md
```

Fields MUST be separated by ` · ` (space, U+00B7, space). The ID MUST be separated
from the text by ` — ` (space, U+2014, space). The item ID prefix MUST match the
ledger's `scope_prefix`. The checkbox state MUST match the section: `[ ]` in Open,
`[x]` in Closed. `opened` is required on every item. `closed` MUST appear on closed
items and MUST NOT appear on open items. The path field is optional and MUST be
relative to the scope root.

#### Scenario: Checkbox contradicts section

- GIVEN an item marked `[x]` sitting under `## Open`
- WHEN the ledger is validated
- THEN validation fails and names the line

#### Scenario: Open item carries a closed date

- GIVEN an item under `## Open` with a `closed` field
- WHEN the ledger is validated
- THEN validation fails

### Requirement: Reserved Characters in Item Text

Item text MUST NOT contain the separator characters U+00B7 or U+2014, and MUST NOT
contain a line break. A stray separator silently splits the text into a fake field,
which corrupts the item without producing a parse error — the validator MUST
therefore detect this case rather than allowing it through.

#### Scenario: Stray separator in item text

- GIVEN an item whose text contains a middle dot
- WHEN the ledger is validated
- THEN validation fails with an error stating that a stray separator has probably
  split the item text
- AND the error names the fragment that was misread as a path

### Requirement: Item Text States an Outcome

Item text SHOULD be written as the finished state rather than the activity, because
the format has no separate exit-condition field and the text alone must answer "is
this done?". Tooling that writes an item SHOULD rewrite activity-shaped text into
outcome-shaped text and show the user what it wrote.

#### Scenario: Activity-shaped text supplied

- GIVEN the user says "log that I need to look at the CI checks"
- WHEN the item is written
- THEN the text reads as an outcome, such as "Three stub CI checks implemented and
  passing"
- AND the rewritten text is shown to the user

### Requirement: Item Identifiers

IDs MUST be minted from the ledger's `next_id`, zero-padded to four digits, after
which `next_id` MUST be incremented. IDs MUST NOT be reused and MUST NOT be
renumbered, including after a sweep deletes the item. Because prefixes are unique
per ledger, two ledgers MUST be mergeable by concatenation without collision.

#### Scenario: Item swept then a new item minted

- GIVEN item PREFIX-0004 has been swept from the ledger
- WHEN a new item is minted
- THEN it receives the current `next_id`, not 0004

### Requirement: Item Lifecycle

An item MUST progress: opened → optionally updated → closed → swept. Logging an
existing item MUST rewrite its text in place and MUST NOT change its ID or `opened`
date. Closing MUST move the line to `## Closed`, flip the checkbox, and append a
`closed` date. A closed item MUST be deleted outright once its `closed` date is more
than 7 days old. There MUST NOT be an archive file — version history serves that
purpose.

#### Scenario: Closed item ages past the sweep window

- GIVEN a closed item whose `closed` date is 8 days ago
- WHEN a sweep runs
- THEN the item line is deleted from the ledger
- AND no archive file is written

#### Scenario: Existing item logged again

- GIVEN item PREFIX-0007 opened on 2026-08-22
- WHEN the same item is logged with revised text
- THEN the text is replaced
- AND the ID and `opened` date are unchanged

### Requirement: Ledgers Are Never Archived

A ledger is a rolling list and MUST NOT have a closed, archived, or snapshot state.
If a scope ends, its folder and its ledger are removed together.

#### Scenario: Scope ends

- GIVEN a project folder that is no longer needed
- WHEN the folder is deleted
- THEN its ledger goes with it and no archival step is required
