from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from keyboards.inline.delete_death_list import delete_victims_keyboard, agreement_keyboard

from keyboards.inline.callback_datas import delete_victims_call
from loader import dp, db_note
from stickers.dn_stickers import death_list


async def parse_db_victims(victims):
    death_note_list = []
    for victim in victims:
        tags = str(victim).find("'")
        new_victim = (str(victim)[tags:].replace(">", ''))
        new_victim = new_victim.replace("'", "")
        death_note_list.append(new_victim.replace('reason=', ' | reason:  '))
    return '\n'.join(death_note_list)


@dp.message_handler(Command("death_list"))
async def show_death_note(message: types.Message):
    user_id = message.from_user.id
    victims = await db_note.select_victims(id_user=user_id)
    await message.answer_sticker(death_list)
    await message.answer(text=f'Write more /write_down✒\n\n '
                              f'🍎 Your Death Note : \n'
                              f'---------------------------------------\n'
                              f'{await parse_db_victims(victims)}', reply_markup=delete_victims_keyboard)


@dp.callback_query_handler(delete_victims_call.filter(name="delete"))
async def agree_victims(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text(text='Are you sure? The whole list will be cleared! ', reply_markup=agreement_keyboard)


@dp.callback_query_handler(delete_victims_call.filter(name='yes'))
async def delete_victims(call: CallbackQuery):
    user_id = call.from_user.id
    await call.answer(cache_time=1)
    await db_note.delete_victims(id_user=user_id)
    await call.message.edit_text(text=f'Write more /write_down✒\n\n '
                                      f'🍎 Your Death Note : \n'
                                      f'---------------------------------------\n'
                                      f'', reply_markup=delete_victims_keyboard)


@dp.callback_query_handler(delete_victims_call.filter(name='no'))
async def delete_victims(call: CallbackQuery):
    user_id = call.from_user.id
    await call.answer(cache_time=1)
    victims = await db_note.select_victims(id_user=user_id)
    await call.message.edit_text(text=f'Write more /write_down✒\n\n '
                                      f'🍎 Your Death Note : \n'
                                      f'---------------------------------------\n'
                                      f'{await parse_db_victims(victims)}', reply_markup=delete_victims_keyboard)
