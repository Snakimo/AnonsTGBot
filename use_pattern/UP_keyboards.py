from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from use_pattern.UP_functions import load_data

def keyboard_list_pattern() -> InlineKeyboardMarkup:
    patterns = load_data()
    buttons = []
    for key in patterns.keys():
        buttons.append([InlineKeyboardButton(text=patterns[key]['title'], callback_data=str(key))])
    buttons.append([InlineKeyboardButton(text='Назад', callback_data='back_to_start_menu')])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

button_change_pattern = InlineKeyboardButton(text='Изменить шаблон', callback_data='change_pattern')
button_reschedule = InlineKeyboardButton(text='Перенести на следующую неделю', callback_data='reschedule')
button_back = InlineKeyboardButton(text='Назад', callback_data='back_to_choose_pattern')
button_publish = InlineKeyboardButton(text='Анонсировать', callback_data='anons')
button_delete = InlineKeyboardButton(text='Удалить шаблон', callback_data='delete')
# --------------------------------------------------------------------------------------------------------
keyboard_choose_option = InlineKeyboardMarkup(inline_keyboard=[[button_change_pattern],
                                                               [button_delete],
                                                               [button_reschedule],
                                                               [button_back, button_publish]])

button_yes = InlineKeyboardButton(text='Да', callback_data='yes')
button_no = InlineKeyboardButton(text='Нет', callback_data='no')

keyboard_yes_no = InlineKeyboardMarkup(inline_keyboard=[[button_no, button_yes]])
# --------------------------------------------------------------------------------------------------------
button_title = InlineKeyboardButton(text='Название', callback_data='title')
button_description = InlineKeyboardButton(text='Описание', callback_data='description')
button_date = InlineKeyboardButton(text='Дата', callback_data='date')
button_time = InlineKeyboardButton(text='Время', callback_data='time')
button_location = InlineKeyboardButton(text='Место', callback_data='location')
button_location_url = InlineKeyboardButton(text='Ссылка', callback_data='location_url')
button_price = InlineKeyboardButton(text='Цена', callback_data='price')
button_inventory = InlineKeyboardButton(text='Инвентарь', callback_data='inventory')
button_afterword = InlineKeyboardButton(text='Послесловие', callback_data='afterword')
button_back = InlineKeyboardButton(text='Назад', callback_data='back')
button_save = InlineKeyboardButton(text='Сохранить', callback_data='save')
button_anons = InlineKeyboardButton(text='Анонсировать', callback_data='anons')

ChP_keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_title],
                                    [button_description],
                                    [button_date],
                                    [button_time],
                                    [button_location, button_location_url],
                                    [button_price],
                                    [button_inventory],
                                    [button_afterword],
                                    [button_save, button_anons],
                                    [button_back]])
# --------------------------------------------------------------------------------------------------------
button_back_to_menu = InlineKeyboardButton(text='Назад', callback_data='back_to_menu')
back_to_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_back_to_menu]])