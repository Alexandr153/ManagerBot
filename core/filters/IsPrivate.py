from aiogram.types import Message
from aiogram.filters import BaseFilter

'''
    [Статус]
    Заверешено
    [Описание фильтра]
    Проверка диалога на личные сообщения с ботом
    [Исполнители]
    Alexandr153
'''


class IsPrivate(BaseFilter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message) -> bool:
        return message.chat.type == "private"
