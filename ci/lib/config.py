"""Configuration resolution for the governance checks.

Resolution order (see BUILDOUT-SPEC / ci/README.md):
  1. config/governance.yaml, if present.
  2. otherwise, detect that the adopter did the documented find-and-replace
     in the committed tree and derive the values from it.
  3. otherwise NOT_CONFIGURED — the caller exits 3 with the copy-the-example
     instruction.
"""

import os
import re

from .loader import load_yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# GOVERNANCE_CONFIG overrides the location of the adopter config. The fixture
# suite uses it so a test run never depends on the developer's own config.
CONFIG_PATH = os.environ.get(
    "GOVERNANCE_CONFIG", os.path.join(REPO_ROOT, "config", "governance.yaml"))
EXAMPLE_PATH = os.path.join(REPO_ROOT, "config", "governance.example.yaml")
SCHEMA_PATH = os.path.join(REPO_ROOT, "schemas", "manifest.schema.json")
TAGMAP_PATH = os.path.join(REPO_ROOT, "projections", "tag-map.yaml")

NOT_CONFIGURED_MESSAGE = (
    "not configured: no config/governance.yaml and the tree still carries "
    "{{...}} placeholders. Run: cp config/governance.example.yaml "
    "config/governance.yaml and set real values (or do the documented "
    "find-and-replace across the tree)."
)

TOKEN_KEYS = {
    "ASSET_ID_PREFIX": "asset_id_prefix",
    "TAG_NAMESPACE": "tag_namespace",
    "ORG_NAME": "org_name",
    "DOC_ID_PREFIX": "doc_id_prefix",
}

_TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


class NotConfigured(Exception):
    """Raised when neither a config file nor a substituted tree is available."""


class Config(object):
    def __init__(self, values, source):
        self.values = values
        self.source = source

    def __getitem__(self, key):
        return self.values[key]

    @property
    def asset_id_prefix(self):
        return self.values["asset_id_prefix"]

    @property
    def tag_namespace(self):
        return self.values["tag_namespace"]

    @property
    def org_name(self):
        return self.values.get("org_name", "")

    @property
    def enforce_pending_insert(self):
        return bool(self.values.get("enforce_pending_insert", False))

    def resolve(self, value):
        """Substitute known {{TOKENS}} in a string (or recursively in a
        list/dict) read out of the generic tree. Unknown tokens are left as
        they are — a check that cares reports them itself."""
        if isinstance(value, str):
            def sub(match):
                key = TOKEN_KEYS.get(match.group(1))
                if key is None or self.values.get(key) is None:
                    return match.group(0)
                return str(self.values[key])
            return _TOKEN_RE.sub(sub, value)
        if isinstance(value, list):
            return [self.resolve(v) for v in value]
        if isinstance(value, dict):
            return dict((k, self.resolve(v)) for k, v in value.items())
        return value


def unresolved_tokens(value):
    """Every {{TOKEN}} still present in a string."""
    return _TOKEN_RE.findall(value) if isinstance(value, str) else []


def _derive_from_tree():
    """Recover the adopter's values from a tree where the documented
    find-and-replace was already done. Returns None if placeholders remain."""
    try:
        with open(SCHEMA_PATH) as handle:
            schema_text = handle.read()
        with open(TAGMAP_PATH) as handle:
            tagmap_text = handle.read()
    except IOError:
        return None
    if "{{" in schema_text or "{{TAG_NAMESPACE}}" in tagmap_text:
        return None

    prefix_match = re.search(
        r'"pattern"\s*:\s*"\^([A-Za-z0-9-]*?)\[A-Z0-9\]', schema_text)
    ns_match = re.search(r'github_topic:\s*"([a-z0-9]+)-ai-governed"', tagmap_text)
    if not prefix_match or not ns_match:
        return None
    return {
        "org_name": "",
        "asset_id_prefix": prefix_match.group(1),
        "tag_namespace": ns_match.group(1),
        "doc_id_prefix": "",
        "enforce_pending_insert": False,
    }


def load_config():
    """Return a Config, or raise NotConfigured."""
    if os.path.exists(CONFIG_PATH):
        values = load_yaml(CONFIG_PATH)
        missing = [k for k in ("asset_id_prefix", "tag_namespace") if not values.get(k)]
        if missing:
            raise NotConfigured(
                "config/governance.yaml is missing required key(s): %s"
                % ", ".join(missing))
        return Config(values, CONFIG_PATH)

    derived = _derive_from_tree()
    if derived is not None:
        return Config(derived, "substituted tree")

    raise NotConfigured(NOT_CONFIGURED_MESSAGE)
