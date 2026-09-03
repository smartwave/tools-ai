# assets/

**Per-asset governance evidence.** One subfolder per minted `asset_id`. The
registry answers *does this id exist*; `assets/<asset_id>/` answers *what has
this asset actually satisfied*.

```
assets/<asset_id>/
  manifest.yaml            # the governance manifest (schemas/manifest.schema.json)
  preflight.yaml           # B1.7 checklist, one entry per item in policy/gates.yaml
  exceptions.yaml          # optional — B1.8 exceptions, one per waived rule
  evaluation/
    eval-set.yaml          # what "correct" means + the acceptable error rate, dated
    results/
      <YYYY-MM-DD>-<label>.yaml
```

The checks in [`ci/`](../ci/README.md) read this layout. `ci/run-all` with no
arguments checks every `assets/*/manifest.yaml`.

## preflight.yaml

Item ids are read from `policy/gates.yaml` (`pre-flight.requires`, plus
`tier_3_additional` at effective Tier 3) — never copied into code, so a policy
edit changes what is required here.

```yaml
items:
  - item: goal-defined-to-root-cause      # an id from policy/gates.yaml
    status: met                           # met | exception | pending
    evidence: https://wiki.example/…      # link or repo path — required for `met`
    checked_by: Dana Example
    date: "2026-03-02"
```

An item marked `met` with empty evidence **fails**: the checklist is an
evidence record, not a box-ticking exercise. `status: exception` requires a
matching, unexpired entry in `exceptions.yaml`.

## exceptions.yaml

```yaml
exceptions:
  - rule: threat-modeled-against-owasp-top-10-agentic-2026   # the item id waived
    reason: Threat model scheduled with Security next sprint.
    compensating_control: Tool allowlist plus rate caps at the gateway.
    accepted_by: Security Lead
    expires: "2026-09-30"
```

## evaluation/

The AIDLC discipline: define what "correct" means and the acceptable error rate
**before** building, then measure against it. `declared_date` in `eval-set.yaml`
must be earlier than the earliest `run_date` in `results/` — ordering is read
from the dates inside the files, never from filesystem timestamps.

```yaml
# eval-set.yaml
owner: Robin Business-Owner        # the business owner, not the builder
scoring_method: rubric-scored by the owner, one point per case
rubric: rubric.md                  # text or path
acceptable_error_rate: 0.05
error_rate_reasoning: >
  Why that number is acceptable for this decision.
unacceptable_error_kinds: [silent-data-loss, wrong-recipient]
declared_date: "2026-01-10"
cases:                             # 20–100; at least one of each kind
  - id: case-01
    input: "…"                     # or input_ref: path
    expected: "…"
    kind: routine                  # routine | edge | ambiguous |
                                   # insufficient-information | known-hard
```

```yaml
# results/2026-03-01-baseline.yaml
run_date: "2026-03-01"
runs: 3                            # the AIDLC asks for 3
model: claude
model_version: …
prompt_version: 1.0.0
scores: [19, 19, 20]
error_rate_range: {min: 0.0, max: 0.04}
failures_by_kind: {silent-data-loss: 0, wrong-recipient: 0}
reviewed_by: Robin Business-Owner
```

Worked fixtures live in `ci/tests/fixtures/assets/`.
