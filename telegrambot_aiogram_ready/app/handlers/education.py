from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from app.texts.about import ABOUT_TEXT

router = Router()

# Кнопки
def education_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Что такое Algo Hub?", callback_data="about")],
        [InlineKeyboardButton(text="Модуль 1", callback_data="mod_1")],
        [InlineKeyboardButton(text="Модуль 2", callback_data="mod_2")],
        [InlineKeyboardButton(text="Модуль 3", callback_data="mod_3")],
        [InlineKeyboardButton(text="Модуль 4", callback_data="mod_4")],
        [InlineKeyboardButton(text="Модуль 5", callback_data="mod_5")],
        [InlineKeyboardButton(text="Модуль 6", callback_data="mod_6")],
        [InlineKeyboardButton(text="Модуль 7", callback_data="mod_7")],
    ])

@router.message(F.text == "🎓 Обучение")
async def show_topics(message: Message):
    await message.answer("Выберите тему:", reply_markup=education_keyboard())

@router.callback_query(F.data == "about")
async def show_about(callback: CallbackQuery):
    await callback.message.edit_text(ABOUT_TEXT, parse_mode="Markdown")
    await callback.answer()

@router.callback_query(F.data.startswith("mod_"))
async def show_module(callback: CallbackQuery):
    mod = callback.data.split("_")[1]
    await callback.message.edit_text(f"Здесь будет Модуль {mod}.", parse_mode="Markdown")
    await callback.answer()
