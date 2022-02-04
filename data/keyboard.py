from aiogram.types import KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

main_inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="✳ Сдать батарейки", callback_data="1")
).add(
    KeyboardButton(text="✳ Сдать Раздельный мусор", callback_data="2")
).add(
    KeyboardButton(text="✳ Сдать стекло", callback_data="3")
).add(
    KeyboardButton(text="✳ Сдать макулатуру", callback_data="4")
)

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="📜 Главное меню", callback_data="5")
)

send_location = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    KeyboardButton(text="🌐 Поделится моим местоположением", request_location=True)
)
