---
name: aeo-snapshot
description: Snapshot a brand's visibility in AI answers (ChatGPT, Perplexity, AI Overviews) — mentions, citations, share of voice vs competitors. Use when asked how visible a brand is in AI, for an AEO/GEO audit, "does AI recommend them", or a prospect-facing AI visibility teaser.
---

## What this skill does

Answers "when someone asks an AI who to hire, do they hear about you?" — for a client (tracking) or a prospect (the sales artifact that starts the conversation).

## Connections used

- **Ahrefs Brand Radar**: mentions overview/history, citations (which pages AI cites), cited domains, share of voice vs. named competitors. Check existing Brand Radar reports first; note when a new prompt set needs configuring.
- **Fallback** without Brand Radar access for the domain: ask the flagship questions directly in available AI surfaces via web research and record who gets named — smaller sample, still a legitimate snapshot; label it as spot-check data.

## Steps

1. Confirm: brand + domain, 2-3 competitors, and the 3-5 questions their customers actually ask AI ("best HVAC company in <city>", "who does <service> near me").
2. Pull mentions, citations, and share of voice for brand and competitors; get the trend, not just the point-in-time number.
3. Produce the snapshot:

```
# AI Visibility Snapshot — <Brand>, <date>

**The one number:** share of voice in AI answers vs. <top competitor> (or:
"AI currently recommends <competitor> — not you — when asked <question>")

## Where you appear      ← mentions by question/topic, trend arrow
## Who AI cites          ← the sources driving answers; whether the brand
                            controls, could influence, or is absent from them
## Competitor gap        ← SOV table, brand vs each competitor
## Why (2-3 bullets)     ← what the cited sources have that the brand lacks
## What would move it    ← 3 concrete actions, each tied to a cited source
                            or gap above
```

## Rules

- **For a prospect**, the snapshot is a Challenger teaching artifact: lead with the finding that stings ("AI recommends your competitor by name"), keep it to one page, end with the reframe — this is a new visibility channel their current marketing doesn't cover. Feed it to /deal-prep.
- **For a client**, it's a trend line: compare to the last snapshot in `projects/<client>/`, celebrate movement, flag slippage.
- Never fabricate an AI answer. Every quoted response comes from Brand Radar data or an actual query run during this session, labeled with its source.
