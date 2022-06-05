from utils.notify_admin import on_startup_notify
from utils.set_commands import set_default_commands
from aiogram import executor
from handlers import dp
from loader import db


async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)
    print('Бот запущен')


if __name__ == '__main__':
    db.setup()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
