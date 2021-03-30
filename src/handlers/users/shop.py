import random

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from loader import dp, _
from src.keyboards.inline.callback_datas import shop_call, close_callback
from src.keyboards.inline.close_keyboard import close_markup, close_markup_shop
from src.keyboards.inline.shop_keyboard import shop_markup
from src.middlewares.language_middleware import get_lang
from src.shop_module.characters import characters_en, characters_ru
from src.shop_module.death_note_pics import pictures
from src.shop_module.quotes import quotes
from src.shop_module.quotes_ru import quotes_ru
from src.utils.db_api import db_helpers


@dp.message_handler(Command("shop"))
async def show_shop(message: types.Message):
    user_id = message.from_user.id
    apples = await db_helpers.add_apples(user_id=user_id, apples=0)
    text = _("Welcome to the store 🏪\n\n"
             "Your number of apples: {} 🍎\n"
             "Replenish apples : "
             "/write or /write_down \n\n"
             "By clicking the button below, you can purchase 🛍\n"
             "Enjoy your time 😌").format(apples)
    await message.answer(text, reply_markup=shop_markup)


@dp.callback_query_handler(shop_call.filter(name="quote"), state='*')
async def buy_quote(call: CallbackQuery):
    await call.answer(cache_time=1)
    user_id = call.from_user.id
    apples = await db_helpers.add_apples(user_id=user_id, apples=0)
    if apples < 5:
        await call.message.answer(_("You don't have enough apples 🍎\n"
                                    "Replenish apples : "
                                    "/write or /write_down"), reply_markup=close_markup_shop)
    else:
        apples = await db_helpers.add_apples(user_id=user_id, apples=-5)
        if await get_lang(call.from_user.id) == "ru":
            text = _("{}\n\n Your apples: {} 🍎").format(random.choice(quotes_ru), apples)
            await call.message.answer(text, reply_markup=close_markup_shop)
        else:
            text = _("{}\n\n Your apples: {} 🍎").format(random.choice(quotes), apples)
            await call.message.answer(text, reply_markup=close_markup_shop)


@dp.callback_query_handler(shop_call.filter(name="picture"), state='*')
async def buy_picture(call: CallbackQuery):
    await call.answer(cache_time=1)
    user_id = call.from_user.id
    apples = await db_helpers.add_apples(user_id=user_id, apples=0)
    if apples < 20:
        await call.message.answer(_("You don't have enough apples 🍎\n"
                                    "Replenish apples : "
                                    "/write or /write_down"), reply_markup=close_markup)
    else:
        apples = await db_helpers.add_apples(user_id=user_id, apples=-20)
        text = _("Your apples: {} 🍎").format(apples)
        await call.message.answer_photo(caption=text, photo=random.choice(pictures),
                                        reply_markup=close_markup_shop)


@dp.callback_query_handler(shop_call.filter(name="character"), state='*')
async def buy_info_character(call: CallbackQuery):
    await call.answer(cache_time=1)
    user_id = call.from_user.id
    apples = await db_helpers.add_apples(user_id=user_id, apples=0)
    if apples < 30:
        await call.message.answer(_("You don't have enough apples 🍎\n"
                                    "Replenish apples : "
                                    "/write or /write_down"), reply_markup=close_markup_shop)
    else:
        apples = await db_helpers.add_apples(user_id=user_id, apples=-30)
        if await get_lang(call.from_user.id) == "ru":
            text = _("You seem to be today: {}\n\n"
                     "Your apples: {} 🍎").format(random.choice(characters_ru), apples)
            await call.message.answer(text, reply_markup=close_markup_shop)
        else:
            text = _("You seem to be today: {}\n\n"
                     "Your apples: {} 🍎").format(random.choice(characters_en), apples)
            await call.message.answer(text, reply_markup=close_markup_shop)


@dp.callback_query_handler(close_callback.filter(name='close_shop'), state='*')
async def close(call: CallbackQuery):
    await call.message.delete()
