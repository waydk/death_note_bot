from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, _
from src.keyboards.inline.close_keyboard import close_markup
from src.utils.db_api import db_helpers


@dp.message_handler(Command("top"), state='*')
async def show_top_users(message: types.Message):
    await message.delete()
    top = []
    top_users = await db_helpers.get_top_users()
    for place, user in enumerate(top_users):
        if place + 1 == 1:
            top.append(f"🥇 {place + 1} {user[0]} - {user[1]} 🍎")
        elif place + 1 == 2:
            top.append(f"🥈 {place + 1} {user[0]} - {user[1]} 🍎")
        elif place + 1 == 3:
            top.append(f"🥉 {place + 1} {user[0]} - {user[1]} 🍎")
        else:
            top.append(f"📓 {place + 1} {user[0]} - {user[1]} 🍎")
    top = '\n'.join(top)
    text = _("😳 TOP dudes with apples:\n{}").format(top)
    await message.answer(text, reply_markup=close_markup)
