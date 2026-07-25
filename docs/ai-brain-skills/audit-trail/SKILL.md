---
name: audit-trail
description: Trace and audit everything the AI Brain did — query the action, release, and incident logs by client, agent, date, or tier; check log completeness; run the monthly governance spot-check. Use when asked what the AI did, to trace or audit an output, show the log, verify a release, or run the spot-check.
---

## What this skill does

Answers "what did the AI Brain do, and can I prove it?" from records instead of recollection. Reads `logs/*.md`, `incidents.md`, `memory.md`, and git history; writes nothing except reports.

## Query modes

**1. Trace** — `"trace everything that touched <client> this week"` / `"what did email-manager do yesterday"` / `"where did this number in the scoreboard come from"`
→ Chronological table from the action log, joined with release IDs, incident links, memory.md decisions, and git commits. Every row keeps its `ref` so you can open the underlying artifact.

**2. Verify a release** — `"verify REL-2026-07-25-03"`
→ The release-log entry, its action-log line, the draft's tier, the disclosure label used, who approved it and when. Flag any missing field.

**3. Completeness check** — `"check the logs for gaps"`
→ Days with vault activity (git commits, new files) but no action log; releases without matching action-log lines; sends found in email Sent folders without release-log entries (the serious one — that's a governance bypass, i.e., an incident); external High-Stakes entries missing `verified-by` or `approval`.

**4. Monthly spot-check** (the v4.9 requirement) — `"run the monthly spot-check"`
→ Sample up to 10 external releases from the month (all of them if fewer — below min-N, report as insufficient data and review qualitatively). For each: tier assigned correctly? prohibited content absent (quantified ROI/contractual language in Routine releases)? disclosure label per taxonomy? log entry complete? Then: incidents with empty CORRECTION DIFF (open loops), drift patterns (same skill flagged repeatedly), and rejection-rate by agent (a rising rejection rate = that agent's file needs editing). Output: a one-page report saved to `logs/spot-checks/YYYY-MM.md`, findings ranked by severity.

## Rules

- Report from records only. If the logs can't answer the question, say exactly what's missing — never reconstruct from plausibility. A gap IS the finding.
- Never alter a log while auditing. Corrections you recommend become new entries or incident records.
- Any governance bypass discovered (an external send with no release log) is reported as an incident candidate with a pre-filled `incidents.md` entry, severity Medium.
- End every report with the two numbers that matter: % of actions logged, and open correction loops. Green is 100% and zero.
