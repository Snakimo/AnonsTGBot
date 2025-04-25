from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import Message, CallbackQuery

from create_event.CE_keyboards import CE_keyboard
from users.keyboard_users import poll_keyboard
from create_event.CE_functions import bild_text, check_id
from start_menu.SM_handlers import FSMStartMenu
from init_bot import bot

router = Router()

data = {'title': None,
        'description': None,
        'date': None,
        'time': None,
        'location': None,
        'inventory': None,
        'price': None,
        'afterword': None}

class FSM_create_event(StatesGroup):
    menu = State()
    fill_title = State()
    fill_description = State()
    fill_date = State()
    fill_time = State()
    fill_location = State()
    fill_inventory = State()
    fill_price = State()
    fill_afterword = State()

@router.callback_query(F.data == 'create_event', StateFilter(FSMStartMenu.start_menu))
async def start (callback: CallbackQuery, state: FSMContext):
    # Смена состояния
    await state.set_state(FSM_create_event.menu)
    # Ответ
    await callback.message.edit_text(text='Введите название', reply_markup=CE_keyboard)

@router.callback_query(~F.data.in_(['publish', 'cancel']), StateFilter(FSM_create_event.menu))
async def CE_menu (callback: CallbackQuery, state: FSMContext):
    # title
    if callback.data == 'title':
        await state.set_state(FSM_create_event.fill_title)
        await callback.answer(text='Напишите название ивента')
    # description
    elif callback.data == 'description':
        await state.set_state(FSM_create_event.fill_description)
        await callback.answer(text='Напишите описание ивента')
    # date
    elif callback.data == 'date':
        await state.set_state(FSM_create_event.fill_date)
        await callback.answer(text='Напишите дату ивента')
    # time
    elif callback.data == 'time':
        await state.set_state(FSM_create_event.fill_time)
        await callback.answer(text='Напишите время ивента')
    # location
    elif callback.data == 'location':
        await state.set_state(FSM_create_event.fill_location)
        await callback.answer(text='Где будет проходить ивент?')
    # inventory
    elif callback.data == 'inventory':
        await state.set_state(FSM_create_event.fill_inventory)
        await callback.answer(text='Что нужно взять?')
    # afterword
    elif callback.data == 'afterword':
        await state.set_state(FSM_create_event.fill_afterword)
        await callback.answer(text='Что написать в конце?')
    # price
    elif callback.data == 'price':
        await state.set_state(FSM_create_event.fill_price)
        await callback.answer(text='Сколько будет стоить?')
    # Сохранение id сообщения для редактирования
    if check_id(await state.get_data()):
        await state.update_data(edit_message_id=callback.message.message_id)
        await state.update_data(edit_chat_id=callback.message.chat.id)
# -----------------------------------------------------------------------------------------
@router.message(StateFilter(FSM_create_event.fill_title))
async def fill_title (message: Message, state: FSMContext):
    # Сохранение ответа
    await state.update_data(title=message.text)
    data['title'] = await state.get_value('title')
    # Смена состояния
    await state.set_state(FSM_create_event.menu)
    # Удаление сообщения от пользователя
    await message.delete()
    # Ответ
    await bot.edit_message_text(message_id=await state.get_value(key='edit_message_id'),
                                chat_id=await state.get_value(key='edit_chat_id'),
                                reply_markup=CE_keyboard,
                                text=bild_text(data),
                                parse_mode='HTML')
# -----------------------------------------------------------------------------------------
@router.message(StateFilter(FSM_create_event.fill_description))
async def fill_description (message: Message, state: FSMContext):
    # Смена состояния
    await state.update_data(description=message.text)
    # Сохранение ответа
    data['description'] = await state.get_value('description')
    await state.set_state(FSM_create_event.menu)
    # Удаление сообщения от пользователя
    await message.delete()
    # Ответ
    await bot.edit_message_text(message_id=await state.get_value(key='edit_message_id'),
                                chat_id=await state.get_value(key='edit_chat_id'),
                                reply_markup=CE_keyboard,
                                text=bild_text(data),
                                parse_mode='HTML')
# -----------------------------------------------------------------------------------------
@router.message(StateFilter(FSM_create_event.fill_date))
async def fill_date (message: Message, state: FSMContext):
    # Смена состояния
    await state.set_state(FSM_create_event.menu)
    # Сохранение ответа
    await state.update_data(date=message.text)
    data['date'] = await state.get_value('date')
    # Удаление сообщения от пользователя
    await message.delete()
    # Ответ
    await bot.edit_message_text(message_id=await state.get_value(key='edit_message_id'),
                                chat_id=await state.get_value(key='edit_chat_id'),
                                reply_markup=CE_keyboard,
                                text=bild_text(data),
                                parse_mode='HTML')
