# open-items Specification

> No `openspec/specs/open-items/spec.md` baseline exists in this repository — the
> `add-personal-assistant-plugin` change that introduced the capability has not
> been archived yet. Per that change's implementer note, the `## MODIFIED`
> requirements are folded into `## ADDED` here and `## REMOVED` is dropped; the
> requirement text is unchanged. What was removed, and why, is recorded in
> `proposal.md` under **Supersedes**.


## ADDED Requirements

### Requirement: Single tracker folder

All tracker files SHALL live in one folder, `~/Documents/Claude/Claude Task
Tracker`. The location SHALL be overridable by the `CLAUDE_TASK_TRACKER`
environment variable so tests do not touch the real folder. Discovery SHALL be a
listing of that folder; there SHALL be no registry, no configured scan roots and
no directory walking.

#### Scenario: Finding tracker files

- **WHEN** the skill needs to know what tracker files exist
- **THEN** it lists the tracker folder for files matching `OPEN-ITEMS *.md`
- **AND** it does not search any other location

### Requirement: Folder access check

The skill SHALL confirm the tracker folder is reachable before any read or write.
When it is not reachable, the skill SHALL state the exact path, ask the user to
grant access, and stop. It SHALL NOT create a tracker file in any other location,
and SHALL NOT fall back to the current working folder.

#### Scenario: Folder unreachable

- **WHEN** `status.py` is run and the tracker folder cannot be listed
- **THEN** it writes the path to standard error and exits with code 2
- **AND** the skill reports the path to the user and takes no further action

#### Scenario: Folder reachable but empty

- **WHEN** the tracker folder exists and holds no tracker files
- **THEN** `status.py` reports the folder as empty and exits with code 0
- **AND** the skill offers to create a project file

### Requirement: One file per project

A tracker file SHALL be named `OPEN-ITEMS <project>.md`, and the project name
SHALL be derived from the filename. A project is a standing body of work returned
to over weeks or months, not a single task. A filename not following this pattern
SHALL fail validation.

#### Scenario: Project name derived from filename

- **WHEN** `OPEN-ITEMS Claude AI Strategy.md` is parsed
- **THEN** the project name is `Claude AI Strategy`

#### Scenario: Filename does not follow the pattern

- **WHEN** a file in the tracker folder is validated and its name lacks the
  `OPEN-ITEMS ` prefix
- **THEN** validation fails naming the filename

### Requirement: Categories within a project

A tracker file SHALL support `###` headings under `## Open` to group items by
category. A category represents a distinct effort inside the project — a topic, a
thread of work, a Claude Code push. Items MAY sit under `## Open` with no
category. An empty category heading SHALL remain in the file until the user
removes it.

#### Scenario: Item grouped under a category

- **WHEN** an item line follows a `### Learning Guides` heading inside `## Open`
- **THEN** the item carries `Learning Guides` as its category

#### Scenario: Category heading outside the Open section

- **WHEN** a `###` heading appears before `## Open`
- **THEN** validation fails naming the line

### Requirement: Locator field

An item MAY carry a `find:` field holding whatever returns the user to the work —
a chat name, a chat ID, a topic, or a plain reference. The field SHALL be
optional and SHALL be omitted rather than left empty.

#### Scenario: Item with a locator

- **WHEN** an item line reads `... · find: chat "Access review memo" · opened 2026-08-27`
- **THEN** the locator is `chat "Access review memo"`

#### Scenario: Empty locator

- **WHEN** an item carries `find:` with nothing after it
- **THEN** validation fails and advises leaving the field off

### Requirement: Labelled fields after the item text

Every field after the item text SHALL carry a label: `find: ` or `opened `. An
unlabelled field SHALL fail validation with a message naming the offending
fragment and identifying it as a probable stray separator in the item text.

#### Scenario: Stray separator in item text

- **WHEN** an item's text contains a middle dot, splitting it into an unlabelled
  field
- **THEN** validation fails naming the fragment and the reserved character

### Requirement: Listing for selection

