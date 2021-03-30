from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from src.keyboards.inline.callback_datas import delete_victims_call
from src.keyboards.inline.delete_death_list import delete_victims_keyboard, agreement_keyboard
from loader import dp, _
from src.utils.db_api import db_helpers


async def make_readable(victims):
    """The function creates a list with victims in readable form and returns the strings"""
    text = _("reason")
    victims_list = []
    for victim in victims:
        victims_list.append(f"📓 {victim.name}: {text} {victim.reason}")
    victims = '\n'.join(victims_list)
    return victims


@dp.message_handler(Command("death_list"), state='*')
async def show_death_note(message: types.Message):
    """The function takes the list of victims from the database and replies to the user"""
    user_id = message.from_user.id
    victims = await db_helpers.select_all_victims(user_id=user_id)
    text = _('Write more /write_down✒\n\n '
             '🍎 Your Death Note : \n'
             '---------------------------------------\n'
             '{}').format(await make_readable(victims))

    await message.answer(text=text, reply_markup=delete_victims_keyboard)


@dp.callback_query_handler(delete_victims_call.filter(name="delete"), state='*')
async def agreement_clear(call: CallbackQuery):
    await call.answer(cache_time=1)
    text = _('Are you sure? The whole list will be cleared! ')
    await call.message.edit_text(text=text, reply_markup=agreement_keyboard)


@dp.callback_query_handler(delete_victims_call.filter(name='yes'), state='*')
async def delete_victims(call: CallbackQuery):
    """The function deletes the user's victims from the database"""
    user_id = call.from_user.id
    await call.answer(cache_time=1)
    await db_helpers.delete_victims(user_id=user_id)
    text = _('Write more /write_down✒\n\n '
             '🍎 Your Death Note : \n'
             '---------------------------------------\n')
    await call.message.edit_text(text=text, reply_markup=delete_victims_keyboard)


@dp.callback_query_handler(delete_victims_call.filter(name='no'), state='*')
async def not_delete_victims(call: CallbackQuery):
    await call.answer(cache_time=1)
    user_id = call.from_user.id
    victims = await db_helpers.select_all_victims(user_id=user_id)
    text = _('Write more /write_down✒\n\n '
             '🍎 Your Death Note : \n'
             '---------------------------------------\n'
             '{}').format(await make_readable(victims))
    await call.message.edit_text(text=text, reply_markup=delete_victims_keyboard)

