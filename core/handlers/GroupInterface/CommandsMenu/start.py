from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

# Основная клавиатура для личных сообщений
from core.keyboards.reply.MainKeyboard import main as kb

router = Router()


# Команда /help
@router.message(Command('help', 'start'))
async def cmd_start(message: Message) -> None:
    if message.chat.type != 'private':
        kb = None
    await message.answer('Добро пожаловать в Manager Bot - бот, созданный для всестороннего модерирования чата и развлечения.\n\n'
                         'Список всех команд\n'
                         'Официальный чат бота\n'
                         'Канал с новостями\n'
                         'Канал разработчика\n\n'
                         'Пользовательское соглашение',
                         parse_mode='HTML',
                         disable_web_page_preview=True,
                         reply_markup=kb)


