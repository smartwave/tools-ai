# Integration snippets

Paste these into the repo. Kept separate so nothing overwrites your existing files.

---

## 1. CATALOG.md row

Per the tools-ai lifecycle. Tier is Claude's proposal via the Governance `01`
question flow, flagged as analysis pending your review — same convention as the
three existing rows.

```markdown
| open-items | skill | Personal | 0 (proposed) | spec | skills/open-items/ | Per-folder OPEN-ITEMS.md ledger for unfinished work, with a cross-scope rollup. |
```

Move status to `built` after the Definition of Done pass in `SPEC.md`.

---

## 2. CLAUDE.md addition

One block per repo or vault that holds a ledger.

```markdown
## Open items

Unfinished work in this repo is tracked in `OPEN-ITEMS.md` at the root.

- Format contract: `skills/open-items/LEDGER-SPEC.md`. Read it before writing.
- Commands: `log-item`, `end-of-session`, `open-items-status`.
- Before ending a session, run `end-of-session` and reconcile the ledger.
- Run `uv run skills/open-items/check_ledger.py OPEN-ITEMS.md` after any write.
- Never write to another scope's ledger from a session in this one.
```

For the vault, adjust the paths to point at the tools-ai skill folder.

---

## 3. GitHub Actions validation

`.github/workflows/check-ledger.yml`. Validates this repo's ledgers on push.

Note what this can and cannot do: a hosted runner gets a clone of **one repository**
and nothing else. It can validate format. It **cannot** produce the cross-scope
rollup, because it cannot see your vault, your Cowork folders, or your other repos.
Rollup is always a local operation.

```yaml
name: check-ledger

on:
  push:
    paths:
      - "**/OPEN-ITEMS.md"
      - "skills/open-items/**"
  pull_request:
    paths:
      - "**/OPEN-ITEMS.md"
      - "skills/open-items/**"

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Validate ledgers
        run: python skills/open-items/check_ledger.py --root .
```

---

## 4. Scheduled local run — deferred, kept here for later

Not part of Phase 1. Add only when on-demand runs prove insufficient.

On macOS use `launchd` rather than `cron`, for one specific reason: **launchd runs
missed jobs when the machine wakes; cron silently skips them.** On a laptop that is
asleep at 07:00, cron gives you nothing and no error.

`~/Library/LaunchAgents/biz.smartwave.open-items.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>biz.smartwave.open-items</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/sh</string>
    <string>-lc</string>
    <string>uv run <repo-root>/skills/open-items/collect.py</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key><integer>7</integer>
    <key>Minute</key><integer>30</integer>
  </dict>
  <key>StandardErrorPath</key>
  <string>/tmp/open-items.err</string>
</dict>
</plist>
```

Load it with `launchctl load ~/Library/LaunchAgents/biz.smartwave.open-items.plist`.

**On Claude scheduled tasks:** worth verifying rather than taking my word, but the
structural problem is that a scheduled task runs in Anthropic's cloud environment,
which cannot see your local disk. Anthropic's own documentation notes that memory
sharing between Cowork and chat only works when Cowork runs in the cloud, not
locally — confirming the two are genuinely separate environments. Assume a cloud
schedule cannot walk your vault.
