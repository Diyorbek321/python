import states
from aiogram import Bot, Dispatcher, types
from asyncio import run
from aiogram.filters import Command

from aiogram.types import BotCommand

from function import userinfo, start_answer, help_answer, sign_up_age, sign_up_name

dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(955631798, "Bot ishga tushdi")


async def shutdown(bot: Bot):
    await bot.send_message(955631798, "bot ishdan toxtadi")


async def start():
    dp.startup.register(startup_answer)

    dp.message.register(start_answer, Command("start"))
    dp.message.register(help_answer, Command("help"))
    dp.message.register(sign_up_name, states.sign_up.name)
    dp.message.register(sign_up_age, states.sign_up.age)
    dp.message.register(userinfo)
    dp.shutdown.register(shutdown)
    bot = Bot('7062062786:AAG0acwkFAQoMVw7dFpH0CzWXY46ySLLVQ8', parse_mode="HTML")
    await bot.set_my_commands([
        BotCommand(command='/start', description="Botni ishga tushirish"),
        BotCommand(command='/help', description="Yordam olish")
    ])
    await dp.start_polling(bot)


run(start())
