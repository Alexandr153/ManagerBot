from core.utils.commands import set_commands
from aiogram import Router, Bot

import logging

'''
    [Статус]
    Своевременное дополнение
    [Описание скрипта]
    Основные состояния бота
    [Исполнители]
    Alexandr153
'''

router = Router()

logger = logging.getLogger(__name__)


# При запуске бота
@router.startup()
async def start_bot(bot: Bot) -> None:
    await set_commands(bot)
    logger.debug('Бот начал работу')


# При завершении работы боты
@router.shutdown()
async def stop_bot() -> None:
    logger.debug('Бот завершил работу')