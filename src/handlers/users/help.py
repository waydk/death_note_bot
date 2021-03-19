from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, _
from src.stickers.dn_stickers import kira


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    text = _("available commands:\n"
             "/start - start a conversation\n"
             "/help - get info\n"
             "/rules - rules for the use of the death note\n"
             "/write_down - write in the death note\n"
             "/write (example: yagami light heart_attack)\n"
             "/death_list - show victim list\n")
    await message.answer_sticker(kira)
    await message.answer(text)
