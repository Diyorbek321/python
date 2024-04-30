from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import BotCommand
from function import start_command_answer, help_command_answer

dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(955631798, "Bot ishga tushdi")


async def shutdown(bot:Bot):
    await bot.send_message(955631798, "Bot ishdan toxtadi")


async def start():
    dp.message.register(startup_answer)
    dp.message.register(start_command_answer, Command("start"))
    dp.message.register(help_command_answer, Command("help"))
    dp.message.register(shutdown)

    bot = Bot("6927897649:AAGCpwxesqpnRskShtdIqpMaV8I85isAmTY", parse_mode='HTML')
    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/help", description="Bot commandalari"),
        BotCommand(command="/new", description="Yangi ariza"),
        BotCommand(command="/stop", description="Arizani to'xtatish")
    ])
    await dp.start_polling(bot, polling_timeout=1)


run(start())
