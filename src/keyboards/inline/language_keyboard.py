from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

languages_markup = InlineKeyboardMarkup()
ru_button = InlineKeyboardButton(text="Русский", callback_data="lang_ru")
en_button = InlineKeyboardButton(text="English", callback_data="lang_en")
languages_markup.insert(ru_button)
languages_markup.insert(en_button)
