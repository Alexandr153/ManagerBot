from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

router = Router()


@router.message(Command('help', 'start'))
async def cmd_start(message: Message) -> None:
    await message.answer('Добро пожаловать в Manager Bot - бот, созданный для всестороннего модерирования чата и развлечения.\n\n'
                         'Список всех команд\n'
                         'Официальный чат бота\n'
                         'Канал с новостями\n'
                         'Канал разработчика\n\n'
                         'Пользовательское соглашение',
                         parse_mode='HTML',
                         disable_web_page_preview=True)


