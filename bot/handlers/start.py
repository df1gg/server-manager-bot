from aiogram import Router, types
from aiogram.filters import CommandStart
from bot import text
from bot.keyboards.main_menu import main_menu_kb
from utils.logging_decorator import log_request


router = Router()


@router.message(CommandStart())
@log_request
async def start_command_handler(message: types.Message):
    await message.answer(text.START, reply_markup=main_menu_kb())
