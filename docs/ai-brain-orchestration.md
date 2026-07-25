# CenseoAI — AI Agent Orchestration Plan

The [agents](ai-brain-agents/) are the roles; this is the operating system that runs them together. It defines who acts when, who hands off to whom, what reaches the operator, and what runs on a schedule — so the virtual org works as one company instead of nineteen specialists waiting to be called.

**The operator's job in this system:** decisions, relationships, and delivery judgment. Everything else is delegated, drafted, or scheduled.

---

## 1. The org chart

```
                        OPERATOR (Scott)
                 decisions · relationships · judgment
                              │
   ┌──────────────────────────┼──────────────────────────┐
   │ COGNITIVE BOARD          │ CHIEF OF STAFF            │
   │ thinking-partner         │ chief-of-staff (core 8)   │
   │ decision-coach           │ + focus-coach             │
   │ (advise, challenge —     │ (triage, priorities,      │
   │  never execute)          │  keeps the plan honest)   │
   └──────────────────────────┴──────────────────────────┘
                              │
   ┌──────────────┬───────────┴──────────┬───────────────┐
   │ GROWTH       │ DELIVERY             │ BACK OFFICE   │
   │ marketing-   │ revops-engineer      │ finance-      │
   │  director    │ project-manager      │  manager      │
   │ bizdev-      │ account-manager      │ legal-        │
   │  partner     │ seo-analyst          │  guardian     │
   │ sales-       │ ops-manager (core 8) │ strategist    │
   │  assistant   │ product-manager      │  (core 8)     │
   │ researcher   │ contractor bench     │               │
   └──────────────┴──────────────────────┴───────────────┘
```

Core-8 agents from the [guide](ai-brain-guide.md) (chief-of-staff, email-manager, researcher, content-writer, sales-assistant, ops-manager, strategist) slot in as shown; copywriter merges into content-writer.

---

## 2. Operating cadences

### Daily (≈20 operator-minutes)
| When | What runs | Who | Operator's part |
|---|---|---|---|
| 7:00 (Routine) | `/daily-brief` — calendar, inbox scan, top-3 vs. strategy | chief-of-staff | Read it |
| 7:20 | `/inbox-triage` — both inboxes, drafts queued | email-manager | Approve/edit drafts |
| Before each meeting | `/meeting-prep` | chief-of-staff | Skim the half-page |
| After each meeting | `/meeting-debrief` from the transcript → CRM, projects/, memory.md | account-manager routes outcomes | None — it files itself |
| Anytime | `/braindump` | filed to the right owner agents | Empty your head |

### Weekly
| When | What runs | Who | Output |
|---|---|---|---|
| Mon 8:00 (Routine) | `/follow-up` sweep + capacity check | email-manager + project-manager | Overdue list w/ drafts; overcommit flagged **before** the week starts |
| Per client, fixed day | data pull → `/revenue-scoreboard` → cadence-call prep | revops-engineer → account-manager | One page + 3 talking points, day before the call |
| Fri 16:00 (Routine) | `/weekly-review` + focus-coach score | strategist + focus-coach | Planned vs. done, hours vs. strategy, one adjustment |

### Monthly
- **Close narrative** — finance-manager: ladder revenue, margins, retainer base, one action.
- **Lead flow** — marketing-director: leads by source, cost, channel verdict.
- **Client health** — account-manager: green/yellow/red across the book, save plays for yellows.
- **Roadmap review** — product-manager: template ratio, ladder deviations, add-on pipeline.

### Quarterly
- Build/kill calls (product-manager) · positioning review (marketing-director) · risk register (legal-guardian) · CenseoAI's own `/aeo-snapshot` (seo-analyst) · strategy.md refresh (strategist + decision-coach, journaled).

---

## 3. Event-driven playbooks

Each playbook is one prompt to start; agents chain and hand back at the decision point.

**New lead appears** (referral, workshop, form)
researcher profiles them → seo-analyst/revops math for the teaching artifact → `/deal-prep` builds the Challenger package → sales-assistant drafts the outreach. *Operator decides: send.*

