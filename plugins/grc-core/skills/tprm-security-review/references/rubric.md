# Rubric — TPRM Security Review

Every value here is transcribed from your organization's own policy. These are not cached answers: re-fetch the source pages each run and confirm the pinned versions before relying on this file.

- **Risk Management Policy** — wiki page `{{PAGE_ID_RISK_MANAGEMENT_POLICY}}`, pinned **v{{RISK_POLICY_VERSION}} ({{RISK_POLICY_DATE}})** — likelihood/impact scales, scoring matrix, risk response.
- **Third Party and Vendor Management Policy** — wiki page `{{PAGE_ID_TPRM_POLICY}}`, pinned **v{{TPRM_POLICY_VERSION}} ({{TPRM_POLICY_DATE}})** — data-sensitivity/impact framing, re-evaluation cadence, engagement gates.

## Stage A — Triage / inherent risk

Set assessment depth and re-evaluation cadence before scoring.

- **Risk axis** is driven by the **sensitivity of data** the vendor will access, process, or store: Restricted > Confidential > Internal > Public.
- **Impact axis** is driven by **business, contractual, and regulatory consequence** to {{ORG_NAME}}, its employees, and its customers.
- **Re-evaluation cadence (TPVM Policy):** high-risk and/or Major/Critical-impact vendors handling sensitive data, or with privileged access, are re-evaluated **at least annually**. Lower-risk vendors are re-evaluated periodically.
- **Engagement gate (TPVM Policy):** Confidential/Restricted data must not be shared until a risk assessment is complete and a written agreement with security terms (and an NDA where confidential data is exchanged) is executed.

## Stage C — Likelihood × Impact scoring

### Likelihood (1–5)
| Grade | Value | Meaning |
|---|---|---|
| Rare | 1 | Never happened; no reason to think it likely now |
| Unlikely | 2 | Possible but probably will not happen |
| Possible | 3 | On balance, more likely to happen than not |
| Likely | 4 | Would be a surprise if it did not occur |
| Certain | 5 | Already happens regularly or is imminent |

For a vendor, Likelihood is the probability of a security incident/breach given the assessed control posture (Stage B) and the data exposure.

### Impact (1–5)
| Grade | Value | Composite meaning (customer/contractual · operational · legal/regulatory) |
|---|---|---|
| Incidental | 1 | No effect · negligible · no implications |
| Minor | 2 | Local disturbance · some · small compliance risk |
| Moderate | 3 | Deliverable with difficulty · unwelcome but bearable · definite danger of operating illegally |
| Major | 4 | Crippled in key areas · severe effect on income/profit · operating illegally in some areas |
| Extreme | 5 | Out of business / no service · crippling · severe fines, possible imprisonment |

### Scoring matrix (reference configuration)

Rating = the cell at Likelihood (row) × Impact (column). This is a conventional 5×5
risk grid, supplied so the skill has a working default. **Your Risk Management Policy
governs**: replace these cells with your own matrix before use, and where the two
disagree, the policy wins. Encode the cells directly rather than re-deriving them
from band ranges — a grid and its prose bands can disagree at the boundaries, and
the grid is what produces a rating.

| Likelihood \ Impact | Incidental (1) | Minor (2) | Moderate (3) | Major (4) | Extreme (5) |
|---|---|---|---|---|---|
| **Certain (5)** | MEDIUM (5) | HIGH (10) | HIGH (15) | CRITICAL (20) | CRITICAL (25) |
| **Likely (4)** | LOW (4) | MEDIUM (8) | HIGH (12) | HIGH (16) | CRITICAL (20) |
| **Possible (3)** | LOW (3) | MEDIUM (6) | MEDIUM (9) | HIGH (12) | HIGH (15) |
| **Unlikely (2)** | LOW (2) | LOW (4) | MEDIUM (6) | MEDIUM (8) | HIGH (10) |
| **Rare (1)** | LOW (1) | LOW (2) | LOW (3) | LOW (4) | MEDIUM (5) |

Product → rating lookup (the only products that occur on a 1–5 grid): **LOW** = 1,2,3,4 · **MEDIUM** = 5,6,8,9 · **HIGH** = 10,12,15,16 · **CRITICAL** = 20,25.

## Risk response (Risk Management Policy)

| Rating | Response |
|---|---|
| Low | Deemed acceptable; formally accepted by the Risk Owner |
| Medium | Documented review by GRC Leadership to decide accept vs. treat |
| High | Outside risk tolerance → mandatory documented Risk Treatment Plan |
| Critical | Outside risk tolerance → mandatory documented Risk Treatment Plan |

A vendor rated High or Critical is **not within tolerance** and must not be engaged/continued until a Risk Treatment Plan is documented and signed off. Residual risk after treatment follows the same acceptance rules.

## Exceptions

Exceptions to the TPVM Policy may be granted only by the {{BUSINESS_TECHNOLOGY_LEAD_ROLE}}, the President, or the Board of Directors. The skill flags the need for an exception; it never grants one.
