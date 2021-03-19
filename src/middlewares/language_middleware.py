from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from src.data.config import I18N_DOMAIN, LOCALES_DIR
from src.utils.db_api import db_helpers


async def get_lang(user_id):
    user = await db_helpers.get_user(user_id)
    if user:
        return user.language


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action, args):
        user = types.User.get_current()
        return await get_lang(user.id) or user.locale


def setup_middleware(dp):
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n

