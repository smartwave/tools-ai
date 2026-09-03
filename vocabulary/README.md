# vocabulary/

The controlled **values** — the source of truth for every enumerated field used
in repository names, governance manifests, AWS tags, and GitHub topics.

- [`vocabulary.yaml`](vocabulary.yaml) — repository grammar, the four workload
  types, `shape`, and the AI-governance overlays (`tier`, `track`, `oversight`,
  `data_class`, `lifecycle`), plus the `asset_id` grammar and tag/topic prefixes.

**Do not restate these values elsewhere.** `policy/`, `schemas/`, and
`projections/` reference them; Confluence references them as prose. If a value
changes, it changes here and nowhere else.
