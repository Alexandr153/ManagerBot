import asyncio
import logging.config
from aiogram import Bot, Dispatcher
from config.config import load_config

from core.handlers.interface.commands_menu import start
from core.handlers.interface.commands_menu import support
from core.states import states

from logging_settings.logging_settings import logging_config


async def main() -> None:
    # Подгрузка конфигурации
    config = load_config()
    API_TOKEN = config.tg_bot.token

    bot: Bot = Bot(API_TOKEN)
    dp: Dispatcher = Dispatcher()

    # Настройка базовой конфигурации логгирования
    logging.config.dictConfig(logging_config)

    # Подключение роутеров
    dp.include_router(states.router)
    dp.include_router(start.router)
    dp.include_router(support.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
