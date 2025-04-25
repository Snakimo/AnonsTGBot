from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_title = InlineKeyboardButton(text='Название', callback_data='title')
button_description = InlineKeyboardButton(text='Описание', callback_data='description')
button_date = InlineKeyboardButton(text='Дата', callback_data='date')
button_time = InlineKeyboardButton(text='Время', callback_data='time')
button_location = InlineKeyboardButton(text='Место', callback_data='location')
button_price = InlineKeyboardButton(text='Цена', callback_data='price')
button_inventory = InlineKeyboardButton(text='Инвентарь', callback_data='inventory')
button_afterword = InlineKeyboardButton(text='Послесловие', callback_data='afterword')
button_cancel = InlineKeyboardButton(text='Отменить создание', callback_data='cancel')
button_publish = InlineKeyboardButton(text='Опубликовать', callback_data='publish')

CE_keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_title],
                                    [button_description],
                                    [button_date],
                                    [button_time],
                                    [button_location],
                                    [button_price],
                                    [button_inventory],
                                    [button_afterword],
                                    [button_cancel, button_publish]])
# ----------------------------------------------------------------------------------------------