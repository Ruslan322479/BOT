import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

TRIGGER_WORDS = ["роздрукувати", "видрукувати", "друк", "принтер"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        if any(word in text for word in TRIGGER_WORDS):
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="З друком допоможе @Viperiukr"
            )

async def main():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Бот запущено. Очікую повідомлення...")
    await app_bot.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
