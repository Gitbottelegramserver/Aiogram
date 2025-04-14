from aiogram import Router, F
from aiogram.types import Message
from app.keyboards.reply import main_menu
from aiogram.utils.markdown import hbold

router = Router()

@router.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer("Добро пожаловать в *ALGO HUB!*", reply_markup=main_menu())

@router.message(F.text == "📚 Курсы")
async def courses(message: Message):
    await message.answer("Вот список доступных курсов: Введение, DeFi, NFT, Торговля, Аналитика")

@router.message(F.text == "💰 Оплата")
async def payment(message: Message):
    await message.answer(
        "*💸 Доступные способы оплаты:*

"
        "📌 USDT (TRC20): `T1234567890`
"
        "🏦 Банк: KASPI
"
        "💳 Карта: `4400 4301 1234 5678`
"
        "👤 Получатель: Александр

"
        "После оплаты пришлите скрин в поддержку.",
        parse_mode="Markdown"
    )

@router.message(F.text == "🛠 Поддержка")
async def support(message: Message):
    await message.answer("По всем вопросам — @support_username")

@router.message(F.text == "👤 Профиль")
async def profile(message: Message):
    await message.answer(f"Ваш ID: `{message.from_user.id}`\nИмя: {hbold(message.from_user.full_name)}")
