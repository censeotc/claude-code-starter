# AI Brain — ready-made agents (the expanded org chart)

Starter agents for the [AI Brain guide](../ai-brain-guide.md) (Step 6). Copy any file into your vault's `.claude/agents/` and edit the specifics. Together with the guide's core 8, this is a full virtual leadership team for a solo operator.

## Business functions

| Agent | Job | Works with |
|---|---|---|
| [revops-engineer](revops-engineer.md) | The delivery engine: leakage audits, RevOS builds, scoreboards | client CRM, automation stack, templates |
| [finance-manager](finance-manager.md) | Cash, receivables, ladder pricing, monthly close | CRM, invoices, memory.md |
| [marketing-director](marketing-director.md) | Own marketing: positioning, outbound support, workshop kits | content skills, bizdev-partner |
| [seo-analyst](seo-analyst.md) | Visibility data: own brand, sales ammunition, vendor checks | Ahrefs/GSC, /client-report, /aeo-snapshot |
| [account-manager](account-manager.md) | Onboarding cadence, weekly reviews, rung conversion, churn flags | CRM, Granola, revops-engineer |
| [project-manager](project-manager.md) | Delivery board, contractor bench, weekly capacity, blockers | projects/, calendar |
| [bizdev-partner](bizdev-partner.md) | Dealer networks, ecosystem, associations, vendor referrals | CRM, /aeo-snapshot, /deal-prep |
| [product-manager](product-manager.md) | The service ladder, template/SOP library, add-on pipeline | feature-prioritizer, memory.md |
| [legal-guardian](legal-guardian.md) | Contract review, templates, compliance watch | vault, risk register |

## Cognitive & critical-thinking functions

These three don't do tasks — they protect the quality of the operator's thinking. They are deliberately allowed to disagree with you.

| Agent | Job | Trigger it with |
|---|---|---|
| [thinking-partner](thinking-partner.md) | Devil's advocate: steelman-then-attack, pre-mortems, bias sweeps | "poke holes in this", "why am I wrong" |
| [decision-coach](decision-coach.md) | Structure big calls, force honest options, keep the decision journal | "help me think through this" |
| [focus-coach](focus-coach.md) | Priorities vs. stated strategy, commitment ledger, weekly score | "what should I focus on", "keep me honest" |

> **Operating manual:** the [AI Agent Orchestration Plan](../ai-brain-orchestration.md) defines the cadences, event-driven playbooks, handoff contracts, and escalation rules that run this roster as one company.

## How they fit together

- **A deal**: bizdev-partner opens the channel → sales-assistant + /deal-prep close it (leakage math as the teaching artifact) → account-manager onboards → revops-engineer delivers the pilot and the scoreboards → account-manager converts pilot → build → retainer → finance-manager bills each rung.
- **A big decision**: decision-coach frames it → thinking-partner attacks it → the decision lands in memory.md → focus-coach holds you to it.
- **Guardrails everywhere**: no agent sends, signs, pays, or publishes anything. They draft and brief; the operator decides.

Conventions follow the guide: trigger-rich `description` fields, no hardcoded `model` (inherit the session's), `tools` omitted so each agent can use whatever's connected — restrict per-agent if you want tighter walls.
