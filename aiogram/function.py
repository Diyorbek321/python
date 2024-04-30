from aiogram import Bot
from aiogram import types
from aiogram.types import Message
from states import sign_up
from aiogram.fsm.context import FSMContext


async def userinfo(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    photo = await message.from_user.get_profile_photos()
    matn = (f'{message.from_user.mention_html("User info")}: \n\n'
            f'Name: {message.from_user.full_name}\n'
            f'ID: {message.from_user.id}')
    if user.bio: matn += f'\nBio: {user.bio}'
    if message.from_user.username: matn += f'\nUsername: @{message.from_user.username}'
    if photo.photos:
        await message.answer_photo(photo.photos[0][-1].file_id, caption=matn)
    else:
        await message.answer(matn, parse_mode="HTML")


async def start_answer(message: Message, bot: Bot, state: FSMContext):
    await message.answer("salom izmingizni kiriting")
    await state.set_state(sign_up.name)
    # await bot.send_message(message.from_user.id,
    #                        f'Hello {message.from_user.mention_html(f'{message.from_user.first_name}')}',parse_mode="HTML")


async def help_answer(message: Message, bot: Bot):
    matn = f'''
        bot buyuruqlari
        /start - start
        /help - help
        '''
    await bot.send_message(message.from_user.id, matn, parse_mode="HTML")


async def sign_up_name(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Yoshingizni kiriting")
    await state.set_state(sign_up.age)


async def sign_up_age(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await message.answer(f'''Malumotlarizngiz 
    Ismingiz: {data.get('name')}
    Yoshingiz: {message.text}''')
    await state.clear()
