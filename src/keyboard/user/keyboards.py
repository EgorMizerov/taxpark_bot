from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from src.keyboard.user.text import ButtonTextDict


def start_markup() -> ReplyKeyboardMarkup:
    sing_up_button = KeyboardButton(
        text=ButtonTextDict['sign_up'],
        request_contact=True,
    )
    sign_in_button = KeyboardButton(
        text=ButtonTextDict['sign_in'],
    )
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True, keyboard=[[sing_up_button, sign_in_button]])
    return markup
