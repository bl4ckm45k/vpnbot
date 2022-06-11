import logging

from aiogram import Dispatcher
from aiogram.types import Message

logger = logging.getLogger(__name__)


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["admin"], state="*", is_admin=True)
