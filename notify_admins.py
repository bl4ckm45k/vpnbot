from aiogram import Dispatcher

from loader import c


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(c.tg_chats.debug_chat, "Бот запущен")
