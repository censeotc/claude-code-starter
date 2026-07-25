# Workflow design: 02 — Lead Qualifier (`WF-lead-qualifier-v1`) — PHASE 2

**Gated on:** workflow 01 running reliably at real volume (approval rate ≥95%, containment measured). Do not build early.

**SOP:** [../sops/lead-qualification-hvac.md](../sops/lead-qualification-hvac.md) · **Prompt:** [../prompts/sales/lead-qualification-v1.md](../prompts/sales/lead-qualification-v1.md)

Shape: GHL inbound (form/SMS/chat) → same compliance/code gates as 01 → AI Agent (GPT-4o cred, scoped) qualifies per SOP's five captures → n8n Switch routes by the CODE rules (emergency / hot-replacement / routine-book / out-of-area) → GHL writes (fields, stage, note, task) → audit_log + Langfuse.

Additions over 01:
- `check_service_area` + deal-size threshold handoff (threshold value lives in SOURCE_OF_TRUTH → synced to an n8n Data Table; NEEDS-INPUT before build).
- Own scoped GHL credential (read/write contacts+opportunities only — no settings, no billing).
- Hand-off payload uses the standard JSON schema (task, context, reason — BUILD-SPEC §7.12) for both human handoffs and future agent-to-agent calls.
