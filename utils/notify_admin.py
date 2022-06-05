import logging
from aiogram import Dispatcher
from data.config import ADMIN_ID


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN_ID, 'Бот запущен')
    except Exception as e:
        logging.exception(e)
