from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.keyboard.admin.callback import CallbackEnum
from src.keyboard.admin.text import ButtonTextDict


def admin_start_markup() -> InlineKeyboardMarkup:
    make_new_employee_button = InlineKeyboardButton(
        text=ButtonTextDict['make_employee'],
        callback_data=CallbackEnum.MAKE_EMPLOYEE,
    )
    cancel_registration_button = InlineKeyboardButton(
        text=ButtonTextDict['cancel_registration'],
        callback_data=CallbackEnum.CANCEL_MAKE_EMPLOYEE,
    )
    first_row = [make_new_employee_button]
    second_row = [cancel_registration_button]
    lines = [first_row, second_row]
    inline_markup = InlineKeyboardMarkup(inline_keyboard=lines)
    return inline_markup


def admin_cancel_make_employee() -> InlineKeyboardMarkup:
    cancel_registration_button = InlineKeyboardButton(
        text=ButtonTextDict['cancel_registration'],
        callback_data=CallbackEnum.CANCEL_MAKE_EMPLOYEE,
    )
    second_row = [cancel_registration_button]
    lines = [second_row]
    inline_markup = InlineKeyboardMarkup(inline_keyboard=lines)
    return inline_markup
