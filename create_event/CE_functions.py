from datetime import datetime

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import Message
from create_event.CE_keyboards import CE_keyboard

days_in_week = {0: 'Пн',
                1: 'Вт',
                2: 'Ср',
                3: 'Чт',
                4: 'Пт',
                5: 'Сб',
                6: 'Вс',}

def bild_text (data: dict) -> str:
    text = ''
    if data['title'] != None:
        text += f'<b>{data["title"]}</b>\n'
    if data['description'] != None:
        text += data["description"] + '\n\n'
    if data['date'] != None:
        if type(data['date']) == str:
            text += f'🗓Дата: {data["date"]}'
        else:
             text += f'🗓Дата: {datetime.strftime(data["date"], "%d.%m")} ({days_in_week[datetime.weekday(data["date"])]})'
    if data['time'] != None:
        text += f'\n🕰Время: {data["time"]}\n'
    if data['location'] != None and data['location_url'] != None:
        try:
            data['location_url'].index('https:')
        except ValueError:
            text += f'📍Место: {data["location"]}\n'
        else:
            url = data['location_url'][data['location_url'].index('https:'):].rstrip()
            text += f'📍Место: <a href="{url}">{data["location"]}</a>\n'
    if data['location'] != None and data['location_url'] == None:
        text += f'📍Место: {data["location"]}\n'
    if data['price'] != None:
        text += f'💰Цена: {data["price"]}\n'
    if data['inventory'] != None:
        text += f'🎒С собой: {data["inventory"]}\n'
    if data['afterword'] != None:
        text += '\n' + data['afterword']
    return text

def check_id (check_dict: dict) -> bool:
    if 'edit_message_id' in check_dict:
        return False
    else:
        return True
