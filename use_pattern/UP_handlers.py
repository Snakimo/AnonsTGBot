from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import timedelta

from start_menu.SM_handlers import FSMStartMenu
from start_menu.SM_keyboards import keyboard_start_menu
from use_pattern.UP_keyboards import keyboard_list_pattern, keyboard_choose_option, keyboard_yes_no, ChP_keyboard, back_to_menu_keyboard
from use_pattern.UP_functions import load_data, delete_data
from create_event.CE_functions import bild_text
from create_pattern.CP_handlers import FSMCreatePattern
from create_pattern.CP_keyboards import CP_keyboard
from init_bot import bot
from general_function import convert_date
import time
from users.keyboard_users import poll_keyboard
from create_pattern.CP_functions import save_data

router = Router()

class FSMUsePattern(StatesGroup):
    choose_pattern = State()
    choose_option = State()
    fill_date_option = State()
    confirm = State()
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


@router.callback_query(F.data == 'use_pattern', StateFilter(FSMStartMenu.start_menu))
async def request_choose_pattern(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Выберите шаблон',
                                     reply_markup=keyboard_list_pattern())
    await state.set_state(FSMUsePattern.choose_pattern)

@router.callback_query(F.data == 'back_to_start_menu', StateFilter(FSMUsePattern.choose_pattern))
async def back_to_change_pattern(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Что вы хотите сделать?',
                                    reply_markup=keyboard_start_menu)
    await state.set_state(FSMStartMenu.start_menu)

@router.callback_query(StateFilter(FSMUsePattern.choose_pattern))
async def choose_pattern(callback: CallbackQuery, state: FSMContext):
    pattern_id = None
    if callback.data == '0':
        pattern_id = 0
    if callback.data == '1':
        pattern_id = 1
    if callback.data == '2':
        pattern_id = 2
    if callback.data == '3':
        pattern_id = 3
    if callback.data == '4':
        pattern_id = 4
    if callback.data == '5':
        pattern_id = 5
    if callback.data == '6':
        pattern_id = 6
    if callback.data == '7':
        pattern_id = 7
    if callback.data == '8':
        pattern_id = 8
    if callback.data == '9':
        pattern_id = 9
    if callback.data == '10':
        pattern_id = 10
    if callback.data == '11':
        pattern_id = 11
    if callback.data == '12':
        pattern_id = 12
    if callback.data == '13':
        pattern_id = 13
    if callback.data == '14':
        pattern_id = 14
    if callback.data == '15':
        pattern_id = 15
    if callback.data == '16':
        pattern_id = 16
    if callback.data == '17':
        pattern_id = 17
    if callback.data == '18':
        pattern_id = 18
    if callback.data == '19':
        pattern_id = 19
    await state.update_data(selected_pattern=load_data()[pattern_id])
    global selected_pattern
    selected_pattern = await state.get_value('selected_pattern')
    await callback.message.edit_text(text=bild_text(selected_pattern),
                                     disable_web_page_preview=True,
                                     reply_markup=keyboard_choose_option)
    await state.set_state(FSMUsePattern.choose_option)

@router.callback_query(F.data == 'reschedule', StateFilter(FSMUsePattern.choose_option))
async def reschedule_date(callback: CallbackQuery, state: FSMContext):
    if selected_pattern['date'] == None:
        await callback.message.edit_text(text='Шаблон не имеет даты\nУкажите дату')
        await state.update_data(edit_message_id=callback.message.message_id)
        await state.set_state(FSMUsePattern.fill_date)
    else:
        selected_pattern['date'] += timedelta(days=7)
        await callback.message.edit_text(text=bild_text(selected_pattern),
                                        disable_web_page_preview=True,
                                        reply_markup=keyboard_choose_option)

@router.message(StateFilter(FSMUsePattern.fill_date_option))
async def fill_date_option(message: Message, state: FSMContext):
    selected_pattern['date'] = convert_date(message.text)
    await state.set_state(FSMUsePattern.choose_option)
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=keyboard_choose_option,
                                disable_web_page_preview=True)
    await message.delete()

@router.callback_query(F.data == 'back_to_choose_pattern', StateFilter(FSMUsePattern.choose_option))
async def back_to_change_pattern(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Выберите шаблон',
                                     reply_markup=keyboard_list_pattern())
    await state.set_state(FSMUsePattern.choose_pattern)

@router.callback_query(F.data == 'anons', StateFilter(FSMUsePattern.choose_option))
async def anons(callback: CallbackQuery, state: FSMContext):
    # Анонсирование
    await callback.message.copy_to(chat_id='-1002669138603', reply_markup=poll_keyboard)
    # Ответ
    await callback.message.edit_text(text='Анонсирую.')
    time.sleep(0.5)
    await callback.message.edit_text(text='Анонсирую..')
    time.sleep(0.5)
    await callback.message.edit_text(text='Анонсирую...')
    time.sleep(0.5)
    await callback.message.edit_text(text='Успешно✅')
    time.sleep(1)
    await callback.message.delete()
    # Смена и очистка машины состояний
    await state.clear()
    # Очистка переменных
    selected_pattern = None

