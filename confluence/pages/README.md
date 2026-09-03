# confluence/pages/

**Full-page authoritative sources.** Each file here is the source of record for
one Confluence page. On merge to `main`, the `confluence-sync` workflow renders
the file and **replaces the entire body** of the corresponding page.

> This inverts the repo's usual "values here / prose in Confluence" split *for
> these documents specifically*: the prose now lives here and Confluence is its
> projection. That is a deliberate choice — the reviewed PR is the change gate.

## File convention

Each `<page-name>.md` is named for the page it carries (not its numeric id) and
starts with YAML front matter — which holds the `page_id` — then the full page
body in Markdown:

```yaml
---
page_id: "{{PAGE_ID_AI_STANDARDS}}"
space: "{{WIKI_SPACE_KEY}}"
title: "{{ORG_NAME}} AI Solution Standards: Deploying AI Solutions"
owner: "{{AI_GOVERNANCE_OWNER}}"   # must match the required CODEOWNERS reviewer
sync: true                         # false = never auto-publish this page
---
# Page body starts here...
```

`sync: false` keeps a source in the repo but excludes it from auto-publish.

## Seeding a source faithfully (do this first)

Do **not** hand-type page bodies. Capture the current live content from the API
so the first sync is a near no-op and fidelity is exact:

```
ci/pull-page {{PAGE_ID_AI_STANDARDS}} > confluence/pages/ai-solution-standards.md   # then add front matter
```

See [`../../ci/pull-page`](../../ci/pull-page).

## Fidelity — verify before enabling writes

Markdown → Confluence storage conversion is lossy. Tables, panels, status
lozenges, `<custom data-type="date">` nodes, smart links, and macros can
degrade. Before flipping the workflow off dry-run:

1. Seed the source via `pull-page`.
2. Run the workflow in **dry-run** (its default) and review the rendered diff.
3. Only then set the publish job live.

## Ownership prerequisites

- **`agentic-sdlc-platform.md`** projects into a page that **does not exist
  yet** — the adopting organization creates it in `{{WIKI_SPACE_KEY}}` (or the
  equivalent in whatever knowledge tool it uses) and records the id as
  `{{PAGE_ID_AGENTIC_SDLC}}`. Before wiring it in: create the page, grant the
  service account write access to that space, substitute
  `{{PLATFORM_SECURITY_LEAD_ROLE}}`, and set the matching CODEOWNERS reviewer.
  `sync: false` until all four are done.
- A service account can only publish where its Confluence permissions allow.
