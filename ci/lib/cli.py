"""Entry-point boilerplate shared by every ci/ check."""

import os
import sys

CI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def bootstrap():
    """Make `lib` importable however the script was invoked."""
    if CI_DIR not in sys.path:
        sys.path.insert(0, CI_DIR)


def run(main):
    """Run a check's main(), turning a missing configuration into exit 3 and a
    malformed data file into exit 1 with a file:line message."""
    from .config import NotConfigured
    from .loader import DataError
    from .report import EXIT_NOT_CONFIGURED, EXIT_VIOLATION, not_configured
    try:
        return main()
    except NotConfigured as exc:
        return not_configured(str(exc))
    except DataError as exc:
        sys.stderr.write("%s\n" % exc)
        return EXIT_VIOLATION
    except KeyboardInterrupt:
        return 130
