from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import _

settings_callback = CallbackData("settings", "title")
text = _("Settings")
settings_markup = InlineKeyboardMarkup()
settings_button = InlineKeyboardButton(text=text, callback_data=settings_callback.new("change_lang"))
settings_markup.insert(settings_button)
