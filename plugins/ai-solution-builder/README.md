# ai-solution-builder

Guides an AI solution through a staged, gated pipeline — from a throwaway proof
of concept to an approved, documented, tracked deployment. Org-wide and
non-engineer friendly. **Refines and records the builder's own input; never
originates, fabricates, or auto-creates.**

This is the vendor-neutral edition: every organization-specific value is a
double-brace placeholder token you fill in before adopting. See
[Configuration](#configuration).

## The pipeline

| Stage | Skill | Produces |
|---|---|---|
| Stage 0 · Frame | `ai-problem-framer` | The **Ultralight Problem Brief** — problem statement (5W1H), validated root cause (Five Whys), process-level future state (lenses). One page, in the person's own words, three gated phases; earlier sections lock as later ones are written |
| Stage 0 · Brief | `ai-poc-brief-author` | The **POC Brief** — the one testable question, smallest build, synthetic data, safety pre-flight, and a paste-ready build prompt for CoWork or Claude Code |
| Stage 0 · Build | `ai-poc-builder` | A local, throwaway proof of concept — built to *learn*, never to deploy — with a change log of every vibe-coded change |
| Stage 0 · Summarise | `ai-poc-summary-author` | The **POC Summary** — what it did, the change log, what was learned, and the person's ask to IT (partner, have IT build, keep personal, stop) |
| Gate 1 | `ai-requirements-doc-author` | The **AI Solution Requirements** document (the ask) and a proposed risk tier |
| Design | `ai-solution-design-author` | The **Solution Design** — architecture plus the authored test plan (required for a new Tier 2/3 solution, B1.10) |
| Build | `ai-solution-spec-author` | The **Solution Spec** — the evidence record for what was actually built, tested, and verified |
| Track | `ai-work-planner` | A work-effort Epic with child issues in your work tracker (B1.9) |

Legacy names: the Requirements document was formerly the "SRB"
(Solution Requirements Brief); the Solution Spec was formerly the "SDR"
(Solution Design Record). Both terms still trigger the relevant skill.

Stage 0 is the first stage of proposing something to IT: a problem brief and a POC summary are
what a person brings to that conversation, and if the answer is to build, Gate 1 follows. The
three Stage 0 documents are not governed records; they feed the Requirements document.

**Also on Gemini.** [`gems/`](gems/) holds five Gemini Gem instruction sets that produce the same
Stage 0 outputs (problem statement, root cause, future state, POC brief, POC summary) for
employees whose tool is Gemini. They inline the same methods and templates; see
[`gems/README.md`](gems/README.md) for why the instructions repeat their governing rule.

## Source of truth

The skills read [`references/`](references/) at runtime rather than restating
policy, so plugin guidance cannot drift from the standard. The bar itself lives
in [`references/deployment-standard.md`](references/deployment-standard.md);
[`references/README.md`](references/README.md) explains the one-way
repo → wiki sync model and carries its own configuration table for the
document set.

## Guardrails

- **Guides, never authors.** In Stage 0 the person writes the problem, root cause,
  and future state; the AI asks, structures, and sharpens. The root-cause phase
  never writes on its first response and treats the problem statement as
  read-only; the future-state phase confirms the exact text before writing.
- **Never originates requirements.** The requester's words are refined into
  review-ready language; they are never invented on the requester's behalf.
- **Never fabricates evidence**, results, attestations, or sign-offs, and never
  checks an un-evidenced pre-flight box.
- **Never publishes.** Every document is handed back as a draft for the
  requester to place themselves.
- **Proposes, never auto-creates.** Work-tracker issues are created only on
  explicit per-issue approval; effort, dates, and confidence come from the
  requester verbatim; people are assigned only by name, by the requester.
- **A POC is not a deployment.** `ai-poc-builder` keeps work personal and off
  sensitive data, and refuses to wire a POC into a system of record, a customer,
  a schedule, or another person's workflow.
- **Reviewer ≠ builder** at Gate 1.

## Configuration

Fill every placeholder below before adopting this plugin. Tokens use
double-brace UPPER_SNAKE syntax. The `references/` document set has its own
table in [`references/README.md`](references/README.md) — this table is the
union of both.

| Placeholder | What to put there |
|---|---|
| `{{ORG_NAME}}` | Your organization's name, as it should read in prose. |
| `{{IT_HELPDESK_EMAIL}}` | Support mailbox for this plugin (the manifest author email). |
| `{{SECURITY_CONTACT_EMAIL}}` | Where security issues and stop-and-report escalations go. |
| `{{AI_GOVERNANCE_OWNER}}` | Person accountable for the bundled standard and templates. |
| `{{AUTOMATION_LEAD_ROLE}}` | Title of the leader of your automation function. |
| `{{SECURITY_LEAD_ROLE}}` | Title of the security leader who owns the Standard. |
| `{{BUSINESS_TECHNOLOGY_LEAD_ROLE}}` | Title of the IT / business-technology leader (third-party-policy exception authority). |
| `{{BUSINESS_TECHNOLOGY_LEAD}}` | Name of the person holding that role, named as an AI Use Framework co-owner. |
| `{{WIKI_HOST}}` | Host of your wiki, e.g. `example.atlassian.net`. |
| `{{WIKI_SPACE_KEY}}` | Space/section key the published documents live in. |
| `{{TRACKER_HOST}}` | Host of your work tracker. Same value as `{{WIKI_HOST}}` in the reference configuration; separate so a split stack works. |
| `{{PRODUCT_TRACKER_PROJECT_KEY}}` | Project key for the **product** track, whose Epic field conventions that track follows. |
| `{{TEAM_CONVENTIONS_DOC}}` | The owning team's conventions document the non-product track defers to. |
| `{{TICKET_REF}}` | The change ticket a changelog entry was delivered under. |
| `{{PAGE_ID_AI_USE_FRAMEWORK}}` | Published page id of the AI Use Framework Guide. |
| `{{PAGE_ID_AI_POLICY}}` | Published page id of your AI Policy. |
| `{{PAGE_ID_RISK_MANAGEMENT_POLICY}}` | Published page id of your Risk Management Policy. |
| `{{PAGE_ID_INFORMATION_SECURITY_POLICY}}` | Published page id of your Information Security Policy. |
| `{{PAGE_ID_CHANGE_MANAGEMENT_POLICY}}` | Published page id of your Change Management Policy. |

**Named integrations are the reference configuration, not a requirement.** Jira
(work tracker), Confluence (wiki), and GitHub (repository host) can each be
swapped for an equivalent product; the connector tool names in the skills are
the real names in the reference configuration, and the surrounding logic is
unchanged when you substitute your own. Likewise the Tier 2+ guardrail control
names a reference enforcement stack — substitute your equivalent out-of-agent
enforcement layer.

**Adopt the control set deliberately.** `references/deployment-standard.md` and
`references/ai-use-framework.md` are template policy documents. They carry a
complete, coherent control set, but they are not ratified policy for *your*
organization until your own security, legal, and risk owners review and adopt
them. Treat them as a starting draft, not as compliance.
