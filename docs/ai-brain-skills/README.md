# AI Brain — ready-made skills

Starter skills for the [AI Brain guide](../ai-brain-guide.md) (Step 5). Copy any folder into your vault's `.claude/skills/` and edit the specifics — your CRM, your inbox, your folder names.

| Skill | Job | Connections it uses |
|---|---|---|
| [inbox-triage](inbox-triage/SKILL.md) | Sweep every inbox, sort, queue drafts | Email (Outlook/Gmail) |
| [client-brief](client-brief/SKILL.md) | Everything about one client, one page | CRM, email, meetings, calendar |
| [meeting-prep](meeting-prep/SKILL.md) | Walk into any meeting ready | Calendar, CRM, meetings, email |
| [follow-up](follow-up/SKILL.md) | Find stale relationships, draft the revival | CRM, email |
| [braindump](braindump/SKILL.md) | Capture raw thoughts, file everything | Vault only |
| [sop-writer](sop-writer/SKILL.md) | Document a process so it's delegable | Vault only |
| [audit-trail](audit-trail/SKILL.md) | Trace/audit everything the Brain did; monthly spot-check | logs/, incidents.md, git |
| [revenue-scoreboard](revenue-scoreboard/SKILL.md) | Weekly client scoreboard — the core delivery artifact | client CRM data, projects/ |
| [client-report](client-report/SKILL.md) | Monthly visibility report (SEO/AEO engagements) | Ahrefs/GSC, Canva |
| [aeo-snapshot](aeo-snapshot/SKILL.md) | AI-answer visibility vs competitors | Ahrefs Brand Radar |
| [deal-prep](deal-prep/SKILL.md) | Challenger-style sales call prep | CRM, email, research, Ahrefs |

Every skill states its connections and degrades gracefully when one isn't available. None of them ever sends anything without approval.

The last three are examples of the [upgrade-path principle](../ai-brain-guide.md#upgrade-paths-if-you-already-run-a-business-stack): skills built on the data tools you already pay for are the ones generic products can't ship.
