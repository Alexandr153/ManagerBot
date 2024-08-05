import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import API_TOKEN

from core.handlers.Interface.CommandsMenu import start
from core.handlers.Interface.CommandsMenu import support
from core.states import states


async def main() -> None:
    bot: Bot = Bot(API_TOKEN)
    dp: Dispatcher = Dispatcher()

    logging.basicConfig(level=logging.INFO)

    # Подключение роутеров
    dp.include_router(states.router)
    dp.include_router(start.router)
    dp.include_router(support.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
