import asyncio
import logging
from datetime import datetime
from config_reader import config
from magic_filter import F
    
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from handlers import starthandlers

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
dp.include_router(starthandlers.rt)
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен с клавиатуры')