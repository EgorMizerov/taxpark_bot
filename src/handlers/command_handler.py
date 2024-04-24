from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.handlers.admin_handler import admin_start
from src.handlers.user_handler import user_start

command_handler = Router()


@command_handler.message(CommandStart())
async def start(message: Message, admin_id: int) -> None:
    if is_admin(message, admin_id):
        await admin_start(message)
    else:
        await user_start(message)


def is_admin(message: Message, admin_id: int) -> bool:
    print(message.from_user.id, admin_id)
    return message.from_user.id == admin_id
