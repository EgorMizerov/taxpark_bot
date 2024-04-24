import asyncio
from configparser import ConfigParser
from typing import Callable, Dict, Any, Awaitable

from aiogram import Dispatcher, BaseMiddleware
from aiogram.types import Message

from bot import bot
from handlers.admin_handler import admin_handler
from handlers.user_handler import user_handler
from handlers.command_handler import command_handler
from handlers.fsm.create_employee import create_employee


def register_routers(dp: Dispatcher) -> None:
    dp.include_router(admin_handler)
    dp.include_router(user_handler)
    dp.include_router(command_handler)
    dp.include_router(create_employee)


def register_arguments(dp: Dispatcher, config: ConfigParser) -> None:
    dp['config'] = config
    dp['admin_id'] = config.getint('general', 'admin_id')


async def main() -> None:
    config = ConfigParser()
    config.read('config.ini')

    dp = Dispatcher()
    register_routers(dp)
    register_arguments(dp, config)

    print("Bot is running")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
