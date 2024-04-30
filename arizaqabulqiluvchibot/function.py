from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Bot


async def start_command_answer(bot: Bot, message: Message):
    await message.answer("Assalomu aleykum , botdan foydalanishni bilmasangiz /help buyrugini yuboring")

async def help_command_answer(bot: Bot, message: Message):
    matn = """
    bot buyuruqlari
    /start - ishga tushirish
    /new - Yangi ariza yuborish
    /stop -ariza yuborishni to'xtatish"""
    await bot.send_message(message.from_user.id, matn, parse_mode='HTML')