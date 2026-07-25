# Workflow design: 03 — Follow-Up / Review Request (`WF-followup-review-v1`) — PHASE 2

**SOP:** [../sops/customer-followup.md](../sops/customer-followup.md)

Shape: GHL job-complete status change → schedule the 3-step sequence (same-evening satisfaction SMS → +2d review request → +30d/seasonal check-in) → each step passes the standard gates (DNC/STOP, time window, output filter, HITL until autonomous criteria met) → negative response at step 1 → SERVICE-RECOVERY branch: kill sequence, human task in GHL, no review ask ever without human decision → audit_log + Langfuse per send.

Copy passes the marketing-copy-review prompt once per template version (not per send): review verdict stored with the template's version in git.
