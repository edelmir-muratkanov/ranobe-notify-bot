from aiogram.dispatcher.filters.state import StatesGroup, State


class AddSource(StatesGroup):
    name = State()
    url = State()
