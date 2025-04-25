from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup

from start_menu.SM_keyboards import keyboard_start_menu

router = Router()

class FSMStartMenu (StatesGroup):
    start_menu = State()

@router.message(CommandStart(), StateFilter(default_state))
async def command_start(message: Message, state: FSMContext):
    # Ответ
    await message.answer(text='Что вы хотите сделать?',
                         reply_markup=keyboard_start_menu)
    # Удаление сообщения /start
    await message.delete()
    # Смена состояния
    await state.set_state(FSMStartMenu.start_menu)
# -----------------------------------------------------------------
@router.message(StateFilter(FSMStartMenu.start_menu))
async def unavailable_option(message: Message):
    await message.delete()

@router.message(StateFilter(default_state))
async def command_start(message: Message):
    # Ответ
    await message.answer(text='Для активизации бота введите команду /start')
    # Удаление ответа
    await message.delete()