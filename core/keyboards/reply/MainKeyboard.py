from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

'''
    [Статус]
    Своевременное дополнение
    [Описание скрипта]
    Основные реплай клавиатуры
    [Исполнители]
    Alexandr153
'''

main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Случайная беседа")
    ],
    [
        KeyboardButton(text="Рейтинг"),
        KeyboardButton(text="Установка")
    ],
    [
        KeyboardButton(text="Пончики"),
        KeyboardButton(text="Рефералы")
    ],
    [
        KeyboardButton(text="Аукцион"),
        KeyboardButton(text="Команды")
    ]
],
    resize_keyboard=True)
