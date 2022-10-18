import logging
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv("../.env")
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=os.environ.get("TELEGRAM_API_TOKEN"))
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    executor.start_polling(dp, skip_updates=True)
