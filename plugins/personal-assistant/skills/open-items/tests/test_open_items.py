#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Tests for the tracker format: parser, validator, folder discovery.

    uv run tests/test_open_items.py     # or: python3 tests/test_open_items.py

No dependencies, no test framework. Exit code 0 = pass.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from check_ledger import validate                       # noqa: E402
from ledger import find_ledgers, parse_ledger           # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def load(name: str):
    return parse_ledger(FIXTURES / name)


def errors_for(name: str) -> list[str]:
    return validate(load(name))


class ValidFile(unittest.TestCase):
    def setUp(self):
        self.led = load("OPEN-ITEMS Valid Project.md")

    def test_no_errors(self):
        self.assertEqual(validate(self.led), [])

    def test_project_name_comes_from_filename(self):
        self.assertEqual(self.led.project, "Valid Project")

    def test_items_parsed(self):
        self.assertEqual(len(self.led.items), 3)

    def test_categories_grouped_in_file_order(self):
        self.assertEqual(list(self.led.categories()), ["Governance", "Learning Guides"])

    def test_locator_read(self):
        item = next(i for i in self.led.items if i.ident == "VP-0002")
        self.assertEqual(item.locator, 'chat "Learning guide drafts"')

    def test_locator_optional(self):
        item = next(i for i in self.led.items if i.ident == "VP-0001")
        self.assertIsNone(item.locator)

    def test_uncategorised_item_allowed(self):
        item = next(i for i in self.led.items if i.ident == "VP-0003")
        self.assertEqual(item.category, "Learning Guides")


class Malformed(unittest.TestCase):
    def setUp(self):
        self.errors = errors_for("OPEN-ITEMS Malformed Project.md")

    def test_fails(self):
        self.assertTrue(self.errors)

    def test_stray_separator_reported_as_unlabelled_field(self):
        self.assertTrue(any("unlabelled field" in e for e in self.errors))

    def test_missing_opened_date_reported(self):
        self.assertTrue(any("missing the opened date" in e for e in self.errors))

    def test_prefix_mismatch_reported(self):
        self.assertTrue(any("does not match the file's scope_prefix" in e for e in self.errors))

    def test_next_id_too_low_reported(self):
        self.assertTrue(any("next_id" in e for e in self.errors))


class RemovedFeatures(unittest.TestCase):
    """The closed section, closed dates and ticked boxes are gone. A file still
    carrying them must fail, not be quietly accepted."""

    def setUp(self):
        self.errors = errors_for("OPEN-ITEMS Legacy Project.md")

    def test_closed_section_rejected(self):
        self.assertTrue(any("unexpected section heading 'Closed'" in e for e in self.errors))

    def test_ticked_item_rejected(self):
        self.assertTrue(any("checked [x]" in e for e in self.errors))


class Naming(unittest.TestCase):
    def test_bad_filename_rejected(self):
        errors = errors_for("badname.md")
        self.assertTrue(any("does not follow" in e for e in errors))


class Discovery(unittest.TestCase):
    def test_finds_only_tracker_files(self):
        names = [p.name for p in find_ledgers(FIXTURES)]
        self.assertIn("OPEN-ITEMS Valid Project.md", names)
        self.assertNotIn("badname.md", names)

    def test_missing_folder_returns_empty(self):
        self.assertEqual(find_ledgers(FIXTURES / "nope"), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