The skill SHALL provide `status.py`, which prints every project file in the
tracker folder with its prefix, its categories, and open counts, and with
`--items` every open item. The skill SHALL run it before asking the user where an
item belongs, so the user picks from a list rather than recalling. The script
SHALL have no third-party dependencies and SHALL contain no judgement — listing,
parsing and counting only.

#### Scenario: Choosing a destination

- **WHEN** the user asks to log an item without naming a destination
- **THEN** the skill runs `status.py`, shows the projects with counts, asks which
  one, then shows that project's categories with counts and asks which one

### Requirement: Fast path for a named destination

When the user names both project and category in the request, the skill SHALL
write the item without asking anything further. Logging SHALL be fast enough to
use mid-task; a prompt sequence that is skipped produces a list with silent gaps,
which is worse than no list because it is still trusted.

#### Scenario: Destination named in the request

- **WHEN** the user says "log to AI Strategy / Governance: ..."
- **THEN** the skill writes the item to that project and category and asks nothing

#### Scenario: Destination chosen earlier in the session

- **WHEN** the user has already chosen a project and category this session
- **THEN** subsequent items go to the same place without re-asking


### Requirement: Item grammar

An item SHALL occupy one line with fields in fixed order: text, optional `find:`,
required `opened`.

```
- [ ] **PREFIX-NNNN** — Item text · opened YYYY-MM-DD
- [ ] **PREFIX-NNNN** — Item text · find: locator · opened YYYY-MM-DD
```

Fields SHALL be separated by ` · ` (space, U+00B7, space) and the ID separated
from the text by ` — ` (space, U+2014, space). The ID prefix SHALL match the
file's `scope_prefix`. Item text SHALL NOT contain `·`, `—`, or a line break. The
checkbox SHALL always be `[ ]`; a `[x]` SHALL fail validation. There SHALL be no
path field.

#### Scenario: Valid item with no locator

- **WHEN** `- [ ] **VP-0001** — Governance checks settled with the owner · opened 2026-08-27` is validated
- **THEN** validation passes

#### Scenario: Ticked checkbox

- **WHEN** an item carries `[x]`
- **THEN** validation fails, stating that closing deletes the line rather than
  ticking it

### Requirement: Closing an item

Closing an item SHALL delete its line from the file. There SHALL be no closed
section, no closed date, no sweep, and no archive file. Before deleting, the
skill SHALL report each deleted line in full in the conversation, because that
report is the only record that will exist afterwards.

#### Scenario: User closes an item

- **WHEN** the user names an open item to cross off
- **THEN** the skill prints the full line, deletes it, and updates `updated` in
  the frontmatter

#### Scenario: Legacy closed section present

- **WHEN** a file still carries a `## Closed` heading
- **THEN** validation fails naming the heading

### Requirement: Completion is the user's decision

Nothing SHALL observe whether work is finished. An item SHALL remain open until
the user explicitly says to close it, however long that takes. The skill SHALL
NOT propose closing an item on the grounds that work on it was seen during a
session.

#### Scenario: Work observed during the session

- **WHEN** the skill has seen substantial work on an open item this session
- **THEN** it lists the item as open and says nothing about whether it looks
  finished

### Requirement: Item text is a reminder

Item text SHALL answer "what was I doing, and where do I pick it back up?" in one
scannable line. The requirement to phrase text as an outcome that proves
completion SHALL NOT apply. Where the user's phrasing is unclear as a reminder,
the skill SHALL rewrite it and show the user what it wrote.

#### Scenario: Logging a paused thread

- **WHEN** the user says they were drafting an access review memo and stopped
- **THEN** the skill writes a reminder line naming the work and, where one is
  known, a `find:` locator

### Requirement: Session-end review

At the end of a session the skill SHALL list what is open in a single message,
ask which items to cross off, delete only those the user names, and propose items
for work started this session that is not yet on the list. It SHALL propose only
work it actually observed.

#### Scenario: Ending a session

- **WHEN** the user says "end session"
- **THEN** the skill runs `status.py --items`, lists everything open in one
  message, and asks which to cross off
