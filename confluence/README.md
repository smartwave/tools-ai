# confluence/

The **prose-projection layer**. Confluence owns the human-readable standard;
this directory maps repo artifacts to the pages they project into and holds the
paste-ready inserts generated from repo values.

| Path | What it is |
|------|-----------|
| [`sync-map.yaml`](sync-map.yaml) | Repo section ↔ Confluence page ↔ owner ↔ live/pending version. |
| [`inserts/`](inserts/) | Paste-ready Markdown inserts, one per pending page change. |

## Write policy

- **Regenerating an insert file here is safe.**
- **Updating a live Confluence page is an outward action** — produce a draft and
  stop for human approval. Never edit a page whose `owner` in `sync-map.yaml`
  differs from the requester without that owner's sign-off. The Agentic SDLC
  page (`{{PAGE_ID_AGENTIC_SDLC}}`) is owned by the
  {{PLATFORM_SECURITY_LEAD_ROLE}}.
