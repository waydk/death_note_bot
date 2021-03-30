from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from loader import dp
from src.data.content import rules_ru, max_pages_rules_ru, rules_en, max_pages_rules_en
from src.keyboards.inline.callback_datas import close_callback
from src.keyboards.inline.pagination import get_page_keyboard, pagination_call
from src.middlewares.language_middleware import get_lang
from src.utils.pages import get_page


@dp.message_handler(Command("rules"), state='*')
async def show_rules(message: types.Message):
    """The function takes the first page"""
    if await get_lang(message.from_user.id) == "ru":
        text = get_page(rules_ru)
        await message.answer(text,
                             reply_markup=get_page_keyboard(max_pages=max_pages_rules_ru))
    else:
        text = get_page(rules_en)
        await message.answer(text,
                             reply_markup=get_page_keyboard(max_pages=max_pages_rules_en))


@dp.callback_query_handler(pagination_call.filter(page="current_page"), state='*')
async def current_page_error(call: CallbackQuery):
    """The function handles clicking on the current page"""
    await call.answer(cache_time=60)


@dp.callback_query_handler(pagination_call.filter(key="rules"), state='*')
async def show_chosen_page(call: CallbackQuery, callback_data: dict):
    """The function gets the page number and returns the text"""
    current_page = int(callback_data.get("page"))
    if await get_lang(call.from_user.id) == "ru":
        text = get_page(rules_ru, page=current_page)
        markup = get_page_keyboard(max_pages=max_pages_rules_ru, page=current_page)
        await call.message.edit_text(text=text, reply_markup=markup)
    else:
        text = get_page(rules_en, page=current_page)
        markup = get_page_keyboard(max_pages=max_pages_rules_en, page=current_page)
        await call.message.edit_text(text=text, reply_markup=markup)


@dp.callback_query_handler(close_callback.filter(name='close'), state='*')
async def close(call: CallbackQuery):
    await call.message.delete()
