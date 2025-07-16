from dotenv import load_dotenv
import os


load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID", 0)
