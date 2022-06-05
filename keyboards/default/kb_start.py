from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Добавить источник'),
            KeyboardButton('Удалить источник')
        ],
        [
            KeyboardButton('Мои источники'),
            KeyboardButton('Проверить обновления')
        ]
    ], resize_keyboard=True)
