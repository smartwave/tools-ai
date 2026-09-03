# policy/

**Rules as data** — the normative controls in machine-readable form, so an agent
can decide what a given asset *must do*, not just what it is called. Where
`vocabulary/` says what values a field can hold, `policy/` says what each value
*requires*.

| File | What it owns |
|------|--------------|
| [`tier-controls.yaml`](tier-controls.yaml) | Tier → required track, oversight, records, gates, approvals; shape/data modifiers; invariants. |
| [`standards.yaml`](standards.yaml) | Index of the B1.x Required Controls (id → title, level, tiers, Confluence anchor). |
| [`gates.yaml`](gates.yaml) | Lifecycle gates (Gate 1, pre-flight) with entry/exit criteria and produced records. |

## Provenance tags (read before enforcing)

- `[REF Bx]` — Required Control, live standard v{{AI_STANDARD_VERSION}}.
  Enforceable now.
- `[REC]` — Recommended Pattern (SHOULD/MAY). Guidance, not a gate.
- `[REF insert]` — pending {{AI_STANDARD_PENDING_VERSION}} naming/tagging
  control. **Do not enforce until ratified.**
- `[PROPOSED]` — inferred, unconfirmed. Surface for review; do not enforce.

Reconciled against the live *AI Solution Standards* (Confluence
`{{PAGE_ID_AI_STANDARDS}}`), **v{{AI_STANDARD_VERSION}}**, on 2026-07-15.
