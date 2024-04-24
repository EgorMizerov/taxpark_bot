from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from src.keyboard.user.text import ButtonTextDict


def signup_markup() -> ReplyKeyboardMarkup:
    sing_up_button = KeyboardButton(
        text=ButtonTextDict['sign_up'],
        request_contact=True,
    )
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True, keyboard=[[sing_up_button]])
    return markup
