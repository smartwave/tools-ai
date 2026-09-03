# Delta for Open Items Rollup

## Purpose

Finding every ledger, checking it against the format contract, and merging the open
items into one view. Covers the validator, the collector, discovery by filesystem
scan, and where the rollup is written.

## ADDED Requirements

### Requirement: Single Parser Implementation

The parsing of ledger files MUST exist in exactly one module, imported by both the
validator and the collector. Parsing logic MUST NOT be duplicated, because two
implementations of one format will drift and the drift will be silent.

#### Scenario: Format changes

- GIVEN the item grammar is amended
- WHEN the parser is updated
- THEN both the validator and the collector pick up the change with no second edit

### Requirement: Validator

A validator MUST check a ledger against the format contract and MUST exit non-zero
on any failure. It MUST report every error found, each naming the line number and
item ID where applicable, rather than stopping at the first. It MUST accept a single
file, a list of files, or a root directory to scan. It MUST detect, at minimum:
missing or malformed frontmatter, an invalid or mismatched `scope_prefix`, a
`next_id` that would reuse an existing ID, duplicate IDs, unexpected section
headings, items outside a section, checkbox state contradicting the section, a
missing or malformed `opened` date, a closed item without a `closed` date, an open
item carrying a `closed` date, a `closed` date earlier than the `opened` date, a
reserved separator character in item text, and a path field containing spaces.

#### Scenario: Multiple errors in one file

- GIVEN a ledger with four distinct format errors
- WHEN the validator runs
- THEN all four are reported
- AND the exit code is non-zero

#### Scenario: Path field contains spaces

- GIVEN an item whose path field reads `middot in it`
- WHEN the validator runs
- THEN it reports that a stray separator has probably split the item text

### Requirement: Discovery by Filesystem Scan

The collector MUST locate ledgers by recursively scanning configured root
directories for files named `OPEN-ITEMS.md`. It MUST NOT read a registry file. It
MUST always skip `.git`, `node_modules`, `_archive` and `__pycache__` regardless of
configuration, and MUST additionally honour user-configured exclude patterns. It
MUST de-duplicate by resolved path so a symlinked or nested root does not produce
the same ledger twice.

#### Scenario: New ledger added

- GIVEN a new folder under a scan root containing an `OPEN-ITEMS.md`
- WHEN the collector runs
- THEN the ledger appears in the rollup with no configuration change

#### Scenario: Archived content under a scan root

- GIVEN an `OPEN-ITEMS.md` inside an `_archive` directory
- WHEN the collector runs
- THEN it is skipped

### Requirement: Duplicate Prefix Detection

Because nothing centrally enforces prefix uniqueness, the collector MUST detect two
ledgers claiming the same `scope_prefix` at scan time and MUST report both file
paths. It MUST report the conflict rather than resolving it.

#### Scenario: Two ledgers share a prefix

- GIVEN two ledgers both using `TAI`
- WHEN the collector runs
- THEN both paths are reported as a problem in the rollup output

### Requirement: Collector Is Deterministic

The collector MUST be a plain script with no model involved, so that it can be run
on a schedule at no cost and cannot invent, omit or paraphrase an item. It MUST NOT
modify any ledger.

#### Scenario: Collector run twice on unchanged ledgers

- GIVEN no ledger has changed between runs
- WHEN the collector runs a second time
- THEN the rollup content is identical apart from the generation date
- AND no ledger file has been modified

### Requirement: Rollup Output

The collector MUST write the rollup as both Markdown and JSON to a configured output
directory. It MUST group items by scope, MUST sort items oldest first by `opened`
date, and MUST state each ledger's `updated` date alongside its items so a scope
that has not been reconciled is visible rather than silently stale. It MUST report
any format errors it encountered as problems rather than failing the whole run. It
MUST support writing additional copies of the Markdown rollup to configured paths,
so the rollup can land somewhere the user already looks.

#### Scenario: One ledger is malformed

- GIVEN three ledgers, one of which fails to parse cleanly
- WHEN the collector runs
- THEN the other two are still rolled up
- AND the malformed ledger is named in a problems section

#### Scenario: Rollup delivered to the vault

- GIVEN an extra output path inside an Obsidian vault
- WHEN the collector runs
- THEN the Markdown rollup is written there as well as to the output directory

### Requirement: Rollup Is Read-Only Downstream

The rollup MUST be treated as a rendering payload, regenerated from the ledgers on
every run, and MUST NOT be a second source of truth. Nothing downstream of the
collector MAY write back to a ledger.

#### Scenario: Rollup edited by hand

- GIVEN a user edits `rollup.md`
- WHEN the collector next runs
- THEN the edit is overwritten
- AND no ledger reflects the edit

### Requirement: Configuration

Configuration MUST consist of a single file outside any scope, holding scan roots,
exclude patterns, the output directory, and any extra output paths. It MUST NOT hold
per-ledger data. When the configuration file is absent, the collector MUST fall back
to defaults and MUST say so rather than failing.

#### Scenario: No configuration present

- GIVEN no configuration file exists
- WHEN the collector runs
- THEN default scan roots are used
- AND a notice is written to standard error

### Requirement: Continuous Integration Validation

Each repository holding a ledger MUST validate its own ledgers on push. Continuous
integration MUST NOT attempt to produce a rollup, because a hosted runner receives a
clone of one repository and cannot see other repositories, vaults, or local folders.

#### Scenario: Malformed ledger pushed

- GIVEN a commit containing a ledger that fails validation
- WHEN the workflow runs
- THEN the job fails and names the errors

### Requirement: Portable Dependencies

Scripts MUST declare their own dependencies inline so that a new machine requires
only a clone and a single runner tool, with no virtual environment to create and no
requirements file to maintain separately.

#### Scenario: Fresh machine

- GIVEN a machine with the runner installed and the repository cloned
- WHEN the collector is invoked
- THEN dependencies resolve automatically and the run succeeds
