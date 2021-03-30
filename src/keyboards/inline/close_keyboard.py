from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.keyboards.inline.callback_datas import close_callback

close_markup = InlineKeyboardMarkup()
close_button = InlineKeyboardButton(text="❌", callback_data=close_callback.new("close"))
close_markup.insert(close_button)