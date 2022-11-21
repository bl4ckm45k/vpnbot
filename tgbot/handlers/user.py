from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ChatType

from loader import bot
from tgbot.keyboards.inline import keyboard_start, keyboard_help


async def user_start(message: Message):
    await message.answer('Привет, я помогу тебе с VPN\n\n'
                         'Исходный код бота - <a href="https://github.com/bl4ckm45k/vpnbot">GitHub</a>\n'
                         'Здесь прячется человек - <a href="https://t.me/pay4fallwall">Telegram</a>',
                         reply_markup=keyboard_start(), disable_web_page_preview=True)


async def help_handler(message: Message):
    await message.answer(f'Outline – это ПО с открытым исходным кодом, '
                         f'которое прошло проверку организаций '
                         f'<a href="https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf">Radically Open Security</a> и '
                         f'<a href="https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf">Cure53</a>.\n\n'
                         f'Outline использует технологии <a href="https://shadowsocks.org/">Shadowsocks</a>',
                         reply_markup=keyboard_help(), disable_web_page_preview=True)


async def help_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id,
                           f'Outline – это ПО с открытым исходным кодом, '
                           f'которое прошло проверку организаций '
                           f'<a href="https://s3.amazonaws.com/outline-vpn/static_downloads/ros-report.pdf">Radically Open Security</a> и '
                           f'<a href="https://s3.amazonaws.com/outline-vpn/static_downloads/cure53-report.pdf">Cure53</a>.\n\n'
                           f'Outline использует технологии <a href="https://shadowsocks.org/">Shadowsocks</a>',
                           reply_markup=keyboard_help(), disable_web_page_preview=True)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], chat_type=ChatType.PRIVATE)
    dp.register_message_handler(help_handler, commands=["help"], chat_type=ChatType.PRIVATE)
    dp.register_callback_query_handler(help_callback_handler, lambda c: c.data == 'why', chat_type=ChatType.PRIVATE)
