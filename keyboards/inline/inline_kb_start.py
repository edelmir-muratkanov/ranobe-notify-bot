from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_start = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить источник',
                                 callback_data='Добавить источник'),
            InlineKeyboardButton(text='Удалить источник',
                                 callback_data='Удалить источник')
        ],
        [
            InlineKeyboardButton(text='Мои источники',
                                 callback_data='Мои источники'),
            InlineKeyboardButton(text='Проверить обновления',
                                 callback_data='Проверить обновления')
        ]
    ])
