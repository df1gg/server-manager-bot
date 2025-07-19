from dotenv import load_dotenv
import os


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_IDS = [int(x) for x in os.getenv("OWNER_IDS", "").split(",") if x]

MONITORING_INTERVAL = 60  # in sec
