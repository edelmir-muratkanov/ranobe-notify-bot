from loader import db, dp
from .parsers import ranobehub, mangaclub


async def check(chat_id=None):
    text = ''
    sources = db.get_all(chat_id)
    for _ in sources:
        _chat_id, _name, _url, _num = _
        if "ranobehub" in _url:
            num, url = await ranobehub(_url)
            if num != _num:
                if chat_id is None:
                    dp.bot.send_message(_chat_id, f'{url}\n')
                else:
                    text += f'{url}\n'
                db.update(_chat_id, _name, _url, num)
        elif "mangaclub" in _url:
            num, url = await mangaclub(_url)
            if num != _num:
                if chat_id is None:
                    dp.bot.send_message(_chat_id, f'{url}\n')
                else:
                    text += f'{url}\n'
                db.update(_chat_id, _name, _url, num)

    return f'Обновы:\n\n{text}' if text != '' else 'Обнов нет'