@router.callback_query(F.data == 'delete', StateFilter(FSMUsePattern.choose_option))
async def delete_pattern(callback: CallbackQuery, state: FSMContext):
    # Ответ
    await callback.message.edit_text(text='Вы уверены?', reply_markup=keyboard_yes_no)
    # Смена состояния
    await state.set_state(FSMUsePattern.confirm)

@router.callback_query(StateFilter(FSMUsePattern.confirm))
async def confirm(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'yes':
        # Ответ
        await callback.message.edit_text(text='Удаляю.')
        time.sleep(0.5)
        await callback.message.edit_text(text='Удаляю..')
        time.sleep(0.5)
        await callback.message.edit_text(text='Удаляю...')
        time.sleep(0.5)
        await callback.message.edit_text(text='Успешно✅')
        time.sleep(1)
        # Удаление
        delete_data(selected_pattern['id'])
        # Смена состояния
        await state.set_state(FSMUsePattern.choose_pattern)
        # Переход к выбору шаблона
        await callback.message.edit_text(text='Выберите шаблон',
                                     reply_markup=keyboard_list_pattern())
    elif callback.data == 'no':
        # Смена состояния
        await state.set_state(FSMUsePattern.choose_option)
        # Переход к выбору опции
        await callback.message.edit_text(text=bild_text(selected_pattern),
                                     disable_web_page_preview=True,
                                     reply_markup=keyboard_choose_option)
# ------------------------------------------------------------------------------------------------
@router.callback_query(F.data == 'change_pattern', StateFilter(FSMUsePattern.choose_option))
async def transition_to_menu(callback: CallbackQuery, state: FSMContext):

    print(selected_pattern)
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)
    # Ответ
    await callback.message.edit_text(text=bild_text(selected_pattern),
                                     reply_markup=ChP_keyboard,
                                     disable_web_page_preview=True)
    await state.update_data(edit_message_id=callback.message.message_id)

@router.callback_query(~F.data.in_({'back', 'anons', 'save'}), StateFilter(FSMUsePattern.menu))
async def CP_menu(callback: CallbackQuery, state: FSMContext):
    # title
    if callback.data == 'title':
        await callback.message.edit_text(text=f'"{selected_pattern["title"]}"\nВведите новое название',
                                         reply_markup=back_to_menu_keyboard)
        await state.set_state(FSMUsePattern.fill_title)
    # description
    if callback.data == 'description':
        await callback.message.edit_text(text=f'<code>{selected_pattern["description"]}</code>\nВведите новое описание',
                                         reply_markup=back_to_menu_keyboard)
        await state.set_state(FSMUsePattern.fill_description)
    # date
    if callback.data == 'date':
        await callback.message.edit_text(text=f'"{selected_pattern["date"]}"\nУкажите новую дату',
                                         reply_markup=back_to_menu_keyboard)
        await state.set_state(FSMUsePattern.fill_date)
    # time
    if callback.data == 'time':
        await callback.message.edit_text(text=f'"{selected_pattern["time"]}"\nУкажите новое время',
                                         reply_markup=back_to_menu_keyboard)
        await state.set_state(FSMUsePattern.fill_time)
    # location
    if callback.data == 'location':
        await callback.message.edit_text(text=f'"{selected_pattern["location"]}"\nУкажите новое место',
                                         reply_markup=back_to_menu_keyboard)
        await state.set_state(FSMUsePattern.fill_location)
    # location_url
    if callback.data == 'location_url':
        await callback.message.edit_text(text=f'"{selected_pattern["location_url"]}"\nУкажите новую ссылку',
                                         reply_markup=back_to_menu_keyboard)
        await state.set_state(FSMUsePattern.fill_location_url)
    # price
    if callback.data == 'price':
        await callback.message.edit_text(text=f'"{selected_pattern["price"]}"\nУкажите новую стоимость',
                                         reply_markup=back_to_menu_keyboard)
        await state.set_state(FSMUsePattern.fill_price)
    # inventory
    if callback.data == 'inventory':
        await callback.message.edit_text(text=f'<code>{selected_pattern["inventory"]}</code>\nВведите новый инвентарь',
                                         reply_markup=back_to_menu_keyboard)
        await state.set_state(FSMUsePattern.fill_inventory)
    # afterword
    if callback.data == 'afterword':
        await callback.message.edit_text(text=f'<code>{selected_pattern["afterword"]}</code>\nВведите новое послесловие',
                                         reply_markup=back_to_menu_keyboard)
        await state.set_state(FSMUsePattern.fill_afterword)
# --------------------------------------------------------------------------------------------------
# title
@router.message(FSMUsePattern.fill_title)
async def fill_title(message: Message, state: FSMContext):
    # Изменения словаря
    selected_pattern['title'] = message.text
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=ChP_keyboard,
                                disable_web_page_preview=True)
    # Удаление сообщения
    await message.delete()
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)

# description
@router.message(FSMUsePattern.fill_description)
async def fill_description(message: Message, state: FSMContext):
    # Изменения словаря
    selected_pattern['description'] = message.text
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=ChP_keyboard,
                                disable_web_page_preview=True)
    # Удаление сообщения
    await message.delete()
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)

