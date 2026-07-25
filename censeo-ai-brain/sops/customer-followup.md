# SOP: Customer Follow-Up & Review Request

**Tier: Reference** · v1 · 2026-07-25

## Purpose
The job isn't done when the truck leaves: confirm satisfaction, catch problems before they become bad reviews, and turn happy customers into public proof and repeat revenue.

## The sequence (per completed job, timed from job-complete status in GHL)
1. **Same evening — satisfaction check.** One SMS: did everything go well? Anything not right → apologize, escalate to human next-business-day promise, tag SERVICE-RECOVERY, stop the sequence.
2. **+2 days — review request** (only if step 1 was positive or unanswered-then-positive). One link, one ask, in the business's voice. Never incentivize reviews, never ask only "happy" customers while suppressing others in the same breath — the request goes to everyone whose step 1 wasn't negative (FTC review-integrity basics).
3. **+30 days (installs) / seasonal (maintenance)** — useful check-in: filter reminder, seasonal tune-up window, membership offer if one exists in the pricing table.

## Rules
- Respect STOP instantly and permanently across all sequences.
- Max one message per step; no re-asks for reviews.
- Service-recovery cases: no review request ever gets sent later without a human deciding to.
- Every send: consent/DNC check + audit_log row, same as all outbound.
- Voice: match the client business's tone config; plain and local, never corporate.

## Parameterization
`{review_link}`, `{business_name}`, timing offsets, and membership/maintenance offers are config per client.
