from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db_note
from states.death_note import DeathNote
from stickers.dn_stickers import ryuk_write_down, death_note_sticker


@dp.message_handler(Command("write_down"))
async def write_in_death_note(message: types.Message):
    await message.answer("📓 You dared to use the death note, a brave thing to do! Good luck!")
    await message.answer_sticker(death_note_sticker)
    await message.answer("Enter the victim's surname and first name \n\n"
                         "             -- example: Yagami Light --")
    await DeathNote.surname_first_name.set()


@dp.message_handler(state=DeathNote.surname_first_name)
async def write_surname_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    surname_first_name = message.text
    victim_id = message.message_id
    await state.update_data(surname_first_name=surname_first_name,
                            user_id=user_id, victim_id=victim_id)
    await message.answer_sticker(ryuk_write_down)
    await message.answer("Write the cause of death, if no cause is given, "
                         "it will be a heart attack, for that write None!")
    await DeathNote.next()


@dp.message_handler(state=DeathNote.cause_of_death)
async def write_cause(message: types.Message, state: FSMContext):
    cause_of_death = message.text
    if cause_of_death == "None" or cause_of_death == "none":
        cause_of_death = "Heart attack"
    await state.update_data(cause_of_death=cause_of_death)
    data = await state.get_data()

    surname_first_name = data.get("surname_first_name")
    cause_of_death = data.get("cause_of_death")
    user_id = data.get("user_id")
    victim_id = data.get("victim_id")

    await db_note.add_victim(id_user=user_id, id_victim=victim_id, name_victim=surname_first_name,reason=cause_of_death)

    await message.answer(f"✒ {surname_first_name} was added to the death note with the cause of "
                         f"{cause_of_death} 🍎 \n\n"
                         f"In order to see the entire list of the death note: /death_list ")
    await state.finish()
