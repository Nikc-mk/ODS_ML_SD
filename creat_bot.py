import telebot
import logging
import botconfig


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = telebot.TeleBot(botconfig.API_TOKEN, parse_mode=None)