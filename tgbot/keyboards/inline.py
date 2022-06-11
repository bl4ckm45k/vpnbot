from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# from loader import c, db
from .callback_data_factory import vpn_callback


def keyboard_start():
    inline_btn_1 = InlineKeyboardButton(f'Доступ к VPN', callback_data=vpn_callback.new(action_type='vpn_settings'))
    inline_btn_2 = InlineKeyboardButton(f'Что за VPN?', callback_data='why')
    return InlineKeyboardMarkup().row(inline_btn_1, inline_btn_2)


def keyboard_help():
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton(
            f'Доступ к VPN', callback_data=vpn_callback.new(
                action_type='vpn_settings'
            )
        )
    ).row(InlineKeyboardButton(f'Клиент Outline VPN',
                               url=f'https://s3.amazonaws.com/outline-vpn/invite.html#/ru/home'))


def keyboard_get_key():
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton(f'Получить ключ', callback_data=vpn_callback.new(action_type='new_key')))


def keyboard_delete_and_get():
    return InlineKeyboardMarkup().row(
        InlineKeyboardButton(f'Удалить действующий ключ', callback_data=vpn_callback.new(action_type='delete_key'))
    ).row(InlineKeyboardButton(f'Оставить как есть', callback_data='pass'))
