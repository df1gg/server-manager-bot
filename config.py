from dotenv import load_dotenv
import os


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_IDS = [int(x) for x in os.getenv("OWNER_IDS", "").split(",") if x]

SERIVICE_MONITORING_INTERVAL = 60  # in sec
SYSTEM_MONITORING_INTERVAL = 30  # in sec
ALERT_THRESHOLDS = {
    "cpu": 80.0,
    "ram": 85.0,
    "disk": 90.0,
    "swap": 60.0,
    "cpu_temp": 75.0,
}
