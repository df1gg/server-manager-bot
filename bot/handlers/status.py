from aiogram import F, Router, types
from utils import system
from bot import text


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
    await message.answer(status_message)
