# SOP: Missed-Call Text-Back

**Tier: Critical** · v1 · 2026-07-25 · Governs workflow `WF-missed-call-textback-v1`

## Purpose
A missed call to a contractor is revenue walking away — the documented recovery benchmark for the trades is 6–14% of missed calls converted to booked appointments. This SOP defines what the text-back agent says, when, and when it must stop and hand off.

## Trigger
GHL detects a missed/unanswered inbound call to the business line during OR outside business hours.

## Consent & compliance gate (before any send)
- An inbound call from the number constitutes the engagement basis for one contextual text-back; log consent status on the event.
- Check the do-not-contact/suppression list. Listed → no send, log, stop.
- Every message includes opt-out handling ("Reply STOP to opt out" on first contact); a STOP reply suppresses the number immediately and permanently.

## The message (first touch, within 2 minutes of the missed call)
Goldilocks guidance — adapt naturally to context, keep these invariants:
- Identify the business by name immediately.
- Acknowledge the missed call and apologize briefly.
- Ask ONE question that moves toward booking: what do they need help with?
- Plain, human, local tone. No marketing language. Under 320 characters.

Example shape (not a script): *"Hi, this is {business_name} — sorry we missed your call! How can we help — is this for a repair, an estimate, or something else? Reply STOP to opt out."*

## Conversation rules
- Goal: book the appointment or capture name + need + address + preferred time, then confirm a human will call.
- **NEVER quote a price, discount, or timeframe-commitment freely.** Prices come only from the pricing lookup (GHL custom fields / Postgres `pricing`); if no priced entry exists for the request → "our team will confirm pricing when we call you."
- The output filter blocks commitment language ("I can offer", "guaranteed", "that's a deal", "we'll definitely") → route to human review.

## Escalation triggers (immediate human handoff, tag URGENT in GHL)
- Safety keywords: gas, leak, smell, smoke, flood, flooding, no heat (below freezing), no AC (heat advisory), carbon monoxide, sparking.
- Anger/complaint signals or mention of a lawyer, refund, or review threat.
- Caller is an existing client with an active job (lookup in GHL).
- Anything the agent scores as unclear after two exchanges.
Escalation = stop replying, notify the human (call + SMS to founder/on-call), log the reason.

## Boundaries (enforced in n8n code, not prompts)
- HITL gate ON: until Module A recognition, every outbound message is human-approved before send.
- No messages outside 8am–9pm recipient local time (queue for morning).
- Max 3 agent messages without a human reply from the caller; then stop.

## Every send logs
`audit_log` row (event id, workflow, channel=sms, recipient ref, consent, DNC, policy-check, release path, approver) + Langfuse trace.

## Parameterization (resale-ready)
`{business_name}`, `{service_area}`, `{business_hours}`, `{escalation_phone}`, pricing table reference — all config, never hardcoded in prompts or workflow JSON.
