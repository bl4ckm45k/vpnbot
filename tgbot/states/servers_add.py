from aiogram.dispatcher.filters.state import StatesGroup, State


class AddServer(StatesGroup):
    server_name = State()
    api_link = State()
