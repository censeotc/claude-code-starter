# AI Brain Project — Master Manifest of Referenced Artifacts & Assets

**Purpose:** the complete index of every external artifact, source, asset, and reference from the founding build session (2026-07-24/25) — the starting record for the larger project. If it was uploaded, cited, produced, or depended on, it is listed here with its current location and status.

**Status legend:** ✅ in repo · 📎 delivered in chat only (re-generatable) · 🔒 kept off-repo by design · ⏳ pending / not yet obtained · 🌐 external live source

---

## 1. Source documents supplied by the founder

| Artifact | What it is | Where it lives now | Status |
|---|---|---|---|
| **CenseoAI Governance Template v4.9 FINAL** (.docx, March 2026) | The signed governance standard: modular recognition (Module A/B), six reliance tiers, 13-field event logging, incident response, TCPA/FTC/NAR compliance gates | Founder's governance records. Operational implementation in [`docs/ai-brain-governance/`](ai-brain-governance/) | 🔒 deliberately not committed |
| **CenseoAI Business Model Canvas** (1-page PDF, Feb 24 2026, "Confidential — prepared for 20Fathoms") | The real business model: Revenue Operating Systems ladder, segments, channels, dealer-network thesis | Founder's records. Facts embedded across agents/SOURCE_OF_TRUTH | 🔒 confidential — not committed |
| **AI Brain Build Spec for Claude Code** (.md) | The production build spec: no-Azure, n8n backbone, GHL system of record, 3-agent cap, phases 1–3 | [`censeo-ai-brain/BUILD-SPEC.md`](../censeo-ai-brain/BUILD-SPEC.md) — updated in place going forward | ✅ |
| **CenseoAI logo — clean, white/transparent background** (PNG 797×721) | Primary logo asset (AI-head mark + wordmark) | [`docs/assets/censeoai-logo.png`](assets/censeoai-logo.png) | ✅ |
| **CenseoAI logo — horizontal lockup** (PNG 329×150, Adobe Express export) | Footer/inline brand lockup | [`docs/assets/censeoai-logo-horizontal.png`](assets/censeoai-logo-horizontal.png) | ✅ |
| **CenseoAI logo — dark glowing render** (PNG 1536×1024) | Dark wallpaper-style render; used for the dark-cover PDF iteration and badge crop | Chat upload only (session uploads expire) | 📎 superseded by clean logo |
| **"Build an AI Agent Orchestration Plan" screenshot** (IMG_3402.jpeg) | Prompt tile that triggered the orchestration plan | Chat upload only | 📎 served its purpose |

> ⚠ **Action:** chat uploads and the session scratchpad are ephemeral. The two 🔒 documents and anything else worth keeping must live in the founder's own storage — confirm the signed v4.9 (plus its future Appendix D, Module A declaration, and day-0 claims inventory) has a permanent home.

## 2. Referenced but never provided (gaps to close)

| Artifact | Referenced by | Why it matters | Status |
|---|---|---|---|
| **`AI-Brain-Blueprint-for-CenseoAI.md`** (486-line research report) | BUILD-SPEC §7, §13 — "read that file for the underlying research and citations" | The evidentiary basis for every BUILD-SPEC decision; the spec says to consult it for "the why" | ⏳ upload to `censeo-ai-brain/` recommended |
| **Appendix D — populated vendor subprocessor inventory** | Governance v4.9 | Gate 1 blocking Module A recognition → blocks all autonomous sends. Now must include: n8n, Hostinger, OpenAI, Anthropic, GoHighLevel, Langfuse, Postgres | ⏳ founder task |
| **Module A Recognition Declaration + day-0 grandfathered claims inventory** | Governance v4.9 | The signature that activates Module A; starts the 60-day Claim-Evidence register clock | ⏳ founder task |
| **Claim-Evidence ID register** | Governance v4.9 | Required operational within 60 days of recognition or recognition auto-suspends | ⏳ founder task |
| **Real pricing figures** | `SOURCE_OF_TRUTH.md` §2, Postgres `pricing` table | NEEDS-INPUT placeholders; agents cannot quote until populated | ⏳ founder task |
| **AI SDR deal-size handoff threshold** | Workflow 02 design, SOURCE_OF_TRUTH | Blocks Phase-2 workflow 02 build | ⏳ founder task |
| **Approved real-estate language snippets** | `sops/real-estate-disclosure-language.md` | Template library for the compliance SOP | ⏳ founder + counsel |

