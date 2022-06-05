from loader import dp, db
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import AddSource


@dp.message_handler(text='Добавить источник')
async def add_source(message: types.Message):
    await message.answer('Введите название: ')
    await AddSource.name.set()


@dp.message_handler(state=AddSource.name)
async def set_state_name(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.answer('Введите ссылку: ')
    await AddSource.url.set()


@dp.message_handler(state=AddSource.url)
async def set_state_url(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(url=answer)

    data = await state.get_data()

    # filepath = os.path.join(APP_PATH, 'data', 'sources.csv')

    # isDup = await find_duplicate(filepath, data)
    # if not isDup:
    #     await save_source_to_file(filepath, data)
    #     await message.answer('Добавлен источник {}'.format(data['name']))
    # else:
    #     await message.answer('Такой источник уже есть')
    # await state.finish()

    try:
        chat_id = message.from_user.id

        db.add(chat_id, data['name'], data['url'])
        await message.answer('Добавлен источник {}'.format(data['name']))
        await state.finish()
    except Exception as e:
        print(e)
