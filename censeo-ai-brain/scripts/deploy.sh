#!/usr/bin/env bash
# Deploy/update the AI Brain stack on the Hostinger VPS.
# Usage (on the VPS): ./scripts/deploy.sh
set -euo pipefail
cd "$(dirname "$0")/.."

if [ ! -f .env ]; then
  echo "ERROR: .env missing. Copy .env.example to .env and fill it in first." >&2
  exit 1
fi

echo "→ Pulling latest repo state..."
git pull --ff-only

echo "→ Pulling images and (re)starting stack..."
docker compose pull
docker compose up -d

echo "→ Waiting for Postgres health..."
until docker compose exec -T postgres pg_isready -U "${POSTGRES_USER:-censeo}" -d censeo >/dev/null 2>&1; do
  sleep 2
done

echo "→ Applying any new migrations..."
for f in db/migrations/*.sql; do
  [ -e "$f" ] || continue
  # naive tracker: applied filenames recorded in a table
  applied=$(docker compose exec -T postgres psql -U "${POSTGRES_USER:-censeo}" -d censeo -tAc \
    "CREATE TABLE IF NOT EXISTS _migrations(name text primary key, applied_at timestamptz default now());
     SELECT 1 FROM _migrations WHERE name='$(basename "$f")';")
  if [ "$applied" != "1" ]; then
    echo "   applying $(basename "$f")"
    docker compose exec -T postgres psql -U "${POSTGRES_USER:-censeo}" -d censeo -v ON_ERROR_STOP=1 < "$f"
    docker compose exec -T postgres psql -U "${POSTGRES_USER:-censeo}" -d censeo -c \
      "INSERT INTO _migrations(name) VALUES ('$(basename "$f")');"
  fi
done

echo "→ Syncing knowledge to pgvector..."
./scripts/sync-knowledge-to-pgvector.sh || echo "WARN: knowledge sync failed — run manually"

echo "✓ Deploy complete. n8n: 127.0.0.1:5678 · Langfuse: 127.0.0.1:3000 (behind your reverse proxy)"
