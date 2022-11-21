from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import dp


async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.answer('Действие отменено.')


async def cancel_callback(callback_query: CallbackQuery, state: FSMContext):

    await dp.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await dp.bot.send_message(chat_id=callback_query.message.chat.id, text='Действие отменено.')
    await state.finish()
    await callback_query.answer()
    current_state = await state.get_state()
    if current_state is None:
        return


def register_cancel(dispatcher: Dispatcher):
    dispatcher.register_callback_query_handler(cancel_callback, lambda c: c.data and c.data == 'cancel', state='*')
    dispatcher.register_message_handler(cancel_handler, commands=["cancel"], state="*")
