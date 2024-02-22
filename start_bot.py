# from aiogram import Bot, Dispatcher, types, executor
# from config import token 

# bot = Bot(token=token)
# dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer("Привет мир! Привет Geeks!")

# @dp.message_handler(commands='help')
# async def help(message:types.Message):
#     await message.answer("Чем я могу вам помочь?")

# @dp.message_handler(text="Geeks")
# async def geeks(message:types.Message):
#     await message.reply("Geeks - это айти курсы в Кыргызстане")

# @dp.message_handler(text="Привет")
# async def hello(message:types.Message):
#     await message.reply("Привет, как дела")

# @dp.message_handler(commands='test')
# async def test(message:types.Message):
#     await message.answer_photo('https://autonews.mowval.com/images/slider/b8affd3f422f706d103efa304dc3528e1456838101.jpg')
#     await message.answer_location(40.51931603792678, 72.80298388177104)
    
# @dp.message_handler()
# async def not_found(message:types.Message):
#     await message.reply("Я вас не понял, введите /help")

# executor.start_polling(dp)