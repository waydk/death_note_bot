from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, _
from src.keyboards.inline.close_keyboard import close_markup
from src.utils.db_api import db_helpers


@dp.message_handler(Command("write"), state="*")
async def write_in_death_note(message: types.Message):
    """A simplified /write_down function that allows you to write
    the victim to the database"""
    await message.delete()
    victim = message.text
    victim = victim.split(" ")
    user_id, victim_id = message.from_user.id, message.message_id
    try:
        name_victim = victim[1] + ' ' + victim[2]
        reason = victim[3]
        await db_helpers.add_victim(id_user=user_id, id_victim=victim_id, name_victim=name_victim, reason=reason)
        apples = await db_helpers.add_apples(user_id=message.from_user.id,
                                             apples=10)
        text = _("📓 {} was added to the death note\n ☠ his cause of death: {}\n"
                 "  Check death note: /death_list").format(name_victim, reason)
        apples_info = _("Congratulations 🎉!\nYou got 10 apples 🍎 \n"
                        "Your number of apples: {} 🍎").format(apples)
        await message.answer(text)
        await message.answer(apples_info, reply_markup=close_markup)
    except IndexError:
        text = _("(」°ロ°)」 Incorrect input\n"
                 "\n"
                 "📌 Example: /write Yagami Light Upal\n"
                 "📌 Only three words after /write")
        await message.answer(text, reply_markup=close_markup)
