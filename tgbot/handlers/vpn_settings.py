import logging
from typing import Dict

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiohttp import ClientConnectorError

from loader import db, bot, outline
from tgbot.keyboards.callback_data_factory import vpn_callback
from tgbot.keyboards.inline import keyboard_get_key

logger = logging.getLogger(__name__)


async def vpn_handler(message: Message):
    await bot.send_message(message.from_user.id, f'Ограничения - один ключ в одни руки',
                           reply_markup=await keyboard_get_key())


async def vpn_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id,
                           f'Выберите страну сервера',
                           reply_markup=await keyboard_get_key())


async def get_new_key(callback_query: CallbackQuery, callback_data: Dict[str, str]):
    await callback_query.answer()
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    logger.info(callback_data)
    try:
        data = await outline.create_key(await db.get_server_key(int(callback_data['server'])))
        await bot.send_message(callback_query.from_user.id,
                               f'Вставьте вашу ссылку доступа в приложение Outline:')
        await bot.send_message(callback_query.from_user.id,
                               f'{data["accessUrl"]}')
    except ClientConnectorError:
        await bot.send_message(callback_query.from_user.id,
                               f'Не удалось связаться с сервером для получения ключа, попробуйте через какое-то время')


def register_vpn_handlers(dp: Dispatcher):
    dp.register_message_handler(vpn_handler, commands=["vpn"], state="*")
    dp.register_callback_query_handler(vpn_callback_handler, vpn_callback.filter(action_type='vpn_settings'))
    dp.register_callback_query_handler(get_new_key, vpn_callback.filter(action_type='new_key'))
