import logging

from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from filters.chat_filters import ChatTypeFilter


'''
    [Статус]
    В работе
    [Описание скрипта]
    Команда поддержки в сети и оффлайн 
    для прочих вопросов вне документации бота
    [Исполнители]
    Alexandr153
'''

router = Router()

logger = logging.getLogger(__name__)


@router.message(Command('support', 'поддержка', prefix='/!'), ChatTypeFilter('private'))
async def support(message: Message) -> None:
    await message.answer(
        'Если у вас возникли вопросы, ответ на который вы не нашли в полном описании бота(гипперссылка),\n'
        'или же у вас есть иные вопросы по работе бота, \n'
        'есть возможность связаться с агентами поддержки!\n\n'
        'Агенты поддержки онлайн:(взять из базы данных агентов онлайн и написать их гипперссылки)\n\n'
        'Агенты поддержки оффлайн:(взять из базы данных агентов онлайн и написать их гипперссылку)',
        parse_mode='HTML',
        disable_web_page_preview=True
    )
