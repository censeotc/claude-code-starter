---
name: braindump
description: Take raw unstructured thoughts and file every piece into the right place in the vault. Use when the user pastes a braindump, voice-note transcript, stream of consciousness, or says "get this out of my head".
---

## What this skill does

The capture valve. The operator dumps everything; nothing gets lost, everything lands where the other skills will find it.

## Steps

1. Read the whole dump first. Split it into atomic pieces (one idea, task, decision, or fact each).
2. Classify each piece:

| Piece is a… | Goes to |
|---|---|
| Decision made | `memory.md` → Decisions table |
| Commitment / task | `memory.md` → Active commitments |
| Fact about a client or person | `people/<name>.md` (and flag for the CRM if one is connected) |
| Project idea or update | `projects/<project>.md` — create the note if new |
| Content idea | `inbox/content-ideas.md` |
| Reference / link / learning | `inbox/` with a descriptive filename |
| Unclassifiable | `inbox/braindump-<date>.md` — never dropped |

3. Show the filing plan as a table (piece → destination → exact line to be written) **before writing anything**.
4. On approval, write all files in one pass and confirm what went where.

## Rules

- Preserve the operator's wording for decisions and commitments — file, don't paraphrase meaning away.
- Anything ambiguous gets ONE clarifying question max; if still unclear, it goes to `inbox/` rather than blocking the dump.
- If a piece contradicts something already in `memory.md` (e.g. reverses an earlier decision), file it AND flag the contradiction out loud.
- Speed matters more than polish — this skill should feel instant, or the operator stops capturing.
