# import logging
# import random
# from aiogram import Bot, Dispatcher, types, executor
# from config import token
# import geopandas as gpd
# from shapely.geometry import Point

# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# land = world[world['continent'] != 'Europe']
# land_bounds = land.bounds

# bot = Bot(token=token)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)

# inline_start_buttons = [
#     types.InlineKeyboardButton('Получить локацию', callback_data='get_location'),
#     types.InlineKeyboardButton('Получить локацию с сайта', callback_data='https://www.naturalearthdata.com/')
# ]
# inline_start_keyboard = types.InlineKeyboardMarkup().add(*inline_start_buttons)


# def generate_random_coordinates():
#     while True:
#         latitude = random.uniform(land_bounds['miny'].iloc[0], land_bounds['maxy'].iloc[0])
#         longitude = random.uniform(land_bounds['minx'].iloc[0], land_bounds['maxx'].iloc[0])
#         point = Point(float(longitude), float(latitude))  # Приведение к типу float
#         if land.geometry.contains(point).any():
#             return latitude, longitude

# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer(f"Привет {message.from_user.full_name}! Я бот, который находит случайные локации\nНажми на кнопку /send_point чтобы получить локацию.", reply_markup=inline_start_keyboard)

# @dp.callback_query_handler(lambda callback_query: callback_query.data == 'https://www.naturalearthdata.com/')
# async def get_location_from_website(callback_query: types.CallbackQuery):
#     await bot.send_message(callback_query.from_user.id, "https://www.naturalearthdata.com/")

# @dp.message_handler(commands=['send_point'])
# async def send_random_point(message: types.Message):
#     latitude, longitude = generate_random_coordinates()
#     await message.reply(f"Случайная точка на суше:\nШирота: {latitude}\nДолгота: {longitude}")


# executor.start_polling(dp, skip_updates=True)


# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.answer(f"Привет {message.from_user.full_name}! Я бот, который находит случайные локации\nНажми на кнопку /send_point чтобы получить локацию.")


# @dp.message_handler(commands=['send_point'])
# async def send_random_point(message: types.Message):
#     latitude, longitude = generate_random_coordinates()
#     await message.reply(f"Случайная точка на суше:\nШирота: {latitude}\nДолгота: {longitude}")


# executor.start_polling(dp, skip_updates=True)

import logging
import random
from aiogram import Bot, Dispatcher, types, executor
from config import token

# Функция для генерации случайных координат
def generate_random_coordinates():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return latitude, longitude

# Функция для формирования ссылки на Google Maps
def generate_google_maps_link(latitude, longitude):
    return f"https://maps.google.com/maps?q={latitude},{longitude}&ll={latitude},{longitude}&z=16"

# Инициализация бота и диспетчера
bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Обработчик команды /start
@dp.message_handler(commands='start')
async def start(message: types.Message):
    # Генерация случайных координат
    latitude, longitude = generate_random_coordinates()
    # Формирование ссылки на Google Maps
    google_maps_link = generate_google_maps_link(latitude, longitude)
    # Отправка сообщения с ссылкой и координатами
    await message.answer("Высылаю случайные координаты...")
    await message.answer("[ Геопозиция ]")
    await message.answer(google_maps_link)
    await message.answer(f"{latitude} {longitude}")

executor.start_polling(dp, skip_updates=True)
