from aiogram import F, Router, types
from utils import system
from utils.logging_decorator import log_request
from utils.safe_edit import safe_edit
from bot import text
from bot.keyboards.server_status import server_status_kb


router = Router()


@router.message(F.text == "📡 Status")
@log_request
async def get_server_status_handler(message: types.Message):
    status_message = generate_server_status_message()
    await message.answer(status_message, reply_markup=server_status_kb())


@router.callback_query(F.data == "refresh_server_status")
@log_request
async def refresh_server_status_handler(callback: types.CallbackQuery):
    await callback.answer()

    status_message = generate_server_status_message()
    await safe_edit(callback.message, status_message, markup=server_status_kb())


def generate_server_status_message() -> str:
    network = system.get_network_traffic()

    return text.SERVER_STATUS.format(
        os=system.get_distro(),
        kernel=system.get_kernel(),
        hostname=f"<tg-spoiler>{system.get_hostname()}</tg-spoiler>",
        cpu=system.get_cpu(),
        temp=system.get_cpu_temperature(),
        ram=system.get_ram(),
        swap=system.get_swap_usage(),
        disk=system.get_disk(),
        top_cpu=system.get_top_process("cpu"),
        top_ram=system.get_top_process("ram"),
        cpu_bar=system.make_bar(system.get_cpu()),
        ram_bar=system.make_bar(system.get_ram()),
        swap_bar=system.make_bar(system.get_swap_usage()),
        disk_bar=system.make_bar(system.get_disk()),
        local_ip=f"<tg-spoiler>{system.get_local_ip()}</tg-spoiler>",
        ip=f"<tg-spoiler>{system.get_ip()}</tg-spoiler>",
        download=network["download"],
        upload=network["upload"],
        packets_in=network["packets_in"],
        packets_out=network["packets_out"],
        uptime=system.get_uptime(),
        time=system.get_time_now(),
    )
