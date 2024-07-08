from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


# Инлайн команды
async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='1'
        ),
        BotCommand(
            command='support',
            description='2'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())