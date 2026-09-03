"""YAML/JSON loading with error messages that carry file and line."""

import json
import os
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - environment problem, not a rule violation
    sys.stderr.write(
        "missing dependency: PyYAML. Install with: "
        "pip install -r ci/requirements.txt\n")
    raise SystemExit(4)


class DataError(Exception):
    """A file could not be read or parsed. Message names file and line."""


def load_yaml(path):
    try:
        with open(path) as handle:
            text = handle.read()
    except IOError as exc:
        raise DataError("%s: cannot read (%s)" % (path, exc.strerror))
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        where = ":%d" % (mark.line + 1) if mark is not None else ""
        raise DataError("%s%s: invalid YAML (%s)"
                        % (path, where, getattr(exc, "problem", exc)))
    return data if data is not None else {}


def load_json(path):
    try:
        with open(path) as handle:
            text = handle.read()
    except IOError as exc:
        raise DataError("%s: cannot read (%s)" % (path, exc.strerror))
    try:
        return json.loads(text)
    except ValueError as exc:
        raise DataError("%s: invalid JSON (%s)" % (path, exc))


def find_line(path, needle):
    """1-based line number of the first line containing `needle`, or None.

    Used to point a violation message at the offending line without carrying a
    full position-tracking YAML loader.
    """
    if not needle or not os.path.exists(path):
        return None
    try:
        with open(path) as handle:
            for number, line in enumerate(handle, start=1):
                if str(needle) in line:
                    return number
    except IOError:
        return None
    return None


def where(path, needle=None):
    """'path:line' when the line can be located, else 'path'."""
    line = find_line(path, needle) if needle else None
    return "%s:%d" % (path, line) if line else path
