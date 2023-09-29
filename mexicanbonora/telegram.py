from __future__ import annotations
from logging import INFO, basicConfig, getLogger
from telegram import Bot, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    ContextTypes,
    Application,
)
from os import environ

from mexicanbonora.chat import chat
from mexicanbonora.translate import translate
from mexicanbonora.utils import retry

PORT = 8080
URL = "https://mexicanbonora.fly.dev"

BOT_USERNAME = "@mexicanbonora_bot"
LOGGER = getLogger(__name__)


@retry
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message is not None
    assert update.message.text is not None
    assert update.effective_chat is not None
    message: str = update.message.text.removeprefix("/chat").strip()
    input = translate(message, "en")
    reply = chat(input)
    final_reply = translate(reply, "es")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=final_reply,
    )


def telegram():
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
    )
    token = environ["TOKEN"]
    debug = "DEBUG" in environ
    application: Application[
        Bot,
        CallbackContext[Bot, None, None, None],
        None,
        None,
        None,
        None,
    ] = (
        ApplicationBuilder().token(token).build()
    )

    message_handler = CommandHandler("chat", callback=reply)
    application.add_handler(message_handler)

    LOGGER.info(f"DEBUG: {__debug__}")
    if __debug__:
        application.run_polling()
    else:
        application.run_webhook(listen="0.0.0.0", port=PORT, webhook_url=URL)


if __name__ == "__main__":
    telegram()
