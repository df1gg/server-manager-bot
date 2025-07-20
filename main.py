import asyncio
import config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from bot import setup_middleware, setup_routers
from db.database import init_db
from utils.logger import logger
from utils.services import monitoring_services
from utils.system import monitoring_load


async def main():
    await init_db()

    bot = Bot(
        token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    setup_middleware(dp)
    setup_routers(dp)
    asyncio.create_task(monitoring_services(bot))
    asyncio.create_task(monitoring_load(bot))

    logger.info("Bot sucess started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Bot starting...")
    asyncio.run(main())
