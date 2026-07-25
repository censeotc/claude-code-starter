---
name: meeting-prep
description: Prepare for an upcoming meeting — attendees, history, agenda, and talking points. Use when asked to prep for a meeting, "get me ready for my 2pm", or before any client or prospect call.
---

## What this skill does

Turns "I have a call in 20 minutes" into a half-page you can walk in with.

## Connections used

- **Calendar** — find the event (by time or name). If ambiguous, list today's events and ask which.
- **CRM (GoHighLevel — the system of record) + vault `people/`** — match each external attendee to what we know about them.
- **Meetings (Granola)** — the last transcript with these attendees: what was decided, what we owe them.
- **Email** — any thread with the attendees since that last meeting.

## Output format (half page)

```
# Prep: <meeting title> — <time>

**Attendees:** name — role/company — one line of context each
**Last time:** date + the 2-3 things that matter from it (decisions, our commitments — flag any we haven't done)
**Since then:** anything from email worth knowing walking in

## Likely agenda
2-4 bullets — theirs and ours

## 3 talking points
The three things to say or ask that move this forward
```

## Rules

- If it's a sales call (prospect, not client), add one **tension point**: the question or insight that reframes how they think about their problem. If a `/deal-prep` skill or challenger-sale material exists, borrow its reframe rather than inventing a new one.
- Unfulfilled commitments from the last meeting go first in talking points — showing up having done the thing is the whole game.
- Internal meetings: skip the CRM lookup, keep it to agenda + open items.
- Keep it scannable in 60 seconds. No paragraphs.
