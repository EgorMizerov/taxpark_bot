import asyncio
from configparser import ConfigParser
from typing import Callable, Dict, Any, Awaitable, Mapping

from aiogram import Dispatcher, BaseMiddleware, Router
from aiogram.types import Message
from bson import ObjectId
from pymongo import MongoClient
from pymongo.database import Database

from bot import bot
from handlers.admin_handler import admin_handler
from handlers.user_handler import user_handler, auth_handler
from handlers.command_handler import command_handler
from handlers.fsm.create_employee import create_employee
from src.handlers.middleware import AuthMiddleware
from src.models.user import User
from src.repository.user_repository import UserRepository


def register_routers(dp: Dispatcher) -> None:
    router = Router()
    router.message.middleware(AuthMiddleware(UserRepository(database=dp['db'])))

    router.include_router(admin_handler)
    router.include_router(user_handler)
    router.include_router(command_handler)
    router.include_router(create_employee)

    dp.include_router(router)
    dp.include_router(auth_handler)


def register_arguments(dp: Dispatcher, config: ConfigParser) -> None:
    dp['config'] = config
    dp['admin_id'] = config.getint('general', 'admin_id')


# TODO: inject arguments for connection string
def register_db(dp: Dispatcher) -> None:
    client = MongoClient("mongodb://localhost:27017")
    database = client["taxpark"]
    dp['db'] = database


async def main() -> None:
    config = ConfigParser()
    config.read('config.ini')

    dp = Dispatcher()
    register_db(dp)
    register_routers(dp)
    register_arguments(dp, config)

    print("Bot is running")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
