from aiogram.types import Message
from aiogram.filters import BaseFilter

'''
    [Статус]
    Завершено
    [Описание фильтра]
    Проверка, является ли пользователь админстратором по списку айди
    [Исполнители]
    Alexandr153
'''


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids
