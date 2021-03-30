from aiogram import types
from asyncpg import UniqueViolationError

from src.utils.db_api.db_gino import db
from src.utils.db_api.schemas.user import User
from src.utils.db_api.schemas.victim import Victim
import operator


async def get_user(user_id):
    user = await User.query.where(User.id == user_id).gino.first()
    return user


async def add_user(id_user: int, name: str, apples: int):
    try:
        user = User(id=id_user, name=name, apples=apples)
        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id_user: int):
    user = await User.query.where(User.id == id_user).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def set_language(language):
    user_id = types.User.get_current().id
    user = await get_user(user_id)
    await user.update(language=language).apply()


async def add_victim(id_user: int, id_victim: int, name_victim: str, reason: str = "Heart Attack"):
    try:
        victim = Victim(id_user=id_user, id_victim=id_victim, name=name_victim, reason=reason)
        await victim.create()

    except UniqueViolationError:
        pass


async def select_all_victims(user_id):
    victims = await Victim.query.where(Victim.id_user == user_id).gino.all()
    return victims


async def delete_victims(user_id):
    await Victim.delete.where(Victim.id_user == user_id).gino.all()


async def add_apples(user_id, apples):
    user = await User.query.where(User.id == user_id).gino.first()
    await user.update(apples=user.apples + apples).apply()
    return user.apples


async def get_top_users():
    users = await User.query.gino.all()
    users_names_apples = {}
    for user in users:
        users_names_apples[f"{user.name}"] = user.apples
    top_users = sorted(users_names_apples.items(), key=operator.itemgetter(1), reverse=True)
    return top_users
