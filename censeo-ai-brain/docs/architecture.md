# Architecture

Mirrors BUILD-SPEC §3 — keep in sync when either changes.

```
┌─────────────────────────────────────────────────────────────┐
│  GoHighLevel (SYSTEM OF RECORD)                              │
│  Contacts · Deals · Pipelines · Conversation AI · Voice AI    │
└───────────────┬─────────────────────────────────────────────┘
                │ webhooks + REST API (OAuth2, HTTP Request node)
                ▼
┌─────────────────────────────────────────────────────────────┐
│  n8n (self-hosted, Hostinger VPS) — orchestration layer        │
│  ├─ AI Agent nodes (OpenAI: tool-heavy · Claude: reasoning/     │
│  │   compliance/content)                                       │
│  ├─ MCP Client/Server nodes                                    │
│  ├─ HITL "tool gate" nodes on every consequential action       │
│  └─ IF/Switch CODE rules for safety/compliance routing         │
└───────┬───────────────────────────────────┬───────────────────┘
        ▼                                   ▼
┌───────────────────────┐        ┌───────────────────────────┐
│ Postgres + pgvector     │        │ Langfuse v2 (observability)│
│ ├─ pricing (quote-only  │        │ traces, evals, cost/latency│
│ │   source of prices)   │        └───────────────────────────┘
│ ├─ audit_log (v4.9      │
│ │   13-field event log) │
│ ├─ knowledge_chunks     │
│ ├─ agent_memory         │
│ │   (temporal facts)    │
│ └─ feedback_queue       │
└───────────────────────┘

Git repo (this directory) = canonical knowledge layer:
SOURCE_OF_TRUTH.md · /sops · /prompts · /n8n-workflows · db/schema
synced into pgvector by scripts/sync-knowledge-to-pgvector.sh
```

## The two layers (decision 2026-07-25)

| | Production layer (this directory) | Founder's cockpit (Claude vault — see ../docs/) |
|---|---|---|
| Runs on | n8n + GHL + Postgres on the VPS | Claude Code/desktop on Scott's machine |
| Agents | Max 3 autonomous roles (Phase 1–2) | 19 advisory copilots, zero autonomy |
| Talks to customers | Yes (HITL-gated until Module A recognition) | Never |
| Governance | v4.9 enforced in code + audit_log | v4.9 manual-path + markdown logs |
| Shared | GHL as the one CRM · Governance v4.9 · SOURCE_OF_TRUTH facts |

## Security posture
- Postgres and service ports bound to 127.0.0.1; reverse proxy + TLS in front of n8n/Langfuse.
- One scoped credential set per agent workflow (least privilege); shared/personal logins are remediation items.
- Protected boundaries (financial thresholds, compliance rules, auth logic) live in code — no agent may modify them (BUILD-SPEC §1.5).
- `.env` never committed; audit_log append-only for agent roles.
