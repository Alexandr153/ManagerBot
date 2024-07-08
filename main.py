import asyncio
from core.config.config import bot, dp

# Commands and handlers and more...
import core.states.states
import core.handlers.GroupInterface.CommandsMenu.start


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
