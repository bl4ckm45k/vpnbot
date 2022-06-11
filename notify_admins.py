from aiogram import Dispatcher
from aiogram.types import BotCommand
from loader import c


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(c.tg_chats.debug_chat, "Бот запущен")
    await dp.bot.set_my_commands([
        BotCommand('start', 'Запустить бота'),
        BotCommand('vpn', 'Доступ к VPN')
    ])