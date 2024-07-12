from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, Bot
from core.filters.IsAdmin import IsAdmin
from config.config import admin_ids

# Основная клавиатура для личных сообщений
from core.keyboards.reply.MainKeyboard import main as kb

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
@router.message(Command('help', 'start', prefix='/!'))
async def cmd_start(message: Message) -> None:
    await message.answer('Добро пожаловать в Manager Bot - бот, созданный для всестороннего модерирования чата и развлечения.\n\n'
                         'Список всех команд\n'
                         'Официальный чат бота\n'
                         'Канал с новостями\n'
                         'Канал разработчика\n\n'
                         'Пользовательское соглашение',
                         parse_mode='HTML',
                         disable_web_page_preview=True,
                         reply_markup=kb)


# Этот хэндлер будет срабатывать, если апдейт от админа
@router.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
@router.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')

