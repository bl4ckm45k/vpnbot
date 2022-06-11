import logging
from typing import Dict

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from loader import db, bot, outline
from tgbot.keyboards.callback_data_factory import vpn_callback
from tgbot.keyboards.inline import keyboard_get_key, keyboard_delete_and_get

logger = logging.getLogger(__name__)


async def vpn_handler(message: Message):
    active, server_id = await db.select_active(message.from_user.id)
    if active:
        await bot.send_message(message.from_user.id, f'У вас уже есть действующий ключ доступа.\n'
                                                     f'{await db.get_server(server_id)}',
                               reply_markup=keyboard_delete_and_get())
    else:
        await bot.send_message(message.from_user.id, f'Ограничения - один ключ в одни руки',
                               reply_markup=await keyboard_get_key())


async def vpn_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    active, server_id = await db.select_active(callback_query.from_user.id)
    if active:
        await bot.send_message(callback_query.from_user.id,
                               f'У вас уже есть действующий ключ доступа.\n'
                               f'{await db.get_server(server_id)}',
                               reply_markup=keyboard_delete_and_get())
    else:
        await bot.send_message(callback_query.from_user.id,
                               f'Ограничения - один ключ в одни руки',
                               reply_markup=await keyboard_get_key())


async def get_new_key(callback_query: CallbackQuery, callback_data: Dict[str, str]):
    await callback_query.answer()
    logger.info(callback_data)
    data = await outline.create_key(await db.get_server_key(int(callback_data['server'])))
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id,
                           f'Вставьте вашу ссылку доступа в приложение Outline:')
    await bot.send_message(callback_query.from_user.id,
                           f'{data["accessUrl"]}')
    await db.update_key(callback_query.from_user.id, int(data['id']), int(callback_data['server']))


async def delete_key(callback_query: CallbackQuery):
    await callback_query.answer()
    key_id, server_id = await db.get_key_id(callback_query.from_user.id)
    result = await outline.delete_key(await db.get_server_key(server_id), key_id)
    if result:
        await bot.send_message(callback_query.from_user.id, f'Ключ удалён')
        await db.delete_key(callback_query.from_user.id)
    else:
        await bot.send_message(callback_query.from_user.id, f'Произошло что-то невероятное (ошибка)')
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)


async def pass_delete(callback_query: CallbackQuery):
    await callback_query.answer()
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, f'Карашо')


def register_vpn_handlers(dp: Dispatcher):
    dp.register_message_handler(vpn_handler, commands=["vpn"], state="*")
    dp.register_callback_query_handler(vpn_callback_handler, vpn_callback.filter(action_type='vpn_settings'))
    dp.register_callback_query_handler(get_new_key, vpn_callback.filter(action_type='new_key'))
    dp.register_callback_query_handler(delete_key, lambda c: c.data == 'delete_key')
    dp.register_callback_query_handler(pass_delete, lambda c: c.data == 'pass')
