from creat_bot import dp
from handlers import main_handlers
from aiogram import executor


try:
    main_handlers.register_handlers_users(dp)
except Exception as ex:
    print(ex)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)