import datetime
from typing import List, Tuple

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from bson import ObjectId

from src.bot import bot
from src.keyboard.admin.callback import CallbackEnum
from src.keyboard.admin.keyboards import admin_cancel_make_employee, admin_start_markup, create_employee_save
from src.models.user import User, DriverLicense
from src.repository.user_repository import UserRepository

create_employee = Router()


class CreateEmployeeState(StatesGroup):
    last_name = State()
    first_name = State()
    middle_name = State()
    user_id = State()
    phone = State()
    starting_v_date = State()
    seria_and_number = State()
    country = State()
    date_of_issue = State()
    date_of_expired = State()
    save_employee = State()


@create_employee.callback_query(F.data == CallbackEnum.CANCEL_MAKE_EMPLOYEE)
async def cancel_creating_employee(callback: CallbackQuery, state: FSMContext) -> None:
    for msg_id in await get_message_ids(state):
        await bot.delete_message(callback.message.chat.id, msg_id)

    await state.clear()
    await callback.message.edit_text(
        f'Меню администратора',
        reply_markup=admin_start_markup(),
    )


@create_employee.callback_query(StateFilter(CreateEmployeeState.save_employee), F.data == CallbackEnum.SAVE_EMPLOYEE)
async def make_employee(callback: CallbackQuery, state: FSMContext, user_repository: UserRepository) -> None:
    user = await build_user_from_state(state)
    user_repository.save(user)
    await cancel_creating_employee(callback, state)


async def build_user_from_state(state: FSMContext) -> User:
    state_data = await state.get_data()
    user = User(
        id=ObjectId(),
        telegram_id=state_data['user_id'],
        first_name=state_data['first_name'],
        middle_name=state_data['middle_name'],
        last_name=state_data['last_name'],
        phone_number=state_data['phone'],
        driver_license=DriverLicense(
            number=state_data['seria_and_number'],
            driver_license_experience=state_data['starting_v_date'],
            issue_date=state_data['date_of_issue'],
            expiry_date=state_data['date_of_expired'],
            country='rus'
        ),
        created_at=datetime.datetime.now(),
    )
    return user


@create_employee.callback_query(StateFilter(None), F.data == CallbackEnum.MAKE_EMPLOYEE)
async def make_employee(callback: CallbackQuery, state: FSMContext) -> None:
    user_info_message = 'Данные пользователя'
    menu_message = user_info_message + '\n\nВведите фамилию пользователя'
    await callback.message.edit_text(menu_message, reply_markup=admin_cancel_make_employee())
    await state.update_data(menu=callback, user_info_message=user_info_message)
    await state.set_state(CreateEmployeeState.last_name)


@create_employee.message(CreateEmployeeState.last_name, F.text)
async def input_last_name(message: Message, state: FSMContext) -> None:
    await state.update_data(last_name=message.text, telegram_id=int(message.from_user.id))
    await append_message_id(state, message.message_id)
    await edit_menu(f'Фамилия: {message.text}', 'Введиет имя пользователя', state)
    await state.set_state(CreateEmployeeState.first_name)


@create_employee.message(CreateEmployeeState.first_name, F.text)
async def input_first_name(message: Message, state: FSMContext) -> None:
    await state.update_data(first_name=message.text)
    await append_message_id(state, message.message_id)
    await edit_menu(f'Имя: {message.text}', 'Введиет отчество пользователя', state)
    await state.set_state(CreateEmployeeState.middle_name)


@create_employee.message(CreateEmployeeState.middle_name, F.text)
async def input_middle_name(message: Message, state: FSMContext) -> None:
    await state.update_data(middle_name=message.text)
    await append_message_id(state, message.message_id)
    await edit_menu(f'Отчество: {message.text}', 'Введиет id пользователя', state)
    await state.set_state(CreateEmployeeState.user_id)


@create_employee.message(CreateEmployeeState.user_id, F.text)
async def input_user_id(message: Message, state: FSMContext) -> None:
    await state.update_data(user_id=message.text)
    await append_message_id(state, message.message_id)
    await edit_menu(f'Идентификатор: {message.text}', 'Введите номер телефона', state)
    await state.set_state(CreateEmployeeState.phone)


@create_employee.message(CreateEmployeeState.phone, F.text)
async def input_phone(message: Message, state: FSMContext) -> None:
    await state.update_data(phone=message.text)
    await append_message_id(state, message.message_id)
    await edit_menu(f'Номер телефона: {message.text}', 'Введите начальную дату вождения пользователя (в формате дд.мм.гггг)', state)
    await state.set_state(CreateEmployeeState.starting_v_date)


