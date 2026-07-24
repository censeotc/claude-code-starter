---
name: sop-writer
description: Turn "how I do X" into a step-by-step standard operating procedure anyone could follow. Use when asked to document a process, write an SOP, create a runbook or checklist, or "write down how I do this".
---

## What this skill does

Interviews the operator about a process they run from memory, then writes the SOP that makes it delegable — to a human or to a future skill.

## Steps

1. Ask for a walkthrough of the process as they actually do it (not the idealized version). Then probe the gaps interviewers miss:
   - What do you check before starting? What tells you it worked?
   - Where does it usually go wrong, and what do you do then?
   - What decisions require judgment vs. rules? For judgment calls: what are you actually weighing?
   - What tools/logins/files does each step touch?
2. Write the SOP to `sops/<process-name>.md` (create the folder if needed):

```
# SOP: <Process name>
**Owner:** · **Frequency:** · **Time:** · **Last verified:** <date>

## When to run this
Trigger conditions, in one or two lines.

## Before you start
Prerequisites, access needed, inputs in hand.

## Steps
1. Numbered, one action each, with the "done when" for any step whose completion isn't obvious.
   ⚠ Failure notes inline where things go wrong.

## Decision points
For each judgment call: the question, the factors, and worked examples of each branch.

## Done when
The observable end state. What to check, who to tell.
```

3. Read it back and ask: "Could someone who's never done this follow it? What did I miss?" Revise once.

## Rules

- One action per step. "Update the record and notify the client" is two steps.
- End by asking whether any part of this SOP should become a skill of its own — an SOP whose steps are mostly reading and writing files or calling connected tools is a `SKILL.md` waiting to happen. Offer to draft it.
