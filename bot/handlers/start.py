from aiogram import Router, types
from aiogram.filters import CommandStart
import config


router = Router()


@router.message(CommandStart())
async def start_command_handler(message: types.Message):
    print(config.OWNER_ID)
    print(message.from_user.id)
    if message.from_user.id != int(config.OWNER_ID):
        return await message.answer("🚫 Access denied.")
    await message.answer("✅ Bot is running!")
