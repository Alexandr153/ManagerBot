from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from typing import Optional

# Основная клавиатура для личных сообщений
from keyboards.reply.main_keyboard import main as kb

'''
    [Статус]
    В работе
    [Описание скрипта]
    Команда в основном меню
    Представлено основное описание бота
    [Исполнители]
    Alexandr153
'''

router = Router()


# Команда /help
@router.message(Command('help', 'start', 'menu', prefix='/!'))
async def cmd_start(message: Message) -> None:
    keyboard: Optional[kb] = kb
    if not message.chat.type == "private":
        keyboard = None
    else:
        pass        # Реализовать функцию с базой данных, заносящую пользователя в список рассылки
    await message.answer(
        'Добро пожаловать в Manager Bot - бот, созданный для всестороннего модерирования чата и развлечения.\n\n'
        'Список всех команд\n'
        'Официальный чат бота\n'
        'Канал с новостями\n'
        'Канал разработчика\n\n'
        'Пользовательское соглашение',
        parse_mode='HTML',
        disable_web_page_preview=True,
        reply_markup=keyboard)
