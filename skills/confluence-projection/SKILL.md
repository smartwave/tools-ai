---
name: confluence-projection
description: >
  Regenerate a paste-ready Confluence insert from current repo values. Drafts
  only; never publishes. STUB — not yet implemented.
version: 0.0.0
status: stub
---

# confluence-projection (stub)

## Intent
Regenerate the paste-ready insert for a Confluence page (per
`confluence/sync-map.yaml`) from current repo values, so the prose surface stays
a projection of this repo rather than drifting.

## Must honor
- **Draft only.** Write the insert into `confluence/inserts/` and stop. Do not
  update a live Confluence page.
- Publishing to Confluence is an outward action requiring explicit human
  approval; a page whose `owner` differs from the requester needs that owner's
  sign-off (e.g. the {{PLATFORM_SECURITY_LEAD_ROLE}} for page
  `{{PAGE_ID_AGENTIC_SDLC}}`).
- Carry the correct SemVer bump and a changelog row in the insert.

## TODO
- [ ] Resolve the page's `projects_from` sources.
- [ ] Render the insert with provenance and changelog.
- [ ] Emit as a draft file; surface the required approvals.