**Deal closes**
account-manager kickoff package → revops-engineer data-readiness check (honest, before promises) → project-manager slots it against capacity → finance-manager invoices. *Operator decides: kickoff date; approve invoice.*

**Scoreboard comes in soft**
revops-engineer diagnoses (adoption vs. system vs. season) → account-manager preps the honest narrative + fix for the same message → if it's the second soft week, thinking-partner asks whether the pilot design is wrong. *Operator decides: the call.*

**Contract or SOW arrives**
legal-guardian structured read → top-3 negotiate list → finance-manager sanity-checks the economics. *Operator decides: sign/negotiate.*

**A distributor or association shows interest**
bizdev-partner program one-pager → finance-manager rollout economics → marketing-director workshop kit. *Operator decides: the pitch meeting.*

**New idea strikes** (the important one)
focus-coach shiny-object filter (what does it displace?) → survives a week → decision-coach frames and classifies it → thinking-partner pre-mortem if irreversible → decision + reasoning journaled to memory.md. *Operator decides: with the whole record in front of him.*

**Client goes quiet / questions value**
account-manager yellow flag + save play → revops-engineer pulls the value evidence → sales-assistant drafts the re-anchor message. *Operator decides: call or email.*

---

## 4. Handoff contracts

A handoff is only complete when it carries:
1. **Source-traced facts** — every number names its origin (CRM record, transcript, bank feed). No source, no claim.
2. **State updates done** — CRM, `projects/<client>.md`, `people/` notes current *before* handing off, not after.
3. **A decision-ready summary** — the receiving agent (or operator) gets the "so what" in ≤5 lines, details beneath.
4. **memory.md entries** for anything that changed a commitment, price, or plan.

Chains break silently without this — enforce it in every agent's output.

---

## 5. Escalation rules — what reaches the operator, when

| Immediately (interrupt) | Daily brief (batched) | Weekly review (batched) |
|---|---|---|
| Client threatening to leave | Emails needing replies | Commitment-ledger gaps |
| Money: payment failed, invoice disputed | Yellow health flags | Channel/lead-flow trends |
| Legal: anything with a signature deadline | Schedule conflicts | Template-ratio, margin drift |
| A scoreboard the client will see today that's wrong | New leads captured | Ideas that survived the week filter |

Everything else waits. The system's promise is *fewer* interruptions, not more.

---

## 6. Hard guarantees (unchanged, everywhere)

- No agent sends, signs, pays, publishes, or deletes. Draft → present → operator approves. Enforced in `settings.json` permissions, not just prompts.
- **Everything is tiered and logged.** Every output carries its reliance tier (Governance Template v4.9), every action lands in the append-only action log, every external release gets a release-log entry *before* it goes out, and incidents follow the [playbook](ai-brain-governance/incident-playbook.md) — full spec in [ai-brain-governance/](ai-brain-governance/), queryable via `/audit-trail`.
- The **no-release rule**: contractual, warranty, guarantee, or refund language never leaves the building without legal review — regardless of who approved what.
- Cognitive agents advise and challenge; they never execute.
- A scheduled Routine may *prepare* anything but *send* nothing.
- When agents disagree (e.g., focus-coach says no, bizdev says yes), both positions go to the operator side by side — no agent overrules another.

---

## 7. Rollout order

1. **Week 1 — the daily loop**: morning Routine, `/inbox-triage`, `/meeting-prep`/`debrief`. Habit first.
2. **Week 2 — the delivery spine**: revops-engineer + `/revenue-scoreboard` + account-manager cadence on one real client.
3. **Week 3 — the weekly layer**: Monday follow-up Routine, Friday review Routine, focus-coach ledger.
4. **Week 4 — growth + back office**: `/deal-prep` on a live prospect, finance close, first monthly health pass.
5. **Ongoing** — add one playbook at a time as its trigger occurs; eval each vs. its real output (guide Step 7) before trusting it blind.

*Companion to the [AI Brain guide](ai-brain-guide.md) · agents in [ai-brain-agents/](ai-brain-agents/) · skills in [ai-brain-skills/](ai-brain-skills/)*
