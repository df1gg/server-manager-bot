import asyncio
import config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from bot import setup_routers


async def main():
    bot = Bot(
        token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    setup_routers(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
