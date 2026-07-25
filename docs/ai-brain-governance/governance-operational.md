# CenseoAI Governance — Operational Summary for the AI Brain

Working summary of the **CenseoAI Governance Template v4.9 (FINAL, March 2026)** — aligned with NIST AI RMF, ISO/IEC 42001/42005, FTC guidance, and the FCC TCPA ruling. This file is what the AI Brain reads and applies; the signed template is authoritative if they ever disagree. **Copy this file into your vault's `context/governance.md`.**

## Current recognition status (governs what the Brain may do)

- **Module A (non-voice)**: HELD pending Appendix D (vendor inventory) population. **Module B (voice/TCPA)**: HELD pending Module A + counsel verification + Appendix F per state.
- **Operating implications until recognition:**
  - The **no-release rule** applies to anything containing contractual, warranty, guarantee, refund, or regulated telecom content: not released without legal review, period.
  - **No autonomous external sends of any kind** — every external communication takes the manual-routine path (human-reviewed, logged).
  - **Voice agents are out of scope entirely** (no AI voice tools in any client workflow) until Module B is recognized.
  - New or revised **quantified public claims** (ROI figures, case-study numbers, calculator outputs) need a Claim-Evidence ID once the register exists; until then, treat every new quantified public claim as blocked.

## The six reliance tiers — every output gets one

| Tier | What it may do | Hard prohibitions | Governance required |
|---|---|---|---|
| **Exploratory** | Inform thinking, brainstorm | No external use, no citing as fact, no decisions | Creator notes AI-generated status |
| **Internal Provisional** | Drafts, preliminary analysis | Can't drive pricing, commitments, published claims | Creator fact-checks; label; log |
| **Internal Operational** | Support internal decisions | No policy, comp, prospect-ROI, segmentation w/o evidence | SME review; cross-check vs. source systems; audit trail |
| **Internal High-Impact** | Inform pricing, positioning, spend, staffing | Not actionable without independent verification | Dual review; source data verified; rationale documented |
| **External Routine** | Low-risk reversible comms (follow-ups, confirmations, scheduling) | No quantified ROI, legal assurances, competitor claims, custom pricing, binding commitments | Manual-routine path: human review + simplified release log |
| **External High-Stakes** | Prospect-specific ROI, pricing, proposals, contractual language | No release without individual verification + written operator approval (+ legal if regulated) | Individual SME verification; full traceability |

**Auto-classification:** contractual / warranty / guarantee / refund language → External High-Stakes automatically → currently the no-release rule.

## Escalation thresholds — when tool-level trust is not enough

Individual output verification is required when ANY of these hit (most conservative trigger wins):

- **Absolute:** prospect-specific dollar figure · ROI/savings claim for a specific business · contractual/guarantee/refund language · named-competitor factual claim · recipient previously dissatisfied · recommendation > $10,000
- **Relative:** > 5% of client's annual revenue · > 10% of quoted job/project value · > 15% of monthly budget · changes projected deal margin > 3 points

## Disclosure taxonomy (labels — use these terms exactly)

| Tier | Label | Recipient disclosure |
|---|---|---|
| Exploratory | AI-Generated (recommended) | n/a |
| Internal Provisional / Operational | AI-Generated or AI-Assisted (+ Human-Reviewed for Operational) | n/a |
| Internal High-Impact | AI-Generated + Human-Reviewed (document header) | n/a |
| External Routine | AI-Assisted in template metadata | Optional; if visible, must use taxonomy terms exactly |
| External High-Stakes | AI-Assisted + Human-Approved for Release (document body) | Yes — substantive AI contribution disclosed |
| Voice (Module B only) | — | "AI-Powered", spoken, within first 15 seconds |

## Tier transitions (admission rules, condensed)

- → Internal Provisional: creator documents output, model, prompt version, limitations.
- → Internal Operational: SME reviews claims against CRM/financial/operational sources.
- → Internal High-Impact: independent second review; source-data snapshot retained.
- → External Routine: current tool validation (≤ 90 days) + monitoring clean + monthly spot-check — or the manual-routine path (human review + simplified log).
- → External High-Stakes: individual verification, figures checked against source data, **written operator approval**, legal review if regulated.

## Revalidation triggers (any of these voids validated status)

Model/provider change · prompt change · knowledge-base change · CenseoAI or client pricing/offer change · >2 AI-attributed complaints/month · 3+ drift flags in 30 days · any governance incident · legal/regulatory change.

## Document-asset conventions (reports, briefs, client deliverables)

- **Source tiers:** T1 primary/official sources → T2 reputable reporting → T3 commentary. Contradictions resolve toward the higher tier. Cite with verification dates.
- **Claim labels:** mark claims **VERIFIED** (checked against T1 today), **GOVERNED** (produced under this template), **RECOMMENDATION** (advice), or **INFERENCE/ESTIMATE** (never present an estimate as fact).
- **Currency & editions:** every asset carries a currency date; content updates bump the edition (x.y for fact refreshes, next whole number for rewrites) with a "What changed" note. Re-verify anything older than **90 days** before relying on it.

## How the AI Brain applies all this

1. Every skill/agent output **states its tier** at the top. Default for drafts: Internal Provisional.
2. Anything crossing the boundary to a client/prospect is **External** — Routine via the manual path (you review, it logs), High-Stakes via individual verification + your written OK.
3. Every action lands in the **action log** (see [logging.md](logging.md)); external releases get release-log entries; incidents follow the [incident playbook](incident-playbook.md).
4. `/revenue-scoreboard`, `/client-report`, `/aeo-snapshot`, and proposal outputs are **External High-Stakes by default** — they carry quantified, client-specific claims.
5. `/inbox-triage`, `/follow-up`, `/email-draft` sends are **External Routine, manual path** — approval = simplified release log entry.
6. Logs are queryable within 24 hours (`/audit-trail`) and retained for the governance period + 2 years (incidents + 3) — in practice: the `logs/` folder is append-only and never pruned; git history is the retention mechanism.
