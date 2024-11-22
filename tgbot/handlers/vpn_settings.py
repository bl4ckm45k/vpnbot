import asyncio
import uuid
from datetime import datetime, timedelta

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import bot
from marzban.client import create_user, get_user_links, get_marz_user

vpn_router = Router()

async def get_links(user_id):
    marz_user = await get_marz_user(user_id)

@vpn_router.message(Command('vpn'))
async def vpn_handler(message: Message):
    keys = await get_user_links(str(message.from_user.id))
    await bot.send_message(message.from_user.id, f'Ваши ключи для подключения:\n\n{keys}')


@vpn_router.callback_query(F.data == 'vpn')
async def vpn_callback_handler(callback_query: CallbackQuery):
    keys = await get_user_links(str(callback_query.from_user.id))
    await bot.send_message(callback_query.from_user.id, f'Ваши ключи для подключения:\n\n{keys}')
