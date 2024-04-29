import asyncio
from configparser import ConfigParser

from aiogram import Dispatcher, Router
from pymongo import MongoClient

from bot import bot
from handlers.admin_handler import admin_handler
from handlers.user_handler import user_handler, auth_handler
from handlers.command_handler import command_handler
from handlers.fsm.create_employee import create_employee
from src.handlers.middleware import AuthMiddleware
from src.repository.user_repository import UserRepository
from src.yandex.client import YandexAPI


def include_routes(dp: Dispatcher) -> None:
    router = Router()
    router.message.middleware(AuthMiddleware(UserRepository(database=dp['db'])))

    router.include_router(user_handler)

    dp.include_router(router)
    dp.include_router(auth_handler)
    dp.include_router(command_handler)
    dp.include_router(admin_handler)
    dp.include_router(create_employee)


def register_arguments(dp: Dispatcher, config: ConfigParser) -> None:
    dp['config'] = config
    dp['admin_id'] = config.getint('general', 'admin_id')


# TODO: inject arguments for connection string
def inject_db(dp: Dispatcher,  config: ConfigParser) -> None:
    client = MongoClient(config.get('database', 'url'))
    database = client["taxpark"]
    dp['db'] = database
    dp['user_repository'] = UserRepository(database)


def inject_yandex_client(dp: Dispatcher, config: ConfigParser) -> None:
    client = YandexAPI(
        client_id=config.get('yandex_api', 'client_id'),
        api_key=config.get('yandex_api', 'api_key'),
        park_id=config.get('yandex_api', 'park_id')
    )
    dp['yandex_client'] = client


async def main() -> None:
    config = ConfigParser()
    config.read('config.ini')

    dp = Dispatcher()
    dp['config'] = config
    dp['admin_id'] = config.getint('general', 'admin_id')

    inject_db(dp, config)
    include_routes(dp)
    inject_yandex_client(dp, config)

    print("Bot is running")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
