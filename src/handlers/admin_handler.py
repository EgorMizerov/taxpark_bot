from aiogram import Router
from aiogram.types import Message

from src.keyboard.admin.keyboards import admin_start_markup

admin_handler = Router()


async def admin_start(message: Message) -> None:
    await message.answer(f'Меню администратора', reply_markup=admin_start_markup())
