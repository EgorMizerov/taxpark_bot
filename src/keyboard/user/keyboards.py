from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
admin = config.get('general', 'admin_url')

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
    subscription_services_button = InlineKeyboardButton(
        text=ButtonTextDict['go_to_subscription_services'],
        callback_data=CallbackEnum.GO_TO_SUBSCRIPTION_SERVICES
    )
    first_row = [current_order_button]
    second_row = [start_shift_button, user_statistics_button]
    third_row = [promotions_statistics_button, profile_manager_button]
    fourth_row = [info_and_help_button]
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


def user_promotions_menu() -> InlineKeyboardMarkup:
    promotions_info_button = InlineKeyboardButton(
        text=ButtonTextDict['promotions_info'],
        callback_data=CallbackEnum.PROMOTIONS_INFO
    )
    copy_referal_button = InlineKeyboardButton(
        text=ButtonTextDict['copy_referal'],
        callback_data=CallbackEnum.COPY_REFERAL
    )
    return_main_menu_button = InlineKeyboardButton(
        text=ButtonTextDict['return_main_menu'],
        callback_data=CallbackEnum.RETURN_MAIN_MENU
    )
    first_row = [promotions_info_button]
    second_row = [copy_referal_button]
    third_row = [return_main_menu_button]
    lines = [first_row, second_row, third_row]
    markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard=lines)
    return markup


def promotions_info_menu() -> InlineKeyboardMarkup:
    refer_friend_button = InlineKeyboardButton(
        text=ButtonTextDict['refer_friend'],
        callback_data=CallbackEnum.REFER_FRIEND
    )
    no_commission_month_button = InlineKeyboardButton(
        text=ButtonTextDict['no_commission_month'],
        callback_data=CallbackEnum.NO_COMMISSION_MONTH
    )
    return_back_button = InlineKeyboardButton(
        text=ButtonTextDict['return_back'],
        callback_data=CallbackEnum.RETURN_BACK
    )
    return_main_menu_button = InlineKeyboardButton(
        text=ButtonTextDict['return_main_menu'],
        callback_data=CallbackEnum.RETURN_MAIN_MENU
    )
    first_row = [refer_friend_button]
    second_row = [no_commission_month_button]
    third_row = [return_back_button]
    fourth_row = [return_main_menu_button]
    lines = [first_row, second_row, third_row, fourth_row]
    markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard=lines)
    return markup

def info_help_menu() -> InlineKeyboardMarkup:
    faq_button = InlineKeyboardButton(
        text=ButtonTextDict['go_to_FAQ'],
        callback_data=CallbackEnum.GO_TO_FAQ
    )
    help_on_road_button = InlineKeyboardButton(
        text=ButtonTextDict['help_on_road'],
        callback_data=CallbackEnum.HELP_ON_ROAD
    )
    make_suggestion_button = InlineKeyboardButton(
        text=ButtonTextDict['make_suggestion'],
        callback_data=CallbackEnum.MAKE_SUGGESTION
    )
    return_main_menu_button = InlineKeyboardButton(
        text=ButtonTextDict['return_main_menu'],
        callback_data=CallbackEnum.RETURN_MAIN_MENU
    )
    first_row = [faq_button]
    second_row = [help_on_road_button]
    third_row = [make_suggestion_button]
    fourth_row = [return_main_menu_button]
    lines = [first_row, second_row, third_row, fourth_row]
    markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard=lines)
    return markup


def get_help_on_road_menu() -> InlineKeyboardMarkup:
    request_help_button = InlineKeyboardButton(
        text=ButtonTextDict['request_help'],
        callback_data=CallbackEnum.REQUEST_HELP
    )
    return_back_button = InlineKeyboardButton(
        text=ButtonTextDict['return_back'],
        callback_data=CallbackEnum.RETURN_BACK
    )
    markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard=[[request_help_button], [return_back_button]])
    return markup


def get_back_info_help_menu() -> InlineKeyboardMarkup:
    return_back_button = InlineKeyboardButton(
        text=ButtonTextDict['return_back'],
        callback_data=CallbackEnum.RETURN_BACK
    )
    markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard=[[return_back_button]])
    return markup


def FAQ_menu() -> InlineKeyboardMarkup:
    bot_capabilites_button = InlineKeyboardButton(
        text=ButtonTextDict['bot_capabilities'],
        callback_data=CallbackEnum.BOT_CAPABILITIES
    )
    taxometr_capabilites_button = InlineKeyboardButton(
        text=ButtonTextDict['taxometr_capabilities'],
        callback_data=CallbackEnum.TAXOMETR_CAPABILITIES
    )
    park_commission_button = InlineKeyboardButton(
        text=ButtonTextDict['park_commission'],
        callback_data=CallbackEnum.PARK_COMMISSION
    )
    auto_license_button = InlineKeyboardButton(
        text=ButtonTextDict['auto_license'],
        callback_data=CallbackEnum.AUTO_LICENSE
    )
    self_employed_instructions_button = InlineKeyboardButton(
        text=ButtonTextDict['self_employed'],
        callback_data=CallbackEnum.SELF_EMPLOYED_INSTRUCTION
    )
    jump_taxi_url_button = InlineKeyboardButton(
        text=ButtonTextDict['jump_taxi'],
        callback_data=CallbackEnum.JUMP_TAXI_URL,
        url='https://my.jump.taxi/'
    )
    admin_contact_button = InlineKeyboardButton(
        text=ButtonTextDict['admin_contact'],
        callback_data=CallbackEnum.ADMIN_CONTACT,
        url=admin              # Замена на админ аккаунт для рабочего телеграмм
    )
    return_back_button = InlineKeyboardButton(
        text=ButtonTextDict['return_back'],
        callback_data=CallbackEnum.RETURN_BACK
    )
    first_row = [bot_capabilites_button, taxometr_capabilites_button]
    second_row = [park_commission_button]
    third_row = [auto_license_button, self_employed_instructions_button]
    fourth_row = [jump_taxi_url_button, admin_contact_button]
    fifth_row = [return_back_button]
    lines = [first_row, second_row, third_row, fourth_row, fifth_row]
    markup = InlineKeyboardMarkup(row_width=5, resize_keyboard=True, inline_keyboard=lines)
    return markup


def go_back_FAQ_menu() -> InlineKeyboardMarkup:
    return_back_button = InlineKeyboardButton(
        text=ButtonTextDict['return_back'],
        callback_data=CallbackEnum.RETURN_BACK
    )
    lines =[[return_back_button]]
    markup = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, inline_keyboard=lines)
    return markup
