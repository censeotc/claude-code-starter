# CenseoAI "AI Brain" — Build Spec for Claude Code

**Owner:** Scott Withers, Founder, CenseoAI (Traverse City, MI) — AI revenue operating system for HVAC/plumbing/gutter contractors, plus real estate technology consulting.

**Purpose of this document:** hand this file to Claude Code as the working spec for scaffolding and building CenseoAI's "AI Brain" — the shared knowledge layer, orchestration workflows, and governed agent workforce that runs CenseoAI's own internal operations and forms the reusable core of a future client-facing product. Claude Code should treat this as the source of truth for the build; update it in place as decisions get made rather than letting knowledge drift into chat history.

This spec synthesizes a full research blueprint already produced for this business (`AI-Brain-Blueprint-for-CenseoAI.md`, 486 lines) into an actionable, opinionated build plan scoped to the confirmed stack below. Read that file for the underlying research and citations if you want the "why" behind any decision here; this file is the "what to build."

---

## 1. Non-Negotiable Constraints

1. **No Azure, anywhere, in any form.** No Azure AI Search, Azure OpenAI, Cognitive Search, Cosmos DB, Event Hubs, or any other Azure service. If a workflow or tutorial defaults to Azure, substitute the self-hosted / open-source equivalent specified in this document.
2. **n8n is the orchestration backbone.** Do not introduce a second automation platform (Zapier, Make, LangGraph, CrewAI, etc.) to duplicate logic n8n can already do. n8n's native AI Agent node (LangChain-based), MCP Client/Server nodes, and HITL "tool gate" nodes (n8n 2.0+) cover the vast majority of orchestration needs for this build.
3. **GoHighLevel (GHL) remains the system of record** for contacts, deals, pipelines, and customer-facing conversation surfaces. n8n is the decision/orchestration layer sitting on top of it — never build parallel contact/deal logic inside n8n that duplicates what GHL already owns.
4. **Solo-founder scale discipline.** Do not build more than 3 agent roles in Phase 1. Every credible source in the underlying research converges on the same lesson: start narrow, expand only once workload data justifies a new specialist agent. The single most common documented regret is over-building (8 agents instead of 3 covering 80% of the value).
5. **No agent may autonomously modify financial thresholds, legal/compliance rules, or authentication logic.** These are hard-coded protected boundaries enforced in code (n8n IF/Switch logic or backend guards), never left to model self-restriction via prompting.
6. **Pricing and binding commitments are never generated freely by an LLM.** Any customer-facing pricing figure must be pulled from a verified database/lookup (GHL custom fields, a Postgres pricing table, or an n8n Data Table) — never composed by the model from its own reasoning. This is a direct response to the Air Canada chatbot liability ruling and the "$1 Chevy Tahoe" prompt-injection incident (see §7).

---

## 2. Confirmed Current Stack (do not re-ask about these)

