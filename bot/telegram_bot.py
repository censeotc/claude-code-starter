#!/usr/bin/env python3
"""
telegram_bot.py - Source-grounded Q&A bot over Anthropic's published sources.

Answers questions in Telegram using Claude with the web_search tool, restricted
to Anthropic's official domains (anthropic.com, docs.claude.com, github.com/anthropics).
Cites every claim. Refuses to answer if the source material doesn't cover it.

Required env vars:
    TELEGRAM_BOT_TOKEN          From @BotFather on Telegram
    TELEGRAM_ALLOWED_USER_ID    Your Telegram numeric user ID (from @userinfobot)
    ANTHROPIC_API_KEY           From console.anthropic.com

Optional env vars:
    CLAUDE_MODEL                Default: claude-sonnet-4-6
    MAX_HISTORY_TURNS           Default: 10 (user+assistant pairs per chat)
    MAX_TOKENS_OUT              Default: 2000

Run:
    pip install -r requirements.txt
    python telegram_bot.py
"""

import asyncio
import logging
import os
import re
import sys
import time
from collections import defaultdict, deque

import anthropic
from telegram import Update
from telegram.constants import ChatAction, ParseMode
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# ----- Config -----

ALLOWED_DOMAINS = [
    "anthropic.com",
    "docs.claude.com",
    "github.com/anthropics",
]

SYSTEM_PROMPT = (
    "You are a research assistant specializing in Anthropic's products, models, "
    "and research. Answer questions based ONLY on information found at "
    "anthropic.com, docs.claude.com, and github.com/anthropics.\n\n"
    "Rules:\n"
    "1. Use web_search to find current information before answering. Search "
    "   multiple queries if needed to cover the question fully.\n"
    "2. Cite sources for every factual claim. Citations are auto-attached by "
    "   the search tool; you don't need inline markers.\n"
    "3. If the answer is not in those sources, say: 'I couldn't find that in "
    "   Anthropic's published materials.' Do NOT invent information.\n"
    "4. Prefer the most recent post when sources disagree or evolve.\n"
    "5. Be specific: include dates, version numbers, names, and concrete details.\n"
    "6. Keep replies concise. Telegram messages are best under 1500 characters. "
    "   Use short paragraphs and bullets ('- '). Avoid Markdown tables."
)

MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-6")
MAX_HISTORY_TURNS = int(os.environ.get("MAX_HISTORY_TURNS", "10"))
MAX_TOKENS_OUT = int(os.environ.get("MAX_TOKENS_OUT", "2000"))
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
ALLOWED_USER_ID = int(os.environ.get("TELEGRAM_ALLOWED_USER_ID", "0") or "0")

TELEGRAM_MAX_CHARS = 4000  # Hard limit is 4096; keep a small buffer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger("anthropic-bot")

# ----- State -----

# In-memory per-chat conversation history. Reset on bot restart.
# Format: deque of {"role": "user"|"assistant", "content": str|list}
history: dict[int, deque] = defaultdict(lambda: deque(maxlen=MAX_HISTORY_TURNS * 2))

# Simple rate limit: max 1 in-flight request per chat
in_flight: set[int] = set()

claude = anthropic.Anthropic()  # picks up ANTHROPIC_API_KEY from env


# ----- Claude call -----

def call_claude(messages: list[dict]) -> tuple[str, list[str]]:
    """Returns (answer_text, list_of_source_urls)."""
    resp = claude.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS_OUT,
        system=[{
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }],
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 5,
            "allowed_domains": ALLOWED_DOMAINS,
        }],
        messages=messages,
    )

    text_parts: list[str] = []
    sources: list[str] = []
    seen_urls: set[str] = set()
    for block in resp.content:
        if block.type == "text":
            text_parts.append(block.text)
            for citation in getattr(block, "citations", None) or []:
                url = getattr(citation, "url", None) or (
                    citation.get("url") if isinstance(citation, dict) else None
                )
                if url and url not in seen_urls:
                    sources.append(url)
                    seen_urls.add(url)
    answer = "\n".join(text_parts).strip()
    return answer or "(no answer returned)", sources


