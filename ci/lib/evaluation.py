"""Evaluation-set convention (AIDLC Stages 3 and 6).

The evaluation set defines what "correct" means and the acceptable error rate
BEFORE the thing is built; results are measured against it afterwards. The file
layout is this toolkit's own design (no policy file defines it):

  assets/<asset_id>/evaluation/eval-set.yaml
  assets/<asset_id>/evaluation/results/<YYYY-MM-DD>-<label>.yaml
"""

import glob
import os

from . import governance as gov
from .loader import load_yaml
from .report import Report

MIN_CASES = 20            # AIDLC range is 20-100; below 20 warns
MIN_RUNS = 3              # AIDLC asks for 3 runs; fewer warns
CASE_KINDS = ["routine", "edge", "ambiguous", "insufficient-information", "known-hard"]

EVAL_SET_REQUIRED = [
    "owner", "scoring_method", "acceptable_error_rate", "error_rate_reasoning",
    "declared_date", "cases",
]
RESULT_REQUIRED = [
    "run_date", "runs", "model", "model_version", "prompt_version",
    "error_rate_range", "reviewed_by",
]


def eval_dir(manifest):
    return os.path.join(gov.asset_dir(manifest), "evaluation")


def eval_set_path(manifest):
    return os.path.join(eval_dir(manifest), "eval-set.yaml")


def result_paths(manifest):
    return sorted(glob.glob(os.path.join(eval_dir(manifest), "results", "*.yaml")))


def _as_date(value):
    return str(value) if value is not None else None


def evaluate(manifest, path, config, policy=None):
    """Run the evaluation checks for one manifest and return the Report."""
    report = Report("check-evaluation", path, config)
    tier, _, _ = gov.effective_tier(manifest, policy)
    tier_1 = tier < 2

    def problem(control, message):
        if tier_1:
            report.warn(control, message + " (tier 1: recommended)")
        else:
            report.fail(control, message)

    set_path = eval_set_path(manifest)
    if not os.path.exists(set_path):
        problem("Standards 4.4", "%s: no evaluation set at %s — define 'correct' "
                                 "and the acceptable error rate before building"
                % (path, set_path))
        return report

    eval_set = load_yaml(set_path)
    for field in EVAL_SET_REQUIRED:
        if not eval_set.get(field):
            problem("Standards 4.4", "%s: missing '%s'" % (set_path, field))

    cases = eval_set.get("cases") or []
    if len(cases) < MIN_CASES:
        report.warn("Standards 4.4",
                    "%s: %d cases — the AIDLC range is %d-100"
                    % (set_path, len(cases), MIN_CASES))
    present_kinds = set(case.get("kind") for case in cases if isinstance(case, dict))
    for kind in CASE_KINDS:
        if kind not in present_kinds:
            report.warn("Standards 4.4", "%s: no case of kind '%s'" % (set_path, kind))
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            problem("Standards 4.4", "%s: case %d is not a mapping" % (set_path, index))
            continue
        if not case.get("id"):
            problem("Standards 4.4", "%s: case %d has no id" % (set_path, index))
        if not case.get("input") and not case.get("input_ref"):
            problem("Standards 4.4",
                    "%s: case '%s' has neither input nor input_ref"
                    % (set_path, case.get("id")))
        if case.get("expected") in (None, ""):
            problem("Standards 4.4",
                    "%s: case '%s' has no expected result" % (set_path, case.get("id")))

    results = result_paths(manifest)
    if not results:
        problem("Standards 4.5", "%s: no results under %s — the evaluation set has "
                                 "never been run" % (path, os.path.join(eval_dir(manifest), "results")))
        return report

    loaded = []
    for result_path in results:
        data = load_yaml(result_path)
        for field in RESULT_REQUIRED:
            if data.get(field) in (None, "", []):
                problem("Standards 4.5", "%s: missing '%s'" % (result_path, field))
        loaded.append((result_path, data))

    # Ordering: the threshold must have been declared before any result existed.
    declared = _as_date(eval_set.get("declared_date"))
    run_dates = [(_as_date(d.get("run_date")), p) for p, d in loaded if d.get("run_date")]
    if declared and run_dates:
        earliest, earliest_path = min(run_dates)
        if declared >= earliest:
            problem("Standards 4.4",
                    "%s: acceptable_error_rate declared %s, but results exist from "
                    "%s (%s) — the threshold must be agreed before results exist"
                    % (set_path, declared, earliest, earliest_path))

    # Latest result against the threshold.
    latest_path, latest = max(loaded, key=lambda item: (_as_date(item[1].get("run_date")) or "", item[0]))
    report.notice("latest result: %s" % latest_path)

    runs = latest.get("runs")
    if isinstance(runs, int) and runs < MIN_RUNS:
        report.warn("Standards 4.5", "%s: %d run(s) — the AIDLC asks for %d"
                    % (latest_path, runs, MIN_RUNS))

    threshold = eval_set.get("acceptable_error_rate")
    observed = (latest.get("error_rate_range") or {}).get("max")
    if isinstance(threshold, (int, float)) and isinstance(observed, (int, float)):
        if observed > threshold:
            problem("Standards 4.5",
                    "%s: measured error rate max %s exceeds the acceptable_error_rate "
                    "%s declared in %s" % (latest_path, observed, threshold, set_path))
    elif threshold is not None:
        problem("Standards 4.5", "%s: error_rate_range.max is missing or not a number"
                % latest_path)

    failures_by_kind = latest.get("failures_by_kind") or {}
    for kind in eval_set.get("unacceptable_error_kinds") or []:
        count = failures_by_kind.get(kind)
        if count is None:
            problem("Standards 4.5",
                    "%s: no failures_by_kind entry for the unacceptable error kind "
                    "'%s'" % (latest_path, kind))
        elif count:
            problem("Standards 4.5",
                    "%s: %s failure(s) of the unacceptable error kind '%s' — zero is "
                    "the only passing count" % (latest_path, count, kind))

    reviewer = latest.get("reviewed_by")
    if reviewer:
        report.notice("results reviewed by: %s" % reviewer)
        report.unknowable("Standards 4.5",
                          "whether the reviewer is independent of the builder "
                          "(manifest owner: %s)" % manifest.get("owner"))

    if not report.failures:
        report.ok("Standards 4.4/4.5",
                  "threshold declared before results; latest run within threshold")
    return report


def passes(manifest, path, config, policy=None):
    """True when the evaluation checks pass outright (no failures)."""
    return not evaluate(manifest, path, config, policy).failures
