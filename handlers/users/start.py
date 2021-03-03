from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from stickers.dn_stickers import ryuk_hi


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_sticker(sticker=ryuk_hi)
    await message.answer(f"hello, {message.from_user.full_name}!\n\n"
                         f"You have the privilege of using the Death Note, so read the rules before you start.\n\n"
                         f"🍎 /rules 🖋 (click here)")
