import asyncio
import logging.config

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config.config import Config, load_config
from aiogram.client.default import DefaultBotProperties

from handlers.interface.commands_menu import support, start
from states import states

from logging_settings.logging_settings import logging_config

# Настройка базовой конфигурации логгирования
logging.config.dictConfig(logging_config)

# Инициализируем логгер
logger = logging.getLogger(__name__)

logger.info('Конфиг логирования загружен')


async def main() -> None:
    logger.info('Запуск бота...')
    # Подгрузка конфигурации
    config: Config = load_config()
    API_TOKEN = config.tg_bot.token

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(
        token=API_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp: Dispatcher = Dispatcher()

    logger.info('Подключение роутеров')
    # Подключение роутеров
    dp.include_router(states.router)
    dp.include_router(start.router)
    dp.include_router(support.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
