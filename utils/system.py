import asyncio
import platform
from aiogram import Bot
import psutil
import socket
import urllib.request
from datetime import datetime
from config import ALERT_THRESHOLDS, OWNER_IDS, SYSTEM_MONITORING_INTERVAL
from utils.format import format_bytes


def to_float(value, default=0.0) -> float:
    if isinstance(value, (int, float)):
        return float(value)

    if isinstance(value, str):
        normalized = value.strip().replace("°C", "")
        try:
            return float(normalized)
        except ValueError:
            return float(default)

    return float(default)


def get_distro():
    if platform.system() == "Linux":
        try:
            with open("/etc/os-release") as f:
                lines = f.readlines()
                distro = ""
                for line in lines:
                    if line.startswith("PRETTY_NAME="):
                        distro = line.strip().split("=")[1].strip('"')
                        break
        except Exception:
            distro = "Unknown"
    else:
        distro = platform.system()

    return distro


def get_kernel():
    return platform.release()


def get_hostname():
    return socket.gethostname()


def get_cpu():
    return psutil.cpu_percent()


def get_ram():
    return psutil.virtual_memory().percent


def get_disk():
    return psutil.disk_usage("/").percent


def get_ip():
    try:
        return (
            urllib.request.urlopen("https://api.ipify.org", timeout=3)
            .read()
            .decode("utf8")
        )
    except Exception:
        return "-"


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "127.0.0.1"


def get_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    delta = now - boot_time
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m"


def get_time_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_cpu_temperature():
    temps = psutil.sensors_temperatures()
    if not temps:
        return "-"

    for name, entries in temps.items():
        if entries:
            return f"{entries[0].current:.1f}°C"

    return "-"


def get_swap_usage():
    swap = psutil.swap_memory()
    if swap.total == 0:
        return "-"

    return swap.percent


def get_top_process(by: str = "cpu"):
    key = "cpu_percent" if by == "cpu" else "memory_percent"

    processes = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            processes.append((proc.info["name"], proc.info[key]))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda x: x[1], reverse=True)

    if not processes or processes[0][1] == 0.0:
        return "-"

    name, usage = processes[0]
    return f"{name} ({usage:.1f}%)"


def get_network_traffic():
    io = psutil.net_io_counters()

    return {
        "download": format_bytes(io.bytes_recv),
        "upload": format_bytes(io.bytes_sent),
        "packets_in": f"{io.packets_recv:,}",
        "packets_out": f"{io.packets_sent:,}",
    }


def make_bar(percent: float, size: int = 8) -> str:
    """Returns a visual progress bar string, like [██████░░░░░░]"""
    percent = to_float(percent, 0)
    filled_length = int(size * percent / 100)
    bar = "█" * filled_length + "░" * (size - filled_length)
    return f"[{bar}]"


async def monitoring_load(bot: Bot):
    ALERT_FLAGS = {
        "cpu": False,
        "ram": False,
        "disk": False,
        "swap": False,
        "cpu_temp": False,
    }

    while True:
        metrics = {
            "cpu": get_cpu(),
            "ram": get_ram(),
            "disk": get_disk(),
            "swap": to_float(get_swap_usage(), 0),
            "cpu_temp": to_float(get_cpu_temperature(), 0),
        }

        for key, value in metrics.items():
            threshold = ALERT_THRESHOLDS.get(key)
            exceeded = value >= threshold
            alert_sent = ALERT_FLAGS.get(key, False)

            if exceeded and not alert_sent:
                ALERT_FLAGS[key] = True
                text = f"🚨 <b>{key.upper()}</b> usage is high: <code>{value:.1f}%</code> (threshold: {threshold}%)"
                for admin in OWNER_IDS:
                    await bot.send_message(admin, text, parse_mode="HTML")
            elif not exceeded and alert_sent:
                ALERT_FLAGS[key] = False
                text = f"✅ <b>{key.upper()}</b> usage back to normal: <code>{value:.1f}%</code>"
                for admin in OWNER_IDS:
                    await bot.send_message(admin, text, parse_mode="HTML")
        await asyncio.sleep(SYSTEM_MONITORING_INTERVAL)
