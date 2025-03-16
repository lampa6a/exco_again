from aiogram.types import CallbackQuery, URLInputFile
from aiogram import Router
from aiogram import F
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from keyboards.start_keyboard import start_kb_gen, profile_back_kb

rt = Router()

text = (
"Ваш профиль:\n"
"Ник: username\n"
"Статус:\n"
"Дата регистрации: DD.MM.YYYY"
)

@rt.message(CommandStart())
async def start_keyboard(message: Message):
    keyboard = await start_kb_gen()
    await message.answer('Вот клавиатура:', reply_markup=keyboard)


@rt.callback_query(F.data=="profile")
async def profile_button(callback: CallbackQuery):
    result: None | str = None
    photo_path = "https://avatars.mds.yandex.net/i?id=7ff07b7f29c84fa946492a15c7b7bdf7_l-4965727-images-thumbs&n=13"
    photo = URLInputFile(photo_path)
    if result is not None:
        await callback.message.answer_photo(
                photo=result.photo[-1].file_id,
                caption=text,
                parse_mode="Markdown",
                reply_markup=await profile_back_kb()
         )
    else:
        result = await callback.message.answer_photo(
                photo=photo,
                caption=text,
                parse_mode="Markdown",
                reply_markup=await profile_back_kb()
        )
    await callback.answer()


