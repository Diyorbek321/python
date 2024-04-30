import asyncio
import psycopg2
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ContentType
from aiogram.utils.markdown import hbold
from sqlalchemy.orm import Session

from butoon import *
from db import UserForm, engine, Base


class AplicationForm(StatesGroup):
    name = State()
    surname = State()
    birthday = State()
    Photo = State()


TOKEN = '6927897649:AAGCpwxesqpnRskShtdIqpMaV8I85isAmTY'

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await message.reply("Kerakli bo'limni tanlang", reply_markup=butoons)


@dp.message(F.text == 'Xodimlar')
async def xodimlar(message: Message, state: FSMContext) -> None:
    await message.answer("xodimning ismini kiriting")
    await state.set_state(AplicationForm.name)


@dp.message(F.content_type == ContentType.TEXT, AplicationForm.name)
async def xodimlar(message: Message, state: FSMContext) -> None:
    await message.answer('Xodimning familiyasini kiriting')
    await state.set_state(AplicationForm.surname)


@dp.message(F.content_type == ContentType.TEXT, AplicationForm.surname)
async def xodimlar(message: Message, state: FSMContext) -> None:
    await message.answer('Xodimnign tugilganyilini kiriting')
    await state.set_state(AplicationForm.birthday)


@dp.message(F.content_type == ContentType.TEXT, F.text.isdigit(), AplicationForm.birthday)
async def xodimlar(message: Message, state: FSMContext) -> None:
    await message.answer('Xodimning rasmini kiriting')
    await state.set_state(AplicationForm.Photo)


@dp.message(F.content_type == ContentType.PHOTO)
async def xodimlar(message: Message, state: FSMContext):
    await message.answer('Xodim databesga qoshildi')
    data = await state.get_data()
    name = data.get('name')
    surname = data.get('surname')
    birthday = data.get('birthday')
    photo = data.get('photo')
    with Session(engine) as session:
        user = UserForm(name=name, surname=surname, birthday=birthday, photo=photo)
        session.add(user)
        session.commit()
    await message.answer(f'{user.id}-{user.name} sizni malumotlaringiz saqlandi')


@dp.message()
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())
