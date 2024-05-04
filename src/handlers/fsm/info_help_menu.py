from typing import Dict

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from src.keyboard.user.callback import CallbackEnum
from src.keyboard.user.keyboards import info_help_menu, FAQ_menu, go_back_FAQ_menu, get_help_on_road_menu, \
    get_back_info_help_menu

edit_faq = Router()


CallbackDataTexts: Dict[str, str] = {
    CallbackEnum.HELP_ON_ROAD: "текст - предупреждение запроса о помощи",
    CallbackEnum.REQUEST_HELP: "Вы запросили помощь у парка, пожалуйста отправьте свою геопозицию с помощью кнопки клавиатуры ниже.",

    CallbackEnum.MAKE_SUGGESTION: "Напишите нам свои идеи и замечания по поводу парка, которые по вашему мнению требуют внимания или переработки.\n\n"
                                  "Для того чтобы ваше сообщение или замечание были конструктивными, постарайтесь придерживаться следующих рекомендаций:\n"
                                  " ⚡️ Будьте конкретными: указывайте конкретные моменты или проблемы, которые вы хотите обсудить. Избегайте общих фраз и абстрактных идей.\n"
                                  " ⚡️ Предлагайте решения: после того как вы обозначили проблему, предложите возможные пути её решения. Это поможет направить разговор в продуктивное русло.\n"
                                  " ⚡️ Используйте факты и доказательства: подкрепляйте свои утверждения фактами и примерами. Это придаст вашим словам больше веса."
                                  " ⚡️ Будьте уважительными: даже если у вас есть критические замечания, старайтесь выражать их тактично и уважительно. Помните, что ваша цель - конструктивный диалог, а не конфликт.",

    CallbackEnum.BOT_CAPABILITIES: "Текст сообщения для BOT_CAPABILITIES",
    CallbackEnum.TAXOMETR_CAPABILITIES: "Текст сообщения для TAXOMETR_CAPABILITIES",
    CallbackEnum.PARK_COMMISSION: "Текст сообщения для PARK_COMMISSION",
    CallbackEnum.AUTO_LICENSE: "Текст сообщения для AUTO_LICENSE",
    CallbackEnum.SELF_EMPLOYED_INSTRUCTION: "Текст сообщения для SELF_EMPLOYED_INSTRUCTION",

    CallbackEnum.RETURN_BACK: '''Вас приветствует современный парк Экспансия!\n
В данном разделе вы можете найти ответы на все часто задаваемые вопросы, запросить помощь от парка, а так же внести предложение по улучшению работы парка'''
}


class FAQSections(StatesGroup):
    wait_section = State()
    show_section = State()
    wait_suggestion = State()

    wait_help_confirm = State()
    wait_help_location = State()
    wait_help_text = State()

    show_bot_capabilities = State()

    return_back = State()
    back_info_help_menu = State()

@edit_faq.callback_query(FAQSections.back_info_help_menu or FAQSections.wait_help_location or FAQSections.wait_help_confirm, F.data == CallbackEnum.RETURN_BACK)
@edit_faq.callback_query(StateFilter(None), F.data == CallbackEnum.GO_TO_INFO_AND_HELP)
async def get_info_help_menu(callback: CallbackQuery, state: FSMContext) -> None:
    user_message = \
        '''Вас приветствует современный парк Экспансия!\n
    В данном разделе вы можете найти ответы на все часто задаваемые вопросы, запросить помощь от парка, а так же внести предложение по улучшению работы парка'''
    await callback.message.edit_text(user_message, reply_markup=info_help_menu())
    await state.set_state(FAQSections.wait_section)
    print(111)


@edit_faq.callback_query(FAQSections.wait_section, F.data == CallbackEnum.HELP_ON_ROAD)
async def get_help_instructions_menu(callback: CallbackQuery, state: FSMContext) -> None:
    user_message = CallbackDataTexts[callback.data]
    await callback.message.edit_text(user_message, reply_markup=get_help_on_road_menu())
    await state.set_state(FAQSections.wait_help_confirm)
    print()


@edit_faq.callback_query(FAQSections.wait_help_confirm, F.data == CallbackEnum.REQUEST_HELP)
async def get_help_instructions_menu(callback: CallbackQuery, state: FSMContext) -> None:
    user_message = CallbackDataTexts[callback.data]
    await callback.message.edit_text(user_message, reply_markup=get_back_info_help_menu())
    await state.set_state(FAQSections.wait_help_location)



@edit_faq.callback_query(FAQSections.return_back, F.data == CallbackEnum.MAKE_SUGGESTION)
async def get_help_instructions_menu(callback: CallbackQuery, state: FSMContext) -> None:
    user_message = CallbackDataTexts[callback.data]
    await callback.message.edit_text(user_message, reply_markup=get_back_info_help_menu())
    await state.set_state(FAQSections.wait_suggestion)



@edit_faq.message(FAQSections.wait_suggestion)
async def get_help_instructions_menu(message: Message, state: FSMContext) -> None:
    if len(message.text) < 15:
        await message.message.edit_text("Пожалуйста напишите ваше предложение более развернуто!", reply_markup=get_back_info_help_menu())

    else:
        await message.message.edit_text("Ваше сообщение обязательно будет рассмотрено и администрация свяжется с вами при необходимости!"
                                        "Спасибо за ваше участи в жизни нашего парка ❤️",
                                        reply_markup=info_help_menu())
        await state.set_state(FAQSections.back_info_help_menu)



@edit_faq.callback_query(FAQSections.return_back, F.data == CallbackEnum.RETURN_BACK)
@edit_faq.callback_query(FAQSections.wait_section, F.data == CallbackEnum.GO_TO_FAQ)
async def get_faq(callback: CallbackQuery, state: FSMContext) -> None:
    user_message = \
        '''Подраздел часто задаваемые вопросы.'''
    await callback.message.edit_text(user_message, reply_markup=FAQ_menu())
    await state.set_state(FAQSections.show_section)
    print(1)


@edit_faq.callback_query(FAQSections.show_section)
async def show_section(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    if callback.data == CallbackEnum.BOT_CAPABILITIES:
        menu_text = CallbackDataTexts[callback.data]
        await callback.message.edit_text(menu_text, reply_markup=info_help_menu()) # меню для описания функционала бота (гиф)
        print("other")
    elif callback.data == CallbackEnum.RETURN_BACK:
        menu_text = CallbackDataTexts[callback.data]
        await callback.message.edit_text(menu_text, reply_markup=info_help_menu())
        await state.set_state(FAQSections.return_back)
        print(111)
    else:
        menu_text = CallbackDataTexts[callback.data]
        await callback.message.edit_text(menu_text, reply_markup=go_back_FAQ_menu())
        await state.set_state(FAQSections.return_back)
