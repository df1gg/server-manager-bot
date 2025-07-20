import re
import subprocess
import asyncio

from aiogram import Bot
from db.services_methods import get_all_services, update_service_status
from utils.logger import logger
from config import OWNER_IDS, SERIVICE_MONITORING_INTERVAL


def get_service_info(name: str) -> dict:
    def run(cmd):
        return subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True
        ).stdout.strip()

    try:
        status = run(["systemctl", "is-active", name])
        enabled = run(["systemctl", "is-enabled", name])

        show_output = run(["systemctl", "show", name])

        props = dict(
            line.split("=", 1) for line in show_output.splitlines() if "=" in line
        )

        pid = props.get("MainPID", "-")
        cpu = mem = uptime = "-"

        if pid and pid != 0 and pid != "-":
            pid = pid.split()[0]
            ps_output = run(["ps", "-p", pid, "-o", "%cpu,%mem,etime", "--no-headers"])
            if ps_output:
                cpu, mem, uptime = ps_output.split(maxsplit=2)

        exec_path = props.get("ExecStart", "-")
        if exec_path != "-":
            match = re.search(r"(/\S+)", exec_path)
            if match:
                exec_path = match.group(1)

        return {
            "name": name,
            "is_running": True if status == "active" else False,
            "is_enabled": True if enabled == "enabled" else False,
            "pid": pid,
            "cpu": cpu,
            "mem": mem,
            "uptime": uptime,
            "path": exec_path,
        }
    except Exception as e:
        logger.error({e})
        return None


def run_systemctl_command(action: str, service_name: str) -> bool:
    """Run systemctl start|stop|restart and return success."""
    try:
        result = subprocess.run(
            ["sudo", "systemctl", action, service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10,
        )
        return result.returncode == 0
    except Exception as e:
        logger.error(e)
        return False


async def monitoring_services(bot: Bot):
    while True:
        services = await get_all_services()
        for s in services:
            info = await asyncio.to_thread(get_service_info, s.name)
            if not info:
                continue

            currently_running = info["is_running"]
            if not currently_running and s.is_running:
                for admin in OWNER_IDS:
                    await bot.send_message(
                        admin,
                        f"🚨 Service <b>{s.display_name}</b> has stopped unexpectedly!",
                    )
            await update_service_status(s.name, currently_running)
        await asyncio.sleep(SERIVICE_MONITORING_INTERVAL)
