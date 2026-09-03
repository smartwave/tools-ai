# plugins/

Built plugins — installable bundles (e.g., Claude/Cowork plugins) that package skills, connectors, or tools together. One subfolder per plugin, lowercase-with-hyphens, each containing a `README.md` and `SPEC.md` from `_templates/`.

Every plugin here is listed in `.claude-plugin/marketplace.json` at the repo root, so it can be installed with `/plugin install <name>@tools-ai` after `/plugin marketplace add smartwave/tools-ai`. A new plugin adds its entry in the same change; the entry's `name` and `version` must match the plugin's `plugin.json`.
