import logging

from aiogram.utils.executor import start_webhook

from loader import bot, c
from notify_admins import on_startup_notify
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.error_handler import register_error_handler
from tgbot.handlers.user import register_user
from tgbot.handlers.vpn_settings import register_vpn_handlers
from tgbot.middlewares.db import DbMiddleware

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_error_handler(dp)
    register_vpn_handlers(dp)


async def on_startup(dispatcher):
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    bot['config'] = c

    register_all_middlewares(dispatcher)
    register_all_filters(dispatcher)
    register_all_handlers(dispatcher)
    data = await bot.get_me()
    print(data)
    await bot.set_webhook(f"https://29cb-79-139-133-121.ngrok.io/vincent/vpn/bot")
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    logging.warning('Shutting down..')
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

    logging.warning('Bye!')
    await dispatcher.bot.close()


if __name__ == '__main__':
    from loader import dp

    start_webhook(dispatcher=dp, webhook_path=f'/vincent/vpn/bot', on_startup=on_startup,
                  on_shutdown=on_shutdown,
                  skip_updates=True, host=c.tg_bot.ip, port=c.tg_bot.port)
