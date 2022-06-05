from loader import db, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import RemoveSource


@dp.message_handler(text='Удалить источник')
async def remove_source(message: types.Message):
    await message.answer('Введите название: ')
    await RemoveSource.name.set()


@dp.message_handler(state=RemoveSource.name)
async def set_state_name(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name=answer)

    data = await state.get_data()

    try:
        chat_id = message.from_user.id

        db.delete(chat_id, data['name'])
        await message.answer('Удален источник {}'.format(data['name']))
        await state.finish()
    except Exception as e:
        print(e)
