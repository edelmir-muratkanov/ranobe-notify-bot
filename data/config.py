import os
from dotenv import load_dotenv

load_dotenv()

APP_PATH = os.path.abspath('.')
DELAY = 60 * 60 * 6
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv('ADMIN_ID')
