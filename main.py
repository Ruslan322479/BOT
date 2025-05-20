import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привіт! Напиши щось про друк, і я зреагую!")

# Обробка повідомлень
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    keywords = ["друк", "роздрукувати", "принтер", "видрукувати"]

    if any(word in text for word in keywords):
        username = update.message.from_user.username
        if username:
            await update.message.reply_text(f"👤 Твій username: @{username}")
        else:
            name = update.message.from_user.first_name
            await update.message.reply_text(f"👤 Привіт, {name}! У тебе немає username 😅")
    else:
        await update.message.reply_text("Я реагую тільки на слова про друк 🖨️")

# Основна функція
async def main():
    app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Бот запущено. Очікую повідомлення...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
