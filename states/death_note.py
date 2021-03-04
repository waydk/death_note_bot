from aiogram.dispatcher.filters.state import StatesGroup, State


class DeathNote(StatesGroup):
    surname_first_name = State()
    cause_of_death = State()