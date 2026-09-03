"""
Shared parser for tracker files.

check_ledger.py and status.py both import this. The format is defined once, in
LEDGER-SPEC.md, and read once, here. Do not duplicate parsing logic elsewhere.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# Default location. Override it with the CLAUDE_TASK_TRACKER environment
# variable; nothing else in this skill hard-codes a path.
DEFAULT_TRACKER_DIR = "~/Documents/Claude/Claude Task Tracker"

FILENAME_PREFIX = "OPEN-ITEMS "
FILENAME_GLOB = "OPEN-ITEMS *.md"

SEP = " \u00b7 "          # space middle-dot space
DASH = " \u2014 "         # space em-dash space
LOCATOR_LABEL = "find: "
OPENED_LABEL = "opened "

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
ITEM_RE = re.compile(r"^- \[( |x)\] \*\*([A-Z][A-Z0-9]{1,7})-(\d{4})\*\*" + DASH + r"(.+)$")
PREFIX_RE = re.compile(r"^[A-Z][A-Z0-9]{1,7}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

REQUIRED_FRONTMATTER = ("title", "scope_prefix", "next_id", "updated")


def tracker_dir() -> Path:
    """The one folder. CLAUDE_TASK_TRACKER overrides it, which is how the tests
    run without touching the real folder."""
    return Path(os.environ.get("CLAUDE_TASK_TRACKER", DEFAULT_TRACKER_DIR)).expanduser()


@dataclass
class Item:
    ident: str                  # full ID, e.g. "AISTRAT-0003"
    prefix: str
    number: int
    text: str
    opened: str | None = None
    locator: str | None = None
    category: str = ""          # the "### Heading" the item sits under, "" if none
    checked: bool = False       # checkbox state; a checked item should not exist
    extra_fields: list[str] = field(default_factory=list)
    line_no: int = 0
    raw: str = ""

    @property
    def opened_date(self) -> date | None:
        return _as_date(self.opened)


@dataclass
class Ledger:
    path: Path
    frontmatter: dict = field(default_factory=dict)
    items: list[Item] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    has_open_section: bool = False

    @property
    def prefix(self) -> str:
        return str(self.frontmatter.get("scope_prefix", ""))

    @property
    def project(self) -> str:
        """Project name taken from the filename, which is the naming rule:
        'OPEN-ITEMS <project>.md'."""
        stem = self.path.stem
        if stem.startswith(FILENAME_PREFIX):
            return stem[len(FILENAME_PREFIX):].strip()
        return stem

    @property
    def title(self) -> str:
        return str(self.frontmatter.get("title", self.project))

    @property
    def updated(self) -> str:
        return str(self.frontmatter.get("updated", ""))

    def categories(self) -> dict[str, list[Item]]:
        """Items grouped by category, in the order the categories appear in the
        file. Uncategorised items group under ''."""
        grouped: dict[str, list[Item]] = {}
        for item in self.items:
            grouped.setdefault(item.category, []).append(item)
        return grouped


def _as_date(value: str | None) -> date | None:
    if not value or not DATE_RE.match(value):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _parse_frontmatter(text: str) -> tuple[dict, list[str]]:
    """Minimal YAML frontmatter reader. Flat `key: value` only, which is all the
    format allows. Avoids a pyyaml dependency for a four-key block."""
    errors: list[str] = []
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, ["missing YAML frontmatter block at the top of the file"]

    data: dict = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"frontmatter line is not `key: value`: {line!r}")
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip("'\"")
        if key == "next_id":
            try:
                data[key] = int(value)
            except ValueError:
                errors.append(f"next_id is not an integer: {value!r}")
                data[key] = value
        else:
            data[key] = value
    return data, errors


def parse_item_line(line: str, line_no: int, category: str) -> tuple[Item | None, list[str]]:
    errors: list[str] = []
    match = ITEM_RE.match(line)
    if not match:
        return None, [f"line {line_no}: does not match the item grammar: {line.strip()!r}"]

    checkbox, prefix, number, remainder = match.groups()
    parts = [p.strip() for p in remainder.split(SEP)]

    item = Item(
        ident=f"{prefix}-{number}",
        prefix=prefix,
        number=int(number),
        text=parts[0],
        category=category,
        checked=(checkbox == "x"),
        line_no=line_no,
        raw=line.rstrip("\n"),
    )

    if not item.text:
        errors.append(f"line {line_no}: {item.ident} has empty item text")

    for part in parts[1:]:
        if part.startswith(OPENED_LABEL):
            if item.opened is not None:
                errors.append(f"line {line_no}: {item.ident} has more than one opened field")
            item.opened = part[len(OPENED_LABEL):].strip()
        elif part.startswith(LOCATOR_LABEL):
            if item.locator is not None:
                errors.append(f"line {line_no}: {item.ident} has more than one find field")
            item.locator = part[len(LOCATOR_LABEL):].strip()
        else:
            item.extra_fields.append(part)

    return item, errors


def parse_ledger(path: Path) -> Ledger:
    ledger = Ledger(path=path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        ledger.errors.append(f"cannot read file: {exc}")
        return ledger

    ledger.frontmatter, fm_errors = _parse_frontmatter(text)
    ledger.errors.extend(fm_errors)

    in_open = False
    category = ""

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()

        if stripped.startswith("## ") and not stripped.startswith("### "):
            heading = stripped[3:].strip()
            in_open = heading == "Open"
            category = ""
            if not in_open:
                ledger.errors.append(
                    f"line {line_no}: unexpected section heading {heading!r} "
                    "(the only allowed '##' heading is 'Open')"
                )
            else:
                ledger.has_open_section = True
            continue

        if stripped.startswith("### "):
            if not in_open:
                ledger.errors.append(
                    f"line {line_no}: category heading appears outside the Open section"
                )
            category = stripped[4:].strip()
            if not category:
                ledger.errors.append(f"line {line_no}: category heading has no name")
            continue

        if stripped.startswith("- ["):
            if not in_open:
                ledger.errors.append(
                    f"line {line_no}: item appears outside the Open section"
                )
                continue
            item, item_errors = parse_item_line(line, line_no, category)
            ledger.errors.extend(item_errors)
            if item:
                ledger.items.append(item)

    if not ledger.has_open_section:
        ledger.errors.append("file has no '## Open' section")

    return ledger


def find_ledgers(folder: Path | None = None) -> list[Path]:
    """Discovery is a directory listing. The filename is the registration."""
    folder = (folder or tracker_dir()).expanduser()
    if not folder.is_dir():
        return []
    return sorted(folder.glob(FILENAME_GLOB))
