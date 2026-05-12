# Anthropic Sources Telegram Bot

Chat with a private Telegram bot that answers questions using **only** Anthropic's published material — anthropic.com, docs.claude.com, and github.com/anthropics. Every answer cites its sources. The bot refuses to answer when the source material doesn't cover the question, instead of inventing something.

```
You (Telegram)
    │
    ▼ "What are the best practices for Claude Design?"
    │
    ▼
Bot (Fly.io, always-on)
    │
    ▼  Claude Sonnet 4.6 + web_search restricted to Anthropic domains
    │
    ▼
Answer + citation URLs
```

Optionally, each Q&A is also mirrored to your email inbox (HTML format with sources) — see "Email mirror" below.

## What you'll need (~30 minutes total)

1. A Telegram account
2. The `claude-code-starter` repo cloned locally (you already have it)
3. A free Fly.io account
4. Your Anthropic API key (you already have this in GitHub secrets)

---

## Step 1 — Create the Telegram bot (~3 min)

1. Open Telegram. Search for **@BotFather** (the official bot, blue checkmark).
2. Send `/newbot`.
3. Send a name for your bot, e.g. `Anthropic Sources`.
4. Send a username, must end in `bot`, e.g. `anthropic_sources_yourname_bot`.
5. BotFather replies with **your bot's HTTP API token**, looks like `7123456789:AAH...xyz`. **Copy and save this.**

## Step 2 — Get your Telegram user ID (~1 min)

1. In Telegram, search for **@userinfobot** and start a chat.
2. Send any message. It replies with your numeric ID, e.g. `Id: 987654321`.
3. **Copy and save this number.**

## Step 3 — Install the Fly CLI (~3 min)

**Windows (PowerShell, run as your user — not admin):**
```powershell
iwr https://fly.io/install.ps1 -useb | iex
```

Close and re-open your terminal so the new `flyctl` is on PATH.

**Verify:**
```powershell
fly version
```

## Step 4 — Sign up and authenticate (~2 min)

```powershell
fly auth signup
```

Browser opens — sign up with email or GitHub. You'll need to **add a credit card** (Fly requires this for abuse prevention), but you won't be charged at this scale.

If you already have an account: `fly auth login`.

## Step 5 — Launch the app (~3 min)

From the repo root:

```powershell
fly launch --config bot/fly.toml --dockerfile bot/Dockerfile --copy-config --no-deploy
```

You'll be asked:
- **App name**: type a unique name like `anthropic-source-bot-<yourname>` (lowercase, dashes only)
- **Region**: pick one near you (e.g. `iad` for US-East, `lax` for US-West, `lhr` for London)
- **Postgres / Redis / Tigris**: answer **No** to all
- **Deploy now?**: answer **No** (we set secrets first)

## Step 6 — Set the secrets (~1 min)

Replace the placeholder values with what you saved in steps 1, 2, and your Anthropic key.

```powershell
fly secrets set --config bot/fly.toml `
  TELEGRAM_BOT_TOKEN="7123456789:AAH...xyz" `
  TELEGRAM_ALLOWED_USER_ID="987654321" `
  ANTHROPIC_API_KEY="sk-ant-..."
```

Verify:
```powershell
fly secrets list --config bot/fly.toml
```

You should see all three secret names (values are hidden).

### Email mirror (optional, but recommended)

If you also want every Q&A delivered to your inbox in HTML, add three more secrets — the same Gmail App Password values you used for the watcher:

```powershell
fly secrets set --config bot/fly.toml `
  SMTP_USER="scott@censeoai.ai" `
  SMTP_PASS="your-16-char-google-app-password" `
  EMAIL_TO="scott@censeoai.ai"
```

If any of those three is missing, the email mirror silently disables itself and the bot still works in Telegram. If SMTP fails at send time, the bot logs a warning and still replies in Telegram.

## Step 7 — Deploy (~5 min)

```powershell
fly deploy --config bot/fly.toml --dockerfile bot/Dockerfile
```

First deploy builds the Docker image and starts the bot. Once you see `1 desired, 1 placed, 1 healthy`, it's live.

## Step 8 — Talk to your bot

1. In Telegram, search for the username you set in Step 1.
2. Tap **Start**.
3. Ask anything: *"What are the best practices for Claude Design?"*

The bot replies with the answer and source URLs. If the answer isn't in Anthropic's sources, it tells you so instead of making something up.

---

## Daily use

- **Just chat normally.** The bot remembers the last 10 question/answer pairs per chat for follow-ups like "tell me more" or "what was the date on that?"
- **`/reset`** — clears the conversation memory if you want a clean slate.
- **`/help`** — usage reminder.

## What it costs

| Item | Cost |
|---|---|
| Fly.io VM (256MB, 1 shared CPU, always on) | ~$0 on free tier; tiny if exceeded |
| Anthropic API per question | ~$0.03 - $0.08 (varies with web searches and answer length) |
| Estimated for 20 questions/day | ~$30/month |

To reduce: lower `MAX_TOKENS_OUT` in `bot/fly.toml`, or change `CLAUDE_MODEL` to `claude-haiku-4-5-20251001`.

## Updating the bot

After changing `bot/telegram_bot.py` or other bot files:

```powershell
fly deploy --config bot/fly.toml --dockerfile bot/Dockerfile
```

## Troubleshooting

**Bot doesn't respond at all**
- `fly status --config bot/fly.toml` should show a healthy machine
- `fly logs --config bot/fly.toml` will show errors. Most common: typo in a secret.

**Bot says "Sorry, this bot is private."**
- The `TELEGRAM_ALLOWED_USER_ID` secret doesn't match your account. Re-run step 2 and update the secret.

**Bot says "I couldn't find that in Anthropic's published materials."**
- That's working as designed — Anthropic hasn't published anything that answers your question. Try rephrasing or ask something covered in their public material.

**Long delays before reply**
- Each question triggers 1-5 web searches plus Claude's reasoning. 10-30 seconds is normal for complex questions.

**Bot stops working after a few days**
- Fly machines occasionally restart. Memory of recent chats is lost (history is in-memory, not persisted). The bot itself comes back up automatically.

## Local run (optional, for debugging)

```powershell
cd bot
copy .env.example .env
# fill in real values in .env
# in PowerShell:
Get-Content .env | ForEach-Object { $name, $value = $_ -split '=', 2; if ($name) { [Environment]::SetEnvironmentVariable($name, $value, 'Process') } }
pip install -r requirements.txt
python telegram_bot.py
```

Runs the same bot on your machine. Stop with Ctrl+C.
