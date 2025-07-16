from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from aiogram.exceptions import TelegramBadRequest
from typing import Callable, Dict, Any, Awaitable
from utils.logger import logger
from bot import text
import os


raw_ids = os.getenv("OWNER_IDS", "")
ALLOWED_IDS = {int(x.strip()) for x in raw_ids.split(",") if x.strip().isdigit()}


class AccessControlMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user = getattr(event, "from_user", None)
        user_id = getattr(event.from_user, "id", None)

        if user_id not in ALLOWED_IDS:
            name = getattr(user, "full_name", "unknown")
            username = getattr(user, "username", "unknown")
            logger.warning(
                f"Access denied: {name} (@{username}, id={user_id}) tried to access the bot"
            )
            try:
                if isinstance(event, Message):
                    await event.answer(text.ACCESS_DENIED)
                elif isinstance(event, CallbackQuery):
                    await event.message.answer(text.ACCESS_DENIED)
            except TelegramBadRequest:
                logger.debug("Couldn't send 'access denied' message.")
            return

        return await handler(event, data)
