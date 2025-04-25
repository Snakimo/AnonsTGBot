from datetime import date, time, datetime
import locale
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
days_in_month = {1: 31,
                 2: 28,
                 3: 31,
                 4: 30,
                 5: 31,
                 6: 30,
                 7: 31,
                 8: 31,
                 9: 30,
                 10: 31,
                 11: 30,
                 12: 31}

days_in_week = {0: 'Пн',
                1: 'Вт',
                2: 'Ср',
                3: 'Чт',
                4: 'Пт',
                5: 'Сб',
                6: 'Вс',}

year = int(datetime.strftime(datetime.today(), '%Y'))
month = int(datetime.strftime(datetime.today(), '%m'))
start_month = datetime.weekday(datetime(year, month, 1))
locale.setlocale(locale.LC_ALL, 'ru_RU')

def leap_year ():
    if year % 400 == 0:
        days_in_month[2] = 29
        return
    if year % 4 == 0 and year % 100 != 0:
        days_in_month[2] = 29
        return
    days_in_month[2] = 28

def numbers_of_weeks(month: int) -> int:
    leap_year()
    n = (days_in_month[month] + datetime.weekday(datetime(year, month, 1))) // 7
    if (days_in_month[month] + datetime.weekday(datetime(year, month, 1))) % 7 != 0:
        n += 1
    return n

def create_keyboard() -> InlineKeyboardMarkup:
    button_left = InlineKeyboardButton(text='<', callback_data='left')
    button_right = InlineKeyboardButton(text='>', callback_data='right')
    button_month = InlineKeyboardButton(text=datetime.strftime(datetime.today(), '%B'), callback_data='_')

    calendar = [[button_left, button_month, button_right], [InlineKeyboardButton(text=days_in_week[i], callback_data='_') for i in range(7)]]

    for i in range(numbers_of_weeks(month)):
        tmp = []
        for j in range(7):
            day = (i*7) + j
            if start_month <= day < (start_month + days_in_month[month]):
                tmp.append(InlineKeyboardButton(text=str(day-start_month+1), callback_data=str(day-start_month+1)))
            else:
                tmp.append(InlineKeyboardButton(text='X', callback_data='_'))
        calendar.append(tmp)

    return InlineKeyboardMarkup(inline_keyboard=calendar)

print(numbers_of_weeks(month))