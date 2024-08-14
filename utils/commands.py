from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot

'''
    [Статус]
    В работе
    [Описание скрипта]
    Меню с основными командами
    [Исполнители]
    Alexandr153
'''


# Встроенные инлайн команды
async def set_commands(bot: Bot) -> None:
    commands = [
        BotCommand(
            command='start',
            description='Описание бота'
        ),
        BotCommand(
            command='support',
            description='Агенты поддержки'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