# -----------------------------------------------------------------------------------------
@router.message(StateFilter(FSM_create_event.fill_time))
async def fill_time (message: Message, state: FSMContext):
    # Смена состояния
    await state.set_state(FSM_create_event.menu)
    # Сохранение ответа
    await state.update_data(time=message.text)
    data['time'] = await state.get_value('time')
    # Удаление сообщения от пользователя
    await message.delete()
    # Ответ
    await bot.edit_message_text(message_id=await state.get_value(key='edit_message_id'),
                                chat_id=await state.get_value(key='edit_chat_id'),
                                reply_markup=CE_keyboard,
                                text=bild_text(data),
                                parse_mode='HTML')
# -----------------------------------------------------------------------------------------
@router.message(StateFilter(FSM_create_event.fill_location))
async def fill_location (message: Message, state: FSMContext):
    # Смена состояния
    await state.set_state(FSM_create_event.menu)
    # Сохранение ответа
    await state.update_data(location=message.text)
    data['location'] = await state.get_value('location')
    # Удаление сообщения от пользователя
    await message.delete()
    # Ответ
    await bot.edit_message_text(message_id=await state.get_value(key='edit_message_id'),
                                chat_id=await state.get_value(key='edit_chat_id'),
                                reply_markup=CE_keyboard,
                                text=bild_text(data),
                                parse_mode='HTML')
# -----------------------------------------------------------------------------------------
@router.message(StateFilter(FSM_create_event.fill_inventory))
async def fill_inventory (message: Message, state: FSMContext):
    # Смена состояния
    await state.set_state(FSM_create_event.menu)
    # Сохранение ответа
    await state.update_data(inventory=message.text)
    data['inventory'] = await state.get_value('inventory')
    # Удаление сообщения от пользователя
    await message.delete()
    # Ответ
    await bot.edit_message_text(message_id=await state.get_value(key='edit_message_id'),
                                chat_id=await state.get_value(key='edit_chat_id'),
                                reply_markup=CE_keyboard,
                                text=bild_text(data),
                                parse_mode='HTML')
# -----------------------------------------------------------------------------------------
@router.message(StateFilter(FSM_create_event.fill_afterword))
async def fill_afterword (message: Message, state: FSMContext):
    # Смена состояния
    await state.set_state(FSM_create_event.menu)
    # Сохранение ответа
    await state.update_data(afterword=message.text)
    data['afterword'] = await state.get_value('afterword')
    # Удаление сообщения от пользователя
    await message.delete()
    # Ответ
    await bot.edit_message_text(message_id=await state.get_value(key='edit_message_id'),
                                chat_id=await state.get_value(key='edit_chat_id'),
                                reply_markup=CE_keyboard,
                                text=bild_text(data),
                                parse_mode='HTML')
# -----------------------------------------------------------------------------------------
@router.message(StateFilter(FSM_create_event.fill_price))
async def fill_price (message: Message, state: FSMContext):
    # Смена состояния
    await state.set_state(FSM_create_event.menu)
    # Сохранение ответа
    await state.update_data(price=message.text)
    data['price'] = await state.get_value('price')
    # Удаление сообщения от пользователя
    await message.delete()
    # Ответ
    await bot.edit_message_text(message_id=await state.get_value(key='edit_message_id'),
                                chat_id=await state.get_value(key='edit_chat_id'),
                                reply_markup=CE_keyboard,
                                text=bild_text(data),
                                parse_mode='HTML')
# -----------------------------------------------------------------------------------------
@router.callback_query(F.data == 'cancel', StateFilter(FSM_create_event.menu))
async def cancel_create_event(callback: CallbackQuery, state: FSMContext):
    # Очистка переменной data
    for key in data.keys():
        data[key] = None
    # Ответ
    await callback.answer(text='Удаляю ивент')
    # Удаление сообщения
    await callback.message.delete()
    # Сброс состояния и данных в хранилище
    await state.clear()
# -----------------------------------------------------------------------------------------
@router.message(StateFilter(FSM_create_event.menu))
async def attention_inappropriate_action (message: Message):
    await message.delete()
# -----------------------------------------------------------------------------------------
@router.callback_query(StateFilter(FSM_create_event.fill_title,
                                   FSM_create_event.fill_description,
                                   FSM_create_event.fill_date,
                                   FSM_create_event.fill_time,
                                   FSM_create_event.fill_location,
                                   FSM_create_event.fill_price,
                                   FSM_create_event.fill_inventory,
                                   FSM_create_event.fill_afterword))
async def attention_another_point (callback: CallbackQuery):
    await callback.answer(text='Завершите редактирование уже выбранного пункта')
# -----------------------------------------------------------------------------------------
@router.callback_query(F.data == 'publish', StateFilter(FSM_create_event.menu))
async def publish (callback: CallbackQuery, state: FSMContext):
    # Ответ
    await callback.message.copy_to(chat_id='-1002669138603', reply_markup=poll_keyboard, parse_mode='HTML')
    await callback.answer(text='Публикую')
    await callback.message.delete()
    # Сброс состояния и данных в хранилище
    await state.clear()
    # Очистка переменной data
    for key in data.keys():
        data[key] = None
# -----------------------------------------------------------------------------------------