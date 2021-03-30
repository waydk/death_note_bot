from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.keyboards.inline.callback_datas import shop_call, close_callback

shop_markup = InlineKeyboardMarkup(row_width=1)
random_quote = InlineKeyboardButton(text="Random quote 5 🍎", callback_data=shop_call.new("quote"))
random_picture = InlineKeyboardButton(text="Random picture 20 🍎", callback_data=shop_call.new("picture"))
random_character = InlineKeyboardButton(text="Which character are you? 30 🍎", callback_data=shop_call.new("character"))
close_button = InlineKeyboardButton(text="❌", callback_data=close_callback.new("close"))
shop_markup.insert(random_quote)
shop_markup.insert(random_picture)
shop_markup.insert(random_character)
shop_markup.insert(close_button)

