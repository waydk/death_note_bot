from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import CallbackQuery

from loader import dp, _, bot
from src.keyboards.inline.callback_datas import close_callback
from src.keyboards.inline.close_keyboard import close_markup
from src.stickers.dn_stickers import kira


@dp.message_handler(CommandHelp(), state='*')
async def show_help_info(message: types.Message):
    await message.delete()
    text = _("available commands:\n"
             "/start - start a conversation\n"
             "/help - get info\n"
             "/rules - rules for the use of the death note\n"
             "/write_down - write in the death note\n"
             "/write (example: yagami light heart_attack) \n"
             "/death_list - show victim list\n"
             "/shop - buy something\n"
             "/top - top users by number of apples\n")
    await message.answer_sticker(kira)
    await message.answer(text, reply_markup=close_markup)


@dp.callback_query_handler(close_callback.filter(name='close'), state='*')
async def close(call: CallbackQuery):
    await call.message.delete()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id - 1)
