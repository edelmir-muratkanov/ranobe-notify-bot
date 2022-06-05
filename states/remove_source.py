from aiogram.dispatcher.filters.state import StatesGroup, State


class RemoveSource(StatesGroup):
    name = State()
    url = State()