@create_employee.message(CreateEmployeeState.starting_v_date, F.text)
async def input_starting_v_date(message: Message, state: FSMContext) -> None:
    await append_message_id(state, message.message_id)

    starting_v_date, ok = await get_date(message.text)
    if not ok:
        answer = await message.answer('Invalid input date')
        await append_message_id(state, answer.message_id)
        return

    await state.update_data(starting_v_date=starting_v_date)
    await edit_menu(f'Начальная дата вождения: {message.text}', 'Введите серию и номер ВУ пользователя', state)
    await state.set_state(CreateEmployeeState.seria_and_number)

@create_employee.message(CreateEmployeeState.seria_and_number, F.text)
async def input_seria_and_number(message: Message, state: FSMContext) -> None:
    await state.update_data(seria_and_number=message.text)
    await append_message_id(state, message.message_id)
    await edit_menu(f'Серия и номер ВУ: {message.text}', 'Введите страну выдачи ВУ пользователя', state)
    await state.set_state(CreateEmployeeState.country)


@create_employee.message(CreateEmployeeState.country, F.text)
async def input_country(message: Message, state: FSMContext) -> None:
    await state.update_data(country=message.text)
    await append_message_id(state, message.message_id)
    await edit_menu(f'Страна выдачи ВУ: {message.text}', 'Введите дату выдачи ВУ пользователю', state)
    await state.set_state(CreateEmployeeState.date_of_issue)


@create_employee.message(CreateEmployeeState.date_of_issue, F.text)
async def input_date_of_issue(message: Message, state: FSMContext) -> None:
    await append_message_id(state, message.message_id)

    date_of_issue, ok = await get_date(message.text)
    if not ok:
        answer = await message.answer('Invalid input date')
        await append_message_id(state, answer.message_id)
        return

    await state.update_data(date_of_issue=date_of_issue)
    await edit_menu(f'Дата выдачи ВУ: {message.text}', 'Введите дату до которой действительно ВУ (в формате дд.мм.гггг)', state)
    await state.set_state(CreateEmployeeState.date_of_expired)


@create_employee.message(CreateEmployeeState.date_of_expired, F.text)
async def input_date_of_expired(message: Message, state: FSMContext) -> None:
    await append_message_id(state, message.message_id)

    date_of_expired, ok = await get_date(message.text)
    if not ok:
        answer = await message.answer('Invalid input date')
        await append_message_id(state, answer.message_id)
        return

    await state.update_data(date_of_expired=date_of_expired)
    await edit_menu(f'Дата до которой действительно ВУ: {message.text}', 'Карточка пользователя заполнена, данному пользователю сгенерирован ключ - vNSnq@rn-', state, full_data=True)
    await state.set_state(CreateEmployeeState.save_employee)


async def edit_menu(user_data: str, input_message: str, state: FSMContext, **kwargs) -> None:
    state_data = await state.get_data()
    state_data = await state.update_data(user_info_message=state_data.get('user_info_message')+f'\n{user_data}')
    user_info_message = state_data.get('user_info_message')
    menu_message = user_info_message + f'\n\n{input_message}'
    menu = state_data.get('menu')

    if kwargs.get('full_data') is True:
        await menu.message.edit_text(menu_message, reply_markup=create_employee_save())
    else:
        await menu.message.edit_text(menu_message, reply_markup=admin_cancel_make_employee())


async def append_message_id(state: FSMContext, id: int) -> None:
    data = await state.get_data()

    message_ids: List[int] = data.get('message_ids')
    if message_ids is None:
        message_ids = list()

    message_ids.append(id)
    data.update({'message_ids': message_ids})
    await state.update_data(data)


async def get_message_ids(state: FSMContext) -> List[int]:
    data = await state.get_data()
    message_ids: List[int] = data.get('message_ids')
    if message_ids is None or len(message_ids) == 0:
        return list()

    return message_ids


async def get_date(message: str) -> Tuple[str, bool]:
    args = message.split('.')
    if len(args) != 3:
        return '', False

    try:
        year = int(args[2])
        month = "{:02d}".format(int(args[1]))
        day = "{:02d}".format(int(args[0]))

        return f'{year}.{month}.{day}', True
    except:
        return '', False
