from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from src.keyboard.user.callback import CallbackEnum
from src.keyboard.user.text import ButtonTextDict


def signup_markup() -> ReplyKeyboardMarkup:
    sing_up_button = KeyboardButton(
        text=ButtonTextDict['sign_up'],
        request_contact=True,
    )
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True, keyboard=[[sing_up_button]])
    return markup


def user_menu_markup() -> InlineKeyboardMarkup:
    current_order_button = InlineKeyboardButton(
        text=ButtonTextDict['go_to_current_order'],
        callback_data=CallbackEnum.GO_TO_CURRENT_ORDER,
    )
    start_shift_button = InlineKeyboardButton(
        text=ButtonTextDict['start_shift'],
        callback_data=CallbackEnum.START_SHIFT
    )
    user_statistics_button = InlineKeyboardButton(
        text=ButtonTextDict['go_to_user_statistics'],
        callback_data=CallbackEnum.GO_TO_USER_STATISTICS,
    )
    profile_manager_button = InlineKeyboardButton(
        text=ButtonTextDict['go_to_profile_manager'],
        callback_data=CallbackEnum.GO_TO_PROFILE_MANAGER
    )
    promotions_statistics_button = InlineKeyboardButton(
        text=ButtonTextDict['go_to_promotions_statistics'],
        callback_data=CallbackEnum.GO_TO_PROMOTION_STATISTICS
    )
    info_and_help_button = InlineKeyboardButton(
        text=ButtonTextDict['go_to_info_and_help'],
        callback_data=CallbackEnum.GO_TO_INFO_AND_HELP
    )
    faq_button = InlineKeyboardButton(
        text=ButtonTextDict['go_to_FAQ'],
        callback_data=CallbackEnum.GO_TO_FAQ
    )
    subscription_services_button = InlineKeyboardButton(
        text=ButtonTextDict['go_to_subscription_services'],
        callback_data=CallbackEnum.GO_TO_SUBSCRIPTION_SERVICES
    )
    first_row = [current_order_button]
    second_row = [start_shift_button, user_statistics_button]
    third_row = [promotions_statistics_button, profile_manager_button]
    fourth_row = [faq_button, info_and_help_button]
    fifth_row = [subscription_services_button]
    lines = [first_row, second_row, third_row, fourth_row, fifth_row]
    markup = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, inline_keyboard=lines)
    return markup


def current_order_menu() -> InlineKeyboardMarkup:
    cancel_finished_order_button = InlineKeyboardButton(
        text=ButtonTextDict['cancel_finished_order'],
        callback_data=CallbackEnum.CANCEL_FINISHED_ORDER
    )
    cancel_not_finished_order_button = InlineKeyboardButton(
        text=ButtonTextDict['cancel_not_finished_order'],
        callback_data=CallbackEnum.CANCEL_NOT_FINISHED_ORDER
    )
    return_main_menu_button = InlineKeyboardButton(
        text=ButtonTextDict['return_main_menu'],
        callback_data=CallbackEnum.RETURN_MAIN_MENU
    )
    first_row = [cancel_finished_order_button]
    second_row = [cancel_not_finished_order_button]
    third_row = [return_main_menu_button]
    lines = [first_row, second_row, third_row]
    markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard=lines)
    return markup


def user_statistics_menu() -> InlineKeyboardMarkup:
    statistics_period = InlineKeyboardButton(
        text=ButtonTextDict['statistics_period'],
        callback_data=CallbackEnum.STATISTICS_PERIOD
    )
    statistics_variants = InlineKeyboardButton(
        text=ButtonTextDict['statistics_variants'],
        callback_data=CallbackEnum.STATISTICS_VARIANTS
    )
    return_main_menu_button = InlineKeyboardButton(
        text=ButtonTextDict['return_main_menu'],
        callback_data=CallbackEnum.RETURN_MAIN_MENU
    )
    first_row = [statistics_period]
    second_row = [statistics_variants]
    third_row = [return_main_menu_button]
    lines = [first_row, second_row, third_row]
    markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard=lines)
    return markup
