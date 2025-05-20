import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import nest_asyncio

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привіт! Я Telegram-бот.")

# Основна функція
async def main():
    app_bot = ApplicationBuilder().token("7695005663:AAGh_s9JjLEpVVZrv5VVEHE7Hg3z8Z8pSzc").build()

    app_bot.add_handler(CommandHandler("start", start))

    print("✅ Бот запущено. Очікую повідомлення...")
    await app_bot.run_polling()

# Запуск з урахуванням активного event loop
if __name__ == '__main__':
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
