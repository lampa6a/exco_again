from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def change_back_kb():
    kb = [
        [
            InlineKeyboardButton(text="Назад", callback_data="back_to_profile")
        ]
    ]
    keyboard = InlineKeyboardMarkup(keyboard=kb)
    return keyboard
