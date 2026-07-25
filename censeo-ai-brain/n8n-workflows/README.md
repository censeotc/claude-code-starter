# n8n Workflows — versioning convention

**Why there are .md design docs here and not fabricated .json:** workflow JSON must be exported from the actual n8n instance (it embeds node versions and credential references specific to that install). Hand-written JSON that never ran is a liability pretending to be a backup.

**The loop:**
1. Each workflow starts as a numbered design doc here (`01-missed-call-textback.md`) — nodes, gates, guardrails, test plan. Build it in the n8n editor on the VPS from that doc.
2. After it works, export it: n8n editor → workflow menu → Download, save as `01-missed-call-textback.json` next to its design doc, commit both.
3. Every meaningful change: re-export, commit with a message saying what changed and why. The JSON in git is the disaster-recovery copy and the change history.
4. Credentials are NEVER in exports (n8n strips them) — they live only in the n8n credential store, one scoped credential set per agent (least privilege, BUILD-SPEC §8.15).

| # | Workflow | Design doc | JSON | Status |
|---|---|---|---|---|
| 01 | Missed-call text-back | [01-missed-call-textback.md](01-missed-call-textback.md) | pending first export | Design complete |
| 02 | Lead qualifier | [02-lead-qualifier.md](02-lead-qualifier.md) | — | Phase 2 |
| 03 | Follow-up / review request | [03-followup-review-request.md](03-followup-review-request.md) | — | Phase 2 |
