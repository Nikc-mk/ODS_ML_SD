import telebot
from creat_bot import bot
from models.func_2 import change_photo_2

start_buttons = ["Информация о боте", "Загрузить фото"]


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['photo'])
def handle_docs_audio(message: telebot.types.Message):
    file_id = message.photo[-1].file_id
    file = bot.get_file(file_id=file_id)
    file_path = file.file_path
    image_name = f"{file_id}.jpg"
    downloaded_file = bot.download_file(file_path=file_path)
    with open("models/download_photo/" + image_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    change_photo_2(image_name=image_name)
    bot.reply_to(message, text="Фото получено")
    with open(f"models/save_photo/out{image_name}", "rb") as photo:
        bot.send_photo(chat_id=message.chat.id, photo=photo)
