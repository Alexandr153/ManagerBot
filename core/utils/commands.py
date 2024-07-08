from aiogram.types import BotCommand, BotCommandScopeDefault


# Инлайн команды
async def set_commands(bot):
    commands = [
        BotCommand(
            command='start',
            description='123'
        ),
        BotCommand(
            command='support',
            description='234'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())