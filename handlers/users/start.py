from aiogram import types
from loader import dp, db
from keyboards.default import kb_start
from utils.check_updates import check
from aiogram.dispatcher.webhook import SendMessage


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    # await message.answer(f'Welcome, {message.from_user.full_name}', reply_markup=kb_start)
    chat_id = message.chat.id
    return SendMessage(chat_id, f'Welcome, {message.from_user.full_name}', reply_markup=kb_start)


@dp.message_handler(text='Мои источники')
async def my_sources(message: types.Message):
    try:
        chat_id = message.from_user.id
        sources = db.get_all(chat_id)
    except Exception as e:
        print(e)

    text = 'Источники:\n\n'
    for _ in sources:
        chat_id, name, url, num = _
        # text += f'{name}\n{url}\n\n'
        text += f'<a href={url}>{name}</a>'
    await message.answer(text, disable_web_page_preview=True)


@dp.message_handler(text='Проверить обновления')
async def check_updates(message: types.Message):
    print('check updates')
    chat_id = message.from_user.id
    text = await check(chat_id)
    await message.answer(text, disable_web_page_preview=True)
