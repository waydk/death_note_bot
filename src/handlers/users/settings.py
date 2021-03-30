from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from src.keyboards.inline.language_keyboard import languages_markup
from src.keyboards.inline.settings_keyboard import settings_callback, settings_markup
from loader import _
from loader import dp
from src.utils.db_api import db_helpers


@dp.message_handler(Command("settings"), state='*')
async def open_settings(message: types.Message):
    await message.delete()
    await message.answer(_("Settings"), reply_markup=settings_markup)


@dp.callback_query_handler(settings_callback.filter(title="change_lang"), state='*')
async def change_language(call: CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.answer(_("Select a language "), reply_markup=languages_markup)
    await call.message.delete()


@dp.callback_query_handler(text_contains="lang", state='*')
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    lang = call.data[-2:]
    await db_helpers.set_language(lang)
    await call.message.answer(_("Your language has been changed", locale=lang))
