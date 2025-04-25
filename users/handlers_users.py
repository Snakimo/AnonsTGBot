from aiogram import Router, F
from aiogram.types import CallbackQuery

from users.keyboard_users import poll_keyboard
from users.functions_users import forming_text_announcement, forming_name, cut_text

chat_id = '-1002669138603'

router = Router()

event = {}

@router.callback_query(F.data.in_({'going', 'not_going'}))
async def event_polling(callback: CallbackQuery):
    # Проверка наличия ивента
    if callback.message.message_id not in event:
        event[callback.message.message_id] = {'description': callback.message.text,
                                              'going': {},
                                              'not_going': {}}
    # Отработка кнопок
    if callback.data == 'going':
        # Удаление выбора
        if callback.from_user.id in event[callback.message.message_id]['going']:
            await callback.answer(text='Отменяю ваш выбор')
            event[callback.message.message_id]['going'].pop(callback.from_user.id)
        # Запись выбора
        elif callback.from_user.id not in event[callback.message.message_id]['going']:
            await callback.answer(text='Записываю ваш выбор')
            event[callback.message.message_id]['going'][callback.from_user.id] = forming_name(first_name=callback.from_user.first_name, last_name=callback.from_user.last_name)
            # Смена выбора
            if callback.from_user.id in event[callback.message.message_id]['not_going']:
                event[callback.message.message_id]['not_going'].pop(callback.from_user.id)
    elif callback.data == 'not_going':
        # Удаление выбора
        if callback.from_user.id in event[callback.message.message_id]['not_going']:
            await callback.answer(text='Отменяю ваш выбор')
            event[callback.message.message_id]['not_going'].pop(callback.from_user.id)
        # Запись выбора
        elif callback.from_user.id not in event[callback.message.message_id]['not_going']:
            await callback.answer(text='Записываю ваш выбор')
            event[callback.message.message_id]['not_going'][callback.from_user.id] = forming_name(first_name=callback.from_user.first_name, last_name=callback.from_user.last_name)
            # Смена выбора
            if callback.from_user.id in event[callback.message.message_id]['going']:
                event[callback.message.message_id]['going'].pop(callback.from_user.id)
    # Вывод информации в канал
    event[callback.message.message_id]['description'] = cut_text(callback.message.text)
    await callback.message.edit_text(text=forming_text_announcement(event[callback.message.message_id]),
                               parse_mode='HTML',
                               reply_markup=poll_keyboard)
