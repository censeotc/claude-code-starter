---
name: agent-best-practices
description: Anthropic's distilled checklist for designing Claude Code sub-agents — frontmatter field reference, least-privilege tool combos, model routing, description-writing rules, and the system prompt template. Use when creating, reviewing, or improving a sub-agent, or deciding whether a task should be a sub-agent, a skill, or the main conversation.
---

Reference checklist distilled from Anthropic's official sub-agent docs. This is a lookup table, not a workflow — the `agent-architect` agent applies it.

## Frontmatter fields

| Field | Required | Notes |
|-------|----------|-------|
| `name` | Yes | lowercase-hyphenated, unique across project + user agents |
| `description` | Yes | What it does + delegation triggers — this is the routing signal |
| `tools` | No | Omitting inherits ALL tools. Always set it — least privilege |
| `model` | No | Full model ID; omit (or `inherit`) to match the main conversation |
| `memory` | No | Directory for notes that persist across runs |
| `skills` | No | Skill names preloaded at agent startup (newer Claude Code versions) |
| `maxTurns` | No | Turn cap — cost control for runaway loops |
| `permissionMode` | No | Leave unset. Never `bypassPermissions` |

## Least-privilege tool combos (official patterns)

| Agent type | Tools |
|------------|-------|
| Reviewer / auditor (read-only) | Read, Grep, Glob |
| Test runner / debugger | Bash, Read, Grep |
| Code modifier | Read, Edit, Write, Grep, Glob |
| Researcher | WebSearch, WebFetch, Read |

Never grant the full set. Add Bash only if commands must run; Write/Edit only if files must change.

## Model routing

| Model | Use for |
|-------|---------|
| `claude-haiku-4-5-20251001` | Cheap, high-volume, formulaic output (copy, formatting) |
| `claude-sonnet-4-6` | Default — balanced review, analysis, code work |
| `claude-opus-4-6` | Judgment-heavy — research synthesis, architecture, design |
| omit / `inherit` | Agent should match whatever the user is running |

## Description rules (this is what triggers delegation)

- What it does, then triggers: "… Use when asked to <verb phrases users actually say>."
- Add "Use proactively" only if it should fire without being named.
- Specific beats clever — list real trigger words, not categories.
- One job per agent. A vague description causes wrong delegations.

## System prompt template

1. Role — one sentence: "You are a <specialist>."
2. Procedure — "When invoked:" + numbered steps
3. Domain checklist — the concrete things to check or do
4. Output contract — "Return this exact format:" + template
5. Boundaries — what it must never do; closing terseness rule

## When NOT to build a sub-agent

- Reusable instructions/checklist, no context isolation needed → make it a **skill**
- Needs mid-task conversation with the user → keep it in the **main conversation** (sub-agents run autonomously and return once)
- One-off task → just do the task
- Job already covered by an existing agent → improve that agent instead

## Non-negotiables

- Project agents live in `.claude/agents/` and are version-controlled
- Never `bypassPermissions`; never every tool "just in case"
- Always show the drafted file for review before writing it
