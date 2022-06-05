import asyncio
from utils.notify_admin import on_startup_notify
from utils.set_commands import set_default_commands
from utils.check_updates import autocheck
from aiogram import executor
from handlers import dp
from loader import db
from data.config import DELAY


async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)


def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)


if __name__ == '__main__':
    db.setup()
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, autocheck, loop)
    executor.start_polling(dp, on_startup=on_startup,
                           loop=loop, skip_updates=True)
