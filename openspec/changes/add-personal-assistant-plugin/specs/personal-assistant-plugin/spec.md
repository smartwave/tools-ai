# Delta for Personal Assistant Plugin

## Purpose

The packaging contract. Defines the `personal-assistant` plugin's layout and
metadata, the marketplace index that makes it installable from GitHub, and the
self-containment rule that keeps a skill usable when copied out of the plugin by
hand. This is the contract read by whoever adds a skill to the plugin, and by
whoever installs it.

## ADDED Requirements

### Requirement: Plugin Layout

The plugin MUST live at `plugins/personal-assistant/` and MUST carry
`.claude-plugin/plugin.json`. Plugin content — `skills/`, and any future
`commands/`, `agents/`, or `hooks/hooks.json` — MUST sit at the plugin root and
MUST NOT sit inside `.claude-plugin/`. The plugin MUST carry `README.md` and
`SPEC.md` derived from `_templates/`, per the repository's tool conventions.

#### Scenario: Skill placed inside the metadata folder

- GIVEN a skill added at `plugins/personal-assistant/.claude-plugin/skills/foo/`
- WHEN the plugin is installed
- THEN the layout is wrong and the skill is not loaded

#### Scenario: Second personal skill added later

- GIVEN a new personal-productivity skill
- WHEN it is added at `plugins/personal-assistant/skills/<name>/`
- THEN no plugin rename, no new plugin, and no new marketplace entry is required

### Requirement: Plugin Metadata

`plugin.json` MUST carry `name`, `version`, and `description`, and SHOULD carry
`displayName`, `author`, and `keywords`. `name` MUST be kebab-case and MUST equal
the plugin's directory name. `version` MUST be semver. `displayName` MUST be
`Personal Assistant`.

The plugin MUST NOT use `{{...}}` placeholder tokens. It is personal tooling
outside the repository's placeholder edition, and its `README.md` MUST state that
exception so it is not read as an oversight.

#### Scenario: Name disagrees with directory

- GIVEN `plugins/personal-assistant/` whose `plugin.json` names `personal-assistant`
- WHEN the plugin is validated
- THEN it fails, naming the mismatch

#### Scenario: Placeholder token in the plugin

- GIVEN `"author": {"name": "{{ORG_NAME}}"}` in the plugin
- WHEN the plugin is reviewed
- THEN it fails, because this plugin is outside the placeholder edition

### Requirement: Skill Frontmatter

Every `SKILL.md` under the plugin MUST carry YAML frontmatter with at least `name`
and `description`. `name` MUST equal the skill's directory name. `description` MUST
name the natural-language phrases that trigger the skill, so it is selectable
without the user knowing the skill exists.

#### Scenario: Description without triggers

- GIVEN a description reading only "Tracks open items"
- WHEN a user says "log where I am"
- THEN the skill may not be selected, and the description fails this requirement

### Requirement: Skill Folder Is Self-Contained

A skill folder MUST be functional when copied out of the plugin and placed
anywhere Claude reads skills, with no other file from this plugin or repository
present. Every path referenced from `SKILL.md` MUST resolve relative to the skill
folder, or MUST come from user configuration that has a documented default.

Shared code between skills MUST NOT be introduced at the plugin root; a module
needed by two skills MUST be duplicated into each. A skill MUST NOT reference a
plugin-root `references/` folder, and MUST NOT reference any repository path.

#### Scenario: Skill folder copied to an empty directory

- GIVEN `skills/open-items/` copied alone to a directory outside any repository
- WHEN the validator is run against a ledger there
- THEN it runs and reports correctly, with nothing else present

#### Scenario: Shared module proposed at the plugin root

- GIVEN a second skill needing `ledger.py`
- WHEN the module is moved to a plugin-root `lib/`
- THEN this requirement fails; the module is duplicated into the second skill
  instead

#### Scenario: External dependency that is not a file

- GIVEN the collector's `~/.open-items/config.yaml`
- WHEN the skill folder is copied out
- THEN the dependency is permitted, because it is user configuration with a
  documented default and a `--config` override
- AND the plugin `README.md` states it as the only external dependency

### Requirement: Marketplace Index

The repository MUST carry `.claude-plugin/marketplace.json` at its root, holding a
kebab-case marketplace `name`, an owner block, and a `plugins` array. Each entry
MUST carry `name`, `source` as a path relative to the repository root, and
`description`, and MUST list every plugin under `plugins/`. There MUST be exactly
one marketplace index in the repository.

Each entry's `name` and `version` MUST equal the values in that plugin's
`plugin.json`. This match is not machine-checked in this change and MUST be
verified by hand before commit.

#### Scenario: Plugin present but unlisted

- GIVEN `plugins/grc-core/` exists
- WHEN the marketplace index omits it
- THEN the index fails this requirement

#### Scenario: Version bumped in one place only

- GIVEN `plugin.json` moved to `1.1.0` and the marketplace entry left at `1.0.0`
- WHEN the change is reviewed
- THEN it fails, naming both files

### Requirement: Installation Path Documented

The plugin `README.md` MUST document both distribution paths: installation from
GitHub via the marketplace, and copying the skill folder by hand. It MUST state
that the repository is private and that marketplace installation therefore
requires git credentials for it.

#### Scenario: A person without repository access

- GIVEN someone who cannot clone the repository
- WHEN they read the README
- THEN the hand-copy path is documented and usable without repository access
