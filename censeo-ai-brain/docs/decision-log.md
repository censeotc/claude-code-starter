# Decision Log

Settled calls, dated. Agents and humans: do not re-litigate — reopen only with new evidence, and log the reopening here.

| # | Date | Decision | Rationale |
|---|---|---|---|
| 1 | pre-2026-07 | No Azure, anywhere | Owner constraint (BUILD-SPEC §1.1) |
| 2 | pre-2026-07 | n8n is the orchestration backbone; no second automation platform | Already running; native AI Agent/MCP/HITL nodes cover needs (§1.2) |
| 3 | pre-2026-07 | GoHighLevel is the system of record | §1.3 |
| 4 | pre-2026-07 | Internal-first, resellable-by-design; everything parameterized | §2 confirmed scope |
| 5 | 2026-07-25 | censeo-ai-brain lives as a subdirectory of claude-code-starter for now; split to its own repo when Scott creates it | Momentum over ceremony; split is cheap later |
| 6 | 2026-07-25 | Two scoped layers: 3-autonomous-agent cap applies to production (n8n); the 19-role Claude roster is advisory-only with zero autonomy | Spec's over-building warning targets deployed agents, not prompt personas |
| 7 | 2026-07-25 | GHL is CRM of record EVERYWHERE, incl. Scott's vault skills; Airtable demoted to non-CRM uses only | One system of record, no sync drift |
| 8 | 2026-07-25 | Launch sequencing: missed-call text-back ships with HITL gate on every send (v4.9 manual-routine path); autonomous only after Module A recognition + tool validation + ≥95% unmodified approval over 30+ sends | Reconciles BUILD-SPEC weeks-1–4 timeline with signed Governance v4.9 |
| 9 | 2026-07-25 | Langfuse v2 (single-Postgres) not v3 | Right-sized for one VPS; revisit on trace volume |

## Open (tracked, non-blocking — BUILD-SPEC §12)
- n8n Embed Partner terms before any Phase 3 resale of n8n-based product
- GHL Standard → Agency tier (gate: 2+ paying workflow clients)
- Persistent-memory framework with temporal fact-invalidation (evaluate 2–3 self-hostable candidates; `agent_memory` table is the interim)
- Second VPS / managed Postgres if pgvector outgrows current box
- SOC 2-style posture as B2B positioning matures
- Fold existing n8n instance into the Compose stack vs. run alongside (decide at first deploy — one instance only)
- Real pricing figures into SOURCE_OF_TRUTH §2 + `pricing` table (NEEDS-INPUT, blocks any price quoting)
- AI SDR deal-size handoff threshold (NEEDS-INPUT before workflow 02)
