# registry/

The org-wide AI **inventory** — the `{{ASSET_ID_PREFIX}}*` asset-ID namespace.

- [`registry.yaml`](registry.yaml) — one entry per in-scope AI asset. The
  `asset_id` is minted here at Gate 1 and is **immutable**: never reused, never
  reassigned. Retire in place (`lifecycle: retired`).

This registry plus the `{{TAG_NAMESPACE}}-ai-governed` marker topic constitute the shared AI
solution inventory the standard monitors. A repo or resource running an in-scope
asset without them is shadow AI.

**Editing rule:** append new entries; do not rewrite or renumber existing IDs.
