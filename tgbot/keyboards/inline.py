import logging

from aiogram.utils.keyboard import InlineKeyboardBuilder

logger = logging.getLogger(__name__)


def keyboard_start():
    builder = InlineKeyboardBuilder()
    builder.button(text='Доступ к VPN', callback_data='vpn')
    builder.button(text='Что за VPN?', callback_data='help')
    builder.adjust(2)
    return builder.as_markup()


def keyboard_help():
    builder = InlineKeyboardBuilder()
    builder.button(text='Клиенты для подключения', url='https://docs.marzban.dev/start/reality_app/')
    return builder.as_markup()


def keyboard_cancel():
    builder = InlineKeyboardBuilder()
    builder.button(text='❌Выйти из меню', callback_data='cancel')
    return builder.as_markup()
