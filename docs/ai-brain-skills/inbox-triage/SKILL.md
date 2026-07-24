---
name: inbox-triage
description: Sweep every connected inbox, sort messages into act-now / needs-reply / read-later / ignore, and queue reply drafts for approval. Use when asked to triage the inbox, check email, process mail, or catch up on messages.
---

## What this skill does

Processes the inbox(es) end to end: reads, categorizes, drafts — but **never sends**.

## Connections used

- **Email** — Microsoft 365 (Outlook) and/or Gmail MCP tools. Sweep EVERY connected inbox, not just one. If neither is connected, say so and stop; do not invent messages.
- **Voice** — `context/brand.md` for draft tone.
- **Context** — `context/icp.md` and `people/` (or the CRM) to recognize who matters.

## Steps

1. Search each connected inbox for unread and recent (last 48h) messages. Skip newsletters, receipts, and automated notifications unless they need action.
2. Sort every remaining message into exactly one bucket:
   - **Act now** — deadline, client escalation, money, or a direct question from a client/prospect
   - **Needs a reply** — expects a response but not urgent
   - **Read later** — informational, worth reading, no response needed
   - **Ignore** — everything else (say how many, don't list them)
3. For each *Act now* and *Needs a reply* message, draft the reply in the operator's voice (study `context/brand.md` first). Under 150 words unless the thread demands more.
4. Present the output in this order: Act now (with drafts) → Needs a reply (with drafts) → Read later (one line each) → Ignore count.
5. Only after explicit approval of a specific draft, place it in the email system's **drafts folder** (e.g. Gmail `create_draft`). Never send directly, even if asked to "just send it" mid-triage — confirm once more first.

## Rules

- A message that appears in two inboxes counts once.
- If a message mentions a known client or open deal, flag it with the client name so /client-brief context is one step away.
- End with one line: anything in the sweep that should be logged to `memory.md` (a decision, a commitment, a date promised).
