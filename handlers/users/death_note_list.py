from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db_note


@dp.message_handler(Command("death_list"))
async def show_death_note(message: types.Message):
    death_list = []
    user_id = message.from_user.id
    victims = await db_note.select_victims(id_user=user_id)
    for victim in victims:
        tags = str(victim).find("'")
        death_list.append(str(victim)[tags:].replace(">", ''))
    death_list = '\n\n'.join(death_list)
    await message.answer(text=f'🍎 Your Death Note :  \n\n'
                              f'{death_list}')



