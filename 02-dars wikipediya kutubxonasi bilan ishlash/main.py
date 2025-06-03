# pip install aiogram wikipedia



"""
WikiBot: Telegram orqali Wikipedia'dan ma'lumot izlovchi bot
Muallif: @it_creative
Kutubxonalar: aiogram, wikipedia
"""

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import wikipedia

# Wikipedia tilini o'zbek tiliga sozlaymiz
wikipedia.set_lang("uz")

# Telegram bot token (BotFather'dan olingan tokeningizni shu yerga yozing)
API_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Bot va dispatcher obyektlarini yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    """
    /start yoki /help komandasi yuborilganda foydalanuvchiga javob beruvchi funksiya

    Args:
        message (Message): Foydalanuvchidan kelgan telegram xabari

    Returns:
        None
    """
    await message.reply(
        "Salom! 👋\n"
        "Menga istalgan mavzuni yozing (masalan: Python, Samarkand, O'zbekiston), "
        "va men sizga Wikipedia'dan qisqacha ma'lumot beraman.\n\n"
        "🧠 Misol: `Sun'iy intellekt`\n"
        "Yordam uchun: /help"
    )


@dp.message_handler()
async def wiki_search(message: Message):
    """
    Foydalanuvchi tomonidan yuborilgan matn bo‘yicha Wikipedia’da izlash va javob yuborish

    Args:
        message (Message): Telegram foydalanuvchisidan kelgan xabar

    Returns:
        None
    """
    search_text = message.text  # Foydalanuvchi yuborgan matn

    try:
        # Wikipedia'dan qisqacha izohni olish
        summary = wikipedia.summary(search_text)

        # Topilgan matnni foydalanuvchiga yuborish
        await message.reply(summary)

    except wikipedia.exceptions.PageError:
        # Mavzu topilmagan holat
        await message.reply("Kechirasiz, bu mavzu bo‘yicha hech narsa topilmadi. ❌")

    except wikipedia.exceptions.DisambiguationError as e:
        # Juda ko'p variantlar mavjud bo‘lsa (noaniqlik)
        options = "\n".join(e.options[:5])
        await message.reply(f"Bu so'z bir nechta ma'noga ega:\n\n{options}\n\nAniqroq yozing.")

    except Exception as e:
        # Boshqa xatoliklar
        await message.reply(f"Xatolik yuz berdi: {e}")


if __name__ == "__main__":
    """
    Botni ishga tushurish uchun asosiy blok.
    skip_updates=True — eski xabarlarni ko'rmaslik uchun
    """
    executor.start_polling(dp, skip_updates=True)
