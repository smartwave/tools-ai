#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
status.py — list what is in the tracker folder.

Usage:
    uv run status.py                  # every project, its categories, its counts
    uv run status.py --items          # also print every open item
    uv run status.py --folder "path"  # look somewhere other than the default

This exists so that choosing a project and a category is picking from a list
rather than remembering. It is deterministic: listing a folder, parsing files and
counting are fully specified operations, so no judgement belongs here.

Exit code 2 means the folder is not reachable — that is the signal to ask for
access rather than to write anywhere else.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ledger import find_ledgers, parse_ledger, tracker_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="List tracker projects and categories.")
    parser.add_argument("--folder", type=Path, help="tracker folder to read")
    parser.add_argument("--items", action="store_true", help="print every open item")
    args = parser.parse_args()

    folder = (args.folder or tracker_dir()).expanduser()

    if not folder.is_dir():
        print(f"tracker folder not reachable: {folder}", file=sys.stderr)
        return 2

    paths = find_ledgers(folder)
    if not paths:
        print(f"tracker folder is empty: {folder}")
        return 0

    total = 0
    print(f"{folder}\n")

    for path in paths:
        led = parse_ledger(path)
        grouped = led.categories()
        count = len(led.items)
        total += count
        flag = "  ! format errors — run check_ledger.py" if led.errors else ""
        print(f"{led.project}  [{led.prefix}]  {count} open  · next id {led.frontmatter.get('next_id', '?')}{flag}")

        for category, items in grouped.items():
            label = category or "(no category)"
            print(f"    {label}  ({len(items)})")
            if args.items:
                for item in items:
                    found = f"  · find: {item.locator}" if item.locator else ""
                    print(f"        {item.ident} — {item.text}  · opened {item.opened}{found}")
        print()

    print(f"{total} open across {len(paths)} project file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
