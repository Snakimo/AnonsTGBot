from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from init_bot import bot
from create_event import CE_handlers_admin
from users import handlers_users
from start_menu import SM_handlers
from create_pattern import CP_handlers
from use_pattern import UP_handlers


async def main():
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(CE_handlers_admin.router)
    dp.include_router(SM_handlers.router)
    dp.include_router(handlers_users.router)
    dp.include_router(CP_handlers.router)
    dp.include_router(UP_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
