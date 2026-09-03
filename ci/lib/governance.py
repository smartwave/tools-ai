"""Policy loading, manifest loading, and effective-tier resolution.

The policy files are the rulebook; nothing here restates a rule that
policy/*.yaml already carries. Item lists (pre-flight, tier extras) are always
read from the policy file so a policy edit changes behaviour without a code
change.
"""

import os

from .config import REPO_ROOT
from .loader import load_json, load_yaml

POLICY_DIR = os.path.join(REPO_ROOT, "policy")
TIER_CONTROLS_PATH = os.path.join(POLICY_DIR, "tier-controls.yaml")
GATES_PATH = os.path.join(POLICY_DIR, "gates.yaml")
STANDARDS_PATH = os.path.join(POLICY_DIR, "standards.yaml")
SCHEMA_PATH = os.path.join(REPO_ROOT, "schemas", "manifest.schema.json")
VOCABULARY_PATH = os.path.join(REPO_ROOT, "vocabulary", "vocabulary.yaml")
TAGMAP_PATH = os.path.join(REPO_ROOT, "projections", "tag-map.yaml")
REGISTRY_PATH = os.path.join(REPO_ROOT, "registry", "registry.yaml")
# Per-asset evidence root. Overridable so the fixture suite can point the
# checks at ci/tests/fixtures/assets without touching the real tree.
ASSETS_DIR = os.environ.get(
    "GOVERNANCE_ASSETS_DIR", os.path.join(REPO_ROOT, "assets"))


def tier_controls():
    return load_yaml(TIER_CONTROLS_PATH)


def gates():
    data = load_yaml(GATES_PATH)
    return dict((gate["id"], gate) for gate in data.get("gates", []))


def standards():
    return load_yaml(STANDARDS_PATH)


def vocabulary():
    return load_yaml(VOCABULARY_PATH)


def tag_map(config):
    return config.resolve(load_yaml(TAGMAP_PATH))


def manifest_schema(config):
    """The schema with {{TOKENS}} resolved in memory. The file on disk stays
    generic."""
    return config.resolve(load_json(SCHEMA_PATH))


def load_manifest(path, config):
    """Load a manifest and resolve configuration tokens in memory only."""
    return config.resolve(load_yaml(path))


def registry(config, path=None):
    data = load_yaml(path or REGISTRY_PATH)
    entries = data.get("registry") or []
    return [config.resolve(entry) for entry in entries]


def asset_dir(manifest):
    return os.path.join(ASSETS_DIR, str(manifest.get("asset_id", "")))


def effective_tier(manifest, policy=None):
    """Resolve the effective tier by applying `modifiers` before reading the
    tier row, exactly as tier-controls.yaml's 'How to read this file' says.

    Returns (effective_tier, declared_tier, [(control, reason), ...]).
    """
    policy = policy or tier_controls()
    modifiers = policy.get("modifiers", {})
    declared = manifest.get("tier")
    tier = declared if isinstance(declared, int) else 1
    reasons = []

    shape = manifest.get("shape")
    shape_mod = (modifiers.get("shape") or {}).get(shape) or {}
    minimum = shape_mod.get("forces_min_tier")
    if minimum and tier < minimum:
        tier = minimum
        reasons.append(("B1.2", "shape '%s' forces tier >= %d" % (shape, minimum)))

    data_class = manifest.get("data_class")
    data_mod = (modifiers.get("data_class") or {}).get(data_class) or {}
    minimum = data_mod.get("forces_min_tier")
    if minimum and tier < minimum:
        tier = minimum
        reasons.append(("B1.3", "data_class '%s' forces tier >= %d"
                        % (data_class, minimum)))

    return tier, declared, reasons


def tier_row(tier, policy=None):
    policy = policy or tier_controls()
    return (policy.get("tiers") or {}).get(tier) or {}


# Manifest fields that carry a controlled vocabulary, and the vocabulary key
# each one is defined by. Values themselves are never restated here.
VOCAB_FIELDS = {
    "workload_type": "workload_type",
    "shape": "shape",
    "tier": "tier",
    "track": "track",
    "oversight": "oversight",
    "data_class": "data_class",
    "lifecycle": "lifecycle",
}

# The Tier 1 manifest shape, per the schema's own description.
TIER_1_REQUIRED = ["asset_id", "name", "version", "workload_type", "owner"]


def vocab_values(vocab, field):
    """The allowed values for a vocabulary field, whichever of the two shapes
    the vocabulary uses (a list, or a mapping of value -> definition)."""
    entry = vocab.get(field) or {}
    values = entry.get("values")
    if isinstance(values, dict):
        return set(values.keys())
    if isinstance(values, list):
        return set(values)
    return set()
