from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, _
from src.utils.db_api import db_helpers


@dp.message_handler(Command("write"), state="*")
async def write_in_death_note(message: types.Message):
    """A simplified /write_down function that allows you to write
    the victim to the database"""
    victim = message.text
    victim = victim.split(" ")
    user_id, victim_id = message.from_user.id, message.message_id
    try:
        name_victim = victim[1] + ' ' + victim[2]
        reason = victim[3]
        await db_helpers.add_victim(id_user=user_id, id_victim=victim_id, name_victim=name_victim, reason=reason)
        text = _("📓 {} was added to the death note, ☠ his cause of death: {}  "
                 "/death_list").format(name_victim, reason)
        await message.answer(text)
    except IndexError:
        text = _("(」°ロ°)」 Incorrect input\n"
                 "\n"
                 "📌 Example: /write Yagami Light Upal\n"
                 "📌 Only three words after /write")
        await message.answer(text)
