from aiogram import F, Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from bot.keyboards.cancel import cancel_kb
from bot.states.service_manager import AddService
from utils.logging_decorator import log_request
from db.services_methods import get_all_services, add_service
from bot import text

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


@router.callback_query(F.data == "add_service")
@log_request
async def start_add_service_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()

    await callback.message.answer(
        "📇 Enter systemd service name:", reply_markup=cancel_kb()
    )
    await state.set_state(AddService.waiting_for_service_name)


@router.message(AddService.waiting_for_service_name)
@log_request
async def get_service_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(service_name=message.text)
    await message.answer(
        "🖼️ Enter a display name for the service:", reply_markup=cancel_kb()
    )
    await state.set_state(AddService.waiting_for_display_name)


@router.message(AddService.waiting_for_display_name)
@log_request
async def get_service_display_name_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    service_name = data["service_name"]
    service_display_name = message.text

    await add_service(name=service_name, display_name=service_display_name)

    await message.answer(f'✅ Service "{service_display_name}" success added!')
    await state.clear()
