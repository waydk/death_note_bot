from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.keyboards.inline.callback_datas import delete_victims_call, close_callback

close_button = InlineKeyboardButton(text="❌", callback_data=close_callback.new("close"))
delete_victims_keyboard = InlineKeyboardMarkup(row_width=1)
delete_victims_button = InlineKeyboardButton(text='Clear', callback_data=delete_victims_call.new("delete"))
delete_victims_keyboard.insert(delete_victims_button)
delete_victims_keyboard.insert(close_button)


agreement_keyboard = InlineKeyboardMarkup(row_width=2)
yes_button = InlineKeyboardButton("Yes", callback_data=delete_victims_call.new('yes'))
no_button = InlineKeyboardButton("No", callback_data=delete_victims_call.new('no'))
agreement_keyboard.insert(yes_button)
agreement_keyboard.insert(no_button)
agreement_keyboard.insert(close_button)
