from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import delete_victims_call
from keyboards.inline.delete_death_list import delete_victims_keyboard, agreement_keyboard
from loader import dp
from utils.db_api import db_helpers


async def retrieved(victims):
    text = "reason"
    victims_list = []
    for victim in victims:
        victims_list.append(f"📓 {victim.name}: {text} {victim.reason}")
    victims = '\n'.join(victims_list)
    return victims


@dp.message_handler(Command("death_list"), state='*')
async def show_death_note(message: types.Message):
    user_id = message.from_user.id
    victims = await db_helpers.select_all_victims(user_id=user_id)
    await message.answer(text=f'Write more /write_down✒\n\n '
                              f'🍎 Your Death Note : \n'
                              f'---------------------------------------\n'
                              f'{await retrieved(victims)}', reply_markup=delete_victims_keyboard)


@dp.callback_query_handler(delete_victims_call.filter(name="delete"), state='*')
async def agree_victims(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(text='Are you sure? The whole list will be cleared! ', reply_markup=agreement_keyboard)


@dp.callback_query_handler(delete_victims_call.filter(name='yes'), state='*')
async def delete_victims(call: CallbackQuery):
    user_id = call.from_user.id
    await call.answer(cache_time=1)
    await db_helpers.delete_victims(user_id=user_id)
    await call.message.edit_text(text=f'Write more /write_down✒\n\n '
                                      f'🍎 Your Death Note : \n'
                                      f'---------------------------------------\n'
                                      f'', reply_markup=delete_victims_keyboard)


@dp.callback_query_handler(delete_victims_call.filter(name='no'), state='*')
async def delete_victims(call: CallbackQuery):
    await call.answer(cache_time=1)
    user_id = call.from_user.id
    victims = await db_helpers.select_all_victims(user_id=user_id)
    await call.message.edit_text(text=f'Write more /write_down✒\n\n '
                                      f'🍎 Your Death Note : \n'
                                      f'---------------------------------------\n'
                                      f'{await retrieved(victims)}', reply_markup=delete_victims_keyboard)
