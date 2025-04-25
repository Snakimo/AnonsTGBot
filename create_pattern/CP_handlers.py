from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import time

from start_menu.SM_handlers import FSMStartMenu
from init_bot import bot
from create_event.CE_functions import bild_text
from create_pattern.CP_keyboards import CP_keyboard
from create_pattern.CP_functions import save_data
from general_function import convert_date

router = Router()

class FSMCreatePattern(StatesGroup):
    menu = State()
    fill_title = State()
    fill_description = State()
    fill_date = State()
    fill_time = State()
    fill_location = State()
    fill_location_url = State()
    fill_price = State()
    fill_inventory = State()
    fill_afterword = State()

pattern = {}

@router.callback_query(F.data == 'create_pattern', StateFilter(FSMStartMenu.start_menu))
async def request_name_pattern(callback: CallbackQuery, state: FSMContext):
    # Сохранение ID сообщения
    await state.update_data(edit_message_id=callback.message.message_id)
    # Создание словаря
    pattern[callback.from_user.id] = {'title': None,
                                     'description': None,
                                     'date': None,
                                     'time': None,
                                     'location': None,
                                     'location_url': None,
                                     'inventory': None,
                                     'price': None,
                                     'afterword': None}
    # Ответ
    await callback.message.edit_text(text='Создайте шаблон\nДля заполнения пунктов, выберите соотствующие кнопки',
                                     reply_markup=CP_keyboard)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.callback_query(~F.data.in_({'cancel', 'save'}), StateFilter(FSMCreatePattern.menu))
async def CP_menu(callback: CallbackQuery, state: FSMContext):
    # title
    if callback.data == 'title':
        await callback.message.edit_text(text='Напишите название')
        await state.set_state(FSMCreatePattern.fill_title)
    # description
    if callback.data == 'description':
        await callback.message.edit_text(text='Напишите описание')
        await state.set_state(FSMCreatePattern.fill_description)
    # date
    if callback.data == 'date':
        await callback.message.edit_text(text='Напишите дату')
        await state.set_state(FSMCreatePattern.fill_date)
    # time
    if callback.data == 'time':
        await callback.message.edit_text(text='Укажите время')
        await state.set_state(FSMCreatePattern.fill_time)
    # location
    if callback.data == 'location':
        await callback.message.edit_text(text='Где будет ивент?')
        await state.set_state(FSMCreatePattern.fill_location)
    # location_url
    if callback.data == 'location_url':
        await callback.message.edit_text(text='Укажите ссылку на место в яндекс картах')
        await state.set_state(FSMCreatePattern.fill_location_url)
    # price
    if callback.data == 'price':
        await callback.message.edit_text(text='Укажите стоимость')
        await state.set_state(FSMCreatePattern.fill_price)
    # inventory
    if callback.data == 'inventory':
        await callback.message.edit_text(text='Что с собой взять?')
        await state.set_state(FSMCreatePattern.fill_inventory)
    # afterword
    if callback.data == 'afterword':
        await callback.message.edit_text(text='Что написать в конце?')
        await state.set_state(FSMCreatePattern.fill_afterword)
# --------------------------------------------------------------------------------------------
@router.message(StateFilter(FSMCreatePattern.fill_title))
async def fill_title(message: Message, state: FSMContext):
    # Сохранить данные
    await state.update_data(title=message.text)
    pattern[message.from_user.id]['title'] = await state.get_value('title')
    # Удаление сообщения
    await message.delete()
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(pattern[message.from_user.id]),
                                reply_markup=CP_keyboard,
                                disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.message(StateFilter(FSMCreatePattern.fill_description))
async def fill_description(message: Message, state: FSMContext):
    # Сохранить данные
    await state.update_data(description=message.text)
    pattern[message.from_user.id]['description'] = await state.get_value('description')
    # Удаление сообщения
    await message.delete()
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(pattern[message.from_user.id]),
                                reply_markup=CP_keyboard,
                                disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.message(StateFilter(FSMCreatePattern.fill_date))
