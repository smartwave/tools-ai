"""Result collection, provenance gating, and exit codes.

Exit codes (contract, see ci/README.md):
  0  pass (warnings and not-machine-checkable notices allowed)
  1  violation
  3  not configured
  4  environment problem (missing dependency)
Exit code 2 ("not implemented") must never occur again.
"""

import sys

EXIT_OK = 0
EXIT_VIOLATION = 1
EXIT_NOT_CONFIGURED = 3
EXIT_ENVIRONMENT = 4

# Provenance tags that are only enforced when the adopter has set
# enforce_pending_insert: true (the pending naming/tagging insert), plus the
# never-enforced inferred tag.
PENDING_TAGS = ("REF insert",)
NEVER_ENFORCED_TAGS = ("PROPOSED", "REC")


class Report(object):
    """Collects findings for one check run over one subject."""

    def __init__(self, check, subject=None, config=None):
        self.check = check
        self.subject = subject
        self.config = config
        self.failures = []
        self.warnings = []
        self.notices = []
        self.not_checkable = []
        self.passes = []

    # -- recording ---------------------------------------------------------

    def ok(self, control, message):
        self.passes.append((control, message))

    def warn(self, control, message):
        self.warnings.append((control, message))

    def notice(self, message):
        self.notices.append(message)

    def unknowable(self, control, message):
        """A rule that exists but cannot be decided from the available data.
        Always printed, so silence never reads as coverage."""
        self.not_checkable.append((control, message))

    def fail(self, control, message, provenance="REF"):
        """Record a violation, downgraded to a warning when its provenance is
        not enforceable under the current config."""
        if self._enforced(provenance):
            self.failures.append((control, message))
        else:
            self.warnings.append(
                (control, "%s  [warn-only: %s not enforced]" % (message, provenance)))

    def _enforced(self, provenance):
        for tag in NEVER_ENFORCED_TAGS:
            if tag in provenance:
                return False
        for tag in PENDING_TAGS:
            if tag in provenance:
                return bool(self.config and self.config.enforce_pending_insert)
        return True

    # -- output ------------------------------------------------------------

    @property
    def status(self):
        if self.failures:
            return "fail"
        if self.warnings:
            return "warn"
        return "pass"

    def render(self, stream=None):
        stream = stream or sys.stdout
        head = self.check if not self.subject else "%s %s" % (self.check, self.subject)
        stream.write("== %s: %s\n" % (head, self.status.upper()))
        for control, message in self.failures:
            stream.write("  FAIL  [%s] %s\n" % (control, message))
        for control, message in self.warnings:
            stream.write("  WARN  [%s] %s\n" % (control, message))
        for control, message in self.not_checkable:
            stream.write("  N/C   [%s] %s (not machine-checkable here)\n"
                         % (control, message))
        for message in self.notices:
            stream.write("  NOTE  %s\n" % message)

    @property
    def exit_code(self):
        return EXIT_VIOLATION if self.failures else EXIT_OK


def not_configured(message):
    sys.stderr.write("%s\n" % message)
    return EXIT_NOT_CONFIGURED