| Component | Status | Detail |
|---|---|---|
| n8n | **Already running** | Self-hosted on a Hostinger VPS. Assume SSH/terminal access is available for deployment tasks. |
| Postgres | **Not yet provisioned** | Needs fresh install. Deploy alongside n8n on the same Hostinger VPS via Docker Compose, with the `pgvector` extension enabled from day one so it doubles as the knowledge-layer vector store — avoids standing up a separate vector-DB vendor. |
| LLM API access | **OpenAI and Anthropic (Claude) keys already held** | Use Claude for complex reasoning, compliance review, and content quality (marketing copy, compliance checks). Use GPT-4o for tool/function-calling-heavy workflows where OpenAI's function-calling reliability has historically had the edge. Bring these as n8n credentials — never rely on a platform's bundled/free AI credits for production workloads. |
| GoHighLevel (CenseoAI's own account) | **Standard/single-account plan** | Sufficient for Phase 1 internal use. **Flag for later:** if/when CenseoAI resells a productized workflow to multiple contractor clients under one agency umbrella, an Agency plan (sub-account + white-label capability) will likely be needed — this is a Phase 3 decision, not a Phase 1 blocker. |
| GHL (client deployments) | Existing pattern | At least one client is already running a "Communication Smart Response System" on a GHL Starter plan + a separate self-hosted n8n instance. Keep the CenseoAI internal Brain and client deployments architecturally separable — shared prompt/SOP libraries and workflow templates, but separate n8n workspaces/credentials per client for security isolation. |
| Cloud/infra | Hostinger VPS only | No AWS, no GCP, no Azure. If VPS resource limits become a bottleneck (CPU/RAM contention between n8n, Postgres, and any local embedding jobs), the fallback is a second, larger Hostinger VPS or migrating Postgres to a managed non-Azure provider (e.g., Supabase's free/low tier) — not a general cloud migration. |
| Observability | Not yet set up | Add Langfuse (open-source, self-hostable, framework-agnostic) in Phase 1 — deploy as a third container in the same Docker Compose stack. |

**Business scope decision (confirmed):** This build is scoped as **internal-first, resellable-by-design**. Build every workflow, prompt, and SOP as a clean, parameterized template (client name, pricing table, and service area as swappable config, not hardcoded) from day one, so Phase 3 productization is a packaging exercise, not a rebuild. See §9 for the licensing implication this creates.

---

## 3. Target Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  GoHighLevel (system of record)                              │
│  Contacts · Deals · Pipelines · Conversation AI · Voice AI    │
└───────────────┬─────────────────────────────────────────────┘
                │ webhooks + REST API (OAuth2, HTTP Request node)
                ▼
┌─────────────────────────────────────────────────────────────┐
│  n8n (self-hosted, Hostinger VPS) — orchestration layer        │
│  ├─ AI Agent nodes (OpenAI / Anthropic credentials)            │
│  ├─ MCP Client/Server nodes                                    │
│  ├─ HITL "tool gate" nodes on every consequential action       │
│  └─ IF/Switch nodes for rule-based safety/compliance routing   │
└───────┬───────────────────────────────────┬───────────────────┘
        │                                   │
        ▼                                   ▼
┌───────────────────────┐        ┌───────────────────────────┐
│ Postgres + pgvector     │        │ Langfuse (observability)   │
│ (Hostinger VPS, Docker) │        │ traces, evals, cost/latency│
│ ├─ knowledge embeddings │        └───────────────────────────┘
│ ├─ pricing/service data │
│ ├─ audit log table      │
│ └─ agent memory (facts) │
└───────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Git-backed knowledge repo (this Claude Code project)          │
│  SOURCE_OF_TRUTH.md · /sops · /prompts · /n8n-workflows (JSON) │
└─────────────────────────────────────────────────────────────┘
```

Everything left of "Git-backed knowledge repo" runs on the Hostinger VPS. The Git repo is the canonical, human-and-agent-readable knowledge layer that n8n workflows read from (via Git/HTTP nodes or a sync job that loads file contents into Postgres/pgvector) — Claude Code's job is to build and maintain this repo, the Docker Compose stack, and the n8n workflow exports.

---

## 4. Repo Structure Claude Code Should Scaffold

```
censeo-ai-brain/
├── SOURCE_OF_TRUTH.md              # canonical facts — always wins over agent memory
├── docker-compose.yml              # n8n + Postgres(pgvector) + Langfuse stack
├── .env.example                    # OPENAI_API_KEY, ANTHROPIC_API_KEY, GHL creds, DB creds — never commit real .env
├── docs/
│   ├── architecture.md             # mirrors §3 of this file, kept in sync
│   └── decision-log.md             # dated log of settled architecture/product decisions
├── sops/
│   ├── missed-call-text-back.md
│   ├── lead-qualification-hvac.md
│   ├── customer-followup.md
│   └── real-estate-disclosure-language.md
├── prompts/
│   ├── sales/lead-qualification-v1.md
│   ├── content/marketing-copy-review-v1.md
│   ├── compliance/real-estate-disclosure-check-v1.md
│   └── deprecated/                 # archived prompts, retained 1 year
├── n8n-workflows/                  # exported workflow JSON, versioned in Git
│   ├── 01-missed-call-textback.json
│   ├── 02-lead-qualifier.json
│   └── 03-followup-review-request.json
├── db/
│   ├── schema.sql                  # pricing tables, service-area tables, audit_log table, pgvector tables
│   └── migrations/
└── scripts/
    ├── sync-knowledge-to-pgvector.sh   # embeds /sops and /prompts content into pgvector on change
    └── deploy.sh                        # pulls repo on the VPS, restarts Docker Compose stack
```

**Claude Code task:** scaffold this structure first, commit it, then build outward. Keep `SOURCE_OF_TRUTH.md` and `docs/decision-log.md` living documents — every settled decision (pricing change, new SOP, new agent role) gets an entry with a date.

---

## 5. `SOURCE_OF_TRUTH.md` — Required Structure

This file is the single canonical document every agent checks before quoting a price, describing a feature, or referencing workflow status. If it conflicts with anything an agent "remembers" from a past session, this file always wins.

Required sections:

1. **Topic Index** — every canonical topic mapped to its governing file, dated.
2. **Live Products/Services** — CenseoAI's current, sellable packages only (pricing, URL). Explicitly exclude anything still in development.
3. **Decisions Already Made** — settled calls agents should not re-litigate (e.g., "n8n is the orchestration layer, not LangGraph," "no Azure," "GHL Standard plan for internal use, Agency plan deferred to Phase 3").
4. **In Development** — current build stage and blockers for each in-progress workflow/agent.
5. **Discontinued/Paused** — retained (not deleted) so an agent can explain why something no longer exists if asked.

**Maintenance rule:** update the relevant section and the topic index the moment something changes. Do a full read-through monthly to catch staleness. Tag every fact with a criticality tier:

| Tier | Example | Max staleness before it must be reviewed |
|---|---|---|
| Critical | Pricing, safety/dispatch protocols, real-estate disclosure language | 0 days (update immediately on change) |
| Reference | Case studies, historical service records | 30 days |
| Contextual | General industry background | 90 days |

---

## 6. Phase 1 — Foundation (Weeks 1–4)

**Goal:** one working, narrowly-scoped agent in production, with the knowledge layer and safety rails in place before it goes live.

1. **Scaffold the repo and Docker Compose stack** (n8n + Postgres/pgvector + Langfuse) on the Hostinger VPS. Confirm n8n's existing instance either gets folded into this Compose stack or is left standalone with Postgres/Langfuse added alongside it — do not run two separate n8n instances.
2. **Write `SOURCE_OF_TRUTH.md`** with CenseoAI's real current pricing/packages, positioning decisions, and the "no Azure / n8n-centric / internal-first-resellable-by-design" decisions already made.
3. **Write the first 3–4 SOPs** as versioned Markdown at the "Goldilocks altitude" — specific enough to reliably guide agent behavior, flexible enough to act as a heuristic, not a brittle script. Start with: missed-call text-back, HVAC lead qualification, customer follow-up/review request, and real-estate disclosure language (compliance-critical — see §8).
4. **Encode safety/compliance-bound logic as explicit n8n IF/Switch rules**, not LLM judgment: emergency dispatch escalation triggers, refund/cancellation policy, and any real-estate compensation-disclosure logic. Reserve semantic/LLM routing for open-ended intent classification only (e.g., "is this a sales inquiry or a support request").
5. **Build the first agent: missed-call text-back**, targeting the documented 6–14% booked-appointment-recovery benchmark for HVAC/plumbing/gutter trades. Build on GoHighLevel Conversation AI (already available on the Standard plan) + n8n's AI Agent node for orchestration and any cross-tool logic GHL's native AI can't handle.
   - This doubles as the first resellable module — build it parameterized (client name, service area, pricing table as config) from the start.
6. **Stand up Langfuse before this agent goes live**, not after the first incident. Trace every agent run: inputs, tool calls, outputs, latency, cost.
7. **Set up the pricing/commitment guardrail immediately**: any GHL Conversation AI or n8n AI Agent response that would quote a price or make a commitment must pull from the Postgres pricing table (or a GHL custom field / n8n Data Table), never be composed freely by the model. Add an output filter that catches commitment-implying language ("I can offer," "that's a deal," "guaranteed") before it reaches a customer, and route it to human review if triggered.

**Definition of done for Phase 1:** the missed-call text-back agent is live for at least one real conversation flow, every action it takes is traced in Langfuse, pricing is never freely generated, and `SOURCE_OF_TRUTH.md` + the first 4 SOPs exist and are accurate as of go-live.

---

## 7. Phase 2 — Expand Deliberately (Months 2–4)

**Goal:** grow from 1 to 3 agent roles (the documented "start with 3, not 8" ceiling for this stage), and add the retrieval/memory layer once the knowledge base outgrows what fits in a single context window.

8. **Add two more agent roles**, each with its own scoped n8n credential (never a shared login) and explicit escalation thresholds:
   - **AI Operations Manager/Orchestrator** — daily task routing, workflow-health monitoring, exception escalation to the founder.
   - **AI SDR/Lead Qualifier** — CRM read/write against GHL, qualification questions, hand-off to a human closer above a deal-size threshold you define in `SOURCE_OF_TRUTH.md`.
9. **Add the retrieval layer only once justified.** Use n8n Data Tables for small, structured facts (pricing rules, service areas) — this is lighter-weight than a full vector index and should be the default for anything that fits. Reserve pgvector (already provisioned in Phase 1) for larger, unstructured corpora: onboarding docs, historical support tickets, compliance reference material. Chunk Markdown/prose recursively at roughly 512–1,024 tokens with 10–20% overlap; use document-structure-aware chunking for the SOP library so headings and lists aren't split mid-section.
10. **Implement n8n HITL "tool gates"** (n8n 2.0+) on every action with real-world consequence: sending client-facing communication, changing pricing, modifying a live automation, or generating real-estate compensation/disclosure language. Lower-stakes internal actions (drafting, tagging, internal logging) can run with audit-trail-only review, no gate.
11. **Add persistent agent memory** via a lightweight, self-hostable framework rather than building one from scratch. Given CenseoAI's CRM-adjacent context where facts genuinely change over time (a lead's stated budget, a contractor's service-area coverage), prioritize a framework with **temporal fact-invalidation** (old facts retained as history, not silently overwritten) over one that only does flat semantic recall. Evaluate self-hostable options against this requirement before picking one — do not default to a managed/cloud-only memory service if a self-hosted equivalent meets the bar.
12. **Standardize the agent-to-agent hand-off payload** as one JSON schema (task description, context, reason) used consistently across every n8n sub-workflow and any human hand-off, so hand-offs aren't "improvised negotiations."

---

## 8. Phase 3 — Governance, Scale, and Productization (Month 4+)

13. **Tag `SOURCE_OF_TRUTH.md` and SOP content by the criticality tiers in §5**, and put a real calendar reminder (not just an agent-run check) on the founder's calendar to review critical-tier content weekly.
14. **Build a feedback queue, not direct edits.** If an agent notices a broken SOP, stale pricing, or a workflow failure, it writes a proposal to a review queue (a Postgres table or a dedicated n8n workflow that surfaces to the founder) — a human reviews and implements the change. No agent edits its own or another agent's core instructions autonomously.
15. **Formalize identity and access control per agent.** Give every agent its own n8n credential set scoped to only what it needs (least privilege). Inventory every agent and its credential type; treat any workflow currently authenticating through a shared/personal login as an immediate remediation item.
16. **Resolve the n8n licensing question before reselling anything built on n8n itself.** n8n's self-hosted Community Edition is distributed under the Sustainable Use License ("fair-code," not OSI open source). Internal business use is free and unrestricted, and building consulting services *around* n8n is explicitly permitted — but **white-labeling or reselling n8n itself as the backend of a paid product to CenseoAI's contractor/real-estate clients requires a separate Embed Partner commercial agreement with n8n.** Confirm current terms and pricing directly with n8n before any Phase 3 productization launch — do not assume the Community Edition license covers a resold/white-labeled product.
17. **Revisit the GHL plan tier.** If productizing for multiple clients under one umbrella, evaluate upgrading CenseoAI's own GHL account from Standard to an Agency-tier plan for sub-account and white-label support. This is a Phase 3 decision gated on having 2+ paying workflow clients, not a Phase 1/2 blocker.
18. **Only after the first 2–3 agent roles are proven reliable at real production volume**, consider a fully custom, code-first agent architecture (e.g., LangGraph — free, MIT-licensed, not tied to a single vendor's roadmap) if CenseoAI wants a fully differentiated, IP-owned agent product distinct from an n8n-based offering. Do not reach for this before Phase 1–2 are proven; it adds engineering surface area a solo founder doesn't need yet.

---

## 9. Agent Roles — Phase 1–2 Org Chart

| Agent role | Analogous title | Core responsibilities | Phase introduced |
|---|---|---|---|
| Missed-Call Text-Back Agent | Front-desk responder | Detects missed call, sends SMS text-back, books or qualifies, escalates on keyword triggers | Phase 1 |
| AI Operations Manager/Orchestrator | COO | Task routing across other agents, workflow-health monitoring, exception escalation to founder | Phase 2 |
| AI SDR/Lead Qualifier | AE/SDR | CRM read/write in GHL, qualification questions, hand-off to founder above a deal-size threshold | Phase 2 |
| **Founder (human, non-delegable)** | CEO/Strategist | Strategic pivots, pricing philosophy, client-relationship judgment calls, final sign-off on anything touching money, legal/compliance exposure, or authentication | Always |

Do not add a 4th automated agent role until the first three are running reliably at real volume with a measured approval/correction rate you're comfortable with (see §10 for what "reliable" should be measured against).

---

## 10. Metrics to Track From Day One

| Metric | What it tells you |
|---|---|
| Task success/accuracy rate | % of agent actions completed correctly without human correction — track at real volume, not just pilot volume (accuracy at 10 test runs does not predict accuracy at 1,000 real runs) |
| Approval/correction rate | % of agent-proposed actions approved unmodified vs. corrected by you — this should drive whether an agent's autonomy expands or contracts |
| Escalation rate & resolution time | Volume of items escalated to you, and how fast you resolve them |
| Cost per resolved task | Token + tool cost ÷ successfully completed tasks — track per agent |
| Containment rate | % of customer interactions (e.g., missed-call text-backs) fully resolved without you stepping in |

Wire these into Langfuse dashboards from Phase 1, not retrofitted later.

---

## 11. Compliance Guardrails (Bake These In, Don't Bolt On Later)

- **Businesses are legally liable for what their AI agents say.** A 2024 tribunal ruling (Moffatt v. Air Canada) held a company liable for its chatbot's false statement, rejecting the argument that a chatbot is a "separate legal entity" — the chatbot's word is the company's word, and customers have no duty to double-check it elsewhere on the site ([American Bar Association](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)). This is the direct justification for the pricing/commitment guardrail in §1 and §6.
- **Prompt injection is a real, demonstrated risk to pricing/commitment logic.** A dealership's chatbot was prompt-injected into "legally" agreeing to sell a vehicle for $1 ([Business Insider](https://www.businessinsider.com/car-dealership-chevrolet-chatbot-chatgpt-pranks-chevy-2023-12)). Guardrails must be enforced in code (the pricing-table lookup, the output filter), never by prompting the model to "not do that" — prompt-only restrictions are necessary but insufficient against injection.
- **Real estate disclosure language must reflect the current post-NAR-settlement rules.** As of January 1, 2026, NAR's Code of Ethics amendments limit compensation-disclosure obligations to a REALTOR's own client(s), and written buyer-broker agreements may include compensation terms with no obligation to disclose them to sellers/their brokers ([NAR, November 2025 Board of Directors Special Report](https://www.nar.realtor/breaking-news/special-report-from-the-november-17-2025-board-of-directors-meeting)). Any agent generating buyer-facing communications or compensation language must route through the compliance SOP (`sops/real-estate-disclosure-language.md`) and, in Phase 2+, a compliance-review gate before reaching a client.
- **Fair Housing Act (FHA) algorithmic-discrimination exposure applies to CenseoAI as a technology provider, not just to the businesses using the technology**, per HUD's reinstated disparate-impact standard — a system can violate the FHA purely through discriminatory outcomes, regardless of intent. Any future AI-assisted property valuation, tenant-screening, or listing-recommendation feature needs bias review before shipping, not after a complaint.
- **Standard comms compliance still applies**: TCPA (texting/calling consent), CAN-SPAM (email), GDPR/CCPA (data handling) — bake consent capture and opt-out handling into the missed-call text-back workflow from day one, since it is customer-communication infrastructure.

---

## 12. Open Decisions for Later (Not Blockers for Phase 1)

Track these in `docs/decision-log.md` as they get resolved — do not let them block starting Phase 1:

- Exact Embed Partner terms/cost for reselling n8n-based workflows (confirm with n8n directly before any Phase 3 client resale launch).
- Whether/when to upgrade CenseoAI's own GHL account from Standard to Agency tier.
- Which self-hostable persistent-memory framework best fits the temporal-fact-tracking requirement in §7 (evaluate 2–3 candidates against real CenseoAI use cases before committing).
- Whether a second Hostinger VPS or a managed Postgres provider is needed once pgvector's corpus grows past what the current VPS comfortably handles.
- Formal SOC 2-style posture (RBAC + ABAC across all agent identities, documented incident-response plan for agent-misfire scenarios) — worth planning toward as CenseoAI's B2B SaaS positioning matures, not required for Phase 1–2.

---

## 13. Source Material

This spec condenses the full research report already produced for CenseoAI: `AI-Brain-Blueprint-for-CenseoAI.md` (486 lines, covering second-brain-to-AI-brain architecture, orchestration platform landscape, organizational design, governance/compliance, change management case studies, and failure modes). Read that file for the underlying citations and deeper reasoning behind any recommendation above. Key sources referenced directly in this spec:

- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [dev.to — What Is a Source-of-Truth Document for AI Systems?](https://dev.to/michael_xero_ai/what-is-a-source-of-truth-document-for-ai-systems-and-why-you-need-one-40f2)
- [AgentMarketCap — Why 78% of Enterprise AI Agent Pilots Never Scale](https://agentmarketcap.ai/blog/2026/04/23/ai-agent-pilot-to-scale-failure-anatomy-2026)
- [DEV Community — I Run a Solo Company with AI Agent Departments](https://dev.to/setas/i-run-a-solo-company-with-ai-agent-departments-50nf)
- [n8n — Sustainable Use License docs](https://docs.n8n.io/privacy-and-security/sustainable-use-license/)
- [HighLevel Support Portal — Pricing & Billing guide](https://help.gohighlevel.com/support/solutions/articles/155000001156-highlevel-pricing-guide)
- [American Bar Association — Air Canada chatbot liability analysis](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)
- [NAR — Special Report from the November 17, 2025 Board of Directors Meeting](https://www.nar.realtor/breaking-news/special-report-from-the-november-17-2025-board-of-directors-meeting)
- [Prestyj — Missed-call text-back conversion benchmark report](https://prestyj.com/blog/missed-call-text-back-conversion-rate-improvement-contractors-2026)
