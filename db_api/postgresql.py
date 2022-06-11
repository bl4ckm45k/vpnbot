import logging
from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from config import load_config

logger = logging.getLogger(__name__)
c = load_config(".env")


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def execute(self, command, *args, fetch: bool = False, fetchval: bool = False, fetchrow: bool = False,
                      execute: bool = False):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(user=c.db.user,
                                                  password=c.db.password,
                                                  host=c.db.host,
                                                  database=c.db.database,
                                                  port=c.db.port
                                                  )
            logger.info(f'Создано подключение к БД')
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
                return result

    async def add_tg_user(self, user_id):
        sql = "INSERT INTO tg_users (user_id) VALUES ($1) ON CONFLICT ON CONSTRAINT tg_users_user_id_key DO NOTHING"
        return await self.execute(sql, user_id, execute=True)

    async def select_active(self, user_id):
        sql = "SELECT active FROM tg_users WHERE user_id=$1"
        return await self.execute(sql, user_id, fetchval=True)

    async def get_key_id(self, user_id):
        sql = "SELECT key_id FROM tg_users WHERE user_id =$1"
        return await self.execute(sql, user_id, fetchval=True)

    async def update_key(self, user_id, key_id):
        sql = "UPDATE tg_users SET active=$3, key_id=$2 WHERE user_id=$1"
        return await self.execute(sql, user_id, key_id, True, execute=True)

    async def delete_key(self, user_id):
        sql = "UPDATE tg_users SET active=$2, key_id=NULL WHERE user_id=$1"
        return await self.execute(sql, user_id, False, execute=True)
