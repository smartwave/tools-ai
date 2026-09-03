#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
check_ledger.py — validate OPEN-ITEMS.md ledgers against LEDGER-SPEC.md.

Usage:
    uv run check_ledger.py                    # validate ./OPEN-ITEMS.md
    uv run check_ledger.py path/to/OPEN-ITEMS.md [more...]
    uv run check_ledger.py --root .           # validate every ledger under a root

Exit code 0 = all valid, 1 = at least one error.

Run this after any write to a ledger. A malformed line is skipped silently by the
collector, which produces a rollup that looks complete and is not — worse than no
rollup at all.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ledger import (
    DATE_RE,
    LEDGER_FILENAME,
    PREFIX_RE,
    REQUIRED_FRONTMATTER,
    Ledger,
    find_ledgers,
    parse_ledger,
)

FORBIDDEN_IN_TEXT = ("\u00b7", "\u2014")


def validate(ledger: Ledger) -> list[str]:
    errors = list(ledger.errors)
    fm = ledger.frontmatter

    for key in REQUIRED_FRONTMATTER:
        if key not in fm:
            errors.append(f"frontmatter missing required key: {key}")

    prefix = str(fm.get("scope_prefix", ""))
    if prefix and not PREFIX_RE.match(prefix):
        errors.append(
            f"scope_prefix {prefix!r} is invalid — 2-8 chars, uppercase letters "
            "and digits, must start with a letter"
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
                f"{where}: prefix {item.prefix!r} does not match the ledger's "
                f"scope_prefix {prefix!r}"
            )

        for char in FORBIDDEN_IN_TEXT:
            if char in item.text:
                errors.append(
                    f"{where}: item text contains a reserved separator character "
                    f"({char!r}) — use a hyphen or a colon instead"
                )

        if item.path and " " in item.path:
            errors.append(
                f"{where}: the field {item.path!r} contains spaces — a stray "
                "separator has probably split the item text. Remove the middle dot "
                "from the text."
            )

        if item.section == "Open" and item.is_closed:
            errors.append(f"{where}: checked [x] but sits in the Open section")
        if item.section == "Closed" and not item.is_closed:
            errors.append(f"{where}: unchecked [ ] but sits in the Closed section")

        if not item.opened:
            errors.append(f"{where}: missing the opened date")
        elif item.opened_date is None:
            errors.append(f"{where}: opened is not a valid ISO date: {item.opened!r}")

        if item.is_closed:
            if not item.closed:
                errors.append(f"{where}: closed item has no closed date")
            elif item.closed_date is None:
                errors.append(f"{where}: closed is not a valid ISO date: {item.closed!r}")
            elif item.opened_date and item.closed_date < item.opened_date:
                errors.append(f"{where}: closed date is earlier than opened date")
        elif item.closed:
            errors.append(f"{where}: open item must not carry a closed date")

    next_id = fm.get("next_id")
    if isinstance(next_id, int) and next_id <= max_number:
        errors.append(
            f"frontmatter next_id is {next_id} but the highest existing ID is "
            f"{max_number:04d} — next_id must be greater, or IDs will be reused"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate OPEN-ITEMS.md ledgers.")
    parser.add_argument("paths", nargs="*", type=Path, help="ledger files to validate")
    parser.add_argument("--root", type=Path, help="validate every ledger under this root")
    args = parser.parse_args()

    if args.root:
        targets = find_ledgers([args.root], [])
    elif args.paths:
        targets = args.paths
    else:
        default = Path.cwd() / LEDGER_FILENAME
        if not default.exists():
            print(f"no {LEDGER_FILENAME} in {Path.cwd()}", file=sys.stderr)
            return 1
        targets = [default]

    if not targets:
        print("no ledgers found", file=sys.stderr)
        return 1

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
                    "prefixes must be unique across ledgers"
                )
            prefixes.setdefault(prefix, target)

        if errors:
            failed = True
            print(f"FAIL  {target}")
            for err in errors:
                print(f"        {err}")
        else:
            print(
                f"ok    {target}  "
                f"[{prefix}] {len(led.open_items())} open, {len(led.closed_items())} closed"
            )

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
