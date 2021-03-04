import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from stickers.dn_stickers import ryuk_hi


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_sticker(sticker=ryuk_hi)
    await message.answer(f"hello, {message.from_user.full_name}!\n\n"
                         f"You have the privilege of using the Death Note, so read the rules before you start:\n\n"
                         f"🍎 /rules 🖋 (click here) \n\n"
                         f"If you have read the rules, you can start using the death note: \n\n"
                         f"📓 /write_down 📓 (click here) \n\n"
                         f"Your Death Note:\n\n /death_list 📔 (click here)")
    name = message.from_user.full_name

    try:
        await db.add_user(id=message.from_user.id,
                          name=name)
    except asyncpg.exceptions.UniqueViolationError:
        pass


