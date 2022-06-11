import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from loader import db, bot
from tgbot.keyboards.inline import keyboard_start, keyboard_help

logger = logging.getLogger(__name__)


async def user_start(message: Message):
    await db.add_tg_user(message.from_user.id)
    logger.info(f'START FROM USER {message.from_user}')
    await message.answer('Привет, я помогу тебе с VPN\n\n'
                         'Исходный код бота - <a href="https://github.com/bl4ckm45k/">GitHub</a>\n'
                         'Здесь прячется человек - <a href="https://twitter.com/Vincent_env">Twitter</a>',
                         reply_markup=keyboard_start(), disable_web_page_preview=True)


async def help_handler(message: Message):
    await message.answer(f'Outline – это ПО с открытым исходным кодом, '
                         f'которое прошло проверку организации Radically Open Security.\n\n'
                         f'Outline использует технологии <a href="https://shadowsocks.org/">Shadowsocks</a>\n\n',
                         reply_markup=keyboard_help(), disable_web_page_preview=True)


async def help_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id,
                           f'Outline – это ПО с открытым исходным кодом, '
                           f'которое прошло проверку организации Radically Open Security.\n\n'
                           f'Outline использует технологии <a href="https://shadowsocks.org/">Shadowsocks</a>\n\n',
                           reply_markup=keyboard_help(), disable_web_page_preview=True)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(help_handler, commands=["help"], state="*")
    dp.register_callback_query_handler(help_callback_handler, lambda c: c.data == 'why')
