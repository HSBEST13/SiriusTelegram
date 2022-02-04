import random
from aiogram.utils import executor
from aiogram import Dispatcher, Bot, types
from data.config import *
from data.locations_worker import LocationsDb, select_best_location
from data.keyboard import main_inline_keyboard, send_location


bot = Bot(TOKEN)
dp = Dispatcher(bot)
locate_db = LocationsDb()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="Привет! я подскажу тебе где ближе всего:",
                           reply_markup=main_inline_keyboard)
    print(message.from_user.id, message.from_user.full_name)


@dp.message_handler(content_types=["location"])
async def handle_location(message: types.Message):
    print(message.location.latitude, message.location.longitude)
    best_lat_lon, name, address = select_best_location(message.location.latitude,
                                                       message.location.longitude,
                                                       locate_db.select_category(CATEGORY))
    await bot.send_message(message.from_user.id, text=f"🏠 Адрес: {address}\n🔎 Название организации: {name}")
    await bot.send_message(message.from_user.id, text=f"И помни:\n{random.choice(QUOTES)}")


@dp.callback_query_handler(text="1")
async def select_batteries(callback: types.CallbackQuery):
    global CATEGORY
    CATEGORY = "batteries"
    await bot.send_message(callback.from_user.id, text="📩 Отлично, осталось "
                           "только поделится своим местоположением",
                           reply_markup=send_location)


@dp.callback_query_handler(text="2")
async def select_waist(callback: types.CallbackQuery):
    global CATEGORY
    CATEGORY = "waist"
    await bot.send_message(callback.from_user.id, text="📩 Отлично, осталось "
                           "только поделится своим местоположением",
                           reply_markup=send_location)


@dp.callback_query_handler(text="3")
async def select_glass(callback: types.CallbackQuery):
    global CATEGORY
    CATEGORY = "glass"
    await bot.send_message(callback.from_user.id, text="📩 Отлично, осталось "
                           "только поделится своим местоположением",
                           reply_markup=send_location)


@dp.callback_query_handler(text="4")
async def select_paper(callback: types.CallbackQuery):
    global CATEGORY
    CATEGORY = "paper"
    await bot.send_message(callback.from_user.id, text="📩 Отлично, осталось "
                           "только поделится своим местоположением",
                           reply_markup=send_location)


@dp.callback_query_handler(text="5")
async def main_keyboard(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text="Главное меню", reply_markup=main_inline_keyboard)


if __name__ == "__main__":
    executor.start_polling(dp)
