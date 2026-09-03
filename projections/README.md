# projections/

How the manifest **projects** onto downstream discovery surfaces.

- [`tag-map.yaml`](tag-map.yaml) — maps each manifest field to an AWS resource
  tag (`{{TAG_NAMESPACE}}:*`) and/or a GitHub topic (`{{TAG_NAMESPACE}}-*` /
  `{{TAG_NAMESPACE}}-ai-*`).

The manifest is the single source of truth; tags and topics are generated from
it and must not be maintained as a second source. Because **GitHub topics are
public even on private repos**, environment, owner, business unit, and any
customer-identifying, secret, or financial value are confined to the manifest
and AWS tags — never a topic. Enforcement of tag validity is via AWS
Organizations tag policies defined in `aws-org-management`.
