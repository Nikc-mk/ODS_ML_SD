from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram import types

start_buttons = ["Информация о боте", "Загрузить фото"]


async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='Нажмите на кнопку ☟')
    # клавиатура при старте
    name_user = message.from_user.first_name  # получаем имя пользователя
    keyboard.add(*start_buttons)
    await message.answer(f"Привет🙋, {name_user}!\nЯ бот. Ниже указаны команды, которые, я могу выполнять\n",
                         reply_markup=keyboard)
    # отвечаем пользователю после старта


def register_handlers_users(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
