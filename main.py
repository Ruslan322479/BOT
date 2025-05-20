import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import Message

# Читання токена з секретів Render
TOKEN = os.environ.get("BOT_TOKEN")

# Ініціалізація бота та диспетчера
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("👋 Привіт! Я бот-друкар. Напиши щось, що треба роздрукувати!")

# Реакція на ключові слова
@dp.message()
async def print_reaction(message: Message):
    keywords = ['роздрукувати', 'друк', 'принтер', 'видрукувати']
    msg_text = message.text.lower()

    if any(keyword in msg_text for keyword in keywords):
        username = message.from_user.username or "Невідомо"
        await message.reply(f"🖨️ Запит на друк від: @{username}")

# Запуск бота
async def main():
    print("✅ Бот запущено")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        print("❌ Бот зупинено")
