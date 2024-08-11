from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

'''
    [Статус]
    Своевременное дополнение
    [Описание скрипта]
    Основные реплай клавиатуры
    [Исполнители]
    Alexandr153
'''

main: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[
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
    resize_keyboard=True,
    one_time_keyboard=True,     # После использования клавиатура будет сворачиваться
    selective=True              # При вызове клавиатуры вызывается только для того, кто её вызвал
)
