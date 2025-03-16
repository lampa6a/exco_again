from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

start_button_dict = {
    'Профиль': 'profile',
    'Банк': 'bank',
    'магазин': 'shop',
                    }

async def start_kb_gen():
    builder = InlineKeyboardBuilder()
    for i, (key, value) in enumerate(start_button_dict.items()):
        builder.button(text=key, callback_data=value)
    builder.adjust(2)
    return builder.as_markup()

async def profile_back_kb():
    kb = [
        [
            InlineKeyboardButton(text="Назад", callback_data="back"),
            InlineKeyboardButton(text="Изменить", callback_data="change")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard