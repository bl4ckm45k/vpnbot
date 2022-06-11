from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from config import load_config
from db_api import Database
from outline.base import OutlineManager

db = Database()
c = load_config(".env")
bot = Bot(token=c.tg_bot.token, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2()
dp = Dispatcher(bot, storage=storage)
outline = OutlineManager()
