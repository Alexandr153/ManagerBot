from aiogram.types import Message
from aiogram.filters import BaseFilter
from typing import Union

'''
    [Статус]
    Заверешено
    [Описание фильтра]
    Проверка типа чата, либо строкой, либо списком ['private', 'supergroup']
    [Исполнители]
    Alexandr153
'''


class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_type: Union[str, list]) -> None:
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type
