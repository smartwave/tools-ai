"""
Shared parser for OPEN-ITEMS.md ledgers.

Both check_ledger.py and collect.py import this. Do not duplicate parsing logic
into either of them — the format is defined once, in LEDGER-SPEC.md, and read
once, here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

LEDGER_FILENAME = "OPEN-ITEMS.md"

SEP = " \u00b7 "          # space middle-dot space
DASH = " \u2014 "         # space em-dash space

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
ITEM_RE = re.compile(r"^- \[( |x)\] \*\*([A-Z][A-Z0-9]{1,7})-(\d{4})\*\*" + DASH + r"(.+)$")
PREFIX_RE = re.compile(r"^[A-Z][A-Z0-9]{1,7}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

REQUIRED_FRONTMATTER = ("title", "scope_prefix", "next_id", "updated")


@dataclass
class Item:
    ident: str                  # full ID, e.g. "TAI-0014"
    prefix: str
    number: int
    text: str
    opened: str | None = None
    closed: str | None = None
    path: str | None = None
    is_closed: bool = False     # checkbox state
    section: str = ""           # "Open" or "Closed"
    line_no: int = 0
    raw: str = ""

    @property
    def opened_date(self) -> date | None:
        return _as_date(self.opened)

    @property
    def closed_date(self) -> date | None:
        return _as_date(self.closed)


@dataclass
class Ledger:
    path: Path
    frontmatter: dict = field(default_factory=dict)
    items: list[Item] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def prefix(self) -> str:
        return str(self.frontmatter.get("scope_prefix", ""))

    @property
    def title(self) -> str:
        return str(self.frontmatter.get("title", self.path.parent.name))

    @property
    def updated(self) -> str:
        return str(self.frontmatter.get("updated", ""))

    @property
    def scope(self) -> str:
        """Human label for where this ledger lives."""
        return self.path.parent.name

    def open_items(self) -> list[Item]:
        return [i for i in self.items if not i.is_closed]

    def closed_items(self) -> list[Item]:
        return [i for i in self.items if i.is_closed]


def _as_date(value: str | None) -> date | None:
    if not value or not DATE_RE.match(value):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _parse_frontmatter(text: str) -> tuple[dict, list[str]]:
    """Minimal YAML frontmatter reader. Flat key: value only, which is all the
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


def parse_item_line(line: str, line_no: int, section: str) -> tuple[Item | None, list[str]]:
    errors: list[str] = []
    match = ITEM_RE.match(line)
    if not match:
        return None, [f"line {line_no}: does not match the item grammar: {line.strip()!r}"]

    checkbox, prefix, number, remainder = match.groups()
    parts = [p.strip() for p in remainder.split(SEP)]
    text = parts[0]

    item = Item(
        ident=f"{prefix}-{number}",
        prefix=prefix,
        number=int(number),
        text=text,
        is_closed=(checkbox == "x"),
        section=section,
        line_no=line_no,
        raw=line.rstrip("\n"),
    )

    if not text:
        errors.append(f"line {line_no}: {item.ident} has empty item text")

    for part in parts[1:]:
        if part.startswith("opened "):
            item.opened = part[len("opened "):].strip()
        elif part.startswith("closed "):
            item.closed = part[len("closed "):].strip()
        elif part:
            if item.path is not None:
                errors.append(f"line {line_no}: {item.ident} has more than one path field")
            item.path = part

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

    section = ""
    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("## "):
            heading = stripped[3:].strip()
            section = heading if heading in ("Open", "Closed") else ""
            if heading not in ("Open", "Closed"):
                ledger.errors.append(
                    f"line {line_no}: unexpected section heading {heading!r} "
                    "(only '## Open' and '## Closed' are allowed)"
                )
            continue
        if stripped.startswith("- ["):
            if not section:
                ledger.errors.append(f"line {line_no}: item appears outside Open/Closed section")
                continue
            item, item_errors = parse_item_line(line, line_no, section)
            ledger.errors.extend(item_errors)
            if item:
                ledger.items.append(item)

    return ledger


def find_ledgers(roots: list[Path], excludes: list[str]) -> list[Path]:
    """Discovery: the filename is the registration."""
    found: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        root = root.expanduser()
        if not root.is_dir():
            continue
        for candidate in root.rglob(LEDGER_FILENAME):
            resolved = candidate.resolve()
            if resolved in seen:
                continue
            if any(candidate.match(pattern) for pattern in excludes):
                continue
            if any(part in {".git", "node_modules", "_archive", "__pycache__"}
                   for part in candidate.parts):
                continue
            seen.add(resolved)
            found.append(candidate)
    return sorted(found)
