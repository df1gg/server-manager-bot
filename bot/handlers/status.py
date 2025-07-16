from aiogram import F, Router, types
from utils import system
from utils.safe_edit import safe_edit
from bot import text
from bot.keyboards.server_status import server_status_kb


router = Router()


@router.message(F.text == "📡 Status")
async def get_server_status_handler(message: types.Message):
    status_message = text.SERVER_STATUS.format(
        cpu=system.get_cpu(),
        ram=system.get_ram(),
        disk=system.get_disk(),
        local_ip=system.get_local_ip(),
        ip=system.get_ip(),
        uptime=system.get_uptime(),
        time=system.get_time_now(),
    )
    await message.answer(status_message, reply_markup=server_status_kb())


@router.callback_query(F.data == "refresh_server_status")
async def refresh_server_status_handler(callback: types.CallbackQuery):
    await callback.answer()

    status_message = text.SERVER_STATUS.format(
        cpu=system.get_cpu(),
        ram=system.get_ram(),
        disk=system.get_disk(),
        local_ip=system.get_local_ip(),
        ip=system.get_ip(),
        uptime=system.get_uptime(),
        time=system.get_time_now(),
    )
    await safe_edit(callback.message, status_message, markup=server_status_kb())
