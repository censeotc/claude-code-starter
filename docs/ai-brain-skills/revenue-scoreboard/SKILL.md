---
name: revenue-scoreboard
description: Build the weekly client revenue scoreboard — booked revenue recovered, estimates revived, response times, pipeline created — from CRM exports or connected data. Use when asked for a scoreboard, weekly numbers, pilot results, "how is <client's> pilot doing", or to prep the weekly cadence call.
---

## What this skill does

Produces the deliverable at the heart of every CenseoAI engagement: the weekly
scoreboard that proves the Revenue Operating System is finding money. This is
what the 45-day pilot sells on, what the weekly cadence call runs on, and what
the rung-conversion conversation (pilot → build → retainer) is argued from.

## Inputs (use whatever exists; name what's missing)

- **CRM data** — export or connected source from the client's system
  (ServiceTitan or equivalent): estimates with statuses and dates, jobs
  booked, customer list activity, response/follow-up timestamps.
- **Baseline** — the leakage audit numbers from `projects/<client>/` (what
  was dying in the system before the pilot). Every scoreboard compares
  against this; without a baseline, week one's job is to establish it and
  say so on the sheet.
- **Last week's scoreboard** — `projects/<client>/scoreboards/` for trend.
- **The promise** — the measurable outcomes stated in the pilot kickoff;
  the scoreboard tracks exactly those, not vanity stats.

## The scoreboard (one page, numbers first)

```
# <Client> — Revenue Scoreboard, week of <date>    (week N of 45-day pilot)

## The headline
$<recovered this week> booked from revived opportunities · $<running total>
since start — vs. $<baseline leakage> identified in the audit.

## The numbers                       this wk | last wk | trend | target
Estimates revived (count / $)
Jobs booked from follow-up ($)
Avg time-to-first-response
Reactivation responses (count / $)
Replacement pipeline created ($)
Cadence adoption (touches done/due)

## What worked            ← 2-3 lines, specific: which cadence, which list
## What needs attention   ← slipping metric or adoption gap + the fix
## This week's focus      ← the one move for the coming week
```

## Steps

1. Identify client and week; load baseline, promise, and prior scoreboards.
2. Compute each metric from the data. **Attribution is conservative**: a
   dollar counts as "recovered" only when the booked job traces to a system
   action (a follow-up cadence touch, a reactivation message, a revived
   estimate) — walk-in luck doesn't go on the board.
3. Check adoption before celebrating outcomes: if touches-done/due is under
   80%, adoption IS the headline — the system can't prove itself unused.
4. Write the one-pager. Save to `projects/<client>/scoreboards/<date>.md`.
5. On request, produce the client-facing version (branded PDF or deck via
   the pptx/slides tools, logo assets in docs/assets/) and 3 talking points
   for the weekly call.

## Rules

- Every dollar traces to CRM records the client can open themselves; note
  the record IDs or filter used. One inflated number destroys the pilot.
- Never smooth a bad week. Flat or down gets said plainly, with the
  diagnosis and the fix in the same breath — account-manager's rule applies:
  CenseoAI's narrative reaches the client before the soft number does.
- Milestone weeks get one extra line: day 30 (evidence file for the next
  rung — hand to account-manager) and day 45 (pilot verdict vs. the
  promise, in the client's own numbers).
- Keep it to one page. The client is an owner between service calls, not
  an analyst.
