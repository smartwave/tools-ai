---
name: mint-asset-id
description: >
  Register a new {{ASSET_ID_PREFIX}}* asset id in the registry at Gate 1. STUB — not yet
  implemented.
version: 0.0.0
status: stub
---

# mint-asset-id (stub)

## Intent
Mint an immutable `{{ASSET_ID_PREFIX}}<DOMAIN>-<SLUG>` id (`vocabulary` → `asset_id`) and
append an entry to `registry/registry.yaml` when an asset comes in scope
(Gate 1).

## Must honor
- Uppercase, hyphen-separated, matches `^{{ASSET_ID_PREFIX}}[A-Z0-9]+(-[A-Z0-9]+)+$`
  (the adopter substitutes a literal `{{ASSET_ID_PREFIX}}` first).
- **Never reuse or reassign** an id; retire in place.
- Append only — do not rewrite existing entries.
- Minting is a Gate-1 action; confirm requirements are approved first.

## TODO
- [ ] Check uniqueness against registry.
- [ ] Validate the pattern.
- [ ] Append entry (asset_id, name, workload_type, domain, vendor, lives_in, lifecycle).
