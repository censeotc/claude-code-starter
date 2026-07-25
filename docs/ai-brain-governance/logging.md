# The Black Box Recorder — Logging Layer

Everything the AI Brain does leaves a record you can trace, query, and audit. Three log types (matching Governance Template v4.9, Step 3C), one folder, one standing rule.

## The folder

```
logs/
├── 2026-07-25.md        ← one action-log file per day, append-only
├── releases.md          ← every external release (simplified log)
└── events.md            ← 13-field event log (autonomous releases — none until Module A recognition + validated workflows)
incidents.md             ← vault root; see incident-playbook.md
```

`logs/` is append-only: entries are never edited or deleted — corrections are new entries referencing the old one. Git history is the retention mechanism (governance period + 2 years; incidents + 3).

## Log type 1 — the action log (everything, every day)

Every agent/skill action appends one line to `logs/YYYY-MM-DD.md`:

```
| time (UTC) | actor | action | tier | data touched | outcome | ref |
| 14:22 | email-manager | drafted reply re: invoice | Ext-Routine (manual) | Outlook thread, CRM-8847 | approved+sent | REL-2026-07-25-03 |
| 14:31 | finance-manager | priced Sheren renewal | Int-High-Impact | CRM, memory.md precedents | presented, pending | — |
| 15:05 | revops-engineer | built scoreboard wk4 | Ext-High-Stakes | ServiceTitan export | approved w/ 1 edit | projects/sheren/scoreboards/2026-07-25.md |
```

- **outcome** ∈ drafted / presented / approved / approved-with-edits / rejected / filed / escalated.
- Rejections are as important as approvals — they're the correction signal `/audit-trail` looks for.

## Log type 2 — the release log (anything that left the building)

Per governance, every **manual-routine external release** (you reviewed and approved the send) appends to `logs/releases.md`:

```
| release ID | output | sender | recipient | channel | timestamp (UTC) | disclosure | tier-compliance confirmed |
| REL-2026-07-25-03 | invoice-reminder reply | Scott | CRM-8847 | email | 2026-07-25T14:29Z | metadata: AI-Assisted | yes — no quantified/contractual content |
```

**External High-Stakes** releases add two fields: `verified-by` (you, individually, against source data) and `approval` (your written OK — the chat approval counts; the log line records it).

## Log type 3 — the event log (autonomous releases only)

The full 13-field record (event ID, workflow ID, validation ID, model/version, prompt version, channel, timestamp, recipient ID, consent status, DNC status, monitor status, policy-check result, escalation result). **Currently unused by design** — no autonomous external sends until Module A is recognized and a workflow is validated. The file exists so the day one is validated, the log is already the recognition artifact.

## The standing rules — paste into your vault's CLAUDE.md

```
## Governance & logging (non-negotiable)
- Read context/governance.md at session start. Every output states its
  reliance tier. Contractual/warranty/guarantee/refund content: no-release
  rule — do not send under any circumstances.
- Log every agent/skill action as one line in logs/YYYY-MM-DD.md
  (time, actor, action, tier, data touched, outcome, ref). Create the
  file if it's the day's first action.
- Every approved external send also gets a logs/releases.md entry before
  the send is executed. No entry, no send.
- Never edit or delete existing log lines. Corrections are new lines.
- If anything matching the incident definitions in incidents.md occurs,
  stop and follow the incident playbook before continuing.
```

## Daily checkpoint (so nothing is ever more than a day untraceable)

Add a fourth scheduled Routine:

```
Every day at 6:00pm: commit everything in this vault to git with the
message "daily checkpoint <date>", including logs/. Do not push anywhere
unless I've configured a private remote. Then verify today's action log
exists and flag any hour-gaps where actions happened but nothing was logged.
```

## Querying it all

That's the [`/audit-trail`](../ai-brain-skills/audit-trail/SKILL.md) skill: trace by client, agent, day, or tier; completeness checks; and the monthly spot-check the governance template requires.
