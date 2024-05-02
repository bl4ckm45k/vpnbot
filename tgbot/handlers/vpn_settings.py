import asyncio
import uuid
from datetime import datetime, timedelta

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import bot
from marzban.client import create_user, get_user_links

vpn_router = Router()


@vpn_router.message(Command('vpn'))
async def vpn_handler(message: Message):
    sub_id = str(uuid.uuid4())
    result = await asyncio.gather(create_user(sub_id, datetime.now() + timedelta(days=3660)))
    if result:
        keys = await get_user_links(sub_id)
        await bot.send_message(message.from_user.id, f'Ваши ключи для подключения:\n\n{keys}')


@vpn_router.callback_query(F.data == 'vpn')
async def vpn_callback_handler(callback_query: CallbackQuery):
    sub_id = str(uuid.uuid4())
    result = await asyncio.gather(create_user(sub_id, datetime.now() + timedelta(days=3660)))
    if result:
        keys = await get_user_links(sub_id)
        await bot.send_message(callback_query.from_user.id, f'Ваши ключи для подключения:\n\n{keys}')
