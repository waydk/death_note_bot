from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import _
from src.keyboards.inline.callback_datas import close_callback

settings_callback = CallbackData("settings", "title")
text = _("Settings")
settings_markup = InlineKeyboardMarkup(row_width=1)
settings_button = InlineKeyboardButton(text=text, callback_data=settings_callback.new("change_lang"))
close_button = InlineKeyboardButton(text="❌", callback_data=close_callback.new("close"))
settings_markup.insert(settings_button)
settings_markup.insert(close_button)
