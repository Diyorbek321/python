import asyncio
import asyncpg
import csv
import os
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ContentType
from aiogram.utils.markdown import hbold
from sqlalchemy.orm import Session
from db import UserForm, engine
from dotenv import load_dotenv


async def retrieve_data_from_postgres():
    # Connect to PostgreSQL database
    conn = await asyncpg.connect(user='posgres', password='2005',
                                 database='postgres', host='5432')

    # Execute query to retrieve data
    data = await conn.fetch("SELECT * FROM users")

    # Close database connection
    await conn.close()

    return data


async def send_csv_to_user():
    # Retrieve data from PostgreSQL
    data = await retrieve_data_from_postgres()

    # Format data as CSV
    csv_data = '\n'.join([','.join(map(str, row)) for row in data])

    # Send CSV data to the user
    return  csv_data

file = send_csv_to_user()

class ApplicationForm(StatesGroup):
    name = State()
    surname = State()
    birth_city = State()


load_dotenv()
TOKEN = os.getenv('TOKEN')
dp = Dispatcher()


@dp.message(F.text == 'admin')
async def admin(message: Message):
    await message.answer_document(f'{file}')


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await message.reply("Ismingizni kiriting")
    await state.set_state(ApplicationForm.name)


@dp.message(F.content_type == ContentType.TEXT, ApplicationForm.name)
async def set_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await message.answer("Familiya kiriting")
    await state.set_state(ApplicationForm.surname)


@dp.message(F.content_type == ContentType.TEXT, ApplicationForm.surname)
async def set_surname(message: Message, state: FSMContext) -> None:
    await state.update_data(surname=message.text)
    await message.answer('Tugilgan hududingiz')
    await state.set_state(ApplicationForm.birth_city)


@dp.message(F.content_type == ContentType.TEXT, ApplicationForm.birth_city)
async def set_birth_city(message: Message, state: FSMContext):
    await state.update_data(birth_city=message.text)
    data = await state.get_data()
    name = data.get('name')
    surname = data.get('surname')
    birth_city = data.get('birth_city')

    with Session(engine) as session:
        user = UserForm(name=name, surname=surname, birth_city=birth_city)
        session.add(user)
        session.commit()
        await message.answer(f'{user.name} sizni malumotlaringiz saqlandi')
    await state.clear()


@dp.message()
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