# ----- Telegram handlers -----

def is_authorized(update: Update) -> bool:
    if not ALLOWED_USER_ID:
        log.warning("TELEGRAM_ALLOWED_USER_ID not set; rejecting everyone.")
        return False
    return update.effective_user and update.effective_user.id == ALLOWED_USER_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update):
        await update.message.reply_text("Sorry, this bot is private.")
        return
    await update.message.reply_text(
        "Hi! Ask me anything about Anthropic's products, models, or research. "
        "I'll search anthropic.com, docs.claude.com, and github.com/anthropics, "
        "then answer with citations.\n\n"
        "Commands:\n"
        "/reset - clear our conversation history\n"
        "/help - show this message"
    )


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update):
        return
    history[update.effective_chat.id].clear()
    await update.message.reply_text("Conversation history cleared.")


def _chunk(text: str, limit: int = TELEGRAM_MAX_CHARS) -> list[str]:
    """Split text into Telegram-sized chunks at paragraph boundaries when possible."""
    if len(text) <= limit:
        return [text]
    chunks: list[str] = []
    buf = ""
    for paragraph in re.split(r"(\n\n+)", text):
        if len(buf) + len(paragraph) <= limit:
            buf += paragraph
        else:
            if buf:
                chunks.append(buf)
            # If a single paragraph is over limit, hard split
            while len(paragraph) > limit:
                chunks.append(paragraph[:limit])
                paragraph = paragraph[limit:]
            buf = paragraph
    if buf:
        chunks.append(buf)
    return chunks


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update):
        await update.message.reply_text("Sorry, this bot is private.")
        return

    chat_id = update.effective_chat.id
    question = (update.message.text or "").strip()
    if not question:
        return

    if chat_id in in_flight:
        await update.message.reply_text(
            "Still working on your previous question — give me a sec."
        )
        return

    in_flight.add(chat_id)
    try:
        await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        chat_history = history[chat_id]
        chat_history.append({"role": "user", "content": question})
        messages = list(chat_history)

        t0 = time.monotonic()
        loop = asyncio.get_running_loop()
        try:
            answer, sources = await loop.run_in_executor(None, call_claude, messages)
        except anthropic.APIError as e:
            log.exception("Claude API error")
            await update.message.reply_text(f"Claude API error: {e}")
            chat_history.pop()  # remove the unanswered user msg
            return
        except Exception as e:
            log.exception("Unexpected error")
            await update.message.reply_text(f"Something broke: {e}")
            chat_history.pop()
            return
        elapsed = time.monotonic() - t0
        log.info("answered in %.1fs (%d sources)", elapsed, len(sources))

        chat_history.append({"role": "assistant", "content": answer})

        # Compose reply: answer + sources
        if sources:
            src_lines = "\n".join(f"- {u}" for u in sources[:8])
            reply = f"{answer}\n\nSources:\n{src_lines}"
        else:
            reply = answer

        for chunk in _chunk(reply):
            await update.message.reply_text(
                chunk,
                disable_web_page_preview=True,
            )
    finally:
        in_flight.discard(chat_id)


# ----- Main -----

def main():
    missing = [k for k, v in (
        ("TELEGRAM_BOT_TOKEN", TELEGRAM_BOT_TOKEN),
        ("TELEGRAM_ALLOWED_USER_ID", ALLOWED_USER_ID),
        ("ANTHROPIC_API_KEY", os.environ.get("ANTHROPIC_API_KEY")),
    ) if not v]
    if missing:
        sys.exit(f"Missing required env vars: {', '.join(missing)}")

    log.info("Starting bot for user_id=%s, model=%s", ALLOWED_USER_ID, MODEL)
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
