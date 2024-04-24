from aiogram import Router, F
from aiogram.types import Message

from src.bot import bot
from src.keyboard.user.keyboards import start_markup

user_handler = Router()


async def user_start(message: Message) -> None:
    await message.answer(f'Меню пользователя', reply_markup=start_markup())


@user_handler.message(F.contact)
async def handle_user_contact(message: Message, admin_id: int) -> None:
    await send_contact_to_admin(message, admin_id)
    message_text = '''Спасибо, что доверились нам!\n
Наш администратор свяжется с вами через пару минут для подтверждения личности, пожалуйста ожидайте.'''
    await message.answer(message_text, reply_markup=None)


async def send_contact_to_admin(message: Message, admin_id: int) -> None:
    await bot.forward_message(
        chat_id=admin_id,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
    )

    message_text = '''Пользователя зовут - {user_name}
id пользователя - {user_id}
его номер телефона - {phone_number}'''

    await bot.send_message(
        chat_id=admin_id,
        text=message_text.format(
            user_name=message.from_user.first_name,
            user_id=message.from_user.id,
            phone_number=message.contact.phone_number,
        ))