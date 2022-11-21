from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import load_config
from db_api import Database
from outline.base import OutlineManager


config = load_config()
db = Database(
    username=config.db.user,
    password=config.db.password,
    host=config.db.host,
    database=config.db.database,
    port=config.db.port)
bot = Bot(token=config.tg_bot.token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
outline = OutlineManager()
