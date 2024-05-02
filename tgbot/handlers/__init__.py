from tgbot.handlers.cancel import cancel_router
from tgbot.handlers.user import user_router
from tgbot.handlers.vpn_settings import vpn_router

routers_list = [
    cancel_router,
    user_router,
    vpn_router
]

__all__ = [
    "routers_list",
]
