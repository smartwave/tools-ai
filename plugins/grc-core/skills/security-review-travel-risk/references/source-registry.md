# Source Registry — Travel Risk Review

Canonical, authoritative sources for each risk domain. **Always fetch the current value in-run and record the source URL + an "as-of" date.** These registry entries are pointers, not cached answers — the standard requires live re-verification every run. If a source has moved, update this file (and re-version per the standard's maintenance rules) rather than guessing.

## Sanctions
- **OFAC Sanctions Programs and Country Information** — https://ofac.treasury.gov/sanctions-programs-and-country-information — is there a country program? (y/n)
- **OFAC SDN List search** — https://sanctionssearch.ofac.treas.gov/ — recent SDN activity for the country.
- A country sanctions program forces **Tier 4 (Decline)**. Unverifiable → **manual review required**, never "clear."
- Sanctions determinations are **Legal's** call — flag, don't conclude.

## Geopolitical
- **U.S. State Department Travel Advisories** — https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html — current advisory level (1–4) and any ordered/authorized-departure notice.
- Active-conflict geopolitical status forces **Tier 4 (Decline)**.

## Data Privacy
- **EU adequacy decisions** — https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en — adequacy status.
- Local data-protection law: confirm existence and nature via the national data-protection authority / official gazette.
- **Internal:** check whether any customer DPA restricts the access location. Do **not** paste customer names or contract terms into the ticket — reference the restriction generically.
- Data-protection determinations are **Legal's** call — flag, don't conclude.

## Information Security — state-sponsored traffic observation
Classify observation as **none / network-layer (A) / endpoint-or-forced-disclosure (B)**.

**Baseline (network layer / signal):**
- **Freedom on the Net** (Freedom House) — https://freedomhouse.org/report/freedom-net — standing/score. Treat as a signal; corroborate before it drives a decline.

**Layer B evidence (endpoint / forced disclosure) — requires a forensic source:**
- **Citizen Lab** — https://citizenlab.ca/ — targeted spyware research.
- **Amnesty International Security Lab** — https://securitylab.amnesty.org/ — forensic spyware evidence.
- **Forbidden Stories (Pegasus Project)** — https://forbiddenstories.org/ — investigative corroboration.
- Also check for: mandatory decryption or VPN prohibition; border device-search practice.

**Rules:**
- Layer B claims require independent **forensic** evidence — a single index is not enough. Note any country denial, but base the rating on the forensic evidence.
- Layer A (network observation) → mitigable → **Tier 3 (contingency:** corporate VPN / reduced scope / clean device**)**.
- Layer B (endpoint/forced disclosure) → unavoidable → **Tier 4 (Decline)**.
- Unverifiable Layer B → **manual review required**, never "clear."
