#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
check_ledger.py — validate tracker files against LEDGER-SPEC.md.

Usage:
    uv run check_ledger.py                          # validate every file in the tracker folder
    uv run check_ledger.py "path/to/OPEN-ITEMS Project.md" [more...]
    uv run check_ledger.py --folder "some/folder"   # validate every file in that folder

Exit code 0 = all valid, 1 = at least one error.

Run this after any write. A malformed line is skipped silently when the file is
read back, which produces a list that looks complete and is not — worse than no
list at all.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ledger import (
    DATE_RE,
    FILENAME_PREFIX,
    PREFIX_RE,
    REQUIRED_FRONTMATTER,
    Ledger,
    find_ledgers,
    parse_ledger,
    tracker_dir,
)

FORBIDDEN_IN_TEXT = ("\u00b7", "\u2014")


def validate(ledger: Ledger) -> list[str]:
    errors = list(ledger.errors)
    fm = ledger.frontmatter

    if not ledger.path.name.startswith(FILENAME_PREFIX):
        errors.append(
            f"filename {ledger.path.name!r} does not follow "
            f"'{FILENAME_PREFIX}<project>.md'"
        )

    for key in REQUIRED_FRONTMATTER:
        if key not in fm:
            errors.append(f"frontmatter missing required key: {key}")

    for key in fm:
        if key not in REQUIRED_FRONTMATTER:
            errors.append(f"frontmatter has an unexpected key: {key}")

    prefix = str(fm.get("scope_prefix", ""))
    if prefix and not PREFIX_RE.match(prefix):
        errors.append(
            f"scope_prefix {prefix!r} is invalid — 2-8 characters, uppercase "
            "letters and digits, must start with a letter"
        )

    updated = str(fm.get("updated", ""))
    if updated and not DATE_RE.match(updated):
        errors.append(f"frontmatter updated is not an ISO date: {updated!r}")

    seen: dict[str, int] = {}
    max_number = 0

    for item in ledger.items:
        where = f"line {item.line_no}: {item.ident}"

        if item.ident in seen:
            errors.append(f"{where}: duplicate ID (also on line {seen[item.ident]})")
        seen[item.ident] = item.line_no
        max_number = max(max_number, item.number)

        if prefix and item.prefix != prefix:
            errors.append(
                f"{where}: prefix {item.prefix!r} does not match the file's "
                f"scope_prefix {prefix!r}"
            )

        if item.checked:
            errors.append(
                f"{where}: item is checked [x] — closing an item deletes the "
                "line, it is not ticked off in place"
            )

        for char in FORBIDDEN_IN_TEXT:
            if char in item.text:
                errors.append(
                    f"{where}: item text contains a reserved separator character "
                    f"({char!r}) — use a hyphen or a colon instead"
                )

        for extra in item.extra_fields:
            errors.append(
                f"{where}: unlabelled field {extra!r} — a stray separator has "
                "probably split the item text. Every field after the text must "
                "start with 'find: ' or 'opened '."
            )

        if not item.opened:
            errors.append(f"{where}: missing the opened date")
        elif item.opened_date is None:
            errors.append(f"{where}: opened is not a valid ISO date: {item.opened!r}")

        if item.locator is not None and not item.locator:
            errors.append(f"{where}: find field is empty — leave it off instead")

    next_id = fm.get("next_id")
    if isinstance(next_id, int) and next_id <= max_number:
        errors.append(
            f"frontmatter next_id is {next_id} but the highest existing ID is "
            f"{max_number:04d} — next_id must be greater, or IDs will be reused"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate tracker files.")
    parser.add_argument("paths", nargs="*", type=Path, help="files to validate")
    parser.add_argument("--folder", type=Path, help="validate every file in this folder")
    args = parser.parse_args()

    if args.paths:
        targets = args.paths
    else:
        folder = args.folder or tracker_dir()
        targets = find_ledgers(folder)
        if not targets:
            print(f"no tracker files in {folder}", file=sys.stderr)
            return 0

    failed = False
    prefixes: dict[str, Path] = {}

    for target in targets:
        led = parse_ledger(target)
        errors = validate(led)

        prefix = led.prefix
        if prefix:
            if prefix in prefixes and prefixes[prefix] != target:
                errors.append(
                    f"scope_prefix {prefix!r} is also used by {prefixes[prefix]} — "
                    "prefixes must be unique across files"
                )
            prefixes.setdefault(prefix, target)

        if errors:
            failed = True
            print(f"FAIL  {target}")
            for err in errors:
                print(f"        {err}")
        else:
            print(f"ok    {target}  [{prefix}] {len(led.items)} open")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
