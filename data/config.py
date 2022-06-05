import os
from dotenv import load_dotenv

load_dotenv()

APP_PATH = os.path.abspath('.')
DELAY = 60 * 60 * 6
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv('ADMIN_ID')
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

