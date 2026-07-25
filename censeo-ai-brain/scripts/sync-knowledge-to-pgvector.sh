#!/usr/bin/env bash
# Embed /sops and /prompts markdown into Postgres pgvector (knowledge_chunks).
# Heading-aware chunking so sections aren't split mid-list (BUILD-SPEC §7.9).
# Requires: python3, psql access via DATABASE_URL, OPENAI_API_KEY (.env).
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; [ -f .env ] && . ./.env; set +a

GIT_SHA=$(git rev-parse --short HEAD)

python3 - "$GIT_SHA" <<'PYEOF'
import os, sys, json, glob, re, urllib.request
import subprocess

git_sha = sys.argv[1]
api_key = os.environ["OPENAI_API_KEY"]
db_url  = os.environ["DATABASE_URL"]
model   = os.environ.get("EMBEDDING_MODEL", "text-embedding-3-small")

def chunks_from(path):
    text = open(path).read()
    # split on headings; merge tiny sections; cap ~1000 tokens (~4000 chars) w/ overlap
    parts = re.split(r'(?m)^(#{1,3} .*)$', text)
    sections, current_head = [], ""
    for p in parts:
        if re.match(r'^#{1,3} ', p or ""):
            current_head = p.strip()
        elif p and p.strip():
            body = p.strip()
            for i in range(0, len(body), 3600):          # ~900 tokens
                sections.append((current_head, body[max(0, i-400):i+3600]))  # ~10% overlap
    return sections

def embed(texts):
    req = urllib.request.Request(
        "https://api.openai.com/v1/embeddings",
        data=json.dumps({"model": model, "input": texts}).encode(),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return [d["embedding"] for d in json.load(r)["data"]]

rows = []
for path in sorted(glob.glob("sops/*.md") + glob.glob("prompts/**/*.md", recursive=True)):
    if "/deprecated/" in path:
        continue
    secs = chunks_from(path)
    if not secs:
        continue
    embs = embed([s[1] for s in secs])
    rows += [(path, h, t, e) for (h, t), e in zip(secs, embs)]

sql = ["BEGIN;", "DELETE FROM knowledge_chunks;"]
for path, head, text, emb in rows:
    t = text.replace("'", "''"); h = (head or "").replace("'", "''")
    sql.append(f"INSERT INTO knowledge_chunks (source_path, heading, chunk_text, embedding, git_sha) "
               f"VALUES ('{path}', '{h}', '{t}', '{json.dumps(emb)}', '{git_sha}');")
sql.append("COMMIT;")

subprocess.run(["psql", db_url, "-v", "ON_ERROR_STOP=1"],
               input="\n".join(sql).encode(), check=True)
print(f"synced {len(rows)} chunks @ {git_sha}")
PYEOF
