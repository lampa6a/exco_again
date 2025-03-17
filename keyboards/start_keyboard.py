from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from profile_text import start_button_dict


async def start_kb_gen():
    builder = InlineKeyboardBuilder()
    for i, (key, value) in enumerate(start_button_dict.items()):
        builder.button(text=key, callback_data=value)
    builder.adjust(2)
    return builder.as_markup()

async def profile_back_kb():
    kb = [
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_profile"),
            InlineKeyboardButton(text="Изменить", callback_data="change_profile")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard

async def yes_or_no_kb():
    kb = [
        [
            InlineKeyboardButton(text="Да", callback_data="yes"),
            InlineKeyboardButton(text="Нет", callback_data="no")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard