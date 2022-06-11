import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from loader import db, bot, outline
from tgbot.keyboards.callback_data_factory import vpn_callback
from tgbot.keyboards.inline import keyboard_get_key, keyboard_delete_and_get

logger = logging.getLogger(__name__)


async def vpn_handler(message: Message):
    active = await db.select_active(message.from_user.id)
    if active:
        await bot.send_message(message.from_user.id, f'У вас уже есть действующий ключ доступа.',
                               reply_markup=keyboard_delete_and_get())
    else:
        await bot.send_message(message.from_user.id, f'Ограничения - один ключ в одни руки',
                               reply_markup=keyboard_get_key())


async def vpn_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    active = await db.select_active(callback_query.from_user.id)
    if active:
        await bot.send_message(callback_query.from_user.id,
                               f'У вас уже есть действующий ключ доступа.',
                               reply_markup=keyboard_delete_and_get())
    else:
        await bot.send_message(callback_query.from_user.id,
                               f'Ограничения - один ключ в одни руки',
                               reply_markup=keyboard_get_key())


async def get_new_key(callback_query: CallbackQuery):
    await callback_query.answer()
    data = await outline.create_key()
    await bot.send_message(callback_query.from_user.id,
                           f'Вставьте вашу ссылку доступа в приложение Outline:')
    await bot.send_message(callback_query.from_user.id,
                           f'{data["accessUrl"]}')
    await db.update_key(callback_query.from_user.id, int(data['id']))


async def delete_key(callback_query: CallbackQuery):
    await callback_query.answer()
    result = await outline.delete_key(await db.get_key_id(callback_query.from_user.id))
    if result:
        await bot.send_message(callback_query.from_user.id, f'Ключ удалён')
        await db.delete_key(callback_query.from_user.id)
    else:
        await bot.send_message(callback_query.from_user.id, f'Произошло что-то невероятное (ошибка)')


def register_vpn_handlers(dp: Dispatcher):
    dp.register_message_handler(vpn_handler, commands=["vpn"], state="*")
    dp.register_callback_query_handler(vpn_callback_handler, vpn_callback.filter(action_type='vpn_settings'))
    dp.register_callback_query_handler(get_new_key, vpn_callback.filter(action_type='new_key'))
    dp.register_callback_query_handler(delete_key, vpn_callback.filter(action_type='delete_key'))
