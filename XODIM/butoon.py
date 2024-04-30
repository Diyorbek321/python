from aiogram import types

button = [
    [
        types.KeyboardButton(text='Lavozimlar'),
        types.KeyboardButton(text='Xodimlar')
    ]
]
butoons = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
lavozimlar = [
    [types.KeyboardButton(text='Muhandis'),
     types.KeyboardButton(text='Direktor'),
     types.KeyboardButton(text='Buxgalter')
     ]
]
lavozim = types.ReplyKeyboardMarkup(keyboard=lavozimlar, resize_keyboard=True)
xodim = [
    [types.KeyboardButton(text='Xodim qoshish')]
]
xodimlar = types.ReplyKeyboardMarkup(keyboard=xodim, resize_keyboard=True)


