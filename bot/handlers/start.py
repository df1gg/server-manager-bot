from aiogram import Router, types
from aiogram.filters import CommandStart
from bot.keyboards.main_menu import main_menu_kb
import config


router = Router()


@router.message(CommandStart())
async def start_command_handler(message: types.Message):
    if message.from_user.id != int(config.OWNER_ID):
        return await message.answer("🚫 Access denied.")
    await message.answer("✅ Bot is running!", reply_markup=main_menu_kb())
