from aiogram import F, Router, types
from utils import system
from utils.safe_edit import safe_edit
from bot import text
from bot.keyboards.server_status import server_status_kb


router = Router()


@router.message(F.text == "📡 Status")
async def get_server_status_handler(message: types.Message):
    status_message = generate_server_status_message()
    await message.answer(status_message, reply_markup=server_status_kb())


@router.callback_query(F.data == "refresh_server_status")
async def refresh_server_status_handler(callback: types.CallbackQuery):
    await callback.answer()

    status_message = generate_server_status_message()
    await safe_edit(callback.message, status_message, markup=server_status_kb())


def generate_server_status_message() -> str:
    cpu = system.get_cpu()
    temp = system.get_cpu_temperature()
    ram = system.get_ram()
    swap = system.get_swap_usage()
    disk = system.get_disk()
    top_cpu = system.get_top_process("cpu")
    top_ram = system.get_top_process("ram")

    cpu_bar = system.make_bar(cpu)
    ram_bar = system.make_bar(ram)
    swap_bar = system.make_bar(swap)
    disk_bar = system.make_bar(disk)

    return text.SERVER_STATUS.format(
        cpu=cpu,
        temp=temp,
        ram=ram,
        swap=swap,
        disk=disk,
        top_cpu=top_cpu,
        top_ram=top_ram,
        cpu_bar=cpu_bar,
        ram_bar=ram_bar,
        swap_bar=swap_bar,
        disk_bar=disk_bar,
        local_ip=system.get_local_ip(),
        ip=system.get_ip(),
        uptime=system.get_uptime(),
        time=system.get_time_now(),
    )
