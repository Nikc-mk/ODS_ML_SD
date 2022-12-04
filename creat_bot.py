from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import logging
import botconfig


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=botconfig.API_TOKEN)
dp = Dispatcher(bot)