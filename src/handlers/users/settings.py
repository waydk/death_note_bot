from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from loader import _
from loader import dp
from src.keyboards.inline.close_keyboard import close_markup
from src.keyboards.inline.language_keyboard import languages_markup
from src.keyboards.inline.settings_keyboard import settings_callback, settings_markup
from src.utils.db_api import db_helpers


@dp.message_handler(Command("settings"), state='*')
async def open_settings(message: types.Message):
    await message.delete()
    await message.answer(_("⚙ Welcome to settings, here you can"
                           " change your language!\n"
                           "🇷🇺 or 🇺🇸 Click the button below"),
                         reply_markup=settings_markup)


@dp.callback_query_handler(settings_callback.filter(title="change_lang"), state='*')
async def change_language(call: CallbackQuery):
    await call.message.delete()
    await call.answer(cache_time=1)
    await call.message.answer(_("Select a language "), reply_markup=languages_markup)


@dp.callback_query_handler(text_contains="lang", state='*')
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    lang = call.data[-2:]
    await db_helpers.set_language(lang)
    await call.message.answer(_("Your language has been changed", locale=lang), reply_markup=close_markup)
