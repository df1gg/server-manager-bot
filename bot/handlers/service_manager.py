from aiogram import F, Router, types
from utils.logging_decorator import log_request

router = Router()


@router.message(F.text == "🗄️ Service Manager")
@log_request
async def show_services_menu(message: types.Message):
    await message.answer("Select a service:")
