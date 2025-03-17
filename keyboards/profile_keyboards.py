from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def yes_or_no_kb():
    kb = [
        [
            InlineKeyboardButton(text="Да", callback_data="yes_change"),
            InlineKeyboardButton(text="Нет", callback_data="no_not_change")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard


async def change_back_kb():
    kb = [
        [
            InlineKeyboardButton(text="Назад", callback_data="profile")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)
    return keyboard

