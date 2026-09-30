# censeo-ai-brain

CenseoAI's actual deployed work inside this repo. The repo's top-level
`README.md` is the upstream Maven course material this repo was forked
from (Hamza Farooq's "Claude Code in Practice"), not about this folder;
everything CenseoAI-specific lives here instead.

**Read `BUILD-SPEC.md` first.** It's the working spec Claude Code builds
against, and the source of truth for build decisions (updated in place as
decisions get made, not left to drift into chat history).

**`SOURCE_OF_TRUTH.md` always wins on facts** (pricing, product
descriptions, build status), if anything conflicts with it, this file is
correct. Reviewed monthly, critical items updated immediately on change.

- `docs/` — `architecture.md`, `decision-log.md`, `PROJECTMANIFEST.md`
  (master index of every external artifact from the founding build
  session, filed here from `incoming/` on 2026-09-30).
- `clients/` — per-client working folders, has its own `README.md` and a
  `_template/` to start a new one from.
- `sops/` — standard operating procedures (customer follow-up, missed-call
  text-back, HVAC lead qualification, real estate disclosure language).
- `n8n-workflows/` — exported n8n workflow definitions.
- `prompts/` — reusable prompt templates.
- `scripts/`, `db/` — supporting code and database material.
- `docker-compose.yml`, `.env.example` — this system's own compose/config,
  separate from `/root/docker-compose.yml` (the host-level traefik/n8n/
  rewards stack) and `/opt/intuasite/mvp` (the IntuaSite site engine).
