# skills/

Built skills — packaged instructions that make one kind of task repeatable (a
drafting style, a checklist workflow, a report format). One subfolder per
skill, lowercase-with-hyphens, each containing a `README.md` and `SPEC.md` from
`_templates/`.

## Governance skills

These five arrived with the governance layer (2026-08-25 consolidation of the
`ai-org-management` repo into this repo's root). They operate **on this repo's
rule files** — governance operations, not general solution-building — and are
covered by `GOVERNANCE-SPEC.md` at the repo root rather than individual SPECs.

| Skill | Does |
|-------|------|
| [`classify-workload/`](classify-workload/) | Given a description, propose workload type / shape / tier and the resulting requirements from `policy/tier-controls.yaml`. |
| [`mint-asset-id/`](mint-asset-id/) | Register a new `{{ASSET_ID_PREFIX}}*` id in `registry/registry.yaml` at Gate 1. |
| [`author-manifest/`](author-manifest/) | Emit a manifest that validates against `schemas/manifest.schema.json`. |
| [`project-tags/`](project-tags/) | Generate AWS tag / GitHub topic sets from a manifest per `projections/tag-map.yaml`. |
| [`confluence-projection/`](confluence-projection/) | Regenerate a paste-ready insert from repo values (draft only; never publishes). |

**Scope guard:** these skills govern *this repo's* governance artifacts.
Authoring assets for deployed solutions belong in `<domain>-claude-*` repos
under the naming grammar, not here — keep the governance layer the inventory
substrate, not an app.

**Status:** stubs. None is implemented.
