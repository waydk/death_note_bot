from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api import db_helpers


@dp.message_handler(Command("write"))
async def write_in_death_note(message: types.Message):
    """A simplified /write_down function that allows you to write
    the victim to the database"""
    name_victim = None
    reason = None
    victim = message.text
    victim = victim.split(" ")
    user_id, victim_id = message.from_user.id, message.message_id
    try:
        name_victim = victim[1] + ' ' + victim[2]
        reason = victim[3]
    except IndexError:
        await message.answer("Incorrect input")
    try:
        await db_helpers.add_victim(id_user=user_id, id_victim=victim_id, name_victim=name_victim, reason=reason)
        await message.answer(f"📓 {name_victim} was added to the death note, ☠ his cause of death: {reason}  "
                             f"/death_list")
    except UnboundLocalError:
        pass
