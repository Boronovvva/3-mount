from aiogram import Bot, Dispatcher, types, executor
from config import token  
import logging, random 
import geopandas as gpd  
from shapely.geometry import Point  

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

land = world[world['continent'] != 'Europe']
land_bounds = land.bounds

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

inline_start_buttons = [
    types.InlineKeyboardButton('Получить локацию', callback_data='get_location'),
    types.InlineKeyboardButton('Наш сайт', url='https://www.naturalearthdata.com/')
]
inline_start_keyboard = types.InlineKeyboardMarkup().add(*inline_start_buttons)

# Функция для генерации случайных координат на суше
# def generate_random_coordinates():
#     while True:
#         latitude = random.uniform(-180.000000, 180.000000)
#         longitude = random.uniform(-90.000000, 90.000000)
#         point = Point(float(longitude), float(latitude))  # Приведение к типу float
#         if land.geometry.contains(point).any():
#             return latitude, longitude

# Обработчик команды /start
@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"Привет {message.from_user.full_name}! Я бот,который находит случайные локации\nНажми на кнопку получить локацию.", reply_markup=inline_start_keyboard)

@dp.callback_query_handler(lambda call: call.data == "get_location")
async def send_random_location(callback: types.CallbackQuery): 
    latitude = random.uniform(-180.000000, 180.000000)
    longitude = random.uniform(-90.000000, 90.000000)
    # longitude, latitude = generate_random_coordinates()
    await callback.message.answer("Высылаю случайные координаты... ")
    await callback.message.answer_location(longitude=longitude, latitude=latitude)
    await callback.message.answer(f'{latitude} {longitude}', reply_markup=inline_start_keyboard)

executor.start_polling(dp, skip_updates=True)
