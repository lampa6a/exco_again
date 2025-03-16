import asyncio
import logging
from datetime import datetime
from config_reader import config
from magic_filter import F
    
from aiogram import Bot, Dispatcher
from aiogram.filters.command import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config_reader

# Для записей с типом Secret* необходимо 
# вызывать метод get_secret_value(), 
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value(),
            default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            )
        )

logging.basicConfig(level=logging.INFO)
# Диспетчер
dp = Dispatcher()  

dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

start_button_dict = {
    'Профиль': 'profile',
    'Банк': 'bank',
    'магазин': 'shop',
                    }

@dp.message(CommandStart())
async def start_keyboard(message: Message):
    builder = InlineKeyboardBuilder()
    for i, (key, value) in enumerate(start_button_dict.items()):
        builder.button(text=key, callback_data=value)
       
    builder.adjust(2)
    await message.answer('Вот клавиатура:', 
                         reply_markup=builder.as_markup())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен с клавиатуры')