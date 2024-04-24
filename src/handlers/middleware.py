from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from src.keyboard.user.keyboards import signup_markup
from src.repository.user_repository import UserRepository


class AuthMiddleware(BaseMiddleware):
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user = self.user_repository.find_one_by({'telegram_id': event.from_user.id})
        if user is None:
            return await event.answer(text='Регистрация', reply_markup=signup_markup())
        return await handler(event, data)
