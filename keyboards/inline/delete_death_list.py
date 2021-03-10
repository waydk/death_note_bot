from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import delete_victims_call

delete_victims_keyboard = InlineKeyboardMarkup()
delete_victims_button = InlineKeyboardButton(text='Clear', callback_data=delete_victims_call.new("delete"))
delete_victims_keyboard.insert(delete_victims_button)

agreement_keyboard = InlineKeyboardMarkup()
yes_button = InlineKeyboardButton("Yes", callback_data=delete_victims_call.new('yes'))
no_button = InlineKeyboardButton("No", callback_data=delete_victims_call.new('no'))
agreement_keyboard.insert(yes_button)
agreement_keyboard.insert(no_button)
