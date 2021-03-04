from typing import Union

import asyncpg
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        pool = await asyncpg.create_pool(
            user=config.PGUSER,
            password=config.PGPASSWORD,
            host=config.IP,
            database='postgres'
        )
        self.pool = pool

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id INT NOT NULL,
            Name varchar(255) NOT NULL,
            PRIMARY KEY (id)
            );
"""
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num + 1}" for num, item in enumerate(parameters)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, id: int, name: str):
        sql = """
        INSERT INTO Users(id, Name) VALUES($1, $2)
        """
        await self.pool.execute(sql, id, name)

    async def count_users(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM Users")


class DatabaseNote:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        pool = await asyncpg.create_pool(
            user=config.PGUSER,
            password=config.PGPASSWORD,
            host=config.IP,
            database='postgres'
        )
        self.pool = pool

    async def create_table_note(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Notes (
            id_user INT NOT NULL,
            id_victim INT NOT NULL,
            Name_Victim varchar(255) NOT NULL,
            reason varchar(255),
            PRIMARY KEY (id_victim)
            );
"""
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num + 1}" for num, item in enumerate(parameters)
        ])
        return sql, tuple(parameters.values())

    async def add_victim(self, id_user: int, id_victim: int, name_victim: str, reason: str = "Heart Attack"):
        sql = """
            INSERT INTO Notes(id_user, id_victim, Name_Victim, reason) VALUES($1, $2, $3, $4)
            """
        await self.pool.execute(sql, id_user, id_victim, name_victim, reason)

    async def select_victims(self, **kwargs):
        sql = f"""
            SELECT * FROM Notes WHERE 
            """
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.pool.fetch(sql, *parameters)

    async def count_victims(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM Notes")
