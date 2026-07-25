# SOP: HVAC Lead Qualification

**Tier: Critical** · v1 · 2026-07-25 · Governs the Phase-2 AI SDR/Lead Qualifier

## Purpose
Turn an inbound inquiry into a qualified, routable opportunity in GHL — or a polite, fast no — without the founder touching routine qualification.

## What "qualified" means (capture all five)
1. **Need** — repair, replacement/install, maintenance, or estimate; equipment type and symptom in the caller's words.
2. **Urgency** — emergency (no heat/no cool in extreme weather → escalate per missed-call SOP), this week, flexible.
3. **Location** — inside the active service area (`service_areas` lookup). Outside → capture and decline politely; log for territory analysis.
4. **Property & ownership** — home/business, own/rent (renters: work orders usually go through the owner/property manager — capture that contact).
5. **Decision & timing** — who decides, and for replacements: are they gathering quotes or ready to schedule?

## Conversation rules
- One question at a time; mirror their channel (SMS stays SMS).
- **Never** diagnose ("sounds like your compressor is dead"), never estimate repair costs, never disparage another contractor's work.
- Pricing: lookup-only, same guardrail as everywhere. Diagnostic/trip fee may be quoted **only** if a priced row exists; otherwise "the technician will confirm."
- Financing questions → flag for human; no terms discussed by the agent.

## Scoring & routing (encoded as n8n rules, not LLM judgment)
- Emergency → immediate human escalation path.
- Replacement/install lead (high ticket) → tag HOT, notify founder same business day; agent hands off above the deal-size threshold in SOURCE_OF_TRUTH (NEEDS-INPUT: set threshold).
- Routine repair/maintenance in-area → book directly onto the calendar.
- Out of area / not a fit → courteous decline template; tag DECLINED-OOA.

## Every qualification writes to GHL
Contact fields updated, pipeline stage set, conversation summary note, next action + owner. No qualification exists if it isn't in GHL — memory of leads lives in the system of record, nowhere else.
