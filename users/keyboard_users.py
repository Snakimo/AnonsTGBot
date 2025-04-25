from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_going = InlineKeyboardButton(text='Приду🙂', callback_data='going')
button_not_going = InlineKeyboardButton(text='Не смогу🙃', callback_data='not_going')

poll_keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_going, button_not_going]])