import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db
from .callback_data_factory import vpn_callback

logger = logging.getLogger(__name__)


def keyboard_start():
    keyboard = InlineKeyboardMarkup()
    inline_btn_1 = InlineKeyboardButton(f'Доступ к VPN',
                                        callback_data=vpn_callback.new(action_type='vpn_settings', server='no'))
    inline_btn_2 = InlineKeyboardButton(f'Что за VPN?', callback_data='why')
    return keyboard.row(inline_btn_1, inline_btn_2)


def keyboard_help():
    keyboard = InlineKeyboardMarkup()
    btn_vpn_client = InlineKeyboardButton(f'Клиент Outline VPN',
                                          url=f'https://getoutline.org/ru/get-started/')
    keyboard.row(btn_vpn_client)
    return keyboard


async def keyboard_servers_list(action_type: str):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for x in await db.get_servers():
        keyboard.insert(InlineKeyboardButton(f'{x[0][1]}', callback_data=vpn_callback.new(action_type=action_type,
                                                                                          server=f'{x[0][0]}')))
    if action_type == 'to_delete':
        keyboard.row(InlineKeyboardButton(f'❌Выйти из меню', callback_data=f"cancel"))
    return keyboard


def keyboard_admin_action():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn_add_server = InlineKeyboardButton(f'Добавить сервер', callback_data='add_server')
    btn_delete_server = InlineKeyboardButton(f'Удалить сервер', callback_data='delete_server')
    btn_cancel = InlineKeyboardButton(f'❌Выйти из меню', callback_data=f"cancel")
    keyboard.add(btn_add_server, btn_delete_server, btn_cancel)
    return keyboard


def keyboard_cancel():
    return InlineKeyboardMarkup().add(InlineKeyboardButton(f'❌Выйти из меню', callback_data=f"cancel"))
