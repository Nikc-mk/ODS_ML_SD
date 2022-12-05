from time import sleep
from models.model_1_opencv import change_photo
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram import types
from aiogram.types import ContentType

from creat_bot import bot

start_buttons = ["Информация о боте", "Загрузить фото"]


async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='Нажмите на кнопку ☟')
    # клавиатура при старте
    name_user = message.from_user.first_name  # получаем имя пользователя
    keyboard.add(*start_buttons)
    await message.answer(f"Привет🙋, {name_user}!\nЯ бот. Ниже указаны команды, которые, я могу выполнять\n",
                         reply_markup=keyboard)
    # отвечаем пользователю после старта


async def cmd_download(message: types.Message):
    name_user = message.from_user.first_name
    await message.answer(f"{name_user} отправьте мне фотографию с людьми, я их обработаю и верну вам")


async def cmd_media(message: types.Message):
    name_user = message.from_user.first_name
    # file_id = message.photo[-1].file_id
    # print(file_id)
    # file = await bot.get_file(file_id)
    # file_path = file.file_path
    # image_name = f"{file_id}.jpg"
    # await bot.download_file(file_path=file_path, destination=f"models/download_photo/{image_name}", timeout=5)
    # sleep(20)
    try:
        change_photo()
    except: Exception
    await message.answer(f"{name_user} отправил фото")



# отвечаем на все неизвестные сообщения
async def cmd_answer_all(message: types.Message):
    await message.answer('Не знаю такой команды.\nВоспользуйтесь командой /start')


def register_handlers_users(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_download, commands='download')
    dp.register_message_handler(cmd_download, Text(equals=start_buttons[1], ignore_case=True))
    dp.register_message_handler(cmd_media, content_types=ContentType.PHOTO)
    dp.register_message_handler(cmd_answer_all)
