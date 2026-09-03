# Delta for Evaluation Lifecycle

## ADDED Requirements

### Requirement: Evaluation set format
Each evaluated asset SHALL carry `assets/<asset_id>/evaluation/eval-set.yaml` with: owner (the business owner, not the builder), scoring_method, rubric, acceptable_error_rate, error_rate_reasoning, unacceptable_error_kinds, declared_date, and cases each typed as routine | edge | ambiguous | insufficient-information | known-hard. Fewer than 20 cases or a missing case kind SHALL warn.

#### Scenario: Thin evaluation set
- GIVEN an eval-set with 12 cases and no ambiguous case
- WHEN check-evaluation runs
- THEN warnings name the case count floor and the missing kind, without failing on those alone

### Requirement: Threshold declared before results
`ci/check-evaluation <manifest>` MUST fail when the eval-set `declared_date` is not earlier than the earliest results file's run_date — the acceptable error rate is a standard only if set before results existed. Ordering SHALL be judged from dates inside the files, not filesystem timestamps.

#### Scenario: Threshold set after the fact
- GIVEN results dated before the eval-set's declared_date
- WHEN check-evaluation runs
- THEN it exits 1 stating the threshold must predate results

### Requirement: Results within the declared standard
For effective tier 2+ (tier 1 warns), the latest results file SHALL show `error_rate_range.max` ≤ `acceptable_error_rate` and zero failures in every `unacceptable_error_kinds` category, with `reviewed_by` non-empty and reported. Fewer than 3 runs in a results file SHALL warn (run-to-run variation unmeasured).

#### Scenario: Unacceptable error kind present
- GIVEN results within the error-rate threshold but with one failure of an unacceptable kind
- WHEN check-evaluation runs
- THEN it exits 1 naming the kind — the rate does not excuse the kind

### Requirement: Pre-flight linkage
The pre-flight item `correct-result-defined-and-tested-including-edge-cases` SHALL auto-satisfy only when check-evaluation passes for the asset; otherwise it requires manual evidence like any other item.

#### Scenario: Passing evaluation satisfies the gate item
- GIVEN an asset whose check-evaluation passes
- WHEN check-preflight runs
- THEN that item is satisfied without a manual evidence entry
