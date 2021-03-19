from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from src.keyboards.inline.language_keyboard import languages_markup
from loader import dp, _
from src.stickers.dn_stickers import ryuk_hi
from src.utils.db_api import db_helpers


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer_sticker(sticker=ryuk_hi)
    text = _("hello, {}!\n\n"
             "You have the privilege of using the Death Note, so read the rules before you start:\n\n"
             "🍎 /rules 🖋 (click here) \n\n"
             "If you have read the rules, you can start using the death note: \n\n"
             "📓 /write_down 📓 (click here) \n\n"
             "Your Death Note:\n\n /death_list 📔 (click here)\n\n"
             "Settings: /settings (click here)").format(message.from_user.full_name)

    await message.answer(text, reply_markup=languages_markup)
    name = message.from_user.full_name
    await db_helpers.add_user(id_user=message.from_user.id,
                              name=name)
