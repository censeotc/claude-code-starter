-- CenseoAI AI Brain — Postgres schema
-- Runs automatically on first boot of a fresh pgdata volume (compose init script).
-- Later changes go in db/migrations/, never by editing this file after deploy.

-- databases for the stack services
CREATE DATABASE n8n;
CREATE DATABASE langfuse;

\connect censeo

CREATE EXTENSION IF NOT EXISTS vector;

-- ============================================================
-- PRICING — the ONLY source agents may quote prices from.
-- (Guardrail per BUILD-SPEC §1.6: never LLM-composed.)
-- ============================================================
CREATE TABLE pricing (
    id            serial PRIMARY KEY,
    package_code  text UNIQUE NOT NULL,      -- e.g. 'leakage-audit', 'pilot-45d'
    display_name  text NOT NULL,
    price_usd     numeric(10,2),             -- NULL = "contact for pricing", never guess
    billing       text NOT NULL,             -- 'fixed' | 'monthly'
    sellable      boolean NOT NULL DEFAULT false,
    notes         text,
    valid_from    timestamptz NOT NULL DEFAULT now(),
    valid_to      timestamptz                -- close the old row, insert a new one on change
);

-- Seed rows: sellable=false + NULL price until Scott inputs real figures.
INSERT INTO pricing (package_code, display_name, price_usd, billing, sellable, notes) VALUES
 ('leakage-audit', 'Revenue Leakage Audit',                    NULL, 'fixed',   false, 'often creditable into pilot'),
 ('pilot-45d',     '45-Day Pilot',                             NULL, 'fixed',   false, NULL),
 ('build-90d',     '90-Day Revenue Operating System Build',    NULL, 'fixed',   false, NULL),
 ('retainer',      'Optimization Retainer',                    NULL, 'monthly', false, 'seasonal optimization');

CREATE TABLE service_areas (
    id         serial PRIMARY KEY,
    client     text NOT NULL DEFAULT 'censeoai',   -- parameterized for resale
    area_name  text NOT NULL,
    zip_codes  text[],
    active     boolean NOT NULL DEFAULT true
);

-- ============================================================
-- AUDIT LOG — Governance Template v4.9 event-level logging.
-- One row per consequential agent action; the 13 event-log fields
-- are first-class columns so the log is queryable, not parsed.
-- Append-only: no UPDATE/DELETE grants to agent roles.
-- ============================================================
CREATE TABLE audit_log (
    id                  bigserial PRIMARY KEY,
    event_id            text UNIQUE NOT NULL,         -- EVT-YYYY-MM-DD-nnnnn
    occurred_at         timestamptz NOT NULL DEFAULT now(),
    workflow_id         text NOT NULL,                -- WF-missed-call-textback-v1
    validation_id       text,                         -- NULL until Module A recognition + tool validation
    model_version       text,
    prompt_version      text,                         -- e.g. prompts/sales/lead-qualification-v1.md@git-sha
    channel             text NOT NULL,                -- sms | email | internal
    recipient_ref       text,                         -- GHL contact id — never raw PII here
    consent_status      text,                         -- opted-in | express-written | n/a-internal
    dnc_status          text,                         -- clear | listed | n/a
    monitor_status      text,                         -- active | down
    policy_check        text,                         -- pass | fail:<reason>
    escalation_result   text,                         -- none | escalated:<to>
    release_path        text NOT NULL,                -- manual-hitl | autonomous  (manual-hitl until Module A)
    approved_by         text,                         -- human approver for manual-hitl rows
    langfuse_trace_id   text,
    payload_summary     text                          -- one-line description, no PII
);
CREATE INDEX ON audit_log (occurred_at);
CREATE INDEX ON audit_log (workflow_id, occurred_at);

-- ============================================================
-- KNOWLEDGE — pgvector store fed by scripts/sync-knowledge-to-pgvector.sh
-- ============================================================
CREATE TABLE knowledge_chunks (
    id          bigserial PRIMARY KEY,
    source_path text NOT NULL,                 -- sops/missed-call-text-back.md
    heading     text,
    chunk_text  text NOT NULL,
    embedding   vector(1536),                  -- text-embedding-3-small
    git_sha     text NOT NULL,
    synced_at   timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX ON knowledge_chunks USING hnsw (embedding vector_cosine_ops);

-- ============================================================
-- AGENT MEMORY — temporal facts: invalidated, never overwritten
-- (BUILD-SPEC §7.11 temporal-fact-invalidation requirement)
-- ============================================================
CREATE TABLE agent_memory (
    id              bigserial PRIMARY KEY,
    subject_ref     text NOT NULL,             -- GHL contact id / 'censeoai' / workflow id
    fact            text NOT NULL,
    source          text NOT NULL,             -- where this was learned
    recorded_at     timestamptz NOT NULL DEFAULT now(),
    invalidated_at  timestamptz,               -- set when superseded; row is kept
    superseded_by   bigint REFERENCES agent_memory(id)
);
CREATE INDEX ON agent_memory (subject_ref) WHERE invalidated_at IS NULL;

-- ============================================================
-- FEEDBACK QUEUE — agents propose, humans dispose (BUILD-SPEC §8.14)
-- ============================================================
CREATE TABLE feedback_queue (
    id           bigserial PRIMARY KEY,
    raised_by    text NOT NULL,                -- workflow/agent id
    raised_at    timestamptz NOT NULL DEFAULT now(),
    category     text NOT NULL,                -- stale-sop | broken-workflow | pricing-stale | other
    proposal     text NOT NULL,
    status       text NOT NULL DEFAULT 'open', -- open | accepted | rejected
    resolved_by  text,
    resolved_at  timestamptz,
    resolution   text
);
