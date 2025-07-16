from functools import wraps
from time import perf_counter
from aiogram.types import Message, CallbackQuery
from utils.logger import logger


def log_request(func):
    @wraps(func)
    async def wrapper(event, *args, **kwargs):
        start = perf_counter()

        user_id = getattr(event.from_user, "id", "unknown")
        username = getattr(event.from_user, "username", "unknown")
        full_name = getattr(event.from_user, "full_name", "unknown")

        action = "CallbackQuery" if isinstance(event, CallbackQuery) else "Message"
        content = event.data if isinstance(event, CallbackQuery) else event.text

        logger.info(
            f"{action} from {full_name} (@{username}, id={user_id}) → {content}"
        )

        result = await func(event, *args, **kwargs)

        elapsed = perf_counter() - start
        logger.debug(f"{func.__name__} completed in {elapsed:.3f}s")

        return result

    return wrapper
