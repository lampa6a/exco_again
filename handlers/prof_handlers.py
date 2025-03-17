from aiogram import Router
from aiogram.types import CallbackQuery, Message

from keyboards.start_keyboard import start_kb_gen, yes_or_no_kb, profile_back_kb
from profile_text import text
from keyboards.profile_nick_change_kb import change_back_kb
from handlers.start_handlers_with_problems import photo_ids

rt = Router()


@rt.callback_query(callback_data="back_to_profile")
async def back_profile(message: Message):
    keyboard = await start_kb_gen()
    await message.answer('Вот клавиатура:', reply_markup=keyboard)


@rt.callback_query(callback_data="change_profile")
async def back_profile(message: Message):
    keyboard = await yes_or_no_kb()
    await message.answer('Вы хотите изменить username?', reply_markup=keyboard)

@rt.callback_query(callback_data="no")
async def answer_no(callback: CallbackQuery):
    
    await callback.message.answer_photo(
            photo=photo_ids[0],
            caption=text,
            parse_mode="Markdown",
            reply_markup=await profile_back_kb()
        )
    
@rt.callback_query(callback_data="yes")
async def answer_yes(message: Message):
    message.answer("На какой ник будете менять?", reply_markup=change_back_kb())
    

