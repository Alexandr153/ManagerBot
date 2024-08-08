from aiogram.types import Message
from aiogram.filters import BaseFilter
from typing import Union

'''
    [Статус]
    Завершено
    [Описание фильтра]
    Проверка на тип чата. На вход подается список типов чата.
    ('private', 'group', 'supergroup' 'channel')
    Возвращает True если текущий чат содержится в списке
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
