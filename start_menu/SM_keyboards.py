from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_create_event = InlineKeyboardButton(text='Создать ивент', callback_data='create_event')
button_use_pattern = InlineKeyboardButton(text='Использовать шаблон', callback_data='use_pattern')
button_create_pattern = InlineKeyboardButton(text='Создать шаблон', callback_data='create_pattern')

keyboard_start_menu = InlineKeyboardMarkup(inline_keyboard=[[button_create_event],
                                                            [button_create_pattern],
                                                            [button_use_pattern]])