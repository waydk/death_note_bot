from loader import db, db_note
from loader import bot, storage
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    await db.create()
    await db_note.create()
    import middlewares
    middlewares.setup(dp)
    await set_default_commands(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await db.create_table_users()
    await db_note.create_table_note()


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
