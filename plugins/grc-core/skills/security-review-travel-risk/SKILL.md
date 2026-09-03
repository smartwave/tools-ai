---
name: security-review-travel-risk
description: Evaluate a request to work internationally from a country outside {{ORG_NAME}}'s pre-approved list. Use when someone asks to assess, review, or triage an international travel work request, or pastes a country/city + dates for a travel risk check. Re-verifies current sanctions, travel-advisory, data-adequacy, and state-surveillance facts; scores the four risk domains (Sanctions, Geopolitical, Data Privacy, Information Security); applies the tiered decision logic; and outputs a Jira-ready summary. Triggers include "travel risk review for [country]", "can we approve work from [country]", "assess this travel request", "risk check [country] [dates]". Produces a recommendation for human review only — never an approval, a legal/compliance determination, or an action.
---

# Security Review — International Travel Risk

This skill implements your organization's **Standard: Evaluating International Travel Work Requests (v{{TRAVEL_STANDARD_VERSION}})**. It re-verifies the current facts across four risk domains, applies the standard's tiered decision logic, and returns a human-readable recommendation that pastes cleanly into a Jira ticket. **It implements the standard's logic; it does not redefine it.** Where this skill and the standard disagree, the standard governs — flag the discrepancy for the standard's owner (Security).

Skill version **v1.0** ↔ standard version **v{{TRAVEL_STANDARD_VERSION}}**.

## Prime directive

This skill produces a **recommendation for a human reviewer**. It never approves a trip, never states a trip "is approved," never creates/transitions tickets, never emails, and never modifies systems. Sanctions and data-protection calls belong to Legal — flag them, don't conclude them.

## When to use / not use

**Use:** any request to evaluate working from a country outside the pre-approved list.

Pre-approved list: **{{TRAVEL_PREAPPROVED_COUNTRIES}}** — the countries your
organization has already accepted as work locations. Substitute your own list;
the skill reads it as data, not as a fact about any particular country.

