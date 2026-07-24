---
name: client-report
description: Build a monthly client performance report from live SEO/AEO data — rankings, search traffic, AI visibility — as a branded deck or document. Use when asked for a client report, monthly report, performance report, or "how is <client's site> doing".
---

## What this skill does

Turns connected data into the deliverable clients pay for: a report that shows movement, explains it, and sets up next month's work.

## Connections used

- **Ahrefs** (primary data source): Rank Tracker (positions and movement), Site Explorer (organic keywords, traffic, referring domains, Domain Rating trend), GSC tools if the client's Search Console is linked (impressions, clicks, CTR), Brand Radar (AI visibility — mentions, citations, share of voice in AI answers), Web Analytics if installed.
- **Fallback** if Ahrefs isn't connected: Search Console alone, or web research for visible rankings — and say clearly which data the report is missing.
- **Output**: draft in markdown → on approval, produce the client-facing version (slide deck or PDF; if Canva is connected, populate the branded report template).

## Steps

1. Confirm: client domain, reporting period (default: last full month vs. the month before), and the 3-5 keywords/topics the engagement promised movement on.
2. Pull the data. Every number gets period-over-period comparison — a number without a delta is noise.
3. Write the report:

```
# <Client> — Performance report, <month>

## Headline (3 bullets, plain English)
What moved, why, what's next. Written for the owner, not an SEO.

## Search visibility        ← rankings table: keyword, position, change
## Traffic & engagement     ← organic traffic, top pages, trend chart
## AI visibility            ← Brand Radar: mentions, citations, share of voice
   vs. named competitors — this is the differentiator section; lead with it
   when the movement is good
## What we did this month   ← from projects/<client>.md and the vault
## Next month               ← 3 priorities, each tied to a number above
```

4. Sanity-check before presenting: does every claim in the headline trace to a number in the body? Is any metric down that the report doesn't address? A report that hides a decline costs the relationship more than the decline does.

## Rules

- Plain English throughout — the reader is a business owner. "More people found you when asking ChatGPT about <service>" beats "AI SOV +12%".
- Charts for trends, tables for rankings; every chart labeled with the period.
- Save the markdown source to `projects/<client>/reports/<YYYY-MM>.md` so next month's report can reference it.
