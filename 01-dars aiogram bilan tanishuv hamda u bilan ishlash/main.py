import asyncio
from os import getenv
from dotenv import load_dotenv  # 👈 BU YANGI QATOR

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()  # 👈 BU YERDA .env faylni yuklaymiz




TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm a bot created with aiogram.")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())