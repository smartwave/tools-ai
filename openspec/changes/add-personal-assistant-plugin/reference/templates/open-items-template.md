---
title: Open Items — [SCOPE NAME]
scope_prefix: [PREFIX]
next_id: 1
updated: [YYYY-MM-DD]
---

# Open Items — [SCOPE NAME]

Format: `LEDGER-SPEC.md` in the open-items skill. Do not change field names or
order without updating the spec.

Write item text as the **outcome**, not the activity. "Three CI checks implemented
and passing" — not "look at the CI checks."

## Open

<!--
Grammar:
- [ ] **PREFIX-NNNN** — Item text · opened YYYY-MM-DD
- [ ] **PREFIX-NNNN** — Item text · opened YYYY-MM-DD · relative/path.md

Separators are ` · ` (middle dot) between fields and ` — ` (em dash) after the ID.
Neither character may appear in the item text.
-->

## Closed

<!--
- [x] **PREFIX-NNNN** — Item text · opened YYYY-MM-DD · closed YYYY-MM-DD

Swept (deleted) once the closed date is more than 7 days old. Git history is the
archive; there is no archive file.
-->
