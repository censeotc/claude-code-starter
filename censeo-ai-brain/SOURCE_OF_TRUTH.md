# SOURCE OF TRUTH — CenseoAI

**This file always wins.** If anything an agent "remembers," a prompt implies, or a past chat said conflicts with this file, this file is correct. Check here before quoting a price, describing a product, or referencing build status.

Last full read-through: 2026-07-25 · Owner: Scott Withers · Review cadence: monthly full pass; Critical-tier items immediately on change.

---

## 1. Topic Index

| Topic | Governing file | Tier | Last verified |
|---|---|---|---|
| Products, pricing, packages | §2 below | Critical | 2026-07-25 (placeholders — see §2) |
| Architecture & stack decisions | §3 below + [docs/architecture.md](docs/architecture.md) | Critical | 2026-07-25 |
| Build status | §4 below | Reference | 2026-07-25 |
| Missed-call text-back behavior | [sops/missed-call-text-back.md](sops/missed-call-text-back.md) | Critical | 2026-07-25 |
| HVAC lead qualification | [sops/lead-qualification-hvac.md](sops/lead-qualification-hvac.md) | Critical | 2026-07-25 |
| Follow-up / review requests | [sops/customer-followup.md](sops/customer-followup.md) | Reference | 2026-07-25 |
| Real-estate disclosure language | [sops/real-estate-disclosure-language.md](sops/real-estate-disclosure-language.md) | Critical | 2026-07-25 |
| Governance (reliance tiers, logging, incidents) | CenseoAI Governance Template v4.9 (signed copy, kept with governance artifacts) + [../docs/ai-brain-governance/](../docs/ai-brain-governance/) | Critical | 2026-07-25 |
| Settled decisions | [docs/decision-log.md](docs/decision-log.md) | Reference | 2026-07-25 |

**Criticality tiers:** Critical = review immediately on change (0-day staleness). Reference = 30 days. Contextual = 90 days.

## 2. Live Products / Services (sellable today)

> ⚠ **NEEDS-INPUT (Critical):** dollar figures below are PLACEHOLDERS. Scott must replace them before any agent references pricing — and per the pricing guardrail, agents never quote from this file's prose anyway: customer-facing prices come only from the Postgres `pricing` table / GHL custom fields (see BUILD-SPEC §1.6).

| Package | What it is | Price | Status |
|---|---|---|---|
| Revenue Leakage Audit | Find the money dying in the client's CRM; often creditable into pilot | NEEDS-INPUT | Live |
| 45-Day Pilot | Fixed-fee Revenue Operating System pilot with measurable outcomes | NEEDS-INPUT | Live |
| 90-Day Revenue Operating System build | Full install inside client's existing stack | NEEDS-INPUT | Live |
| Optimization retainer | Monthly, seasonal optimization | NEEDS-INPUT | Live |
| Real estate technology consulting | Advisory engagements | NEEDS-INPUT | Live |

**Explicitly NOT sellable yet** (do not describe as available): AI voice agents (blocked by Governance Module B), channel/dealer rollouts (Phase 3), any white-labeled n8n-based product (licensing unresolved — decision-log #7).

**Target market:** HVAC / plumbing / gutter contractors (primary; service-heavy, 10+ trucks, ServiceTitan or similar), plus real estate technology consulting.

## 3. Decisions Already Made (do not re-litigate)

1. **No Azure. Anywhere.** Self-hosted / open-source equivalents only.
2. **n8n is the orchestration backbone** (self-hosted, Hostinger VPS). No second automation platform.
3. **GoHighLevel is the system of record** for contacts, deals, pipelines, conversation surfaces — everywhere, including Scott's personal vault skills (decided 2026-07-25). n8n orchestrates on top; never duplicate contact/deal logic.
4. **Internal-first, resellable-by-design.** Everything parameterized (client name, pricing table, service area as config) from day one.
5. **Max 3 autonomous agent roles through Phase 2.** The 19-role Claude-side roster is a separate layer: advisory copilots for the founder with zero autonomy and zero infrastructure — the 3-agent cap applies to production agents only (decided 2026-07-25).
6. **Pricing/commitments are never LLM-composed.** Database lookup + output filter, enforced in code.
7. **Launch sequencing: HITL now, autonomous later.** Missed-call text-back goes live with a human-approval gate on every send (v4.9 manual-routine path). Autonomous mode only after Governance Module A recognition (Appendix D populated), with the 13-field event log writing to Postgres `audit_log` (decided 2026-07-25).
8. **GHL Standard plan for now.** Agency tier is a Phase 3 decision gated on 2+ paying workflow clients.
9. **Langfuse for observability**, deployed with the stack before the first agent goes live.
10. **Postgres + pgvector on the same VPS** — no separate vector-DB vendor.

## 4. In Development

| Item | Stage | Blocker |
|---|---|---|
| Repo scaffold + Docker Compose stack | Scaffolded in git; not yet deployed to VPS | Run `scripts/deploy.sh` on the VPS; fold existing n8n into the stack (one instance only) |
| SOURCE_OF_TRUTH pricing section | Placeholders | Scott inputs real prices; then seed `db/schema.sql` pricing table |
| Missed-call text-back agent (Phase 1 agent #1) | SOP + workflow design written | Build in n8n from [n8n-workflows/01-missed-call-textback.md](n8n-workflows/01-missed-call-textback.md); HITL gate ON |
| Governance Module A recognition | HELD | Populate Appendix D vendor inventory (now includes: n8n, Hostinger, OpenAI, Anthropic, GoHighLevel, Langfuse, Postgres) + sign declaration + day-0 claims snapshot |
| Langfuse tracing | In compose file; not deployed | Deploy; wire n8n agent runs to Langfuse before go-live |
| AI Ops Manager + AI SDR (agents #2, #3) | Not started | Phase 2 — gated on agent #1 running reliably at real volume |

## 5. Discontinued / Paused (kept so agents can explain why)

| Item | Status | Why |
|---|---|---|
| Airtable as CRM of record in vault skills | Superseded 2026-07-25 | GHL is the single system of record (decision #3) |
| AEO/GEO/SEO-first positioning | Deprioritized | Business model is Revenue Operating Systems; SEO/AEO is a supporting/partner function (see vault seo-analyst agent) |
| AI voice agents in any client workflow | Paused | Governance Module B held: counsel verification + per-state Appendix F required first |
| Autonomous external sends of any kind | Paused | Module A recognition pending; manual-routine (HITL) path only |
