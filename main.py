import asyncio
import logging.config
from aiogram import Bot, Dispatcher
from config.config import API_TOKEN

from core.handlers.interface.commands_menu import start
from core.handlers.interface.commands_menu import support
from core.states import states

from logging_settings.logging_settings import logging_config


async def main() -> None:
    bot: Bot = Bot(API_TOKEN)
    dp: Dispatcher = Dispatcher()

    logging.config.dictConfig(logging_config)

    # Подключение роутеров
    dp.include_router(states.router)
    dp.include_router(start.router)
    dp.include_router(support.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
