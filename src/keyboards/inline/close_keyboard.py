from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.keyboards.inline.callback_datas import close_callback

close_markup = InlineKeyboardMarkup()
close_button = InlineKeyboardButton(text="❌", callback_data=close_callback.new("close"))
close_markup.insert(close_button)

close_markup_shop = InlineKeyboardMarkup()
close_button_shop = InlineKeyboardButton(text="❌", callback_data=close_callback.new("close_shop"))
close_markup_shop.insert(close_button_shop)
