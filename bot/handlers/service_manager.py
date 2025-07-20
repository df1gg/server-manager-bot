from aiogram import F, Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext import asyncio
from bot.keyboards.cancel import cancel_kb
from bot.keyboards.services import confirm_delete_service_keyboard, service_control_kb
from bot.keyboards.main_menu import main_menu_kb
from bot.states.service_manager import AddService, DeleteService
from utils.logging_decorator import log_request
from db.services_methods import (
    delete_service,
    get_all_services,
    add_service,
    get_service,
)
from bot import text
from utils.services import get_service_info, run_systemctl_command
from utils.safe_edit import safe_edit

router = Router()


@router.message(F.text == "🗄️ Service Manager")
@log_request
async def show_services_menu_message_handler(message: types.Message):
    services = await get_all_services()
    builder = InlineKeyboardBuilder()

    for s in services:
        info = get_service_info(s.name)
        status = "🟢" if info and info["is_running"] else "🔴"
        builder.button(
            text=f"{status} {s.display_name}", callback_data=f"service:{s.name}"
        )
    builder.button(text="➕ Add new service", callback_data="add_service")
    builder.adjust(1)

    await message.answer(text.SERVICES_MANAGER_LIST, reply_markup=builder.as_markup())


@router.callback_query(F.data == "back_to_service_list")
@log_request
async def show_services_menu_callback_hanlder(callback: types.CallbackQuery):
    services = await get_all_services()
    builder = InlineKeyboardBuilder()

    for s in services:
        info = get_service_info(s.name)
        status = "🟢" if info and info["is_running"] else "🔴"
        builder.button(
            text=f"{status} {s.display_name}", callback_data=f"service:{s.name}"
        )
    builder.button(text="➕ Add new service", callback_data="add_service")
    builder.adjust(1)

    await safe_edit(callback.message, text.SERVICES_MANAGER_LIST, builder.as_markup())


@router.callback_query(F.data.startswith("start_service:"))
@log_request
async def start_service_handler(callback: types.CallbackQuery):
    await callback.answer()
    service_name = callback.data.split(":", 1)[1]

    info = get_service_info(service_name)
    if not info:
        await callback.message.answer(f"🚫 Service not found!")
        return

    success = run_systemctl_command("start", service_name)
    info = get_service_info(service_name)  # update info
    if not success:
        await callback.message.answer(
            f"❌ Failed to start service <code>{service_name}</code>."
        )
        return

    message_text = text.SERVICE_INFO.format(**info)
    await safe_edit(callback.message, message_text, service_control_kb(service_name))


@router.callback_query(F.data.startswith("restart_service:"))
@log_request
async def restart_service_handler(callback: types.CallbackQuery):
    await callback.answer()
    service_name = callback.data.split(":", 1)[1]

    info = get_service_info(service_name)
    if not info:
        await callback.message.answer(
            f"❌ Service <code>{service_name}</code> not found!"
        )
        return

    success = run_systemctl_command("restart", service_name)
    info = get_service_info(service_name)  # update info
    if not success:
        await callback.message.answer(
            f"❌ Failed to restart service <code>{service_name}</code>."
        )
        return

    message_text = text.SERVICE_INFO.format(**info)
    await safe_edit(callback.message, message_text, service_control_kb(service_name))


@router.callback_query(F.data.startswith("stop_service:"))
@log_request
async def stop_service_handler(callback: types.CallbackQuery):
    await callback.answer()
    service_name = callback.data.split(":", 1)[1]

    info = get_service_info(service_name)
    if not info:
        await callback.message.answer(
            f"❌ Service <code>{service_name}</code> not found!"
        )
        return

    success = run_systemctl_command("stop", service_name)
    info = get_service_info(service_name)  # update info
    if not success:
        await callback.message.answer(
            f"❌ Failed to stop service <code>{service_name}</code>."
        )
        return

    message_text = text.SERVICE_INFO.format(**info)
    await safe_edit(callback.message, message_text, service_control_kb(service_name))


@router.callback_query(F.data.startswith("service:"))
@router.callback_query(F.data.startswith("refresh_service:"))
@log_request
async def service_info_handler(callback: types.CallbackQuery):
    await callback.answer()

    service_name = callback.data.split(":")[1]
    info = get_service_info(service_name)
    if not info:
        await callback.message.answer("🚫 Service not found!")
        return

    message_text = text.SERVICE_INFO.format(**info)
    await safe_edit(callback.message, message_text, service_control_kb(service_name))


@router.callback_query(F.data.startswith("delete_service:"))
@log_request
async def delete_service_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()

    service_name = callback.data.split(":")[1]

    db_info = await get_service(service_name)
    if not db_info:
        await callback.message.delete()
        await callback.message.answer("🚫 Service not found!")
        return

    await state.update_data(service_name=service_name)
    await state.set_state(DeleteService.confirm)

    await safe_edit(
        callback.message,
        f"❗ Are you sure you want to delete the service with name <code>{service_name}</code>?",
        confirm_delete_service_keyboard(),
    )


@router.callback_query(F.data == "confirm_delete_service")
@log_request
async def confirm_delete_service_handler(
    callback: types.CallbackQuery, state: FSMContext
):
    await callback.answer()

    data = await state.get_data()
    service_name = data["service_name"]

    db_info = await get_service(service_name)
    if not db_info:
        await callback.message.delete()
        await callback.message.answer("🚫 Service not found!")
        return

    await delete_service(service_name)
    await safe_edit(
        callback.message,
        f"✅ Service with name <code>{service_name}</code> success deleted!",
    )
    await state.clear()


@router.callback_query(F.data == "cancel_delete_service")
@log_request
async def cancel_delete_service_handler(
    callback: types.CallbackQuery, state: FSMContext
):
    await callback.answer()
    await safe_edit(
        callback.message,
        f"❌ Service cancel deleted!",
    )
    await state.clear()


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
    info = get_service_info(message.text)
    if not info:
        await message.answer(
            "🚫 Service not found! Try another name:", reply_markup=cancel_kb()
        )
        return

    db_info = await get_service(message.text)
    if db_info:
        await message.answer(
            "🚫 Service already exists! Try another name:", reply_markup=cancel_kb()
        )
        return

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

    await message.answer(
        f"✅ Service <code>{service_display_name}</code> success added!",
        reply_markup=main_menu_kb(),
    )
    await state.clear()
