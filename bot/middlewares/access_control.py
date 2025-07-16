from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from aiogram.exceptions import TelegramBadRequest
from typing import Callable, Dict, Any, Awaitable
from bot import text
import os


ALLOWED_IDS = {int(os.getenv("OWNER_ID", 0))}


class AccessControlMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user_id = getattr(event.from_user, "id", None)

        if user_id not in ALLOWED_IDS:
            try:
                if isinstance(event, Message):
                    await event.answer(text.ACCESS_DENIED)
                elif isinstance(event, CallbackQuery):
                    await event.message.answer(text.ACCESS_DENIED)
            except TelegramBadRequest:
                pass
            return

        return await handler(event, data)
