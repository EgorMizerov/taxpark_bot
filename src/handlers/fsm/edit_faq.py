from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery

from src.keyboard.user.callback import CallbackEnum
from src.keyboard.user.keyboards import info_help_menu, FAQ_menu, go_back_FAQ_menu

edit_faq = Router()


class FAQSections(StatesGroup):
    wait_section = State()
    show_section = State()


@edit_faq.callback_query(F.data == CallbackEnum.GO_TO_INFO_AND_HELP)
async def get_info_help_menu(callback: CallbackQuery, state: FSMContext) -> None:
    user_message = \
        '''Вас приветствует современный парк Экспансия!\n
        В данном разделе вы можете найти ответы на все часто задаваемые вопросы, запросить помощь от парка, а так же внести предложение по улучшению работы парка'''
    await callback.answer(text=user_message, markup=info_help_menu())


@edit_faq.callback_query(F.data == CallbackEnum.GO_TO_FAQ, StateFilter(None))
async def get_faq(callback: CallbackQuery, state: FSMContext) -> None:
    user_message = \
        '''Раздел часто задаваемые вопросы.'''
    await callback.answer(text=user_message, markup=FAQ_menu())
    await state.set_state('wait_section')
    await state.update_data(menu=callback, user_message=user_message)


@edit_faq.callback_query(func=lambda call: True)
async def faq_text(call, state: FSMContext) -> None:
    if call.data == CallbackEnum.BOT_CAPABILITIES:
        await call.message.edit_text(menu=call, reply_markup=go_back_FAQ_menu())
        await edit_menu(f'Подраздел возможности бота: ', state)
    elif call.data == CallbackEnum.TOXOMETR_CAPABILITIES:
        await call.message.edit_text(menu=call, reply_markup=go_back_FAQ_menu())
        await edit_menu(f'Подраздел возможности таксометра: ', state)
    elif call.data == CallbackEnum.PARK_COMMISSION:
        await call.message.edit_text(menu=call, reply_markup=go_back_FAQ_menu())
        await edit_menu(f'Подраздел информации о комиссии парка: ', state)
    elif call.data == CallbackEnum.AUTO_LICENSE:
        await call.message.edit_text(menu=call, reply_markup=go_back_FAQ_menu())
        await edit_menu(f'Подраздел информации для получения лицензии на авто: ', state)
    elif call.data == CallbackEnum.SELF_EMPLOYED_INSTRUCTION:
        await call.message.edit_text(menu=call, reply_markup=go_back_FAQ_menu())
        await edit_menu(f'Подраздел информации для оформления самозанятым: ', state)



async def edit_menu(input_message: str, state: FSMContext, **kwargs) -> None:
    state_data = await state.get_data()
    state_data = await state.update_data(
        user_message=state_data.get('user_message'))
    user_message = state_data.get('user_message')
    menu_message = user_message + f'\n\n{input_message}'
    menu = state_data.get('menu')

    if kwargs.get('full_data') is True:
        await menu.message.edit_text(menu_message, reply_markup=go_back_FAQ_menu())
    else:
        await menu.message.edit_text(menu_message, reply_markup=FAQ_menu())