## 3. Produced deliverables — the repo record

Repository: **github.com/censeotc/claude-code-starter** · all merged to `main` via PRs #5–#8.

| PR | Merge commit | What it shipped |
|---|---|---|
| [#5](https://github.com/censeotc/claude-code-starter/pull/5) | `e81bedc` | AI Brain guide (+9 starter skills, agents v1, brand assets, branded guide PDF) |
| [#6](https://github.com/censeotc/claude-code-starter/pull/6) | `1616424` | AI Agent Orchestration Plan |
| [#7](https://github.com/censeotc/claude-code-starter/pull/7) | `3541c6a` | Plain-English setup guide (+PDF), governance/audit layer, censeo-ai-brain scaffold |
| [#8](https://github.com/censeotc/claude-code-starter/pull/8) | `fb3d58c` | Client onboarding SOP + config template (+PDFs) |

**Founder's cockpit layer** (`docs/`): [ai-brain-guide.md](ai-brain-guide.md) · [ai-brain-setup.md](ai-brain-setup.md) · [ai-brain-orchestration.md](ai-brain-orchestration.md) · [ai-brain-skills/](ai-brain-skills/) (11 skills incl. `/revenue-scoreboard`, `/audit-trail`) · [ai-brain-agents/](ai-brain-agents/) (12 advisory agents) · [ai-brain-governance/](ai-brain-governance/) (v4.9 operational summary, logging spec, incident playbook) · [assets/](assets/) (2 logos + 2 branded PDFs).

**Production layer** (`censeo-ai-brain/`): BUILD-SPEC · SOURCE_OF_TRUTH · docker-compose (n8n+pgvector+Langfuse v2) · db/schema.sql (pricing, 13-field audit_log, temporal agent_memory, feedback_queue) · 5 SOPs (incl. client-onboarding) · 3 versioned prompts · workflow design docs 01–03 · clients/_template/config.yml · deploy + pgvector-sync scripts · docs/ (architecture, decision-log — **10 settled decisions**) · docs/pdf/ (2 branded PDFs).

**Chat-only deliverables** (re-generatable via `gen_branded_pdf.py`, currently in the ephemeral session scratchpad): the original unbranded 12-page guide PDF; two superseded branded-cover iterations (dark full-bleed; badge-on-white); the branded PDF pipeline scripts themselves (`gen_branded_pdf.py`, `md2pdf_branded.py`, `render_final.py`). ✅ Resolved in this commit: the reusable generator is now [`scripts/gen_branded_pdf.py`](../scripts/gen_branded_pdf.py) (usage: `python3 scripts/gen_branded_pdf.py <src.md> <out-base> "<title-html>" "<subtitle>" <repo-rel-dir>`; needs `markdown`, `playwright`, Chromium, `qpdf`). The superseded iteration scripts remain chat-only by design.

## 4. External web sources cited

### In the AI Brain guide (product teardown)
- Kieren Newborn "AI Brain": kierennewborn.com · kierennewborn.com/install · the AI Brain webinar page ($99 webinar / $2,000 install — the product deconstructed)
- Open-source second-brain ecosystem: noahvnct.substack.com second-brain guide · github.com/AgriciDaniel/claude-obsidian · github.com/huytieu/COG-second-brain · github.com/eugeniughelbur/obsidian-second-brain · github.com/coleam00/second-brain-starter
- Course: maven.com/boring-bot/claude-code-in-practice

### In BUILD-SPEC §11/§13 (research & compliance evidence)
- Anthropic — Effective context engineering for AI agents (anthropic.com/engineering)
- dev.to — What Is a Source-of-Truth Document for AI Systems (michael_xero_ai)
- AgentMarketCap — Why 78% of Enterprise AI Agent Pilots Never Scale (2026-04-23)
- DEV Community — I Run a Solo Company with AI Agent Departments (setas)
- n8n — Sustainable Use License docs (docs.n8n.io) — **governs the resale/Embed question**
- HighLevel Support Portal — Pricing & Billing guide
- American Bar Association — Moffatt v. Air Canada chatbot-liability analysis (2024) — **basis of the pricing guardrail**
- Business Insider — the "$1 Chevy Tahoe" prompt-injection incident (2023) — **basis of code-enforced (not prompt) guardrails**
- NAR — Special Report, Nov 17 2025 Board of Directors meeting (rules effective 2026-01-01) — **basis of the real-estate disclosure SOP**
- Prestyj — missed-call text-back conversion benchmark (6–14% recovery, contractors, 2026)

### Anthropic official docs (skills best-practices verification, retrieved 2026-07-25)
- code.claude.com/docs/en/skills.md (structure, frontmatter, progressive disclosure, evals)
- platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (+ /overview)
- code.claude.com/docs/en/agent-sdk/skills.md
- github.com/anthropics/claude-plugins-official — skill-creator plugin

### Regulatory / standards framework (via Governance v4.9 and BUILD-SPEC)
NIST AI RMF · ISO/IEC 42001 · ISO/IEC 42005 · FTC guidance (substantiation, impersonation, review integrity) · FCC TCPA ruling + eCFR exemption structure · CAN-SPAM · GDPR/CCPA · HUD disparate-impact standard (Fair Housing Act) · NAR Code of Ethics amendments (eff. 2026-01-01)

## 5. Platforms, tools & accounts the system depends on

| Layer | Dependencies |
|---|---|
| Production stack | **n8n** (self-hosted, Hostinger VPS — Sustainable Use License) · **GoHighLevel** (system of record; Standard plan; existing client on Starter + separate n8n) · **Postgres + pgvector** · **Langfuse v2** · **Hostinger VPS** (SSH) · OpenAI + Anthropic API keys |
| Founder's cockpit | **Claude** (Pro/Max: Claude Code, desktop app, Routines) · connectors in active use: **Microsoft 365/Outlook** (primary email), Gmail, Google Calendar, Google Drive, **Airtable** (demoted to non-CRM uses, decision #7), **Granola** (transcripts), **Ahrefs** (incl. Brand Radar), **Canva**, Twilio, Higgsfield |
| Client ecosystem | ServiceTitan (primary segment's CRM) + adjacent dispatch/CRM tools · client GHL accounts (isolation rule) |
| Brand assets in Canva | "CenseoAI" design (id DAGc8d3NvWM — logo on white, business card) · "CenseoMarketingLogo2026-01" (id DAG_FV3Yhgw) · Sheren Plumbing & Heating brand kit (client) |

## 6. Organizations & relationships referenced

**20Fathoms** (Traverse City incubator — canvas prepared for; community channel) · **HBANWMI** (trade association — workshop/event channel) · **Kieren Newborn** (competitor product deconstructed) · existing client running the "Communication Smart Response System" (GHL Starter + self-hosted n8n — the client-deployment pattern) · **Sheren Plumbing & Heating** (client; brand kit in Canva) · HVAC wholesalers/distributors + building-supply distributors (dealer-network channel) · SEO/PPC, finance, and ops/ERP complementary vendors (referral partners) · n8n GmbH (future Embed Partner counterparty).

## 7. Open threads at session end (the larger project's starting backlog)

1. **VPS deploy walk-through** — step 1 issued (SSH reconnaissance: `docker --version && docker compose version; docker ps; free -h; df -h /`); awaiting output.
2. **`launching-products` meta-skill** — design agreed (checklist orchestrator + 5 phase reference files + bundled `gen_branded_pdf.py`, built eval-driven with skill-creator); sequenced after the deploy.
3. Items in §2 above (blueprint file, Appendix D → Module A, pricing, threshold, RE language snippets).
4. Build workflow 01 in the n8n editor from its design doc; export JSON back to git.
5. Split `censeo-ai-brain/` to its own private repo when created (decision #5); flip the clients/ gitignore there.
6. Copy vault skills/agents into the founder's actual vault; set the four Routines; run `voice-dna`; move never-send rules into settings permissions (setup guide Parts 5–8).

---

*Founding session: 2026-07-24 → 2026-07-25 · This manifest is itself a governed asset: Reference tier, review within 30 days or on any structural change to the project.*
