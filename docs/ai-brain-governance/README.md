# AI Brain — Governance & Audit Layer

The AI Brain's implementation of the **CenseoAI Governance Template v4.9** (NIST AI RMF / ISO 42001-aligned), plus the logging and correction machinery that makes every action traceable and every failure a one-time event.

| File | What it is |
|---|---|
| [governance-operational.md](governance-operational.md) | The working summary the Brain reads: reliance tiers, escalation thresholds, disclosure taxonomy, admission rules, recognition status. Copy into your vault as `context/governance.md`. |
| [logging.md](logging.md) | The black box recorder: daily action log, release log, event-log spec, the CLAUDE.md standing rules, and the daily-checkpoint routine. |
| [incident-playbook.md](incident-playbook.md) | Severity tiers, the six response steps, the incidents.md template, and the correction loop (no incident closes without a file diff). |

Query layer: the [`/audit-trail`](../ai-brain-skills/audit-trail/SKILL.md) skill — trace by client/agent/date, verify releases, find log gaps, run the monthly spot-check.

**Note:** the signed Governance Template v4.9 itself is the authoritative document and is intentionally NOT stored in this repo — this layer is the operational implementation. Keep the signed template wherever your governance artifacts live, and update `governance-operational.md` if the template revs.