# date
@router.message(FSMUsePattern.fill_date)
async def fill_date(message: Message, state: FSMContext):
    # Изменения словаря
    selected_pattern['date'] = convert_date(message.text)
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=ChP_keyboard,
                                disable_web_page_preview=True)
    # Удаление сообщения
    await message.delete()
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)

# time
@router.message(FSMUsePattern.fill_time)
async def fill_time(message: Message, state: FSMContext):
    # Изменения словаря
    selected_pattern['time'] = message.text
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=ChP_keyboard,
                                disable_web_page_preview=True)
    # Удаление сообщения
    await message.delete()
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)

# location
@router.message(FSMUsePattern.fill_location)
async def fill_location(message: Message, state: FSMContext):
    # Изменения словаря
    selected_pattern['location'] = message.text
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=ChP_keyboard,
                                disable_web_page_preview=True)
    # Удаление сообщения
    await message.delete()
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)

# location_url
@router.message(FSMUsePattern.fill_location_url)
async def fill_location_url(message: Message, state: FSMContext):
    # Изменения словаря
    selected_pattern['location_url'] = message.text
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=ChP_keyboard,
                                disable_web_page_preview=True)
    # Удаление сообщения
    await message.delete()
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)

# price
@router.message(FSMUsePattern.fill_price)
async def fill_price(message: Message, state: FSMContext):
    # Изменения словаря
    selected_pattern['price'] = message.text
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=ChP_keyboard,
                                disable_web_page_preview=True)
    # Удаление сообщения
    await message.delete()
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)

# inventory
@router.message(FSMUsePattern.fill_inventory)
async def fill_inventory(message: Message, state: FSMContext):
    # Изменения словаря
    selected_pattern['inventory'] = message.text
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=ChP_keyboard,
                                disable_web_page_preview=True)
    # Удаление сообщения
    await message.delete()
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)

# afterword
@router.message(FSMUsePattern.fill_afterword)
async def fill_afterword(message: Message, state: FSMContext):
    # Изменения словаря
    selected_pattern['afterword'] = message.text
    # Ответ
    await bot.edit_message_text(chat_id=message.chat.id,
                                message_id=await state.get_value(key='edit_message_id'),
                                text=bild_text(selected_pattern),
                                reply_markup=ChP_keyboard,
                                disable_web_page_preview=True)
    # Удаление сообщения
    await message.delete()
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)

@router.callback_query(F.data == 'back', StateFilter(FSMUsePattern.menu))
async def back_to_choose_option(callback: CallbackQuery, state: FSMContext):
    # Ответ
    await callback.message.edit_reply_markup(reply_markup=keyboard_choose_option)
    # Смена состояния
    await state.set_state(FSMUsePattern.choose_option)

@router.callback_query(F.data == 'save', StateFilter(FSMUsePattern.menu))
async def save_pattern(callback: CallbackQuery):
    # Сохранение
    save_data(selected_pattern)
    # Ответ
    await callback.message.edit_text(text='Сохраняю.')
    time.sleep(0.5)
    await callback.message.edit_text(text='Сохраняю..')
    time.sleep(0.5)
    await callback.message.edit_text(text='Сохраняю...')
    time.sleep(0.5)
    await callback.message.edit_text(text='Успешно✅')
    time.sleep(1)
    await callback.message.edit_text(text=bild_text(selected_pattern),
                                    reply_markup=ChP_keyboard,
                                    disable_web_page_preview=True)

@router.callback_query(F.data == 'anons', StateFilter(FSMUsePattern.menu))
async def anons_from_change_pattern(callback: CallbackQuery, state: FSMContext):
    # Анонс
    await callback.message.copy_to(chat_id='-1002669138603', reply_markup=poll_keyboard, parse_mode='HTML')
    # Ответ
    await callback.message.edit_text(text='Анонсирую.')
    time.sleep(0.5)
    await callback.message.edit_text(text='Анонсирую..')
    time.sleep(0.5)
    await callback.message.edit_text(text='Анонсирую...')
    time.sleep(0.5)
    await callback.message.edit_text(text='Успешно✅')
    time.sleep(1)
    # Удаление
    await callback.message.delete()
    # Очистка машины состояния
    await state.clear()
    # Очистка словаря
    selected_pattern = None

@router.callback_query(F.data == 'back_to_menu', StateFilter(FSMUsePattern.fill_title,
                                                             FSMUsePattern.fill_description,
                                                             FSMUsePattern.fill_date,
                                                             FSMUsePattern.fill_time,
                                                             FSMUsePattern.fill_location,
                                                             FSMUsePattern.fill_location_url,
                                                             FSMUsePattern.fill_price,
                                                             FSMUsePattern.fill_afterword,
                                                             FSMUsePattern.fill_inventory))
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    # Ответ
    await callback.message.edit_text(text=bild_text(selected_pattern),
                                    reply_markup=ChP_keyboard,
                                    disable_web_page_preview=True)
    # Смена состояния
    await state.set_state(FSMUsePattern.menu)