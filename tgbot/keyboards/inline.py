from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
from loader import db
from .callback_data_factory import vpn_callback

logger = logging.getLogger(__name__)
def keyboard_start():
    inline_btn_1 = InlineKeyboardButton(f'Доступ к VPN', callback_data=vpn_callback.new(action_type='vpn_settings', server='n'))
    inline_btn_2 = InlineKeyboardButton(f'Что за VPN?', callback_data='why')
    return InlineKeyboardMarkup().row(inline_btn_1, inline_btn_2)


def keyboard_help():
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton(
            f'Доступ к VPN', callback_data=vpn_callback.new(
                action_type='vpn_settings', server='n'
            )
        )
    ).row(InlineKeyboardButton(f'Клиент Outline VPN',
                               url=f'https://getoutline.org/ru/get-started/'))


async def keyboard_get_key():
    kb = InlineKeyboardMarkup(row_width=2)
    for x in await db.get_servers():
        logger.info(f'{x}')
        kb.insert(InlineKeyboardButton(f'{x[0][1]}', callback_data=vpn_callback.new(action_type='new_key', server=f'{x[0][0]}')))
    return kb


def keyboard_delete_and_get():
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton(f'Удалить действующий ключ', callback_data='delete_key')
    ).row(InlineKeyboardButton(f'Оставить как есть', callback_data='pass'))
