import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ChatType
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from loader import config
from tgbot.handlers import routers_list
from tgbot.middlewares.flood import ThrottlingMiddleware
from utils import broadcaster

logger = logging.getLogger(__name__)


async def on_startup(bot: Bot):
    await broadcaster.broadcast(bot, [config.tg_bot.admin_id], "Бот запущен")
    await register_commands(bot)
    if config.webhook.use_webhook:
        await bot.set_webhook(f"https://{config.webhook.domain}{config.webhook.url}webhook")


async def register_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Главное меню 🏠'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='vpn', description='Получить ключи'),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


def register_global_middlewares(dp: Dispatcher):
    """
    Register global middlewares for the given dispatcher.
    Global middlewares here are the ones that are applied to all the handlers (Specify for the type of update)

    :param dp: The dispatcher instance.
    :type dp: Dispatcher
    :param config: The configuration object from the loaded configuration
    :return: None
    """

    middleware_types = [
        ThrottlingMiddleware(),
    ]
    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)
    dp.callback_query.outer_middleware(CallbackAnswerMiddleware())
    dp.message.filter(F.chat.type == ChatType.PRIVATE)


def main_webhook():
    from loader import bot, dp

    dp.include_routers(*routers_list)
    dp.startup.register(on_startup)
    register_global_middlewares(dp)

    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        # secret_token=WEBHOOK_SECRET,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=f'{config.webhook.url}webhook')

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host='vpn_bot', port=config.tg_bot.port)


async def main_polling():
    from loader import bot, dp
    dp.include_routers(*routers_list)

    register_global_middlewares(dp)
    await on_startup(bot)
    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == '__main__':
    if config.webhook.use_webhook:
        main_webhook()
    else:
        try:
            asyncio.run(main_polling())
        except (KeyboardInterrupt, SystemExit):
            logging.error("Бот выключен!")
