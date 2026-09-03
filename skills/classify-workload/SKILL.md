---
name: classify-workload
description: >
  Propose a workload's type, shape, and tier from a plain-language description,
  then resolve what the AI Solution Standards require of it. STUB — not yet
  implemented.
version: 0.0.0
status: stub
---

# classify-workload (stub)

## Intent
Given a description of a proposed non-product AI solution, determine:
1. **workload_type** — `tool` / `platform` / `service` / `app`, by dependency
   position (`vocabulary/vocabulary.yaml`).
2. **shape** — `workflow` / `agent` / `multi-agent` (`vocabulary`).
3. **tier** — by the worse of harm and independence, then apply modifiers
   (`policy/tier-controls.yaml`).
4. **requirements** — the matched tier row plus modifiers, invariants, and
   `security_triggers`.

## Inputs / outputs (proposed)
- **In:** free-text description; optional known fields.
- **Out:** proposed classification + the required track, oversight envelope,
  records, gates, and approvals, each with its provenance tag.

## Must honor
- Apply `modifiers` (agent → ≥Tier 2; regulated → Tier 3) before reading the
  tier row.
- Never present a `[PROPOSED]` or `[REF insert]` rule as enforceable.
- Classification is a proposal for human confirmation, not an approval.

## TODO
- [ ] Load and parse vocabulary + tier-controls.
- [ ] Implement modifier resolution.
- [ ] Emit a structured classification with citations.
