from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from stickers.dn_stickers import kira


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    text = ("available commands: ",
            "/start - start a conversation",
            "/help - get info",
            "/rules - rules for the use of the death note"
            "/write_down - write in the death note\n"
            "/death_list - show victim list ")

    await message.answer_sticker(kira)
    await message.answer("\n".join(text))
