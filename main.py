import asyncio
from aiogram import Bot, Dispatcher
from config.config import API_TOKEN

from core.handlers.GroupInterface.CommandsMenu import start
from core.states import states


async def main() -> None:
    bot: Bot = Bot(API_TOKEN)
    dp: Dispatcher = Dispatcher()

    dp.include_router(states.router)
    dp.include_router(start.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
