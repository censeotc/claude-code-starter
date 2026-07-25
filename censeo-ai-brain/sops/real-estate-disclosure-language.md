# SOP: Real-Estate Disclosure & Compensation Language

**Tier: Critical — compliance** · v1 · 2026-07-25 · Reviewed against NAR Nov 2025 Board of Directors Special Report (rules effective Jan 1, 2026)

## Scope
Applies to ANY agent- or AI-assisted output touching real-estate representation, broker compensation, buyer agreements, or listing/tenant/valuation content — for CenseoAI's real-estate technology consulting clients or its own materials.

## The current rule baseline (post-NAR-settlement, as amended effective 2026-01-01)
- Compensation-disclosure obligations under the NAR Code of Ethics are limited to a REALTOR's **own client(s)**.
- Written buyer-broker agreements may include compensation terms **with no obligation to disclose those terms to sellers or their brokers**.
- Do not generate language implying: compensation must be broadcast to all parties, that any commission rate is "standard," or that compensation terms are set by anyone other than negotiation between the parties.

⚠ This baseline is a summary for agent routing, **not legal advice**. State rules and MLS policies layer on top. Anything novel goes to the client's broker/counsel.

## Hard gates (enforced in code — n8n IF/Switch, not prompts)
1. Output mentioning commission, compensation, buyer agreement terms, dual agency, or agency relationships → **route to compliance review**; never auto-sends. (Under Governance v4.9 this is the no-release class until a legal review process exists.)
2. Never generate: commission amounts/percentages as recommendations; "standard rate" claims; steering language (favoring listings by compensation offered).
3. **Fair Housing:** no output may describe people rather than property. Blocklist-plus-review for protected-class proxies (familial status, religion, national origin, disability, "safe neighborhood," "great schools for families," etc.). Any future valuation/tenant-screening/listing-recommendation feature requires a documented bias review BEFORE shipping (HUD disparate-impact standard — outcomes count, intent doesn't).

## Drafting rules for permitted content
- Facts about property, process, and timelines: fine, with sources.
- Anything about who pays whom: template language only, from this SOP's approved snippets (to be added as the consulting practice defines them — NEEDS-INPUT), merged with client-specific terms by lookup, never composed.
- Every draft in this category is labeled per the Disclosure Taxonomy and carries the compliance-review flag in the audit log.

## Refresh trigger
Any NAR, state-license-law, MLS-policy, or HUD guidance change → this SOP is stale IMMEDIATELY (0-day tier): re-verify before the next output in this category ships.