**Short-circuit (state the outcome, don't run the full review):**
- Destination on the pre-approved list **and** stay ≤ {{TRAVEL_SHORT_STAY_LIMIT}} → no security review needed; say so.
- Stay > {{TRAVEL_SHORT_STAY_LIMIT}} (even pre-approved) → no security review needed, but output the **HR/tax notification** flag and stop.
- Pure vacation with no system/data access → out of scope; say so.

## Inputs

- **Required:** country.
- **Recommended:** city, travel dates, duration, purpose.
- **Optional:** systems/data classes in scope; whether any customer data is involved.

Do **not** collect or embed confidential customer names, contract values, or personal data beyond what the ticket needs. If duration is unknown, ask once; otherwise proceed and note the assumption.

## Process

### Step 1 — Intake and short-circuit checks
Normalize the country and resolve territory ambiguity before rating — an overseas territory is not automatically covered by its parent state's privacy regime. Apply the pre-approved-list and duration checks above.

### Step 2 — Re-verify facts, per domain (mandatory)
Re-verify in the current run. **Do not rely on prior runs, memory, or a prior approval on file.** For each domain, fetch current data from the source registry (see `references/source-registry.md`) and record the value **plus the source URL and an "as-of" date**:

- **Sanctions** — OFAC: is there a country sanctions program (y/n)? Note recent SDN activity for the country.
- **Geopolitical** — current U.S. State Department advisory level (1–4); any ordered/authorized-departure notice.
- **Data Privacy** — EU adequacy status; existence/nature of the local data-protection law; (internal) whether any customer DPA restricts access location.
- **Information Security — state-sponsored traffic observation** — Freedom on the Net standing; then check for **Layer B** evidence: targeted spyware (Citizen Lab / Amnesty Security Lab / Forbidden Stories), mandatory decryption or VPN prohibition, border device-search practice. Classify observation as **none / network-layer (A) / endpoint-or-forced-disclosure (B)**.

### Step 3 — Score each domain
Rate each domain **Low / Moderate / Elevated / High** against the rubric in the standard, citing the Step 2 evidence. Every rating carries a source link.

### Step 4 — Apply decision tiers
- **Tier 1 — Auto-approve:** Low across domains (e.g., adequacy country, advisory 1, no observation).
- **Tier 2 — Approve:** manageable risk, no blockers (e.g., data privacy handled via a transfer-impact assessment).
- **Tier 3 — Approve with contingency:** InfoSec **Layer A** → require corporate VPN / reduced scope / clean device; conditional data-privacy or HR/Legal gates.
- **Tier 4 — Decline:** InfoSec **Layer B**; **Sanctions country program**; or **active-conflict Geopolitical**. Any one of these forces Tier 4.

The InfoSec **A-vs-B** classification is what decides contingency (A) vs decline (B).

### Step 5 — Assemble the Jira-ready output
Use the template below. Include contingencies, approvals needed, a re-review date, every source with its as-of date, and the disclaimer.

## Fact-verification requirements

- **Freshness:** all four domains re-verified this run; stamp each with an as-of date.
- **Citations:** no rating without a source link.
- **No fabrication:** if a fact cannot be verified (source unreachable, no data), mark it **UNVERIFIED** and lower confidence — never guess.
- **Fail safe:** unverifiable **Sanctions** or **Layer B InfoSec** defaults the item to **"manual review required,"** never to "clear."
- **Corroboration:** Layer B (spyware/endpoint) claims require a **forensic** source (Citizen Lab / Amnesty), not a single index. Note any country denial, but base the rating on independent forensic evidence.
- **Balance:** treat a single surveillance index as a signal; corroborate before it drives a decline.

## Output format (Jira-ready)

Primary format is Jira wiki markup (Jira is the work tracker in the reference configuration — substitute the equivalent markup for another tracker); a Markdown fallback is acceptable for Jira Cloud's editor. Keep it to one screen, lead with the verdict, and never omit the disclaimer or the source/as-of stamps.

```
h2. International Travel Work Request — Risk Review

*Verdict:* {AUTO-APPROVE | APPROVE | APPROVE WITH CONTINGENCY | DECLINE | MANUAL REVIEW}
*Destination:* {Country} ({City})   *Dates:* {start–end}   *Duration:* {n days}
*Decision tier:* {1–4}
*Reviewed:* {YYYY-MM-DD}   *Re-review by:* {YYYY-MM-DD}

||Domain||Rating||Basis||Source (as-of)||
|Sanctions|{L/M/E/H}|{one line}|{url} ({date})|
|Geopolitical|{L/M/E/H}|{advisory level + notes}|{url} ({date})|
|Data Privacy|{L/M/E/H}|{adequacy + law + DPA note}|{url} ({date})|
|Information Security|{L/M/E/H}|{observation: none / Layer A / Layer B}|{url} ({date})|

*State-sponsored traffic observation:* {None | Network-layer (mitigable) | Endpoint/forced-disclosure (unavoidable)} — {evidence}
*Blockers:* {none | list}
*Required contingencies:* {none | corporate VPN | reduced scope | clean device | ...}
*Approvals required:* Security [ ]  Legal (sanctions/data) [ ]  HR (tax, if >2 wks) [ ]
*Assumptions / gaps:* {list, incl. any UNVERIFIED items}

_Recommendation only — not an approval and not a legal or compliance determination. Facts re-verified as of the review date above; re-verify before final decision. Do not include confidential customer or personal data in this ticket._
```

## Guardrails

- **Recommendation, not decision.** Never state a trip "is approved." Output a recommended verdict for a human.
- **No action.** Do not create/transition tickets, email, or modify systems. If later wired to Jira, creation must be a reviewed draft, not an auto-submit.
- **Defer determinations.** Sanctions and data-protection calls are Legal's; flag, don't conclude.
- **Data minimization.** No confidential customer names, contract values, usage data, or excess personal data in the output — it lands in a ticket.
- **Fail safe.** Unverifiable blocker-domain facts → "manual review required," never "clear."

## Edge cases

- **Country not in any source / tiny jurisdiction:** return **MANUAL REVIEW** with what was found.
- **Territory ambiguity** (overseas territories and constituent countries, which may sit outside their parent state's legal regime): resolve the governing regime before rating Data Privacy.
- **Conflicting sources:** present both, take the **more conservative** rating, note the conflict.
- **Pre-approved country, over the short-stay limit:** no security review needed, but output the HR/tax flag.
- **Prior approval on file:** still re-verify and say so if the facts have moved. A
  prior approval is evidence about a date, not about today.

## Acceptance test cases

A build passes when each returns the expected tier **with** live-sourced, as-of-dated evidence per domain.

| Input profile | Expected verdict | Why |
|---|---|---|
| Adequacy country, short stay, Low across domains | Auto-approve (Tier 1) | Nothing to mitigate |
| No sanctions program, data privacy managed via a TIA | Approve (Tier 2) | Manageable, no blockers |
| InfoSec Layer A (network-layer observation) | Approve with contingency (Tier 3) | Contingencies apply |
| InfoSec Layer B (endpoint or forced disclosure) | Decline (Tier 4) | Layer B forces Tier 4 |
| Conditional data-privacy plus Legal/HR gates | Approve with contingency (Tier 3) | Gates, not blockers |
| Country sanctions program | Decline (Tier 4) | Sanctions force Tier 4 |
| Active-conflict geopolitical rating | Decline (Tier 4) | Conflict forces Tier 4 |

Profiles, not countries, on purpose: a country's rating is whatever Step 2 returns
on the day the review runs, and a fixed list of named verdicts would both go stale
and read as a standing judgement about those countries. Test with whatever
destinations your own sources currently place in each profile.

## Maintenance

- Owner: **Security**. Changes to decision logic require the standard owner's approval.
- Keep the description tight for accurate triggering; test against the acceptance cases before publishing.
- Version the skill to the standard (skill v1.0 ↔ standard v{{TRAVEL_STANDARD_VERSION}}). When the standard changes (rubric, tiers, sources), re-version both.
- Review at least every 12 months, or when a source-registry entry moves.