async def fill_date(message: Message, state: FSMContext):
    # Сохранить данные
    await state.update_data(date=convert_date(message.text))
    pattern[message.from_user.id]['date'] = await state.get_value('date')
    # Удаление сообщения
    await message.delete()
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(pattern[message.from_user.id]),
                                reply_markup=CP_keyboard,
                                disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.message(StateFilter(FSMCreatePattern.fill_time))
async def fill_time(message: Message, state: FSMContext):
    # Сохранить данные
    await state.update_data(time=message.text)
    pattern[message.from_user.id]['time'] = await state.get_value('time')
    # Удаление сообщения
    await message.delete()
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(pattern[message.from_user.id]),
                                reply_markup=CP_keyboard,
                                disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.message(StateFilter(FSMCreatePattern.fill_location))
async def fill_location(message: Message, state: FSMContext):
    # Сохранить данные
    await state.update_data(location=message.text)
    pattern[message.from_user.id]['location'] = await state.get_value('location')
    # Удаление сообщения
    await message.delete()
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(pattern[message.from_user.id]),
                                reply_markup=CP_keyboard,
                                disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.message(StateFilter(FSMCreatePattern.fill_location_url))
async def fill_location_url(message: Message, state: FSMContext):
    # Сохранить данные
    await state.update_data(location_url=message.text)
    pattern[message.from_user.id]['location_url'] = await state.get_value('location_url')
    # Удаление сообщения
    await message.delete()
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(pattern[message.from_user.id]),
                                reply_markup=CP_keyboard,
                                disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.message(StateFilter(FSMCreatePattern.fill_price))
async def fill_price(message: Message, state: FSMContext):
    # Сохранить данные
    await state.update_data(price=message.text)
    pattern[message.from_user.id]['price'] = await state.get_value('price')
    # Удаление сообщения
    await message.delete()
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(pattern[message.from_user.id]),
                                reply_markup=CP_keyboard,
                                disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.message(StateFilter(FSMCreatePattern.fill_inventory))
async def fill_inventory(message: Message, state: FSMContext):
    # Сохранить данные
    await state.update_data(inventory=message.text)
    pattern[message.from_user.id]['inventory'] = await state.get_value('inventory')
    # Удаление сообщения
    await message.delete()
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(pattern[message.from_user.id]),
                                reply_markup=CP_keyboard,
                                disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.message(StateFilter(FSMCreatePattern.fill_afterword))
async def fill_afterword(message: Message, state: FSMContext):
    # Сохранить данные
    await state.update_data(afterword=message.text)
    pattern[message.from_user.id]['afterword'] = await state.get_value('afterword')
    # Удаление сообщения
    await message.delete()
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(pattern[message.from_user.id]),
                                reply_markup=CP_keyboard,
                                disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMCreatePattern.menu)
# --------------------------------------------------------------------------------------------
@router.callback_query(F.data == 'cancel', StateFilter(FSMCreatePattern.menu))
async def CP_cancel(callback: CallbackQuery, state: FSMContext):
    # Очистка словаря
    pattern.pop(callback.from_user.id)
    # Удаление сообщения
    await callback.message.delete()
    # Смена состояния и очистка FSM машины
    await state.clear()
# --------------------------------------------------------------------------------------------
@router.callback_query(F.data == 'save', StateFilter(FSMCreatePattern.menu))
async def CP_save(callback: CallbackQuery, state: FSMContext):
    if save_data(pattern[callback.from_user.id]): # Если 'title' != None
        # Очистка словаря
        pattern.pop(callback.from_user.id)
        # Смена состояния и очистка FSM машины
        await state.clear()
        # Ответ
        await callback.message.edit_text(text='Сохраняю шаблон.')
        time.sleep(0.5)
        await callback.message.edit_text(text='Сохраняю шаблон..')
        time.sleep(0.5)
        await callback.message.edit_text(text='Сохраняю шаблон...')
        time.sleep(0.5)
        await callback.message.edit_text(text='Успешно✅')
        time.sleep(0.5)
         # Удаление сообщения
        await callback.message.delete()
    else: # Если 'title' == None
        await callback.message.edit_text(text='Ошибка сохранения - ивент не имеет названия\nУкажите название ивента')
        await state.set_state(FSMCreatePattern.fill_title)
