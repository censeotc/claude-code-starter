# SOP: New Client AI Brain Onboarding

**Tier: Critical** · v1 · 2026-07-25 · The productization runbook — client #2 onward is "copy the template, fill the config, run the tests."

**Deliverable definition:** a client "AI Brain" = the productized workflow modules (starting with missed-call text-back) running on THE CLIENT'S OWN accounts, configured from `clients/<client>/config.yml`, launched HITL-first. It is not a copy of CenseoAI's internal vault.

---

## Gate 0 — Commercial gates (before any technical work)

- [ ] **Licensing lane confirmed.** This deal is service/configuration on the client's own n8n + GHL accounts (permitted under n8n Sustainable Use). It is NOT white-labeled resale of n8n as our product — that lane stays closed until an Embed Partner agreement exists (decision-log open item).
- [ ] **Account topology.** Client has (or we create for them, in their name) their own GHL account. Revisit Agency-tier sub-accounts only at 2+ paying workflow clients.
- [ ] **Signed agreement** from the current service-agreement template. Contract language = no-release rule: legal review before signature, both directions.
- [ ] **TCPA basis documented**: whose customers get texted, engagement basis (inbound call, form submission), opt-out mechanics. Written into config, not assumed.

## Gate 1 — Isolation (the non-negotiable architecture rule)

- [ ] Their own n8n instance or workspace. Never shared with CenseoAI internal or any other client.
- [ ] Their own credential set in that n8n, scoped least-privilege (their GHL location key; LLM keys per the deal — theirs, or ours with per-client cost tags).
- [ ] Their own `.env` on their instance. Nothing client-specific in CenseoAI's internal stack.
- [ ] Their own Langfuse project + `audit_log` rows tagged `client_code`.
- [ ] What IS shared: the templates in this repo (SOPs, prompts, workflow designs). Never data, credentials, or running workflows.

## Gate 2 — Configuration (the actual setup)

- [ ] `cp -r clients/_template clients/<client-code>` and fill **every** field in `config.yml`. NEEDS-INPUT left in a Critical field = not launchable.
- [ ] **Pricing table populated from their real price book** (their GHL custom fields or their Postgres `pricing` rows). Empty pricing = agent says "our team will confirm" — correct behavior, never a reason to let the model improvise.
- [ ] Safety-keyword list adjusted for their trade (plumbing adds sewage/burst; gutter work drops gas).
- [ ] Suppression/DNC list imported BEFORE anything can send.

## Gate 3 — Voice and judgment (one hour with the owner)

- [ ] 3–5 real messages from their front desk pasted into the voice section of config.
- [ ] Owner walk-through: "what should ALWAYS reach a human immediately?" → escalation list in config.
- [ ] Their review link, hours, on-call phone confirmed by them in writing (email is fine — link it in config).

## Gate 4 — Test before any real caller

Run the workflow-01 test plan with THEIR config — all seven cases: normal missed call · price question · safety keyword · STOP · injection attempt · out-of-area · after-hours. Pass = correct path taken AND correct audit_log row written, per case. Record the run (date, who, results) at the bottom of their config.yml.

## Gate 5 — HITL launch (every client, every time)

- [ ] HITL gate ON. Approver named in config (their office manager or CenseoAI, per the deal).
- [ ] Flip-to-autonomous is PER CLIENT: Module A recognition current + tool validation recorded for their instance + 30+ approved sends at ≥95% unmodified. First-touch flips first; replies stay gated 30 more days. Never launch a new client straight to autonomous — including client #10.

## Gate 6 — Wire CenseoAI's own delivery machinery

- [ ] Client record in CenseoAI's GHL; `projects/<client>.md` in the founder vault; account-manager kickoff package.
- [ ] Weekly `/revenue-scoreboard` cadence scheduled — missed-calls-recovered is the headline metric of this product.
- [ ] Day-30 evidence file on the calendar (rung-conversion conversation).
- [ ] Decision-log entry: client added, lane used, anything nonstandard about the deal.

## Offboarding (define it at onboarding, not at the breakup)

Their accounts, their data — offboarding = we revoke OUR access: remove CenseoAI credentials from their n8n/GHL, hand over admin, export their audit_log slice on request, mark the client dir archived. Workflows keep running; they own them. That's a selling point — say it in the pitch.
