---
name: project-tags
description: >
  Generate AWS resource tags and GitHub topics from a manifest. STUB — not yet
  implemented.
version: 0.0.0
status: stub
---

# project-tags (stub)

## Intent
From a validated manifest, generate the `{{TAG_NAMESPACE}}:*` AWS tag set and the
`{{TAG_NAMESPACE}}-*` / `{{TAG_NAMESPACE}}-ai-*` GitHub topic set per
`projections/tag-map.yaml`, always including the `{{TAG_NAMESPACE}}-ai-governed`
marker topic.

## Must honor
- **Never** project environment, owner, business_unit, or any customer/secret/
  financial value into a public GitHub topic. Those go to the manifest and AWS
  tags only.
- Respect the platform limits (GitHub: lowercase/numbers/hyphens, ≤50 chars, ≤20
  topics; AWS: ≤50 tags, key ≤128, value ≤256, `aws:` reserved).

## TODO
- [ ] Read tag-map + manifest.
- [ ] Emit tag set and topic set separately.
- [ ] Assert the public-topic exclusions.
