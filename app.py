import asyncio
from utils.notify_admin import on_startup_notify
from utils.set_commands import set_default_commands
from utils.check_updates import autocheck
from aiogram import Dispatcher, executor
from handlers import dp
from loader import db, bot
from data.config import DELAY, WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT


async def on_startup(dp: Dispatcher):

    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)

    await on_startup_notify(dp)
    await set_default_commands(dp)


async def on_shutdown(dp: Dispatcher):
    await dp.bot.delete_webhook()

    await dp.storage.close()
    await dp.storage.wait_closed()


def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)


if __name__ == '__main__':
    db.setup()
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, autocheck, loop)
    executor.start_polling(dp, on_startup=on_startup, loop=loop)

    # executor.start_webhook(
    #     dispatcher=dp,
    #     webhook_path=WEBHOOK_PATH,
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     loop=loop,
    #     skip_updates=True,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT
    # )
