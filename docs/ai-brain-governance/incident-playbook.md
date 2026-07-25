# Incident Playbook — When Something Goes Wrong

Matches Governance Template v4.9, Step 3H. The point is not blame — it's containment, correction, and making sure the same failure can't repeat (every incident ends with a file diff).

## What counts as an incident

1. False, misleading, or unsubstantiated AI claim **reaches a client or prospect**
2. Confidential or proprietary information disclosed by an AI output
3. Governance bypass — an unrecognized/unlogged output used for downstream reliance
4. Client or prospect complains about AI-generated content
5. Persistent drift — 3+ quality flags on the same skill/agent within 30 days
6. Model-provider breach, policy change, or outage affecting governed workflows
7. (Module B era only) a voice agent fails to identify as AI

## Severity and response clock

| Severity | Examples | Contain | Notify |
|---|---|---|---|
| **High** | False claim reached a client; privacy breach; impersonation | Pause the workflow immediately, business hours or not | Operator interrupted immediately (push/phone) |
| **Medium** | Client complaint; persistent drift; governance bypass; provider disruption | Pause within 1 business hour | Operator within 4 business hours |
| **Low** | Isolated drift flag; tone/format miss in a spot-check; minor log exception | No pause; flag it | Log it; review at monthly audit |

## The six response steps (every incident, in order)

1. **Contain** — pause per the table. For a sent communication: stop any related queued sends.
2. **Assess** — severity, scope, who received what.
3. **Remediate** — correct the output; fix the workflow.
4. **Communicate** — if a client/prospect received inaccurate information, a correction goes out (drafted by the Brain, approved by you). Honesty beats optics; same rule as the scoreboard.
5. **Document** — full entry in `incidents.md` (template below).
6. **Review** — did this trip a revalidation trigger? Does a standing control need to change?

## incidents.md entry template

```
## INC-2026-07-25-01 · severity: Medium · status: open/contained/closed
- What happened:      (one paragraph, plain facts)
- Output tier:        (what tier was it operating at — and should it have been?)
- How detected:       (spot-check / client flagged / audit-trail / self-caught)
- Who received it:    (or "internal only")
- Containment:        (what was paused, when)
- Root cause:         (thin context file / bad prompt / missing rule / wrong tier / data error)
- Remediation:        (the correction issued)
- CORRECTION DIFF:    (the file(s) changed so it can't recur — path + what changed;
                       "none" is only acceptable for pure data errors, with why)
- Revalidation:       (triggered? which workflow?)
- Links:              (action-log lines, release IDs, client)
```

## The correction loop — the part that makes the system self-improving

An incident is not closed until something in the vault changed:

- Wrong facts → the context file that should have known gets updated
- Wrong behavior → the SKILL.md or agent .md gets a new rule, and (per guide Step 7) gets re-evaled against the failure case
- Wrong tier → the auto-classification note in governance.md gets the missing pattern
- Repeated near-misses on one skill (3 in 30 days) → full revalidation: re-run its eval suite before it's trusted again

`/audit-trail`'s monthly spot-check reports incidents with empty CORRECTION DIFF fields — those are open loops, and open loops are how the same failure happens twice.
