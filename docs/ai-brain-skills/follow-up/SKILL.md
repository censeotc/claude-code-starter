---
name: follow-up
description: Scan clients, prospects, and sent mail for overdue follow-ups and draft the openers. Use when asked who needs a follow-up, who's gone quiet, what's overdue, or for the weekly follow-up sweep.
---

## What this skill does

Finds every relationship going stale and hands you the first line of the message that revives it.

## Connections used

- **CRM (Airtable)** — records where last-contact is older than the threshold for their stage (active client: 14 days; open deal: 5 days; warm prospect: 30 days — adjust to taste).
- **Email (Outlook and/or Gmail)** — sent mail where WE wrote last, got no reply, and 4+ days have passed.
- **Vault** — `memory.md` active commitments and `people/` notes with promised next steps.

## Steps

1. Build the overdue list from all three sources; merge duplicates (same person from CRM and email = one entry).
2. Rank by consequence of silence: open deals first, then active clients, then prospects.
3. For the top entries, draft a 2-3 sentence follow-up opener in the operator's voice (`context/brand.md`). Not "just checking in" — each opener must carry something: a next step, a useful link, a specific question, or a deadline.

## Output format

```
# Follow-up sweep — <date>

## Overdue (<n>)
1. **<Name / company>** — <stage> — last contact <date>, <who wrote last>
   Why now: <one line>
   Draft: "<the opener>"
...

## Going quiet (watch list)
Names approaching threshold — no drafts, just awareness.
```

## Rules

- Never send anything; drafts are queued for approval like /inbox-triage.
- If someone was followed up within the last sweep and still hasn't replied, escalate the suggestion (call instead of email, or a break-up message) rather than repeating the same nudge.
- End by offering to update last-contact dates in the CRM for any follow-ups the operator approves and sends.
