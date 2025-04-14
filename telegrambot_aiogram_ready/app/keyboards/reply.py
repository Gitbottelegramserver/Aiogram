from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="📚 Курсы")
    builder.button(text="🎓 Обучение")
    builder.button(text="💰 Оплата")
    builder.button(text="🛠 Поддержка")
    builder.button(text="👤 Профиль")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
