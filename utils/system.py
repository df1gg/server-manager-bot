import psutil
import socket
from datetime import datetime


def get_cpu():
    return psutil.cpu_percent()


def get_ram():
    return psutil.virtual_memory().percent


def get_disk():
    return psutil.disk_usage("/").percent


def get_ip():
    return socket.gethostbyname(socket.gethostname())


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
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


def make_bar(percent: float, size: int = 8) -> str:
    """Returns a visual progress bar string, like [██████░░░░░░]"""
    filled_length = int(size * percent / 100)
    bar = "█" * filled_length + "░" * (size - filled_length)
    return f"[{bar}]"
