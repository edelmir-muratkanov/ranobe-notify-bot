import asyncio
from aiogram import Dispatcher
from loader import db, dp
from .parsers import ranobehub, mangaclub


async def check(chat_id: str) -> str:
    text = ''
    sources = db.get_all(chat_id)
    for _chat_id, _name, _url, _num in sources:
        if "ranobehub" in _url:
            num, url = await ranobehub(_url)
            if num != _num:
                text += f'{url}\n\n'
                db.update(_chat_id, _name, _url, num)
        elif "mangaclub" in _url:
            num, url = await mangaclub(_url)
            if num != _num:
                text += f'{url}\n\n'
                db.update(_chat_id, _name, _url, num)

    return f'Обновы:\n\n{text}' if text != '' else 'Обнов нет'


async def autocheck():
    await asyncio.sleep(10)
    print('autocheck')
    sources = db.get_all(None)
    for chat_id, name, url, num in sources:
        res = await check(chat_id)
        if res != 'Обнов нет':
            dp.bot.send_message(chat_id, res)
