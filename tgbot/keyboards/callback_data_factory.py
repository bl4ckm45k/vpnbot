from aiogram.filters.callback_data import CallbackData


class VpnCallback(CallbackData, prefix='vpn'):
    action_type: str
