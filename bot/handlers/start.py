from aiogram import Router, types
from aiogram.filters import CommandStart
from bot import text
from bot.keyboards.main_menu import main_menu_kb
from utils.logger import logger
import config


router = Router()


@router.message(CommandStart())
async def start_command_handler(message: types.Message):
    logger.info(f"Status requested by {message.from_user.id}")
    if message.from_user.id != int(config.OWNER_ID):
        return await message.answer(text.ACCESS_DENIED)
    await message.answer(text.START, reply_markup=main_menu_kb())
