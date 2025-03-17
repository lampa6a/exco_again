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
            InlineKeyboardButton(text="Назад", callback_data="back_for_profile"),
            InlineKeyboardButton(text="Изменить", callback_data="change_profile")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard

