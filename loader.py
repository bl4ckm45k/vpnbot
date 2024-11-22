import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import load_config
from marzban.init_client import MarzClientCache
from utils.logger import APINotificationHandler

config = load_config()


def setup_logging():
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=log_level,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger_init = logging.getLogger(__name__)
    api_handler = APINotificationHandler(config.tg_bot.token, config.tg_bot.admin_id)
    api_handler.setLevel(logging.ERROR)  # Установка уровня логирования ERROR для обработчика API
    logger_init.addHandler(api_handler)

    return logger_init


logger = setup_logging()
bot = Bot(token=config.tg_bot.token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML, link_preview_is_disabled=True))

dp = Dispatcher(storage=MemoryStorage())
# base_url = f'https://{config.webhook.domain}/' if config.webhook.use_webhook else
marzban_client = MarzClientCache('http://marzban:8002', config, logger)
