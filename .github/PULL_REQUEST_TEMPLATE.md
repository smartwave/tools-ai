## What changed

<!-- One or two sentences. What is different after this PR? -->

## Change class (B1.6)

- [ ] Standard — pre-approved, low risk, reversible
- [ ] Normal (minor)
- [ ] Normal (major) — needs a rollback plan and a post-implementation review
- [ ] Emergency — needs a rollback plan and a post-implementation review

## Acceptance

**Accepted by (not the author):** <!-- name -->

Every material change MUST be accepted by someone other than the builder
(B1.6). A PR review by another person satisfies this for code.

## Rollback

<!-- How this is undone, and who can do it. "Revert the commit" is a valid
     answer when it really is one. -->

## Does this change a rule in `policy/`?

- [ ] No
- [ ] Yes — Confluence ratification status:
      <!-- ratified in the live standard / pending insert / not yet raised.
           A rule that is not ratified must stay [REF insert] or [PROPOSED] and
           must not be enforced by default. -->

## Does this change an asset's behavior?

- [ ] No
- [ ] Yes — evaluation re-run and results committed under
      `assets/<asset_id>/evaluation/results/` (model, prompt, tool, or scope
      changes all trigger a re-run)

## Checks

- [ ] `ci/run-all` passes locally
- [ ] `ci/tests/run` passes locally
