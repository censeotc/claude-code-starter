---
name: client-brief
description: Pull everything known about one client or prospect into a single one-page brief. Use when asked for a client brief, "everything on <name>", account overview, or context before a client call.
---

## What this skill does

Joins every source that knows about one client into one page: CRM record, email history, meeting history, upcoming calendar, and vault notes.

## Connections used (use every one that's connected; note which were unavailable)

- **CRM (GoHighLevel — the system of record)** — search for the client's contact/deal record: status, pipeline stage, deal value, services, last contact, owner. Via the GHL API/MCP connection; if unavailable this session, say so and use the vault note only.
- **Email (Outlook and/or Gmail)** — last 5 relevant threads: who wrote last, what's pending.
- **Meetings (Granola)** — most recent meeting(s) with them: decisions and action items from the transcript.
- **Calendar (Google Calendar / Outlook)** — anything upcoming with them.
- **Vault** — `people/<client>.md` and any `projects/` note that mentions them.

## Output format (one page, max ~400 words)

```
# <Client> — brief (<date>)

**Status:** stage, value, services, owner          ← from CRM
**Relationship health:** 1 line, your judgment, with the evidence

## Where things stand
3-5 bullets: current work, last contact and what it said, open commitments (theirs and ours)

## Open items
- [ ] each unresolved action item, with owner and source (email of <date> / meeting of <date>)

## Next touchpoint
Upcoming meeting or, if none, recommended next action

## Watch out
1-2 lines: risks, unanswered emails, sentiment shifts
```

## Rules

- Every claim traces to a source; write the source inline. No source = don't claim it.
- If the CRM record and the vault note disagree (e.g. different status), show both and flag the conflict — don't silently pick one.
- Offer at the end: "Update `people/<client>.md` and the CRM record with what this brief surfaced?" — only write after a yes.
