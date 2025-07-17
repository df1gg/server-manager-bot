from aiogram import F, Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot import text
from utils.logging_decorator import log_request
from db.services_methods import get_all_services

router = Router()


@router.message(F.text == "🗄️ Service Manager")
@log_request
async def show_services_menu(message: types.Message):
    services = await get_all_services()
    builder = InlineKeyboardBuilder()

    for s in services:
        builder.button(text=s.display_name, callback_data=f"service:{s.name}")
    builder.button(text="➕ Add new service", callback_data="add_service")
    builder.adjust(1)

    await message.answer(text.SERVICES_MANAGER_LIST, reply_markup=builder.as_markup())
