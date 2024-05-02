from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from cachetools import TTLCache

THROTTLE_RATE_L2 = 0.5


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self):
        self.cache_l1 = TTLCache(maxsize=10_000, ttl=0.5)
        self.cache_l2 = TTLCache(maxsize=10_000, ttl=THROTTLE_RATE_L2)

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:

        if event.from_user.id in self.cache_l1:
            if event.from_user.id in self.cache_l2:
                return

            self.cache_l2[event.from_user.id] = None
            await event.answer(text="Не спамь!")
            return

        self.cache_l1[event.from_user.id] = None

        return await handler(event, data)

# class CallbackThrottlingMiddleware(BaseMiddleware):
#     def __init__(self):
#         self.cache_l1 = TTLCache(maxsize=10_000, ttl=config.THROTTLE_RATE)
#         self.cache_l2 = TTLCache(maxsize=10_000, ttl=THROTTLE_RATE_L2)
#
#     async def __call__(
#             self,
#             handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#             event: TelegramObject,
#             data: Dict[str, Any],
#     ) -> Any:
#         if event.from_user.id in self.cache_l1:
#             if event.from_user.id in self.cache_l2:
#                 return
#
#             self.cache_l2[event.from_user.id] = None
#             await event.answer(text="Не спамь!", show_alert=True)
#             return
#
#         self.cache_l1[event.from_user.id] = None
#
#         return await handler(event, data)
