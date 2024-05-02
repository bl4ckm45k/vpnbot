from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import bot

cancel_router = Router()


@cancel_router.message(Command("cancel"))
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer('Действие отменено.')


@cancel_router.callback_query(F.data == 'cancel')
async def cancel_callback(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer('Действие отменено.')
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
