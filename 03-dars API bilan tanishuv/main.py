# Kerakli kutubxona: pip install openai==0.28.0 aiogram==2.25.1 python-dotenv
import logging
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# .env fayldan ma'lumotlarni yuklash
load_dotenv()

# API kalitlar
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI sozlash
openai.api_key = OPENAI_API_KEY

# Aiogram konfiguratsiyasi
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# /start komandasi
@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    await message.reply("Assalomu alaykum! Menga savolingizni yozing. Men OpenAI yordamida javob beraman.")

# Matnli so'rovlar uchun handler
@dp.message_handler()
async def ask_openai(message: Message):
    user_input = message.text

    try:
        # OpenAI API chaqiruv
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # yoki gpt-4 agar sizda mavjud bo‘lsa
            messages=[
                {"role": "system", "content": "Siz foydalanuvchiga yordam beruvchi Telegram botisiz."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=1000,
            temperature=1.5,
        )
        
        reply = response["choices"][0]["message"]["content"]
        await message.reply(reply)

    except Exception as e:
        await message.reply("Xatolik yuz berdi: " + str(e))

# Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



# Rasm yuborish
# https://api.telegram.org/bot8083728455:AAFdKBNykypbOpipRgLpZEZXsjEnKy2n8B4/sendPhoto?chat_id=7336586209&photo=https://ubuntu.com/wp-content/uploads/c9f4/visualstudio_code-card.png
# Matin yozish
# https://api.telegram.org/bot8083728455:AAFdKBNykypbOpipRgLpZEZXsjEnKy2n8B4/sendMessage?chat_id=7336586209&text=Salom%20dunyo
