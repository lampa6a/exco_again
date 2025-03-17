from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from keyboards.start_keyboards import start_kb_gen
from profile_text import text
from keyboards.profile_keyboards import change_back_kb, yes_or_no_kb
from handlers.start_handlers import photo_ids, profile_button


rt = Router()


@rt.callback_query(F.data == "back_for_profile")
async def back_profile(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Вот клавиатура:', reply_markup=await start_kb_gen())
    await callback.answer()

@rt.callback_query(F.data == "change_profile")
async def back_profile(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        'Вы хотите изменить ник?',
        reply_markup=await yes_or_no_kb())
    await callback.answer()
    
@rt.callback_query(F.data == "yes_change")
async def answer_yes(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
                            "На какой ник будете менять?", 
                            reply_markup=await change_back_kb())
    await callback.answer()
    
@rt.callback_query(F.data == "no_not_change")
async def answer_no(callback: CallbackQuery):
    await callback.message.delete()
    await profile_button(callback)
    await callback.answer()
