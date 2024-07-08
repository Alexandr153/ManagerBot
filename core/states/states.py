from core.utils.commands import set_commands
from aiogram import Router, Bot

router = Router()


@router.startup()
async def start_bot(bot: Bot) -> None:
    await set_commands(bot)
    print("[-] Бот начал работу")


@router.shutdown()
async def stop_bot() -> None:
    print("[-] Бот закончил работу")