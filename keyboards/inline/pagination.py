from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import close_callback, pagination_call


def get_page_keyboard(max_pages: int, key="rules", page: int = 1):
    previous_page = page - 1
    previous_page_text = "<< "

    current_page_text = f" 📓 {page}  "

    next_page = page + 1
    next_page_text = ">> "

    markup = InlineKeyboardMarkup(row_width=3)

    if previous_page > 0:
        markup.insert(
            InlineKeyboardButton(text=previous_page_text,
                                 callback_data=pagination_call.new(key=key, page=previous_page))
        )

    markup.insert(
        InlineKeyboardButton(
            text=current_page_text,
            callback_data=pagination_call.new(key=key, page="current_page")
        )
    )

    if next_page <= max_pages:
        markup.insert(
            InlineKeyboardButton(
                text=next_page_text,
                callback_data=pagination_call.new(key=key, page=next_page)
            )
        )

    close_button = InlineKeyboardButton(text="❌", callback_data=close_callback.new("close"))
    markup.insert(close_button)

    return markup
