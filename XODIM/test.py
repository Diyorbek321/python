import psycopg2
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

# PostgreSQL ma'lumotlar bazasiga ulanish
conn = psycopg2.connect(
    dbname="your_database", user="your_username", password="your_password", host="your_host"
)
cursor = conn.cursor()

# Telegram botni yaratish
bot = '6927897649:AAGCpwxesqpnRskShtdIqpMaV8I85isAmTY'
dp = Dispatcher(bot)

# Bugungi sana
today = datetime.now().date()

# Xodimlar jadvalidan bugungi tug'ilgan kuniga ishlaydiganlar ro'yxati
cursor.execute("SELECT ism, familiya, rasmi FROM Xodimlar WHERE EXTRACT(MONTH FROM tugilgan_kun) = %s AND EXTRACT(DAY FROM tugilgan_kun) = %s", (today.month, today.day))
employees_today = cursor.fetchall()

# Xabar tayyorlash va yuborish
async def send_birthday_message():
    for employee in employees_today:
        ism, familiya, rasmi = employee
        message = f"Bugun {ism} {familiya}ning tug'ilgan kunidir! Tabriklaymiz! 🥳"
        with open(rasmi, 'rb') as photo:
            await bot.send_photo(chat_id='YOUR_CHAT_ID', photo=photo, caption=message)

# Botni ishga tushirish
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Bot ishga tushdi")

# Telegram xabarlarni tekshirish va yuborish
async def scheduler():
    while True:
        if datetime.now().hour == 8 and datetime.now().minute == 0:
            await send_birthday_message()
        await asyncio.sleep(60)  # Har bir daqiqa tekshirish

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
