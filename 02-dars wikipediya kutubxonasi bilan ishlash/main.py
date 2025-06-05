# pip install aiogram wikipedia

"""
Wikipedia Telegram Bot (Aiogram 3.x uchun)
Muallif: @it_creative
Mentor: Suyunov Husan
📌 Ushbu bot foydalanuvchi yuborgan mavzu bo‘yicha Wikipedia'dan qisqacha ma'lumot topadi va jo‘natadi.
"""

import asyncio
import wikipedia
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties  # ✅ Yangi aiogram uchun kerak

# Wikipedia tilini o'zbek tiliga sozlaymiz
wikipedia.set_lang("uz")

# Bot tokeningizni shu yerga yozing
API_TOKEN = "8083728455:AAFdKBNykypbOpipRgLpZEZXsjEnKy2n8B4"  # ❗ E'tibor: tokenni GitHub yoki YouTube'ga oshkor qilmang

# ✅ Bot obyektini yaratamiz (ParseMode.HTML endi `default` orqali uzatiladi)
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# Dispatcher - botga kelgan xabarlarni boshqaradi
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    """
    /start komandasi yuborilganda ishga tushadi.
    
    Args:
        message (Message): Foydalanuvchidan kelgan Telegram xabari
    """
    await message.answer(
        f"Salom {hbold(message.from_user.full_name)}! 👋\n"
        "Menga istalgan mavzuni yozing va men Wikipedia'dan ma'lumot topib beraman.\n\n"
        "🧠 Misol: Python, O'zbekiston, Samarkand"
    )


@dp.message()
async def wiki_handler(message: Message):
    """
    Foydalanuvchi yuborgan matn bo‘yicha Wikipedia’da izlab, natijani qaytaradi.

    Args:
        message (Message): Foydalanuvchidan kelgan xabar
    """
    query = message.text  # Izlanayotgan matn

    try:
        result = wikipedia.summary(query)  # Wikipedia'dan qisqacha matn
        await message.answer(result)

    except wikipedia.exceptions.DisambiguationError as e:
        # Bir nechta ma'noli maqolalar topilsa
        variants = "\n".join(e.options[:5])
        await message.answer(
            f"Bu so‘z bir nechta ma'noga ega:\n{variants}\n\n"
            "Iltimos, mavzuni aniqroq yozing. 🔍"
        )

    except wikipedia.exceptions.PageError:
        # Maqola topilmasa
        await message.answer("Kechirasiz, bu mavzu bo‘yicha hech narsa topilmadi. ❌")

    except Exception as err:
        # Kutilmagan xatoliklar
        await message.answer(f"Xatolik yuz berdi: {err}")


async def main():
    """
    Botni ishga tushiruvchi asosiy funksiya
    """
    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)


# Dastur boshlanishi
if __name__ == "__main__":
    asyncio.run(main())
