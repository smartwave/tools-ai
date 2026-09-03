# Delta for Open Items Commands

## Purpose

The three commands a Claude skill exposes for working with ledgers: capturing an
item, reconciling a ledger at the end of a working stretch, and reporting what is
open. Defines what each command does, what it must confirm with the user, and what
it must never do on its own.

## ADDED Requirements

### Requirement: The User Asserts Completion

No command MAY close an item without explicit user confirmation. Tooling MAY propose
closing an item based on work it observed during the current session, but the
proposal MUST be presented and confirmed before the ledger is written. Tooling MUST
NOT infer completion from work it did not observe.

#### Scenario: Agent observed the work

- GIVEN the user ran a test suite successfully during this session
- AND an open item's text describes that suite passing
- WHEN `end-of-session` runs
- THEN the item is proposed for closing, with the observation stated
- AND the item is closed only after the user confirms

#### Scenario: Work done outside any session

- GIVEN the user fixed something without an agent present
- WHEN `end-of-session` runs
- THEN that item is not proposed for closing
- AND it remains open until the user states it is done

### Requirement: Validate After Every Write

Any command that writes to a ledger MUST run the validator against that ledger
afterwards, and MUST fix any failure before ending its turn. A malformed ledger is
skipped silently by the collector, which produces a rollup that appears complete and
is not.

#### Scenario: Write produces a malformed line

- GIVEN a command has written an item
- WHEN validation of that ledger fails
- THEN the command corrects the file and re-validates before returning

### Requirement: Command `log-item`

`log-item` MUST record an item's current state in the current scope's ledger. It
MUST read the ledger first and compare the proposed item against existing **open**
items using the path field and text similarity. On a probable match it MUST update
the existing item rather than create a new one. On an ambiguous match it MUST ask
the user. Closed items MUST NOT be matched against. It MUST NOT prompt for priority,
effort, or dates, because the format has no such fields.

#### Scenario: Duplicate of an existing open item

- GIVEN an open item referencing `ci/check_tier_controls.py`
- WHEN a new item referencing the same path is logged
- THEN the existing item is updated rather than duplicated

#### Scenario: Ambiguous match

- GIVEN an open item whose text is partially similar to the new item
- WHEN `log-item` runs
- THEN the user is asked whether to update the existing item or create a new one

#### Scenario: Match against a closed item

- GIVEN a closed item with text similar to the new item
- WHEN `log-item` runs
- THEN a new item is created, because closed items are not matched against

### Requirement: Command `end-of-session`

`end-of-session` MUST read the ledger's Open list, present all open items in a
single message asking which are done, close the ones the user confirms, and then
sweep closed items older than 7 days. It MUST update the frontmatter `updated` date.
It MAY propose new items for work it observed starting during this session. It MUST
NOT present items one at a time, because a per-item exchange makes a two-minute
operation feel like a meeting and it will be skipped.

#### Scenario: Several items open

- GIVEN a ledger with five open items
- WHEN `end-of-session` runs
- THEN all five are listed in one message
- AND the user answers once

#### Scenario: Sweep during reconciliation

- GIVEN a closed item dated 9 days ago and another dated 2 days ago
- WHEN `end-of-session` runs
- THEN the 9-day-old item is deleted and the 2-day-old item remains

### Requirement: Command `open-items-status`

`open-items-status` MUST report open items. By default it MUST report the current
scope only, oldest first by `opened` date. With an `--all` argument or an equivalent
instruction it MUST run the collector and report across every ledger. If the
collector cannot run in the current surface, it MUST fall back to the last written
rollup and MUST state that rollup's generation date, so a stale rollup is never
presented as current.

#### Scenario: Collector unavailable in this surface

- GIVEN a surface without filesystem access to the scan roots
- WHEN `open-items-status --all` runs
- THEN the last written rollup is reported
- AND its generation date is stated in the response

### Requirement: Ledger Creation on First Use

When a command runs in a folder with no ledger, it MUST offer to create one from the
template and MUST ask the user for a `scope_prefix`. It MUST NOT invent a prefix,
because prefixes must be unique across ledgers and nothing centrally enforces that.

#### Scenario: No ledger present

- GIVEN a folder with no `OPEN-ITEMS.md`
- WHEN `log-item` runs
- THEN the user is offered a new ledger
- AND asked for a scope prefix before anything is written
